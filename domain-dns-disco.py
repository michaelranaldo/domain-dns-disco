#!python3

import dns.resolver, argparse, os.path

parser = argparse.ArgumentParser(description="")
parser.add_argument("domain", help="The domain to request")
parser.add_argument("outfile", help="[Optional]: an output file location", nargs="?")
args = parser.parse_args()

if args.outfile is not None:
    if os.path.exists(args.outfile):
        print("Output file already exists")
        print("Quitting...")
        quit()

dns_records = ["_ldap._tcp", "_gc._tcp", "_kerberos._tcp", "_kpasswd._tcp"]
hosts = []

for dns_record in dns_records:
    print()
    print("Locating " + dns_record + "." + args.domain)
    print()
    try:
        dns_response = dns.resolver.query(dns_record + "." + args.domain, "SRV").response
        if len(dns_response.answer) > 0:
            for host in dns_response.answer[0]:
                neathost = str(host.target).rstrip(".")
                print(neathost.lower())
                hosts.append(neathost.lower())
        else:
            raise Exception
    except:
        print("No results for " + dns_record + "." + args.domain)

    if args.outfile is not None:
        f = open(args.outfile, "a")

        unique_hosts = []
        for host in hosts:
            if host not in unique_hosts:
                f.write(host + "\n")
                unique_hosts.append(host)
        f.close()

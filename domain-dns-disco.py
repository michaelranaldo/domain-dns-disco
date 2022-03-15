#!python3

import dns.resolver, argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("domain", help="The domain to request")
args = parser.parse_args()



dns_records = ["_ldap._tcp", "_gc._tcp", "_kerberos._tcp", "_kpasswd._tcp"]

for dns_record in dns_records:
    print()
    print("Locating " + dns_record + "." + args.domain)
    print()
    try:
        dns_response = dns.resolver.query(dns_record + "." + args.domain, "SRV").response
        if len(dns_response.answer) > 0:
            for host in dns_response.answer[0]:
                print(host.target)
        else:
            raise Exception
    except:
        print("No results for " + dns_record + "." + args.domain)

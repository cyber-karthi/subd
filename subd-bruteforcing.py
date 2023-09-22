import dns.resolver

domain = input("Enter domain:")
wordlist = "/home/cyber_karthi/New/subdomain.txt"

resolver = dns.resolver.Resolver()

try:
    with open(wordlist, 'r') as file:
        subdomains = file.read().splitlines()
except FileNotFoundError:
    print(f"Wordlist file '{wordlist}' not found.")

for subdomain in subdomains:
    full_domain = f"{subdomain}.{domain}"

    try:
        answers = resolver.resolve(full_domain)
        for rdata in answers:
            print(f"Subdomain found: {full_domain} -> IP: {rdata.address}")
    except dns.resolver.NXDOMAIN:
        pass
    except Exception as e:
        print(f"Error for {full_domain}")

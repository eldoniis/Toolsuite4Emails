import whois
import dns.resolver
import validators

#domain = "google.com"

def perform_whois(domain):
    if validators.domain(domain):
        return whois.whois(domain)
    else:
        return "Error while parsing domain"

def perform_dns_query(domain):
    if validators.domain(domain):
        dns_results = {}
        DNS_RECORDS = ["A", "AAAA", "CNAME", "MX",
                    "TXT", "NS", "SOA", "SRV", "PTR"]
        resolver = dns.resolver.Resolver()
        for RECORD in DNS_RECORDS:
            try:
                query_result = resolver.resolve(domain, RECORD)
            except dns.resolver.NoAnswer:
                dns_results[RECORD] = "Empty record"
                continue
            dns_results[RECORD] = [str(rdata) for rdata in query_result]
        return dns_results
    else:
        return "Error while parsing domain"

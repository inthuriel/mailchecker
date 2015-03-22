# -*- coding: utf-8 -*-
import dns.resolver
from tech import getdomain
from re import sub
from collections import defaultdict

def getmx(mail):

    domain = getdomain(mail)
    try:
        mxes = dns.resolver.query(domain,'MX')
    except dns.exception.DNSException as e:
        if isinstance(e, dns.resolver.NoAnswer):
            raise Exception("noMx", "Can't get MX from DNS server.")
        elif isinstance(e, dns.resolver.Timeout):
            raise Exception("timeoutDNS", "DNS Timeout.")
        else:
            raise Exception("unknownDns", "Unknown DNS exception.")

    servers = defaultdict(list)

    for server in mxes:
        serverData = str(server).split(' ')
        serverAdress = sub('\.$', '', serverData[1])
        servers[int(serverData[0])].append(serverAdress)

    return sorted(servers.iteritems(), key=lambda k: k[1])

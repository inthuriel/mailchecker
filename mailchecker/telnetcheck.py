# -*- coding: utf-8 -*-
import telnetlib
import re
from mx import getmx
from tech import getdomain
from ports import getcontypes

def correctcheckmail(mail, authmail):

    mxes = getmx(mail)
    primarymx = None
    ports = None

    breaker = False
    for k,v in mxes:
        for value in v:
            try:
                ports = getcontypes(value)
            except Exception as e:
                response = e[0]

            if ports is not None:
                primarymx = value
                breaker = True
                break
        if breaker:
            break

    authdomain = getdomain(authmail)

    try:
        tn = telnetlib.Telnet(primarymx, 25)
        tn.read_until('^220', 35)
        tn.read_until('^\r\n', 5)
    except tn.timeout:
        raise Exception("telConErr", "Can't connect to host.")

    try:
        tn.write("HELO "+authdomain+"\r\n")
        tn.read_until('^\r\n', 5)
    except EOFError:
        raise Exception("heloErr", "Can't send HELO.")

    try:
        tn.write("mail from:<"+authmail+">\r\n")
        tn.read_until('^\r\n', 5)
    except EOFError:
        raise Exception("mailFromErr", "Can't send mail from.")


    try:
        tn.write("rcpt to:<"+mail+">\r\n")
        existenceresponse = tn.read_until('^\r\n', 10)
        existenceresponse = re.sub('\r\n', '', existenceresponse)
    except EOFError:
        raise Exception("rcptErr", "Can't send rcpt to.")

    test = re.compile('^250.*')

    if (test.match(existenceresponse.lower())):
        resp = [1, existenceresponse]
    else:
        resp = [0, existenceresponse]

    return resp


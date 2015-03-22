# -*- coding: utf-8 -*-
from telnetcheck import correctcheckmail
from ports import getcontypes
from mx import getmx
from mx import getdomain

def checkmail(mail, authMail):

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

    dataset = {}

    dataset['mail'] = mail
    dataset['domain'] = getdomain(mail)
    dataset['mx'] = mxes
    dataset['ports'] = ports
    dataset['correct'] = correctcheckmail(mail, authMail)

    return dataset






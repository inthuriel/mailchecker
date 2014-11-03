Mailchecker library
===========

*Python library provides email checking feature based on telnet*


**Basic methods**

- check MX records
```
from mailchecker import getmx
 
print getmx(mail)
```

- check open ports of MX server
```
" " "
  checked ports: 25, 465, 143, 993
" " "
from mailchecker import getcontypes
 
print getcontypes(mx)
```

- check if email is correct
```
from mailchecker import correctcheckmail
 
print correctcheckmail(mailToCheck, mailToVerify)
```

- complex mail check
```
from mailchecker import checkmail
 
print checkmail(mailToCheck, mailToVerify)

```

*Distributed under **Apache License**.*


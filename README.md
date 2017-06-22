## Mailchecker library

*Python* library provides email checking features based on *telnet* methods


### Provided methods

- check MX records
```python
from mailchecker import get_mx

mail = 'sample@example.com'
print get_mx(mail)
```

- check open ports of MX server
```python
from mailchecker import get_open_email_ports
# default checked ports: 25, 465, 143, 993

mail = 'sample@example.com'
print get_open_email_ports(mail)
```

- check if email is correct
```python
from mailchecker import check_if_mail_is_correct

mail_to_check = 'sample@example.com'
my_reference_email = 'reference@example.com'
print check_if_mail_is_correct(mail_to_check, my_reference_email)
```

- complex mail check
```python
from mailchecker import full_email_check
 
mail_to_check = 'sample@example.com'
my_reference_email = 'reference@example.com'
print full_email_check(mail_to_check, my_reference_email)
```

### Installation
```bash
git clone https://github.com/inthuriel/mailchecker.git
pip install -e ./mailchecker
```

### Licence

*Distributed under GNU Library or Lesser General Public License (LGPL).*


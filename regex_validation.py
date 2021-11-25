import re

email = ['wesley.fcb@hotmail.com.br',
        'joker@gmail.com',
        '123',
        'ABC@Gmail.com.br',
        '33.fcb@kalr.com.br']

dates = ['Jan 01','feb 28','Mar 08','APR 30','May 04','jul 07']


# Mounths validation with regex
print('\n---------------- Mounths Validation With Regex ---------\n')
regex = re.compile('^[A-Z]\w+ \d+')
for month in dates:
    result = regex.match(month)
    if result is not None:
        print(result.group(0))


# Email validation with regex
print('\n---------------- Email Validation With Regex ---------\n')
regex = re.compile('^([a-zA-Z][\.\-\_]*)+@[a-zA-Z]+(\.com|\.com\.br)$')
for x in email:
    result = regex.match(x)
    if result is not None:
        print(result.group(0))


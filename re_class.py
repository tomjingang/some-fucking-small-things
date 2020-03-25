import re

a = ' accbccdcceccasdfjakfljlayxccc'

def convert(value):

    convert = value.group()

    return '!!' + convert + '!!'

p = re.sub('cc', convert, a, 0)

q = re.search('accb', a, 0)

print(p)

print(q)

r = re.

print(r)
import re

a = 'abc, acc, acd, ace, adc, aec, afc'

r = re.findall('a[cd][cde]', a)

p = re.findall('^a[cd][cde]', a)

print(r)

print(p)
import re

from personal_info import personal_info

class check(personal_info):

    a = []

    def visitor(self, name, age):

        super(check, self).name_age(name, age)

        self.a = ['Tanglichen', 'Gaopeixuan']

        if len(re.findall(name, personal_info.namelist)) <= 0  :

            print ('这个名字不在访客名单中')

        else:

            print ('允许进入')


person_1 = check()

person_1. visitor('Tanglichen',21)

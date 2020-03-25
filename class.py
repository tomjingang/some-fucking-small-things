class Chinese():

    Name = ''

    City = ''

    def dianming(self):

        print('what\'s your name')

        self.Name = input()

        print ('where are you from')

        self.City = input()

        print (self.Name + 'is from ' + self.City)



chinese = Chinese()

chinese.dianming()
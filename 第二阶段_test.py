class Maicai():

    maicai_plan_list = list()

    maicai_actuell_list = list()

    def maicai_plan(self):

        print ('what do you want to buy')

        x = input()

        self.__class__.maicai_plan_list = x.split(',')

        self.__class__.maicai_plan_list = list(self.__class__.maicai_plan_list)

        print(self.__class__.maicai_plan_list)

        return x

    def maicai_actuell(self):

        print ('what have you bought')

        y = input()

        self.__class__.maicai_actuell_list = y.split(',')

        self.__class__.maicai_actuell_list = list(self.__class__.maicai_actuell_list)

        print(self.__class__.maicai_actuell_list)

        return y

    def judge(self):

        list_1 = sorted(self.__class__.maicai_plan_list)

        list_2 = sorted(self.__class__.maicai_actuell_list)

        if list_1 == list_2:
            
            print ('you have already bought all food')

        else:

            for q in list_1:

                if q not in list_2:

                    list_dont_bought = q.split(',')

                    print ('you havent bought' + str(list_dont_bought))

                else:    

                    for p in list_2:

                        if p not in list_1:

                            list_dont_need_buy = p.split(',')

                            print('you dont need to buy' + str(list_dont_need_buy))






today = Maicai()

today.maicai_plan()

today.maicai_actuell()

today.judge()










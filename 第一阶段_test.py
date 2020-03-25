jineng = input ('你放了什么技能')

def damage(**param):

    for skill,damage in param.items():

        if damage >= 100:

            print ('你成功击杀了一个敌人')

        else:

            print('伤害不致死')

def skill():

    q, w, e = 'shenmiezhan', 'siwangyizhi', 'longpozhan'

    a = { 'shenmiezhan' : 120, 'siwangyizhi' : 150, 'longpozhan' : 90, 'siwangdiaoling' : 50} 

    print('请释放技能')

    jineng = input()

    print (a[jineng])

    if a[jineng] >= 100:

        print('success')

    else:
        
        print('fail')


    


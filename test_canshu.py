def account( **param):

    for account, password in param.items():

        print('please type your account')

        user_account = input()

        print('please type your password')

        user_password = input()

        if user_account == account and user_password == password:
            
            print ('success')

            break

        else:
            print ('fail')

            break



account(tanglichen = 'yuming1734', tomjingang = 'tlc5520742')
            
 

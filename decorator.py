import time

def control(button):

        def decorator(func):


            # 装饰器一定要有一个函数参数

            def hours():

                if button == 'on':

                    print(time.time() / 3600)

                func()
        
            return hours

            # 注意装饰器下面的函数都要返回值

        return decorator 

        # 想成为装饰器必须最终还是返回函数      

@control('on')
def f1():

    print ('what time is it')

f1()



            

            


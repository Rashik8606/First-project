lis = []
class login_pass():
    def __init__(self,password):
        self.Password=password

    def display(self):
        print('1.Login \n2.Reset \n3.Exit')

    def login(self,paw):
        lis.append(paw)

        if self.Password ==paw:
            print('Logged in successfully !')
        elif lis[-1]==lis[-2]:
            print('New Password !!')
        else:
            print('You Entered Wrong Password !!')

    def reset(self,reset):
        lis.append(reset)
        print('Password Reseted')

    def exit():
        print('Exit...')


password = int(input('Enter Your Password -->'))
call=login_pass(password)
call.display()

while True:
    user_choice = int(input('Enter Your option -->'))
    if user_choice==1:
        pas=int(input('enter Your Password -->'))
        call.login(pas)

    elif user_choice==2:
        res=int(input('Enter YOur New Password -->'))
        call.reset(pas)

    elif user_choice==3:
        call.exit(pas)
        break

    else:
        print('Wrong Password !!')

print(lis)


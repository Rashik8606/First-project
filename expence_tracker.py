expence = {}
wallet = 1000

while True:
    print(f"{'1.ADD EXPENCE'} {'2.ADD BALANCE'} {'3.VIEW BALANCE'} {'4.EXIT'}")
    user_Input = int(input('SELECT YOUR OPTION -->'))
    if user_Input==1:
        print('ENTER YOUR EXPENCE !')
        expence_Name = input('ENTER YOUR EXPENCE-->')
        if expence_Name in expence:
            print(expence_Name,'IS ALREADY EXCEED !!!')
            print('ENTER YOUR AMOUNT !')
            amount_Num = int(input('ENTER YOUR AMOUNT--->'))
            if amount_Num<=wallet:
                old_Amount = expence[expence_Name]
                expence[expence_Name]=amount_Num+old_Amount
                wallet=wallet-amount_Num
            else:
                print('EXPENCE EXCEED ALREADY THE BALANCE !!')
        else:
            amount_Num = int(input('ENTER YOUR AMOUNT -->'))
            expence[expence_Name]=amount_Num
            wallet=wallet-amount_Num

    elif user_Input==2:
        print('UPDATED > ',wallet)
        



    elif user_Input==3:
        print(expence)
        print('WALLET BALANCE >',wallet)
        


    else:
        exit('EXIT !!')           

               

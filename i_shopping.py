class i_shopping():
    def __init__(self):
        pass
        
    def fashion(self):
        print("You looking For :\n.jeans\n.sarees\n.bra")
        fashion = input('Select Your Option ---> ').lower()
        if fashion == 'jeans':
            print("👖Peter England >RS.1'007\n👖Campus sutra >RS.721")
        elif fashion == 'sarees':
            print("🥻kanjiwram silk >RS.1500\n🥻Choffon >RS.750")
        elif fashion == 'bra':
            print("👙Love Maker >RS.160\n👙IMSA Moda >RS.199\n👙Pretty Cat >RS.379")
        else:
            print("Invalid Option")
            return
        
        user_fashion = input("SELECT YOUR FASHION :").lower()
        lis_user_fashion = ["peter england" or "campus sutra" or "kanjiwram silk" or "choffon" or "love maker" or "imsa moda" or "pretty cat"]
        if user_fashion in lis_user_fashion:
            print(f"you select > {user_fashion.title()} ")
            print("YOUR ITEM WILL BE AT YOUR HOME WITHIN TWO DAYS... ")
            print("So Glad you choose I Shopping🧳")
        else:
            print("Oder Cancelled ! becuse you entered invalid option")
            

    def mobile(self):
        print("available mobile brands\nI.Phone\nPOCO\nREALME")
        mobile = input("SELECT YOUR MOBILE COMPANY --> ").lower()
        if mobile == "iphone":
            print("📱I.phone 14 plus >RS.58'000 \n📱iphone 15 pro >RS.1'19'000 ")
        elif mobile == "poco":
            print("📱POCO X6 >RS.15000\n📱POCO S2 >RS.20000")
        elif mobile == "realme":
            print("📱REALME MX PRO >RS.45000\n📱REALME S2 >RS.33000")
        else:
            print("INVALID OPTION ! please try again")
            return
        user_phone = input("select your phone : ").lower()
        user_phone_lis = ["iphone 14 plus" or "iphone 15 pro" or "pop x6" or "pop s2" or "realme mx pro" or "realme s2"]
        if user_phone in user_phone_lis:
            print(f"you select > {user_phone.title()} ")
            print("YOUR ITEM WILL BE AT YOUR HOME WITHIN TWO DAYS... ")
            print("So Glad you choose I Shopping🧳")
        else:
            print("Oder Cancelled ! becuse You entred invalid Option")

    def fight_tickets(self):
        from_user = input("FROM :")
        to_user = input("TO :")
        if from_user and to_user:
            print("🛫SELECT YOUR CLASS \nEconomy\nBusiness")
            class_user = input("> ")
            if class_user == 'economy':
                print("Economy Price : 20000")
            elif class_user == 'business':
                print("Business Price : 50000")
            else:
                print('invalid option')
                return
        
        if class_user or "economy" or "business":
            print(f"you Select {class_user.title()}  class !")
            print("_________________________")
            print("Have a Nice Trip 🛫")
            print("📜Ticket Date : 12/11/2024")
        else:
            print("Sorry Ticket Cancelled !  Becuse you entered invalid option")

def main():
    print("First You create account I.Shopping")
    first_usr = input("Your Name Is : ? -->")
    create_password =input("Enter Passkey :")

    exp = i_shopping()
    while True:
            print("🧳 WELCOME TO THE I SHOPPING ")
            print("_______________________________")
            print("1.👗Fashion 2.📱Mobile 3.✈️Fight tickets")
            print()
            select_user = input("Which of these are you looking for ? ")
            if select_user == "fashion":
                exp.fashion()
            elif select_user == "mobile":
                exp.mobile()
            elif select_user == "fight ticket":
                exp.fight_tickets()
            else:
                exit('YOU ENTERED INVALID OPTION')
if __name__=="__main__":
    main()



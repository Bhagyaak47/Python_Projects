
class Bank :
    users={
        # userName : [phNo, Addr, PAN, email, password, accBalance]
        "Bhagyashree":["2418928965","Nerul","MH12373789","bhagya@gmail.com","123",0.0],
        "Abhi":["8888888888","Nerul","MH12373796","abhi@gmail.com","123",0.0],
        "Shraddha":["7777777777","Thane","MH11554437","gan@gmail.com","123",0.0],
        "Shreyas":["6666666666","Pune","MH12373745","shre@gmail.com","123",0.0],
        "D":["5555555555","Vashi","MH12373267","d@gmail.com","123",0.0]}   
    bankname = "Axis Bank"
    branch   = "Haware fantasia,Vashi"
    
    def create_acc(self):
        name = self.fn_user_name()
        contact_no = self.fn_contact_number()
        address = self.fn_address()
        pan_card_no = self.fn_pan_number()
        mail = self.fn_email_id()
        password = self.fn_password()
        self.users.update({name: [contact_no, address, pan_card_no, mail, password, 0.0]})
       
        print("                  ")
        print(f'Dear {name},\nThank you very much for choosing {Bank.bankname}') 
        print("Your registration completed successfully....")
        
    def fn_user_name(self):
        name = input("Enter user name : ")
        if name.isdigit() or name=="":
            print("  x-x-x-x---->|  print valid name  |<-----x-x-x-x  ")
            name = self.fn_user_name()
        else:
            for i in self.users.items():
                if name == i[0]:
                    print(f"Account for this {name} already exists enter new name.")
                    name = self.fn_user_name()
                    break
        return name

    def fn_contact_number(self):
        phNo = input("Enter contact number : ")
        if phNo.isdigit():
            for i in self.users.items():
                if phNo == i[1][0]:
                    print("  x-x-x-x---->|  This contact no. is already registered | Enter new contact no. |<----x-x-x-x  ")
                    phNo = self.fn_contact_number()
                    break
        else: 
            print("  x-x-x-x---->|  Enter Valid Contact Number  |<----x-x-x-x  ")
            phNo = self.fn_contact_number()

        return phNo
    
    def fn_address(self):
        addr = input("Enter address : ")
        return addr

    def fn_pan_number(self):
        pan = input("Enter PAN number : ")
        if len(pan) != 10:
            print("  x-x-x-x---->|  This PAN Card no. is Invalid Please enter another PAN Card No. |<------x-x-x-x  ")
            pan = self.fn_pan_number()

        for i in self.users.items():
            if pan == i[1][2]:
                print(f"  x-x-x-x---->|  {pan} is already registered | Enter new PAN no. |<----x-x-x-x  ")
                pan = self.fn_pan_number()    
                break       
            
        return pan 
    
    def fn_email_id(self):
        email = input("Enter email id (must contain @gmail.com) : ")
        if "@gmail.com" not in email :
            print("  x-x-x-x--->|  Enter valid email ID having @gmail.com  |<-----x-x-x-x  ")
            email = self.fn_email_id()
            
        for i in self.users.items():
            if email == i[1][3]:
                print("  x-x-x-x--->|  This E-mail is already registered | Enter valid email id  |<-----x-x-x-x  ")   
                email = self.fn_email_id()
                break

        return email
    
    def fn_password(self):
        password = input("Enter Password : ")
        return password
    
    def admin_login(self):
        self.admin_name=input("Enter your name : ")
        if self.admin_name=="admin":
            password=input("Enter password : ")
            if password=="pass@123":
                print("----->| Welcome Admin |<-----")     
                while(True):
                    print("....................")
                    print("\n1.Check Users \n2.Delete User \n3:Exit ")
                    print("....................")
                    choice2=input("Enter your choice : ")
                    if choice2=="1":
                        print(self.users)
                    elif choice2=="2":
                        del_user_name = input("Enter User Name to Delete : ")
                        if(del_user_name in self.users.keys()) :
                            if(self.users.get(del_user_name)[5] != 0):
                                print(f"Unable to delete account for {del_user_name}. \nAccount has available balance : {self.users.get(del_user_name)[5]} ")
                            else :
                                self.users.pop(del_user_name)
                                print("User deleted : " , del_user_name)
                        else:
                            print("Wrong user name..Kindly enter correct user name to delete.")
                    elif choice2=="3":
                        break
                    else:
                        print("  x-x-x-x  Enter valid choice  x-x-x-x  ")           
            else:
                print("  x-x-x-x  Incorrect Password  x-x-x-x  ")       
        else:
            print("  x-x-x-x  Enter valid name   x-x-x-x  ")

    def user_login(self):
        self.name2=input("Enter your name : ")             
        if self.name2 in self.users.keys():    
            password=input("Enter password : ")
            if password==self.users.get(self.name2)[4]:
                print("----->| Welcome",self.name2,"|<-----")
                while True:
                    print("                        ")
                    print("Please Select any option : ")
                    print("1.Deposit1\n2.Withdraw\n3.Ministatement\n4.Transfer\n5.Log out")
                    print(".......................")
                    option=input("Enter your option :")
                    print("........................")

                    if option == "1":
                        amount= input("Enter Deposit Amount: ")
                        if amount.isdigit():
                            Obj.deposit(int(amount))
                        else:
                            print("  x-x-x-x---->|  Enter valid amount  |<----x-x-x-x  ")
                            
                    if option == "2":
                        amount=input("Enter Withdraw Amount:")
                        if amount.isdigit():
                            Obj.withdraw(int(amount))
                        else:
                            print("  x-x-x-x----->|  Enter valid amount  |<-----x-x-x-x  ")
                                                
                    if option == "3":
                        Obj.ministatement()
                        
                    if option == "4":
                        amount=input("Enter Transfer Amount:")
                        if amount.isdigit():
                            self.name3 = input("Enter beneficiary name : ")
                            Obj.Transfer(int(amount))
                        else:
                            print("  x-x-x-x----->|  Enter valid amount  |<-----x-x-x-x  ")
                            
                    if option == "5":
                        print("      ")
                        print(f"Logged out successfully !!! \nThanks for using {Bank.bankname}, {Bank.branch}.")
                        break  
                    
                    else :
                        print("Enter valid choice")       
            else:
                print("  x-x-x-x------>|  Incorrect Password   |<-----x-x-x-x  ") 
        else:
            print("  x-x-x-x---->|  Enter valid name  |<----x-x-x-x  ")      

    def deposit(self,amount):
        if amount >0:
           self.users.get(self.name2)[5] = self.users.get(self.name2)[5] + amount
           print(f'Transaction Completed. INR {amount} credited successfully!!!...')
           print(f'Current Balance is INR  {self.users.get(self.name2)[5]}')
        else:
           print("Invalid amount transaction aborted...")        
    
    def withdraw(self,amount):
        if amount <= self.users.get(self.name2)[5] and amount >0:
            self.users.get(self.name2)[5] = self.users.get(self.name2)[5]-amount
            print(f'Transaction Completed.INR {amount} debited successfully!!!...')
            print(f'Available Balance is {self.users.get(self.name2)[5]}')
        else:
            print("Insufficient balance.. transaction aborted...")
   
    def ministatement(self):
            print(f"Your account balance is INR {self.users.get(self.name2)[5]}")

    def Transfer(self,amount):
        if amount<= self.users.get(self.name2)[5] and amount>0:
            self.users.get(self.name2)[5] = self.users.get(self.name2)[5]-amount
            self.users.get(self.name3)[5] = self.users.get(self.name3)[5] + amount
            print(f'Transaction Completed. INR {amount} Transfered to {self.name3} successfully!!!')
            print(f'Available Balance is {self.users.get(self.name2)[5]}')  
        else:
            print(f'Insufficient available balance. Entered amount is : {amount}. Transfer aborted.')
                     
    def home(self):
        print(f"\n----->|  Welcome to,{Bank.bankname},{Bank.branch}  |<-----")
        while(True):
            print("....................")
            print("1:Create new account \n2:Log In \n3.Admin login \n4.exit")
            print("....................")
            choice=(input("Enter your choice : "))
            if choice=="1":
                Obj.create_acc()    
            elif choice=="2":
                Obj.user_login()
            elif choice=="3":
                Obj.admin_login()
            elif choice=="4":
                break
            else:
                print("  x-x-x-x---->|  Enter valid choice  |<-----x-x-x-x   ")

Obj=Bank()
Obj.home()
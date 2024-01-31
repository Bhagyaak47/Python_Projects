
#----- Imports ------------------------------------------------------------------------------------------------------


import mysql.connector
import sys
import datetime


#----- Creating New Account ------------------------------------------------------------------------------------------

def Create_account():

        print("─────────────────────> Creating New Account <────────────────────")
        print("*"*65)
         
        data=()
        Acc_No=fn_Acc_No()
        Cus_Name=fn_Cust_Name()
        Email_ID=fn_Email_ID()
        Contact_No=fn_contact_number()
        Opening_Balance=fn_Opening_Balance()
        Password=input("Enter Password to be set:")
        data=(Acc_No,Cus_Name,Email_ID,Contact_No,Opening_Balance,Password) 
        query="INSERT INTO Customer VALUES (%s, %s,%s,%s,%s,%s)"
        mycursor.execute(query,data)
        mydb.commit()  
        
        print("                  ")
        print("*"*65)
        print("─────────────────────> Check Your Details <────────────────────")
        print("                  ")
        print(f'Account No      :       {Acc_No}         ')
        print(f'Customer Name   :       {Cus_Name}       ')
        print(f'Email ID        :       {Email_ID}       ')
        print(f'Contact No      :       {Contact_No}     ')
        print(f'Opening Balance :       {Opening_Balance}')
        print(f'Password        :       {Password}       ')
        print("                  ")
        print("*"*65)
        print(f'Dear {Cus_Name},\nThank you very much for choosing +-< BHAGYA BANK [-: Life Ko Banao Rich :-] >-') 
        print("Your registration completed successfully....")
        print("                   ")
        print("*"*65)
              
#-------------------------------------------------------------------------------------------------------------------------


def fn_Acc_No():

    Acc_No=input("Enter Acc_No : ")
    if Acc_No.isdigit():
        mycursor.execute("SELECT Acc_No from Customer where Acc_No={0}".format("\'"+Acc_No+"\'"))
        result=mycursor.fetchone()
        if not result:
            return Acc_No
        else:
            print("  x-x-x-x---->|  Enter another Account Number as it may already registered with us  |<----x-x-x-x  ")
            Acc_No=fn_Acc_No()
            return Acc_No
    else: 
        print("  x-x-x-x---->|  Enter Valid Account Number  |<----x-x-x-x  ")
        Acc_No=fn_Acc_No()
        return Acc_No

def fn_Cust_Name():

    Cust_Name = input("Enter user name : ")
    if Cust_Name.isdigit() or Cust_Name=="":
        print("  x-x-x-x---->|  Enter valid name  |<-----x-x-x-x  ")
        Cust_Name = fn_Cust_Name()
        return Cust_Name
    else:
        return Cust_Name
    
def fn_Email_ID():

    Email_ID = input("Enter email id (must contain @gmail.com) : ")
    if "@gmail.com" not in Email_ID :
        print("  x-x-x-x--->|  Enter valid email ID having @gmail.com  |<-----x-x-x-x  ")
        Email_ID = fn_Email_ID() 
        return Email_ID           
    else:          
        return Email_ID

def fn_contact_number():

    Contact_No = input("Enter contact number : ")
    if Contact_No.isdigit() and len(Contact_No)==10:
        return Contact_No                    
    else: 
        print("  x-x-x-x---->|  Enter Valid Contact Number  |<----x-x-x-x  ")
        Contact_No = fn_contact_number()
    

def fn_Opening_Balance():

    Opening_Balance=input("Enter Bank_Account Opening Amt -->Min limit 1000 Rs.) : ")
    if Opening_Balance.isdigit():
        Opening_Balance=int(Opening_Balance)
        if Opening_Balance >0:
            return Opening_Balance
        else:
            print("  x-x-x-x---->| Invalid amount !!!  |<----x-x-x-x  ") 
            Opening_Balance=fn_Opening_Balance()
    else:
        print("  x-x-x-x---->| Invalid amount !!!  |<----x-x-x-x  ") 
        Opening_Balance=fn_Opening_Balance()

#--- Login to user -----------------------------------------------------------------------------------------------------------------

                  
def login_to_user():
         
        
        print("─────────────────────> Login to your Account <────────────────────")
        print("*"*65) 
        print("WARNING : Only three Attempts to login at a time") 
        
        Acc_No=input("Enter Acc_No : ")
        mycursor.execute("SELECT Cust_Name from Customer where Acc_No={0}".format("\'"+Acc_No+"\'"))
        result=mycursor.fetchone() 
        if result:
            Cus_Name=result[0]
            for attempts in range(0,3):   
                Password=input("Enter Your PIN:")
                print()
                print("*"*65)
                mycursor.execute("SELECT Password from Customer where Acc_No={0}".format("\'"+Acc_No+"\'"))
                result=mycursor.fetchone()
                if result:
                    temp,=result #coverting tuple to integer fro comparing password
                    if temp==Password and attempts != 3: # authenticated usernames and passwords
                        print(f"\nDear {Cus_Name},\nWelcome to BHAGYA BANK [-: Life Ko Banao Rich :-] \n ".format("\'"+Cus_Name+"\'"))
                        print("*"*65)
                        while True:
                            print("                        ")
                            print("Please Select any option : ")
                            
                            print()

                            print("  ┌────────────────┐  ╭───────────────────────╮     ")
                            print("  │  ╭┼┼╮          │  │ ▶︎ 1 • Deposite              ")
                            print("  │  ╰┼┼╮          │  ├───────────────────────|     ")
                            print("  │  ╰┼┼╯          │  │ ▶︎ 2 • Withdraw              ")
                            print("  │                │  ├───────────────────────|     ")
                            print("  │  B H A G Y A   │  │ ▶︎ 3 • Ministatement         ")
                            print("  │  B A N K       │  ├───────────────────────|      ")
                            print("  │                │  │ ▶︎ 4 • Transfer               ")
                            print("  │ Life Ko Banao  │  ├───────────────────────|      ")
                            print("  │ Rich.....      │  │ ▶︎ 5 • Feedback               ")
                            print("  │ ║│┃┃║║│┃║│║┃│  │  ├───────────────────────|       ")
                            print("  │ ║│┃┃║║│┃║│║┃│  │  │ ▶︎ 6 • Log Out                ")
                            print("  └────────────────┘  ╰───────────────────────|       ")
                                                                
                            option = input("\n ☞ Enter Your option: ")
                            print("*"*65)
                            if option == '1':
                                amount = input("Enter Deposit Amount: ")
                                amount = fn_get_amount(amount)
                                fn_deposite(amount, Acc_No)
                                continue
                            
                            if option == "2":
                                amount=input("Enter Withdraw Amount:")
                                amount = fn_get_amount(amount)
                                fn_Withdraw(amount, Acc_No)
                                continue

                            if option == "3":
                                fn_Ministatement(Acc_No)
                                continue

                            if option == "4":
                                amount=input("Enter Transfer Amount:")
                                amount = fn_get_amount(amount)
                                fn_Transfer(Acc_No, amount)
                                continue

                            if option == '5':
                                comment = input("Write your feedback/Suggestions :")
                                fn_Feedback(Acc_No, comment)
                                continue

                            if option == '6':
                                home()
                                break
                    else :
                        print("\t INVALID PASSWORD OR USERNAME ! TRY AGAIN ")
                        print("\t {0}st attempt is over \n ".format(attempts + 1))
                        continue
        else :
            print("\t NO SUCH ACCOUNT  ! TRY AGAIN ")
            login_to_user()

#-----------------------------------------------------------------------------------------------------------                    

def fn_get_amount(amount):
    if amount.isdigit():
        return (int(amount))
    else:
        print("  x-x-x-x---->|  Enter valid amount  |<----x-x-x-x  ")
        amount = fn_get_amount()

#------------------------------------------------------------------------------------------------------------


def fn_deposite(amount, Acc_No):
    data=(amount, datetime.datetime.now(), Acc_No, 'Credit')
    mycursor.execute("SELECT Cust_Name from Customer where Acc_No={0}".format("\'"+Acc_No+"\'"))
    result=mycursor.fetchone() 
    if result:
        Cust_Name=result[0]

        query="INSERT INTO transaction VALUES (%s,%s,%s,%s)"
        mycursor.execute(query,data)

        data=(amount, Acc_No)
        query="update customer set available_bal = available_bal+%s where acc_no = %s"
        mycursor.execute(query,data)
        mydb.commit()  
        print(f'Dear {Cust_Name} {amount}Rs. credited to your Account Number {Acc_No} successfully!!!')
        print("             ")
        print("*"*65)

#-------------------------------------------------------------------------------------------------------------
 
   
def fn_Withdraw(amount, Acc_No):
    mycursor.execute("SELECT Available_Bal from Customer where Acc_No={0}".format("\'"+Acc_No+"\'"))
    result=mycursor.fetchone()
    if result[0] > amount:
        mycursor.execute("SELECT Cust_Name from Customer where Acc_No={0}".format("\'"+Acc_No+"\'"))
        result=mycursor.fetchone()
        cust_name = result[0]

        data=(amount, datetime.datetime.now(), Acc_No, 'Debit')
        query="INSERT INTO transaction VALUES (%s,%s,%s,%s)"
        mycursor.execute(query,data)

        data=(amount, Acc_No)
        query="update customer set available_bal = available_bal-%s where acc_no = %s"
        mycursor.execute(query,data)
        mydb.commit()
           
        print(f'Dear {cust_name} {amount}Rs. debited from your account number:{Acc_No} successfully!!!')
        print("             ")
        print("*"*65)
    else:
        print("insufficient balance!!!")


#--------------------------------------------------------------------------------------------------------------


def fn_Ministatement(Acc_No):
    
    print("upto Last 10 Transactin's can be seen under mini statement.")
    mycursor.execute("SELECT Available_Bal from Customer where Acc_No={0}".format("\'"+Acc_No+"\'"))
    result=mycursor.fetchone()
    print(f'Your current balance is {result[0]} Rs.')
    print("---------------------------------------------------------------")
    print("             ")
    mycursor.execute("SELECT Amount, Trans_Date, Transaction_type from transaction where Beneficiary_Acc={0} limit 10".format("\'"+Acc_No+"\'"))
    result=mycursor.fetchall()
    for i in range(0, len(result)):
        print("Serial No: ",i+1,result[i])
        print("-----------------------------------------------------------")
      

#-----------------------------------------------------------------------------------------------------------------



def fn_Transfer(acc_no, amount):
    ben_acc_no = input("Enter beneficiary account number")
    mycursor.execute("SELECT Available_Bal from Customer where Acc_No={0}".format("\'"+ben_acc_no+"\'"))
    result=mycursor.fetchone()
    if result:
        fn_Withdraw(amount, acc_no)
        fn_deposite(amount, ben_acc_no)
    else:
        print("Beneficiary account number invalid..")
        fn_Transfer(acc_no, amount)

#--------------------------------------------------------------------------------------------------------------------


def fn_Feedback(acc_no, comment):
    rating = input("Enter rating (1 to 5)")
    if rating.isdigit():
        rating = int(rating)
        if rating >0 and rating < 6:
            data=(acc_no, comment, rating, datetime.datetime.now())
            query="INSERT INTO feedback VALUES (%s,%s,%s,%s)"
            mycursor.execute(query,data)
            mydb.commit()
            print("Thank you for your feedback!!!")
            print("             ")
            print("*"*65)
        else:
            rating = fn_Feedback(acc_no, comment)
    else:
        rating = fn_Feedback(acc_no, comment)     

#---- Admin Login -------------------------------------------------------------------------------------------------------------------

def Admin_login():
    print("─────────────────────> Admin Login <────────────────────")
    print("*"*65) 
    AdminID=input("Enter your AdminID: ")
    if AdminID=="Bhagya5":
        password=input("Enter password : ")
        if password=="pass@123":
            print("      ")
            print("*"*65)
            print("\tDear Admin, ")
            print("\tWelcome to BHAGYA BANK [-: Life Ko Banao Rich :-]  ")     
            while(True):
                print("*"*65)
                
                print("► 1 ∙ Check Users ")
                
                print("► 2 ∙ Delete User ")

                print("► 3 ∙ Check Customer Feedback ")
                
                print("► 4 ∙ Exit ")
                
                # print("\n1.Check Users \n2.Delete User \n3:Exit ")
                print("*"*65)
                choice2=input("Enter your choice : ")
                if choice2=="1":
                    mycursor.execute("Select Acc_No,Cust_Name from Customer")
                    result=mycursor.fetchall()
                    for i in range(0, len(result)):
                        print("Serial No: ",i+1,result[i])
                        print("             ")
                elif choice2=="2":
                    Close_Acc()
                    pass
                elif choice2=="3":
                    mycursor.execute("Select Acc_No,Feedback,Rating,Date from Feedback")
                    result=mycursor.fetchall()
                    if len(result)>0:                        
                        for i in range(0, len(result)):
                            print("Serial No: ",i+1,result[i])
                            print("             ")
                    else:
                        print("No Record Found...")
                elif choice2=="4":
                    home()
                else:
                    print("  x-x-x-x  Enter valid choice  x-x-x-x  ") 
        else:
                print("  x-x-x-x  Incorrect Password  x-x-x-x  ")
                Admin_login()
    else:
            print("  x-x-x-x  Enter valid name   x-x-x-x  ")
            Admin_login()



#-------------------------------------------------------------------------------------------------------------------


def Close_Acc():
    Acc_No=input("Enter Acc_No : ")
    mycursor.execute("SELECT Cust_Name from Customer where Acc_No={0}".format("\'"+Acc_No+"\'"))
    result=mycursor.fetchone() 
    if result:
        Cust_Name=result[0]
        mycursor.execute("SELECT Acc_No from Customer where Acc_No={0}".format("\'"+Acc_No+"\'"))
        result=mycursor.fetchone()
        if result:
            temp,=result
            if temp==Acc_No:
                mycursor.execute("Delete from Customer where Acc_No={0}".format("\'"+Acc_No+"\'")) 
                print("*"*65)
                print(f'Dear {Cust_Name},\nThank you very much for using +-< BHAGYA BANK [ : Life Ko Banao Rich : ] >-')
                print(f'Account No.{Acc_No},has been successfully deleted..')
                print("             ")
                print("*"*65)
               


#---  Main Menu Home ----------------------------------------------------------------------------------------------------------------


def home() :

    print("  ┌─────────────────────────────────────────────────────────────┐             ")
    print("  │  ╭┼┼╮   -: W E L C O M E  TO  B H A G Y A  B A N K :-       │             ")
    print("  │  ╰┼┼╮         ( Life Ko Banao Rich.... )                    │             ")
    print("  │  ╰┼┼╯  Our Branches : Maharashtra | Delhi | London | Dubai  │             ")
    print("  │                                                             │             ")
    print("  └─────────────────────────────────────────────────────────────┘             ")
    print("*"*65)

    print("  ┌────────────────┐  ╭──────────────────────────────┐       ")
    print("  │  ╭┼┼╮          │  │ ▶︎ 1 • Create Account                 ")
    print("  │  ╰┼┼╮          │  ├──────────────────────────────|       ")
    print("  │  ╰┼┼╯          │  │ ▶︎ 2 • Log In                        ")
    print("  │ B H A G Y A    │  ├──────────────────────────────|       ")
    print("  │ B A N K        │  │ ▶︎ 3 • Admin Login                    ")
    print("  │                │  ├──────────────────────────────|        ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  │ ▶︎ 4 • Close An Account                ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  ├──────────────────────────────|        ")
    print("  │                │  │ ▶︎ 5 • Exit System                     ")
    print("  └────────────────┘  ╰──────────────────────────────┘         ")


    print("*"*65)

    while True :
        ch= int(input("\n  ☞ Enter your command --> Select [ 1/2/3/4/5/6/7 ]: "))
        print()
        print("*"*65)
        if ch== 1:
            Create_account()
            home()
            break
        elif ch== 2 :
            login_to_user()
            break
        elif ch== 3 :
            Admin_login()
            break
        elif ch== 4 :
            Close_Acc()
            home()
            break
        elif ch== 5 :
            cancel_request = input(" DO YOU WISH TO EXIT... [yes/no ] :  ")
            if cancel_request in ["yes","Yes","YES"] :
                sys.exit()
            break
        else :
            print(" INVALID COMMAND ")
            print(" RETRY \n")
            continue
#--------------------------------------------------------------------------------------------------------- 

print("Establishing connection ..... ")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password",database="bankproject")
mycursor=mydb.cursor()
print("connected !!! ")

home()
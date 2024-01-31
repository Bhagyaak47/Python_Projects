import mysql.connector

print("-----"*20)
#---------------------------------------------------------------------------------------------------------

mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="password")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Bankproject")
mycursor.execute("USE Bankproject")
print("Database created..")
#------------------------------------------------------------------------------------------------------------
print("-----"*20)
mycursor.execute("SHOW TABLES LIKE 'Customer'")

result=mycursor.fetchone()
if result : 
    pass
    print("Customer table already created...")
else : #if Table doesn't exists then it will be created
    mycursor.execute("CREATE TABLE Customer(Acc_No varchar(35) PRIMARY KEY,Cust_Name varchar(35) NOT NULL ,Email_Id varchar(30) NOT NULL,Contact_No varchar(35) NOT NULL,Available_Bal int(30) DEFAULT '0',Password varchar(35) NOT NULL)")
    
    data1=("100","Bhagyashree","bhagya@gmail.com","1295944255","1000","123")
    data2=("101","Kavya","kavya@gmail.com","8475963215","1000","123")
    data3=("102","Soniya","soni@gmail.com","9685741235","1000","123")
    query1="INSERT INTO Customer VALUES(%s, %s, %s,%s, %s, %s)"
    mycursor.execute(query1,data1)
    mycursor.execute(query1,data2)
    mycursor.execute(query1,data3)
    mydb.commit()
    print("Customer Table values inserted successully....")

#---------------------------------------------------------------------------------------------------------------
print("-----"*20)

mycursor.execute("SHOW TABLES LIKE 'Transaction' ")

result=mycursor.fetchone()
if result :
    pass
    print("Transaction table already created...") 
else : #if Table doesn't exists then it will be created
    mycursor.execute("CREATE TABLE Transaction (Amount int(20) NOT NULL , Trans_Date date NOT NULL , Beneficiary_Acc varchar(10) NOT NULL ,Transaction_type varchar(35) NOT NULL)")
    print("Transaction table created successfully...")
    
#------------------------------------------------------------------------------------------------------------------
print("-----"*20)

mycursor.execute("SHOW TABLES LIKE 'AdminRecord' ")

result=mycursor.fetchone()
if result : 
    pass
    print("Adminrecord table already created..")
else: #if Table doesn't exists then it will be created
    mycursor.execute("CREATE TABLE AdminRecord(AdminID varchar(10) PRIMARY KEY, Password varchar(20))")
    print("AdminRecord table created successfully..")
    
    data4=("Bhagya5","123")
    query2="INSERT INTO AdminRecord VALUES(%s, %s)"
    mycursor.execute(query2,data4)
    mydb.commit()
    print("Inserted values successfully in Admin_record table")

#-------------------------------------------------------------------------------------------------------------------
print("-----"*20)

mycursor.execute("SHOW TABLES LIKE 'Feedback' ")

result=mycursor.fetchone()
if result : 
    pass
    print("Feedback table already created..")
else : #if Table doesn't exists then it will be created
    mycursor.execute("CREATE TABLE Feedback(Acc_no varchar(35), Feedback varchar(100), Rating varchar(10), Date DATE)")
    print("Feedback table created..")
    

#--------------------------------------------------------------------------------------------------------------------
print("-----"*20)
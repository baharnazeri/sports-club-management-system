import csv
import re
#import pandas as pd 
#pip install tabulate 
#we creat a dictionary
from tabulate import tabulate

'''data_swim1=[ ['saturday','sunday','monday','tuesday','wednesday'],
      ['8-10','poya','Darya','NA','Harry','Ava'],
      ['10-12','Ava','Harry','poya','NA','NA'],
      ['2_4','NA','NA','Darya','poya','NA'],
      ['4_6','Ava','NA','Darya','Harry','NA'],
      ['6_8','NA','Ava','poya','Harry','NA']]
#data[2][5]='lalala'
with open("data_swim1.csv",mode='w')as file:
    writer=csv.writer(file)
    for row in data_swim1:
        writer.writerow(row)'''

'''data_aerobic1=[ ['saturday','sunday','monday','tuesday','wednesday'],
      ['8-10','Sara','Alex','NA','Tara','ALI'],
      ['10-12','Sara','Tara','Alex','NA','NA'],
      ['2_4','NA','Ali','Ali','Tara','Sara'],
      ['4_6','Alex','NA','Sara','Sara','NA'],
      ['6_8','NA','ALI','Sara','NA','NA']]
with open("data_aerobic1.csv",mode='w')as file:
    writer=csv.writer(file)
    for row in data_aerobic1:
        writer.writerow(row)'''

'''data_bodybulding1=[ ['saturday','sunday','monday','tuesday','wednesday'],
      ['8-10','Alex','Alex','NA','Tara','ALI'],
      ['10-12','Sara','Tara','Alex','NA','NA'],
      ['2_4','NA','Ali','Ali','Tara','Sara'],
      ['4_6','Alex','NA','Sara','Sara','NA'],
      ['6_8','NA','ALI','Sara','NA','NA']]
with open("data_bodybulding1.csv",mode='w')as file:
    writer=csv.writer(file)
    for row in data_bodybulding1:
        writer.writerow(row)'''

'''data_swim2=[['saturday','sunday','monday','tuesday','wednesday'],
       ['8_10','NR','NR','NR','NR','NR'],
       ['10_12','NR','NR','NR','NR','NR'],
       ['2-4','NR','NR','NR','NR','NR'],
       ['4_6','NR','NR','NR','NR','NR'],
       ['6_8','NR','NR','NR','NR','NR']]
with open("data_swim2.csv",mode='w')as file:
    writer=csv.writer(file)
    for row in data_swim2:
        writer.writerow(row)'''

'''data_aerobic2=[['saturday','sunday','monday','tuesday','wednesday'],
       ['8_10','NR','NR','NR','NR','NR'],
       ['10_12','NR','NR','NR','NR','NR'],
       ['2-4','NR','NR','NR','NR','NR'],
       ['4_6','NR','NR','NR','NR','NR'],
       ['6_8','NR','NR','NR','NR','NR']]
with open("data_aerobic2.csv",mode='w')as file:
    writer=csv.writer(file)
    for row in data_aerobic2:
        writer.writerow(row)'''

'''data_bodybulding2=[['saturday','sunday','monday','tuesday','wednesday'],
       ['8_10','NR','NR','NR','NR','NR'],
       ['10_12','NR','NR','NR','NR','NR'],
       ['2-4','NR','NR','NR','NR','NR'],
       ['4_6','NR','NR','NR','NR','NR'],
       ['6_8','NR','NR','NR','NR','NR']]
with open("data_bodybulding2.csv",mode='w')as file:
    writer=csv.writer(file)
    for row in data_bodybulding2:
        writer.writerow(row)'''

#df=pd.DataFrame(data)

    
class reserve:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        #self.password=password

    '''def information(self):
       fheader={'name','email','rswim','rbodybulding','raerobic','bill'}
       dict={'name':self.name , 'email':self.email,'rswim':'NR','rbodybulding':'NR','raerobic':'NR','bill':0}
       with open("r_information.csv",'a',newline='')as file:
           File=csv.DictWriter(file,fieldnames=fheader)
           File.writerow(dict)'''


    def check_class(self):
        x=int(input("1.swimming\n2.aerobic\n3.bodybulding\n4.classes fee"))
        if x==1:
           print("swiming classes are offered as follows:\n\n")
           with open("data_swim1.csv",'r')as file:
            reader=csv.reader(file)
            matrix=list(reader)
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
        elif x==2:
            print("Aerobic classes are offered as follows:\n\n")
            with open("data_aerobic1.csv",'r')as file:
             reader=csv.reader(file)
             matrix=list(reader)
             print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))

        elif x==3:
           print("Bodybulding classes are offered as follows:\n\n")
           with open("data_bodybulding1.csv",'r')as file:
            reader=csv.reader(file)
            matrix=list(reader)
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
        elif x==4:
            print("the cost of the classes are as follows:")
            print("bodybulding:600$")
            print("swimming:450$")
            print("aerobic:270$")
            print("you can choose the teacher you want and get the diet plan or supplement from her")
            print("the cost of diet plan:200$")
            print("the price of supplement:100$")
        else:
            print('wrong!!')


    def reserve_swim(self):
        with open("data_swim2.csv",'r')as file:
            reader=csv.reader(file)
            matrix=list(reader)
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
        email=input("enter your email:")
        with open("userss22.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email:
                 if row[7]=='NW':
                   print("you cant reserve class!first you should charge your wallet ")
                   sighn_up_user()
                 else:
                  day=int(input("which day do you choose:1.saturday\n2.sunday\n3.monday\n4.tuesday\n5.wednesday"))
                  time=int(input("which time do you choose:1.8_10\n2.10_12\n3.2_4\n4.4_6\n5.6_8"))
        #email=input("enter your email:")
                  day=day
                  time=time
                  day_time=str(day)+('.')+str(time)
                  with open("data_swim2.csv",'r')as file:
                    reader=csv.reader(file)
                    matrix=list(reader)
                    #print(matrix)
                    for row in rows:
                     if matrix[time][day]!='reserved':
                       matrix[time][day]='reserved'
                       with open("data_swim2.csv",'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerows(matrix)      
                 print("your reserve saved.thank you")
                 print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
                 with open("userss22.csv",'r')as file:
                     reader=csv.reader(file)
                     rows=list(reader)
                     for row in rows:
                         if row[1]==email:
                             row[8]=int(row[8])+450
                             with open("userss22.csv",'w',newline='')as file:
                                writer=csv.writer(file)
                                writer.writerows(rows)
                 with open("r_informations2.csv",'r')as file:
                     reader=csv.reader(file)
                     rows2=list(reader)
                     for row in rows2:
                         if row[1]==email:
                          
                          row[2]=day_time
                          row[5]=int(row[5])+450
                          with open("r_informations2.csv",'w',newline='')as file:
                             writer=csv.writer(file)
                             writer.writerows(rows2)
                 sighn_up_user()
        ''' with open("userss2.csv",'r')as file:
               reader=csv.reader(file)
               rows=list(reader)
               for row in rows:
                 if row[1]==email:
                    if row[5]>=2000:
                     row[5]=int(row[5])-2000                 
                     with open("userss2.csv",'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerows(rows)
                        print("the cost was deducted from your account")
                    else:
                        print("insufficient inventory\nyou have to charge your wallet first")
                        sighn_up_user()
                 else:
                     print("where are u")'''
        
        '''else:
            print("this time has already reserved pleas select another time")
            sighn_up_user()'''

    def reserve_aerobic2(self):
        with open("data_aerobic2.csv",'r')as file:
            reader=csv.reader(file)
            matrix=list(reader)
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
        email=input("enter your email:")
        with open("userss22.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email:
                 if row[7]=='NW':
                   print("you cant reserve class!first you should charge your wallet ")
                   sighn_up_user()
                 else:
                  day=int(input("which day do you choose:1.saturday\n2.sunday\n3.monday\n4.tuesday\n5.wednesday"))
                  time=int(input("which time do you choose:1.8_10\n2.10_12\n3.2_4\n4.4_6\n5.6_8"))
        #email=input("enter your email:")
                  day=day
                  time=time
                  day_time=str(day)+('.')+str(time)
                  with open("data_aerobic2.csv",'r')as file:
                    reader=csv.reader(file)
                    matrix=list(reader)
                    #print(matrix)
                    for row in rows:
                     if matrix[time][day]!='reserved':
                       matrix[time][day]='reserved'
                       with open("data_aerobic2.csv",'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerows(matrix)      
                 print("your reserve saved.thank you")
                 print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
                 with open("userss22.csv",'r')as file:
                     reader=csv.reader(file)
                     rows=list(reader)
                     for row in rows:
                         if row[1]==email:
                             row[8]=int(row[8])+270
                             with open("userss22.csv",'w',newline='')as file:
                                writer=csv.writer(file)
                                writer.writerows(rows)
                 with open("r_informations2.csv",'r')as file:
                     reader=csv.reader(file)
                     rows2=list(reader)
                     for row in rows2:
                         if row[1]==email:
                          
                          row[4]=day_time
                          row[5]=int(row[5])+270
                          with open("r_informations2.csv",'w',newline='')as file:
                             writer=csv.writer(file)
                             writer.writerows(rows2)
                 sighn_up_user()
       

    def reserve_bodybulding(self):
         with open("data_bodybulding2.csv",'r')as file:
            reader=csv.reader(file)
            matrix=list(reader)
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
         email=input("enter your email:")
         with open("userss22.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email:
                 if row[7]=='NW':
                   print("you cant reserve class!first you should charge your wallet ")
                   sighn_up_user()
                 else:
                  day=int(input("which day do you choose:1.saturday\n2.sunday\n3.monday\n4.tuesday\n5.wednesday"))
                  time=int(input("which time do you choose:1.8_10\n2.10_12\n3.2_4\n4.4_6\n5.6_8"))
        #email=input("enter your email:")
                  day=day
                  time=time
                  day_time=str(day)+('.')+str(time)
                  with open("data_bodybulding2.csv",'r')as file:
                    reader=csv.reader(file)
                    matrix=list(reader)
                    #print(matrix)
                    for row in rows:
                     if matrix[time][day]!='reserved':
                       matrix[time][day]='reserved'
                       with open("data_bodybulding2.csv",'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerows(matrix)      
                 print("your reserve saved.thank you")
                 print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
                 with open("userss22.csv",'r')as file:
                     reader=csv.reader(file)
                     rows=list(reader)
                     for row in rows:
                         if row[1]==email:
                             row[8]=int(row[8])+600
                             with open("userss22.csv",'w',newline='')as file:
                                writer=csv.writer(file)
                                writer.writerows(rows)
                 with open("r_informations2.csv",'r')as file:
                     reader=csv.reader(file)
                     rows2=list(reader)
                     for row in rows2:
                         if row[1]==email:
                          
                          row[3]=day_time
                          row[5]=int(row[5])+600
                          with open("r_informations2.csv",'w',newline='')as file:
                             writer=csv.writer(file)
                             writer.writerows(rows2)
                 sighn_up_user()
        
    
    def cancel_reserve_s(self):
        email=input("enter your email for canceling reserve:")
        with open("r_informations2.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email:
                   if row[2]!='NR':
                       a=row[2].split('.')
                       print(a)
                       day=int(a[0])
                       time=int(a[1])
                       row[2]='NR'
                       row[5]=int(row[5])-450
                       with open("r_informations2.csv",'w',newline='')as file:
                             writer=csv.writer(file)
                             writer.writerows(rows)
                       with open("data_swim2.csv",'r')as file:
                           reader=csv.reader(file)
                           matrix=list(reader)
                           for row in rows:
                             if matrix[time][day]=='reserved':
                               matrix[time][day]='NR'
                               with open("data_swim2.csv",'w',newline='')as file:
                                 writer=csv.writer(file)
                                 writer.writerows(matrix)   
                       with open("userss22.csv",'r') as file:
                            reader=csv.reader(file)
                            rows=list(reader)
                            for row in rows:
                                 if row[1]==email:
                                    if int(row[8])>=450:
                                      row[8]=int(row[8])-450
                                    else:
                                      row[5]=int(row[5])+450
                                    with open("userss22.csv",'w',newline="")as file:
                                        writer=csv.writer(file)
                                        writer.writerows(rows)                                
                       print("your reservation canceld successfully!")
                   else:
                       print("you dont have any reservation in this day and time!")
                


    def cancel_reserve_a(self):         
         email=input("enter your email for canceling reserve:")
         with open("r_informations2.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email:
                   if row[2]!='NR':
                       a=row[4].split('.')
                       print(a)
                       day=int(a[0])
                       time=int(a[1])
                       row[4]='NR'
                       row[5]=int(row[5])-270
                       with open("r_informations2.csv",'w',newline='')as file:
                             writer=csv.writer(file)
                             writer.writerows(rows)
                       with open("data_aerobic2.csv",'r')as file:
                           reader=csv.reader(file)
                           matrix=list(reader)
                           for row in rows:
                             if matrix[time][day]=='reserved':
                               matrix[time][day]='NR'
                               with open("data_aerobic2.csv",'w',newline='')as file:
                                 writer=csv.writer(file)
                                 writer.writerows(matrix)     
                                 print("your reservation canceld successfully!")     
                       with open("userss22.csv",'r') as file:
                            reader=csv.reader(file)
                            rows=list(reader)
                            for row in rows:
                                 if row[1]==email:
                                    if int(row[8])>=270:
                                      row[8]=int(row[8])-270
                                    else:
                                      row[5]=int(row[5])+270
                                    with open("userss22.csv",'w',newline="")as file:
                                        writer=csv.writer(file)
                                        writer.writerows(rows)                                
                       print("your reservation canceld successfully!")
                   else:
                       print("you dont have any reservation in this day and time!")
                
    def cancel_reserve_b(self):
        email=input("enter your email for canceling reserve:")
        with open("r_informations2.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email:
                   if row[2]!='NR':
                       a=row[3].split('.')
                       print(a)
                       day=int(a[0])
                       time=int(a[1])
                       row[3]='NR'
                       row[5]=int(row[5])-600
                       with open("r_informations2.csv",'w',newline='')as file:
                             writer=csv.writer(file)
                             writer.writerows(rows)
                       with open("data_bodybulding2.csv",'r')as file:
                           reader=csv.reader(file)
                           matrix=list(reader)
                           for row in rows:
                             if matrix[time][day]=='reserved':
                               matrix[time][day]='NR'
                               with open("data_bodybulding2.csv",'w',newline='')as file:
                                 writer=csv.writer(file)
                                 writer.writerows(matrix)     
                                 print("your reservation canceld successfully!")
                       with open("userss22.csv",'r') as file:
                            reader=csv.reader(file)
                            rows=list(reader)
                            for row in rows:
                                 if row[1]==email:
                                    if int(row[8])>=600:
                                      row[8]=int(row[8])-600
                                    else:
                                      row[5]=int(row[5])+600
                                    with open("userss22.csv",'w',newline="")as file:
                                        writer=csv.writer(file)
                                        writer.writerows(rows)                                
                       print("your reservation canceld successfully!")
                   else:
                       print("you dont have any reservation in this day and time!")
                


    def payment(self):
        email=input("enter your email:")
        with open("userss22.csv",'r')as file:
            reader=csv.reader(file)
            rows=list(reader)
            for row in rows:
                if row[1]==email:
                 if row[7]=='ok':
                    pay=int(row[8])
                    print(f'your bill is {pay}$')
                    x=int(input("do you wanna pay?yes:1 no=else\n"))
                    if x==1:
                        if int(row[5]) > int(row[8])+10 :
                            print(f'you are in {row[0]} account')
                            pay=int(row[8])
                            row[5]=int(row[5])-int(row[8])
                            row[8]=0
                            with open("userss22.csv",'w',newline='')as file:
                                writer=csv.writer(file)
                                writer.writerows(rows)
                                print("payment was succesful! Thank You")
                            with open("supplement.csv",'r')as file:
                               reader=csv.reader(file)
                               rows=list(reader)
                               for row in rows:
                                  row[3]=int(row[3])+pay
                                  with open("supplement.csv",'w',newline='')as file:
                                     writer=csv.writer(file)
                                     writer.writerows(rows)
                                  
                            sighn_up_user()
                        else:
                            print("your account balance is not enogh!!")
                            sighn_up_user()
                    else:
                      sighn_up_user()
                 else:
                     print("you have to recharge your account first")
                     sighn_up_user()
               
                
                            

class person:
    def __init__(self,name,email,phone,password,wallet):
        self.name=name
        self.email=email
        self.phone=phone
        self.password=password
        self.wallet=wallet

    

    def sighn_up(self):
        fheader=['name','email','phone','password','supplement','wallet','change_pass','situation','bill']
       # self.name=input("enter your name:")
       # self.email=input("enter your email:")
       # self.phone=input("enter your phone number:")
        password_regex=r"^[a-zA-Z0-9!@#$%^&*()_+]{6}$"
        self.password=input("set a password for your account:")
        while not re.match(password_regex,self.password):
           print("your password should be 6digit!")
           self.password=input("set a password=")
        dict={"name":self.name , "email":self.email ,"phone":self.phone , "password":self.password,'supplement':'NA','wallet':0,'change_pass':'user','situation':'NW','bill':0}
        with open("userss22.csv","a",newline="") as file:
            File=csv.DictWriter(file , fieldnames=fheader)
            File.writerow(dict)
        fheader2=['name','email','rswim','rbodybulding','raerobic','bill']
        dict2={'name':self.name , 'email':self.email ,'rswim':'NR','rbodybulding':'NR','raerobic':'NR','bill':0}
        with open("r_informations2.csv",'a',newline='')as file:
           File=csv.DictWriter(file , fieldnames=fheader2)
           File.writerow(dict2)
           #File.writeheader()
           
        print("welcome to our comminuty:))")
        
    def login(self):
        #self.name=input("enter your name:")
        self.password=input("enter your password:")
        with open('userss22.csv','r')as file:
            reader=csv.reader(file)
            userss22={row[0]:row[3] for row in reader}
        if self.name in userss22 and userss22[self.name]==self.password:
           print("you have loged in successfuly!!")
           #s=int(input("if you wanna change your password click 0"))
         
        else:
            print("wrong information!!!\n\n")
            menu()

    def change_password(self):
      
       self.email=input("enter ur email")
       npass=int(input("enter your new password:"))
       with open("userss22.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==self.email:
                print(f'pasword was changed by the {row[6]} last time')
                row[3]=npass               
                row[6]='user'
              
                with open('userss22.csv','w',newline='')as file:
                     writer=csv.writer(file)
                     writer.writerows(rows)
       print("changes saved.")
       sighn_up_user()

    def change_password_m(self):
       email=input("enter the user email:")
       npass=int(input("enter the new password:"))
       with open("userss22.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email:
                print(f'pasword was changed by the {row[6]} last time')
                row[3]=npass                
                row[6]='maneger'              
                with open('userss22.csv','w',newline='')as file:
                     writer=csv.writer(file)
                     writer.writerows(rows)
       print("changes saved.")
       manger_access()

         
      
    def deposit(self,amount):
        self.wallet=amount
        self.email=input("enter ur email for add money to your wallet:")
        with open("userss22.csv",'r')as file:
            reader=csv.reader(file)
            rows=list(reader)
            for row in rows:
                if row[1]==self.email:
                    print(f"you are in {row[0]} account")
                    row[5]=int(row[5])+int(self.wallet)
                    self.wallet=row[5]
                    if self.wallet>=10:
                        row[7]='ok'
                    else:
                        print("your account balance is still not enough")
                        print("you should have at least 10$ in your wallet")
                    #self.wallet=row[5]
                #else:
                  #  print("wrong email")
                   # sighn_up_user()
        with open("userss22.csv",'w',newline='')as file:
            writer=csv.writer(file)
            writer.writerows(rows)
        #sighn_up_user()
        #print("your account balance:")
        #print(self.wallet)
        #sighn_up_user()
        #return self.wallet


    def withdraw(self,amount):
        
        self.email=input("enter ur email:")
       # if amount>self.wallet:
          #  print("insufficient balance!!")
       # else:
        self.wallet=amount
        with open("userss22.csv",'r')as file:
               reader=csv.reader(file)
               rows=list(reader)
               for row in rows:
                 if row[1]==self.email:
                    row[5]=int(row[5])-int(self.wallet)
                    self.wallet=row[5]
                    print(f'you are in {row[0]} account') 
                    if self.wallet<=10:
                        print("your balance is less than enough!!\nyou have to charge your wallet or your account wont work!")
                        k=int(input("1.charge account\n2.continue"))
                        if k==2:
                            with open("userss22.csv",'r')as file:
                              reader=csv.reader(file)
                              rows=list(reader)

                              for row in rows:
                                 if row[1]==self.email:              
                                  row[7]='NW'  

                                         
                            with open('userss22.csv','w',newline='')as file:
                                    writer=csv.writer(file)
                                    writer.writerows(rows)
                                    print("changes saved.")
                    '''if self.wallet<=10:
                        print("your balance is less than enough!!\nyou have to charge your wallet or your information will remove")
                        with open("userss2.csv",'r')as file:
                            reader=csv.reader(file)                           
                            lines=list()
                            for row in reader:
                                lines.append(row)
                                for field in row:
                                    if field==self.email:
                                        lines.remove(row)
                        with open('userss2.csv','w',newline='')as file:
                            writer=csv.writer(file)
                            writer.writerows(lines)'''
                 #else:
                 #   print("wrong email")
                 #   sighn_up_user()
        with open("userss22.csv",'w',newline='')as file:
              writer=csv.writer(file)
              writer.writerows(rows)
        #sighn_up_user()
            #print("you have"+str(self.wallet)+"$ in your wallet now\n\n")
            #sighn_up_user()

    
    '''def recharge(self,amount):
        self.wallet=amount
        self.email=input("enter ur email for add money to your wallet:")
        with open("userss2.csv",'r')as file:
            reader=csv.reader(file)
            rows=list(reader)
            for row in rows:
                if row[1]==self.email:
                    row[5]=int(row[5])+int(self.wallet)
                    self.wallet=row[5]
                    if self.wallet>10:
                        row[7]='ok'
                    else:
                        print("your account balance is still not enough!!")
                    #self.wallet=row[5]
                #else:
                  #  print("wrong email")
                   # sighn_up_user()
        with open("userss2.csv",'w',newline='')as file:
            writer=csv.writer(file)
            writer.writerows(rows)'''

    def balance(self):
          return int(self.wallet)
    def disscount(self):
        self.email=input("enter your email pleas:")
        with open("userss22.csv",'r')as file:
               reader=csv.reader(file)
               rows=list(reader)
               for row in rows:
                 if row[1]==self.email:
                    print(f"you are in {row[0]} account")
                    balance=int(row[5])
                    if balance>=650:
                        print("you have gold cart and you can have 50% disscount in your next class\n also you can get recommend for supplement of uour teacher free")
                        print("thank you for your accompaniment\n\n")
                        sighn_up_user()
                    elif 400<=balance<650:
                        print("you have silver cart and you can have 30% disscount in your next class")
                        print("thank you for your accompaniment\n\n")
                        sighn_up_user()
                    elif 300<=balance<400:
                        print("you have bronze cart and you can have 15% disscount in your next class")
                        print("thank you for your accompaniment\n\n")
                        sighn_up_user()
                    else:
                        print("unfortunatly you cant have disscount! for more information you can refer to information section in menue")
                        print("thank you for your accompaniment\n\n")
                        sighn_up_user()

    def check_account(self):
        self.email=input("enter your email:")
        with open("userss22.csv",'r')as file:
            reader=csv.reader(file)
            for row in reader:
                if row[1]==self.email:
                    print(f"you are in {row[0]} account")
                    print(f"account balance is {row[5]}$")
                    print(f"your bill is {row[8]}$")


    def supplement_p1(self):
        self.email=input("please enter your email:")
        with open("userss22.csv",'r')as file:
              reader=csv.reader(file)
              rows=list(reader)
              for row in rows:
                  if row[1]==self.email:
                      row[4]='requested'
        with open("userss22.csv",'w',newline='')as file:
              writer=csv.writer(file)
              writer.writerows(rows)
        print("your request saved!")
            #sighn_up_user()

    def supplement_p2(self):
            self.email=input("enter your email:")
            #print("supplement prices are 70$")
            #x2=input("If you wanna buy the recommended supplement pess 1(the money willtake from your wallet):")
            with open("userss22.csv",'r')as file:
                 reader=csv.reader(file)
                 rows=list(reader)
                 for row in rows:
                     if row[1]==self.email:
                        if row[4]!='NA' and row[4]!='requested':
                            sup=row[4]
                            print(f"your teacher recommend is {sup}")
                            row[4]='NA'
                            with open("userss2.csv",'w',newline='')as file:
                                writer=csv.writer(file)
                                writer.writerows(rows)             
                                     
                            sighn_up_user()
                        else:
                            print("you have to request for supplement first\n if you have requested wait for respond")
                            print("check the site some hours later.")
                            sighn_up_user()
             
            #sighn_up_user()
    

    def supplement_p3(self):
        self.email=input("enter your email:")
        self.password=input("enter your acccount password:")
        with open("userss22.csv",'r')as file:
            reader=csv.reader(file)
            rows=list(reader)
            for row in rows:
                if row[1]==self.email and row[2]==self.password:
                  if row[4]!='NA' and row[4]!='requested':
                      if row[7]=='ok':
                          if int(row[5])>=80:
                              sup=row[4]
                              print(f"you are in {row[0]} account")
                              s=int(row[5])-70
                              row[5]=int(row[5])-70
                              print(f'you are in {row[0]} account') 
                              print(f"your account balance is {s}$")
                              with open("userss22.csv",'w',newline='')as file:
                                writer=csv.writer(file)
                                writer.writerows(rows)    
                              with open("supplement.csv",'r')as file:
                                 reader=csv.reader(file)
                                 rows=list(reader)
                                 for row in rows:
                                    if sup=='sup1':
                                       row[0]=int(row[0])-1
                                       row[3]=int(row[3])+70
                                    elif sup=='sup2':
                                       row[1]=int(row[1])-1
                                       row[3]=int(row[3])+70
                                    elif sup=='sup3':
                                       row[2]=int(row[2])-1
                                       row[3]=int(row[3])+70
                                    with open("supplement.csv",'w',newline='')as file:
                                       writer=csv.writer(file)
                                       writer.writerows(rows)
                              sighn_up_user()
                          else:
                              print('your account balance is not enough!')
                              print("you should have 10$ at least in your account and the supplement price is 70$")
                              print("so you have to have at least 80$ in your wallet>")
                              sighn_up_user()
                      else:
                          print("you have to renew your membership.")
                          print("and for this you need to charge your wallet.")
                          sighn_up_user()
            
            sighn_up_user()
                       

                                     


                             
    def supplement_t(self):
        s=int(input("which supplement you wanna recommend?\n1.sup1\n2.sup2\n3.sup3\n"))
        if s==1 or s==2 or s==3:
          self.email=input("enter the user email:")
          
          with open("userss22.csv",'r')as file:
               reader=csv.reader(file)
               rows=list(reader)
               for row in rows:
                 if row[1]==self.email:                    
                    if s==1:
                      row[4]='sup1'
                    elif s==2:
                       row[4]='sup2'
                    elif s==3:
                       row[4]='sup3'
                 #else:
                 #   print("wrong email")
                 #   sighn_up_user()
          with open("userss22.csv",'w',newline='')as file:
              writer=csv.writer(file)
              writer.writerows(rows)
          print("thanks information saved!\n\n")
          sighn_up_teacher()
        else:
           sighn_up_teacher()

    def search_user(self):
        email=input("enter the user email:")
        with open("userss22.csv","r")as file:
            reader=csv.reader(file)
            for row in reader:
                if row[1]==email:
                    print(f"name:{row[0]}\nemail:{row[1]}\nphone number:{row[2]}\nsupplement:{row[4]}\nwallet balance:{row[5]}\nsituation:{row[7]}\nbill:{row[8]}$\n")
                   
                '''else:
                    print("wrong email!!")
                    manger_access()'''
    def search_user_t(self):
        email=input("enter ur email:")
        with open("userss22.csv","r")as file:
            reader=csv.reader(file)
            for row in reader:
                if row[1]==email:
                    print(f"name:{row[0]}\nemail:{row[1]}\nphone number:{row[2]}\nsupplement:{row[4]}")
class teacher:
     def __init__(self,name,email,resume,password):
         self.name=name
         self.email=email
         self.resume=resume
         self.password=password

     def sighnup(self):
         fheader=['name','email','resume','password','swim','bodybulding','aerobic']
        # self.name=input("please enter your name:")
        # self.phone=input("please enter your phone number:")
        #self.resume=input("tell us about your sport resume:")
         password_regex=r"^[a-zA-Z0-9!@#$%^&*()_+]{6}$"
         self.password=input("please set a password for ur account:")
         while not re.match(password_regex,self.password):
            print("wrong!your password should be 6 digit!!")
            self.password=input("enter your password:")

         
         dict2={'name':self.name ,'email':self.email,'resume':self.resume,'password':self.password , 'swim':'NA' , 'bodybulding':"NA",'aerobic':'NA'}
         with open("teacherss2.csv","a",newline="") as file:
            File=csv.DictWriter(file , fieldnames=fheader)
            File.writerow(dict2)
         print("welcome to our comminuty:))\n your informations have saved as a new teacher")

     def login(self):
        
        self.password=input("enter your password:")
        with open('teacherss2.csv','r')as file:
            reader=csv.reader(file)
            users={row[0]:row[3] for row in reader}
        if self.name in users and users[self.name]==self.password:
           print("you have loged in successfuly!!")
        else:
            print("wrong information!!!\n\n")
            menu()

     def change_password(self):
       self.email=input("enter ur email")
       npass=int(input("enter your new password:"))
       with open("teacherss2.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==self.email:
                row[3]=npass
              
                with open('teacherss2.csv','w',newline='')as file:
                     writer=csv.writer(file)
                     writer.writerows(rows)
       print("changes saved.")
       sighn_up_teacher()


     def search_teacher(self):
        email=input("enter the teacher email:").lower()
        with open("teacherss2.csv","r")as file:
            reader=csv.reader(file)
            for row in reader:
                if row[1]==email:
                    print(f"name:{row[0]}\nemail:{row[1]}\nresume:{row[2]}")
                    manger_access()
                '''else:
                    print("wrong email!!")
                    manger_access()'''
                
     def reserve_swim1(self):
         with open("data_swim1.csv",'r')as file:
            reader=csv.reader(file)
            matrix=list(reader)
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
         name=input("enter ur name:")
         email=input("enter your email:")
         with open("teacherss2.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email and row[0]==name:
                  day=int(input("which day do you choose:1.saturday\n2.sunday\n3.monday\n4.tuesday\n5.wednesday"))
                  time=int(input("which time do you choose:1.8_10\n2.10_12\n3.2_4\n4.4_6\n5.6_8"))
        #email=input("enter your email:")
                  day=day
                  time=time
                  day_time=str(day)+('.')+str(time)
                  with open("data_swim1.csv",'r')as file:
                    reader=csv.reader(file)
                    matrix=list(reader)
                    #print(matrix)
                    for row in rows:
                     if matrix[time][day]=='NA':
                       matrix[time][day]=name
                       with open("data_swim1.csv",'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerows(matrix)      
                  print("your reserve saved.thank you")
                  print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
                  with open("teacherss2.csv",'r')as file:
                     reader=csv.reader(file)
                     rows=list(reader)
                     for row in rows:
                         if row[1]==email:
                             row[4]=day_time
                             with open("teacherss2.csv",'w',newline='')as file:
                                writer=csv.writer(file)
                                writer.writerows(rows)
                   

     def reserve_bodybulding1(self):
        with open("data_bodybulding1.csv",'r')as file:
            reader=csv.reader(file)
            matrix=list(reader)
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
            name=input("enter ur name:")
            email=input("enter your email:")
        with open("teacherss2.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email and row[0]==name:
                  day=int(input("which day do you choose:1.saturday\n2.sunday\n3.monday\n4.tuesday\n5.wednesday"))
                  time=int(input("which time do you choose:1.8_10\n2.10_12\n3.2_4\n4.4_6\n5.6_8"))
        #email=input("enter your email:")
                  day=day
                  time=time
                  day_time=str(day)+('.')+str(time)
                  with open("data_bodybulding1.csv",'r')as file:
                    reader=csv.reader(file)
                    matrix=list(reader)
                    #print(matrix)
                    for row in rows:
                     if matrix[time][day]=='NA':
                       matrix[time][day]=name
                       with open("data_bodybulding1.csv",'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerows(matrix)      
                  print("your reserve saved.thank you")
                  print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
                  with open("teacherss2.csv",'r')as file:
                     reader=csv.reader(file)
                     rows=list(reader)
                     for row in rows:
                         if row[1]==email:
                             row[5]=day_time
                             with open("teacherss2.csv",'w',newline='')as file:
                                writer=csv.writer(file)
                                writer.writerows(rows)

     def reserve_aerobic1(self):
        with open("data_aerobic1.csv",'r')as file:
            reader=csv.reader(file)
            matrix=list(reader)
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
        name=input("enter ur name:")
        email=input("enter your email:")
        with open("teacherss2.csv",'r')as file:
           reader=csv.reader(file)
           rows=list(reader)
           for row in rows:
               if row[1]==email and row[0]==name:
                  day=int(input("which day do you choose:1.saturday\n2.sunday\n3.monday\n4.tuesday\n5.wednesday"))
                  time=int(input("which time do you choose:1.8_10\n2.10_12\n3.2_4\n4.4_6\n5.6_8"))
        #email=input("enter your email:")
                  day=day
                  time=time
                  day_time=str(day)+('.')+str(time)
                  with open("data_aerobic1.csv",'r')as file:
                    reader=csv.reader(file)
                    matrix=list(reader)
                    #print(matrix)
                    for row in rows:
                     if matrix[time][day]=='NA':
                       matrix[time][day]=name
                       with open("data_aerobic1.csv",'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerows(matrix)      
                  print("your reserve saved.thank you")
                  print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
                  with open("teacherss2.csv",'r')as file:
                     reader=csv.reader(file)
                     rows=list(reader)
                     for row in rows:
                         if row[1]==email:
                             row[6]=day_time
                             with open("teacherss2.csv",'w',newline='')as file:
                                writer=csv.writer(file)
                                writer.writerows(rows)

'''class sport:
    def __init__(self,sports,teachers,time):
        self.sports=sports
        self.teachers=teachers
        self.time=time
        f=open("sport.txt",'x')'''

class manager:
    def __init__(self):
      
        self.password=123456
        self.safety='rose'
        self.safety2='black'
    def supplement(self):
       fheader=['sup1','sup2','sup3','wallet']
       dict={'sup1':10,'sup2':10,'sup3':10,'wallet':0}
       with open ("supplement.csv",'a',newline='')as file:
          File=csv.DictWriter(file,fieldnames=fheader)
          File.writerow(dict)

    def check_s(self):
       with open("supplement.csv",'r')as file:
             reader=csv.reader(file)
             rows=list(reader)
             for row in rows:
                print(f"sup1={row[0]}\nsup2={row[1]}\nsup3={row[2]}\n\nwallet balance={row[3]}$\n")
                manger_access()
       
    def recharge(self):
      x=int(input("which supplement you wanna charge?\n1.sup1\n2.sup2\n3.sup3\n"))
      if x==1 or x==2 or x==3:
       if x==1:
          x2=int(input("how many sup1 you wanna order?"))
          money=x2*60
          with open("supplement.csv",'r')as file:
             reader=csv.reader(file)
             rows=list(reader)
             for row in rows:
                if int(row[3])>=money:
                  row[0]=int(row[0])+int(x2)
                  row[3]=int(row[3])-money
                  with open('supplement.csv','w',newline='')as file:
                     writer=csv.writer(file)
                     writer.writerows(rows)
                else:
                   print("accout balance is not enough!first charge the wallet")

       elif x==2:
          x2=int(input("how many sup1 you wanna order?"))
          money=x2*60
          with open("supplement.csv",'r')as file:
             reader=csv.reader(file)
             rows=list(reader)
             for row in rows:
                if int(row[3])>=money:
                  row[1]=int(row[11])+int(x2)
                  row[3]=int(row[3])-money
                  with open('supplement.csv','w',newline='')as file:
                     writer=csv.writer(file)
                     writer.writerows(rows)
                else:
                   print("accout balance is not enough!first charge the wallet")
       elif x==3:
          x2=int(input("how many sup1 you wanna order?"))
          money=x2*60
          with open("supplement.csv",'r')as file:
            #if row[0]!='sup1':
             reader=csv.reader(file)
             rows=list(reader)
             for row in rows:
                if int(row[3])>=money:
                  row[2]=int(row[2])+int(x2)
                  row[3]=int(row[3])-money
                  with open('supplement.csv','w',newline='')as file:
                     writer=csv.writer(file)
                     writer.writerows(rows)

    def charge_wallet(self):
       x=int(input("how much do you wanna charge the wallet?"))
       with open("supplement.csv",'r')as file:
          reader=csv.reader(file)
          rows=list(reader)
          for row in rows:
             row[3]=int(row[3])+int(x)
             with open("supplement.csv",'w',newline='')as file:
                writer=csv.DictWriter(file)
                writer.writerows(rows)
    def login(self):
      password=int(input("enter your password:"))
      if password==self.password:
          print("correct\nfor our safety please answer the question below\n")
          x2=input("what is the manager favorite flower?").lower()
          if x2==self.safety:
                print("correct!")
                manger_access()
          else:
             print("wrong!!\n\n")
             menu()
      else:
            print("wrong!\n\n")
            menu()

    def change_password(self):
       passw=input("enter ur past password:")
       
       if passw==self.password:
           x=input("for safety tell us what is your favorite color:").lower()
           if x==self.safety2:
            npass=int(input("enter your new password:"))
            self.password=npass
            manger_access()
           else:
               print("wrong!!")
               manger_access()
       else:
           print("wrong!!")
           manger_access()
    
    def remove_r_s(self):
        with open("data_swim2.csv",'r')as file:
            reader=csv.reader(file)
            matrix=list(reader)
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
            day=int(input("which day do you choose:1.saturday\n2.sunday\n3.monday\n4.tuesday\n5.wednesday"))
            time=int(input("which time do you choose:1.8_10\n2.10_12\n3.2_4\n4.4_6\n5.6_8"))
            with open("data_swim2.csv",'r')as file:
                    for row in matrix:
                     if matrix[time][day]=='reserved':
                       matrix[time][day]='NR'
                       with open("data_swim2.csv",'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerows(matrix)      
            print("you canceld reservation succesfully")
            print(tabulate(matrix,headers='firstrow',tablefmt='fancy_grid'))
             


        


def menu():
    role=int(input("choose your role:\n1:user\n2:teacher\n3:manager\n\nyour choice:"))
    if role==1:
        n=int(input("choose:\n1.sign up\n2.login\n"))
        name_regex=r"^[a-zA-Z0-9]+$"
        email_regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}\b"
        phone_regex=r"\d{6}"
        if n==1:
            name=input("enter your name:").lower()
            while not re.match(name_regex , name):
               print("your name can contain only letter and digit!try again")
               name=input("enter your name:").lower()
            email=input("enter your email:").lower()
            while not re.match(email_regex , email):
               print("wrong email!! please try again")
               email=input("enter your email:").lower()
            phone=input("enter your phone number:")
            while not re.match(phone_regex , phone):
               print("your phone number must be 6 digit!try again!!")
               phone=input("enter your phone number:")
            user=person(name,email,phone,'password','wallet')
            #reserv=reserve(name,email)

            user.sighn_up()
            #reserv.information()
            sighn_up_user()
        if n==2:
             name=input("enter your name:").lower()
             user2=person(name,'email','phone','password','wallet')
             user2.login()
             sighn_up_user()
            
             
       

    if role==2:
        m=int(input("1.sighn up\n2.login\n"))
        name_regex=r"^[a-zA-Z0-9]+$"
        email_regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if m==1:
          name=input("please enter your name:").lower()
          while not re.match(name_regex,name):
             print("your name can contain only letter andd digir!please try again!")
             name=input("enter your name:").lower()
          email=input("please enter your email:").lower()
          while not re.match(email_regex,email):
             print("wrong email!")
             email=input("enter your email:").lower()
          resume=input("tell us about your sport resume:").lower()
          teach=teacher(name,email,resume,'password')
          teach.sighnup()
          sighn_up_teacher()
        elif m==2:
           name=input("enter your name:").lower()
           teach2=teacher(name,'email','resume','password')
           teach2.login()
           sighn_up_teacher()


    if role==3:
       m=manager()
       m.login()
       ''' password=123456
        favf='rose'
        x=int(input("enter the password:"))
        if x==password:
            print("correct\nfor our safety please answer the question below\n")
            x2=input("what is the manager favorite flower?").lower()
            if x2==favf:
                print("correct!")
                man=manager(password,favf)
                manger_access()
            else:
             print("wrong!!\n\n")
             menu()
        else:
            print("wrong!\n\n")
            menu()'''
            


def sighn_up_user():
    n=int(input('\nenter :\n1. reserve\n2. cancle reseve\n3.change password\n4.wallet\n5.disscount\n6.supplement\n7.information\n8.back to main menu\n9.quit\n\n ur choice:'))
    #print("yyyyy")
    m = person(1,2,3,4,5)
    mm=reserve(1,2)
    if n==1:
        v=int(input("1.check classes\n2.reserve swimming class\n3.reserve aerobic class\n4.reserve budybulding class\n5.payment\n6.back\n\nur choice:"))
        if v==1:
            mm.check_class()
            sighn_up_user()
          
        if v==2:
            mm.reserve_swim()
        elif v==3:
            mm.reserve_aerobic2()
        elif v==4:
            mm.reserve_bodybulding()
        elif v==5:
            mm.payment()
        elif v==6:
            sighn_up_user()
        else:
            print("wrong!!")
            sighn_up_user()
    elif n==2:
        z=int(input("1.swim\n2.bodybulding\n3.aerobic\n4.back"))
        if z==1:
          mm.cancel_reserve_s()
          sighn_up_user()
        elif z==2:
            mm.cancel_reserve_b()
            sighn_up_user()
        elif z==3:
            mm.cancel_reserve_a()
            sighn_up_user()
        elif z==4:
            sighn_up_user()
        else:
            sighn_up_user()
    elif n==3:
        m.change_password()
    elif n==4:
       
        n2=int(input("1.deposit(recharge)\n2.withdraw\n3.check your account\n4.back\n\nur choice:"))
        if n2==1:
           amount=input("your wallet must be more that10$\nenter the amount of money you wanna pay:")
           m.deposit(amount)
           print("your account balance:")
           x=m.balance()
           print(x)
           sighn_up_user()
        elif n2==2:
            amount=int(input("enter the ammount of money you wanna get:"))
            m.withdraw(amount)
            print("your account balance:")
            x=m.balance()
            print(x)
            sighn_up_user()
        elif n2==3:
            m.check_account()
            sighn_up_user()
            '''elif n2==4:
            amount=int(input("enter the amount of money you wanna pay\nyour wallet must be more than 10$\n"))
            m.recharge(amount)
            print("your account balance:")
            x=m.balance()
            print(x)
            sighn_up_user()'''

        elif n2==4:
            sighn_up_user()

    elif n==5:
        m.disscount()

    elif n==6:
        b=int(input("1.request for supplement\n2.check recommended supplement\n3.buy the suplement\n4.back"))

        if b==1:
            m.supplement_p1()
            sighn_up_user()
        elif b==2:
            m.supplement_p2()
            sighn_up_user()
        elif b==3:
            m.supplement_p3()
            sighn_up_user()
        elif b==4:
           sighn_up_user()
            

    elif n==7:
        print("welcome to our academy. in our academy you can participate in swiming,bodybulding and aerobic classes.")
        print("the cost of classes is as follows.Also we have prepared discount cards for our users.")
        print("bodybulding:600$\nswimming:450$\nAerobic:270$")
        print("disscount :\n in our academi you can get disscount:")
        print("if your wallet balance is more than 650 you get gold cart which consider 50% disscount in your next class and a free supplement which you can get from your teacher")
        print("if your wallet balance is between 400-650 you get silver cart which consider 30% disscount in your next class ")
        print("and if your wallet balance is between 300-400 you get bronze cart which consider 15% disscount in your next class")
        print("the supplements dont have disscount.")
        print("\nCONTACT US:09129644802")
        print("\n\nproducer:Bahar Nazeri\t14016327919")
        print('\nIt make us happy to hear your comments and you criticisms:)')
        x=int(input("if you wanna send us a comment press1:"))
        if x==1:
            x2=input("your comment:")
            print("thank you for your openion.")
            x3=int(input("press a number 1-10:"))
            if x3==1 or x3==2 or x3==3 or x3==4 or x3==5 or x3==6 or x3==7 or x3==8 or x3==9 or x3==10:
                sighn_up_user()
        else:
            sighn_up_user()
        
    elif n==8:
        menu()
    elif n==9:
        while True:
            x=int(input("are u sure?click 1"))
            if x==1:
                break
            else:
                print("request canceled\n")
                sighn_up_user()
    


def sighn_up_teacher():
     n=int(input("\nchoose:\n1.reserve class\n2.supplement\n3.change password\n4.search users\n5.back to main menu\n6.quit\n\nyour choice:"))
     m=teacher(1,2,3,4)
     p=person(1,2,3,4,5)
     if n==1:
       r=int(input("1.reserve swimming\n2.reserve bodybulding\n3.reserve aerobic\n4.back"))
       if r==1:
           m.reserve_swim1()
           sighn_up_teacher()
           
       elif r==2:
           m.reserve_bodybulding1()
           sighn_up_teacher()

       elif r==3:
           m.reserve_aerobic1()
           sighn_up_teacher()

       elif r==4:
           sighn_up_teacher()

       else:
           print("wrong")
           sighn_up_teacher()

     elif n==2:      
        p.supplement_t()

     elif n==3:
        m.change_password()

     elif n==4:
         p.search_user_t()
         sighn_up_teacher()

     elif n==5:
         menu()

     elif n==6:
         while True:
             x=int(input('are u sure??click 0'))
             if x==0:
                 break
             else:
                 print("request cancled!\n")
                 sighn_up_teacher()

def manger_access():
    n=int(input("\nchoose:\n1.users information\n2.teachers information\n3.check classes\n4.check and edit reservs\n5.supple,ment\n6.back to main menu\n7.quit\n\nyour choice:"))
    m=manager()
    p=person(1,2,3,4,5)
    t=teacher(5,6,7,8)
    r=reserve(1,2)
    if n==1:
        n2=int(input("\n1.search users\n2.change user password\n3.check user wallet\n4.back\n"))
        if n2==1:
          p.search_user()
          manger_access()
        elif n2==2:
          p.change_password_m()
        elif n2==3:
            p.check_account()
            manger_access()
        elif n2==4:
            manger_access()
            
    elif n==2:
        print("\n1.search teacher\n")
        t.search_teacher()
    elif n==3:
        r.check_class()
        manger_access()
    elif n==4:
        x=int(input("1.check reservation\n2.cancel reservation\n3.back\n"))
        if x==1:
          n=int(input("1.swim\n2.bodybulding\n3.aerpbic\n4.back\n"))
          if n==1:
              print('ss')
          elif n==2:
              print("nn")
          elif n==3:
              print("mmm")
          elif n==4:
              manger_access()
        elif x==2:
            f=int(input("1.swim\n2.bodybulding\n3.aerobic\n4.back\n"))
            if f==1:
                m.remove_r_s()
                manger_access()
            elif f==2:
                print("uu")
                manger_access()
            elif f==3:
                manger_access()
            elif f==4:
                manger_access()
        elif x==3:
            manger_access()
        else:
            manger_access()
    elif n==5:
       p=int(input("1.recharge supplements\n2.recharge wallet\n3.check supplements\n4.back"))   
       if p==1:
          m.recharge()       
          manger_access()
       elif p==2:
          m.charge_wallet()
          manger_access()
       elif p==3:
          m.check_s()
          manger_access()
       elif p==4:
          manger_access()
       else:
          manger_access()
                

    elif n==6:
        menu()
        '''elif n==6:
        m.change_password()'''
    elif n==7:
         while True:
             x=int(input('are u sure??click 0'))
             if x==0:
                 break
             else:
                 print("request cancled!\n")
                 manger_access()

    
import unittest    
class testuser_login(unittest.TestCase):
    def login_user(self):
        user=person('bahar','67894','654321')
        self.assertEqual(user.sighn_up(),True)
    

#unittest.main()
#table1=tabulate(data)
#print(tabulate(data,headers='firstrow',tablefmt='fancy_grid'))
menu()




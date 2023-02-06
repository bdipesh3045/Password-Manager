from sqlalchemy import Integer,String,create_engine,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from font import font,thank
from prettytable import PrettyTable
import os
print(font)
data= declarative_base()
class Password_Manager(data):
    # __tablename__="User_data"
    # Sn_No=Column("Sn_No",Integer,autoincrement=True,primary_Key=True)
    # Site=Column("Site",String,unique=True)
    
    # Email=Column("Email",String)
    # password=Column("Password",String)
    # __table_args__ = {"sqlite_autoincrement": True}
    __tablename__="User_data"
    Sn_No=Column("Sn_No", Integer, primary_key=True)
    Site=Column("Site", String, unique=True)
    
    Email=Column("Email", String)
    Password=Column("Password", String)

    __table_args__ = {"sqlite_autoincrement": True}
    
    def __init__(self,Site,email,password):
        self.Site=Site
        self.Email=email
        self.Password=password
        
def clean():
    os.system('clear')
    print(font)  
    print("Press A to add data\nPress V to view the data\nPress S to print credentials from a specific site\nPress M to modify the data \nPress R to remove all the database\nPress Q to exit\n")
def end():
    os.system('clear')
    print(font) 
    print(thank)
    
        
db="sqlite:///manager.db"
engiene=create_engine(db)
data.metadata.create_all(bind=engiene)
Session=sessionmaker(bind=engiene)
session=Session()

def add_pw(Site,email,pw):
    with Session() as session:
            student=Password_Manager(Site,email,pw)
            session.add(student)
            session.commit()
    print("Data added correctly!")
a=True    
print("Press A to add data\nPress V to view the data\nPress S to print credentials from a specific site\nPress M to modify the data \nPress R to remove all the database\nPress Q to exit\n")

while a:
    value=input("Enter the command:").lower()
    if value=="a":
        clean()
        try:
            add_pw(input("Enter the  site from where the credentials belong:"),input("Enter your email or User-Id:"),input("Enter your password:"))
        except:
            print("You tried adding Duplicate data")
            
        
    elif value=="v":
        clean()
        # result = session.query(Password_Manager.Email).all()
        # email=[i for i in result]
        # y=[x for x in email]
        # print(y)
        result = session.query(Password_Manager).all()

        table = PrettyTable(['Sn_No', 'Site', 'Email', 'Password'])
        for i in result:
            
            table.add_row([i.Sn_No, i.Site, i.Email, i.Password])

        print(table)
        
    elif value=="s":
        clean()
        try:
            site = input("Enter the name of site:")
            result = session.query(Password_Manager).filter_by(Site=site).all()

            table = PrettyTable(['Sn_No', 'Site', 'Email', 'Password'])
            for i in result:
                table.add_row([i.Sn_No, i.Site, i.Email, i.Password])

            print(table)
        except:
            print("Sorry you mispelled the Site name!")
        
    elif value=="r":
        clean()
        print("Are you sure you want to delete Database?\nif you are sure write yes:")
        if input("Enter your choice:").lower()=="yes":
            
            data.metadata.drop_all(engiene)
            data.metadata.create_all(engiene)
            print("Database reset succesull!")
    elif value=="q":
        end()
        os._exit(0)
    elif value=="m":
        clean()
        record = session.query(Password_Manager).filter(Password_Manager.Site == input("Enter the site name:").lower()).first()
        record.Email =input("Enter the new Email")
        record.Password = input("Enter the new password")
        session.commit()
        print("Data updated!")
        
    else:
        print("Invalid command recieved!")

        
 

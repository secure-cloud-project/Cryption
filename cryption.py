from array import array
import os
from cryptography.fernet import Fernet,InvalidToken
class Encryption:
    fernet = ""
    data = ""
    key = ""
    key_file_name = ""

    def __init__(self,arg,data):
        self.key_file_name = "key.key"
        if arg=="n":
            self.create_key()
        self.data = data
        self.load_key()
        self.fernet = Fernet(self.key)
        
    def create_key(self):
        self.key = Fernet.generate_key()
        self.write_key()

    def write_key(self):    
        file_path = os.path.dirname(os.path.realpath(__file__))+"\\"+str(self.key_file_name)
        with open(file_path, "wb") as key_file:
            key_file.write(self.key)

    def load_key(self):
        file_path = os.path.dirname(os.path.realpath(__file__))+"\\"+str(self.key_file_name)
        self.key = open(file_path, "rb").read()
    
    def encrypt_data(self):
        self.data = self.fernet.encrypt(self.data.encode())
    def decrypt_data(self):
        self.data = self.fernet.decrypt(self.data)

    def get_data(self):
        return self.data

class FileEncyrption(Encryption):

    file_location_name = ""
    file = ""

    def __init__(self,file_name):
        self.file_location_name = file_name
        self.key_file_name = "key.key"
        self.load_key()
        self.fernet = Fernet(self.key)

    

    def read_file(self):
        if self.file_location_name=="":
            return
        try:
            file_path = os.path.dirname(os.path.realpath(__file__))+"\\"+str(self.file_location_name)
            with open(file_path, "rb") as file:
                self.file = file.read()
        except TypeError:
            print("{} is not location".format(self.file_location_name))        

    def read_files(self):
        if self.file_location_name=="":
            return
        file_path = os.path.dirname(os.path.realpath(__file__))+"\\"+str(self.file_location_name)
        for file in os.listdir(file_path):
            with open("{}\\{}".format(file_path,file),'rb') as original_file:
                self.file.append(original_file.read())


    def write_file(self):
        if self.file_location_name=="":
            return
        try:
            file_path = os.path.dirname(os.path.realpath(__file__))+"\\"+str(self.file_location_name)
            with open(file_path, "wb") as file:
                file.write(self.file)
        except TypeError:
            print("{} is not location".format(self.file_location_name)) 
    
    def write_files(self):
        if self.file_location_name=="":
            return
        
        file_path = os.path.dirname(os.path.realpath(__file__))+"\\"+str(self.file_location_name)
        i=0
        for file in os.listdir(file_path):
            with open("{}\\{}".format(file_path,file),'wb') as original_file:
                original_file.write(self.file[i])
            i+=1    
        
       

      
    def encrypt_file(self):
        self.read_file()
        self.file = self.fernet.encrypt(self.file)
        self.write_file()
            
        
            

    def decrypt_file(self):
        
        try:
            self.read_file()
            self.file= self.fernet.decrypt(self.file)
            self.write_file()
        except InvalidToken:
            print("not encrypted")
        except TypeError:
            print("not encrypted")
        

    
   

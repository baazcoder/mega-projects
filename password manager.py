import time
from cryptography.fernet import Fernet

'''
def write_key():
   key = Fernet.generate_key()
   with open('key.key', 'wb') as key_file:
      key_file.write(key)
                           '''

def load_key():
   with open('key.key', 'rb') as f:
      key = f.read()  
   return key


key = load_key() 
fer = Fernet(key)
time.sleep(1)

# key + password + text to encrypt = random text
# random text + key + password = text to encrypt


def view():
   with open('password.txt', 'r') as f:
      for line in f.readlines():
        data = line.rstrip()
        user,pwd = data.split('|')
        decrypted_pwd = fer.decrypt(pwd.encode()).decode()
        print(f"user: {user} | password: {decrypted_pwd}")

def add():
   username = input('account name: ')
   pwd = input('password: ')
   encrypted_pwd = fer.encrypt(pwd.encode()).decode()
   with open('password.txt', 'a') as f:
      f.write(f'{username}|{encrypted_pwd}\n')
   print("Credentials saved successfully!")
      

while True:
 mode = input('would to like to add a new pass or wanna view existing one?? (add/view). Q to back:\n').lower()
 if mode == 'view':
     view()
 elif mode == 'q':
    quit
 elif mode == 'add':
     add()
 else:
     print('invalid option!')
     continue
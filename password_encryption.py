from cryptography.fernet import Fernet

#key + password + text to encrypt = random text
#random text + key + password = text to encrypt
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()#read file
    file.close()#close file
    return key

master_pwd = input("What is your password? ")
key = load_key() + master_pwd.encode() #converting master pwd to bytes and adding it to the key
fer = Fernet(key)#initalizating the cryptography moduel

def view():
    with open('passwords.txt', 'r') as f:#creating/opening a file with closes file, open(filename, mode(a,w,r)) as file
        for line in f.readlines():#getting all the lines in the file
            data = line.rstrip()#removing the \n of the add line
            user, passw = data.split("|")#splitting the '|' string or character, return a list format, user is set to the first element in the list and passw is the second
            print("User:", user,", Password:", fer.decrypt(passw.encode()).decode())
            

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:#creating/opening a file with closes file, open(filename, mode(a,w,r)) as file
        f.write(name +"|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones?(add, view) press q to quit: ").lower()
    if mode == 'q':
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid")
        continue

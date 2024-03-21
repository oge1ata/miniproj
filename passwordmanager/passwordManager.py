from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.passwordFile = None
        self.passwordDict = {}
    
    def createKey(self, path):
        self.key = Fernet.generate_key()
        self.passwordFile = open(path, "wb")
        self.passwordFile.write(self.key)
        self.passwordFile.close()
        # with open(path, "wb") as f:
        # f.write(self.key)
    
    def loadKey(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()
    
    def createPasswordFile(self, path, initialValues=None):
        self.passwordFile = path

        if initialValues is not None:
            for key, value in initialValues.items():
                self.addPassword(key, value)
    
    def loadPasswordFile(self, path):
        self.passwordFile = path

        with open(self.password, 'r') as f:
            for line in f:
                site, encrypted = line.split(':')
                self.passwordDict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def addPassword(self, site, password):
        self.passwordDict[site] = password

        if self.passwordFile is not None:
            with open(self.passwordFile, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ':' + encrypted.decode() + '\n')
    
    def getPassword(self, site):
        return self.passwordDict[site]
         

def main():
    password = {
        "email": "PasswordManager@gmail.com",
        "facebook": "yuio1221221",
        "twitter": "224whncjn42244",
        "youtube": "0909090juwnj"
    }

    pm = PasswordManager()

    print("""What do you want to do
          1 Create a new key
          2 Load an existing key
          3 Create a new password file
          4 Load an existing password file
          5 Add a new password
          6 Get a password
          7 Exit
          """)

    done = False

    while not done:
        choice = int(input("Enter your choice: "))
        # try:
        #     choice = int(input("Enter your choice: "))
        # except ValueError:
        #     print("Please enter a number")
        #     continue
        if choice == 1: # create
            path = input("Enter your path: ")
            pm.createKey(path)
        elif choice == 2: # load
            path = input("Enter your path: ")
            pm.loadKey(path)
        elif choice == 3: # create
            path = input("Enter your path: ")
            pm.createPasswordFile(path, password)
        elif choice == 4: # load
            path = input("Enter your path: ")
            pm.loadPasswordFile(path)
        elif choice == 5: # add
            site = input("Enter your site: ")
            password = input("Enter your password: ")
            pm.addPassword(site, password)
        elif choice == 6: # get
            site = input("Enter your site: ")
            print(f'Password for {site} is {pm.getPassword(site)}')
        elif choice == 7: # exit
            done = True
            print('Okay Bye!')
        else:
            print("Please enter a number")

if __name__ == '__main__':
    main()
    

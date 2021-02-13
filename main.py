import random, string
from colorama import init, Fore
import webbrowser


print(Fore.GREEN + '''
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝ 
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗ 
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
''')
print("It will only generate nitro for you, you need checker to check them find them online.\n")
print("We do not allow copies of this generator, we don't recommend making a video on it, we will take it down.\n")
input("Press enter if you agree to this, program will start\n")


num=input('Input How Many Codes to Generate: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print(Fore.BLUE + 'Wait, Generating for you!')
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")
       

print(Fore.CYAN + 'Successfully, generated they are in Nitro Codes.txt"')           
input("Press Enter To Close!")

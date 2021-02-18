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


num = input('Input How Many Codes to Generate: ')
charSet = f"{string.ascii_uppercase}{string.digits}{string.ascii_lowercase}"
bigStr = ""

with open("Nitro Codes.txt","w", encoding='utf-8') as file:

    print(f'{Fore.BLUE}Wait, Generating for you!')

    for i in range(int(num)):
        bigStr += f'https://discord.gift/{"".join(random.choices(charSet, k = 16))}\n'
        if i % 100_000 == 0:
            file.write(f'{bigStr}\n')
            bigStr = ""


    print(f'{Fore.CYAN}Successfully, generated they are in Nitro Codes.txt"')
    input("Press Enter To Close!")

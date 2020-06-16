import random, string
import webbrowser

print("Benz, Nitro Code Generator! ")
print("Thank you for using it!\n\n\n")

num=input('Input How Many Codes to Generate: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Wait, Generating for you!")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()
input("\n\nFinished, Press enter to exit. Codes saved in Nitro Codes")

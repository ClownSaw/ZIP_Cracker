#!/usr/bin/python3
#Autor: ClownSaw
#Web: www.clownsaw.tk
from colorama import init, Fore
import zipfile, sys, random, time, os

#colores colorama
BLUE = Fore.BLUE
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
RESET = Fore.RESET

init()

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

def ClownLogo():
    from colorama import init, Fore
    import sys, random, time
    init()
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """


╔═╗╦╔═╗ + * #                   
╔═╝║╠═╝      * # +               
╚═╝╩╩         * # +             
 + # *  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
   + #  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
      + ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
            Autor: ClownSaw
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

def usage():
    print(f"{RED}usage {BLUE}: {GREEN}pdf_cracker.py [example.pdf] [wordlist.txt]{RESET}")

ClownLogo()

count = 1

try:
    zip_file = sys.argv[1]

    wordlist = sys.argv[2]
except:
	usage()
	exit()

try:	
    with open(wordlist,'rb') as text:
        for entry in text.readlines():
            password = entry.strip()
            try:
                with zipfile.ZipFile(zip_file,'r') as zf:
                    zf.extractall(pwd=password)

                    data = zf.namelist()[0]

                    data_size = zf.getinfo(data).file_size

                    print(f'   {GREEN}[{RED}+{GREEN}] Password Found!! : {BLUE}'+password.decode('utf8'))
                    break

            except:
                number = count
                print(f'{GREEN}[{CYAN}{number}{GREEN}]{RESET}', f'{BLUE}Password failed!: {RED}'+password.decode('utf8'))
                count += 1
                pass
except:
	print("")
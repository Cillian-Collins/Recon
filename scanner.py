#############################################################################
#                                                                           #
#                                  Created By                               #
#                                Cillian Collins                            #
#                       https://github.com/Cillian-Collins                  #
#                                                                           #
#############################################################################

import argparse, sys, requests, time, threading
if sys.version[0]=="3": raw_input=input
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', help='Config file.', required=True)
args = parser.parse_args()
arrayList = []
with open(args.f, 'r') as f:
    for line in f:
        arrayList.append(line.strip())

class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def start(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        self.busy = False
        time.sleep(self.delay)

print ("+--------------------------------------------+")
print ("|               Recon Scanner                |")
print ("|    https://github.com/Cillian-Collins      |")
print ("+--------------------------------------------+")

print("   .:'                                `:.")
print("  ::'                                   `::")
print(" :: :.                                 .: ::")
print("  `:. `:.             .             .:'  .:'")
print("   `::. `::           !           ::' .::'")
print("       `::.`::.    .' ! `.    .::'.::'")
print("         `:.  `::::'':!:``::::'   ::'")
print("         :'*:::.  .:' ! `:.  .:::*`:")
print("        :: HHH::.   ` ! '   .::HHH ::")
print("       ::: `H TH::.  `!'  .::HT H' :::")
print("       ::..  `THHH:`:   :':HHHT'  ..::")
print("       `::      `T: `. .' :T'      ::'")
print("         `:. .   :         :   . .:'")
print("           `::'               `::'")
print("             :'  .`.  .  .'.  `:")
print("             :' ::.       .:: `:")
print("             :' `:::     :::' `:")
print("              `.  ``     ''  .'")
print("               :`...........':")
print("               ` :`.     .': '")
print("                `:  `""'''  :'")

count = 0
countFound = 0
website = 0
spinner = Spinner()
alive = requests.Session()
alive.max_redirects = 2
while True:
    website = ('http://www.' + raw_input('URL: http://www.'))
    try:
        res = alive.get(website, timeout = 2)
        res.status_code == 200
        break
    except:
        print("Sorry, that website can't be scanned.")
        pass
for item in arrayList:
    spinner.start()
    try:
        r = alive.get(website + item, timeout = 2)
    except requests.exceptions.RequestException:
        count += 1
    if str(r.status_code) == str(404):
        count += 1
    else:
        spinner.stop()
        print (str(r.status_code) + " | " + str(item))
        countFound += 1
    spinner.stop()
print ("#------------------------------------------------#")
print ("Found a total of " + str(countFound) + " pages.")
print ("Ignoring " + str(count) + " 'Page Not Found' errors.")
print ("#------------------------------------------------#")
raw_input("Press enter to exit.")

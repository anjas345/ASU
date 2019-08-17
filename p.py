#import module
import os,sys,time

#Menu
def menu():
        os.system('clear')
        print "            Code With Love By 4njas "
        print "                 Tools Instaler   "
        print " "
        print " 1.Asu Toolkit v.3 "
        print " 2.sedang perbaikan"
        pilih()

#pilih

def pilih():
                p = raw_input("pilih > ")
                if  p == "":
                              print " Jangan kosong "
                              pilih()
                elif p == "1":
                              os.system('clear')
                              os.system('figlet - Anjas "Gans" ')
                              os.system('pkg install python2 git -y ')
                              os.system('pip2 install requests')
                              os.system('pip2 install mechanize')
                              os.system('git clone https://github.com/Gh0stroot/asu')
                              print "Tools terinstall"
                              print "silahkan ketik ls"
                              sys.exit()                         
                
menu()                      
                             
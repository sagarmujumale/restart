#!/usr/bin/python

import sys, getopt

def main(argv):
   ENV = ''
   ACCESS = ''
   SECRET = ''
   try:
       opts, args = getopt.getopt(argv,"he:a:s:",["efile=","afile=", "sfile"])
   except getopt.GetoptError:
      print 'test.py -e <environment> -a <aws-access-key> -s <aws-secret-key>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -e <environment> -a <aws-access-key> -s <aws-secret-key>'
         sys.exit()
      elif opt in ("-e", "--efile"):
         ENV = arg
      elif opt in ("-a", "--afile"):
         ACCESS = arg
      elif opt in ("-s", "--sfile"):
         SECRET = arg
   print 'ENVIRONMWNT is "', ENV
   print 'AWS-ACCESS-KEY is "', ACCESS
   print 'AWS-SECRET-KEY is "', SECRET
   acc = 'aws_access_key_id: ' + ACCESS
   sec = 'aws_secret_access_key: ' + SECRET 
   with open("restart/vars/main.yml", "a") as file_object:
      file_object.write("\n")
      file_object.write(acc)
      file_object.write("\n")
      file_object.write(sec)
      if ENV == 'prf'
         print 'Stopping AWS instanes for PRF environment'
      elif ENV == 'prv'
         print 'Stopping AWS instanes for PRV environment'
      elif ENV == 'dev'
         print 'Stopping AWS instanes for DEV environment'
      elif ENV == 'all'
         print 'Stopping AWS instanes for ALL environment'

if __name__ == "__main__":
   main(sys.argv[1:])

#!/usr/bin/python

import sys, getopt, os
def prf():
  file1 = open('restart/files/prf', 'r')
  print 'Stopping AWS instanes for PRF environment'
  count = 0
  for line in file1:
    count += 1
    print(line.strip())
    with open("restart/vars/main.yml", "r") as f:
      filedata = f.read()
    filedata = filedata.replace('aws-inst', line.strip())
    with open('restart/vars/main.yml', 'w') as f:
      f.write(filedata)
    cmd = 'ansible-playbook restart.yml'
    cmd2 = 'cp restart/files/variable restart/vars/main.yml '
    os.system(cmd)
    os.system(cmd2)
  file1.close()

def prv():
  file1 = open('restart/files/prv', 'r')
  print 'Stopping AWS instanes for PRV environment'
  count = 0
  for line in file1:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
  file1.close()

def dev():
  file1 = open('restart/files/dev', 'r')
  print 'Stopping AWS instanes for DEV environment'
  count = 0
  for line in file1:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
  file1.close()


def everything():
  prf()
  prv()
  dev()

def main(argv):
  ENV = ''
  ACCESS = ''
  SECRET = ''
  try:
    opts, args = getopt.getopt(argv,"he:a:s:",["efile=","afile=", "sfile"])
  except getopt.GetoptError:
    print 'test.py -e <environment> -a <aws-access-key> -s <aws-secret-key> '
    sys.exit(4)
  for opt, arg in opts:
    if opt == '-h':
      print 'test.py -e <environment> -a <aws-access-key> -s <aws-secret-key> '
      sys.exit()
    elif opt in ("-e", "--efile"):
      ENV = arg
    elif opt in ("-a", "--afile"):
      ACCESS = arg
    elif opt in ("-s", "--sfile"):
      SECRET = arg
  print 'ENVIRONMWNT is :- ', ENV
  print 'AWS-ACCESS-KEY is :- ', ACCESS
  print 'AWS-SECRET-KEY is :-', SECRET
  acc = 'aws_access_key_id: ' + ACCESS
  sec = 'aws_secret_access_key: ' + SECRET 
  with open("restart/vars/main.yml", "a") as file_object:
    file_object.write("\n")
    file_object.write(acc)
    file_object.write("\n")
    file_object.write(sec)
    file_object.write("\n")
  cmd1 = 'cp restart/vars/main.yml restart/files/variable'
  os.system(cmd1) 
  if ENV == 'prf':
    print 'Stopping AWS instanes for PRF environment'
    prf()
  elif ENV == 'prv':
    prv()
  elif ENV == 'dev':
    dev()
  elif ENV == 'all':
      everything()

if __name__ == "__main__":
   main(sys.argv[1:])

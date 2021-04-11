#!/usr/bin/python

import sys, argparse, os
def prf():
  file1 = open('stop/files/prf', 'r')
  print 'Stopping AWS instanes for PRF environment'
  count = 0
  for line in file1:
    count += 1
    print(line.strip())
    with open("stop/vars/main.yml", "r") as f:
      filedata = f.read()
    filedata = filedata.replace('awsinst', line.strip())
    with open('stop/vars/main.yml', 'w') as f:
      f.write(filedata)
    cmd = 'ansible-playbook stop.yml'
    cmd2 = 'cp stop/files/variable stop/vars/main.yml '
    os.system(cmd)
    os.system(cmd2)
  file1.close()

def prv():
  file1 = open('stop/files/prv', 'r')
  print 'Stopping AWS instanes for PRV environment'
  count = 0
  for line in file1:
    count += 1
    print(line.strip())
    with open("stop/vars/main.yml", "r") as f:
      filedata = f.read()
    filedata = filedata.replace('awsinst', line.strip())
    with open('stop/vars/main.yml', 'w') as f:
      f.write(filedata)
    cmd = 'ansible-playbook stop.yml'
    cmd2 = 'cp stop/files/variable stop/vars/main.yml '
    os.system(cmd)
    os.system(cmd2)
  file1.close()

def dev():
  file1 = open('stop/files/dev', 'r')
  print 'Stopping AWS instanes for DEV environment'
  count = 0
  for line in file1:
    count += 1
    print(line.strip())
    with open("stop/vars/main.yml", "r") as f:
      filedata = f.read()
    filedata = filedata.replace('awsinst', line.strip())
    with open('stop/vars/main.yml', 'w') as f:
      f.write(filedata)
    cmd = 'ansible-playbook stop.yml'
    cmd2 = 'cp stop/files/variable stop/vars/main.yml '
    os.system(cmd)
    os.system(cmd2)
  file1.close()

def everything():
  prf()
  prv()
  dev()

def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument("env")
  parser.add_argument("key")
  parser.add_argument("secret")
  parser.add_argument("token")
  args = parser.parse_args()
#  print('ENVIRONMWNT is :- ' + args.env)
#  print('AWS-ACCESS-KEY is :- ' + args.key)
#  print('AWS-SECRET-KEY is :-' + args.secret)
#  print('AWS-SESSION-TOKEN is :-' + args.token)
  acc = 'aws_access_key_id: ' + args.key
  sec = 'aws_secret_access_key: ' + args.secret
  tok = 'aws_session_token: ' + args.token 
  with open("stop/vars/main.yml", "a") as file_object:
    file_object.write("\n")
    file_object.write(acc)
    file_object.write("\n")
    file_object.write(sec)
    file_object.write("\n")
    file_object.write(tok)
    file_object.write("\n")
  cmd1 = 'cp stop/vars/main.yml stop/files/variable'
  os.system(cmd1) 
  if args.env == 'prf':
    prf()
  elif args.env == 'prv':
    prv()
  elif args.env == 'dev':
    dev()
  elif args.env == 'all':
    prf()
    prv()
    dev()

if __name__ == "__main__":
   main(sys.argv[1:])

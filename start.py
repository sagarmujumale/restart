#!/usr/bin/python

import sys, argparse, os
def prf():
  file1 = open('start/files/prf', 'r')
  print 'Starting AWS instanes for PRF environment'
  count = 0
  for line in file1:
    count += 1
    print(line.strip())
    with open("start/vars/main.yml", "r") as f:
      filedata = f.read()
    filedata = filedata.replace('awsinst', line.strip())
    with open('start/vars/main.yml', 'w') as f:
      f.write(filedata)
    cmd = 'ansible-playbook start.yml'
    cmd2 = 'cp start/files/variable start/vars/main.yml '
    os.system(cmd)
    os.system(cmd2)
  file1.close()

def prv():
  file1 = open('start/files/prv', 'r')
  print 'Starting AWS instanes for PRV environment'
  count = 0
  for line in file1:
    count += 1
    print(line.strip())
    with open("start/vars/main.yml", "r") as f:
      filedata = f.read()
    filedata = filedata.replace('awsinst', line.strip())
    with open('start/vars/main.yml', 'w') as f:
      f.write(filedata)
    cmd = 'ansible-playbook start.yml'
    cmd2 = 'cp start/files/variable start/vars/main.yml '
    os.system(cmd)
    os.system(cmd2)
  file1.close()

def dev():
  file1 = open('start/files/dev', 'r')
  print 'Stopping AWS instanes for DEV environment'
  count = 0
  for line in file1:
    count += 1
    print(line.strip())
    with open("start/vars/main.yml", "r") as f:
      filedata = f.read()
    filedata = filedata.replace('awsinst', line.strip())
    with open('start/vars/main.yml', 'w') as f:
      f.write(filedata)
    cmd = 'ansible-playbook start.yml'
    cmd2 = 'cp start/files/variable start/vars/main.yml '
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
  with open("start/vars/main.yml", "a") as file_object:
    file_object.write("\n")
    file_object.write(acc)
    file_object.write("\n")
    file_object.write(sec)
    file_object.write("\n")
    file_object.write(tok)
    file_object.write("\n")
  cmd1 = 'cp start/vars/main.yml start/files/variable'
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

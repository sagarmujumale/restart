import os
import socket

def playbook():
  cmd = 'ansible-playbook gitlab.yml'
  os.system(cmd)


def __main__():
  export AWS_ACCESS_KEY_ID='AK123'
  export AWS_SECRET_ACCESS_KEY='abc123'
  keeper = None
    keeper = raw_input("Enter your choice:- ").lower()
    if keeper in yes:
      print("Installation has been started......")
      playbook()
      break
    if keeper in no:
      cert()
      cert_key()
      playbook()
      break
    else:
      print(" Invalid choice... Please enter yes or no.")

__main__()

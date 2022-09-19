#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import re
import subprocess
import os



### HELPER FUNCTIONS (IF NECESSARY) ###
z = 0


print("Welcome to the quick and simple text-based Firewall Builder!")
print("For this program to work, it needs to be run as Administrator.")
print("If you did not run this program as Administrator, please exit and run it as Administrator")
print("You may type 'EXIT' at any time to close the program.")
print("We'll need to get some information from you to start.")
def ufw_maker(argv):
  result = ""
  rule1 = ""
  rule2 = ""
  rule3 = ""
  rule4 = ""
  rule5 = ""
  action = ""
  with open('/tmp/script.sh', 'w') as f:
    f.write(rule1)
  print("Here are the current firewall rules.")
  subprocess.call(["sudo", "ufw", "status", "numbered"])
  while action != "add" or action != "remove":
    action = input("Do you want to ADD or REMOVE a rule?\n").lower()
    if action == "exit":
      os.system('rm /tmp/script.sh')
      return
    if action == "add" or action == "remove":
      break
    
  
  if action == "add":
    while rule1 != 0:
      rule1 = input("Do you want to ALLOW, DENY, or DROP traffic?\n").lower()
      if rule1 == "exit":
        os.system('rm /tmp/script.sh')
        return
      if rule1 == "allow" or rule1 == "deny" or rule1 == "drop":
        break
    while rule2 != 0:
      rule2 = input("Is this applicable to INcoming or OUTgoing traffic (Respond with 'IN' or 'OUT')\n").lower()
      if rule2 == "exit":
        os.system('rm /tmp/script.sh')
        return
      if rule2 == 'in' or rule2 == 'out':
        break 
    while rule3 != 0:    
      rule3 = input("What IP Address should this rule apply to? (Respond with 'ANY' for all IP Addresses)\n").lower()
      x = re.findall(r"\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}", rule3)
      y = re.findall(r"\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}/24", rule3)
      if rule3 == "exit":
        os.system('rm /tmp/script.sh')
        return
      if x != [] or rule3 == "" or rule3 == "any" or y != []:
        break
    while rule4 != 0:      
      rule4 = input("Which port number (if any) should this rule apply to? (Respond with 'NONE' for no specific port or 'ALL' for all ports)\n").lower()
      y = re.findall(r"\d{1,5}", rule4)
      if rule4 == "exit":
        os.system('rm /tmp/script.sh')
        return
      if rule4 == "none" or rule4 == "all":
        rule4 = ""
        break
      if y != []:
        rule4 = y[0] 
        break
      elif rule4 == "":
        0 == 0
        break  
    if rule4 != "":
      while rule5 != 0:
        rule5 = input("TCP or UDP?\n").lower()
        if rule5 == "exit":
          os.system('rm /tmp/script.sh')
          return
        if rule5 == "tcp" or rule5 == "udp":
          break
         

    print("Thank you.")
       
  elif action == "remove":
    delete = input("Which number rule would you like to remove?\n")
    if delete == "exit":
      os.system('rm /tmp/script.sh')
      return

  if result == "" and action == 'add':
    if rule4 == "":
      with open('/tmp/script.sh', 'w') as f:
        f.write('sudo ' + 'ufw ' + str(rule1) + ' ' + str(rule2) + ' from ' + str(rule3))
    elif rule4 != "":
      with open('/tmp/script.sh', 'w') as f:
         f.write('sudo ' + 'ufw ' + str(rule1) + ' ' + str(rule2) + ' from ' + str(rule3) + " " + "proto" + " " + str(rule5) + " port " + str(rule4))
  
    os.chmod("/tmp/script.sh", 0o775)
    os.system('/tmp/script.sh')
    os.system('rm /tmp/script.sh')
  elif result == "" and action == 'remove':
    with open('/tmp/script.sh', 'w') as f:
      f.write('sudo ' + 'ufw ' + 'delete ' + str(delete))
  
    os.chmod("/tmp/script.sh", 0o775)
    os.system('/tmp/script.sh')
    os.system('rm /tmp/script.sh')

  cont = input("Do you wish to add/remove another rule? (y|n)\n").lower()
  if cont == "y":
    ufw_maker(z)
  elif cont == "exit" or cont == "n":
    with open('/tmp/script.sh', 'w') as f:
      f.write(' ')
    os.system('rm /tmp/script.sh')
    return

### MAIN FUNCTION ###
def main():
  f = 0
  with open(f) as y:
    ufw_maker(f)

### DUNDER CHECK ###

        
if __name__ == "__main__":
  main()

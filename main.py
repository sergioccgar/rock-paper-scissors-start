rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice = int(input("Wählen Sie bitte zwischen Stein (1), Schere (2) und Papier(3)"))
cpu_choice = random.randint(1,3)

if choice == 1:
  print(rock)
elif choice == 2:
  print(scissors)
elif choice == 3:
  print(paper)
else:
  print("Invalid option.")
  exit()

print("Auswahl des Computers:")
if cpu_choice == 1:
  print(rock)
elif cpu_choice == 2:
  print(scissors)
elif cpu_choice == 3:
  print(paper)

if choice == cpu_choice:
  print("Sie und der Computer sind punktgleich!")
elif cpu_choice - choice == 1 or choice - 2 == cpu_choice:
  print("Sie haben gewonnen!")
else:
  print("Sie haben verloren!")
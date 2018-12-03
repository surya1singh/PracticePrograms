print('welcome to Rock Paper Scissors.'.center(110," "))
print("Created By Surya Pratap Singh")
print("Version 1.0")
import random
username = input("Please Enter Your Name : ")
if not username.strip():
    username = "Player"
computer = "Computer"

#Rules 
# Rock breaks Scissors
# Scissors cuts Paper
# Paper covers Rock.”
# Defaut lives 5
# exit with e, exit, q, quit
# allow small and cap words

def compute_win(p,c):
    "return 0 if player win, 1 if computer win, 2 if tie"
    if p in ('R','ROCK'):
        if c == 'S':
            return 0
        elif c == 'P':
            return 1
    elif p in ('P','PAPER'):
        if c == 'R':
            return 0
        elif c == 'S':
            return 1
    elif p in ('S','SCISSOR'):
        if c == 'P':
            return 0
        elif c == 'R':
            return 1
    return 2

p = input("Select (R)ock, (P)aper, (S)cissor : ").upper()
c = random.choice(['R','P','S'])

if p not in ('R','ROCK','P','PAPER','S','SCISSOR'):
    raise ValueError('Invalid Input. Please select from R,P,S')
else:
    result = compute_win(p,c)
    if result == 2:
        print('Game Tie')
    else:
        print('%s wins'%[username, computer][result])



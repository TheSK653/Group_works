import random

def rps(x):
    l=['Rock','Paper','Scissor']
    return l[int(x)-1]

print('Rock Paper Scissor Game!')
print('\nKey Instructions:\n\
1 = Rock\n\
2 = Paper\n\
3 = Scissor\n\
4 = Quit\n\
')

choices=['1','2','3']
matches=0
wins=0
loses=0
draws=0

while True:
    user=input('\nUser: ')
    
    if user in choices:
        comp=random.choice(choices)
        print(f'\nYou: {rps(user)} vs {rps(comp)} :Bot\nOutcome => ',end='')

        if user==comp:
            print('Draw')
            draws+=1

        elif (user,comp) in (('2','1'),('3',"2"),('1','3')):
            print('Win')
            wins+=1

        else:
            print('Lose')
            loses+=1
        matches+=1

    elif user=='4':
        print(f'\nResults:\n{matches = }\n{wins = }\n{loses = }\n{draws = }')
        input()
        break
    
    else :
        print('Input is invalid')
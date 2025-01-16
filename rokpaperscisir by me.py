import random
while True:
    choices=['rock','scissor','paper']
    rando=random.choice(choices)
    a=input('enter your call==>').lower()
    if rando==a:
        print('***DRAW***')
    if rando=='rock'  and a=='paper':
        print('paper wraps rock! \nyou won!')
    if rando=='rock' and a=='scissor':
        print('rock breaks the scissor!\ncomputer won!')
    if rando=='paper' and a=='scissor':
        print('the scissor cuts the paper!\nyou won!')
    if rando=='paper' and a=='rock':
        print('paper wraps rock! \ncomputer won!')
    if rando=='scissor' and a=='rock':
        print('rock breaks the scissor!\nyou won!')
    if rando=='scissor' and a=='paper' :
        print('the scissor cuts the paper!\ncomputer won!')
    n=input("do you wanna play more?").lower()
    if n!='yes' and n!='y':
        break
print('\n \n THANKYOU VERY MUCH!!')    


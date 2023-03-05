import random


guess_num=random.randint(1,100)

# print(guess_num)

user_num=None

no_of_guess=0

while(user_num!=guess_num):
    user_num=int(input("Enter the your number between 1 to 100: "))
    no_of_guess+=1

    if(user_num==guess_num):
        print("You have guessed it correct")
    else :

        if(user_num>guess_num):

            print("Oh!,choose the lesser number")
        else:
            print("Oh!,Choose greater number")

else:
    print(f"You have guessed  the correct number in {no_of_guess} times")



with open('guess\score.txt','w') as f:

    
    f.write('Last score was: ')
    f.write(str(no_of_guess))

with open('guess\score.txt','r') as ff: 

    scr=ff.read()

    if(scr<str(no_of_guess)):
        scr=no_of_guess



   

import random

li=['head','tail']

random_choice=random.choice(li)

User_input=int(input('what you want to choose head or tail \t for head press 1  \t and \t for tail press 2'))
if User_input==1:
     print("your choice is head")
     user_choice="head"
elif User_input==2:
    print("your choicce is tail")
    user_choice='tail'
else:
    print("not valid option")

print(f" And the coin after flipping is {random_choice}")

if user_choice==random_choice:
    print('congratulations you win ')
    
elif user_choice!=random_choice:
     print('you lose! try again')

if user_choice!=random_choice:
    print('you lose because you choose not correct option😣')
else:
    print('congratulations you win beacuse your choice is match when the coin flip 🙌🎆🎉')

     




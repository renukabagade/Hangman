import random
import stages

names=["solapur","kolhapur","Mumbai","chennai","delhi","nagpur","hyderabad","banglore","trivedrum","satara","sangli","nashik"]
machine=random.choice(names).lower()
# print(machine)

l=len(machine)
#print(l)
dash=[]
life=6
flag=0
stage=6

for i in range(0,l):
    dash+='-'
print(dash)

while(life>0):
    guess=input("Guess a letter:").lower()
    if guess in dash:
            print("letter is already guessed,you lose a life")
            life-=1
    else:
        
        for i in range(0,l):
            if(guess==machine[i]):
                dash[i]=guess
                flag=1
    print(dash)
    if '-' not in dash:
        print("congratulations! you win")
        break
    if flag==0:
        life-=1
    print(f"Remaining chances are:{life}")
    flag=0
        
    print("*")
    print(stages.s[stage-life])
if(life==0):
    print("Sorry, you've run out of chances.")
    print(f"the correct word was:{machine}")
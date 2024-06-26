name_1=input("enter your name: ")
name_2=input("enter your partner name: ")

couple_name=(name_1+name_2).lower()

t=couple_name.count("t")
r=couple_name.count("r")
u=couple_name.count("u")
e=couple_name.count("e")

true=t+r+u+e

l=couple_name.count("l")
o=couple_name.count("o")
v=couple_name.count("v")
e=couple_name.count("e")

love=l+o+v+e

love_score=int(str(true)+str(love))

if(love_score<10)or(love_score<90):
 print(f"your score is{love_score},you go togather like coke and mentos")
elif(love_score>=40)and(love_score<=50):
    print(f"your score is{love_score},you are allright togather")
else:
    print(f"your score{love_score}")    
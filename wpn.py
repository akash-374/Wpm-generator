import random
import time
quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Believe you can and you're halfway there.",
    "Dream big, work hard, stay focused.",
    "The best way to predict the future is to create it.",
    "Every expert was once a beginner.",
    "Don't watch the clock; do what it does. Keep going.",
    "Your only limit is your mind.",
    "Learning never exhausts the mind.",
    "Small progress is still progress.",
    "Consistency beats intensity."
]
print("----------------typing test-----------------")
print("1 -> try or continue test")
print("2 -> stop testing")
exit=True
while exit:
    choice=int(input("enter choice :"))
    if choice==1:
        rw=random.choice(quotes)
        n=len(rw.split())
        print("->",rw)
        start=time.time()
        write=input("->")
        end=time.time()
        sec=end-start
        minute=sec/60
        if(rw==write):
            print("👏prefect,you done a great job 👏")
            print("words per minute:",int(n/minute),"wpn")
        else:
            print("👏well done,some where you make mistake👏")
            print("words per minute:",int(n/minute),"wpn")    
    elif choice==2:
        exit=False
        print("👍 come back soon")
    else:
        print("invalid chioce")        
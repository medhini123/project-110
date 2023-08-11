import random
response="y"

print("do you want to roll a dice ?")
response=input("type y if yes and n to exit:")
while response=="y":
    no=random.randint(1,6)
    print(no)
    if no==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    
    if no==2:
        print("[-----]")
        print("[     ]")
        print("[0   0]")
        print("[     ]")
        print("[-----]")
        
    if no==3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")

    if no==4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]") 

    if no==5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")   

    if no==6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]") 
        
    response=input("enter y for contniung and enter n for exiting:")       





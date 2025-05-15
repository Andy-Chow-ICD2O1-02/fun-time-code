'''
    Casino Simulator 
    Author: Andy Chow 
    Date Updated: May 2nd 2025 
    Date Created: May 15th 2025
'''

import random 

gameplay = True 
balance = 1000

print("Hello! Welcome to the Very Fair Casino!")

while gameplay == True: 


    betAmount = input(f"You have {balance}. Please bet an amount: ")

    betCheck = False 

    while betCheck == False: 
        if betAmount.isdigit():
            if int(betAmount) <= balance:
                betCheck = True
    
        if betCheck == False:
            betAmount = input(f"Invalid Input! You have {balance}. Please bet an amount:")
    
    betAmount = int(betAmount)
    
    print("\nGame modes\n1. Coin Flip\n2. Jackpot\n3. Omega Jackpot")
    gameType = input("Please select a game mode by number: ")
    
    typeCheck = False
    
    while typeCheck == False:
    
        if gameType == "1": 
            
            typeCheck = True
            
            headsOrTails = input("\nChoose heads or tails: ")
        
            htCheck = False 
            while htCheck == False:
                if headsOrTails.lower() == "heads" or headsOrTails.lower() == "tails":
                    htCheck = True 
                else: 
                    headsOrTails = input("Invalid Input! Choose heads or tails: ")
        
            coinValue = random.randrange(1,3)
        
            if headsOrTails.lower() == "heads":
                if coinValue == 1:
                    balance = (balance-betAmount)+(betAmount*1.5)
                    print (f"You Won! Your balance is now {balance}.\n")
                else: 
                    balance = balance-betAmount  
                    print (f"You lost. Your balance is now {balance}.\n")
                
            if headsOrTails.lower() == "tails":
                if coinValue == 2:
                    balance = (balance-betAmount)+(betAmount*1.5) 
                    print (f"You Won! Your balance is now {balance}.\n")
                else: 
                    balance = balance-betAmount
                    print (f"You lost. Your balance is now {balance}.\n")
        
        elif gameType == "2": 
            
            typeCheck = True 
            
            slotValue = random.randrange(1,101)
            if slotValue == 1:
                balance = (balance-betAmount)+(betAmount*10000000000000000)
                print(f"\nYou hit the big jackpot! Your balance is now {balance}.\n")
            elif slotValue >= 2 and slotValue <= 10:
                balance = (balance-betAmount)+(betAmount*2)
                print(f"\nyou hit the small jackpot! Your balance is now {balance}.\n")
            else:
                balance = balance-betAmount
                print(f"\nYou lost. Your balance is now {balance}.\n")
    
        elif gameType == "3":
            
            typeCheck = True
            
            slotValue2 = random.randrange(1,10000000000000000000001)
            if slotValue2 == 1:
                balance = (balance-betAmount)+(betAmount*1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
                print(f"\nYou hit the big jackpot! Your balance is now {balance}.\n")
            elif slotValue2 >= 2 and slotValue2 <= 10:
                balance = (balance-betAmount)+(betAmount*20000000)
                print(f"\nYou hit the small jackpot! Your balance is now {balance}.\n")
            else:
                balance = balance-betAmount
                print(f"\nYou lost. Your balance is now {balance}.\n")
                
        else:
            gameType = input("Invalid Input! Please select a game mode by number: ")
    
    if balance <= 0:
        print(f"You Lost! Your final balance is {balance}")
        gameplay = False 


'''
    Casino Simulator 
    Author: Andy Chow 
    Date Updated: May 2nd 2025 
    Date Created: May 15th 2025
'''

import random 

gameplay = True 
balance = int(1000)

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
    
    print("\nGame modes\n1. Coin Flip\n2. Jackpot\n3. Omega Jackpot\n4. Job\n5. Robbery\n")
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
                    balance = int((balance-betAmount)+(betAmount*1.5))
                    print (f"You Won! Your balance is now {balance}.\n")
                else: 
                    balance = int(balance-betAmount)
                    print (f"You lost. Your balance is now {balance}.\n")
                
            if headsOrTails.lower() == "tails":
                if coinValue == 2:
                    balance = int((balance-betAmount)+(betAmount*1.5))
                    print (f"You Won! Your balance is now {balance}.\n")
                else: 
                    balance = int(balance-betAmount)
                    print (f"You lost. Your balance is now {balance}.\n")
        
        elif gameType == "2": 
            
            typeCheck = True 
            
            slotValue = random.randrange(1,101)
            if slotValue == 1:
                balance = int((balance-betAmount)+(betAmount*10000000000000000))
                print(f"\nYou hit the big jackpot! Your balance is now {balance}.\n")
            elif slotValue >= 2 and slotValue <= 10:
                balance = int((balance-betAmount)+(betAmount*2))
                print(f"\nyou hit the small jackpot! Your balance is now {balance}.\n")
            else:
                balance = int(balance-betAmount)
                print(f"\nYou lost. Your balance is now {balance}.\n")
    
        elif gameType == "3":
            
            typeCheck = True
            
            slotValue2 = random.randrange(1,10000000000000000000001)
            if slotValue2 == 1:
                balance = int((balance-betAmount)+(betAmount*1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
                print(f"\nYou hit the big jackpot! Your balance is now {balance}.\n")
            elif slotValue2 >= 2 and slotValue2 <= 10:
                balance = int((balance-betAmount)+(betAmount*20000000))
                print(f"\nYou hit the small jackpot! Your balance is now {balance}.\n")
            else:
                balance = int(balance-betAmount)
                print(f"\nYou lost. Your balance is now {balance}.\n")

        elif gameType == "4":

            typeCheck = True 

            jobValue = int(random.randrange(1,1001))
            if jobValue == 1000: 
                balance = int(balance-(betAmount+999999))
                print(f"\nYou did a horrible job! You lost {betAmount+999999}.\n")
            else: 
                balance = int(balance+(jobValue/25))
                print(f"\nYou have earned {int(jobValue/25)} from working a {jobValue} hour shift!\n")
            

        elif gameType == "5":

            typeCheck = True 

            print("\nChoose a place to rob:\n1. Casino\n2. Bank\n3. Gas Station")
            robType = input("Choose a number: ")
            robCheck = False 

            while robCheck == False:
                if robType == "1" or robType == "2" or robType == "3":
                    robCheck = True 
                else:
                    robType = input("Invalid Input! Choose a number: ")
            
            robGen = random.randrange(1,101)

            if robType == "1":
                if robGen >= 1 and robGen <= 20:
                    balance = int(balance+(betAmount*200))
                    print(f"\nYou've robbed {int(betAmount*200)} from the Casino!\n")
                if robGen <= 100 and robGen >= 80:
                    balance = int(balance-betAmount)
                    print(f"\nYou got caught and got fined {int(betAmount)}.\n")
                else:
                    print("\nYou got caught and let off with a warning.\n")
            
            if robType == "2":
                if robGen >= 1 and robGen <= 5:
                    balance = int(balance+betAmount*200000)
                    print(f"\nYou robbed the bank and got {int(betAmount*200000)}!\n")
                else: 
                    balance = int(balance-(betAmount+999))
                    print(f"\nYou got caught and got fined {int(betAmount+999)}.\n")
            
            if robType == "3":
                if robGen >= 1 and robGen <= 75:
                    balance = int(balance+(betAmount/5))
                    print(f"\nYou've successfully robbed the gas station for {int(betAmount/5)}.\n")
                else:
                    balance = int(balance-(betAmount/2))
                    print(f"\nYou got caught and the cashier robbed you for {int(betAmount/2)}.\n")

        else:
            gameType = input("Invalid Input! Please select a game mode by number: ")
    
    if balance <= 0:
        print(f"You Lost! Your final balance is {balance}")
        gameplay = False 


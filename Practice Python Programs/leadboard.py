import random

Leaderboard= []

while True:
    print("1. Create Learderboard")
    print("2. Highest Score")
    print("3. Lowest Score")
    print("4. High to low")
    print("5. Low to High")
    print("6. Add Multiple Players")
    print("7. Remove a Player")
    print("8. Check Leaderboard")
    print("9. single player score ")
    print("10. Find player score ")
    print("11. Tie Breaker Check")
    print("12. Top & Least Player")
    print("13. Score Division (Gold, Silver, Bronze)")
    print("14. Clear Scoreboard")
    print("15. Exit")

    choice = int(input("Enter your choice: "))

    if choice==1:    
        Leaderboard = [(random.randint(0, 5))*100 for i in range(10)]
        print(Leaderboard)
    elif choice == 2:
        if len(Leaderboard) == 0:
            print('Enter Choice 1 for create leaderboard so i can give you Higest score')
        else:
            print(max(Leaderboard))
    elif choice==3:
        if len(Leaderboard) == 0:
            print('Leardboard is empty select choice 1 to create random numbers & i can give to Lowest score to High Score')
        else:
            print(min(Leaderboard))
    elif choice==4:
        if len(Leaderboard)==0:
            print('Leardboard is empty select choice 1 to create random numbers & i can give to Lowest score to High Score')
        else:
            desc_score = sorted(Leaderboard, reverse=True)
            print("Sorted (High to Low):", desc_score)
    elif choice==5:
        if len(Leaderboard)==0:
            print('Leardboard is empty select choice 1 to create random numbers & i can give to High score to Lowest Score')
        else:
            desc_score = sorted(Leaderboard)
            print("Sorted (Low to High):", desc_score)
    elif choice==6:
        n=int(input('enter no of player you want to add:'))
        for i in range(n):
            added= int(input(f'enter the score {i+1} person:'))
            Leaderboard.append(added)
        print("Players added successfully!")
        print("Updated Leaderboard:", Leaderboard)
    elif choice==7:
        if len(Leaderboard)==0:
            print('Leaderboard is empty select choice 1 first to remove the players')
        else:
            print(Leaderboard)
            select = int(input('Select the number From the Leaderboard'))
            if select in Leaderboard:
                index = Leaderboard.index(select)
                Leaderboard.pop(index)
            else:
                print('Select from displayed numbers only')
            print('Player is removed')
            print(Leaderboard)
    elif choice==8:
        if len(Leaderboard)==0:
            print('Leaderboard is empty select choice 1 to display the players Score')
        else:
            print(Leaderboard)
    elif choice == 9:
        if len(Leaderboard)==0:
            print('Leaderboard is empty select choice 1 to select player score')
        else:
            print(Leaderboard)
            single_player = int(input('select the number you want to select from 1 to 10'))
            index_player = single_player-1
            print(Leaderboard[index_player])
    elif choice == 10:
        if len(Leaderboard)==0:
            print('Leaderboard is empty select choice 1 to select player score')
        else:
            print(Leaderboard)
            find_score = int(input('Enter The player no to display his score'))
            fs= find_score-1
            print(Leaderboard[fs])
    elif choice == 11:
        if len(Leaderboard)==0:
            print('Leaderboard is empty select choice 1 to two are more player got same score')
        else:
            print(Leaderboard)
            checking = list(map(str, Leaderboard))

            check_tie=[]
            for i in Leaderboard:
                if Leaderboard.count(i) > 1:
                    if i not in check_tie:
                        check_tie.append(score)
            print('tie Break:', check_tie)

    elif choice == 12:
        if len(Leaderboard)==0:
            print('Leaderboard is empty select choice 1 to check the Top and Least score')
        else:
            print('The top score is:', max(Leaderboard))
            print('The Least Score is :', min(Leaderboard))
    elif choice == 13:
        
        if len(Leaderboard) == 0:
            print("Leaderboard is empty. Select choice 1 to rank the players.")
        else:
            sort_score = sorted(Leaderboard, reverse=True)  # Sort from high to low
            gold = []
            silver = []
            bronze = []

            for score in Leaderboard:
                if score > 75:
                    gold.append(score)  
                elif score >= 65:
                    silver.append(score)
                elif score < 50:
                   bronze.append(score)
                else:
                    print("Something went wrong.")
                    print("Gold:", gold)
                    print("Silver:", silver)
                    print("Bronze:", bronze)
    elif choice== 14:
        if len(Leaderboard) == 0:
            print("Leaderboard is empty. no need to clear")
        else:
            Leaderboard.clear()

    elif choice ==15:
        print('Thankyou for visiting, See you again')
        break
    else:
        print('invalid input! enter number between 1 to 15')

        
        
            

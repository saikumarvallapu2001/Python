import random

Leaderboard = []

while True:
    print("\n1. Create Leaderboard")
    print("2. Highest Score")
    print("3. Lowest Score")
    print("4. High to Low")
    print("5. Low to High")
    print("6. Add Multiple Players")
    print("7. Remove a Player")
    print("8. Check Leaderboard")
    print("9. Single Player Score")
    print("10. Find Player Score")
    print("11. Tie Breaker Check")
    print("12. Top & Least Player")
    print("13. Score Division (Gold, Silver, Bronze)")
    print("14. Clear Scoreboard")
    print("15. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Leaderboard = [random.randint(1, 100) for _ in range(10)]
        print("Leaderboard Created:", Leaderboard)

    elif choice == 2:
        if Leaderboard:
            print("Highest Score:", max(Leaderboard))
        else:
            print("Leaderboard is empty.")

    elif choice == 3:
        if Leaderboard:
            print("Lowest Score:", min(Leaderboard))
        else:
            print("Leaderboard is empty.")

    elif choice == 4:
        if Leaderboard:
            print("High to Low:", sorted(Leaderboard, reverse=True))
        else:
            print("Leaderboard is empty.")

    elif choice == 5:
        if Leaderboard:
            print("Low to High:", sorted(Leaderboard))
        else:
            print("Leaderboard is empty.")

    elif choice == 6:
        n = int(input("Enter number of scores to add: "))
        for _ in range(n):
            score = int(input("Enter score: "))
            Leaderboard.append(score)
        print("Scores added successfully.")

    elif choice == 7:
        score = int(input("Enter score to remove: "))
        if score in Leaderboard:
            Leaderboard.remove(score)
            print(f"Score {score} removed.")
        else:
            print("Score not found.")

    elif choice == 8:
        print("Leaderboard:", Leaderboard if Leaderboard else "Leaderboard is empty.")

    elif choice == 9:
        index = int(input("Enter index of score: "))
        if 0 <= index < len(Leaderboard):
            print(f"Score at index {index}: {Leaderboard[index]}")
        else:
            print("Invalid index.")

    elif choice == 10:
        score = int(input("Enter score to find: "))
        if score in Leaderboard:
            index = Leaderboard.index(score)
            print(f"Score {score} found at index: [{index}]")
        else:
            print("Score not found.")

    elif choice == 11:
        duplicates = [score for score in set(Leaderboard) if Leaderboard.count(score) > 1]
        print("Tie Breakers:", duplicates if duplicates else "No ties found.")

    elif choice == 12:
        if Leaderboard:
            print(f"Top Player Score: {max(Leaderboard)}")
            print(f"Least Player Score: {min(Leaderboard)}")
        else:
            print("Leaderboard is empty.")

    elif choice == 13:
        if Leaderboard:
            sorted_scores = sorted(Leaderboard, reverse=True)
            n = len(sorted_scores)
            gold = sorted_scores[:n//3]
            silver = sorted_scores[n//3: 2*n//3]
            bronze = sorted_scores[2*n//3:]
            print("Gold:", gold)
            print("Silver:", silver)
            print("Bronze:", bronze)
        else:
            print("Leaderboard is empty.")

    elif choice == 14:
        Leaderboard.clear()
        print("Leaderboard cleared.")

    elif choice == 15:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")

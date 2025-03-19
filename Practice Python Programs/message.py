messages = [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1]

for i in range(len(messages)):
    if messages[i] == 0:
        print("You have not seen this message.")
        read_mgs = input("Do you want to read this message Enter 1: ")
        
        if read_mgs == "1":
            messages[i] = 1  
            print("You seen this message Go to your work.")
        else:
            print("Message still unread.")
    else:
        print("You have already read this message.")

print(messages)

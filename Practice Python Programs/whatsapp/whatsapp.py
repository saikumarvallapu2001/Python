chat_data = []
num_messages = int(input("Enter the number of messages: "))

for _ in range(num_messages):
    chat_data.append(input())

print("\nChoose an analysis option:")
print("1. Count Total Messages")
print("2. Identify Unique Users")
print("3. Count Total Words")
print("4. Find Average Words Per Message")
print("5. Identify Longest Message Sent")
print("6. Find Most Active User")
print("7. Get Message Count for Specific User")
print("8. Find Most Frequently Used Word by a User")
print("9. Retrieve First and Last Message by User")
print("10. Check if a User is Present in the Chat")
print("11. Find Commonly Repeated Words")
print("12. Find Messages Containing a Specific Keyword")
print("13. Identify User with Longest Average Message Length")
print("14. Count Messages Mentioning a Specific User")
print("15. Display First and Last Message in the Chat")
print("16. Remove Duplicate Messages")
print("17. Find Commonly Used Phrases")
print("18. Sort Messages Alphabetically")
print("19. Display Messages in Reverse Order")
print("20. Find Messages Containing Emojis")
print("21. Find Most Frequently Used Word in the Chat")
print("22. Extract All Questions Asked in the Chat")
print("23. Calculate Reply Ratio Between Two Users")
print("24. Check for Deleted Messages")
print("25. Find Messages Sent After a Specific Keyword")

option = int(input("Enter your choice: "))

if option == 1:
    print("Total messages:", len(chat_data))

elif option == 2:
    users = set()
    for msg in chat_data:
        user = msg.split(":")[0]
        users.add(user)
    print("Unique users in the chat:", users)

elif option == 3:
    total_words = 0
    for msg in chat_data:
        total_words += len(msg.split(": ")[1].split())
    print("Total words in chat:", total_words)

elif option == 4:
    total_words = sum(len(msg.split(": ")[1].split()) for msg in chat_data)
    print("Average words per message:", total_words / len(chat_data))

elif option == 5:
    longest_msg = max(chat_data, key=lambda x: len(x.split(": ")[1]))
    print("Longest message:", longest_msg)

elif option == 6:
    user_count = {}
    for msg in chat_data:
        user = msg.split(":")[0]
        user_count[user] = user_count.get(user, 0) + 1
    most_active_user = max(user_count, key=user_count.get)
    print("Most active user:", most_active_user)

elif option == 7:
    user = input("Enter username: ")
    count = sum(1 for msg in chat_data if msg.startswith(user + ":"))
    print(f"{user} sent {count} messages.")

elif option == 8:
    user = input("Enter username: ")
    word_count = {}
    for msg in chat_data:
        if msg.startswith(user + ":"):
            words = msg.split(": ")[1].split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    most_common_word = max(word_count, key=word_count.get)
    print(f"Most frequently used word by {user}: {most_common_word}")

elif option == 9:
    user = input("Enter username: ")
    user_messages = [msg for msg in chat_data if msg.startswith(user + ":")]
    if user_messages:
        print("First message:", user_messages[0])
        print("Last message:", user_messages[-1])

elif option == 10:
    user = input("Enter username: ")
    users = {msg.split(":")[0] for msg in chat_data}
    print(f"{user} {'is' if user in users else 'is not'} in the chat.")

elif option == 15:
    print("First message:", chat_data[0])
    print("Last message:", chat_data[-1])

elif option == 16:
    print("Unique messages:", set(chat_data))

elif option == 18:
    print("Messages in alphabetical order:", sorted(chat_data))

elif option == 19:
    print("Messages in reverse order:", chat_data[::-1])

elif option == 20:
    emojis = "😀😂😍🔥😊🥰😎💖👍😭"  # Add more as needed
    messages_with_emojis = [msg for msg in chat_data if any(char in emojis for char in msg)]
    print("Messages containing emojis:", messages_with_emojis)

elif option == 21:
    word_count = {}
    for msg in chat_data:
        words = msg.split(": ")[1].split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    most_common_word = max(word_count, key=word_count.get)
    print("Most frequently used word in chat:", most_common_word)

elif option == 22:
    questions = [msg for msg in chat_data if "?" in msg]
    print("Questions asked in the chat:", questions)

elif option == 24:
    deleted_count = sum(1 for msg in chat_data if "This message was deleted" in msg)
    print("Deleted messages count:", deleted_count)

elif option == 25:
    keyword = input("Enter a keyword: ")
    found = False
    for msg in chat_data:
        if found:
            print(msg)
        if keyword in msg:
            found = True

else:
    print("Invalid option.")

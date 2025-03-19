def guessNumber():
    print("Think of a number between 0 and 100 and I will guess it in 7 tries.")
    low = 0
    high = 100
    count = 0

    for i in range(100):        
        mid = (low + high) // 2 
        print("Is your number", mid, "?")
        answer = input("Enter 'yes', 'lower' or 'higher': ")
        if answer == 'yes':
            print(f"Udalo mi sie zgadnac Twoja liczbe w {count} podejsciach!")
            break
        elif answer == 'lower':
            high = mid - 1
            count += 1
        else:
            low = mid + 1
            count += 1

guessNumber()



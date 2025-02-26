#  Day 3 – Daily Python Challenge 🐍
#  Challenge: Aisa Python program likho jo user se ek number le aur check kare ke wo prime number hai ya nahi! 


n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Number is prime")

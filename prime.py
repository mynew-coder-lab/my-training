n = input("Enter a number to check if it's prime: ")
if not n.isdigit() or int(n) < 2:
    print(f"{n} is not a valid input for prime checking.")
else:
    n = int(n)
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
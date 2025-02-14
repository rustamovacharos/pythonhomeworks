for num in range(2, 101):  # Start from 2 since 1 is not prime
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break  # Exit loop early if a divisor is found

    if is_prime:
        print(num)
def fibonacci(n):
    #Fn = Fn-1 + Fn-2  with seed values F0 = 0 and F1 = 1.
    #Initialize 0, 1 as first and second Fibonacci terms.
    start = [0, 1]

    #Map every fibonacci term unto nth term using formula Fn = Fn-1 + Fn-2.
    list(map(lambda x: start.append(sum(start[-2:])),range(2, n)))

    #Stop appending fibonacci elements when the nth term has been reached.
    return start[:n]

v = int(input("Enter Fibonacci's nth term: "))
print(fibonacci(v))



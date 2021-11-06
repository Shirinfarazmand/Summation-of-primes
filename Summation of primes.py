while True:
    def is_prim(n):
        prime = True
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                prime = False
                break
        return prime


    a= input("Enter a number: ")
    a = int(a)
    sum_prime = 0
    for i in range(2,a):
        if is_prim(i):
            sum_prime += i
            

    print(sum_prime)

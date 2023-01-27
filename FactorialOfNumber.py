class FactorialOfNumber:

    def factorialNum(self,number):
        fact=number
        for i in range(1,number):
            fact=fact*i

        print(fact)

    s="   This is my Python   programme"
    print(s.strip())
    print(s.replace(" ", ""))

fac=FactorialOfNumber()
fac.factorialNum(10)



'''WAP to print Fibonacci numbers from 1 to 100
1 1 2 3 5 8 13 21 34 .......'''

class FibonacciSeries:

    def calculateFib(self, start_num, end_num):
        num=1
        print(num)
        for num in range(1, 100):
            for x in range(num,100):
                fib=num+x
                print(fib, "\t")




f=FibonacciSeries()
f.calculateFib(1, 100)
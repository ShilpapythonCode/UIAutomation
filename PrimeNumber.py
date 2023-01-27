'''WAP to Calculate the Prime Numbers between 1 to 100'''

class PrimeNumber:


    def calculatePrimeNumber(self, start_num,end_num):
        i=0
        for num in range(start_num,end_num) :
            for i in range(2,num+1):
                if num%i==0:
                    break
            if num==i:
                print(num, "Number is Prime No.")


p=PrimeNumber()
p.calculatePrimeNumber(1,100)
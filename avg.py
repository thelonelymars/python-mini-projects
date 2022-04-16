
def average():
    bool=True
    print("enter e to end the loop")
    while(bool):
        num = input("enter a number")
        end=input()
        if(end=="e"):
            bool=False
            print(avg)
        sum=0

        sum=sum+int(num)
        count=0
        count=count+1
        avg=sum/count



average()
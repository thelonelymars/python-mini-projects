num=input("enter a number")
convert_num=int(num)
count=0
while(True):
    if(convert_num<=1):
        print(f"steps required for the operation is {count}")
        break
    if (convert_num % 2) == 0:
        convert_num = convert_num / 2
        count+=1
        print(convert_num)

    else:
        convert_num = convert_num * 3 + 1
        count+=1
        print(convert_num)


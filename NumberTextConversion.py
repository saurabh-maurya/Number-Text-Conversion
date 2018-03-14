def conversion(num):
    if len(num)==1 and num=='0':
        print("Zero")
    if len(num)==1 :
        unit(num)
    if len(num)==2:
        tens(num)
    if len(num)>2:
        hun_bil(num)


def hun_bil(num):
    if len(num)==3:
        unit(num[0])
        print("Hundred",end=" ")
        newnum=num[1:]
        tens(newnum)
    if len(num)==4:
        unit(num[0])
        print("Thousand",end=" ")
        hun_bil(num[1:])
    if len(num)==5:
        tens(num[0:2])
        print("Thousand",end=" ")
        hun_bil(num[2:])
    if len(num)==6:
        unit(num[0])
        print("Hundred",end=" ")
        hun_bil(num[1:])
    if len(num)==7:
        unit(num[0])
        print("Million",end=" ")
        hun_bil(num[1:])
    if len(num)==8:
        tens(num[0:2])
        print("Million", end=" ")
        hun_bil(num[2:])
    if len(num)==9:
        unit(num[0])
        print("Hundred",end=" ")
        hun_bil(num[1:])
    if len(num)==10:
        unit(num[0])
        print("Billion",end=" ")
        hun_bil(num[1:])
    if len(num)==11:
        tens(num[0:2])
        print("Billion", end=" ")
        hun_bil(num[2:])
    if len(num)==12:
        unit(num[0])
        print("Hundred",end=" ")
        hun_bil(num[1:])




def tens(num):
    if num[-2]=='1':
        num10_19(num)
    if num[-2]=='2':
        print("Twenty",end=" ")
        unit(num)
    if num[-2]=='3':
        print("Thirty",end=" ")
        unit(num)
    if num[-2]=='4':
        print("Fourty",end=" ")
        unit(num)
    if num[-2]=='5':
        print("Fifty",end=" ")
        unit(num)
    if num[-2]=='6':
        print("Sixty",end=" ")
        unit(num)
    if num[-2]=='7':
        print("Seventy",end=" ")
        unit(num)
    if num[-2]=='8':
        print("Eighty",end=" ")
        unit(num)
    if num[-2]=='9':
        print("Ninety",end=" ")
        unit(num)

def unit(num):
    if num[-1]=='1':
        print("One",end=" ")
    if num[-1]=='2':
        print("Two",end=" ")
    if num[-1]=='3':
        print("Three",end=" ")
    if num[-1]=='4':
        print("Four",end=" ")
    if num[-1]=='5':
        print("Five",end=" ")
    if num[-1]=='6':
        print("Six",end=" ")
    if num[-1]=='7':
        print("Seven",end=" ")
    if num[-1]=='8':
        print("Eight",end=" ")
    if num[-1]=='9':
        print("Nine",end=" ")


def num10_19(num):
    if num[-1]=='0':
        print("ten")
    if num[-1]=='1':
        print("Eleven")
    if num[-1]=='2':
        print("Twelve")
    if num[-1]=='3':
        print("Thirteen")
    if num[-1]=='4':
        print("Fourteen")
    if num[-1]=='5':
        print("Fifteen")
    if num[-1]=='6':
        print("Sixteen")
    if num[-1]=='7':
        print("Seventeen")
    if num[-1]=='8':
        print("Eighteen")
    if num[-1]=='9':
        print("Nineteen")
x=1
while x==1:
    print("**** NUMBER TO TEXT CONVERSION ****")
    num=int(input("Give Integer For Conversion :  "))
    num=str(num)
    conversion(num)
    y=str(input("\n Do You want to enter new Number Y/N :  "))
    if y=='n' or y=='N' :
        x=0


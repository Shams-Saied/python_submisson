card_num=input("Enter card number: ")

temp_card_num=int(card_num)

sum1=0
sum2=0

while(temp_card_num):
    digit=temp_card_num%10
    temp_card_num//=10
    sum1+=digit
    digit=temp_card_num%10
    temp_card_num//=10
    digit*=2
    while(digit):
        sum2+=digit%10
        digit//=10

sum=sum1+sum2

if sum%10==0:
    if card_num[0]=="3":
        if card_num[1]=="4" or card_num[1]=="7":
            print("American Express")
    elif card_num[0]=="5":
        if card_num[1]=="1" or card_num[1]=="2" or card_num[1]=="3" or card_num[1]=="4" or card_num[1]=="5":
            print("MasterCard")
    elif card_num[0]=="4":
        print("Visa")
else:
    print("invalid")



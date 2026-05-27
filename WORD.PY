num=int(input("enter a two digit number:"))

ones = ["Zero","One","Two","Three","Four",
        "Five","Six","Seven","Eight","Nine"]
tens = ["","","Twenty","Thirty","Forty",
        "Fifty","Sixty","Seventy","Eighty","Ninety"]
special = ["Ten","Eleven","Twelve","Thirteen","Fourteen",
           "Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
if 10 <= num <= 19:
  print(special[num-10])
else:
    print(tens[num//10],ones[num%10])
    

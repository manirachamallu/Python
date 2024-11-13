word = input('enter your word')
if word.isalpha():
    if word in 'aeiouAEIOU':
        print('Vowel')
    else:
        print('Not a vowel') 
else:
    print('Enter only Alphabets')
    
    
    
 # current bill
 
units = int(input('Enter Units'))
if units <= 200:
    bill = units * 0.5
elif units <= 400:
    bill = units * 0.65 + 100
elif units <= 600:
    bill = units * 0.80 + 200
elif units > 600:
    bill = units * 1.25 + 425
    print("Rs" + str(int(bill)))   
Ammount = int(input("Enter Ammount for withdraw :"))

note_1 = Ammount//100
note_2 = (Ammount%100)//50
note_3 = ((Ammount%100)%50)//10

print("notes of 100 rupees :",note_1)
print("notes of 50 rupees  :",note_2)
print("notes of 10 rupees  :",note_3)
# You are tea stall owner
# selling products --> Tea, Coffee, Water, Paav
# allow user to select the order from menu driven
# once order done exit

tea = coffee = water = paav = 0
while True:
  user = int(input(" 1. Tea \t 12 \n 2. Coffee \t 22 \n 3. Water \t 20 \n 4. Paav \t 10 \n 0. Exit \n"))

  if user == 1:
    print("Tae Selected")
    tea += 1
  elif user == 2:
    print("Coffee Selected")
    coffee += 1
  elif user == 3:
    print("Water Selected")
    water += 1
  elif user == 4:
    print("Paav Selected")
    paav += 1
  elif user == 0:
    print("Thanls For Order...")
    break
  else:
    print("Bhai dekh ke...")

total = tea * 12 + coffee * 22 + water * 20 + paav * 10
print("Total Amount \t : ", total)
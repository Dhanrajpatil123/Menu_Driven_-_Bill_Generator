# Bill No : 100000101
# ---------------------------
#  1. Tea 	   10   120
#  2. Coffee 	 05   110
#  3. Water 	 02   40
#  4. Paav 	   05   50
#  --------------------------
#  Total Amount  :   500


bill_no = 10000100
total_amount = 0

while True:
  yes_no = int(input("Do You Want To Order : 1. Yes \t 2. No"))

  if yes_no == 1:
    bill_no += 1  # generate bill number
    tea = coffee = water = paav = 0

    tea = int(input("Tea \t : "))
    coffee = int(input("Coffee \t : "))
    water = int(input("Water \t : "))
    paav = int(input("Paav \t : "))


    print("Bill No : ", bill_no)
    print("-----------------------------")
    if tea > 0:
      print("Tea \t ", tea, tea* 12)
    if coffee > 0:
      print("Coffee \t ", coffee, coffee* 22)
    if water > 0:
      print("Water \t ", water, water* 20)
    if paav > 0:
      print("Paav \t ", paav, paav* 10)
    print("-----------------------------")

    total = tea * 12 + coffee * 22 + water * 20 + paav * 10
    print("Total Amount \t : ", total)
    print("******** Thanks For Ordering ********")
  else:
    print("******** Thanks to Used My Application ********")
    break
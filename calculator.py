
def calc():
    print("WELCOME TO MY CALCULATOR...")
    print("THE OPERATIONS HERE YOU CAN DO ARE LISTED AS FOLLOWS :-\n 1.ADDITION)\n 2.SUBTRACTION \n 3.MIULTIPLICATION \n 4.DIVISION \n 5.FLOOR DIVISOIN \n.6.REMAINDER DIVISION \n 7.EXPONENTIATION \n 8.SQUARE \n 9.SQUARE ROOT \n 10.HISTORY \n 11.EXIT")
    his = []
    opt = int(input("ENTER THE NUMBER CORRESPONDING TO DESIRED OPERATION : "))
    match-case opt:
      case 10|11 :
      if case==10:
        f = open("sample.txt",'rt')
        reader = f.read()
        for i in reader():
            print(i,end = '\n')
        f.close()
      case _:
            

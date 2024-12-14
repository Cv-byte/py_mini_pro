
def calc():
    print("WELCOME TO MY CALCULATOR...")
    print("THE OPERATIONS HERE YOU CAN DO ARE LISTED AS FOLLOWS :-\n 1.ADDITION)\n 2.SUBTRACTION \n 3.MIULTIPLICATION \n 4.DIVISION \n 5.FLOOR DIVISOIN \n.6.REMAINDER DIVISION \n 7.EXPONENTIATION \n 8.SQUARE \n 9.SQUARE ROOT \n 10.HISTORY \n 11.EXIT")
    his = []
    while True:
      opt = int(input("ENTER THE NUMBER CORRESPONDING TO DESIRED OPERATION : "))
      result = None
      match opt:
        case 10|11:
          if opt ==10:
            f = open("history.txt",'rt')
            contnt = f.read()
            for hist in contnt:
              print(hist,end='\n')
            f.close()
          else:
            break
        case 1|2|3|4|5|6:
          a = int(input("ENTER FIRST OPERAND : "))
          b = int(input("ENTER SECOND OPERAND : "))
          if opt == 1:
            result =a+b
          elif opt==2:
            result =a-b
          elif opt==3:
            result =a*b
          elif opt==4:
            result =a//b
          elif opt==5:
            result =a/b
          else:
            result =a%b
        case _:
          raise ValueError("INVAILD INPUT")
      with open("hist.txt",'wt') as f:
        contnt = f"OPERATION : {opt} --> OPERANDS : {a} AND {b} ; RESULT : {result}"
        f.write(contnt)   
      f.close()
      return result

calc()
final =calc()
print(final)

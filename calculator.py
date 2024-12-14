import math
def calc():
    print("WELCOME TO MY CALCULATOR...")
    print("THE OPERATIONS HERE YOU CAN DO ARE LISTED AS FOLLOWS :-\n 1.ADDITION)\n 2.SUBTRACTION \n 3.MIULTIPLICATION \n 4.DIVISION \n 5.FLOOR DIVISOIN \n.6.REMAINDER DIVISION \n 7.EXPONENTIATION \n 8.SQUARE \n 9.SQUARE ROOT \n 10.HISTORY \n 11.EXIT")
    

    while True:
      try:
        opt = int(input("ENTER THE NUMBER CORRESPONDING TO DESIRED OPERATION : "))
        result = None
      
        match opt:
          case 10|11:

            if opt ==10:
              try:
                with open("hist.txt",'rt') as f:
                  print(f.read())
              except FileNotFoundError:
                print("No history found!.Do some Operations First") 

            else:
              print("GOOD BYE!")
              break

          case 1|2|3|4|5|6|7:
            a = float(input("ENTER FIRST OPERAND : "))
            b = float(input("ENTER SECOND OPERAND : "))

            match opt:
              case 1:
                result = a + b
              case 2:
                result = a-b
              case 3:
                result = a*b
              case 4:
                result = a/b
              case 5:
                result = a // b
              case 6:
                result = a%b
              case 7:
                result = pow(a,b)

            with open("hist.txt",'at') as f:
              contnt = f"OPERATION : {opt} --> OPERANDS : {a} AND {b} ; RESULT : {result}"
              f.write(contnt)   
            
      
          case 8|9:
            a = float(input("ENTER A NUMBER : "))
            b = None

            if opt==9:
              if a>=0:
                result = math.sqrt(a)
              else:
                print("ERROR! Cannot calculate the square root of a negative number") 
                continue
            else:
              result = a**2   

            with open("hist.txt",'at') as f:
              contnt = f"OPERATION : {opt} --> OPERANDS : {a} AND {b} ; RESULT : {result}"
              f.write(contnt) 
                
          case _:
            raise ValueError("INVAILD INPUT")
      except ValueError as e:
        print(f"Invalid Input : {e}")
      except ZeroDivisionError:
        print("ZERO DIVISION ERROR IS NOT ALLOWED!")

      

      print("THE RESULT : ",result)

calc()


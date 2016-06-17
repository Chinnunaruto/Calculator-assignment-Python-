def add(x ,y):
    summing=x+y;
    print(summing);

def subtract(x ,y):
    subt=x-y;
    print(subt);

def multiply(x ,y):
    multi=x*y;
    print(multi);

def divide(x ,y):
    div=x/y;
    print(div);


#inp=input("Enter Y/y to continue");
inp=True;
while(inp):
  num=int(input("Press,\n1 to add\n2 to subtract\n3 to multiply\n4 to divide\n"));
  if(num==1):
   n1=float(input("Enter first number "));
   n2=float(input("Enter second number "));
   add(n1,n2);

  elif(num==2):
   n1=float(input("Enter first number "));
   n2=float(input("Enter second number "));
   subtract(n1,n2);
            
  elif(num==3):
   n1=float(input("Enter first number "));
   n2=float(input("Enter second number "));
   multiply(n1,n2);

  elif(num==4):
   n1=float(input("Enter first number "));
   n2=float(input("Enter second number "));
   divide(n1,n2);

  else:
   print("Invalid Entry");
  state=input("Enter Y/y to continue ");          
  if((state=='y') or (state=='Y')):
    inp=True;
  else:
    inp=False;


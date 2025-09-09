import csv
import random

a = True
print('''1  =  Admission
2  =  TC
3  =  Marks
4  =  Suggestion
5  =  Library Management''')

n = int(input('enter your choice:'))
if n == 1:
    fa = open('helio3.O.csv', 'a')
    stuwriter0 = csv.writer(fa)
    stuwriter0.writerow(['AName', 'DOB', 'Fname', 'Mname', 'Sex', 'mmun', 'Blood_group', 'Classes', 'Caste', 'Occupation', 'Aadm_no'])
    print('enter the details below')
    AName = input('Enter Candidate name:')
    DOB = input('enter date of birth:')
    Address = input('enter your permanent address')
    Fname = input("enter father's name:")
    Mname = input("enter mother's name:")
    print('''M = Male
F = Female
O = Others''')
    Sex = input('enter from above:')
    if Sex == 'M':
        SM = 'male'
    elif Sex == 'F':
        SM == 'Female'
    elif Sex == 'O':
        SM == 'Others'
    MNum = int(input('enter gaurdians Mobilr number:'))
    mmun = str(MNum)
    if len(mmun) != 10:
        print('error!! enter valid Mobile Number:')
    else:
        pass
    Blood_group = input('enter the blood group of the candidate:')
    Classes = int(input('Enter the class in which the child is to enrolled:'))
    print('''1 = GEN
2 = SC
3 = ST
4 = OBC''')
    Caste = int(input('enter the option from the above:'))
    Occupation = input('enter your occupation')

    print('Thank you for Enrolling your Ward in our SChool, you will soon receive an phone call from us and you have to come to school for some Document Submission')
    Aadm_no = random.randrange(10000,99999)
    print('new Admission No. for Your Ward is:', Aadm_no)
    sturec0 = [AName, DOB, Fname, Mname, Sex, mmun, Blood_group, Classes, Caste, Occupation, Aadm_no]
    stuwriter0.writerow(sturec0)
    fa.close()

elif n == 2:
    ft = open('tc.csv', 'a')
    stuwriter1 = csv.writer(ft)
    stuwriter1.writerow(['Tname', 'Tadm_no', 'Reason'])
    print('Enter some details Below:')
    TName = input('enter students name:')
    Tadm_no = int(input('enter students admission no.:'))
    Reason = input('enter reason for applying for TC:')
    print('please submit a blank and cancelled cheque to the office and also bring some document mentioned on the message sent on your registerd Mobile no.:')
    sturec1 = [TName, Tadm_no, Reason]
    stuwriter1.writerow(sturec1)
    ft.close()

elif n == 3:
    
    w = int(input('enter the number of students:'))

    with open('marks.csv', 'a', newline='') as fr:
      stuwriter2 = csv.writer(fr)
      stuwriter2.writerow(['S No.','RName', 'RAdm_no', 'Smob', 'E', 'H', 'M', 'SS', 'S', 'Avg'])
      for s in range(1,w+1):
        print('please check your ward result below by entering some details:')
        RName = input("enter ward's name:")
        Radm_no = int(input('enter admission no.:'))
        roll_no = int(input('enter your wards roll no.'))
        Rmob = int(input('enter your registered Mobile no.:'))
        mob = str(Rmob)
        q = len(mob)
        if q != 10:
            print('please, enter valid mobile no.......... Aborting....... ')
        else:
            pass
        E = eval(input('enter marks of english'))
        H = eval(input('enter marks of hindi'))
        M = eval(input('enter marks of mathematics'))
        SS = eval(input('enter marks of social science'))
        S = eval(input('enter marks of science'))
      
        Avg = (E+H+M+SS+S)/5
      
        print('Average =',Avg)
        if Avg >=75:
            print('Grade = A')
        elif Avg >60 or Avg <75:
            print('Grade = B')
        elif Avg >50 or Avg <60:
            print('Grade = C')
        elif Avg >40 or Avg<50:
            print('Grade = D')
        elif Avg >33 or Avg<40:
            print('Grade = E')
        else:
            print('Grade = F')
        sturec2 = [s ,RName, Radm_no, Rmob, E, H, M, SS, S ,Avg]
        stuwriter2.writerow(sturec2)
        
      
    

elif n == 4:
  fs = open('suggestion.csv', 'w')
  stuwriter3 = csv.writer(fs)
  stuwriter3.writerow(['SName', 'SClass', 'Suggestion'])
  print('you can enter suggestion below given by the parents:')
  SName = input('enter wards name:')
  SClass = int(input('enter ward class:'))
  Suggestion = input('enter your suggestion:')
  print('tehank u for your valueable suggestion')
  sturec3 = [SName, SClass, Suggestion]
  stuwriter3.writerow(sturec3)
  fs.close()

elif n == 5:
  print('Library Management')
  

  def display_books():
      with open('library.csv', 'r') as file:
          reader = csv.reader(file)
          for row in reader:
              print(f"Book ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Quantity: {row[3]}")

  def add_book():
      book_id = input("Enter Book ID: ")
      title = input("Enter Title: ")
      author = input("Enter Author: ")
      quantity = input("Enter Quantity: ")
      with open('library.csv', 'a', newline='') as file:
          writer = csv.writer(file)
          writer.writerow([book_id, title, author, quantity])
      print("Book added successfully.")

  def issue_book():
      book_id = input("Enter Book ID: ")
      with open('library.csv', 'r') as file:
          reader = csv.reader(file)
          rows = list(reader)
          for row in rows:
              if row[0] == book_id:
                  if int(row[3]) > 0:
                      row[3] = str(int(row[3]) - 1)
                      print(f"Book '{row[1]}' issued successfully.")
                  else:
                      print("Book not available.")
                  break
          else:
              print("Book not found.")
    
      with open('library.csv', 'w', newline='') as file:
          writer = csv.writer(file)
          writer.writerows(rows)

  def return_book():
      book_id = input("Enter Book ID: ")
      with open('library.csv', 'r') as file:
          reader = csv.reader(file)
          rows = list(reader)
          for row in rows:
              if row[0] == book_id:
                  row[3] = str(int(row[3]) + 1)
                  print(f"Book '{row[1]}' returned successfully.")
                  break
          else:
              print("Book not found.")
    
      with open('library.csv', 'w', newline='') as file:
          writer = csv.writer(file)
          writer.writerows(rows)
  
  # Main program
  while True:
      print("\nLibrary Management System")
      print("1. Display Books")
      print("2. Add Book")
      print("3. Issue Book")
      print("4. Return Book")
      print("5. Exit")

      choice = input("Enter your choice: ")
      if choice == '1':
          display_books()
      elif choice == '2':
          add_book()
      elif choice == '3':
          issue_book()
      elif choice == '4':
          return_book()
      elif choice == '5':
          break
      else:
          print("Invalid choice. Please try again.")


else:
  print('wrong input')

import sqlite3
import datetime

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

while True:
  print("Select an option:")
  print("1.Enter a new expenditure")
  print("2.View expenditures summary")
  choice = int(input())
  if choice == 1:
    date = input("Enter the date of the expenditures (YYYY-MM-DD): ")
    description = input("Enter the description of the expenditure: ")
    cur.execute("SELECT DISTINCT category FROM expenses")
    categories = cur.fetchall()
    print("Select a category by number:")
    for idx,category in enumerate(categories):
       print(f"{idx +1},{category[0]}")
    print(f"{len(categories) +1}.Create a new category")
    category_choice=int(input())
    if category_choice==len(categories)+1:
       category=input("enter the new category name: ")
    else:
       category=categories[category_choice-1][0]
    price=input("enter the price of the expenditure: ")
    cur.execute("INSERT INTO expenses (Date,description,category,price) VALUES (?,?,?,?)",(date,description,category,price))
    conn.commit()
  elif choice==2:
    print("Select an option:")
    print("1.View all expenditures")
    print("2.View monthly expenditures by category")
    view_choice=int(input())
    if view_choice==1:
       cur.execute("SELECT*FROM expenses")
       expenses=cur.fetchall()
       for expense in expenses:
          print(expense)
    elif view_choice==2:
       month=input("enter the month (MM): ")
       year=input("enter the year (YYYY): ")
       cur.execute("""SELECT category,SUM(price) FROM expenses"
                   WHERE strftime('%m',Date)=? AND strftime('%Y',Date)=?
                   GROUP BY category""",(month,year))
       expenses=cur.fetchall()
       for expense in expenses:
          print(f"Category:{expense[0]},Total:{expense[1]}")
    else:
       exit()
  else:
    exit()
  repeat = input("Would you like to do something else (y/n)?\n")
  if repeat.lower() !="y":
    break
conn.close()
bill=int(input("enter the total amount of bill: "))
tip=int(input("enter the percentage of tip? 4,8,12: "))
people=int(input("how many people to share the bill: "))
tip_as_percentage=tip/100
total_tip=bill*tip_as_percentage
total_bill=bill+total_tip
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"each person has to pay:Rs {final_amount}")
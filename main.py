import fun

#fun.create_database()

a = input("enter your choice" + "1.Show all entries" + "2.add contact")
if a == 1:
    fun.show_all()

else:
    name = input("Enter name")
    number = input("Enter number")
    fun.add_con(name,number)

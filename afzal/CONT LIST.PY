names_list = []
phone_numbers_list = []
number_of_entries = 1
for _ in range(number_of_entries):
    name = input("please enter your the valid name: ")
    phone_number = input("please enter your the valid phone no: ") 
    names_list.append(name)
    phone_numbers_list.append(phone_number)
print("\n\nname\t\t\t\tphone number\n\n")
for i in range(number_of_entries):
    print(f"{names_list[i]}\t\t\t{phone_numbers_list[i]}")
search_term = input("\nEnter  your search term: ")
print("Searching the  result:")
if search_term in names_list:
    index = names_list.index(search_term)
    phone_number = phone_numbers_list[index]
    print(f"Name: {search_term}, Phone Number: {phone_number}")
else:
    print("Name that you entered is not there")
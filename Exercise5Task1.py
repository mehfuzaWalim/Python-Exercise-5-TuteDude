#Program to use dictionary data type to store data about students' name and marks
#It asks name from the user and searches for marks. Prints marks if name is found else prints student not found

students={"Mark": 85, "John": 78, "Mary": 65, "Henry":90, "Mike":72}
name= input("Enter student's name: ")
#Capitalize names so that we can search even if user enter data in different case
name= name.capitalize()
if(name in students):
	print("Marks of ", name, ": ", students[name])
else:
	print("Student ", name, " not found.")
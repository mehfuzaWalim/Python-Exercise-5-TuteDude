#Program to demonstrate list Slicing. Creates list of 10 numbers from 1 to 10. 
#Extracts first 5 elements, reverses the elements and prints both lists
list=list(range(1,11))
print("Original List: ", list)

extracted_list=list[0:5]
print("Extracted first five elements: ", extracted_list)

#reverses the original list. returns null
extracted_list.reverse()
print("Reversed extracted elements: ",extracted_list )
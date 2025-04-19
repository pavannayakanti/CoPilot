try:
    with open('data.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    data = "File not found. Please check the file path."
except Exception as e:
    data = f"An error occurred: {e}"
print(data)


# This code attempts to open a file named 'data.txt' in read mode. 
# If the file is not found, it catches the FileNotFoundError and assigns a message to the variable 'data'.
# Finally, it prints the content of 'data'.

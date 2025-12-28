user_input=input("Enter text to write to the file :")

with open("output.txt","w") as file:
    file.write(user_input+"\n")

print("Data successfully written to output.txt.")

extra_text = input("\nEnter additional text to append: ")

with open("output.txt","a") as file:
    file.write(extra_text+"\n")

print("Data successfully appended.")


print("\nFinal content of output.txt:")
with open("output.txt","r") as file:
    for line in file:
        print(line.strip())


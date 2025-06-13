new_member = input("Add a new member: ") + "\n"
with open("members.txt", "a") as file:
    file.write(new_member)
    file.close()

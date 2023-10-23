import os
try:
    from design import logo
    logo()
except:
    os.system("figlet ToDo")


def add():
    ctr = 1
    print("--Enter your to-do--\n")
    nTodo = int(input("How many records to be Added: "))

    # Open the file for writing outside the loop
    with open("todo.txt", "a") as fh:
        while ctr <= nTodo:
            todo = input(f"[{ctr}]: ")
            if todo == "":
                todo = input(f"[{ctr}]: ")
            fh.write(todo + '\n')
            ctr += 1
        print("\nAdded Successfully :D")

def show(yourname):
    list = []
    ctr = 1
    print(f"{yourname}, your To-Do are: \n")
    # Open the file for reading and print its content
    with open('todo.txt', 'r') as r:
        lines = r.readlines()
        for ls in lines:
            add = list.append(ls)
        while  ctr <= len(list):
            for line in lines:
                print(f"[{ctr}]: ",line)
                ctr += 1            



def completed():
    ctr = 1
    bab = int(input("Enter line to mark as done: "))  # User input for the line to mark as done

    # Read the content of the file
    with open("todo.txt", "r") as com:
        lines = com.readlines()

    # Check if the line number is valid
    if 1 <= bab <= len(lines):
        # Mark the specified line as done
        lines[bab - 1] = "[+] " + lines[bab - 1]

        # Write the modified content back to the file
        with open("todo.txt", "w") as com:
            com.writelines(lines)

        print(f"Line {bab} marked as done.")
    else:
        print(f"Invalid line number. Please choose a valid line.")


def uncompleted():
    ctr = 1
    bab = int(input("Enter line to mark as  not done: "))  # User input for the line to mark as done

    # Read the content of the file
    with open("todo.txt", "r") as com:
        lines = com.readlines()

    # Check if the line number is valid
    if 1 <= bab <= len(lines):
        # Mark the specified line as done
        lines[bab - 1] = "[-] " + lines[bab - 1]

        # Write the modified content back to the file
        with open("todo.txt", "w") as com:
            com.writelines(lines)

        print(f"Line {bab} marked as done.")
    else:
        print(f"Invalid line number. Please choose a valid line.")

def delete_line():
    # Read the content of the file
    with open("todo.txt", "r") as de:
        lines = de.readlines()

    # Display the current content of the file with line numbers
    for i, line in enumerate(lines, start=1):
        print(f"{i}: {line}", end="")

    # Get the line number to delete from the user
    line_to_delete = int(input("Enter the line number to delete: "))

    # Check if the line number is valid
    if 1 <= line_to_delete <= len(lines):
        # Remove the specified line from the list
        del lines[line_to_delete - 1]

        # Write the modified content back to the file
        with open("todo.txt", "w") as de:
            de.writelines(lines)

        print(f"Line {line_to_delete} deleted.")
    else:
        print("Invalid line number. Please choose a valid line.")

def delet_all():
    try:
        with open("todo.txt", "w") as dl:
            dl.truncate(0)
        print("Deleted all line successful")
    except:
        print("Deletion error")

def delete():
    print('''
1. Delete by line
2. Delete all lines
''')
    ask = int(input("> "))
    if ask == 1:
        delete_line()
    elif ask == 2:
        delet_all()


    
if __name__ == "__main__":
    try:
        try:
            os.system("cls")
        except:
            os.system("clear")
        logo()
        print('''
1. Add a new To-Do
2. Show All To-Do
3. Completed a To-Do
4. Uncompleted To-Do
5. Delete all T-Do
        ''') 
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                os.system("cls")
                add()
            case 2:
                os.system("cls")
                show("Abdullah")
            case 3:
                os.system("cls")
                completed()
            case 4:
                os.system("cls")
                uncompleted()
            case 5:
                os.system("cls")
                delete()
            case _:
                print("Choice out of Range")
    except ValueError as e:
        print("String not allowed")
    except KeyboardInterrupt as er:
        print('\nAborted...')


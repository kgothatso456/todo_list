#TO DO LIST

print('TO DO LIST')

# a dictionary that holds all the list names and their tasks
list_dictionary = {}

# add a new list to the dictionary

def add_new_list():
    print("\n~Adding new list~")
    name = input("Name your list: ").strip().lower()

    # automatically create a list if the user doesn't
    if name == "":
        len_list_dictionary = len(list_dictionary)+1
        name = "list{}".format(len_list_dictionary)

    # handle duplicate names
    if name in list_dictionary:
        print("The name {} already exists. Create a new name.".format(name))
    else:
        list_dictionary[name] = []
        print("Created a new list {}.".format(name))
    
    return name

# ask the user for the name of the file they want

def ask_list_name():
    if len(list_dictionary) == 0:
        print("\nYou currently don't have any lists. Please create a list first.")
        return None

    else:
        print("\nWhat is the name of the list you are looking for")

        # loop to keep asking the user for a list name until they enter an existing name
        while True:
            choice = input("1. To enter list name \n2. To view available list names \nEnter choice: ").strip().lower()
            # check if uswer input is valide
            if choice.isdigit() and int(choice)>0 and int(choice)<3:
                choice = int(choice)

                if choice == 1:
                    while True:
                            list_name = input("\nEnter the name of the list: ").strip().lower()
                            if list_name in list_dictionary:
                                return list_name
                            else:
                                print("Enter the name of an existing list!")

                
                if choice == 2:
                        print("Present list names:")
                        for keys in list_dictionary.keys():
                            print(keys)
                        return None
            else:
                print("Enter a valid number 1 or 2")



# add new tasks to the list names   

def add_task(name):
    while True:
        task_name = input("Enter task or enter 'q' to quit: ").strip().lower()
        if task_name == 'q':
            break
        else:
            list_dictionary[name].append(task_name)


#delete a task

def task_remove(name):
    if list_dictionary[name] == []:
        print("List name: {} is empty".format(name))
    else:
        while True:
            task_name = input("Enter task to delete or enter 'q' to quit: ").strip().lower()
            if task_name == 'q':
                break
            else:
                if task_name in list_dictionary[name]:
                    list_dictionary[name].remove(task_name)
                    print("Removed {} from list".format(task_name))
                else:
                    print("check if task name in list")


#view list of user choice

def view_list(name):
    print("\nViewing list name: {}".format(name))
    items = list_dictionary[name]
    for i, item in enumerate(items, 1):
        print("{}. {}".format(i,item))
        


#delete a list and its task

def delete_list(name):
    if name in list_dictionary:
        del list_dictionary[name]
    return list_dictionary


def run_list():
    while True: 
        user_choice = input("\n1. To add a new list or task \n2. To view list \n3. To remove a task or list \n4. To exit \nEnter choice: ")

        if user_choice.isdigit() and int(user_choice)<5:
            user_choice = int(user_choice)
            
            #Add a new list or a task to an existing list
            if user_choice == 1:

                while True:
                    what_to_add = input("\n1. Add a new list \n2. Add a task to existing list \n3. To go back \nEnter choice: ")
                    if what_to_add.isdigit() and int(what_to_add)<4 :
                        what_to_add = int(what_to_add)

                        # ask user to add a new list and it's tasks
                        if what_to_add == 1:
                            new_list = add_new_list()
                            add_task(new_list)
                            break

                        # ask user for existing user name and add tasks to it
                        elif what_to_add == 2:
                            existing_list = ask_list_name()
                            if existing_list is not None:
                                add_task(existing_list)
                                break

                        elif what_to_add == 3:
                            break

                        else:
                            print("Please enter a valid choice between 1 and 3")

                continue

            # ask user for a list to view 
            elif user_choice == 2:
                list_name = ask_list_name()
                if list_name is not None:
                    view_list(list_name)
                    continue

            # remove a task or a list
            elif user_choice == 3:  
                # Ask name of existing list
                    list_name = ask_list_name()
                    
                    if list_name != None:
                        while True:
                            what_to_remove = input("\n1. To remove a list \n2. To remove a task \nEnter Choice : ")   
                            # check if user input is between the range
                            if what_to_remove.isdigit() and int(what_to_remove)<3 and int(what_to_remove)>0:
                                what_to_remove = int(what_to_remove)

                                # delete the whole list
                                if what_to_remove == 1:
                                    delete_list(list_name)
                                    break 

                                # Remove a task from said list
                                elif what_to_remove == 2:
                                    task_remove(list_name)
                                    break
                            
                            # handles out of range input given
                            else:
                                print("Plase enter a valid number : 1 or 2")
                        

            # quit
            elif user_choice == 4:
                print("Goodbye!")
                break

        else:
            print("Plase enter a valid number between 1 and 5")


run_list()
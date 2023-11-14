print('TO DO LIST')


def add_new_list(list_dictionary):
    """gets user input for the new list, checks for duplicates and adds the new list to the list dictionary 

    Returns: 
        string: the name of the list
    """
    print("\n~Adding new list~")
    name = input("Name your list: ").strip().lower()

    if name == "":
        len_list_dictionary = len(list_dictionary)+1
        name = "list{}".format(len_list_dictionary)
        
    while True:
        if name in list_dictionary:
            print("The name {} already exists. Create a new name.".format(name))
            name = input("Name your list: ").strip().lower()
        else:
            break 

    list_dictionary[name] = []
    print("Created a new list {}.".format(name))
    
    return name


def get_list_name(list_dictionary):
    """asks the user for a list name and checks if the list exists

    Returns:
        string: the name of the list
    """
    while True:
        list_name = input("\nEnter the name of the list: ").strip().lower()
        if list_name in list_dictionary:
            return list_name
        else:
            print("Enter the name of an existing list!")


def validate_choice(choice, list_dictionary):
    """validates the users choice

    Args:
        choice (string): user choice
        list_dictionary (dictionary): dictionary with all the lists

    Returns:
        _type_: _description_
    """
    if choice.isdigit() and int(choice)>0 and int(choice)<3:
        choice = int(choice)

        if choice == 1:
            list_name = get_list_name(list_dictionary)
            return True

        elif choice == 2:
                print("Present list names:")
                for keys in list_dictionary.keys():
                    print(keys)
                return True
    else:
        print("Enter a valid number 1 or 2")
        return False


def ask_list_name(list_dictionary):
    """asks the user for the name of the list they are looking for or to view the current available lists

    Returns:
        string: 
    """
    if len(list_dictionary) == 0:
        print("\nYou currently don't have any lists. Please create a list first.")
        return None

    else:
        print("\nWhat is the name of the list you are looking for ?")

        choice = input("1. To enter list name \n2. To view available list names \nEnter choice: ").strip().lower()
        while True:
            if not validate_choice(choice, list_dictionary):
                choice = input("1. To enter list name \n2. To view available list names \nEnter choice: ").strip().lower()
            else:
                break


def add_task(name, list_dictionary):
    """adds tasks to a list

    Args:
        name (_type_): _description_
    """
    task_name = input("Enter task or enter 'q' to quit: ").strip().lower()
    while True:
        if task_name == 'q':
            break
        else:
            list_dictionary[name].append(task_name)
            task_name = input("Enter task or enter 'q' to quit: ").strip().lower()


def task_remove(name, list_dictionary):
    """removes tasks from a list

    Args:
        name (list): name of a list
    """
    if list_dictionary[name] == []:
        print("List name: {} is empty".format(name))

    else:
        while True:
            task_name = input("Enter task to delete or enter 'q' to quit: ").strip().lower()
            if task_name == 'q':
                break
            
            elif task_name in list_dictionary[name]:
                list_dictionary[name].remove(task_name)
                print("Removed {} from list".format(task_name))
           
            else:
                print("check if task name in list")


def view_list(name, list_dictionary):
    """lists all the items in the list name given

    Args:
        name (list): the name of a list
    """
    print("\nViewing list name: {}".format(name))
    items = list_dictionary[name]
    for i, item in enumerate(items, 1):
        print("{}. {}".format(i,item))
        

def delete_list(name, list_dictionary):
    """deletes list and its items

    Args:
        name (list): the name of the list

    Returns:
        dictionary: dictionary with all the lists
    """
    if name in list_dictionary:
        del list_dictionary[name]
    return list_dictionary


def remove_list_or_task(list_name, list_dictionary):
    while True:
        what_to_remove = input("\n1. To remove a list \n2. To remove a task \nEnter Choice : ")   
        if what_to_remove.isdigit() and int(what_to_remove)<3 and int(what_to_remove)>0:
            what_to_remove = int(what_to_remove)

            if what_to_remove == 1:
                delete_list(list_name, list_dictionary)
                break 

            elif what_to_remove == 2:
                task_remove(list_name, list_dictionary)
                break
        
        else:
            print("Plase enter a valid number : 1 or 2")


def add_list_or_task(list_dictionary):
    while True:
        what_to_add = input("\n1. Add a new list \n2. Add a task to existing list \n3. To go back \nEnter choice: ")
        if what_to_add.isdigit() and int(what_to_add)<4 :
            what_to_add = int(what_to_add)

            if what_to_add == 1:
                new_list = add_new_list(list_dictionary)
                add_task(new_list, list_dictionary)

            elif what_to_add == 2:
                existing_list = ask_list_name(list_dictionary)
                if existing_list is not None:
                    add_task(existing_list, list_dictionary)
                    break

            elif what_to_add == 3:
                break

            else:
                print("Please enter a valid choice between 1 and 3")


def run_list():
    list_dictionary = {}
    while True: 
        user_choice = input("\n1. To add a new list or task \n2. To view list \n3. To remove a task or list \n4. To exit \nEnter choice: ")

        if user_choice.isdigit() and int(user_choice)<5:
            user_choice = int(user_choice)
            
            if user_choice == 1:
                add_list_or_task(list_dictionary)

            elif user_choice == 2:
                list_name = ask_list_name(list_dictionary)
                if list_name is not None:
                    view_list(list_name, list_dictionary)
                    

            elif user_choice == 3:  
                    list_name = ask_list_name(list_dictionary) 
                    if list_name != None:
                        remove_list_or_task(list_name, list_dictionary)
                        
            elif user_choice == 4:
                print("Goodbye!")
                break

        else:
            print("Plase enter a valid number between 1 and 5 according to the given options")


run_list()
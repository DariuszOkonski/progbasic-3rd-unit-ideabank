import os

def clear_console():
    os.system('cls')

def write_to_file(ideas_list):
    with open('ideabank.txt', 'w') as f:
        for item in ideas_list:
            f.write("%s--\n" % item)

def read_from_file(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def sanitize_list(ideas_list):
    temp_list = []
    for item in ideas_list:
        temp_list.append(item.split('--')[0])
    return temp_list

def menu():
    print('Idea bank')
    print('=========')
    print('--add')
    print('--list')
    print('--delete nr')
    print('--quit')
    print()
    option = input("Get option: ").lower()
    return option

def print_ideas(ideas_list):
    index = 1
    for item in ideas_list:
        print(f"{index} - {item}")
        index += 1

def get_idea(ideas_list):
    while True:
        try:
            idea = input('What is your new idea?: ')
            ideas_list.append(idea)
            print_ideas(ideas_list)
        except KeyboardInterrupt:
            write_to_file(ideas_list)
            break

def sanitize_option(option):
    option = option.split(' ')
    isCasted = False
    option_additional = ''
    
    option_base = option[0]
    if len(option) == 2:
        option_additional, isCasted = cast_option_to_int(option[1])
    else:
        option_additional = 0
    
    return (option_base, option_additional, isCasted)

def cast_option_to_int(option):
    option_additional = 0
    isCasted = True
    try:
        option_additional = int(option)
    except ValueError:
        isCasted = False

    return (option_additional, isCasted)

def delete_idea(ideas_list, element_to_remove, isCasted):    
    if(not isCasted) :
        print("Specify a number after --delete")
    else:
        if(len(ideas_list) < element_to_remove or element_to_remove <= 0):
            print(f'There is no element with number: {element_to_remove}')
        else:
            del ideas_list[element_to_remove - 1]
            write_to_file(ideas_list)


def run():
    clear_console()
    ideas_list = []
    
    ideas_list = read_from_file('ideabank.txt')
    ideas_list = sanitize_list(ideas_list)


    while True:
        option = menu()
        
        option_base, option_additional, isCasted = sanitize_option(option)

        if option_base == '--add':
            get_idea(ideas_list)
        elif option_base == '--list':
            print_ideas(ideas_list)
        elif option_base == '--delete':
            if(option_additional != 0):
                delete_idea(ideas_list, option_additional, isCasted)
        elif option_base == '--quit':
            break
        else:
            print("DO NOT HAVE SUCH AN OPTION")

        print("")

run()
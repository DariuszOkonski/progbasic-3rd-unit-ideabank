list_ideas = []

def ask_about_idea():
    new_idea = input("What is your new idea?")
    return new_idea


def add_idea_to_list(list_ideas):
    new_idea = ask_about_idea()
    list_ideas.append(new_idea)

def reveal_ideas(ideas):
    index = 1
    for single_idea in ideas:
        print(f'{index}. {single_idea}')
        index += 1


def save_list_to_file(list_of_ideas):
    new_file = open("Nowy_plik.txt", "w")
    # new_file.writelines(list_of_ideas)
    for element in list_of_ideas:
        new_file.write(element + "\n")
    new_file.close()

def load_ideas_file():
    loaded_file = open("Nowy_plik.txt", "r")
    content = loaded_file.readlines()
    loaded_file.close()
    return content

def format_file_content(file_content):
    formatted_list = []
    for entry in file_content:
        formatted_list.append(entry.strip("\n"))
    return formatted_list

def start_program():
    list_ideas = format_file_content(load_ideas_file())
    print(list_ideas)
    while True:
        add_idea_to_list(list_ideas)
        reveal_ideas(list_ideas)
        save_list_to_file(list_ideas)


start_program()

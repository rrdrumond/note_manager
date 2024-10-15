import os

file_name = 'note.txt'


# add note
def add ():
    notes = input('Write the note that you want add: ').lower().strip().capitalize()
    with open(file_name, 'r') as file:
        reader = file.readlines()
        lists = []
         
        if notes +'\n' in reader:
            print('This note exist!')
        else:
                lists.append(notes)
                print('Note has been add!')
                
    with open(file_name, 'a') as file:
        for note in lists:
            file.write(note +'\n')
    
                    
#show list of notes
def show_list():
    with open(file_name, 'r')as file:
        reader = file.readlines()
        i = 1
        
        for row in reader:
            if row == 'Note Manager \n':
                print(row)
            else:
                print(f'{i}.{row.strip()}')
                i += 1
                
#Sear specific note
def search_note():
    notes = input('Write down what you looking for: ').lower().strip().capitalize()
    
    with open(file_name, 'r')as file:
        reader = file.readlines()
        
        for row in reader:
            if row == notes +'\n':
                print(f'The note {notes} was found!')
                break
            elif row == reader[-1]:
                if row != notes +'\n':
                    print(f'The note {notes} doesn\'t exist!')
                    
#Delete a note
def delete_note():
    notes = input('Write the note that you want to delete: ').lower().strip().capitalize()
    
    with open(file_name, 'r') as file:
        reader  = file.readlines()
        lists = []
        found = False
        
        for row in reader:
            if row == notes +'\n':
                print('The note has been removed!')
                found = True
            else:
                lists.append(row)
            
    if not found:
        print(f'The note {notes} was not found!')
                
    with open(file_name, 'w')as file:
         for row in lists:
            file.write(row)
                        
#Create file txt if not exist
if not os.path.exists(file_name):
    with open(file_name, 'w') as file:
        file.write('Note Manager \n')

out = True

while out:
    option = int(input('Select one option in number:\n 1. Add note.\n 2.List all notes.\n 3.Search note.\n 4.Delete note.\n 5.Out.:  '))

    if option == 1:
        add()

    elif option == 2:
        show_list()
        
    elif option == 3:
        search_note()
        
    elif option == 4:
        delete_note()
        
    elif option == 5:
        out = False
        print('Exiting the system!')
    else:
        print('Invalid option, please try again!')

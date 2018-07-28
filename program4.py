#Program 4 - Journal App

#Main method contains the print header function and the run event loop function
def main():
    print_header()
    run_event_loop()
    list_entries()
    add_entries()


#Define method print header
def print_header():
    print('----------------')
    print('  JOURNAL APP   ')
    print('----------------')

#Added upper string method to input since most users will type the lower
#case letter by default. Other wise it will default to exit.

def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None

    journal_data = [] #list data structure

    while cmd != 'x':
        #Add strip string method to remove any extra spaces entered by the user.
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ').upper().strip()
        if cmd == 'L':
            list_entries(journal_data)
        elif cmd == 'A':
            add_entries(journal_data)
        elif cmd != 'x':
            print("Sorry, we don't understand {}.".format(cmd))

    print('Done, goodbye.')

def list_entries(data):
    print('Your journal entries: ')
    #Show the journal entries in reverse order so latest is shown first

    entries = reversed(data)
    #Enumerate adds a counter to each item in the journal_data list.
    #In other languages you would have to add a counter. The Pythonic way is to
    #enumerate which creates a tuple and automatically adds a counter to each item
    #in the for loop. It is the for loop that binds the counter number to the element in the list. https://stackoverflow.com/questions/22171558/what-does-enumerate-mean?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

    for entry in enumerate(data):
        print(entry)

def add_entries(data):
    text = input('Type your entry, <enter> to exit: ')
    data.append(text)




#Call main function to run entire script
main()

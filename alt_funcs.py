def check(response):
    if response == 'q':         # if 'q' is entered the program will exit
        exit()
    elif response == '':        # if nothing is entered, the user is returned to the main body
        return        
    else:                       # if anything else is entered, the function restarts recursively
        return check(input('I\'m not sure what you typed. Please hit "Enter" on your keyboard or type "q" to quit.  '))


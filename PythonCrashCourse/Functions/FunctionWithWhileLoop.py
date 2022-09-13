def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#This is an infinite loop without break!
while True:
    print(f"\n Please tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    
    quitOrContinue = input(f"\nDo you wish to continue {formatted_name}? Type 'quit' or 'continue': ")
    #print(quitOrContinue)
    if quitOrContinue == 'quit':
        break
    
    #break


"""
Hello World App
This app provides the solution to the problem of the Hello World, presented when you begin your day and you have to say hello to your relatives
"""

""" Main function
This function presents the menu of the app and allows the user to place an input to select who to salute.
"""

def main():
    print("********** Select an option **********") # List of options.
    print("*    1- Say hello to the world       *")
    print("*    2- Say hello to your family     *")
    print("*    3- Say hello to your neighbours *")
    print("**************************************")
    option = int(input()) # Get the selected option by the user. 
    match option: # 
        case 1:
            hello("world")
        case 2:
            return hello("family")
        case 3:
            return hello("neighbours")
        case _:
            print("********************************")
            print("* Please select a valid option *")
            print("********************************")


"""Hello Function
This function salutes your friends, family and world.
Takes as an input a string that will represent the person who is getting saluted. 
"""

def hello(who): # Takes a string as a parameter that will provide the salute subject.
    print(f"Hello {who.capitalize()}") # Places the parameter into a print function to salute whoever you want to.

main() # Call the main function to start the program.
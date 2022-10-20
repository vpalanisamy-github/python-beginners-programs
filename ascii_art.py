from colorama import init
import termcolor, pyfiglet

init()

def colored_message():
	message = input("What message do you want to print?\n")



	col = input("what color?\n")

	print(message)
	return (termcolor.colored(pyfiglet.figlet_format(message), color= col))
print(colored_message())
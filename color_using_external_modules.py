from colorama import init
import termcolor

#Initializing init to use termcolor to work on Windows too
init()

#then using termcolor to get colored text output
print(termcolor.colored('Hello, World!', 'red', 'on_grey', ['bold'] ))
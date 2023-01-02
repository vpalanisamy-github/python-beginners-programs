# # --To get the idea of packages and class we are using turtle package here
#
#
# import turtle
#
# from turtle import Turtle, Screen
#
# dummyturtle = Turtle("turtle")
#
#
# dummyturtle
# dummyturtle.color('blue')
# dummyturtle.forward(100)
# Screen().exitonclick()


##prettytable package installed from PyPI.

from prettytable import PrettyTable
table = PrettyTable()

#--Adding data to the table row by row
table.field_names = ["Pokeman Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

#Aligning the table using align attribute.
table.align = "l"
print(table)    
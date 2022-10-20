from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
#Navigating from html elements(tags)
t = soup.find("div")#Gives the first div tag
a = soup.find_all("div") #Gives all the div tags
f = soup.find(id="first") #Gives first attribute tag
g = soup.find(attrs={"data-example": "yes"}) #Gives all of same attributes
c = soup.find_all(class_="special") #Please use class_ while try to find the class tags


#Navigating elements(tags) using css selecters 
#Note: select always return list as an output.
t = soup.select("div") # Based on the tag. we can simply pass the tag name
v = soup.select("#first") #Based on an id(Here # is called octothorp)
d = soup.select(".special") #Based on a class
d = soup.select("[data-example]") #Based of an attribute
print(d)



#Navigating with BeautifulSoup(Parent to child and also to next and previous siblings)
#Using tags
data = soup.body.contents #produces the list of elements of an parsed file including newlines.
data = soup.body.contents[0].next_sibling #Gives the 2nd element of the list(1st is newline)

#Using searching methods(preferrable)
data = soup.find(id = "first").find_next_sibling(attrs = {"data-example": "yes"})
data = soup.select("div")[0].find_next_sibling(attrs = {"data-example": "yes"})
print(data)




#Accessing data in elements(tags):
for el in soup.select(".special"):
  print(el) #returns whole element
  print(el.get_text()) #returns the data which we want
  print(el.name) #return an element name alone like li, div etc..,
  print(el.attrs) #returns the attribute of an element in a dictionary format.
e = soup.find("div")["id"] #accessing using the key to find the values in an attribute
print(e) #output(first)

# http://quotes.toscrape.com
from os import system, name
from bs4 import BeautifulSoup
from csv import writer, reader, DictWriter
import requests
import random

# Getting all page contents into the list
quote_list = []
name_list = []
author_url_list = []
author_details_list = []
new_list = []


next_page = ""

while True:
    url = f"http://quotes.toscrape.com{next_page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quote = soup.select(".text")
    name = soup.select(".author")
    author_urls = soup.select(".author")

    for i in quote:
        quote_list.append(i.get_text())

    for j in name:
        name_list.append(j.get_text())

    for k in author_urls:
        new_list.append(k.find_next_sibling()["href"])
        author_url_list.append(new_list)

    for u in new_list:
        author_url = f"http://quotes.toscrape.com{u}"
        response = requests.get(author_url)
        author_soup = BeautifulSoup(response.text, 'html.parser')
        # name_list.append(str(author_soup.find(class_="author-title").contents[0]))
        author_details = "The author was born " + author_soup.find(
            class_="author-born-location").get_text() + " on " + author_soup.find(
            class_="author-born-date").get_text()
        author_details_list.append(author_details)
        new_list = []

    print("page completed")
    try:
        next_page = soup.find("nav").find(class_="next").find("a")["href"]
    except AttributeError:
        break


# Seperating first and last names
first_name = []
last_name = []
for i in name_list:
    val = i.split(" ")
    first_name.append(val[0])
    last_name.append(val[1])

# Copying the content into csv file.
with open("scraped_quotes_data.csv", "w", encoding="utf-8") as file:
    header = [
        "Quotes",
        "Author Name",
        "First Name",
        "Last Name",
        "Author Details"]
    csv_file = DictWriter(file, fieldnames=header)
    csv_file.writeheader()
    for i in range(len(quote_list)):
        csv_file.writerow({"Quotes": quote_list[i],
                           "Author Name": name_list[i],
                           "First Name": first_name[i],
                           "Last Name": last_name[i],
                           "Author Details": author_details_list[i]})


"""HTML tags reference"""

# <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
# <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>
# <span>by <small class="author" itemprop="author">Steve Martin</small>
# <a href="/author/Steve-Martin">(about)</a>
# </span>
# <div class="tags">
#             Tags:
#             <meta class="keywords" content="humor,obvious,simile" itemprop="keywords"/>
# <a class="tag" href="/tag/humor/page/1/">humor</a>
# <a class="tag" href="/tag/obvious/page/1/">obvious</a>
# <a class="tag" href="/tag/simile/page/1/">simile</a>
# </div>
# </div>


""""Guessing the author's name using Quote Game"""


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')


def win_game():
    print("You Win..!")


def quote_maker():
    with open("scraped_quotes_data.csv", encoding="utf-8") as file:
        print("Welcome to the Game!")
        csv_reader = reader(file)
        full_list = list(csv_reader)
        quote_line = random.choice(full_list)
        while quote_line == [] and quote_line != full_list[0]:
            quote_line = random.choice(full_list)
        return quote_line


# Game logic
game_over = False
while not game_over:
    quote_row = quote_maker()
    print(quote_row)
    print(quote_row[0])
    guess = input("Guess the author's name.")
    if guess.lower() == quote_row[1].lower():
        win_game()
    else:
        print(f"Incorrect. Your first hint: {quote_row[4]}")
        guess = input("Guess again: ")
        if guess.lower() == quote_row[1].lower():
            win_game()
        else:
            print(
                f"Incorrect. Your second hint(first letter of the name): {quote_row[1][0]}")
            guess = input("Guess again: ")
            if guess.lower() == quote_row[1].lower():
                win_game()
            else:
                print(
                    f"Incorrect. Your third hint(last letter of the name): {quote_row[1][-1]}")
                guess = input("Guess again: ")
                if guess.lower() == quote_row[1].lower():
                    win_game()
                else:
                    print("Sorry..!Your quote_row out of guesses.")

    play_again = input("Do you want to play again?: ")
    if play_again == "yes":
        clear()
    else:
        print("Thanks for playing.")
        game_over = True

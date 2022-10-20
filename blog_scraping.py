#https://www.rithmschool.com/blog
import requests 
from bs4 import BeautifulSoup
from csv import writer, reader

response= requests.get("https://www.rithmschool.com/blog")
# print(response.text)

#parsing 
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
# print(articles)

with open("scraped_blog_data.csv", "w") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["title", "link", "date"])

	for article in articles:
		title= article.find("a").get_text()
		time= article.find("time").attrs["datetime"]  #We can also directly call using: article.find("time")["datetime"] 
		url= article.find("a").attrs["href"]
		csv_writer.writerow([title, url, time])




#single element


# <article>
# <h4 class="section-heading">
# <a href="/blog/looking-back-women-in-tech">Looking Back On Our First Women In Tech Event Series</a>
# </h4>
# <div class="card">
# <time datetime="2020-03-31 00:00:00 UTC" pubdate=""></time>
# <p dir="ltr">At the end of 2019, sitting down as a company and reviewing the year behind us, we decided that increasing the number of women enrolled in our program was something worth prioritizing. In an effort to do so, we decided to host an event series targeted at women with no previous programming experience.</p>
# <p><a href="/blog/looking-back-women-in-tech">Continue Reading</a><p>
# <h4 class="service-heading"><small>March 31, 2020</small></h4>
# </p></p></div>
# </article>
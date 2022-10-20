def week():
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = 0
    while True:
        try:
            yield week_days[day]
            day +=1

        except IndexError:
            break

days = week()
for i in days:
	print(i)



def make_song(count = 99, beverage = "soda"):
    while True:
    	if count >1:
    	    yield "{} bottles of {} on the wall.".format(count, beverage)
    	    count-=1
    	elif count == 1:
    	    yield "Only {} bottle of {} left!".format(count, beverage)
    	    count -=1
    	elif count == 0:
    		yield "No more {}!".format(beverage)
    		count -=1
    		break

kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song)) # '5 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '4 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '3 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
print(next(kombucha_song)) # 'Only 1 bottle of kombucha left!'
print(next(kombucha_song)) # 'No more kombucha!'
print(next(kombucha_song)) # StopIteration
print(next(kombucha_song))


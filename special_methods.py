class Train():
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
    	return "{} car train".format(self.num_cars)
    
    def __len__(self):
    	return self.num_cars
        
    

new_train = Train(4)
print(new_train)
print(len(new_train))
#class Point():
#def __init__(self,a,b):
        #self.x=a
#        self.y=b
#p=Point(3,5)
#print(p.x)
#print(p.y)

# class Flight():
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.passengers=[]

#     def add_passengers(self,name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True

#     def open_seats(self):
#         return self.capacity - len(self.passengers)
        
# flight=Flight(3)

# p=["Sarmad","Malaika","Ali","Kashif"]
# for person in p:
#     if flight.add_passengers(person):
#         print(f"Added {person} to the flight ")
#     else:
#         print(f"No available seats for {person}")

def anounce(f):
    def wraper():
        print("the function is about is start...")
        f()
        print ("the function has runn successfully.")
    return wraper

@anounce   
def hello():
    print("I am the Funtion")


hello()

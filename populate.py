# Marisa Gross
# CIS 125
# Collaborated with Jacob and Daniel; got help from Dr. Neumann


# populate
def populate(world,h,w):
    dummy = 0

#display
def display(world,h,w):
    dummy2 = 2

#generate
def generation(world,h,w):
    dummy3 = 3

#import random, define variables
def main ():
    import random
    height = 22
    width = 80
    world = [ ]
    
#run the populate function    
    populate(world,height,width)
    
    x = input("Enter Q to quit")
    while x != "Q":
        
#run display function        
        display(world,height,width)
        
#run generation function        
        generation(world,height,width)
        
        x = input("Enter Q to quit")
        
main ()

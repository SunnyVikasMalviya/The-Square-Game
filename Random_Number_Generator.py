from random import randint

#Function to Generate Numbers 1-15 in random order
list_ =[]
def generate_list_() :
    #list_ = []
    while len(list_)<15 :
        x = randint(1,15)
        if x not in list_ :
            list_.append(x)
    list_.append(0)    
    print(list_)

#generate_list_()

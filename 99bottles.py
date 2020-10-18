'''
99 bottles of beer basically is a program that
writes the lyrics of the song... 99 bottles of beer
and does it in a countdown fashion... from 99 to no bottles.
'''



'''
This function tells what state of the noun to use, 
either singular or plural. The function has a counter 
as its parameter. The counter determines what should 
be used, i.e either 'bottles' or 'bottle'
we use 'bottle' only when the counter is 1.  
'''
def bottle_bottles(counter):
    if counter==1:
        return "bottle"
    return "bottles"

#We initialize counter to 99
counter=99

#we create another function that defines the 
#two parts of the chorus and displays them in a 
#decreasing fashion
#note that the same parameter is used... counter 
def song(counter):
    #chorus1 leaves two spaces to be filled up by 
    #the number at every instant firstly and then  
    #the word 'bottles' or 'bottle'
    chorus1="{0} {1} of beer on the wall, {0} {1} of beer."
    #chorus two does same... leaves room for the
    #same order of words; number then bottle(s)
    chorus2="Take one down and pass it around, {0} {1} of beer on the wall!\n"
    
    #for every element in the range between 99 to 0
    #print the chorus 1, fill in the first blank 
    #position with i which is the number in the counter
    #and the selected word... bottle or bottles
    for i in range (counter, 0, -1):
        print (chorus1.format(i, bottle_bottles(i)))
        #decrease the value of counter by 1. This is 
        #especially useful in the chorus2. without this,
        #the decrease on the number of bottles won't be 
        #done once one 'Takes one down and pass it around'.
        counter=i-1
        #setting the condition for a change in lyrics 
        #when there are no more bottles left. instead
        #of saying 0 bottles, we say "no more"
        if counter==0:
            counter="no more"
        #this line of code operates as a pair with the 
        #print chorus1. it still does pay attention 
        #to conditions coming between chorus1 and chorus2
        #and going through a condition check of counter
        print(chorus2.format(counter, bottle_bottles(counter)))
    #this line of code is set to print by default in 
    #this function although, it listens to the sequence
    #of code coming from above and executes only when  
    #they have all been executed    
    print("No more bottles of beer on the wall,"\
          " no more bottles of beer.\n"\
          "Go to the store and buy some more, No "\
              "more bottles of beer on the wall!")
        
'''
Calling the function alongside the parameter counter 
which has already been defined as 99
This can be altered and set to 1000 or whatever value
'''
song(counter)











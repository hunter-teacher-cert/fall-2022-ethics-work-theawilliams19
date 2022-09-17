# FILENAME: binsearch.py
# First Last: Théa Williams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: thinkcspy text, Datacamp Intro to Python course

def binarySearch(list, value):
  #create assign variables representing the high, low and middle indices. This search returns the index of the value you are searching for. 
      
  low = 0
  high = len(list) # len in python is equivalent to.length and .length() and .size() in Java/
  middle = (low + high) // 2
 

  #while we're not done:
  while True:
    #edge case, if the value is not found, this will break out of the loop. Otherwise, it will go to the else cases below (update high, low, and middle).
    if high <= low: 
      if middle == 0 and list[middle] == value:
        return middle
      return -1 #not found in the list

    #if the item is at data.get(middle), return middle array[3]
    elif list[middle] == value:
      return middle #the value defined in the main is found
      
    elif value < list[middle]:
      high = middle - 1 #sets the "high" index to the one below the old "middle" index.This adjustment happens if necessary.
    else:
      low = middle + 1 #sets the "low" index to the one above the old "middle" index.This adjustment happens if necessary.
        
    middle = (low + high) // 2
    

## list test:
print("List test")
testList = [0,2,4,7,9,11,24,27,35,35,43,51,67,75,88,92,100]
print(binarySearch(testList, 0)) #should be 0
print(binarySearch(testList, 7)) #should be 3
print(binarySearch(testList, 35)) #should be 35
print(binarySearch(testList, 100)) #should be 16
print(binarySearch(testList, 101)) #should be -1
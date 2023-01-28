#Pattern in Python

#get row length from user
r = int(input("Enter Row : ")) #for this project row is 5 but you should "set 6" (because its start to count from 0)

#Programs to print number pattern
#1
#22
#333
#4444
#55555

for i in range(r): #i is for row
    for j in range(i): #j is for coulomn
        print (i , end = "") #the increase is work on row --> i
    print ("\n") #go to next line

####################

#Pyramid pattern of numbers
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5

for i in range(0 , r):
    for j in range(1 , i+1):
        print (j , end = "")
    print ("\n")

####################

#Inverted pyramid pattern of numbers
#1 1 1 1 1 
#2 2 2 2 
#3 3 3 
#4 4 
#5

k = 0
for i in range(r , 0 , -1): #-1 is for reverse loop
    k = k + 1
    for j in range(1 , i):
        print (k , end = "")
    print ("\n")

####################

#Inverted Pyramid pattern with the same digit
#5 5 5 5 5 
#5 5 5 5 
#5 5 5 
#5 5 
#5

for i in range(r, 0, -1):
    for j in range(0, i):
        print(r, end = "")
    print("\n")
    
####################


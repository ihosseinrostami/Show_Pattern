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



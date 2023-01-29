#Pattern in Python

#get row length from user
#this r is used for all problem blow
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

########################################

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

########################################

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

########################################

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
    
########################################

#Inverted half pyramid pattern with number
#0 1 2 3 4 5 
#0 1 2 3 4 
#0 1 2 3 
#0 1 2 
#0 1

for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\n")
    
########################################

#Alternate numbers pattern using while loop
#1 
#3 3 
#5 5 5 
#7 7 7 7 
#9 9 9 9 9

for i in range(0, r):
    for j in range(0, i):
        print(2*i-1, end = "")
    print("\n")
    
########################################

#Reverse number pattern
#5 5 5 5 5 
#4 4 4 4 
#3 3 3 
#2 2 
#1

for i in range(r, 0, -1):
    for j in range(0, i):
        print(i, end=' ')
    print("\n")
    
########################################

#Reverse Pyramid of Numbers
#1 
#2 1 
#3 2 1 
#4 3 2 1 
#5 4 3 2 1

for i in range(0 , r):
    for j in range(i , 0 , -1):
        print(j, end=' ')
    print("\n")
    
########################################

#Another reverse number pattern
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1

for i in range(0, r + 1):
    for j in range(r - i, 0, -1):
        print(j, end=' ')
    print()
    
########################################

#Print reverse number from 10 to 1
#1
#3 2
#6 5 4
#10 9 8 7

start = 1
stop = 2
current_num = stop
for i in range(2, 6):
    for j in range(start, stop):
        current_num -= 1
        print(current_num, end=" ")
    print("")
    start = stop
    stop  = stop + i
    current_num = stop
    
########################################

#Number triangle pattern
#          1
#        1 2
#      1 2 3
#    1 2 3 4
#  1 2 3 4 5

for i in range(1, r):
    num = 1
    for j in range(r, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
    
########################################

#Pascal’s triangle pattern using numbers
#1 
#1 1 
#1 2 1 
#1 3 3 1 
#1 4 6 4 1 
#1 5 10 10 5 1 
#1 6 15 20 15 6 1

def decide_number(n, k): #define pascal
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

for i in range(0, r):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()
        
########################################

#Square pattern with numbers
#1 2 3 4 5 
#2 2 3 4 5 
#3 3 3 4 5 
#4 4 4 4 5 
#5 5 5 5 5

for i in range(1, r + 1):
    for j in range(1, r + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
    
########################################

#Multiplication table pattern
#1  
#2  4  
#3  6  9  
#4  8  12  16  
#5  10  15  20  25  
#6  12  18  24  30  36  
#7  14  21  28  35  42  49  
#8  16  24  32  40  48  56  64  

for i in range(1, r + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()
    
########################################

#Pyramid of numbers up to 10
#1 
#2 3 
#4 5 6 
#7 8 9 10

current_num = 1
stop = 2
for i in range(r):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop = stop 1

########################################
#Simple half pyramid pattern
#* 
#* * 
#* * * 
#* * * * 
#* * * * *

for i in range(0, r):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")

########################################

Right triangle pyramid of Stars Pattern
#        * 
#      * * 
#    * * * 
#  * * * * 
#* * * * * 

k = 2 * r - 2
for i in range(0, r):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")
    
########################################

#Downward half-Pyramid Pattern of Star
#* * * * *  
#* * * *  
#* * *  
#* *  
#*

for i in range(r + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")
    
########################################

#Downward full Pyramid Pattern of star
#        * * * * * * 
#         * * * * * 
#          * * * * 
#           * * * 
#            * * 
#             * 

k = 2 * r - 2
for i in range(r, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
    
########################################

#Right down mirror star Pattern
#*****
# ****
#  ***
#   **
#    *

i = r
while i >= 1:
    j = r
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1
    
########################################

#Equilateral triangle pattern of star
#            *   
#           *  *   
#          *  *  *   
#         *  *  *  *   
#        *  *  *  *  *   
#       *  *  *  *  *  *   
#      *  *  *  *  *  *  *   

m = (2 * r) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
    
########################################

#Print two pyramids of stars
#*  
#* *  
#* * *  
#* * * *  
#* * * * *  
#* * * * * *  
# 
#* * * * * *  
#* * * * *  
#* * * *  
#* * *  
#* *  
#*  

for i in range(0, r):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(r + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
    
########################################

#Right start pattern of star
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#* 

for i in range(0, r):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(r, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
    
########################################

#Left triangle pascal’s pattern
#        * 
#      * * 
#    * * * 
#  * * * * 
#* * * * * 
#  * * * * 
#    * * * 
#      * * 
#        * 

i = 1
while i <= r:
    j = i
    while j < r:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = r
while i >= 1:
    j = i
    while j <= r:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
    
########################################

#Sandglass pattern of star
#* * * * * 
# * * * * 
#  * * * 
#   * * 
#    * 
#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * * 

i = 0
while i <= r - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= r - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = r - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
    
########################################

#Pant style pattern of stars
#****************
#*******__*******
#******____******
#*****______*****
#****________****
#***__________***
#**____________**
#*______________*

print("*" * r, end="\n")
i = (r // 2) - 1
j = 2
while i != 0:
    while j <= (r - 2):
        print("*" * i, end="")
        print("_" * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2
        
########################################

#Diamond-shaped pattern of stars
#        * 
#       * * 
#      * * * 
#     * * * * 
#    * * * * * 
#   * * * * * * 
#    * * * * * 
#     * * * * 
#      * * * 
#       * * 
#        * 

k = 2 * r - 2
for i in range(0, r):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = r - 2

for i in range(r, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
########################################

#Middle empty diamond pattern of star
#    *
#   * *
#  *   *
# *     *
#*       *
# *     *
#  *   *
#   * *
#    *

i = 1
while i <= r:
    j = r
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = r - 1
while i >= 1:
    j = r
    while j > i:
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i -= 1
    
########################################

#Pattern to display letter of the word
#P
#Py
#Pyt
#Pyth
#Pytho
#Python

word = "Python"
x = ""
for i in word:
    x += i
    print(x)

########################################


"""
The program will take the students grades from the Final.txt and count how many 
grades are in the file. Next it will return to the user how many grades there where.
It will then add up all the grades and divide by the number of grades 
there were to determine the class grade average and return that number to the user.
Lastly, it will calculate the percentage of grades that are above the class average
and return that number to the user.
"""

"""
def main
    open list
    count list
    close list
return results

def main
    open list
    add numbers in list / 24
return results

def main
    open list
    determine grades above class average
return results
"""

def numberofgrades(Final):
    with open(Final) as f:
        for i, l in enumerate(f):
            pass
        return i + 1
print("Number of grades:", numberofgrades("Final.txt"))

def averagegrade(Final):
    numbersfile = open("Final.txt", "r")

    total = 0

    for line in numbersfile:
        averagegrade = total + int(line)

print("Average grade:", averagegrade) 
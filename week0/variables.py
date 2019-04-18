# http://www.codeskulptor.org/iipp-practice-experimental/#user46_aCRmf6SW1D_0.py

# Compute the number of feet corresponding to a number of miles.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
miles = 13


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#miles = 57


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#miles = 82.67


###################################################
# Miles to feet conversion formula
# Student should enter formula on the next line.

feet = miles * 5280

###################################################
# Test output
# Student should not change this code.

print str(miles) + " miles equals " + str(feet) + " feet."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#13 miles equals 68640 feet.

# Test 2 output:
#57 miles equals 300960 feet.

# Test 3 output:
#82.67 miles equals 436497.6 feet.

# http://www.codeskulptor.org/iipp-practice-experimental/#user46_vvDdEJADKq_0.py

# Compute the number of seconds in a given number of hours, minutes, and seconds.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
hours = 7
minutes = 21
seconds = 37


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#hours = 10
#minutes = 1
#seconds = 7


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#hours = 1
#minutes = 0
#seconds = 1


###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter formula on the next line.

total_seconds = (hours * 60 + minutes) * 60 + seconds

###################################################
# Test output
# Student should not change this code.

print str(hours) + " hours, " + str(minutes) + " minutes, and",
print str(seconds) + " seconds totals to " + str(total_seconds) + " seconds."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
# Test 1 output:
#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.

# Test 2 output:
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.

# Test 3 output:
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.

# Compute the distance between the points (x0, y0) and (x1, y1).

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
x0 = 2
y0 = 2
x1 = 5
y1 = 6


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#x0 = 1
#y0 = 1
#x1 = 2
#y1 = 2


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#x0 = 0
#y0 = 0
#x1 = 3
#y1 = 4

# http://www.codeskulptor.org/iipp-practice-experimental/#user46_JzfZGkKgW7_0.py

###################################################
# Distance formula
# Student should enter formula on the next line.

# Hint: You need to use the power operation ** .

distance = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** (1 / 2.0)

###################################################
# Test output
# Student should not change this code.

print "The distance from (" + str(x0) + ", " + str(y0) + ") to", 
print "(" + str(x1) + ", " + str(y1) + ") is " + str(distance) + "."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The distance from (2, 2) to (5, 6) is 5.0.

# Test 2 output:
#The distance from (1, 1) to (2, 2) is 1.41421356237.

# Test 3 output:
#The distance from (0, 0) to (3, 4) is 5.0.

# http://www.codeskulptor.org/iipp-practice-experimental/#user46_q6tone2C75_0.py

# Compute the area of a triangle (using Heron's formula),
# given its side lengths.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
x0, y0 = 0, 0
x1, y1 = 3, 4
x2, y2 = 1, 1


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#x0, y0 = -2, 4
#x1, y1 = 1, 6
#x2, y2 = 2, 1


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#x0, y0 = 10, 0
#x1, y1 = 0, 0
#x2, y2 = 0, 10


###################################################
# Triangle area (Heron's) formula
# Student should enter formulas on the next lines.

def side_length(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2.0)

a = side_length((x0, y0), (x1, y1))
b = side_length((x1, y1), (x2, y2))
c = side_length((x2, y2), (x0, y0))
s = (1 / 2.0) * (a + b + c)
area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2.0)

###################################################
# Test output
# Student should not change this code.

print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
print "(" + str(x1) + "," + str(y1) + "), and",
print "(" + str(x2) + "," + str(y2) + ") has an area of " + str(area) + "."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.

# Test 2 output:
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.

# Test 3 output:
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
#mouse to coordinates.py
#Written by: David (Dawid) Pietrzyk
#July 26, 2022

#all can be done using internal python packages
'''
#externally imported packages
import win32api, win32con
'''

#internally imported packages
import ctypes

#make variable for user32
user32 = ctypes.windll.user32

# hard coded aspect ratio (max for x and y of coordinates)
aspectRatio = (16,9)

#get the amount of pixel of the given monitor screen
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# hard coded coordinates (x,y)
coordinates = (8,4.5)

print("Let's say your screen aspect ratio of your screen is 16:9.\n")

#TUPLES ARE NOT MUTABLE 
'''
#coordiList = list(coordinates)

#coordiList[0] = input("Enter your x value of your coordinate \n")
#coordiList[1] = input("Enter your y value of your coordinate \n")

#coordinates = tuple(coordiList)

#coordinates[0] = int(coordinates[0])
#coordinates[1] = int(coordinates[1])
'''

#get percent of coordinate to the apspect ratio

getX = coordinates[0] / aspectRatio[0]
getY = coordinates[1] / aspectRatio[1]

#for testing
'''
#print(getX)
#print(getY)
#print(screensize)
#print(screensize[0])
#print(screensize[1])
#print(xPositionCursor)
#print(yPositionCursor)
'''

#calculate the x and y position depending on pixels
xPositionCursor = getX * screensize[0]
yPositionCursor = getY * screensize[1]

#typecast to int 
xPositionCursor = int(xPositionCursor)
yPositionCursor = int(yPositionCursor)

#set the mouse cursor to that point
ctypes.windll.user32.SetCursorPos(xPositionCursor, yPositionCursor)

print("Your cursor should now be at: ",coordinates)
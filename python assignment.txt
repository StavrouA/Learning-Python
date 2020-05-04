data_list = [["John", "Physics", 5],["John", "Programming", 7],["John", "Mathematics", 8], ["Marie", "Physics", 6], ["Marie", "Programming", 10], ["Marie", "Linear Algebra", 7], ["Helen", "Physics", 7], ["Helen", "Programming", 6], ["Helen", "Linear Algebra", 8], ["Helen", "Analysis", 10], ["Pantelis", "Programming", 10], ["Pantelis", "Mathematics", 8], ["Pantelis", "Analysis", 6], ["Pantelis", "Biology", 6], ["Michael", "Analysis", 10]]

print("data_list:")
print(*data_list, sep = "\n")									#print lsit
print("\n") 

#QUESTION 1
n = len(data_list)												    #list length

sorted_names = [0]*n										  	  #list initialization

for i in range(n):
  sorted_names[i] = data_list[i][0]						#list with all of the names from "data_list"

sorted_names.sort()												    #ordered name list
x = len(set(sorted_names))										#number of different names in the list
names = [0]*x												        	#initialize a 5x1 list
names[0] = sorted_names[0]										#initialize first value of the list with a name
counter = 1													        	#counter to keep track of the row

for i in range(1,n):
  if sorted_names[i] != sorted_names[i-1]:			
    names[counter] = sorted_names[i]					#creating a list with all of the name values
    counter+=1
  
print("Question 1 \n")
print("The ascending order of the names is the following:")		
print(names,"\n")												      #print names in ascending order

#QUESTION 2
sorted_courses = [0]*n											  #list initialization

for i in range(n):
  sorted_courses[i] = data_list[i][1]				  #list with all of the courses from "data_list"

sorted_courses.sort(reverse=True)							#descending order of the courses
y = len(set(sorted_courses))									#number of different courses in the list
courses = [0]*y													      #initialize a 6x1 list
courses[0] = sorted_courses[0]								#initialize first value of the list with a course
counter = 1														        #counter to keep track of the row

for i in range(1,n):
  if sorted_courses[i] != sorted_courses[i-1]:			
    courses[counter] = sorted_courses[i]			#creating a lsit with all of the courses values
    counter+=1

print("Question 2\n")
print("The ascending order of the courses is the following:")
print(courses,"\n")												    #print courses in descending order

#QUESTION 3
names_and_courses = [["0"]*(y+1) for i in range(x)]				#initialize a 5x7 list with zeros for the names and the courses

for i in range(x):
  names_and_courses[i][0] = names[i]					#putting names in the first column
    

for i in range(x):							
  counter = 1
  for j in range(n):
    if names_and_courses[i][0] == data_list[j][0]:				#if the names of the 2 lists match
      names_and_courses[i][counter] = data_list[j][1]			#put the name of the course in the next column
      counter+=1												      #increase counter by 1 since now this column is not zero

#sublists for each student to delete zeros

John = [i for i in names_and_courses[0] if i != "0"]	
Helen = [i for i in names_and_courses[1] if i != "0"]
Marie = [i for i in names_and_courses[2] if i != "0"]
Michael = [i for i in names_and_courses[3] if i != "0"]
Pantelis = [i for i in names_and_courses[4] if i != "0"]

names_and_courses = [John, Helen, Marie, Michael, Pantelis]	#merging the lists

print("Question 3 \n")
print(*names_and_courses, sep = "\n")							#print lsit
print("\n")

#QUESTION 4

courses_and_names = [["0"]*(x+1) for i in range(y)]				#create a 6x6 list for the courses and names
 
for i in range(y):
  courses_and_names[i][0] = courses[i]				#putting the courses in the first column
  

for i in range(y):							
  counter = 1
  for j in range(n):
    if courses_and_names[i][0] == data_list[j][1]:				#if the courses match
      courses_and_names[i][counter] = data_list[j][0]			#put the name in the column
      counter+=1												                  #increase counter since column is no longer zero

#sublists for each course to delete zeros

Physics = [i for i in courses_and_names[0] if i != "0"]			
Programming = [i for i in courses_and_names[1] if i != "0"]	
Mathematics = [i for i in courses_and_names[2] if i != "0"]	
Linear_Algebra = [i for i in courses_and_names[3] if i != "0"]	
Biology = [i for i in courses_and_names[4] if i != "0"]	
Analysis = [i for i in courses_and_names[5] if i != "0"]	

courses_and_names = [Physics, Programming, Mathematics, Linear_Algebra, Biology, Analysis] #merge lists

print("Question 4 \n")											#print list
print(*courses_and_names, sep = "\n") 
print("\n")

#QUESTION 5

names_and_stats = [["0"]*(3) for i in range(x)]	#create a 5x3 list for the students and their stats

for i in range(x):
  names_and_stats[i][0] = names[i]							#putting students names in the first column
  names_and_stats[i][1] = len(names_and_courses[i])-1 		#taking the number of courses from "names_and_courses" list
  total = 0													            #a sum to find average  
  for j in range(len(data_list)):							  #if names match, add to the total
    if names_and_stats[i][0] == data_list[j][0]:
      total += data_list[j][2]
  names_and_stats[i][2] = round(total/names_and_stats[i][1],2)	#get a rounded average (2 digits)
 
print("Question 5 \n")			
print(*names_and_stats, sep = "\n")							#print list
print("\n")

#QUESTION 6

courses_and_stats = [["0"]*(3) for i in range(y)]	#create 3x6 list for the courses and their stats

for i in range(y):
  courses_and_stats[i][0] = courses[i]						#put courses in first column
  courses_and_stats[i][1] = len(courses_and_names[i])-1 	#the number of courses taken by "courses_and_names"
  total = 0													          #total to find average
  for j in range(len(data_list)):							#if courses match, add to the total
    if courses_and_stats[i][0] == data_list[j][1]:
      total += data_list[j][2]
  courses_and_stats[i][2] = round(total/courses_and_stats[i][1],2)	#get a rounded average (2 digits)
 
print("Question 6 \n")			
print(*courses_and_stats, sep = "\n")						#print list
print("\n")

#QUESTION 7

total = 0													#initialize sum

for i in range(x):
  if names_and_stats[i][2] >= 8.5:  #find number of students with grade greater than 8.5
    total = total+1
    
perc = (total/x)*100                #find the respective percentage

print("Question 7 \n")			
print("The percentage of students with grade greater than 8.5 is", perc, "%\n")		#print %
print("\n")

#QUESTION 8

max1 = courses_and_stats[0][1]							#initialize max value 
max_course = courses_and_stats[0][0]        #the respective course

for i in range(1,y):
  if courses_and_stats[i][1] > max1:				
    max1 = courses_and_stats[i][1]						#if its greater than max, replace max value
    max_course = courses_and_stats[i][0]      #also, replace the respective course

print("Question 8 \n")			
print("The most-selected course is", max_course, ", which was selected by", max1, "students. \n")		#print course and number of students
print("\n")

#QUESTION 9

print("Question 9 \n")			
print("Choose and option:")	
print("\t 1. Find the percentage of students with grade greater than 8.5.")
print("\t 2. Find what courses a student has taken.")
print("\t 3. Find the course with most students attending.")
print("\t 0. Quit program. \n")

test = 0

while test == 0:
  ans = int(input("Your option (choose 0 to exit):"))
  if ans == 1:
    print("The percentage of students with grade greater than 8.5 is", perc, "%\n")
  elif ans == 2:
      test2 = 0
      while test2 == 0:
        ans2 = str(input("Student's name:"))
        for i in range(x):
          if ans2 == names_and_courses[i][0]:
           print(ans2, "has taken the following courses:")
           test2 = 1
           for j in range(1,len(names_and_courses[i])):
             print(names_and_courses[i][j])
        if test2 == 0:
          if ans2 == "0":
            print("Quit program.")
            test2 = 1
          else:
            print("There is no student with this name, try another name or 0 to exit:")
  elif ans == 3:
      print("The most-selected course is", max_course, ", which was selected by", max1, "students. \n")
  elif ans == 0:
  	print("Quit Program.")
  	test = 1
  else:
      print("Choose a right option, an integer from 0 to 3. To exit the program, press 0.")
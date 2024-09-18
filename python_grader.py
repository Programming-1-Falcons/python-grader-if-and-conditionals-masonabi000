'''0 - 50% = F
51% - 60% = D
61% - 75% = C
76% - 88% = B
89% - 100% = A'''

# establish points possible and what the student earned
points_possible = float(input("Max points student can earn on this assignemnt?: "))
points_earned = float(input("How many points did this student earn?: "))

#calculate percentage
percentage_earned = float(( points_earned / points_possible ) * 100)

#find letter grade
if percentage_earned < 51:
    print("Grade: F")

elif percentage_earned < 60 and percentage_earned >= 51 :
    print ("Grade: D")

elif percentage_earned >= 60 and percentage_earned < 75:
    print ("Grade: C")

elif percentage_earned >= 75 and percentage_earned < 88:
    print ("Grade: B")

else:
    print ("Grade: A")




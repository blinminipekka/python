# my_set = {1,2,3}
# #my_set = set()
# #my_set = set({4,5,6})
#
# #print(my_set)
# #
# #
# # set1 = {1, 2 , 3}
# # set2 = {3, 4, 5}
# #
# # union_result_method = set1.union(set2)
# # print ("Union: ", union_result_method)
# #
# #
# # union = set1 | set2
# # print("Union Method:", union)
# #
# # intersection = set1 & set2
# # print("Intersection Method:", intersection)
# #
# # difference = set1 - set2
# # print("Difference Method:", difference)
# #
# # symmetrical_difference = set1 ^ set2
# # print("Symmetrical Difference Method:", symmetrical_difference)
#
# #Set Methods
#
# my_set = {1, 2 , 3}
#
# my_set.add(4)
# my_set.remove(3)
# my_set.discard(1)
# my_set.clear()
#
# print(my_set)
#
# set_length = len(my_set)
# print("Length of set: ", set_length)
#
#
# Using sets - removing duplicates
#
#
# my_list = [1, 2, 2, 3, 3, 4, 5]
#
# unique_set = set(my_list)
#
# unique_list = list (unique_set)
#
# print(unique_list)
#
#
#
# # IN and NOT IN
#
# loyalty_members = {"Alice", "Bob", "Charlie"}
#
# customer = "Bob"
#
# is_member = customer in loyalty_members
#
# print(is_member)


# age = 18
#
# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")
#
#
#
#


# temp = 28
#
# if temp > 30:
#     print("It's a hot day")
# elif 20 <+ temp <= 30:
#     print("It's a good day")
# else:
#     print("It's a cold day")
#
#
student_gpa = 4.5
student_score = 75

if student_gpa >= 3.5:
    if 50 <= student_score <= 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} may be eligible for a partial scolarship.")
    elif student_score > 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} may be eligible for a full scolarship.")
    else:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a partial scolarship.")

else:
    print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a partial scolarship.")














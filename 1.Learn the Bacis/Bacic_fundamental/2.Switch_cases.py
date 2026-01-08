"""
Given the integer day denoting the day number, print on the screen which day of the week it 
is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
Ensure only the 1st letter of the answer is capitalised.

Example 1
Input: day = 3
Output: Wednesday

Example 2
Input: day = 8
Output: Invalid

"""
day=int(input("Enter a number between 1-7 :"))
match day:
    case 1:
        result="Monday"
    case 2:
        result="tuesday"
    case 3:
        result="wednesday"
    case 4:
        result="thursday"
    case 5:
        result="Friday"
    case 6:
        result="saturday"
    case 7:
        result="Sunday"
    case _:
        result="unknown"

print(result)
# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!

"""
def show_excitement():
    # Your code goes here!
    " ".join(["I am super excited for this course!"] * 5)
    return ""

print(show_excitement())
"""

def show_excitement():
    # Your code goes here!
    return "I am super excited for this course! " * 5

print(show_excitement())



"""
def show_excitement(str,n):
    global result
    if(n==0):
        return result.strip()
    else:
        result=result+" "+str
        return show_excitement(str,n-1)


result = ""
i="I am super excited for this course!"
print(show_excitement(i,5))
"""

"""
for i in range(5):
    print("Printing...")
    """

"""
def show_excitement():
    # Your code goes here!
    # excitement = "I am super excited for this course!"
    #i = 0
    #while i < 5:
    for i in range(5):
        return "I am super excited for this course!"
    #i = i + 1

print(show_excitement())"""
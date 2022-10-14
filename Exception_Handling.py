# Syntax :-

# try:
    # Code Block
    # these statements are those which can probably have error.

# except:
    # This block is optional.
    # If the try block encounters an exception, this block will handle it.

# else:
    # If there is no exception, this code block will be excuted by the python interpreter
    
# finally
    # python interpreter will always excute this code.
    
    
# Examples of Exception Handling :-

# 1 Zero Division Error :

# try:
#     print ("try block.")
#     x=int(input ("Enter a number : "))
#     y=int(input ("Enter another number : "))
#     z=x/y
# except ZeroDivisionError:
#     print ("except ZeroDivisionError block.")
#     print("Division by zero is not accepted.")
# else:
#     print ("else block.")
#     print("Division = ",z)
# finally:
#     print("finally block.")
#     x=0
#     y=0
# print ("Out of try,except,else and finally blocks.")   

# 2 Raise an exception.

# try:
#     x=int(input ("Enter a number upto 100 : "))
#     if x>100:
#         raise ValueError(x)
# except ValueError:
#     print(x, " is out of allowed range.")
# else:
#     print(x, "is within allowed range.")

# ------------------------------------------------------
#                      Assignment
# ------------------------------------------------------

print("Assignment")


blog_posts = [{'Photos':3,'Likes':21,'Comments':2,},{'Likes':13,'Comments':2,'Shares':1},
              {'Photos':5,'Likes':33,'Comments':8,'Shares':3},{'Comments':4,'Shares':2},
              {'Photos':8,'Comments':1,'Shares':1},{'photos':3,'Likes':19,'Comments':3}]
total_likes = 0

for post in blog_posts:
    try:
        post.keys() == "Likes"
        total_likes = total_likes + post['Likes']
    except:
        pass
    if("Likes" not in post.keys()):
        post['Likes']=0
print("Total likes : ",total_likes)
print("Updated dictionary : ",blog_posts)
          

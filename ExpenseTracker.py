import os
import pwd

# Define a function 'get_username' to retrieve the username of the current user.
def get_username():
    # Use 'os.getuid()' to get the user ID of the current user, and then pass it to 'pwd.getpwuid' to get the user information.
    # The '[0]' index extracts the username from the user information.
    return pwd.getpwuid(os.getuid())[0]

# Call the 'get_username' function and print the result to the console.
print(get_username())
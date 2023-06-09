# Jordan Allen

# Set identifiers
originalPassWord = input()
passWord = ''

# Use a for loop and change the characters of the original string to their new values
for char in originalPassWord:
    if char == 'i':
        passWord = passWord + '!'
    elif char == 'a':
        passWord = passWord + '@'
    elif char == 'm':
        passWord = passWord + 'M'
    elif char == 'B':
        passWord = passWord + '8'
    elif char == 'o':
        passWord = passWord + '.'
    else:
        passWord = passWord + char

# Finish the new password by adding the final string
passWord = passWord + 'q*s'

# Display the result
print(passWord)

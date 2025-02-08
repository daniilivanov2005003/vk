def get_user(line):
    file = open("users.txt", "r")
    counter = 0
    while (True):
        user = file.readline()
        if (counter < line):
            break
    user = user.split(':')
    return(user)

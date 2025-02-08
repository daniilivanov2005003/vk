def get_user(line):
    file = open("users.txt", "r")
    counter = 0
    while (True):
        user = file.readline()
        if (counter == line):
            break
        counter += 1
    user = user.split(':')
    return(user)

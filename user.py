def get_user(user_number):
    file = open("users.txt", "r")
    counter = 0
    while (True):
        parameters = file.readline()
        if (counter == user_number):
            break
        counter += 1
    parameters = parameters.split(':')
    file.close()
    if (parameters == ['']):
        return(None)
    else:
        user = {}
        user.update({'username' : parameters[0]})
        if (parameters[1][-1:] == '\n'):
            user.update({'password' : parameters[1][:-1]})
        else:
            user.update({'password' : parameters[1]})
        return(user)
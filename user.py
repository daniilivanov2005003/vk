def get_user(user_number):
    with open('users.txt', 'r') as f:
        try:
            user = f.readlines()[user_number].strip().split(':')
        except IndexError:
            return None
        return {'username': user[0], 'password': user[1]}
    
print(get_user(1))
    
    
    #with open('users.txt', 'r') as f:
    #    for index, line in enumerate(f):
    #        if index == user_number:
    #            parametrs = line.strip().split(':')
    #            if len(parametrs) < 2:
    #                return None
    #            return {'username': parametrs[0], 'password': parametrs[1]}

    #file = open("users.txt", "r")
    #counter = 0
    #while (True):
    #    parameters = file.readline()
    #    if (counter == user_number):
    #        break
    #    counter += 1
    #parameters = parameters.split(':')
    #file.close()
    #if (parameters == ['']):
    #    return(None)
    #else:
    #    user = {}
    #    user.update({'username' : parameters[0]})
    #    if (parameters[1][-1:] == '\n'):
    #        user.update({'password' : parameters[1][:-1]})
    #    else:
    #        user.update({'password' : parameters[1]})
    #    return(user)
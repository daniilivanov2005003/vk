def get_proxy(proxy_number):
    file = open("proxys.txt", "r")
    counter = 0
    while (True):
        parameters = []
        for i in range(4):
            parameters.append(file.readline())
            if (i <= 2):
                parameters[i] = parameters[i].replace('\n', '')
        if (counter == proxy_number):
            break
        counter += 1
    file.close()
    if (parameters[0] == ''):
        return(None)
    else:
        proxy = {}
        proxy.update({'username' : parameters[0]})
        proxy.update({'password' : parameters[1]})
        proxy.update({'adress' : parameters[2]})
        proxy.update({'port' : parameters[3]})
        return(proxy)
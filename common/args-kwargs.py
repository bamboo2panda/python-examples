def greet_me(**kwargs):
    print (kwargs['fname'])
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


if __name__ == '__main__':
    greet_me(fname="yasoob")
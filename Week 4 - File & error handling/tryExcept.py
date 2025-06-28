#try lets you test a block of code for errors.
#except lets you handle the error
#else lets you execute code when there is no error
#finally lets you excecute code regardless of the result

try:
    print(x)
except:
    print("An exception occurred")
#Above it tries to print x, but an error occurs because x is not defined
#since it tried and failed, it runs the command in the except


#Example of try/except with specific error handling(it specifically looks at if it is a NameError)
try:
    print(x)
except NameError:
    print('Variable x is not defined')
except:
    print("Something else went wrong")


#Example of try/except with else

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("nothing went wrong")


#Finally block will always execute regardless of error
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("the 'try except' is finished")


#trying to open and write to a file that is not writable

try:
    f = open('demofile.txt')
    try:
        f.write("Lorum ipsum")
    except:
        print("something went wrong when opening the file ")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")



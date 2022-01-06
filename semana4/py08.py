def hello_func():
    """ function that returns hello world"""
    print('Hello World !')
    print("")

hello_func()
print(hello_func)


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["Math", "Art"]
info = {'name':"Jhon", 'age': 22}
print("")
student_info(courses, info)
print("")
student_info(*courses, **info)


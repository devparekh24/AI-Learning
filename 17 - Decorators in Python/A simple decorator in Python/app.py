user = {"username": "Jhon Doe", "role": "admin"}


# using function
def user_has_secure_connection(fun):
    if user.get("role") == "admin":
        return fun
    # else:
    #     return "Access Denied"
    raise RuntimeError


def my_fun():
    return "password for the admin panel is 1234"


check_sec_connection = user_has_secure_connection(my_fun)
print(check_sec_connection())


# using decorator
def checking_secure_connection_decorator(fun):
    def wrapper():
        if user.get("role") == "admin":
            return fun()
        else:
            return "Access Denied"
        # raise RuntimeError

    return wrapper


checked = checking_secure_connection_decorator(my_fun)
print(checked())

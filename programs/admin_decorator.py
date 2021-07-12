def admin_required(func):
    def wrapper(user_type, pin):
        if user_type != 'admin':
            raise Exception("You are not allowed")
        else:
            return func(user_type, pin)
    return wrapper


@admin_required
def change_pin(user, pin):
    my_pin = pin
    return str(my_pin) + " new pin"


@admin_required
def del_acc(user, acc_no):
    return str(acc_no) + " deleted"


print(change_pin('admin', 1234))
print(del_acc('admin', 1000))

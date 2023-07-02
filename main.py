

bot_on = True


contact_dict = {"name" : "phone"}


def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except UnboundLocalError:
            print('Enter command')
            return func(*args)        
        except TypeError:
            print('Name not found in dictionary...')
            return func(*args)
        except KeyError:
            print('Not name given! Enter name after command...')
            return func(*args)
        except IndexError:
            print('Only one argumet given! Require name or phone number! Try again...')
            return func(*args)
    return inner()


def helper(*args):
    res = ''
    for key in comands.keys():
        res += f"-{key}\n"
    return  "\n | Available bot functions:|\n{:<10}\n".format(res)


def error(*args):
    return "Unknown command"


def add(*args):
        name = args[0]
        phone = args[1]
        if not name.isalpha():
            return "Name must be alphabetic! Try again..."
        elif not phone.isdigit():
            return "Number must be numerical! Try again..."
        else:
            contact_dict.update({name: phone})
            return "Add success"


def hello(*args):
    return 'How can I help you?'


def change(*args):
    name = args[0]
    new_phone = args[1]
    if name in contact_dict.keys():
        contact_dict[name] = new_phone
        return f"{name} : {new_phone}"
    raise IndexError


def phone(*args):
    name = args[0]
    return f"{name} : {contact_dict[name]}"

def show_all(*args):
    res = ''
    for name, phone in contact_dict.items():
        res += f"{name} : {phone} \n"
    return res


comands =  {'hello':hello,
            'add': add,
            'change':change,
            'phone':phone,
            'show_all':show_all,
            'help':helper,
            }  


@input_error
def main():             #Вирішую робити через таку структуру щоб програма одразу оцінювала те що вводиться з консолі, як на мене такий варіант є логічним так як можна в будьякий момент додати нові ключі в команди і записати під кожен ключ нову окрему функцію. Також усі варіанти окрім ключів-функцій одразу відсіюються. А при правильному введені функції скрипт повертає одразу значення з потрібної функції.

    while True:
        user_input = input(">>> ")
        key_word = user_input.split()
        if user_input in ("good bye", "close", "exit"): #такий варіант доречний бо можна додати у будь-який момент значення для завершення скрипту
            print("Good bye!")
            break
        elif key_word[0] not in comands.keys(): # усе крім ключів повератє не правильне значення.
            result = error(user_input) 
            print(result) 
        else:
            for key in comands.keys():          #скрипт знаходить ключ у введеному в консоль повідомленні і підставляє значення у відповідну функцію
                comand = user_input.lower()
                        
                if comand.startswith(key):
                    func = comands.get(key)
                    args = comand.replace(key, "").strip().split()
                    result = func(*args)
                    print(result)



if __name__ == "__main__":
    main()
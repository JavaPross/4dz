result = []
def divider(a, b):
 if a < b:
    raise ValueError("vALUEeRROR")
 if b > 100:
    raise IndexError('iNDEXERROR')
 return a / b
data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ZeroDivisionError:
        print("деление на ноль")
    except ValueError:
        print("ошибка ввода")
    except NameError:
        print("плохое имя")
        
        

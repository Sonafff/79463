result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більше або рівне b")
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль")
        if b > 100:
            raise IndexError("b має бути менше або рівне 100")
        return a/b
    except ValueError as ve:
        print("ValueError:", ve)
    except ZeroDivisionError as zde:
        print("ZeroDivisionError:", zde)
    except IndexError as ie:
        print("IndexError:", ie)

data = {10: 2, 2: 5, 123: 4, 18: 0, 7: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)

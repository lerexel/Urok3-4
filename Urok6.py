import warnings


warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('always', ImportWarning)


warnings.warn("warning no code here", SyntaxWarning)
warnings.warn("warning import", ImportWarning)



try:
    first = int(input("Введіть 1 число"))
    second = int(input("Введіть 2 число"))
    result = first / second
    print('Results:', result)
except ZeroDivisionError:
    print("Помилка ділення на нуль")
except ValueError:
    print("pomulka bibevena dani uisla")


except:
    pass





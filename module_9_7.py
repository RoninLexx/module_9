def is_prime(func):
    def wrapper(*args, **kwargs):
        # Вызываем функцию sum_three, чтобы получить результат
        result = func(*args, **kwargs)

        # Проверяем, является ли результат простым числом
        if result < 2:
            print("Составное")  # Числа меньше 2 не являются простыми
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

# Декоратор is_prime:
# Аргументом является функция func, которую мы декорируем.
# Внутри is_prime определена функция wrapper, которая принимает произвольное количество аргументов (*args и **kwargs),
# чтобы обрабатывать вызовы функции sum_three.
# Внутри wrapper мы вызываем функцию func (т.е. sum_three) с переданными аргументами и
# сохраняем результат в переменной result.
# Затем происходит проверка: если result меньше 2, мы печатаем "Составное". Если больше или равно 2, мы проверяем,
# делится ли нацело на числа от 2 до квадратного корня из result. В случае нахождения делителя выводим "Составное".
# Если делителей нет, выводим "Простое".
# Функция sum_three:
# Этой функции присваивается декоратор @is_prime.
# Она просто принимает три числа и возвращает их сумму.
# Пример использования:
# Мы вызываем sum_three(2, 3, 6), что дает в результате 11, проверяется на простоту и напечатается "Простое",
# после чего результат 11 будет также выведен на экран.
# ... надо постараться это запомнить....

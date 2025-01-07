# Реализация нормальныго алгоритма Маркова на Python.

# Ранее я много пытался написать свой интерпретатор/компилятор для существующего языка программирования или для придуманного мною.
# Но всегда забрасывал это дело то ли из-за нехватки решимости, то ли из-за незнания теории.
# Этот файлик - попытка начать с чистого листа, с самых основ.
# Чуть позже напишу интерпретатор машины Тьюринга :)

# чистая функция D:
def algorithm(string: str, rules: dict[str, str]) -> list[str]:
    steps: list[str] = [string]

    while True:
        modified = False

        for key in rules.keys():
            last_step = steps[-1]
            if last_step.find(key) != -1:
                steps.append(last_step.replace(key, rules[key], 1))
                modified = True
                break

        if not modified:
            break

    return steps

def print_steps(steps: list[str]) -> None:
    for n, step in enumerate(steps):
        print(f"{n}. {step}")
    print()

if __name__ == "__main__":
    # Примеры из Википедии.
    rules = {
        "А": "апельсин",
        "кг": "килограмм",
        "М": "магазинчике",
        "Т": "том",
        "магазинчике": "ларьке",
        "в том ларьке": "на том рынке",
    }
    input_string = "Я купил кг Аов в Т М."
    print_steps(algorithm(input_string, rules))

    # Преобразование чисел из двоичной СС в единичную (унарную) СС
    rules = {
        "1": "0|",
        "|0": "0||",
        "0": "",
    }
    input_string = "101"
    print_steps(algorithm(input_string, rules))

    # Пробела остановки (https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0_%D0%BE%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8)
    # существует и здесь. Следующая "программа" будет работать вечно.
    rules = {
        "1": "0",
        "0": "1",
    }
    input_string = "101"
    print_steps(algorithm(input_string, rules))

# Этот файл написан благодаря статье на Википедии: https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC

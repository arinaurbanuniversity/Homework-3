from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

compare_chars = lambda f, s: list(map(lambda x, y: x == y, f, s))
result = compare_chars(first, second)

print("Результат сравнения букв:", result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print("Ответы магического шара:")
print(first_ball())
print(first_ball())
print(first_ball())

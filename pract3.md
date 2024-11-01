# Практическое занятие №3. Конфигурационные языки

## Задача 1
Реализовать на `Jsonnet` приведенный ниже пример в формате `JSON`. Использовать в реализации свойство программируемости и принцип `DRY`.
### Решение:
```jsonnet
{
  groups: ["ИКБО-1-20", "ИКБО-2-20", "ИКБО-3-20", "ИКБО-4-20", "ИКБО-5-20", 
           "ИКБО-6-20", "ИКБО-7-20", "ИКБО-8-20", "ИКБО-9-20", "ИКБО-10-20", 
           "ИКБО-11-20", "ИКБО-12-20", "ИКБО-13-20", "ИКБО-14-20", "ИКБО-15-20",
           "ИКБО-16-20", "ИКБО-17-20", "ИКБО-18-20", "ИКБО-19-20", "ИКБО-20-20", 
           "ИКБО-21-20", "ИКБО-22-20", "ИКБО-23-20", "ИКБО-24-20", "ИКБО-63-23"],

  students: [
    { name: "Иванов И.И.", age: 19, group: "ИКБО-4-20" },
    { name: "Петров П.П.", age: 20, group: "ИКБО-5-20" },
    { name: "Сидоров С.С.", age: 18, group: "ИКБО-6-20" },
    { name: "Нартаджиев А.Р..", age: 18, group: "ИКБО-63-23" },
  ]
}
```
### Результат:
![image](https://github.com/user-attachments/assets/ebb8180b-17ee-43f1-8bbc-6b9a71d9a646)


## Задача 2
Реализовать на `Dhall` приведенный ниже пример в формате `JSON`. Использовать в реализации свойство программируемости и принцип `DRY`.
### Решение:
```dhall
-- Файл: students.dhall

let Group = List Text
let Student = { age : Natural, group : Text, name : Text }

let studentsData = 
      { groups = [ "ИКБО-1-20", "ИКБО-2-20", "ИКБО-3-20", "ИКБО-4-20", "ИКБО-5-20",
                   "ИКБО-6-20", "ИКБО-7-20", "ИКБО-8-20", "ИКБО-9-20", "ИКБО-10-20",
                   "ИКБО-11-20", "ИКБО-12-20", "ИКБО-13-20", "ИКБО-14-20", "ИКБО-15-20",
                   "ИКБО-16-20", "ИКБО-17-20", "ИКБО-18-20", "ИКБО-19-20", "ИКБО-20-20",
                   "ИКБО-21-20", "ИКБО-22-20", "ИКБО-23-20", "ИКБО-24-20", "ИКБО-63-23" ] : Group,
      
        students = 
            [ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }
            , { age = 20, group = "ИКБО-5-20", name = "Петров П.П." }
            , { age = 18, group = "ИКБО-6-20", name = "Сидоров С.С." }
            , { age = 18, group = "ИКБО-63-20", name = "Нартаджиев А.Р." }
            ] : List Student
      }

in studentsData
```
### Результат:
![image](https://github.com/user-attachments/assets/fccda954-1993-4863-afc1-a5e657850a76)

# `#`
Для решения дальнейших задач потребуется программа на Питоне, представленная ниже.

```Python
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
E = a
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))

```

Реализовать грамматики, описывающие следующие языки (для каждого решения привести БНФ). Код решения должен содержаться в переменной BNF:

## Задача 3

Язык нулей и единиц.
### Решение:
```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
E = 10 | 100 | 11 | 101101 | 000
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
### Результат:
![image](https://github.com/user-attachments/assets/c191f75a-bcf2-456a-bcf4-015225c91034)


## Задача 4

Язык правильно расставленных скобок двух видов.
### Решение:
```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
E = (E) | {E} | E E | ''
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```

### Результат:
![image](https://github.com/user-attachments/assets/699c1454-b233-431b-900f-5cca663945aa)


## Задача 5
Язык выражений алгебры логики.

### Решение:
```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
E = E & E | E | E | ~E | (E) | x | y
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
### Результат:
![image](https://github.com/user-attachments/assets/d981959a-1a09-4e26-a3da-18904947a2d8)


## Полезные ссылки

Configuration complexity clock: https://mikehadlow.blogspot.com/2012/05/configuration-complexity-clock.html

Json: http://www.json.org/json-ru.html

Язык Jsonnet: https://jsonnet.org/learning/tutorial.html

Язык Dhall: https://dhall-lang.org/

Учебник в котором темы построения синтаксических анализаторов (БНФ, Lex/Yacc) изложены подробно: https://ita.sibsutis.ru/sites/csc.sibsutis.ru/files/courses/trans/LanguagesAndTranslationMethods.pdf

Полезные материалы для разработчика (очень рекомендую посмотреть слайды и прочие ссылки, все это актуально и для других тем нашего курса): https://habr.com/ru/company/JetBrains-education/blog/547768/

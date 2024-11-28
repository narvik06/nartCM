# Практическое занятие №5. Вопросы виртуализации

## Задача 1
Исследование виртуальной стековой машины CPython.

Изучите возможности просмотра байткода ВМ CPython.
```
import dis

def foo(x):
    while x:
        x -= 1
    return x + 1

print(dis.dis(foo))
```
Опишите по шагам, что делает каждая из следующих команд (приведите эквивалентное выражение на Python):
```
 11           0 LOAD_FAST                0 (x)
              2 LOAD_CONST               1 (10)
              4 BINARY_MULTIPLY
              6 LOAD_CONST               2 (42)
              8 BINARY_ADD
             10 RETURN_VALUE
```

### Решение:
Разбор байткода:
```
LOAD_FAST 0 (x)
Загружает значение переменной x из локальных переменных в стек.

LOAD_CONST 1 (10)
Загружает константу 10 в стек.

BINARY_MULTIPLY
Выполняет операцию умножения над двумя элементами в стеке. В нашем случае, это умножение значения x на 10 (значение, загруженное на предыдущем шаге).

LOAD_CONST 2 (42)
Загружает константу 42 в стек.

BINARY_ADD
Выполняет операцию сложения на верхних двух значениях в стеке. Это сложение результата умножения (полученного на шаге 3) с константой 42.

RETURN_VALUE
Возвращает результат из текущей функции (или завершает выполнение кода, если это основной код).
```
Эквивалентное выражение:
```python
def foo(x):
    return (x * 10) + 42
```

### Результат:
Просмотр байткода:
```
  3           RESUME                   0

  4           LOAD_FAST                0 (x)
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L2)

  5   L1:     LOAD_FAST                0 (x)
              LOAD_CONST               1 (1)
              BINARY_OP               23 (-=)
              STORE_FAST               0 (x)

  4           LOAD_FAST                0 (x)
              TO_BOOL
              POP_JUMP_IF_FALSE        2 (to L2)
              JUMP_BACKWARD           14 (to L1)

  6   L2:     LOAD_FAST                0 (x)
              LOAD_CONST               1 (1)
              BINARY_OP                0 (+)
              RETURN_VALUE
None

```


## Задача 2
Что делает следующий байткод (опишите шаги его работы)? Это известная функция, назовите ее.
```
  5           0 LOAD_CONST               1 (1)
              2 STORE_FAST               1 (r)

  6     >>    4 LOAD_FAST                0 (n)
              6 LOAD_CONST               1 (1)
              8 COMPARE_OP               4 (>)
             10 POP_JUMP_IF_FALSE       30

  7          12 LOAD_FAST                1 (r)
             14 LOAD_FAST                0 (n)
             16 INPLACE_MULTIPLY
             18 STORE_FAST               1 (r)

  8          20 LOAD_FAST                0 (n)
             22 LOAD_CONST               1 (1)
             24 INPLACE_SUBTRACT
             26 STORE_FAST               0 (n)
             28 JUMP_ABSOLUTE            4

  9     >>   30 LOAD_FAST                1 (r)
             32 RETURN_VALUE
```

### Решение:
Функция - вычисление факториала.
```
# Инициализация r
LOAD_CONST               1 (1)
STORE_FAST               1 (r)

# Условие цикла while n > 1
>> 4 LOAD_FAST           0 (n)
LOAD_CONST               1 (1)
COMPARE_OP               4 (>)
# Если условие ложно, прыжок на адрес 30 (выход из цикла).
POP_JUMP_IF_FALSE       30

# Умножение на месте
LOAD_FAST                1 (r)
LOAD_FAST                0 (n)
INPLACE_MULTIPLY
STORE_FAST               1 (r)

# Декрементирование n
LOAD_FAST                0 (n)
LOAD_CONST               1 (1)
INPLACE_SUBTRACT
STORE_FAST               0 (n)

# Переход к началу цикла
JUMP_ABSOLUTE            4

# Возврат результата
>>   30 LOAD_FAST        1 (r)
RETURN_VALUE
```


## Задача 3
Приведите результаты из задач 1 и 2 для виртуальной машины JVM (Java) или .Net (C#).

### Задача 3.1

### Решение:


### Результат:



### Задача 3.2

### Решение:



## Задача 4
Работа с qemu. Скачать и установить ISO-образ Alpine Linux для виртуальных машин с официального сайта.
Создать с помощью qemu образ жесткого диска (опция -f qcow2). Объем диска 500 Мб.
Запустить Alpine Linux с CD-ROM.
Установить систему на sda. Изменить motd.
Загрузиться уже с sda.
Прислать полный список команд для установки и загрузки, а также скриншот с motd, где фигурируют ваши имя и фамилия.

### Решение:


### Результат:



## Задача 5
(после разбора на семинаре и написания у доски базовой части эмулятора древней игровой приставки CHIP-8)
1. Реализовать вывод на экран.
2. Добиться запуска Тетриса.
3. Реализовать ввод с клавиатуры.
4. Добиться успешной работы всех приложений.

[Архив эмулятора CHIP-8](chip.zip)

### Решение:


### Результат:




## Полезные ссылки

Compiler Explorer: https://godbolt.org/

Байткод CPython: https://docs.python.org/3/library/dis.html

QEMU для Windows: https://www.qemu.org/download/#windows
http://sovietov.com/tmp/mqemu.zip

Документация по QEMU: https://www.qemu.org/docs/master/system/index.html

Старая документация по QEMU (рус.): https://www.opennet.ru/docs/RUS/qemu_doc/

Образы Alpine Linux: https://alpinelinux.org/downloads/

Документация по игровому компьютеру CHIP-8: http://devernay.free.fr/hacks/chip8/C8TECH10.HTM

Учебник по созданию миниатюрной ОС: https://www.cs.bham.ac.uk/~exr/lectures/opsys/10_11/lectures/os-dev.pdf

Nasm: https://nasm.us/

Прерывания BIOS: http://www.ctyme.com/intr/int.htm

Игры в загрузочном секторе: https://github.com/nanochess/Invaders

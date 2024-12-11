# Практическое задание №4. Системы контроля версий

Работа с Git.

## Задача 1
На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ (цвета могут отличаться, есть команды undo/redo) с помощью команд эмулятора git получить следующее состояние проекта (сливаем master с first, перебазируем second на master): см. картинку ниже. Прислать свою картинку.
![](images/git.png)

### Решение:
```
git commit
git tag in
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout in
```

### Результат:
![image](https://github.com/user-attachments/assets/d4047dbf-ea34-4b7e-b5cb-e5dd7dc982b5)


## Задача 2
Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.

### Решение-Результат:
```cmd
Задача2-3>git init local
Initialized empty Git repository in C:/Users/narvik/Desktop/MIREA/КонфУ/pract4/Задача2-3/local/.git/

Задача2-3>cd local

Задача2-3\local>git config user.email qwe1@nevo.com

Задача2-3\local>git config user.name qwe1

Задача2-3\local>echo print("Sorry for the late deadline!") > sorry.py

Задача2-3\local>git add .

Задача2-3\local>git commit -m "first"
[master (root-commit) ae4ffcb] first
 1 file changed, 1 insertion(+)
 create mode 100644 sorry.py
```


## Задача 3
Создать рядом с локальным репозиторием bare-репозиторий с именем server. Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 с server.
Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее – coder2). Добавить файл readme.md с описанием программы. Обновить сервер.
Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.
Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.
Прислать список набранных команд и содержимое git log.
Пример лога коммитов:
```
*   commit a457d748f0dab75b4c642e964172887de3ef4e3e
|\  Merge: 48ce283 d731ba8
| | Author: Coder 2 <coder2@corp.com>
| | Date:   Sun Oct 11 11:27:09 2020 +0300
| | 
| |     readme fix
| | 
| * commit d731ba84014d603384cc3287a8ea9062dbb92303
| | Author: Coder 1 <coder1@corp.com>
| | Date:   Sun Oct 11 11:22:52 2020 +0300
| | 
| |     coder 1 info
| | 
* | commit 48ce28336e6b3b983cbd6323500af8ec598626f1
|/  Author: Coder 2 <coder2@corp.com>
|   Date:   Sun Oct 11 11:24:00 2020 +0300
|   
|       coder 2 info
| 
* commit ba9dfe9cb24316694808a347e8c36f8383d81bbe
| Author: Coder 2 <coder2@corp.com>
| Date:   Sun Oct 11 11:21:26 2020 +0300
| 
|     docs
| 
* commit 227d84c89e60e09eebbce6c0b94b41004a4541a4
  Author: Coder 1 <coder1@corp.com>
  Date:   Sun Oct 11 11:11:46 2020 +0300
  
      first commit
```

### Решение:
```cmd
Задача2-3>git init --bare server

Задача2-3>cd local

Задача2-3\local>git remote add server ..\server

Задача2-3\local>git push server master

Задача2-3\local>git remote -v

Задача2-3\local>git pull server master

Задача2-3\local>cd ..

Задача2-3>mkdir local2

Задача2-3>git clone server local2

Задача2-3>cd local2

Задача2-3\local2>git config user.email qwe2@nevo.com

Задача2-3\local2>git config user.name qwe2

Задача2-3\local2>echo Чета делаит > readme.md

Задача2-3\local2>git add .

Задача2-3\local2>git commit -m "second"

Задача2-3\local2>git remote add server ..\server

Задача2-3\local2>git push server master

Задача2-3\local2>git remote remove origin

Задача2-3\local2>git status

Задача2-3\local2>cd ..\local

Задача2-3\local>git pull server master

Задача2-3\local>(echo. && echo "Авторы: qwe1, qwe1@nevo.com") >> readme.md

Задача2-3\local>git add .

Задача2-3\local>git commit -m "third"

Задача2-3\local>git push server master

Задача2-3\local>cd ..\local2

Задача2-3\local2>(echo. && echo "Авторы: qwe2, qwe2@nevo.com") >> readme.md

Задача2-3\local2>git add .

Задача2-3\local2>git commit -m "third"

Задача2-3\local2>git pull server master

Задача2-3\local2>git mergetool

Задача2-3\local2>git add .

Задача2-3\local2>git commit -m "conflict resolved third"

Задача2-3\local2>git push server master

Задача2-3\local2>cd ..\local

Задача2-3\local>git pull server master
```

### Результат:
```cmd
C:\Users\narvik\Desktop\MIREA\КонфУ\pract4\Задача2-3\local>git log --graph --all
*   commit 8a4e84b81cf07839f4201422a1b83783db7d6526 (HEAD -> master, server/master)
|\  Merge: 671b104 22db68f
| | Author: qwe2 <qwe2@nevo.com>
| | Date:   Mon Nov 18 01:38:57 2024 +0300
| |
| |     conflict resolved third
| |
| * commit 22db68f7290ddb7f3da0fd817d72b77c3f0ffb41
| | Author: qwe1 <qwe1@nevo.com>
| | Date:   Mon Nov 18 00:49:56 2024 +0300
| |
| |     third
| |
* | commit 671b104a43e3fd25bb261492ba74b9d28a7114f0
|/  Author: qwe2 <qwe2@nevo.com>
|   Date:   Mon Nov 18 00:56:44 2024 +0300
|
|       third
|
* commit 934b72efc47eefd2b34bdab0062a14396cfc6919
| Author: qwe2 <qwe2@nevo.com>
| Date:   Sun Nov 17 23:52:14 2024 +0300
|
|     second
|
* commit ae4ffcbd546429b423390fe75fd98c404ca27f26
  Author: qwe1 <qwe1@nevo.com>
  Date:   Sun Nov 17 23:29:34 2024 +0300
```


## Задача 4
Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.

### Решение:
```python
import subprocess

def get_git_objects():
    # Получаем список всех объектов в репозитории
    result = subprocess.run(['git', 'rev-list', '--objects', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    objects = result.stdout.splitlines()

    for obj in objects:
        # Получаем хеш объекта
        obj_hash = obj.split(' ')[0]

        # Получаем информацию о типе объекта с помощью git cat-file
        result = subprocess.run(['git', 'cat-file', 'commit', obj_hash], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:  # Если не коммит (например, блоб или дерево)
            result = subprocess.run(['git', 'cat-file', 'blob', obj_hash], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                result = subprocess.run(['git', 'cat-file', 'tree', obj_hash], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode != 0:
                    print(f"Failed to get object {obj_hash}")
                    continue
                object_type = "tree"
            else:
                object_type = "blob"
        else:
            object_type = "commit"

        # Выводим комментарий о типе объекта
        print(f"Object {obj_hash} ({object_type}):")
        print(result.stdout)
        print("\n---\n")

if __name__ == '__main__':
    get_git_objects()
```

### Результат:
```
C:\Users\narvik\Desktop\MIREA\КонфУ\pract4\Задача4\local>python objects.py
Object 8a4e84b81cf07839f4201422a1b83783db7d6526 (commit):
tree 0f4751d28c222d2f2049635c3d970101be28ca38
parent 671b104a43e3fd25bb261492ba74b9d28a7114f0
parent 22db68f7290ddb7f3da0fd817d72b77c3f0ffb41
author qwe2 <qwe2@nevo.com> 1731883137 +0300
committer qwe2 <qwe2@nevo.com> 1731883137 +0300

conflict resolved third


---

Object 671b104a43e3fd25bb261492ba74b9d28a7114f0 (commit):
tree 39193c2cca39201e7cec9b289d447c1d242d10f5
parent 934b72efc47eefd2b34bdab0062a14396cfc6919
author qwe2 <qwe2@nevo.com> 1731880604 +0300
committer qwe2 <qwe2@nevo.com> 1731880604 +0300

third


---

Object 22db68f7290ddb7f3da0fd817d72b77c3f0ffb41 (commit):
tree c10cc6363774d56a651cc16c618e4b8c6f0b16dc
parent 934b72efc47eefd2b34bdab0062a14396cfc6919
author qwe1 <qwe1@nevo.com> 1731880196 +0300
committer qwe1 <qwe1@nevo.com> 1731880196 +0300

third


---

Object 934b72efc47eefd2b34bdab0062a14396cfc6919 (commit):
tree fa938cb206193ee2b08a59525a15f431e3cb8ec4
parent ae4ffcbd546429b423390fe75fd98c404ca27f26
author qwe2 <qwe2@nevo.com> 1731876734 +0300
committer qwe2 <qwe2@nevo.com> 1731876734 +0300

second


---

Object ae4ffcbd546429b423390fe75fd98c404ca27f26 (commit):
tree 05bd15740ba4a4c8ec4e089e30b43709b3c824a3
author qwe1 <qwe1@nevo.com> 1731875374 +0300
committer qwe1 <qwe1@nevo.com> 1731875374 +0300

first


---

Object 0f4751d28c222d2f2049635c3d970101be28ca38 (tree):
100644 readme.md \‰,Жв”П.Ы™†BЃїь"f2aП100644 sorry.py ћ=ВOГB¶♣b¤№¤БiФur+

---

Object 5c892cc6e294cf2edb99864281bffc22663261cf (blob):
—Ґв  ¤Ґ« Ёв


"Ђўв®ал: qwe2, qwe2@nevo.com"

"Ђўв®ал: qwe1, qwe1@nevo.com"



---

Object 9e3dc24fc342b60562a4b9a4c169d475fd08722b (blob):
print("Sorry for the late deadline!")
```

## Полезные ссылки

Git

Учебник (рус.): https://git-scm.com/book/ru/v2

Шпаргалка (рус.): https://training.github.com/downloads/ru/github-git-cheat-sheet/

Официальная документация: https://git-scm.com/docs

Эксцентричный доклад Л. Торвальдса о Git: https://www.youtube.com/watch?v=4XpnKHJAok8

Дерево Меркла: http://cryptowiki.net/index.php?title=Дерево_Merkle

Git for Windows: https://git-scm.com/download/win

Репозиторий chibicc: https://github.com/rui314/chibicc.git

Игра по git: https://learngitbranching.js.org/?locale=ru_RU

SHA-1

Описание алгоритма: https://ru.wikipedia.org/wiki/SHA-1

Вероятность хеш-коллизии: https://preshing.com/20110504/hash-collision-probabilities/

https://ru.m.wikipedia.org/wiki/Парадокс_дней_рождения

https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html

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

### Решение:
```
git init
git config user.name "narvik"
git config user.email "nrtdzh@gmail.com"
echo print("Hello, World!") > test.py
git add test.py
git commit -m "first commit"
```

### Результат:
```
C:\Users\narvik\Desktop\MIREA\КонфУ\pract4\Задание2>git init
Initialized empty Git repository in C:/Users/narvik/Desktop/MIREA/КонфУ/pract4/Задание2/.git/

C:\Users\narvik\Desktop\MIREA\КонфУ\pract4\Задание2>git config user.name "narvik"

C:\Users\narvik\Desktop\MIREA\КонфУ\pract4\Задание2>git config user.email "nrtdzh@gmail.com"

C:\Users\narvik\Desktop\MIREA\КонфУ\pract4\Задание2>echo print("Hello, World!") > test.py

C:\Users\narvik\Desktop\MIREA\КонфУ\pract4\Задание2>git add test.py

C:\Users\narvik\Desktop\MIREA\КонфУ\pract4\Задание2>git commit -m "first commit"
[master (root-commit) 1434286] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 test.py

C:\Users\narvik\Desktop\MIREA\КонфУ\pract4\Задание2>git log
commit 14342863c1062c47c447a218c806b0b2c12bfdd2 (HEAD -> master)
Author: narvik <nrtdzh@gmail.com>
Date:   Fri Nov 15 12:26:10 2024 +0300

    first commit
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


### Результат:
```
C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3>git init local
Initialized empty Git repository in C:/Users/narvik/Desktop/МИРЭА/КонфУ/pract4/Задание3/local/.git/

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3>cd local

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git config user.email qwe1@nevo.com

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git config user.name qwe1

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>echo print("Sorry for the late deadline!") > sorry.py

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git add .

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git commit -m "first"
[master (root-commit) ae4ffcb] first
 1 file changed, 1 insertion(+)
 create mode 100644 sorry.py

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>cd ..

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3>git init --bare server
Initialized empty Git repository in C:/Users/narvik/Desktop/МИРЭА/КонфУ/pract4/Задание3/server/

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3>cd local

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git remote add server ..\server

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git push server master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 238 bytes | 238.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ..\server
 * [new branch]      master -> master

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git remote -v
server  ..\server (fetch)
server  ..\server (push)

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git pull server master
From ..\server
 * branch            master     -> FETCH_HEAD
Already up to date.

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>cd ..

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3>mkdir local2

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3>git clone server local2
Cloning into 'local2'...
done.

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3>cd local2

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git config user.email qwe2@nevo.com

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git config user.name qwe2

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>echo Чета делаит > readme.md

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git add .

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git commit -m "second"
[master 934b72e] second
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git remote add server ..\server

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git push server master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 275 bytes | 275.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ..\server
   ae4ffcb..934b72e  master -> master

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git remote remove origin

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git status
On branch master
nothing to commit, working tree clean

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>cd ..\local

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git pull server master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 255 bytes | 31.00 KiB/s, done.
From ..\server
 * branch            master     -> FETCH_HEAD
   ae4ffcb..934b72e  master     -> server/master
Updating ae4ffcb..934b72e
Fast-forward
 readme.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>(echo. && echo "Авторы: qwe1, qwe1@nevo.com") >> readme.md

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git add .

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git commit -m "third"
[master 22db68f] third
 1 file changed, 2 insertions(+)

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git push server master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 304 bytes | 304.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ..\server
   934b72e..22db68f  master -> master

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>cd ..\local2

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>(echo. && echo "Авторы: qwe2, qwe2@nevo.com") >> readme.md

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git add .

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git commit -m "third"
[master 671b104] third
 1 file changed, 2 insertions(+)

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git pull server master
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 284 bytes | 35.00 KiB/s, done.
From ..\server
 * branch            master     -> FETCH_HEAD
   934b72e..22db68f  master     -> server/master
Auto-merging readme.md
CONFLICT (content): Merge conflict in readme.md
Automatic merge failed; fix conflicts and then commit the result.

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git mergetool

This message is displayed because 'merge.tool' is not configured.
See 'git mergetool --tool-help' or 'git help config' for more details.
'git mergetool' will now attempt to use one of the following tools:
tortoisemerge emerge vimdiff nvimdiff
Merging:
readme.md

Normal merge conflict for 'readme.md':
  {local}: modified file
  {remote}: modified file
Hit return to start merge resolution tool (vimdiff):
4 files to edit

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git add .

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git commit -m "conflict resolved third"
[master 8a4e84b] conflict resolved third

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git push server master
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 16 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 625 bytes | 625.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ..\server
   22db68f..8a4e84b  master -> master

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local2>git status
On branch master
nothing to commit, working tree clean

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git log --graph --all
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

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git status
On branch master
nothing to commit, working tree clean

C:\Users\narvik\Desktop\МИРЭА\КонфУ\pract4\Задание3\local>git pull server master
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), 605 bytes | 43.00 KiB/s, done.
From ..\server
 * branch            master     -> FETCH_HEAD
   22db68f..8a4e84b  master     -> server/master
Updating 22db68f..8a4e84b
Fast-forward
 readme.md | 4 ++++
 1 file changed, 4 insertions(+)
```


## Задача 4
Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.

### Решение:


### Результат:



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

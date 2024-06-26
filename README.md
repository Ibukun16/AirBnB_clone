# AirBnB Clone
![hbnb](https://github.com/Ibukun16/AirBnB_clone/assets/81274116/55fb97e5-4b78-4c22-9846-707791da4805)

## Description:
This is a Team project, to build a clone of [AirBnB](https://www.airbnb.com/). 
This project is very important for an aspiring full-stack engineer because it will be used to execute other projects like; HTML/CSS templating, database storage, API, front-end integration and the likes. 

# AirBnB_Console - The Console
## 0x00. Table of Contents

- [0x01 Introduction](#0x01-Introduction)
- [0x02 Environment](#0x02-Environment)
- [0x03 Installation](#0x03-Installation)
- [0x04 Testing](#0x04-Testing)
- [0x05 Usage](#0X05-Usage)
- [0x06 Authors](#0x06-Author)
  
## 0x01 Introduction
The project is in phases. This phase is the first step towards building a full web application: AirBnB clone. 
The first segment of the project which is the first task or phase 1, is to build a Console. 
The console is a command interpreter to manage objects' abstraction between objects and how they are stored.
To see the fundamental background of the project visit the [Wiki](https://en.wikipedia.org/wiki/Airbnb).

The console will perform the following tasks:

* Create a new object.
* Retrieve an object from a file.
* Do operations on objects.
* Destroy an object.

### Storage
All the classes are handled by the `Storage` engine in the `FileStorage` Class.


## 0x02 Environment ##
<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a> <!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> </a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>
 <!-- Style guidelines -->
* Style guidelines:
  - [pycodestyle (version 2.8.*)](https://pycodestyle.pycqa.org/en/2.8.0/)
  - [PEP8](https://peps.python.org/pep-0008/)

All the development and testing was runned over an operating system

**Ubuntu 20.04 LTS** using **Python 3.8.3 programming language**. 
The editors used were **VIM 8.1.2269, VSCode 1.6.1 and Atom 1.58.0** control version, using **Git 2.25.1**.

## 0x03 Installation

```bash
git clone https://github.com/aysuarex/AirBnB_clone.git
```
change to the `AirBnB` directory and run the command:

 ```bash
 ./console.py
```

* ### Execution
 
**In interactive mode**

```bash 
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
**In Non-interactive mode**
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## 0x04 Testing

All the tests are defined in the tests folder.

### Documentation

- _Modules_:
```
python3 -c 'print(__import__("my_module").__doc__)'
```
- _Classes_:
```
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```
- _Functions (inside and outside a class)_:
```
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```
and
```
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Python Unit Tests
- Unittest module
- File `extension .py`
- Files and folders star with `test_`
- Organization: for `models/base.py`, unit tests in: tests/test_models/test_base.py
- Execution command: `python3 -m unittest discover tests`
or: `python3 -m unittest tests/test_models/test_base.py`

### Run test in interactive mode
```
echo "python3 -m unittest discover tests" | bash
```
### Run test in non-interactive mode
To run the tests in non-interactive mode, and discover all the tests, you can use the command:
```
python3 -m unittest discover tests
```

## 0x05 Usage
- **Start the console in interactive mode**:
```
$ ./console.py
(hbnb)
```
- **Use help to see the available commands**:
```
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
```
- **Quit the console**:
```
(hbnb) quit
$
```
### Commands
> _The commands are displayed in the following format Command/usage/ example with output_

- **Create**
> _Creates a new instance of a given class. The class's ID is printed and the instance is saved to the file file.json_.
```
create <class>
```
```
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```
- **Show**
```
show <class> <id>
```
```
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```
- **Destroy**
> _Deletes an instance of a given class with a given ID. Update the file.json_
```
(hbnb) create User
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
```
**No instance found**
```
(hbnb)
```
- **All**
> _Prints all string representation of all instances of a given class. If no class is passed, all classes are printed_.
```
(hbnb) create BaseModel
e45ddda9-eb80-4858-99a9-226d4f08a629
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) [BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) {'id': '4c8f7ebc-257f-4ed1-b26b-e7aace459897', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447257), 'name': 'My First Model', 'my_number': 89}"]
["[BaseMode]]
```
- **Count**
> _Prints the number of instances of a given class_.
```
(hbnb) create City
4e01c33e-2564-42c2-b61c-17e512898bad
(hbnb) create City
e952b772-80a5-41e9-b728-6bc4dc5c21b4
(hbnb) count City
2
(hbnb)
```
- **Update**
> _Updates an instance based on the class name, id, and kwargs passed. Update the file.json_

## 0x06 Author
<details>
    <summary>AGUNBIADE Ibukun</summary>
    <ul>
    <li><a href="https://www.github.com/Ibukun16">Github</a></li>
    <li><a href="mailto:messageib.agunbiade18@gmail.com">e-mail</a></li>
    </ul>
</details>

### How to add Author file
```
Bash script for generating the list of authors in git repo
```
```
#!/bin/sh

git shortlog -se
| perl -spe 's/^\s+\d+\s+//'
| sed -e '/^CommitSyncScript.*$/d' 
```

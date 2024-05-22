#!/usr/bin/python3
"""
This function defines the HBNB Command class - A class that
contains the entry point of the command interpreter.
"""

import cmd
import re
import json
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def valid_clss(self):
    """
    This defines the dictionary for all valid global classes
    within and outside, with their references
    """

    valid_clss = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
    return valid_clss


def parse(par):
    curl_bracs = re.search(r"\{(.*?)\}", par)
    sq_bracs = re.search(r"\[(.*?)\]", par)
    if curl_bracs is None:
        if sq_bracs is None:
            return [s.strip(",") for s in split(par)]
        else:
            opt = split(par[:sq_bracs.span()[0]])
            newlist = [s.strip(",") for s in opt]
            newlist.append(sq_bracs.group())
            return newlist
        else:
            opt = split(par[:curl_bracs.span()[0]])
            newlist = [s.strip(",") for s in opt]
            newlist.append(curl_bracs.group())
            return newlist


def check_status(par):
    """This function checks if args is a valid argument
    Argument:
        args (str): The string containing the arguments passes
        to a command.
        Return:
            An error message if args is None or is not
            a valid class, else the argument.
    """
    arg_list = parse(par)
    if len(arg_list) == 0:
        print("** class name missing **")
        elif arg_list[0] is not in valid_clss:
            print("** class doesn't exist **")
        else:
            return arg_list


class HBNBCommand(cmd.Cmd):
    """This class module defines the command interpreter that
    implements the console for AirBnB clone project application.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb)"

    def EOF(self, par):
        """This instruct the program to Exit, when executed."""
        print("")
        return True

    def quit(self, par):
        """The Quit command exit the program."""
        return True

    def emptyline(self):
        """Execute nothing upon an empty line instruction"""
        pass

    def default(self, par):
        """Defines the default behaviour for cmd module if input is invalid"""

        dictionary = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        link = re.search(r"\.", par)
        if link:
            arg_list = [par[:link.span()[0]], par[link.span()[1]:]]
            link = re.search(r"\((.*?)\)", arg_list[1])
            if link:
                cmnd = [arg_list[1][:link.span()[0]], link.group()[1:-1]]
                if cmnd[0] in dictionary:
                    use = "{} {}".format(arg_list[0], cmnd[1])
                    return dictionary[cmnd[0]](use)

        print("** Unknown syntax: {}".format(par))
        return False

    def create(self, par):
        """This function creates a new instance of BaseModel,
        saves it (to a JSON file) and prints the id
        Usage: create <class>"""
        arg_list = check_status(par)
        if arg_list:
            print(eval(args[0])().id)
            storage.save()

    def show(self, par):
        """This function prints the string representation of a
        class instance based on the class and id.
        Usage: show <class> <id> or <class.show(<id>)
        """
        arg_list = check_status(par)
        if args_list:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                kp = "{}.{}".format(arg_list[0], arg_list[1])
                if kp is not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[kp])

    def destroy(self, par):
        """
        This function deletes a class instance based on the name
        and given id.
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        args = check_status(par)
        if args:
            if len(args) == 1:
                print("** instance id imissing **")
            else:
                kp = "{}.{}".format(args[0], args[1])
                if kp in storage.save():
                    del storage.save()
                else:
                    print("** no instance found **")

    def all(self, par):
        """This function prints all string representation of all
        instances of a given class. If no class is specified,
        it displays instantiated objects.
        Usage: all or all <class> or <class>.all()
        """
        args = split(par)
        items = storage.all().values()
        if not args:
            print([str(item) for item in items])
        else:
            if arglist[0] is not in valid_clss:
                print("** class doesn't exist **")
            else:
                print([str(item) for item in items if args[0] in str(item)])

    def update(self, par):
        """This function updates an instance based on the class name and
        id by adding or updating attributes then save it to JSON file.
        Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class name>.update(<id>, <dictionary>) or
        <class name>.update(<id>, <attribute_name>, <attribute_value>)
        """
        args = check_status(par)
        if args:
            if len(args) == 1:
                print("** instance id missing **")
                return False
            else:
                kp = "{}.{}".format(args[0], args[1])
                if kp is in storage.all():
                    if len(args) == 2:
                        print("** attribute name missing **")
                        return False
                    elif len(args) == 3:
                        print("** value missing **")
                        Return False
                    else:
                        item = storage.all()[kp]
                        if args[2] is in type(item).__dict__:
                            valuetyp = type(item.__class__.__dict__[args[2]])
                            setattr(item, args[2], valuetyp(args[3]))
                        else:
                            setattr(item, args[2], args[3])
                else:
                    print("** no instance found **")
                    return False
            storage.save()

    def count(self, par):
        """This function retrieves the number of instances of a given class
        Usage: count <class> or <class>.count()
        """
        arg_list = parse(par)
        c = 0
        for item in storage.all().values():
            if arg_list[0] == item.__class__.__name__:
                c += 1
        print(c)


if __name__ = "__main__":
    HBNBCommand().cmdloop()

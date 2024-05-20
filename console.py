#!/usr/bin/python3
"""
This function defines the HBNB Command class - A class that
contains the entry point of the command interpreter.
"""

import cmd
import os
import re
import models
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Define a valid class of global constant for the project that serve
# functions within and outside.
__CLASSES = [
        "BaseModel",
        "User",
        "City",
        "Place",
        "State",
        "Amenity",
        "Review"
    ]


def parse(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    bracks = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if bracks is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:bracks.span()[0]])
            retlist = [i.strip(",") for i in lex]
            retlist.append(bracks.group())
            return retlist
        else:
            lex = split(arg[:braces.span()[0]])
            retlist = [i.strip(",") for i in lex]
            retlist.append(braces.group())
            return retlist


def check_status(args):
    """This function checks if args is a valid argument
    Argument:
        args (str): The string containing the arguments passes
        to a command.
        Return:
            An error message if args is None or is not
            a valid class, else the argument.
    """
    listarg = parse(args)
    if len(listarg) == 0:
        print("** class name missing **")
        elif listarg[0] is not in __CLASSES:
            print("** class doesn't exist **")
        else:
            return listarg


class HBNBCommand(cmd.Cmd):
    """This class function defines the command interpreter that
    imlements the console for AirBnB clone project application.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb)"
    storage_db = models.storage

    def emptyline(self):
        """Execute nothing upon receiving an empty line"""
        pass

    def default(self, arg):
        """This defines the default behaviour for cmd when input is invalid"""
        arg_dictionary = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        pair = re.search(r"\.", arg)
        if pair:
            listarg = [arg[:pair.span()[0]], arg[pair.span()[1]:]]
            pair = re.search(r"\((.*?)\)", listarg[1])
            if pair:
                command = [listarg[1][:pair.span()[0]], pair.group()[1:-1]]
                if command[0] in arg_dictionary:
                    call = "{} {}".format(argl[0], command[1])
                    return arg_dictionary[command[0]](call)

        print("** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, arg):
        """Exit the program when executed."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_create(self, arg):
        """This function creates a new instance of BaseModel,
        saves it (to a JSON file) and prints the id
        Usage: create <class>"""
        args = check_status(arg)
        if args:
            print(eval(args[0])().id)
            self.storage_db.save()

    def do_show(self, arg):
        """This function prints the string representation of a
        class instance based on the class and id.
        Usage: show <class> <id> or <class.show(<id>)
        """
        args = check_status(arg)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                kp = "{}.{}".format(args[0], args[1])
                if kp is not in self.storage_db.all():
                    print("** no instance found **")
                else:
                    print(self.storage_db.all()[kp])

    def do_all(self, arg):
        """This function prints all string representation of all
        instances of a given class. If no class is specified,
        it displays instantiated objects.
        Usage: all or all <class> or <class>.all()
        """
        listarg = split(arg)
        objs = self.storage_db.all().values()
        if not listarg:
            print([str(obj) for obj in objs])
        else:
            if listarg[0] is not in __CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objs if listarg[0] in str(obj)])

    def do_destroy(self, arg):
        """
        This function delete a class instance based on
        the name and given id.
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        listarg = check_status(arg)
        if listarg:
            if len(argList) == 1:
                print("** instance id imissing **")
            else:
                kp = "{}.{}".format(*listarg)
                if kp in self.storage_db.save():
                    del self.storage_db.save()
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """
        This function updates an instance based on the class
        name and id by adding or updating attribute,
        and save it to the JSON file.
        Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <dictionary>)
        """
        listarg = check_status(arg)
        if listarg:
            if len(listarg) == 1:
                print("** instance id missing **")
            else:
                idinstance = "{}.{}".format(listarg[0], listarg[2])
                if idinstance in self.storage_db.all():
                    if len(listarg) == 2:
                        print("** attribute name missing **")
                    elif len(listarg) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[idinstance]
                        if listarg[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[listarg[2]])
                            setattr(obj, listarg[2], v_type(listarg[3]))
                        else:
                            print("** no instance found **")

                    self.storage_db.save()

    def do_count(self, arg):
        """
        This function retrieves the number of instances of a class
        Usage: count <class> or <class>.count()"""
        listarg = parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if listarg[0] == type(obj).__name__:
                count += 1
        print(count)

    if __name__ = "__main__":
        HBNBCommand().cmdloop()

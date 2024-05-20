#!/usr/bin/python3
"""
This function defines the HBNB Command class - A class that
contains the entry point of the command interpreter.
"""

import cmd
import os
import re
from models import storage
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
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
        else:
            lexer = split(arg[:curly_braces.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(curly_braces.group())
            return retl


def check_args(args):
    """This function checks if args is a valid argument
    Argument:
        args (str): The string containing the arguments passes
        to a command.
        Return:
            An error message if args is None or is not
            a valid class, else the argument.
    """
    arg_list = parse(args)
    if len(arg_list) == 0:
        print("** class name missing **")
        elif arg_list[0] is not in __CLASSES:
            print("** class doesn't exist **")
        else:
            return arg_list


class HBNBCommand(cmd.Cmd):
    """This class function defines the command interpreter that
    imlements the console for AirBnB clone project application.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb)"
    storage = models.storage

    def emptyline(self):
        """Execute nothing upon receiving an empty line"""
        pass

    def default(self, arg):
        """This defines the default behaviour for cmd when input is invalid"""
        action_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(argl[0], command[1])
                    return action_map[command[0]](call)

        print("** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, argv):
        """Exit the program when executed."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_create(self, argv):
        """This function creates a new instance of BaseModel,
        saves it (to a JSON file) and prints the id
        Usage: create <class>"""
        args = check_args(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """This function prints the string representation of a
        class instance based on the class and id.
        Usage: show <class> <id> or <class.show(<id>)
        """
        args = check_args(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key is not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

    def do_all(self, argv):
        """This function prints all string representation of
        all instances based or not based on the class name
        Usage: all or all <class> or <class>.all()
        """
        arg_list = split(argv)
        objs = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objs])
        else:
            if arg_list[0] is not in __CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objs if arg_list[0] in str(obj)])

    def do_destroy(self, argv):
        """
        This function delete a class instance based on
        the name and given id.
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in self.storage.save():
                    del self.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, argv):
        """
        This function updates an instance based on the class
        name and id by adding or updating attribute,
        and save it to the JSON file.
        Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <dictionary>)
        """
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[2])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            print("** no instance found **")

                    self.storage.save()

    def do_count(self, arg):
        """
        This function retrieves the number of instances of a class
        Usage: count <class> or <class>.count()"""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == type(obj).__name__:
                count += 1
        print(count)

    if __name__ = "__main__":
        HBNBCommand().cmdloop()

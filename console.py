#!/usr/bin/python3
"""The module contains the HBNBCommand class"""
import cmd
import re
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The class defines the command interpreter for the console,
    with the custom prompt (hbnb).

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    acpt_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    }

    def do_create(self, args):
        """
        This module creates a new class instance and print its id.

        Usage: create <class name>
        """
        if args:
            if args not in HBNBCommand.acpt_classes:
                print("** class doesn't exist **")
                return

            typ = eval(args.strip())
            typical = typ()
            print(typical.id)
            typical.save()
        else:
            print("** class name missing **")

    def do_show(self, args):
        """
        This function display the string representation of a
        class instance of a given id

        Usage: show <class name> <id> or <class name>.show(<id>)
        """
        if args:
            par = args.split()
            if par[0] not in HBNBCommand.acpt_classes:
                print("** class doesn't exist **")
            elif len(par) < 2:
                print("** instance id missing **")
            else:
                kp = storage.all()
                link = par[0] + "." + par[1]
                result = kp.get(link, None)
                if result:
                    print(result)
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """
        This function deletes a class instance of a given id

        Usage: destroy <class name> <id> or <class name>.destroy(<id>)
        """
        if args:
            par = args.split()
            if par[0] not in HBNBCommand.acpt_classes:
                print("** class doesn't exist **")
            elif len(par) < 2:
                print("** instance id missing **")
            else:
                kp = storage.all()
                link = par[0] + "." + par[1]
                result = kp.get(link, None)
                if result:
                    remove = kp.pop(link)
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """
        This module displays the string representations of all
        instances of a given class. If no class is specified,
        it displays all instantiated objects.

        Usage: all or all <class name> or <class name>.all()
        """
        kp = storage.all()
        if args:
            par = args.split()
            if par[0] in HBNBCommand.acpt_classes:
                arg_list = [
                    str(val) for key, val in kp.items()
                    if key.startswith(par[0])
                ]
                print(arg_list)
            else:
                print("** class doesn't exist **")
        else:
            clsargs = [str(val) for val in kp.values()]
            print(clsargs)

    def do_update(self, args):
        """
        This function updates a class instance of a given id by adding
        or updating a given attribute key/value pair.

        Usage: update <class name> <id> <attribute-name> <attribute_value>
        or <class>.update(<id>, <attribute_name>, <attribute_value>)
        """
        if args:
            par = args.split()
            if par[0] not in HBNBCommand.acpt_classes:
                print("** class doesn't exist **")
            elif len(par) == 1:
                print("** instance id missing **")
            else:
                kp = storage.all()
                link = par[0] + "." + par[1]
                result = kp.get(link, None)
                if result:
                    if len(par) == 2:
                        print("** attribute name missing **")
                    elif len(par) == 3:
                        print("** value missing **")
                    else:
                        try:
                            setattr(result, par[2],
                                    ast.literal_eval(par[3].strip()))
                        except (ValueError):
                            setattr(result, par[2], par[3])
                        result.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def _do_update_dict(self, args, cname):
        """Usage: <class name>.update(<id>, <dictionary representation>)"""
        par = args.split(',', 1)
        try:
            add_feat = ast.literal_eval(par[1].strip())
            if type(add_feat) is not dict:
                print("** Invalid dictionary **")
                return
            func = "{}.{}".format(classname, par[0].strip('"').strip())
            item = storage.all().get(func, None)

            if item is None:
                print("** no instance found **")
                return

            for k in add_feat:
                setattr(item, k, add_feat[k])
        except BaseException:
            print("** Invalid dictionary **")

    def _do_count(self, args):
        """
        This function retrieves the number of instances
        of a given class.

        Usage: <class name>.count() or count <class name>
        """
        match = args.split()[0]
        link = [k for k in storage.all().keys()
                if k.startswith(match)]
        print(len(link))

    def default(self, args):
        """
        This function execute the default console action
        on all other commands when the input is invalid
        """
        dictionary = {
            'count': self._do_count,
            'all': self.do_all,
            'show': self.do_show,
            'update': self.do_update,
            'destroy': self.do_destroy
        }
        match = args.split('.', 1)

        if len(match) == 1:
            print(f'*** Unknown syntax: {args}')
            return

        build = match[1].split("(", 1)

        if build[0] not in dictionary or len(build) < 2:
            print(f'*** Unknown syntax: {args}')
            return

        if (len(match[0].strip()) < 1):
            print("** class name missing **")
            return

        if (match[0] not in HBNBCommand.acpt_classes):
            print("** class doesn't exist **")
            return

        build[1] = build[1].strip()
        if len(build[1]) < 1 or build[1][-1] != ')':
            print(f'*** Unknown syntax: {args}')
            return
        par = build[1][:-1]

        if build[0] == 'update':

            if (len(par) < 1):
                print("** instance id missing **")
                return

            feature = par.split(',', 1)

            if len(feature) < 2:
                func = f'{match[0].strip()}.{feature[0].strip()}'
                av = storage.all().get(func, None)
                if av:
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
                return

            if feature[1].strip()[0] == '{':
                self._do_update_dict(par, match[0])
            else:
                par = par.strip().replace(',', '')
                kp = "{} {}".format(match[0], par)
                kp = kp.replace('"', '')
                return self.do_update(kp)
        else:
            kp = '{} {}'.format(match[0], par)
            return dictionary[build[0]](kp)

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """
        This function instruct the program to initiate quit on the
        command interpreter
        """
        print
        return True

    def emptyline(self):
        """
        This function instruct the console to do nothing
        when given an empty line instruction
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

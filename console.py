#!/usr/bin/python3
"""
The module that contains the entry point of the comand interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ The class for comand interpreter """
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_create(self, line):
        if len(line) < 1:
            print("** class name missing **")
        elif line not in HBNBCommand.l_classes:
            print("***")

    def do_EOF(self, line):
        """ EOF command to quite the program """
        return True

    def do_quit(self, line):
        """ Quite command to exit the program """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""
The module that contains the entry point of the comand interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ The class for comand interpreter """
    prompt = '(hbnb) '
    list_cls = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

    def emptyline(self):
        """ """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id """
        if len(line) < 1:
            print("** class name missing **")
        elif line not in HBNBCommand.list_cls:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id """

        if not line:
            print("** class name missing **")
            return
        
        line = line.split(' ')

        if line[0] not in HBNBCommand.list_cls:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if obj_name == line[0] and obj_id == line[1].strip('"'):
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id 
        (save the change into the JSON file). """
        if not line:
            print("** class name missing **")
            return
        
        line = line.split(' ')

        if line[0] not in HBNBCommand.list_cls:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if obj_name == line[0] and obj_id == line[1].strip('"'):
                    del v
                    del storage._FileStorage__objects[k]
                    storage.save()
                    return

            print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name """

        if not line:
            print("** class name missing **")
            return

        line = line.split(' ')

        if line[0] not in HBNBCommand.list_cls:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_inst = []
            for k, v in all_objs.items():
                obj_name = v.__class__.__name__
                if obj_name == line[0]:
                    list_inst += [v.__str__()]
            print(list_inst)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        if not line:
            print("** class name missing **")
            return

        a = ""

        for line in line.split(','):
            a = a + line

        line = shlex.split(a)

        if line[0] not in HBNBCommand.items():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if obj_name == line[0] and obj_id == line[1].strip('"'):
                    if len(line) == 2:
                        print("** attribute name missing **")
                    if len(line) == 3:
                        print("** value missing **")
                    else:
                        setattr(v, line[2], line[3])
                        storage.save()
                    return
            print("** no instance found **")
                
    def do_EOF(self, line):
        """ EOF command to quite the program """
        return True

    def do_quit(self, line):
        """ Quite command to exit the program """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

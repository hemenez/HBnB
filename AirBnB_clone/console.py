#!/usr/bin/python3
"""Console Module"""
import shlex
import cmd
import models
import models.engine


class HBNBCommand(cmd.Cmd):
    """Holberton AirBnb console
    """
    prompt = '(hbnb) '

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to a JSON file
        """
        my_line = shlex.split(line)
        if len(my_line) != 1:
            print('** class name missing **')
        elif my_line[0] not in models.classes:
            print('** class doesn\'t exist **')
        else:
            new_instance = models.classes[my_line[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints a string representation of an instance based on the class
        name and id
        """
        my_line = shlex.split(line)
        my_storage = models.storage._FileStorage__objects
        if len(my_line) == 0:
            print('** class name missing **')
        elif my_line[0] not in models.classes:
            print('** class doesn\'t exist **')
        elif len(my_line) == 1:
            print('** instance id missing **')
        elif '{}.{}'.format(my_line[0], my_line[1]) not in my_storage:
            print('** no instance found **')
        else:
            desired_key = my_line[0] + '.' + my_line[1]
            print(my_storage[desired_key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id. Changes are then
        saved into the JSON file
        """
        my_line = shlex.split(line)
        my_storage = models.storage._FileStorage__objects
        if len(my_line) == 0:
            print('** class name missing **')
        elif my_line[0] not in models.classes:
            print('** class doesn\'t exist **')
        elif len(my_line) == 1:
            print('** instance id missing **')
        elif '{}.{}'.format(my_line[0], my_line[1]) not in my_storage:
            print('** no instance found **')
        else:
            desired_key = my_line[0] + '.' + my_line[1]
            del my_storage[desired_key]
            models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances either based on
        class name or not. If not, it prints all instances. If a class is
        specified, it prints all instances of that class.
        """
        my_line = shlex.split(line)
        my_list = []
        my_storage = models.storage._FileStorage__objects
        if len(my_line) == 0:
            for k in my_storage:
                my_list.append(my_storage[k])
            print(my_list)
        elif my_line[0] not in models.classes:
            print('** class doesn\'t exist **')
        else:
            for k in my_storage:
                my_class, my_id = k.split('.')
                if my_line[0] == my_class:
                    my_list.append(my_storage[k])
            print(my_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating the attribute. Once updated, the change will be
        saved to the JSON file.
        """
        my_line = shlex.split(line)
        my_storage = models.storage._FileStorage__objects
        if len(my_line) == 0:
            print('** class name missing **')
        elif my_line[0] not in models.classes:
            print('** class doesn\'t exist **')
        elif len(my_line) == 1:
            print('** instance id missing **')
        elif '{}.{}'.format(my_line[0], my_line[1]) not in my_storage:
            print('** no instance found **')
        elif len(my_line) == 2:
            print('** attribute name missing **')
        elif len(my_line) == 3:
            print('** value missing **')
        else:
            my_key = '{}.{}'.format(my_line[0], my_line[1])
            attr_name = '{}'.format(my_line[2])
            if type(my_line[3]) is str:
                my_line[3] = my_line[3].replace('"', '')
            my_storage[my_key].__dict__[attr_name] = my_line[3]
            models.storage.save()

    def do_EOF(self, line):
        """Exits program if EOF is triggered
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_exit(self, line):
        """Exit command to quit the program
        """
        return True

    def emptyline(self):
        """Method will not execute anything if blank line is entered
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

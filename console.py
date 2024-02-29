#!/usr/bin/python3

from cmd import Cmd
from models.Basemodel import BaseModel
from models.Food import Food
from models.Ingredient import Ingredient
from models.Recipe import Recipe
from models.bridges.food_ingredients import Food_Ingredients
from models import storage


class RecipEaseCLI(Cmd):
    
    prompt = 'recipEase> '

    def do_quit(self, line):
        """Exits the program with a newline."""
        print('Bye!')
        return True
    
    def do_exit(self, line):
        """Exits the program with a newline."""
        print('Bye!')
        return True
    
    def do_EOF(self, line):
        """Exits the program."""
        print("Bye!")
        return True
    
    def do_help(self, arg):
        """Choose from (exit, quit, help, EOF) for help."""
        if arg:
            if hasattr(self, 'do_' + arg):
                doc = getattr(self, 'do_' + arg).__doc__
                if doc:
                    print(doc)
                else:
                    print(f'No help available for "{arg}"')
            else:
                print(f'Unknown command: "{arg}"')
    
    def __cmd_validation(usage, obj=None):
        for k, v in usage.items():
            if k == "class_name" and v == "":
                print("RecipEase Error: Class name missing 😴")
                return 0

            try:
                if k == "class_name":
                    eval(v)
            except NameError:
                print("RecipEase Error: Class doesn't exist 😒")
                return 0

            if v == "" and k == "obj_id":
                print("RecipEase Error: Instance id missing 🤨")
                return 0

        if obj is not None:
            for v in obj.values():
                if v.id == usage["obj_id"]:
                    break
            else:
                print("RecipEase Error: No instance found 🧐")
                return 0

        if "attributes" in usage:
            pass

    # _______________________________________________________________________________

    @staticmethod
    def __handle_usage(line, usage, doc):
        
        # split the line from each space character 
        args = line.split()

        # get the attributes part of the list
        attributes_args = [arg for arg in args if '=' in arg]

        # get the non attributes part of the list
        args = [arg for arg in args if '=' not in arg]

        # If command entered without any arguments, the function must return
        if len(args) < 1:
            return

        # If arguments are greater than the usage length - 1 then it means that there were too many arguments passed
        if len(args) > (len(usage) - 1):
            doc = doc[doc.find('Usage'):]
            print("RecipEase Error: Many Arguments have been entered! 😉\n"
                  f"{doc}")
            return -1

        # if len(usage) != 1:
        #     args = args[:len(usage) - 1]

        # Add the attributes to the attributes property
        if attributes_args:
            for att in attributes_args:
                [key, value] = att.split('=')

                attrs_obj = usage['attributes_args']

                attrs_obj[key] = value.replace('_', ' ').replace('"', '')

        # if len(args) < len(usage):
        #     for _ in range(len(usage) - len(args)):
        #         args.append("")

        i = 0

        for k in usage.keys():
            if i > len(args) - 1:
                break

            if k != 'attributes_args':
                usage[k] = args[i]

            i += 1

    # _______________________________________________________________________________
                
    def do_create(self, line):
        """Creates an instance (record) of a class (table) and save it to the DB.
Usage: create class_name att1=value1 att2=value2 att3=value3"""
        
        usage_create = {
            'class_name': '',
            'attributes_args': {}
        }

        if RecipEaseCLI.__handle_usage(line, usage_create, self.do_create.__doc__) == -1\
        or RecipEaseCLI.__cmd_validation(usage_create) == 0:
            return

        attributes = usage_create.get('attributes_args')

        if usage_create['class_name'] == 'Food_Ingredients':
            food_id = attributes.get('food_id')
            ingredient_id = attributes.get('ingredient_id')
            quantity = attributes.get('quantity')
            storage.append_ingredient_to_food(food_id, ingredient_id, quantity)
        else:
            cls = eval(usage_create.get('class_name'))
            obj = cls(**attributes)
            obj.save()
    
    # _______________________________________________________________________________
            
    def do_update(self, line):
        """Updates an instance (record) of a class (table) and save it to the DB.
Usage: update class_name obj_id att1=value1 att2=value2 att3=value3"""
        if line.split()[0] == 'Food_Ingredients':
            usage_update = {
            'class_name': '',
            'attributes_args': {}
            } 
        else:
            usage_update = {
                'class_name': '',
                'obj_id': '',
                'attributes_args': {}
            }

        if RecipEaseCLI.__handle_usage(line, usage_update, self.do_update.__doc__) == -1\
        or RecipEaseCLI.__cmd_validation(usage_update) == 0:
            return

        attributes = usage_update.get('attributes_args')
        obj_id = usage_update.get('obj_id')
        cls = eval(usage_update.get('class_name'))

        if cls == Food_Ingredients:
            food_id = attributes.get('food_id', None)
            ingredient_id = attributes.get('ingredient_id', None)
            quantity = attributes.get('quantity', None)
            food_ingredient_row = [food_id, ingredient_id, quantity]

            if None in food_ingredient_row:
                return

            storage.update_food_ingredient(food_id, ingredient_id, quantity)
            food = storage.get_obj_by_id(Food, food_id)

            if food:
                food.save()
            return

        try:
            obj = storage.get_obj_by_id(cls, obj_id)
            for k, v in attributes.items():
                setattr(obj, k, v)
            obj.save()
        except AttributeError:
            print('RecipEase Error: Object not found!')
    
    # _______________________________________________________________________________

    def do_delete(self, line):
        """Updates an instance (record) of a class (table) and save it to the DB.
Usage: update class_name obj_id att1=value1 att2=value2 att3=value3"""

        usage_delete = {
            'class_name': '',
            'obj_id': '',
            'attributes_args': {} # hatethandely yakhty
        }

        if RecipEaseCLI.__handle_usage(line, usage_delete, self.do_update.__doc__) == -1\
        or RecipEaseCLI.__cmd_validation(usage_delete) == 0:
            return
        
        cls_name = eval(usage_delete.get('class_name', None))
        obj_id = usage_delete.get('obj_id', None)
        obj = storage.get_obj_by_id(cls_name, obj_id)
        
        try:
            obj.delete()
        except AttributeError:
            print("RecipEase Error: Object does not exist!")

        
        

if __name__ == "__main__":
    RecipEaseCLI().cmdloop()

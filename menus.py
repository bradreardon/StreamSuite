import random
import shlex

__author__ = 'bradreardon'

class MenuItem(object):
    def __init__(self, label, callback):
        self.label = label
        self.callback = callback

    def display(self, number):
        print "{}. {}".format(number, self.label)

    def execute(self, *args):
        return self.callback(*args)


class Menu(object):
    def __init__(self, title, items, is_main_menu=False):
        """
        :param basestring title: The title to show for the menu
        :param items: A list of MenuItems
        :type items: list[MenuItem]
        """
        self.title = title
        self.items = items
        self.is_main_menu = is_main_menu

    def as_menu_item(self):
        class_dict = {
            'label': '[MENU] {}'.format(self.title),
            'callback': self.show
        }
        return type('MenuItem{}'.format(random.randrange(1, 999999)), (MenuItem,), class_dict)(**class_dict)

    def show(self, *args):
        while True:
            try:
                print
                print "---"
                print self.title
                print "---"
                for i, item in enumerate(self.items):
                    item.display(i + 1)
                print "0. Go back" if not self.is_main_menu else "0. Exit"
                print "---"
                selection = shlex.split(raw_input(":: "))
                selection[0] = int(selection[0])
                if selection[0] == 0:
                    break
                selected_item = self.items[selection[0] - 1]
                selected_item.execute(*selection[1:])
            except ValueError:
                print "Invalid choice, try again."
            except KeyboardInterrupt:
                exit(0)

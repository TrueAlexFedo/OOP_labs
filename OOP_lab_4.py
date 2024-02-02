import time

class Key:
    def __init__(self, keyName):
        self.__keyName = keyName

    def get_name(self):
        return self.__keyName

    def press_key(self, actions):
        print(f"Нажата кнопка: {self.__keyName}")
        time.sleep(0.5)
        actions.add_action(self)

    def reassign_key(self, new_key, actions):
        print(f"Переназначаем: {self.__keyName} -> {new_key.get_name()}")
        for i in range(len(actions.get_actions())):
            if actions.get_actions()[i].get_name() == self.__keyName:
                actions.get_actions()[i] = new_key


class Actions:
    def __init__(self):
        self.__actions = []

    def get_actions(self):
        return self.__actions

    def add_action(self, key):
        self.__actions.append(key)

    def delete_last(self):
        if self.__actions:
            last_action = self.__actions.pop()
            #print(f"Последнее нажатие - {last_action.get_name()}")
        else:
            print("нет нажатий для удаления")

    def print_actions(self):
        for i in self.__actions:
            print(i.get_name())


class Volume(Key):
    def do(self, actions):
        print(f"Увеличиваем звук: {self.get_name()}")
        time.sleep(0.5)
        actions.add_action(self)

    def undo(self, actions):
        print(f"Уменьшаем звук: {self.get_name()}")
        time.sleep(0.5)
        actions.delete_last()




if __name__ == '__main__':
    actions = Actions()

    key1 = Key('Enter')
    key1.press_key(actions)

    key2 = Key('Esc')
    key2.press_key(actions)

    actions.print_actions()
    print("*******\n")

    actions.delete_last()
    actions.print_actions()
    print('*******\n')

    key2.press_key(actions)
    actions.print_actions()
    print('*******\n')

    key3 = Key("Alt")
    key2.reassign_key(key3, actions)
    actions.print_actions()
    print('*******\n')

    # Используем Volume
    button_action = Volume("VolumeUp")
    button_action.do(actions)
    butt2 = Volume("VolumeDown")
    butt2.undo(actions)
    actions.print_actions()
    print('*******\n')

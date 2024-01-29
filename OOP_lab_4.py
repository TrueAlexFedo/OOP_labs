#Пишем имитацию нажатия кнопок на клавиватуре
import time

class Key:
    def __init__(self, keyName):
        self.__keyName = keyName

    def getName(self):
        return self.__keyName

    def setName(self, newKey):
        self.__keyName = newKey

    #нажатие
    def press_key(self):
        print(f"Нажата кнопка: {self.__keyName}")
        time.sleep(0.5)  # задержка между нажатиями клавиш
        actions.AddAction(self)

    #переназначение клавиш
    def reassign_key(self, newKey, actions):
        print(f"Переназначаем: {self.__keyName} -> {newKey.getName()}")
        for i in range(len(actions.getActions())):
            if actions.getActions()[i].getName() == self.__keyName:
                actions.getActions()[i] = newKey


class Actions:

    def __init__(self):
        self.__actions = []

    def getActions(self):
        return self.__actions

    def AddAction(self, key):
        self.__actions.append(key)

    #отмена нажатия
    def deletelast(self):
        if len(self.__actions) > 0:
            last_action = self.__actions.pop()
            print(f"Последнее нажатие - {last_action.getName()}")
        else:
            print("нет нажатий для удаления")

    def printActions(self):
        for i in self.__actions:
            print(i.getName())


if __name__ == '__main__':
    actions = Actions()

    key1 = Key('Enter')
    key1.press_key()
    key2 = Key('Esc')
    key2.press_key()
    actions.printActions()
    print("*******\n")

    actions.deletelast()
    actions.printActions()
    print('*******\n')

    key2.press_key()
    actions.printActions()
    print('*******\n')

    key3=Key("Alt")
    key2.reassign_key(key3, actions)
    actions.printActions()
    print('*******\n')


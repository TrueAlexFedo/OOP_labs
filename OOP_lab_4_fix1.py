import time


class Key:
    def __init__(self, keyName, actions):
        self.keyName = keyName
        self.actions = actions

    def get_name(self):
        return self.keyName

    def setName(self, newKey):
        self.keyName = newKey

    def set_keyboard(self, Keyboard):
        self.Keyboard = Keyboard

    def use_Button(self):
        print(f'Нажата кнопка: {self.keyName}')
        time.sleep(0.5)
        self.actions.new_action(self.keyName)

    def reassign_Button(self, newButton, actions):
        print(f'Переназначаем: {self.keyName} ==> {newButton.get_name()}')
        print('\n')
        for i in range(len(actions.get_actions())):
            if actions.get_actions() == self.keyName:
                actions.setName(newButton)
        return actions


class Actions:
    def __init__(self, Keyboard_name):
        self.app = {'Ctrl+Alt+Delete': 'Диспетчер задач', 'Win+G': 'Виджет', 'Win+R':'Выполнить'}
        self.Keyboard_name = Keyboard_name
        self.actions = []
        self.active_app = []

    def set_actions(self, actions):
        self.actions = actions

    def get_actions(self):
        return self.actions

    def new_action(self, action_name):
        self.actions.append(action_name)
        self.realise_action(action_name)

    def realise_action(self, press_name):
        if press_name in self.app:
            self.active_app.append(self.app[str(press_name)])
        else:
            self.active_app.append(str(press_name)+' - нет назначения')

    def delete_app(self,app):
        #app - приложение, которое нужно закрыть
        print('Закрытие: '+str(app))

    def undo_last_action(self):
        if len(self.actions) > 0:
            print('\nОтмена последнего действия:')
            last_action = self.actions.pop()
            print(f'Последнее нажатие - {last_action}')
            last_active_app = self.active_app.pop()
            self.delete_app(last_active_app)
            #print(f'Last app - {last_active_app}')

        else:
            print('Нет последних нажатий')

    def print_actions_history(self):
        print('История нажатий:')
        for action in self.actions:
            print(action)
        print('')

    def print_actve_app(self):
        print('Последние действия')
        for action in self.active_app:
            print(action)
        print('')



if __name__ == '__main__':
    actions = Actions('Keyboard')
    print(
        "Создать виртуальную клавиатуру с переназначаемыми действиями для клавиш и комбинаций клавиш, с возможностью отката действий назад.")
    Button1 = Key('Win+G', actions)
    Button1.use_Button()
    Button2 = Key('Ctrl+Alt+Delete', actions)
    Button2.use_Button()

    actions.print_actions_history()
    actions.print_actve_app()

    actions.undo_last_action()

    actions.print_actions_history()
    actions.print_actve_app()

    Button3 = Key('Ctrl+F', actions)
    Button3.use_Button()
    Button1.reassign_Button(Button3, actions)



    actions.print_actions_history()
    actions.print_actve_app()


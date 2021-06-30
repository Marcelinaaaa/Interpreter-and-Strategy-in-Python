# import characters as characters
# import command as command
from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums

# event ::= command token receiver token arguments
# command ::= word+
# word ::= a collection of one or more alphanumeric characters
# token ::= ->
# receiver ::= word+
# arguments ::= word+


class Boiler:
    def __init__(self):
        self.temperature = 83 # in celsius

    def __str__(self):
        return f'boiler temperature: {self.temperature}'

    def increase_temperature(self, amount):
        print(f"increasing the boiler's temperature by {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self, amount):
        print(f"decreasing the boiler's temperature by {amount} degrees")
        self.temperature -= amount

class Gate:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False


class Garage:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True

    def close(self):
        print('closing the garage')
        self.is_open = False


class Aircondition:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the air condition')
        self.is_on = True

    def turn_off(self):
        print('turning off the air condition')
        self.is_on = False


class Heating:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the heating')
        self.is_on = True

    def turn_off(self):
        print('turning off the heating')
        self.is_on = False


class Fridge:
    def __init__(self):
        self.temperature = 2  # in celsius

    def __str__(self):
        return f'fridge temperature: {self.temperature}'

    def increase_temperature(self, amount):
        print(f"increasing the fridge's temperature by {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self, amount):
        print(f"decreasing the fridge's temperature by {amount} degrees")
        self.temperature -= amount


def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)

    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boiler()
    fridge = Fridge()

    tests = ('open -> gate',
             'close -> garage',
             'turn on -> air condition',
             'turn off -> heating',
             'increase -> boiler temperature -> 5 degrees',
             'decrease -> fridge temperature -> 2 degrees')

    open_actions = {'gate': gate.open,
                    'garage': garage.open,
                    'air condition': airco.turn_on,
                    'heating': heating.turn_on,
                    'boiler temperature': boiler.increase_temperature,
                    'fridge temperature': fridge.increase_temperature}
    close_actions = {'gate': gate.close,
                     'garage': garage.close,
                     'air condition': airco.turn_off,
                     'heating': heating.turn_off,
                     'boiler temperature': boiler.decrease_temperature,
                     'fridge temperature': fridge.decrease_temperature}

    dzialanie_programu = input("Wybierz urządzenie [U] lub Zamknij program [Z]")
    while dzialanie_programu in 'Uu':
        nazwa = input("Które urządzenie wybierasz? [B]-brama, [G]-garaż, [K]-klimatyzacja, [O]-ogrzewanie, "
                      "[W]-woda(boiler), [L]-lodówka")
        if nazwa in 'Bb':
            czynnosc = input("Co chcesz zrobić? [O]-otworzyć / [Z]-zamknąć bramę")
            if czynnosc in 'Oo':
                otworz_brame = 'open -> gate'
                cmd, dev = event.parseString(otworz_brame)
                cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
                open_actions[dev_str]()
            elif czynnosc in 'Zz':
                zamknij_brame = 'close -> gate'
                cmd, dev = event.parseString(zamknij_brame)
                cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
                close_actions[dev_str]()
        elif nazwa in 'Gg':
            czynnosc = input("Co chcesz zrobić? [O]-otworzyć / [Z]-zamknąć garaż")
            if czynnosc in 'Oo':
                otworz = 'open -> garage'
                cmd, dev = event.parseString(otworz)
                cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
                open_actions[dev_str]()
            elif czynnosc in 'Zz':
                zamknij = 'close -> garage'
                cmd, dev = event.parseString(zamknij)
                cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
                close_actions[dev_str]()
        elif nazwa in 'Kk':
            czynnosc = input("Co chcesz zrobić? [W]-włączyć / [Z]-zatrzymać klimatyzację")
            if czynnosc in 'Ww':
                wlacz = 'turn on -> air condition'
                cmd, dev = event.parseString(wlacz)
                cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
                open_actions[dev_str]()
            elif czynnosc in 'Zz':
                zatrzymaj = 'turn of -> air condition'
                cmd, dev = event.parseString(zatrzymaj)
                cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
                close_actions[dev_str]()
        elif nazwa in 'Oo':
            czynnosc = input("Co chcesz zrobić? [W]-włączyć / [Z]-zatrzymać ogrzewanie")
            if czynnosc in 'Ww':
                wlacz = 'turn on -> heating'
                cmd, dev = event.parseString(wlacz)
                cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
                open_actions[dev_str]()
            elif czynnosc in 'Zz':
                zatrzymaj = 'turn of -> heating'
                cmd, dev = event.parseString(zatrzymaj)
                cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
                close_actions[dev_str]()
        elif nazwa in 'Ww':
            czynnosc = input("Co chcesz zrobić? [P]-podnieść / [Z]-zmniejszyć temperaturę wody")
            stopnie = input("O ile stopni?")
            if czynnosc in 'Pp':
                podnies = 'increase -> boiler temperature'
                podnies += " -> "
                podnies += str(stopnie)
                cmd, dev, arg = event.parseString(podnies)
                cmd_str = ' '.join(cmd)
                dev_str = ' '.join(dev)
                arg_str = ' '.join(arg)
                num_arg = 0
                try:
                    # extract the numeric part
                    num_arg = int(arg_str.split()[0])
                except ValueError as err:
                    print(f"expected number but got: '{arg_str[0]}'")
                if num_arg > 0:
                    open_actions[dev_str](num_arg)
            elif czynnosc in 'Zz':
                zmniejsz = 'decrease -> boiler temperature'
                zmniejsz += " -> "
                zmniejsz += str(stopnie)
                cmd, dev, arg = event.parseString(zmniejsz)
                cmd_str = ' '.join(cmd)
                dev_str = ' '.join(dev)
                arg_str = ' '.join(arg)
                num_arg = 0
                try:
                    # extract the numeric part
                    num_arg = int(arg_str.split()[0])
                except ValueError as err:
                    print(f"expected number but got: '{arg_str[0]}'")
                if num_arg > 0:
                    close_actions[dev_str](num_arg)
        elif nazwa in 'Ll':
            czynnosc = input("Co chcesz zrobić? [P]-podnieść / [Z]-zmniejszyć temperaturę lodówki")
            stopnie = input("O ile stopni?")
            if czynnosc in 'Pp':
                podnies = 'increase -> fridge temperature'
                podnies += " -> "
                podnies += str(stopnie)
                cmd, dev, arg = event.parseString(podnies)
                cmd_str = ' '.join(cmd)
                dev_str = ' '.join(dev)
                arg_str = ' '.join(arg)
                num_arg = 0
                try:
                    # extract the numeric part
                    num_arg = int(arg_str.split()[0])
                except ValueError as err:
                    print(f"expected number but got: '{arg_str[0]}'")
                if num_arg > 0:
                    open_actions[dev_str](num_arg)
            elif czynnosc in 'Zz':
                zmniejsz = 'decrease -> fridge temperature'
                zmniejsz += " -> "
                zmniejsz += str(stopnie)
                cmd, dev, arg = event.parseString(zmniejsz)
                cmd_str = ' '.join(cmd)
                dev_str = ' '.join(dev)
                arg_str = ' '.join(arg)
                num_arg = 0
                try:
                    # extract the numeric part
                    num_arg = int(arg_str.split()[0])
                except ValueError as err:
                    print(f"expected number but got: '{arg_str[0]}'")
                if num_arg > 0:
                    close_actions[dev_str](num_arg)
        dzialanie_programu = input("Wybierz urządzenie [U] lub Zamknij program [Z]")


if __name__ == '__main__':
    main()

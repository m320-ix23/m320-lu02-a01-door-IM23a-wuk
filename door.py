"""
Dieses Modul definiert eine Klasse Door und eine Dummy-Klasse DoorLock
zur Simulation eines Tür- und Schlossmechanismus.
"""


class Door:
    """
    Klass, die eine Tür mit einem Schlossmechanismus simuliert

    :param ref2door_lock: Referenz zu einem Türschloss-Objekt
    :param base_color: Die Farbe der Tür
    """

    def __init__(self, ref2door_lock, base_color):
        """
        Erzeugt ein Tür-Objekt.
        :param ref2door_lock: Referenz zu einem Türschloss-Objekt
        :param base_color: Die Farbe der Tür
        """
        self._the_door_lock = ref2door_lock
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False

    def open_the_door(self):
        """Methode für das Öffnen der Tür, wenn sie nicht verriegelt ist."""
        if not self._door_is_locked:
            self._door_is_open = True

    def close_the_door(self):
        """Methode für das Schließen der Tür."""
        self._door_is_open = False

    def lock_the_door(self):
        """Methode für das Verriegeln der Tür, wenn sie geschlossen ist."""
        if not self._door_is_open:
            self._door_is_locked = self._the_door_lock.lock()

    def unlock_the_door(self):
        """Methode für das Entriegeln der Tür, wenn sie verriegelt ist."""
        if self._door_is_locked:
            self._door_is_locked = self._the_door_lock.unlock()

    def test(self):
        """Gibt alle Attribute der Tür aus."""
        print(f'Türfarbe: {self.color}\n'
              f'Türe offen: {self._door_is_open}\n'
              f'Türe verriegelt: {self._door_is_locked}')

    @property
    def door_is_open(self):
        return self._door_is_open

    @property
    def door_is_locked(self):
        return self._door_is_locked

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color


class DoorLock:
    """Dummy-Klasse für ein Türschloss."""

    def __init__(self):
        print("Ein Schloss wurde erzeugt")

    def lock(self):
        return True

    def unlock(self):
        return False


if __name__ == "__main__":
    print("Test für Tür-Objekt")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "grün")
    the_door.test()
    print("-- Türe jetzt öffnen --")
    the_door.open_the_door()
    the_door.test()

class RubberDuck:
    color = 'yellow'

    def __init__(self, quack_volume=5):
        self.quack_volume = quack_volume

    @staticmethod
    def squeak():
        print("duck is squeaking...")

    @classmethod
    def get_color(cls):
        return cls.color

    def boost_volume(cls):
        cls.quack_volume *= 2

    @property
    def quack_volume(self):
        return self.__quack_volume

    @quack_volume.setter
    def quack_volume(self, value):
        if value < 0:
            self.__quack_volume = 0
        else:
            self.__quack_volume = value

    def __str__(self):
        return f"RubberDuck (volume={self.__quack_volume})"


# main.py

duck = RubberDuck()
print(duck)  # שימוש ב-__str__

RubberDuck.squeak()

duck.quack_volume = 10
print("🔊 New volume:", duck.quack_volume)

duck.boost_volume()
print("🚀 Boosted volume:", duck.quack_volume)

print("🎨 Default color:", RubberDuck.get_color())

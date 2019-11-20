class GameObject(object):
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc


class Rogue(GameObject):
    def __init__(self, name):
        self.class_name = "rogue"
        self.health = 3
        self.desc = "A little rogue"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        else:
            health_line = "It is dead"
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self.desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        else:
            health_line = "It is dead"
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Rogue:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the Rogue!"
            else:
                msg = "You hit the {}".format(thing.class_name)
        else:
            msg = "There is no {} here".format(noun)
        return msg


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)


def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}". format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())


def say(noun):
    return 'You said "{}"'.format(noun)


verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit,
}
rogue = Rogue("Josh the rogue")
goblin = Goblin("Little goblin")

print("Hi. It's me, voice in your head. I help you, to survive." + "\n"
      "Well, i think you should know, what you can do." + "\n"
      "You can say something using the keyword 'say' and say what" + "\n"
      "you want. Also, you can fight with enemy with keyword 'hit'," + "\n"
      "but you should say who will die by your hand" + "\n"
      "(like 'hit goblin', kill 'em all c:). And last, you can" + "\n"
      "examine your enemies. Just say 'examine' and your enemy." + "\n"
      "Then you will know all about your enemy. It's all. Good Luck")
while True:
    get_input()

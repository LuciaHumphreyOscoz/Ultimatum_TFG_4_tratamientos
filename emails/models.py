from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'emails'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    email = models.StringField(
        blank=False
    )

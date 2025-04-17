from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'asignacion_tratamiento_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDER_CHOICES = ['Hombre', 'Mujer', 'No binario']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    gender = models.StringField(choices=C.GENDER_CHOICES,)
    custom_participant_id = models.IntegerField(min=100,
        max=999,)
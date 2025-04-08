# models.py
from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'tarea_competitiva_2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 400  

class Subsession(BaseSubsession):
    def creating_session(self):
        """
        Generates a sequence of vowels and ensures all players receive the SAME sequence
        in a given round. Stores the sequence in session vars.
        """
        if self.round_number == 1:
            self.session.vars['sequences'] = {}  # Store sequences for all rounds

        vowels = ['A', 'E', 'I', 'O', 'U']
        sequence = ''.join(random.choices(vowels, k=30))  # Generate a sequence of 30 vowels

        # Store the sequence for this round
        self.session.vars['sequences'][self.round_number] = sequence

        for player in self.get_players():
            player.sequence = sequence  # Assign sequence to each player

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    sequence = models.StringField()  
    guess = models.IntegerField(label="¿Cuántas letras 'A' aparecen en la secuencia?")
    score = models.IntegerField(initial=0) 
    time_limit = models.IntegerField()  
    correct_count = models.IntegerField()
    custom_participant_id = models.IntegerField( label="Código de Participante")
    

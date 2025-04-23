from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'tarea_competitiva_3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['memory_sequences'] = []
            self.session.vars['target_positions'] = []
            self.session.vars['correct_letters'] = []

            LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            SEQUENCE_LENGTH = 8

            for _ in range(C.NUM_ROUNDS):
                seq = random.choices(LETTERS, k=SEQUENCE_LENGTH)
                position_weights = [1, 2, 3, 4, 4, 3, 2, 1]
                pos = random.choices(
                    population=list(range(1, SEQUENCE_LENGTH + 1)),
                    weights=position_weights,
                    k=1
                )[0]
                correct = seq[pos - 1]

                self.session.vars['memory_sequences'].append(seq)
                self.session.vars['target_positions'].append(pos)
                self.session.vars['correct_letters'].append(correct)

        for player in self.get_players():
            round_index = self.round_number - 1
            player.sequence = ''.join(self.session.vars['memory_sequences'][round_index])
            player.target_position = self.session.vars['target_positions'][round_index]
            player.correct_letter = self.session.vars['correct_letters'][round_index]

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    sequence = models.StringField()
    target_position = models.IntegerField()
    correct_letter = models.StringField()
    answer = models.StringField(blank=True)
    score = models.IntegerField(initial=0)
    custom_participant_id = models.IntegerField()
    def save_custom_id(self):
        self.custom_participant_id = self.participant.vars.get('custom_id', '')
    

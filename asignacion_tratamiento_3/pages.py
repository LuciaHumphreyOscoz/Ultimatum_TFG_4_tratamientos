# pages.py
from otree.api import *
from .models import C
import time
import random

class EnterID(Page):
    form_model = 'player'
    form_fields = ['custom_participant_id']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.participant.vars['custom_id'] = self.player.custom_participant_id

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class IntroductionEjemplos(Page):
    def is_displayed(self):
        return self.round_number == 1


class EjemplosTask(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        if 'example_sequence_1' not in self.session.vars:
            letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

            # Ejemplo 1
            seq1 = random.choices(letters, k=8)
            pos1 = random.randint(1, 8)
            correct1 = seq1[pos1 - 1]

            # Ejemplo 2
            seq2 = random.choices(letters, k=8)
            pos2 = random.randint(1, 8)
            correct2 = seq2[pos2 - 1]

            # Guardar en session.vars
            self.session.vars['example_sequence_1'] = ''.join(seq1)
            self.session.vars['example_position_1'] = pos1
            self.session.vars['example_answer_1'] = correct1

            self.session.vars['example_sequence_2'] = ''.join(seq2)
            self.session.vars['example_position_2'] = pos2
            self.session.vars['example_answer_2'] = correct2

        # Devolver al template con seguridad
        return dict(
            seq1=self.session.vars.get('example_sequence_1', ''),
            pos1=self.session.vars.get('example_position_1', 'X'),
            answer1=self.session.vars.get('example_answer_1', ''),
            seq2=self.session.vars.get('example_sequence_2', ''),
            pos2=self.session.vars.get('example_position_2', 'X'),
            answer2=self.session.vars.get('example_answer_2', ''),
        )

class IntroductionTask(Page):
    def is_displayed(self):
        return self.round_number == 1


class Showsequence(Page):

    def vars_for_template(self):
        return dict(sequence=self.player.sequence)
    
    def before_next_page(self):
        self.player.custom_participant_id = self.participant.vars.get('custom_id', '')

    def is_displayed(self):
        return True

class Taskanswer(Page):
    form_model = 'player'
    form_fields = ['answer']
    timeout_seconds = 20  # Tiempo máximo para responder

    def vars_for_template(self):
        return {'position': self.player.target_position,
        'round_number': self.round_number
        }

    def before_next_page(self):
        correct = self.player.correct_letter.upper().strip()
        given = (self.player.answer or '').upper().strip()

        prev_score = self.player.in_round(self.round_number - 1).score if self.round_number > 1 else 0

        if correct == given:
            self.player.score = prev_score + 1
        else:
            self.player.score = prev_score

        # Guardar score acumulado para resultados finales
        self.participant.vars['final_score'] = self.player.score
        

class FinalPage(Page):
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS



page_sequence = [EnterID, Introduction, IntroductionEjemplos, EjemplosTask, IntroductionTask,Showsequence, Taskanswer,FinalPage]
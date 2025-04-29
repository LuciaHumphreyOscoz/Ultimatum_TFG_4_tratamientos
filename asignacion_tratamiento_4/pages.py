from otree.api import *
import time
import random

class C(BaseConstants):
    NAME_IN_URL = 'tarea_competitiva_4'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 300


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
    def vars_for_template(self):
        return dict(
            time_minutes=8
        )


class EjemplosTask(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        if 'example_sequence_1' not in self.session.vars:
            vowels = ['A', 'E', 'I', 'O', 'U']
            seq1 = ''.join(random.choices(vowels, k=40))
            seq2 = ''.join(random.choices(vowels, k=40))
            self.session.vars['example_sequence_1'] = seq1
            self.session.vars['example_sequence_2'] = seq2
            self.session.vars['example_answer_1'] = seq1.count('A')
            self.session.vars['example_answer_2'] = seq2.count('A')

        return dict(
            seq1=self.session.vars['example_sequence_1'],
            seq2=self.session.vars['example_sequence_2'],
            answer1=self.session.vars['example_answer_1'],
            answer2=self.session.vars['example_answer_2'],
        )


class IntroductionTask(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.participant.vars['expiry'] = time.time() + 480

    def vars_for_template(self):
        return dict(
            time_minutes=8
        )



class Task(Page):
    form_model = 'player'
    form_fields = ['guess']

    def get_timeout_seconds(self):
        expiry = self.player.participant.vars.get('expiry', time.time())
        return max(expiry - time.time(), 0)

    def is_displayed(self):
        return self.round_number >= 1 and self.get_timeout_seconds() > 0

    def vars_for_template(self):
        if not self.player.sequence:
            self.player.sequence = self.player.session.vars['sequences'].get(self.round_number, "ERROR")

        return dict(
            round_number=self.round_number,
            total_rounds=C.NUM_ROUNDS,
            sequence=self.player.sequence,
        )

    def before_next_page(self, timeout_happened=False):
        prev_score = self.player.in_round(self.round_number - 1).score if self.round_number > 1 else 0

        if not self.player.sequence:
            self.player.sequence = self.player.session.vars['sequences'].get(self.round_number, "ERROR")

        correct_count = self.player.sequence.count('A')
        self.player.correct_count = correct_count
        player_guess = self.player.field_maybe_none('guess')

        if timeout_happened or player_guess is None:
            self.player.score = prev_score
        elif player_guess == 0 and timeout_happened:
            self.player.score = prev_score
        else:
            self.player.score = prev_score + 1 if player_guess == correct_count else prev_score

        self.player.participant.vars['final_score'] = self.player.score
        self.player.custom_participant_id = self.player.participant.vars.get('custom_id', '')



   
    
class FinalPage(Page):
    def is_displayed(self):
        expiry = self.player.participant.vars.get('expiry', time.time())
        time_up = time.time() >= expiry
        last_round = self.round_number == C.NUM_ROUNDS
        return time_up or last_round


page_sequence = [EnterID, Introduction, IntroductionEjemplos, EjemplosTask, IntroductionTask, Task, FinalPage]

from otree.api import *
from .models import Player

class EnterID(Page):
    form_model = 'player'
    form_fields = ['custom_participant_id']

    def before_next_page(self):
        self.player.participant.vars['custom_id'] = self.player.custom_participant_id

class Introduction(Page):
    def is_displayed(player):
        return True

    def vars_for_template(player):
        return dict()

class GenderPage(Page):
    form_model = 'player'
    form_fields = ['gender']

class FinalPage(Page):
    pass

page_sequence = [EnterID, Introduction, GenderPage, FinalPage]

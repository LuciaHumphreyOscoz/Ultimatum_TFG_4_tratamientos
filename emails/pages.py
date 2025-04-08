from otree.api import *

class EmailPage(Page):
    form_model = 'player'
    form_fields = ['email']


page_sequence = [EmailPage]


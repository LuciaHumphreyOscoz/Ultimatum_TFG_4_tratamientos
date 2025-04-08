from .models import *

def set_payoffs(group: Group):
    """Calculate final payoffs based on allocator's decision"""
    players = group.get_players()
    allocator = next((p for p in players if p.assigned_role == 'allocator'), None)
    receiver = next((p for p in players if p.assigned_role == 'receiver'), None)

    if allocator and receiver:
        allocator.final_payment = C.ENDOWMENT - group.offer
        receiver.final_payment = group.offer

        allocator.participant.vars['dictator_final_payment'] = allocator.final_payment
        receiver.participant.vars['dictator_final_payment'] = receiver.final_payment

class EnterID(Page):
    form_model = 'player'
    form_fields = ['custom_participant_id']

    def before_next_page(self):
        self.player.participant.vars['custom_id'] = self.player.custom_participant_id

class Introduction(Page):
    pass

class RoleAssignment(Page):
    def vars_for_template(self):
        return {
            'assigned_role': self.player.assigned_role
        }

class Decision(Page):
    form_model = 'group'
    form_fields = ['offer']

    def is_displayed(self):
        return self.player.assigned_role == 'allocator'

    def before_next_page(self):
        set_payoffs(self.group)

class WaitForResults(WaitPage):
    wait_for_all_groups = True
    
class PerceptionQuestion(Page):
    form_model = 'player'
    form_fields = ['perception_others_allocators', 'perception_allocators']

    def vars_for_template(self):
        return {
            'role': self.player.assigned_role,
        }

class PerceptionQuestion(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.player.assigned_role == 'allocator':
            return ['perception_others_allocators']
        else:
            return ['perception_allocators']



class ResultsAllocator(Page):
    form_model = 'player'
    form_fields = ['explanation']
    timeout_seconds = 90

    def is_displayed(self):
        return self.player.assigned_role == 'allocator'

    def vars_for_template(self):
        return {
            'amount_sent': self.group.offer,
            'final_payment': self.player.final_payment,
        }

class ResultsReceiver(Page):
    def is_displayed(self):
        return self.player.assigned_role == 'receiver'

    def vars_for_template(self):
        return {
            'final_payment': self.player.final_payment,
        }


class FinalPage(Page):

    def is_displayed(self):
        return True  # Se muestra a todos

    def vars_for_template(self):
        euros = round(float(self.player.final_payment) * 0.5, 2)
        self.player.payment_in_euros = euros 
        return {
            'final_payment': self.player.final_payment,
            'payment_in_euros': euros
        }


    
class FinalQuestionnaire(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'age',
        'studies',
        'socialcapital',
        'becaMEC',
        'football_team',
        'payoff_satisfaction',
        'discrimiation_level',
        'role_fairness',
    ]



page_sequence = [EnterID, Introduction, RoleAssignment, Decision, WaitForResults,PerceptionQuestion, ResultsAllocator, ResultsReceiver, FinalPage,FinalQuestionnaire]

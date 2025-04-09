from .models import *

def set_payoffs(group: Group):
    players = group.get_players()
    allocator = next((p for p in players if p.assigned_role == 'allocator'), None)
    receiver = next((p for p in players if p.assigned_role == 'receiver'), None)

    if allocator and receiver:
        allocator.final_payment = C.ENDOWMENT - group.offer
        receiver.final_payment = group.offer

        # Asignar el payoff oficial
        allocator.payoff = allocator.final_payment
        receiver.payoff = receiver.final_payment

        allocator.total_payment_euros = 1.00 + float(allocator.final_payment) * 0.5
        receiver.total_payment_euros = 1.00 + float(receiver.final_payment) * 0.5



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
    pass  

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
        return True

    def vars_for_template(self):
        payoff_points = self.player.payoff or 0
        fixed_part = 1.00
        variable_part = float(payoff_points) * 0.5
        total_payment = fixed_part + variable_part
        return {
            "fixed_part": round(fixed_part, 2),
            "variable_part": round(variable_part, 2),
            "total_payment_euros": round(total_payment, 2),
            "final_payment": payoff_points  # en puntos
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

page_sequence = [
    EnterID,
    Introduction,
    RoleAssignment,
    Decision,
    WaitForResults,
    PerceptionQuestion,
    ResultsAllocator,
    ResultsReceiver,
    FinalPage,
    FinalQuestionnaire
]

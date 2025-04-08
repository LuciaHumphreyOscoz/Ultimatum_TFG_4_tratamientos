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

        if self.player.custom_participant_id:  # Evitar errores si es None
            numeric_id = int(self.player.custom_participant_id)  # Convertir a número
            self.player.time_limit = 15 if numeric_id % 2 == 0 else 18
            self.player.participant.vars['time_limit'] = self.player.time_limit
            
class WaitForPartner(WaitPage):
    title_text = "Por favor, espera..."
    body_text = "Estamos esperando a que tu pareja entre al juego. Esta página avanzará automáticamente cuando ambos estéis listos."

    def after_all_players_arrive(self):
        pass


class ResultsCompetitiveTask(Page):
      def vars_for_template(self):
        my_time = self.player.time_limit if self.player.time_limit is not None else 0
        return {
            'assigned_role': self.player.assigned_role,
            'my_time': my_time
        }         

class Introduction(Page):
    pass


class RoleAssignment(Page):
    """ Página donde se muestra el rol asignado a cada jugador junto con el tiempo asignado. """
    def vars_for_template(self):
        # Obtener el tiempo asignado al jugador actual
        my_time = self.player.time_limit if self.player.time_limit is not None else 0

        # Buscar al otro jugador en el grupo
        other_player = self.player.get_others_in_group()[0]  # Solo hay 1 rival en el grupo
        other_time = other_player.time_limit if other_player.time_limit is not None else 0
        
        return {
            'assigned_role': self.player.assigned_role,
            'my_time': my_time,
            'other_time': other_time
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
        'class_level',
        'role_fairness',
    ]


page_sequence = [EnterID, WaitForPartner, ResultsCompetitiveTask, Introduction, RoleAssignment, Decision, WaitForResults,PerceptionQuestion, ResultsAllocator, ResultsReceiver,FinalPage,FinalQuestionnaire]

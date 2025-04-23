from .models import *


def set_payoffs(group: Group):
    proposer = next((p for p in group.get_players() if p.assigned_role == 'proposer'), None)
    receiver = next((p for p in group.get_players() if p.assigned_role == 'receiver'), None)

    if proposer and receiver:
        if group.offer_accepted:
            proposer.final_payment = C.ENDOWMENT - group.offer
            receiver.final_payment = group.offer
        else:
            proposer.final_payment = 0
            receiver.final_payment = 0

        proposer.payoff = proposer.final_payment
        receiver.payoff = receiver.final_payment

        proposer.total_payment_euros = 2.00 + float(proposer.final_payment) * 0.5
        receiver.total_payment_euros = 2.00 + float(receiver.final_payment) * 0.5

class EnterID(Page):
    form_model = 'player'
    form_fields = ['custom_participant_id']

    def before_next_page(self):
        self.player.participant.vars['custom_id'] = self.player.custom_participant_id

        if self.player.custom_participant_id:  # Evitar errores si es None
            numeric_id = int(self.player.custom_participant_id)  # Convertir a número
            self.player.time_limit = 10 if numeric_id % 2 == 0 else 12
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

class Offer(Page):
    form_model = 'group'
    form_fields = ['offer']

    def is_displayed(self):
        return self.player.assigned_role == 'proposer'

class WaitForOffer(WaitPage):
    def is_displayed(self):
        return self.player.assigned_role == 'receiver'
    
class PerceptionQuestion(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.player.assigned_role == 'proposer':
            return ['perception_others_proposers']
        else:
            return ['perception_proposers']

    def vars_for_template(self):
        return {
            'role': self.player.assigned_role,
        }
    
class DictatorOffer(Page):
    form_model = 'player'
    form_fields = ['hypothetical_offer']

    def is_displayed(self):
        return self.player.assigned_role == 'proposer'

class AcceptReject(Page):
    form_model = 'group'
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.assigned_role == 'receiver'

    def vars_for_template(self):
        return {
            'offer': self.group.offer,
            'proposer_payoff': C.ENDOWMENT - self.group.offer,
            'receiver_payoff': self.group.offer,
        }

    def before_next_page(self):
        if self.player.assigned_role == 'receiver':
            set_payoffs(self.group)



class WaitForResults(WaitPage):
    pass



class ResultsProposer(Page):
    form_model = 'player'
    form_fields = ['explanation1']
    timeout_seconds = 90

    def is_displayed(self):
        return self.player.assigned_role == 'proposer'

    def vars_for_template(self):
        return {
            'amount_offered': self.group.offer,
            'accepted': self.group.offer_accepted,
            'final_payment': self.player.final_payment,
        }


class ResultsReceiver(Page):
    form_model = 'player'
    form_fields = ['explanation2']
    timeout_seconds = 90
    def is_displayed(self):
        return self.player.assigned_role == 'receiver'

    def vars_for_template(self):
        return {
            'offer_received': self.group.offer,
            'accepted': self.group.offer_accepted,
            'final_payment': self.player.final_payment,
        }


class FinalPage(Page):
    def is_displayed(self):
        return True

    def vars_for_template(self):
        payoff_points = self.player.payoff or 0
        fixed_part = 2.00
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
        'payoff_satisfaction',
        'class_level',
        'role_fairness',
    ]


page_sequence = [EnterID, WaitForPartner, ResultsCompetitiveTask, Introduction, RoleAssignment,  Offer, WaitForOffer, DictatorOffer, AcceptReject,WaitForResults, PerceptionQuestion, ResultsProposer, ResultsReceiver,FinalPage,FinalQuestionnaire]

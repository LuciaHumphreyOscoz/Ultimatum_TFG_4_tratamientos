from otree.api import *


class C(BaseConstants): 
    NAME_IN_URL = 'ultimatum_game_1:M'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = 10  # Cantidad inicial que el proponente puede ofrecer


class Subsession(BaseSubsession):
    def creating_session(self):
        players = self.get_players()
        players.sort(key=lambda p: p.participant.id_in_session)

        groups = [players[i:i + 2] for i in range(0, len(players), 2)]
        self.set_group_matrix(groups)

        for group in self.get_groups():
            p1, p2 = group.get_players()
            p1.assigned_role = 'proposer'
            p2.assigned_role = 'receiver'

            p1.participant.vars['assigned_role'] = 'proposer'
            p2.participant.vars['assigned_role'] = 'receiver'



class Group(BaseGroup):
    offer = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="¿Cuántos puntos deseas ofrecer al receptor?"
    )
    offer_accepted = models.BooleanField(label="¿Aceptas la oferta?")



class Player(BasePlayer):
    assigned_role = models.StringField()
    final_payment = models.CurrencyField()
    custom_participant_id = models.IntegerField( label="Código de Participante")
    total_payment_euros = models.FloatField()
    
    explanation1 = models.LongStringField(
        label="¿Por qué decidiste ofrecer esa cantidad ?"
    )
    explanation2 = models.LongStringField(blank=True)
    def save_custom_id(self):
        self.custom_participant_id = self.participant.vars.get('custom_id', '')

    def role(self):
        return self.assigned_role
    
    hypothetical_offer = models.CurrencyField(
        min=0,
        max=10,
        label="¿Cuántos puntos habrías repartido si la otra persona no pudiera rechazar tu propuesta?"
    )


    # Percepciones sobre el comportamiento de otros
    perception_others_proposers = models.FloatField(
        label="¿Cuántos puntos experimentales crees que han ofrecido de media los demás proponentes?",
        min=0,
        max=10
    )
    perception_proposers = models.FloatField(
        label="¿Cuántos puntos experimentales crees que han ofrecido de media los proponentes?",
        min=0,
        max=10
    )

    # Cuestionario final
    gender = models.StringField(
        label="Género",
        choices=["Hombre", "Mujer", "Otro"],
        widget=widgets.RadioSelect
    )
    age = models.IntegerField(label="Edad")
    studies = models.StringField(label="¿Qué estudias?")
    socialcapital = models.StringField(
        label="¿Alguno de tus padres ha obtenido un título universitario?",
        choices=["Sí", "No", "No estoy seguro"],
        widget=widgets.RadioSelect
    )
    becaMEC = models.StringField(
        label="¿Has recibido la Beca del Ministerio de Educación (beca MEC) alguna vez en lo que llevas de carrera?",
        choices=["Sí", "No", "No estoy seguro"],
        widget=widgets.RadioSelect
    )
    payoff_satisfaction = models.IntegerField(
        label="¿En una escala del 1 al 10, cuán satisfecho/a estás con tus ganancias en el experimento? (1 = totalmente insatisfecho/a, 10 = totalmente satisfecho/a)",      
        min=1,
        max=10,
    )
    role_fairness = models.IntegerField(
        min=1,
        max=10,
        label="¿En una escala del 1 al 10, cuán justa consideras la asignación de roles? (1 = totalmente injusta, 10 = totalmente justa)"
    )
    discrimiation_level = models.IntegerField(
        min=1,
        max=10,
        label="¿En una escala del 1 al 10, hasta qué punto sentiste que el uso del género como criterio fue una forma de discriminación? (1 = para nada, 10 = totalmente)"
    )

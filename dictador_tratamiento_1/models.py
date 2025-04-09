from otree.api import *

class C(BaseConstants): 
    NAME_IN_URL = 'dictator_game1'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = 10

class Subsession(BaseSubsession):
    def creating_session(self):
        players = self.get_players()
        players.sort(key=lambda p: p.participant.id_in_session)
        groups = [players[i:i + 2] for i in range(0, len(players), 2)]
        self.set_group_matrix(groups)

        for group in self.get_groups():
            p1, p2 = group.get_players()
            p1.assigned_role = 'allocator'
            p2.assigned_role = 'receiver'
            p1.participant.vars['assigned_role'] = 'allocator'
            p2.participant.vars['assigned_role'] = 'receiver'

class Group(BaseGroup):
    offer = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="¿Cuántos puntos deseas enviar al receptor?"
    )

class Player(BasePlayer):
    assigned_role = models.StringField()
    final_payment = models.CurrencyField()
    total_payment_euros = models.FloatField()
    custom_participant_id = models.IntegerField()
    explanation = models.LongStringField(
        label="¿Por qué decidiste enviar esa cantidad al receptor?"
    )

    def save_custom_id(self):
        self.custom_participant_id = self.participant.vars.get('custom_id', '')

    def role(self):
        return self.assigned_role

    def set_payments(self):
        self.fixed_part = 1.00
        self.variable_part = self.payoff * 0.5
        self.total_payment_euros = self.fixed_part + self.variable_part

    perception_others_allocators = models.FloatField(
        label="¿Cuántos puntos experimentales crees que han compartido de media los demás asignadores?",
        min=0,
        max=10
    )
    perception_allocators = models.FloatField(
        label="¿Cuántos puntos experimentales crees que han compartido de media los asignadores?",
        min=0,
        max=10
    )

    gender = models.StringField(
        label="Género",
        choices=["Hombre", "Mujer", "Otro"],
        widget=widgets.RadioSelect
    )
    age = models.IntegerField(label="Edad")
    studies = models.StringField(label="¿Qué estudias?")
    socialcapital = models.StringField(
        label="¿Alguno de tus padres ha obtenido un título unversitario?",
        choices=["Sí", "No", "No estoy seguro"],
        widget=widgets.RadioSelect
    )
    football_team = models.StringField(label="¿Con qué equipo de fútbol simpatizas más?")
    becaMEC = models.StringField(
        label="¿Has recibido la Beca del Ministerio de Educación (beca MEC) alguna vez en lo que llevas de carrera?",
        choices=["Sí", "No", "No estoy seguro"],
        widget=widgets.RadioSelect
    )
    payoff_satisfaction = models.IntegerField(min=1, max=10, label="¿Cuán satisfecho/a estás con tus ganancias?")
    role_fairness = models.IntegerField(min=1, max=10, label="¿Cuán justa consideras la asignación de roles?")
    discrimiation_level = models.IntegerField(min=1, max=10, label="¿Hasta qué punto sentiste discriminación?")

    
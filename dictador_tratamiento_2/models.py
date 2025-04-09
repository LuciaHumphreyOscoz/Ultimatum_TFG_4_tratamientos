from otree.api import *


class C(BaseConstants): 
    NAME_IN_URL = 'dictator_game_2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = 10  # Cantidad inicial que el asignador puede repartir

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
    custom_participant_id = models.IntegerField( label="Código de Participante")
    total_payment_euros = models.FloatField()
    time_limit = models.IntegerField()
    payment_in_euros = models.FloatField()
    
    explanation = models.LongStringField(
        label="¿Por qué decidiste enviar esa cantidad al receptor?"
    )

    def save_custom_id(self):
        self.custom_participant_id = self.participant.vars.get('custom_id', '')

    def role(self):
        return self.assigned_role
    
    
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

    
      # Cuestionario final
    gender = models.StringField(
        label="Género",
        choices=["Hombre", "Mujer", "Otro"],
        widget=widgets.RadioSelect
    )
    age = models.IntegerField(label="Edad")
    studies = models.StringField(label="¿Qué estudias?")
    socialcapital=models.StringField(label="¿Alguno de tus padres ha obtenido un título unversitario?", choices=["Sí","No", "No estoy seguro"],widget=widgets.RadioSelect)
    football_team=models.StringField(label="¿Con que equipo de fútbol simpatizas más?")
    becaMEC= models.StringField(label="¿Has recibido la Beca del Ministerio de Educación (beca MEC) alguna vez en lo que llevas de carrera?", choices=[ "Sí", "No", "No estoy seguro"],widget=widgets.RadioSelect)
    payoff_satisfaction = models.IntegerField(min=1,max=10,label="¿En una escala del 1 al 10, cuán satisfecho/a estás con tus ganancias en el experimento? (1 = totalmente insatisfecho/a, 10 = totalmente satisfecho/a)")
    role_fairness = models.IntegerField(min=1, max=10, label="¿En una escala del 1 al 10, cuán justa consideras la asignación de roles? (1 = totalmente injusta, 10 = totalmente justa)")
    class_level=models.IntegerField(min=1, max=10, label="¿En una escala del 1 al 10, cuánto crees que la ventaja inicial de tiempo ha afectado la asignación de roles? (1 = nada, 10 = completamente)")

    
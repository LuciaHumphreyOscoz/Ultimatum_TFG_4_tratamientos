from os import environ

SESSION_CONFIGS = [
    {
        'name': 'Emails',
        'display_name': "Correos electrónicos",
        'num_demo_participants': 4,
        'app_sequence': ['emails'],
    },
    {
        'name': 'Tratamiento_1_Asignacion',
        'display_name': "Tratamiento 1 Asignacion",
        'num_demo_participants': 2,
        'app_sequence': ['asignacion_tratamiento_1'],
    },
    {
        'name': 'Tratamiento_1_Ultimatum_H',
        'display_name': "Tratamiento 1 Ultimatum",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum_tratamiento_1_H'],
    },
    {
        'name': 'Tratamiento_1_Ultimatum_M',
        'display_name': "Tratamiento 1 Ultimatum",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum_tratamiento_1_M'],
    },
    {
        'name': 'Tratamiento_2_Asignacion',
        'display_name': "Tratamiento 2 Asignación",
        'num_demo_participants': 2,
        'app_sequence': ['asignacion_tratamiento_2'],
    },
    {
        'name': 'Tratamiento_2_Ultimatum',
        'display_name': "Tratamiento 2 Ultimatum",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum_tratamiento_2'],
    },
    {
        'name': 'Tratamiento_3_Asignacion',
        'display_name': "Tratamiento 3 Asignación",
        'num_demo_participants': 2,
        'app_sequence': ['asignacion_tratamiento_3'],
    },
    {
        'name': 'Tratamiento_3_Ultimatum',
        'display_name': "Tratamiento 3 Ultimatum",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum_tratamiento_3'],
    },
    {
        'name': 'Tratamiento_4_Asignacion',
        'display_name': "Tratamiento 4 Asignación",
        'num_demo_participants': 2,
        'app_sequence': ['asignacion_tratamiento_4'],
    },
    {
        'name': 'Tratamiento_4_Ultimatum',
        'display_name': "Tratamiento 4 Ultimatum",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum_tratamiento_4'],
    },
]


ROOMS = [
    dict(
        name='room_tratamiento_1',
        display_name='Tratamiento 1 Asignación',
        # participant_label_file='labels_tratamiento_1.txt',
    ),
    dict(
        name='room_tratamiento_2',
        display_name='Tratamiento 2 Asignación',
        # participant_label_file='labels_tratamiento_2.txt',
    ),
    dict(
        name='room_tratamiento_3',
        display_name='Tratamiento 3 Asignación',
        # participant_label_file='labels_tratamiento_3.txt',
    ),
    dict(
        name='room_tratamiento_4',
        display_name='Tratamiento 4 Asignación',
        # participant_label_file='labels_tratamiento_4.txt',
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.50,
    participation_fee=2.00,
    doc="",
)

# Seguimos permitiendo que puedas usar session_label si quieres (con Edit o URL)
SESSION_CONFIGS_CONFIGURABLE_FIELDS = ['session_label']

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'es'

REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4212205253044'

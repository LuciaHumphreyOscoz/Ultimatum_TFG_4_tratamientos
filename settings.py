from os import environ

SESSION_CONFIGS = [
    {
        'name': 'Emails',
        'display_name': "Correos electrónicos",
        'num_demo_participants': 4,
        'app_sequence': ['emails'],
        'session_label': None,
    },
    {
        'name': 'Tratamiento_1_Asignacion',
        'display_name': "Tratamiento 1 Asignacion",
        'num_demo_participants': 2,
        'app_sequence': ['asignacion_tratamiento_1'],
        'session_label': None,
    },
    {
        'name': 'Tratamiento_1_Dictador',
        'display_name': "Tratamiento 1 Dictador",
        'num_demo_participants': 2,
        'app_sequence': ['dictador_tratamiento_1'],
        'session_label': None,
    },
    {
        'name': 'Tratamiento_2_Asignacion',
        'display_name': "Tratamiento 2 Asignación",
        'num_demo_participants': 2,
        'app_sequence': ['asignacion_tratamiento_2'],
        'session_label': None,
    },
    {
        'name': 'Tratamiento_2_Dictador',
        'display_name': "Tratamiento 2 Dictador",
        'num_demo_participants': 2,
        'app_sequence': ['dictador_tratamiento_2'],
        'session_label': None,
    },
    {
        'name': 'Tratamiento_3_Asignacion',
        'display_name': "Tratamiento 3 Asignación",
        'num_demo_participants': 2,
        'app_sequence': ['asignacion_tratamiento_3'],
        'session_label': None,
    },
    {
        'name': 'Tratamiento_3_Dictador',
        'display_name': "Tratamiento 3 Dictador",
        'num_demo_participants': 2,
        'app_sequence': ['dictador_tratamiento_3'],
        'session_label': None,
    },
    {
        'name': 'Tratamiento_4_Asignacion',
        'display_name': "Tratamiento 4 Asignación",
        'num_demo_participants': 2,
        'app_sequence': ['asignacion_tratamiento_4'],
        'session_label': None,
    },
    {
        'name': 'Tratamiento_4_sDictador',
        'display_name': "Tratamiento 4 Dictador",
        'num_demo_participants': 2,
        'app_sequence': ['dictador_tratamiento_4'],
        'session_label': None,
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
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'es'

REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4212205253044'

from os import environ

SESSION_CONFIGS = [
    dict(
        name='enviro_study2',
        display_name='Enviro - Study 2',
        #app_sequence=['survivor', 'outro'],
        app_sequence=['intro', 'enviro', 'survivor', 'outro'],
        num_demo_participants=5,
    ),
]


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['participant_code']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'cs'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CZK'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'validation'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4652999600098'

ROOMS = [
    dict(
        name='lab',
        display_name='Laboratory',
        participant_label_file='_rooms/lab_labels.txt',
    ),
]

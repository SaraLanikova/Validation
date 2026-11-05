from otree.api import *
import random
from pathlib import Path


doc = """
Introduction: language requirement and general instructions.
Generates a unique four-digit code for each participant (used to link
both waves of the study and to look up the donation in the Survivor task).
Used codes are stored in _used_codes.txt so they are never repeated across sessions.
"""

# file with all codes used so far (in the project folder, next to settings.py)
USED_CODES_FILE = Path(__file__).resolve().parent.parent / "_used_codes.txt"


class C(BaseConstants):
    NAME_IN_URL = 'intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    # 1) read codes used in previous sessions
    used = set()
    if USED_CODES_FILE.exists():
        used = set(USED_CODES_FILE.read_text().split())

    # 2) choose new codes only from those not used yet
    available = [str(n) for n in range(1000, 10000) if str(n) not in used]
    players = subsession.get_players()
    if len(available) < len(players):
        raise ValueError("Not enough unused four-digit codes left.")

    codes = random.sample(available, len(players))
    for p, code in zip(players, codes):
        p.participant_code = code                  # saved in the data (intro.1.player.study_code)
        p.participant.participant_code = code      # available in all apps

    # 3) remember the new codes for future sessions
    with USED_CODES_FILE.open("a") as f:
        f.write("\n".join(codes) + "\n")


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    participant_code = models.StringField()

    consent = models.BooleanField(
        label="Souhlasíte s účastí ve studii?",
        choices=[
            [True, "Souhlasím a chci pokračovat"],
            [False, "Nesouhlasím"],
        ],
        widget=widgets.RadioSelect,
    )

# PAGES
class Intro(Page):
    pass

class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def error_message(player, values):
        if not values['consent']:
            return ("Bez souhlasu s účastí nelze ve studii pokračovat. "
                    "Pokud se studie nechcete zúčastnit, zvedněte prosím ruku "
                    "a vyčkejte příchodu administrátora.")


class ObecneInstrukce(Page):
    pass

page_sequence = [Intro, Consent, ObecneInstrukce]
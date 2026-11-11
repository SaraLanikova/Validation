from otree.api import *
import time
import math
import random


doc = """
Survivor Task (Zíka, Olšová & Jánská, 2025).
Participants press the spacebar at least once every 20 seconds to keep the task running.
Every minute the task runs, the experimenters donate 6 CZK to environmental NGO.
The task ends automatically 20 seconds after the last keypress.
Main outcome: task_seconds.
"""


class C(BaseConstants):
    NAME_IN_URL = 'survivor'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    WINDOW_SECONDS = 20         # time limit for pressing the spacebar
    CZK_PER_MINUTE = 6          # donation rate
    SECONDS_PER_CZK = 10        # 60 s / 6 CZK
    MAX_RETURNS = 1             # default number of returns (overridden by session config 'max_returns')
    CONFIRM_SECONDS = 60        # time to answer the confirmation screen, then the task ends


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # control questions (correct answer must be selected to continue)
    cq1 = models.IntegerField(
        label="Za každou minutu, kterou strávíte na následující stránce s odpočtem, "
              "darujeme na výsadbu nových stromů nebo keřů:",
        choices=[[1, "4 Kč"], [2, "5 Kč"], [3, "6 Kč"]],
        widget=widgets.RadioSelect,
    )
    cq2 = models.IntegerField(
        label="V jakém časovém limitu musíte stisknout klávesu mezerník "
              "na následující stránce s odpočtem?",
        choices=[[1, "10 sekund"], [2, "30 sekund"], [3, "20 sekund"]],
        widget=widgets.RadioSelect,
    )
    cq3 = models.IntegerField(
        label="Co se stane, když během časového limitu stisknete klávesu mezerník?",
        choices=[
            [1, "Studie se ukončí a s tím i navyšování částky, kterou darujeme na výsadbu stromů nebo keřů."],
            [2, "Odpočet se restartuje a navyšování částky, kterou darujeme na výsadbu stromů nebo keřů, bude pokračovat."],
            [3, "Navýší se částka, kterou darujeme na výsadbu stromů nebo keřů."],
        ],
        widget=widgets.RadioSelect,
    )
    cq4 = models.IntegerField(
        label="Co se stane, když během časového limitu NEstisknete klávesu mezerník?",
        choices=[
            [1, "Studie se ukončí a s tím i navyšování částky, kterou darujeme na výsadbu stromů nebo keřů."],
            [2, "Odpočet se restartuje a navyšování částky, kterou darujeme na výsadbu stromů nebo keřů, bude pokračovat."],
            [3, "Navýší se částka, kterou darujeme na výsadbu stromů nebo keřů."],
        ],
        widget=widgets.RadioSelect,
    )

    task_start = models.FloatField()           # Unix timestamp – task shown
    task_end = models.FloatField()             # Unix timestamp – task ended
    task_seconds = models.IntegerField()         # MAIN OUTCOME: time on task (s)
    donation_czk = models.IntegerField()
    presses = models.IntegerField(blank=True)  # number of spacebar presses
    returns_used = models.IntegerField(initial=0)   # how many times the participant returned to the task
    pause_ms = models.IntegerField(initial=0)       # total time on the confirmation screen (not counted)
    end_reason = models.StringField(blank=True)     # 'countdown' / 'confirmed' / 'confirm_timeout'

    comment = models.LongStringField(
        label="",
        blank=True,
    )


# PAGES
class TaskIntro(Page):
    pass

class TaskInstructions(Page):
    form_model = 'player'
    form_fields = ['cq1', 'cq2', 'cq3', 'cq4']

    @staticmethod
    def error_message(player, values):
        correct = dict(cq1=3, cq2=3, cq3=2, cq4=1)
        wrong = [f for f, ok in correct.items() if values[f] != ok]
        if wrong:
            return ("Některé odpovědi nejsou správné. Přečtěte si prosím znovu "
                    "instrukce a odpovědi opravte.")


class Task(Page):
    form_model = 'player'
    form_fields = ['presses', 'returns_used', 'pause_ms', 'end_reason']

    @staticmethod
    def vars_for_template(player):
        # start time is set only once – a page refresh does not reset it
        if player.field_maybe_none('task_start') is None:
            player.task_start = time.time()
        elapsed_ms = int((time.time() - player.task_start) * 1000)
        cfg = player.session.config
        return dict(
            elapsed_ms=elapsed_ms,
            window_seconds=C.WINDOW_SECONDS,
            sec_per_czk=C.SECONDS_PER_CZK,
            max_returns=cfg.get('max_returns', C.MAX_RETURNS),
            confirm_seconds=cfg.get('confirm_seconds', C.CONFIRM_SECONDS),
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.task_end = time.time()
        # time on the confirmation screen is not part of the task
        exact_seconds = player.task_end - player.task_start - player.pause_ms / 1000
        player.task_seconds = math.floor(exact_seconds)
        player.donation_czk = math.ceil(player.task_seconds / C.SECONDS_PER_CZK)

class TaskEnd(Page):
    form_model = 'player'
    form_fields = ['comment']

page_sequence = [TaskIntro, TaskInstructions, Task, TaskEnd]
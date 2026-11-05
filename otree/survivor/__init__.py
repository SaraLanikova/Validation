from otree.api import *
import time
import math
import random


doc = """
Survivor Task (Zíka, Olšová & Jánská, 2025).
Participants press the spacebar at least once every 20 seconds to keep the task running.
Every minute the task runs, the experimenters donate 5 CZK to Čmelák (cmelak.cz).
The task ends automatically 20 seconds after the last keypress.
Main outcome: task_seconds.
"""


class C(BaseConstants):
    NAME_IN_URL = 'survivor'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    WINDOW_SECONDS = 20         # time limit for pressing the spacebar
    CZK_PER_MINUTE = 5          # donation rate
    SECONDS_PER_CZK = 12        # 60 s / 5 CZK


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # control questions (correct answer must be selected to continue)
    cq1 = models.IntegerField(
        label="Za každou minutu, kterou strávíte na následující stránce s odpočtem, "
              "darujeme na vybudování nových prvků zeleně v příměstské krajině:",
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
            [1, "Studie se ukončí a s tím i navyšování částky, kterou darujeme na vybudování "
                "nových prvků zeleně v příměstské krajině."],
            [2, "Odpočet se restartuje a navyšování částky, kterou darujeme na vybudování "
                "nových prvků zeleně v příměstské krajině, bude pokračovat."],
            [3, "Navýší se částka, kterou darujeme na vybudování nových prvků zeleně "
                "v příměstské krajině."],
        ],
        widget=widgets.RadioSelect,
    )
    cq4 = models.IntegerField(
        label="Co se stane, když během časového limitu NEstisknete klávesu mezerník?",
        choices=[
            [1, "Studie se ukončí a s tím i navyšování částky, kterou darujeme na vybudování "
                "nových prvků zeleně v příměstské krajině."],
            [2, "Odpočet se restartuje a navyšování částky, kterou darujeme na vybudování "
                "nových prvků zeleně v příměstské krajině, bude pokračovat."],
            [3, "Navýší se částka, kterou darujeme na vybudování nových prvků zeleně "
                "v příměstské krajině."],
        ],
        widget=widgets.RadioSelect,
    )

    task_start = models.FloatField()           # Unix timestamp – task shown
    task_end = models.FloatField()             # Unix timestamp – task ended
    task_seconds = models.FloatField()         # MAIN OUTCOME: time on task (s)
    donation_czk = models.IntegerField()       # donation generated (CZK)
    presses = models.IntegerField(blank=True)  # number of spacebar presses

    comment = models.LongStringField(
        label="",
        blank=True,
    )


# PAGES
class TaskInstructions(Page):
    form_model = 'player'
    form_fields = ['cq1', 'cq2', 'cq3', 'cq4']

    @staticmethod
    def error_message(player, values):
        correct = dict(cq1=2, cq2=3, cq3=2, cq4=1)
        wrong = [f for f, ok in correct.items() if values[f] != ok]
        if wrong:
            return ("Některé odpovědi nejsou správné. Přečtěte si prosím znovu "
                    "instrukce a odpovědi opravte.")


class Task(Page):
    form_model = 'player'
    form_fields = ['presses']

    @staticmethod
    def vars_for_template(player):
        # start time is set only once – a page refresh does not reset it
        if player.field_maybe_none('task_start') is None:
            player.task_start = time.time()
        elapsed_ms = int((time.time() - player.task_start) * 1000)
        return dict(elapsed_ms=elapsed_ms)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.task_end = time.time()
        player.task_seconds = round(player.task_end - player.task_start, 2)
        player.donation_czk = math.ceil(player.task_seconds / C.SECONDS_PER_CZK)


class TaskEnd(Page):
    form_model = 'player'
    form_fields = ['comment']

page_sequence = [TaskInstructions, Task, TaskEnd]
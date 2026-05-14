# Определение персонажей игры.
define Vika = Character('Вика', color="#815f01", image="charecter/Vika/vika") #Лаомедея
define diller = Character('Диллер', color="#47ff0f") # Умбриель
define shahmatist1 = Character('Первый шахматист', color="#815f01", image="charecter/shahmatist1/ded") # Шедар
define shahmatist2 = Character('Второй шахматист', color="#815f01", image="charecter/shahmatist2/shahmatist2") # Садачбия
define Medsestra = Character('Медсестра', color="#ffffff") # Нахуй не нужна
define chingis = Character('Чингыс', color="#e5ff00") #Алнилам
define vitya = Character('Витя', color="#003cff") #Алнилам
define nobody = Character('Неизвестный', color="#ffffff") # Anna Sokolova
define operator = Character('Оператор', color="#ffffff") # Isla Skye
define nachalnik = Character('Начальник', color="#ffffff") #Альгениб
define maker = Character('Создатель', color="#dacb00") #Зубенельгенуби
define ment = Character('Полицейский', color="#dacb00") # Расалгети
define barmen = Character('Бармен', color="#dacb00") # Пульчеррима
define fishman = Character('Продавец рыбы', color="#dacb00") # Орус
define posetitel = Character('Посетитель', color="#dacb00") # Коре
define teacher = Character('Учитель', color="#dacb00", image="charecter/masha/masha") #Деспина 
define Voice1 = Character('Голос 1', color="#dacb00") # Энцелад
define Voice2 = Character('Голос 2', color="#dacb00") #Деспина 
define model = Character('Фотограф', color="#dacb00") #Леда
define ohrana = Character('Охранник', color="#dacb00") # умбриэль
define it = Character('Сисадмин', color="#dacb00") #Япет
define artem = Character('Артём', color="#dacb00") # Харон
define arina = Character('Арина', color="#dacb00") # Ахернар
define edik = Character('Эдик', color="#dacb00") # Ахирд
define veduschiy = Character('Ведущий', color="#dacb00") # Харон
define turniket = Character('Турникет', color="#dacb00") # ChatGPT
define sekretarsha = Character('Секретарша', color="#dacb00") # Леда
define alina = Character('Алина Эдуардовна', color="#dacb00")  # Зефир
define clara = Character('Клара', color="#ffffff", image="charecter/clara/clara_neutral") #Ахернар
define perehod_diss = Dissolve(0.4)
define fish_list = ["yaz", "sazan", "jereh", "golavl", "vyun", "elec", "gustera", "shuka", "okun", "ukleyka", "plotva", "karas"]
define config.adv_nvl_transition = None
define config.nvl_adv_transition = None

default card_money = 1825
default bacteria = []
default slojnost_igry = "easy"
default polojenie = "home"
default inventory_items = [None] * 25
default hp = 100
default fatigue = 50
default intellect = 0
default luck = 0
default money = 0
default be_schet = 30
default correct_password = "поставщик"
default correct_easy_password = "комод"
default password = ""
default number = ""
default hair_color = "default"
default lips_color = "default"
default lins_color = "default"
default eyes_color = "default"
default inin_pressed = False
default out_pressed = False
default block_ui = False
default days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
default day_index = 5
default day_name = days[day_index]
default clicks_enabled = True
default default_mouse = "default"
default game_hour = 22
default game_minute = 0
default game_time = "22:00"
default take_money_from_box_mainroom = False
default take_vibro_from_box_mainroom = False
default take_rebus_from_box_mainroom = False
default pc_is_unlocked = False
default password_first_time_flag = True
default visit_chees_first_time = 1
default selected_kosti = None
default selected_roulette = None
default resoult_roulette = None
default resoult_kosti = 6
default first_game_dice = True
default chingis_dialog = 0
default rozetka_is_broken = False
default i_know_sudoku = False
default selected_otlata = None
default show_buner = 0
default kvest_na_lazanyu = False
default lazania_temp = 0
default lazania_time = 0
default vitya_in_room = True
default vitya_lock = "close"
default piano_lock = "close"
default money_10_1_taken = False
default money_10_2_taken = False
default money_10_3_taken = False
default gvozd_taken = False
default humer_taken = False
default superkley_taken = False
default magnet_taken = False
default brush_taken = False
default beer_taken = False
default i_know_casino = False
default vilojeno_obyavleniya = False
default bil_zvonok_shluhe = False
default i_know_bar = False
default i_know_masterskaya = False
default rozetka_pochinena = False
default selected_cell = None
default sudoku_proideno = False
default sudoku_download = False
default vitya_rozetka = True
default i_know_password = False
default Chingis_chem_zanyat = False
default vitya_password = False
default diller_is_here = True
default magnet_v_rouletke = False
default ball_v_rouletke = False
default i_know_chingis = False
default i_ask_uvolnenie = False
default i_know_quest_today = False
default car_is_broken = False
default uvolena = False
default kvartira_snyata = False
default bileti_kupleni = False
default sigame_is_available = False
default razgovor_pro_piter = False
default vitya_points = 0
default alexander_points = 0
default vika_points = 0
default ruslan_points = 0
default cup = "empty"
default question1 = ""
default question2 = ""
default question3 = ""
default question4 = ""
default question5 = ""
default first_dialog = True
default i_ask_recept = False
default quest_list = [
    {"text": "Поговорить с витей о сне", "available": False, "done": False, "checked": False},
    {"text": "Разблокировать компьютер", "available": False, "done": False, "checked": False},
    {"text": "Найти деньги на переезд", "available": False, "done": False, "checked": False},
    {"text": "Сдать квартиру", "available": False, "done": False, "checked": False},
    {"text": "Убрать банер", "available": False, "done": False, "checked": False},
    {"text": "Починить розетку", "available": False, "done": False, "checked": False},
    {"text": "Решить судоку", "available": False, "done": False, "checked": False},
    {"text": "Купить продукты для лазаньи", "available": False, "done": False, "checked": False},
    {"text": "Придумать как залезть в витин ящик", "available": False, "done": False, "checked": False},
    {"text": "Уволиться с работы", "available": False, "done": False, "checked": False},
    {"text": "Придумать как выиграть в кубик в казино", "available": False, "done": False, "checked": False},
    {"text": "Придумать как выиграть в рулетку в казино", "available": False, "done": False, "checked": False},
    {"text": "Сказать вите, что все дела сделаны", "available": False, "done": False, "checked": False},
    {"text": "Выиграть в свою игру", "available": False, "done": False, "checked": False},
    {"text": "Купить билеты", "available": False, "done": False, "checked": False},
    {"text": "Снять квартиру", "available": False, "done": False, "checked": False},
    {"text": "Приготовить лазанью", "available": False, "done": False, "checked": False},
    {"text": "Поехать в полицию", "available": False, "done": False, "checked": False},
    {"text": "Принести пиво с рыбой", "available": False, "done": False, "checked": False},
    {"text": "Выловить рыбу по списку", "available": False, "done": False, "checked": False},
    {"text": "Разобрать папки", "available": False, "done": False, "checked": False},
    {"text": "Сходить в школу", "available": False, "done": False, "checked": False},
    {"text": "Найти тайник", "available": False, "done": False, "checked": False},
    {"text": "Отнести документы", "available": False, "done": False, "checked": False},
    {"text": "Найти как отмазаться от вечера", "available": False, "done": False, "checked": False},
    {"text": "Подменить клару на съемке", "available": False, "done": False, "checked": False},
    {"text": "Отвязаться от мента", "available": False, "done": False, "checked": False},
    {"text": "Поговорить с Витей", "available": False, "done": False, "checked": False},
    {"text": "Поехать на работу", "available": False, "done": False, "checked": False},
    {"text": "Узнать рецепт напитка", "available": False, "done": False, "checked": False},
    {"text": "Починить лифт", "available": False, "done": False, "checked": False},
    {"text": "Вскрыть пароль", "available": False, "done": False, "checked": False},
    {"text": "Доделать проект Артёма", "available": False, "done": False, "checked": False},
    {"text": "Найти сахар", "available": False, "done": False, "checked": False},
    {"text": "Найти алкоголь", "available": False, "done": False, "checked": False},
    {"text": "Пройти тест сисадмина", "available": False, "done": False, "checked": False},
    {"text": "Принести боссу напиток", "available": False, "done": False, "checked": False},
    {"text": "Придумать как попасть в эмерген", "available": False, "done": False, "checked": False},
    {"text": "Найти доказательства", "available": False, "done": False, "checked": False},
    {"text": "Поговорить с Витей", "available": False, "done": False, "checked": False},
    {"text": "Найти паспорт", "available": False, "done": False, "checked": False},
]

default higher_pressed = False
default lower_pressed = False
default i_ask_about_barmen = False
default may_ask_about_casino = False
default i_ask_about_work = False
default i_ask_about_chees_players = False
default iphone_is_showed = False
default maker_first_call = True
default kak_dela_maker = False
default why_are_you_make_game = False
default ask_sudoku = 0
default ask_produkti = 0
default ask_work = False
default ask_yaschik = False
default ask_buner = False
default ask_pc2 = False
default ask_pc1 = False
default ask_rozetka = False
default ask_money = False
default lock_is_locked = True
default ask_pincode = False
default selected_najivka = 0
default messange_from_ment = False
default ment_first_dialog = True
default i_know_fishstore = False
default i_know_school = False
default fishman_first_dialog = True
default i_know_river = False
default first_fishbook = True
default selected_plase = "none"
default coughted_fish = []
default fish_quest_done = False
default barmen_dialog_first_time = True
default i_ask_glass = False
default zakaz = 0
default zakaz_point = 0
default i_sold_beer = False
default i_take_beer = False
default papka1 = False
default papka2 = False
default papka3 = False
default papka4 = False
default papka5 = False
default papka6 = False
default i_do_papki = "nit"
default i_say_done = False
default ment_is_here = True
default i_saw_telegramm = False
default masha_is_here = True
default i_want_piano_first_time = True
default i_say_about_ment = False
default masha_and_husband_dialog = False
default need_suck = False
default i_know_studio = False
default first_model_dialog = True
default makeup_level = 0
default clara_suck_now = False
default i_ask_chingis_about_piano = False
default messange_from_nachalnik = False
default i_know_work = False
default nachalnik_first_dialog = True
default i_can_go_out = True
default napitok_quest = False
default security_first_dialog = True
default i_ask_about_sad = False
default need_fix_lift = False
default it_first_dialog = True
default vitya_can_help = False
default i_take_tool = False
default lift_button_open = False
default ohrana_say = False
default laborant_5_first_dialog = True
default i_say_about_lift = False
default bacteri_number = "0"
default laborant_2_dialog_first_time = True
default i_say_about_kabinet = False
default box_take = [False, False, False, False, False, False, False]
default ves_sugar = []
default can_ves = 0
default edik_in_emergen = False
default i_know_tea = False
default i_know_black_tea = False
default i_know_alcohol = False
default i_know_sugar = False
default napitok = []
default i_know_about_sluts = False
default i_ask_about_clients = False
default phone_is_brocken = False
default keys_is_taken = False
default id_is_taken = False
default i_can_talk_with_director = False
default director_first_dialog = True
default door_3_is_closet = True
default project_taken = 0
default vitya_have_work = False
default i_talk_about_work = False
default was_screem = False
default i_know_blackmail = False
default clara_show = False
default no_signal = False
default kosmetik_is_taken = False
default current_mouse = ""



init python:
    config.gl2 = True

# Скрытый экран для таймера
init python:
    import time

    def _enable_afm():
        _preferences.afm_enable = True
        # запускаем таймер снова через 1 секунду
        renpy.invoke_in_thread(_afm_timer)

    def _afm_timer():
        time.sleep(1.0)
        renpy.run(_enable_afm)

    def start_afm_timer():
        renpy.invoke_in_thread(_afm_timer)

    # запускаем при старте игры
    config.start_callbacks.append(start_afm_timer)
    # и при загрузке сохранения
    config.after_load_callbacks.append(start_afm_timer)
    
    def travel(first_point, second_point):
        global block_ui
        block_ui = True
        renpy.movie_cutscene(f"video/from_{first_point}_to_{second_point}.webm")
        block_ui = False
    
    def start_dialog():
        global default_mouse
        global current_mouse
        if default_mouse != "empty":
            current_mouse = default_mouse
        default_mouse = "empty"
        renpy.show_screen("no_escape")
        
    
    def stop_dialog():
        global default_mouse
        global current_mouse
        default_mouse = current_mouse
        renpy.hide_screen("no_escape")

screen no_escape:
    key "K_ESCAPE" action NullAction()

init python:
    config.mouse = {
        "default": [("gui/cursors/default.png", 0, 0)],
        "penguin": [("gui/cursors/penguin.png", 0, 0)],
        "tool": [("icon/tool.png", 0, 0)],
        "kosmetik": [("icon/kosmetik.png", 0, 0)],
        "pasport": [("icon/pasport.png", 0, 0)],
        "phone": [("icon/phone.png", 0, 0)],
        "project": [("icon/project.png", 0, 0)],
        "keys_2_lab": [("icon/keys_2_lab.png", 0, 0)],
        "propusk": [("icon/propusk.png", 0, 0)],
        "napitok": [("icon/napitok.png", 0, 0)],
        "sugars": [("icon/sugars.png", 0, 0)],
        "viskey": [("icon/viskey.png", 0, 0)],
        "izolenta": [("icon/izolenta.png", 0, 0)],
        "produkti": [("icon/produkti.png", 0, 0)],
        "cheese": [("icon/cheese.png", 0, 0)],
        "onion": [("icon/onion.png", 0, 0)],
        "knife": [("icon/knife.png", 0, 0)],
        "dice": [("icon/dice.png", 0, 0)],
        "dice_with_gvozd_colour": [("icon/dice.png", 0, 0)],
        "carrot": [("icon/carrot.png", 0, 0)],
        "nuts": [("icon/nuts.png", 0, 0)],
        "oil": [("icon/oil.png", 0, 0)],
        "muka": [("icon/muka.png", 0, 0)],
        "milk": [("icon/milk.png", 0, 0)],
        "salt": [("icon/salt.png", 0, 0)],
        "cut_nuts": [("icon/cut_nuts.png", 0, 0)],
        "beshamel": [("icon/beshamel.png", 0, 0)],
        "orange_bakteria": [("icon/orange_bakteria.png", 0, 0)],
        "green_bakteria": [("icon/green_bakteria.png", 0, 0)],
        "red_bakteria": [("icon/red_bakteria.png", 0, 0)],
        "blue_bakteria": [("icon/blue_bakteria.png", 0, 0)],
        "cut_onion": [("icon/cut_onion.png", 0, 0)],
        "cut_carrot": [("icon/cut_carrot.png", 0, 0)],
        "meat": [("icon/meat.png", 0, 0)],
        "paper": [("icon/paper.png", 0, 0)],
        "ketchup": [("icon/ketchup.png", 0, 0)],
        "pasta": [("icon/pasta.png", 0, 0)],
        "list": [("icon/list.png", 0, 0)],
        "bolonieze": [("icon/bolonieze.png", 0, 0)],
        "mini_cheese": [("icon/mini_cheese.png", 0, 0)],
        "fresh_lazania": [("icon/fresh_lazania.png", 0, 0)],
        "green_tea": [("icon/green_tea.png", 0, 0)],
        "black_tea": [("icon/black_tea.png", 0, 0)],
        "cofe": [("icon/cofe.png", 0, 0)],
        "humer": [("icon/humer.png", 0, 0)],
        "gvozd": [("icon/gvozd.png", 0, 0)],
        "superkley": [("icon/superkley.png", 0, 0)],
        "magnet": [("icon/magnet.png", 0, 0)],
        "brush": [("icon/brush.png", 0, 0)],
        "beer": [("icon/beer.png", 0, 0)],
        "dice_with_o": [("icon/dice_with_o.png", 0, 0)],
        "dice_with_gvozd": [("icon/dice_with_gvozd.png", 0, 0)],
        "white_colour": [("icon/white_colour.png", 0, 0)],
        "black_colour": [("icon/black_colour.png", 0, 0)],
        "blue_colour": [("icon/blue_colour.png", 0, 0)],
        "green_colour": [("icon/green_colour.png", 0, 0)],
        "podshipnik": [("icon/podshipnik.png", 0, 0)],
        "ball_metall": [("icon/ball_metall.png", 0, 0)],
        "ball_white": [("icon/ball_white.png", 0, 0)],
        "magnet_with_clay": [("icon/magnet_with_clay.png", 0, 0)],
        "udochka": [("icon/udochka.png", 0, 0)],
        "glass": [("icon/glass.png", 0, 0)],
        "german_beer": [("icon/german_beer.png", 0, 0)],
        "keys": [("icon/keys.png", 0, 0)],
        "label1": [("icon/label1.png", 50, 23)],
        "label2": [("icon/label2.png", 50, 23)],
        "label3": [("icon/label3.png", 50, 23)],
        "label4": [("icon/label4.png", 50, 23)],
        "label5": [("icon/label5.png", 50, 23)],
        "label6": [("icon/label6.png", 50, 23)],
        "empty": [("icon/empty.png", 50, 23)]

    }

init python:
    def update_game_time():
        store.game_time = "{:02}:{:02}".format(store.game_hour, store.game_minute)

    def advance_time(hours=0, minutes=0):
        total_minutes = store.game_hour * 60 + store.game_minute + hours * 60 + minutes
        new_hour = (total_minutes // 60) % 24
        new_minute = total_minutes % 60

        # Проверка на переход дня
        days_passed = (store.game_hour * 60 + store.game_minute + hours * 60 + minutes) // (24 * 60)
        for _ in range(days_passed):
            next_day()

        store.game_hour = new_hour
        store.game_minute = new_minute
        update_game_time()

    def next_day():
        store.day_index = (store.day_index + 1) % len(store.days)
        store.day_name = store.days[store.day_index]

    # Пример задач, каждая — это массив с фигурами по индексам (64 клетки)
    chess_puzzles = [
    {
        "board": ["", "", "", "", "", "lb", "kb", ""] + ["pb"] + [""] + ["hb"] + [""] + ["pw"] + [""] * 2 + ["pb"] + [""] + ["pb"] + [""] * 5 + ["pb"] + [""] * 3 + ["pb"] + ["qw"] + [""] * 2 + ["sw"] + [""] * 3 + ["pw"] + ["qb"] + [""] * 11 + ["pw"] * 2 + [""] * 4 + ["pw"] * 2 + [""] * 6 + ["kw"] + [""], 
        "solution": [(28, 7), (6, 7), (12, 5)],
        },
    {
        "board": ["", "", "", "", "kb", "", "", "lb"] + ["pb", "pw", "pb", "hb", "", "pb", "pb", "pb"] + ["", "sb", "", "", "", "", "", ""] + ["", "", "", "lw", "", "", "sw", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["pw", "pw", "", "", "", "pw", "pw", "pw"] + ["", "", "", "", "", "", "kw", ""], 
        "solution": [(9, 1), (11, 1), (27, 3)],
        },
    {
        "board": ["", "lb", "sb", "", "lb", "", "kb", ""] + ["", "", "qb", "", "pb", "pb", "", "pb"] + ["pb", "", "", "pb", "", "", "pb", "sw"] + ["", "", "pb", "pw", "", "", "", ""] + ["", "pb", "pw", "", "", "qw", "", ""] + ["", "pw", "", "hb", "", "", "", ""] + ["pw", "", "", "", "", "pw", "pw", "pw"] + ["", "", "lw", "", "lw", "", "kw", ""],
        # добавь еще 8 задач,
        "solution": [(37, 21), (12, 21), (60, 4)],
        },
    {
        "board": ["qw", "qb", "kb", "", "hw", "", "", ""] + ["", "", "", "pb", "kw", "", "", ""] + ["pw", "", "", "pw", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["", "lb", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""], 
        "solution": [(0, 18), (11, 18), (19, 11)],
        },
    {
        "board": ["", "", "", "", "", "", "hb", "kb"] + ["", "", "", "", "", "", "", "pb"] + ["", "", "sb", "", "", "", "pw", ""] + ["", "", "", "", "", "qb", "hb", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "lw", "qw"] + ["", "", "", "", "", "", "", "kw"], 
        "solution": [(55, 15), (30, 15), (22, 14)],
        },
    {
        "board": ["kb", "", "", "", "", "", "lb", ""] + ["pb", "pb", "kw", "hw", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["pw", "pw", "", "", "", "", "", ""] + ["lw", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "pb", ""] + ["", "", "", "", "", "", "", ""],
        "solution": [(11, 17), (8, 17), (24, 17)],
        },
    {
        "board": ["", "", "sb", "kb", "qb", "", "", "lb"] + ["", "lb", "", "hb", "", "", "", ""] + ["", "pw", "qw", "", "", "", "", "pb"] + ["pb", "", "", "hw", "pb", "pw", "", ""] + ["", "", "", "pw", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["pw", "pw", "", "", "", "", "pw", "pw"] + ["lw", "", "sw", "", "", "lw", "kw", ""],
        "solution": [(18, 10), (9, 10), (17, 10)],
        },
    {
        "board": ["lb", "hb", "sb", "kb", "", "lb", "", ""] + ["", "", "", "pb", "hb", "", "", "pb"] + ["", "", "pb", "hw", "", "", "", ""] + ["pb", "pb", "", "", "", "", "", "qw"] + ["", "", "", "", "pw", "sw", "", ""] + ["", "sw", "qb", "", "", "", "", ""] + ["pw", "", "pw", "", "kw", "", "pw", ""] + ["lw", "", "", "", "", "", "", "lw"],
        "solution": [(31, 4), (5, 4), (19, 13)],
        },
    {
        "board": ["", "qw", "sb", "kb", "", "sb", "", "lb"] + ["", "pb", "", "hb", "", "pb", "pb", ""] + ["hb", "", "", "", "", "", "", "pb"] + ["", "qb", "", "", "", "", "", ""] + ["", "", "", "", "", "sw", "", ""] + ["", "", "", "", "", "hw", "", ""] + ["pw", "pw", "", "", "", "pw", "pw", "pw"] + ["", "", "", "lw", "lw", "", "kw", ""],
        "solution": [(1, 2), (3, 2), (60, 4)],
        },
    {
        "board": ["lb", "", "sb", "", "kb", "", "", "lb"] + ["pb", "pb", "", "qb", "", "", "pb", ""] + ["", "", "pb", "sw", "pb", "", "", "pb"] + ["", "", "", "pw", "", "", "", ""] + ["pw", "", "", "", "", "qw", "", ""] + ["", "", "pw", "", "", "", "", "pw"] + ["", "", "", "", "", "", "pw", ""] + ["lw", "", "", "", "", "lw", "kw", ""],
        "solution": [(37, 5), (7, 5), (61, 5)],
        },
    {
        "board": ["", "", "", "", "lb", "kb", "", ""] + ["", "pb", "", "sb", "", "", "pb", "pb"] + ["pb", "sb", "", "", "", "hb", "", ""] + ["", "", "qb", "", "", "", "hw", ""] + ["", "", "", "", "", "", "", ""] + ["", "sw", "", "", "", "", "", ""] + ["pw", "pw", "pw", "", "qw", "pw", "pw", "pw"] + ["", "", "", "", "lw", "lw", "kw", ""],
        "solution": [(52, 4), (21, 4), (30, 15)],
        },
    {
        "board": ["lb", "", "sb", "", "kb", "", "hb", "lb"] + ["pb", "pb", "qw", "pb", "", "", "", "pb"] + ["", "", "", "pw", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "hb", "pw", "", "", ""] + ["", "", "sb", "", "", "", "", ""] + ["pw", "", "pw", "", "", "", "pw", "pw"] + ["", "", "", "", "", "lw", "kw", ""],
        "solution": [(10, 3), (4, 3), (61, 5)],
        },
    {
        "board": ["", "lb", "", "", "kb", "", "lb", ""] + ["pb", "", "qw", "hb", "hb", "", "sb", "pw"] + ["", "", "", "pb", "hw", "", "", ""] + ["", "", "", "pw", "", "", "", ""] + ["", "", "", "", "pw", "", "qb", ""] + ["", "", "hw", "", "", "", "pw", ""] + ["pw", "", "pw", "", "", "lw", "kw", ""] + ["", "", "", "", "", "", "", "lw"],
        "solution": [(10, 3), (4, 3), (20, 10)],
        },
    {
        "board": ["lb", "", "sb", "kb", "", "", "hb", "lb"] + ["pb", "", "", "pb", "", "pb", "hw", "pb"] + ["hb", "", "", "sw", "", "", "", ""] + ["", "pb", "", "hw", "pw", "", "", "pw"] + ["", "", "", "", "", "", "pw", ""] + ["", "", "", "pw", "", "qw", "", ""] + ["pw", "", "pw", "", "kw", "", "", ""] + ["qb", "", "", "", "", "", "sb", ""],
        "solution": [(45, 21), (6, 21), (19, 12)],
        },
    {
        "board": ["", "", "", "", "kb", "sb", "", "lb"] + ["pb", "", "", "hb", "", "pb", "pb", "pb"] + ["", "", "", "", "qb", "", "", ""] + ["", "", "", "", "pb", "", "sw", ""] + ["", "", "", "", "pw", "", "", ""] + ["", "qw", "", "", "", "", "", ""] + ["pw", "pw", "pw", "", "", "pw", "pw", "pw"] + ["", "", "kw", "lw", "", "", "", ""],
        "solution": [(41, 1), (11, 1), (59, 3)],
        },
    {
        "board": ["lb", "", "sb", "qb", "", "", "", ""] + ["pb", "pb", "pb", "hb", "", "", "lw", ""] + ["", "", "", "pb", "", "kb", "", ""] + ["", "", "", "", "pw", "", "", "pb"] + ["", "", "", "pw", "", "", "pb", "kb"] + ["", "", "", "qw", "", "", "", ""] + ["pw", "pw", "pw", "", "", "", "pw", ""] + ["lw", "hw", "", "", "", "", "kw", ""],
        "solution": [(43, 47), (38, 47), (54, 46)],
        },
    {
        "board": ["lb", "", "sb", "", "qb", "lb", "", ""] + ["pb", "pb", "pb", "", "", "pb", "", "kb"] + ["", "", "hb", "pb", "", "", "pb", "sw"] + ["", "", "sb", "", "pb", "pw", "", "qw"] + ["", "", "sw", "", "pw", "", "", ""] + ["", "", "hw", "pw", "", "", "", ""] + ["pw", "pw", "pw", "", "", "", "pw", ""] + ["lw", "", "", "", "", "kw", "", "lw"],
        "solution": [(31, 22), (13, 22), (23, 5)],
        },
    {
        "board": ["lb", "", "", "", "qb", "sb", "", "lb"] + ["pb", "pb", "pb", "sb", "kb", "", "pb", ""] + ["", "", "hb", "pb", "", "", "hb", "pb"] + ["", "", "", "", "pb", "", "", "qw"] + ["", "", "sw", "pw", "pw", "", "", ""] + ["", "", "pw", "", "", "", "", ""] + ["pw", "pw", "", "", "", "pw", "pw", "pw"] + ["lw", "hw", "sw", "", "", "lw", "kw", ""],
        "solution": [(31, 30), (23, 30), (58, 30)],
        },
    {
        "board": ["", "", "", "", "", "lb", "kb", "lb"] + ["pb", "pb", "", "", "lw", "pb", "", ""] + ["", "sb", "", "pb", "", "pw", "sb", ""] + ["", "", "", "pw", "", "", "qw", ""] + ["", "", "hb", "", "", "", "pw", ""] + ["", "", "pb", "", "", "", "", ""] + ["pw", "", "", "", "", "pw", "", ""] + ["", "", "", "", "lw", "", "kw", ""],
        "solution": [(30, 22), (13, 22), (12, 14)],
        },
    {
        "board": ["lb", "", "sb", "", "kb", "", "lb", ""] + ["pb", "pb", "pb", "pb", "", "pb", "", "pb"] + ["", "", "", "qb", "hw", "", "", "qw"] + ["", "", "sb", "", "hb", "", "sw", ""] + ["", "", "sw", "pb", "pw", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["pw", "pw", "pw", "", "", "pw", "pw", "pw"] + ["lw", "hw", "", "", "kw", "", "", "lw"],
        "solution": [(23, 5), (19, 5), (20, 10)],
        },
    {
        "board": ["", "lb", "", "kb", "lb", "", "", ""] + ["hw", "sb", "pb", "pb", "hb", "", "pb", "pb"] + ["", "sb", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "qw", ""] + ["", "", "", "sw", "", "pw", "", ""] + ["pw", "qb", "", "", "", "pw", "", "pw"] + ["", "", "", "lw", "lw", "", "kw", ""],
        "solution": [(38, 11), (3, 11), (43, 25)],
        },
    {
        "board": ["lb", "", "", "kb", "", "", "", ""] + ["pb", "pb", "pb", "", "hb", "", "", "pb"] + ["", "", "", "qb", "qw", "lb", "", ""] + ["", "", "", "pw", "", "", "", ""] + ["sw", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["pw", "pw", "pw", "", "", "", "pw", "pw"] + ["", "", "", "", "lw", "", "kw", ""],
        "solution": [(20, 6), (12, 6), (60, 4)],
        },
    {
        "board": ["", "", "kb", "lb", "", "sb", "", "lb"] + ["pb", "pb", "", "hb", "", "", "", "pb"] + ["", "", "pb", "", "pb", "qb", "", ""] + ["", "", "", "", "", "hb", "", ""] + ["", "", "sw", "pw", "", "sw", "", ""] + ["", "", "pw", "", "", "qw", "", ""] + ["pw", "pw", "", "hw", "", "", "pw", "pw"] + ["lw", "", "", "", "", "", "kw", ""],
        "solution": [(45, 18), (9, 18), (34, 16)],
        },
    {
        "board": ["", "", "lb", "", "", "", "", "kb"] + ["", "pb", "", "sb", "", "", "", "pb"] + ["pb", "", "", "", "pb", "", "", "qw"] + ["", "", "", "pb", "qb", "pb", "", ""] + ["", "pw", "", "", "", "", "", ""] + ["", "", "", "", "", "", "lw", "kw"] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", "lw"],
        "solution": [(23, 15), (7, 15), (47, 54)],
        },
    {
        "board": ["lb", "", "sb", "", "", "kb", "", "lb"] + ["", "pb", "", "", "sb", "pb", "pb", "pb"] + ["pb", "", "sw", "", "", "qb", "", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["", "", "", "", "", "", "", ""] + ["pw", "pw", "pw", "qw", "", "pw", "", "pw"] + ["", "", "kw", "lw", "lw", "", "", ""],
        "solution": [(51, 3), (12, 3), (60, 4)],
        },
    {
        "board": ["", "", "lb", "", "kb", "sb", "", "lb"] + ["pb", "pb", "pb", "", "pb", "qb", "", ""] + ["", "", "hb", "", "hw", "", "pb", ""] + ["", "", "", "", "", "pw", "pb", ""] + ["", "", "", "pw", "qw", "", "pw", ""] + ["", "", "", "", "", "", "", ""] + ["pw", "pw", "pw", "", "", "pw", "sw", ""] + ["lw", "", "sw", "", "kw", "", "", ""],
        "solution": [(36, 18), (9, 18), (54, 18)],
        },
    {
        "board": ["lb", "", "sb", "qb", "kb", "", "", "lb"] + ["pb", "", "pb", "hb", "", "pb", "pb", ""] + ["", "pb", "", "", "pb", "hb", "", "pb"] + ["", "", "", "", "", "", "", ""] + ["", "", "", "pw", "", "", "", ""] + ["sw", "", "pw", "sw", "", "", "", ""] + ["pw", "", "pw", "", "qw", "pw", "pw", "pw"] + ["lw", "", "", "", "kw", "", "hw", "lw"],
        "solution": [(52, 20), (13, 20), (43, 22)],
        }
    ]

    def get_random_puzzle():
        import random
        return random.choice(chess_puzzles)
python early:
    def hide_all_ui():
        renpy.hide_screen("hud")
        renpy.hide_screen("time_display")
        renpy.hide_screen("pc_in_mainroom")
        renpy.hide_screen("tv_in_mainroom")
        renpy.hide_screen("bed_in_mainroom")
        renpy.hide_screen("door_in_mainroom")
        renpy.hide_screen("box_in_mainroom")
        renpy.hide_screen("pc_in_mainroom_night")
        renpy.hide_screen("tv_in_mainroom_night")
        renpy.hide_screen("bed_in_mainroom_night")
        renpy.hide_screen("door_in_mainroom_night")
        renpy.hide_screen("box_in_mainroom_night")
        renpy.hide_screen("inventory_bag")
        renpy.hide_screen("inventory")
        renpy.hide_screen("money_mainroom")
        renpy.hide_screen("vibro_mainroom")
        renpy.hide_screen("sigame_logo")
        renpy.hide_screen("back_arrow")
        renpy.hide_screen("yandex_browzer_logo")
        renpy.hide_screen("cian")
        renpy.hide_screen("aviasales")
        renpy.hide_screen("casino_sochi")
        renpy.hide_screen("litres")
        renpy.hide_screen("back_ya_1")
        renpy.hide_screen("rebus_mainroom")
        renpy.hide_screen("door_to_street")
        renpy.hide_screen("door_to_mainroom")
        renpy.hide_screen("door_to_vitya_room")
        renpy.hide_screen("door_to_toilet")
        renpy.hide_screen("door_to_kitchen")
        renpy.hide_screen("back_arrow_to_hallway")
        renpy.hide_screen("home_point")
        renpy.hide_screen("casino_map_point")
        renpy.hide_screen("airport_map_point")
        renpy.hide_screen("back_arrow_to_map")
        renpy.hide_screen("masterskaya_map_point")
        renpy.hide_screen("police_map_point")
        renpy.hide_screen("iphone")
        renpy.hide_screen("big_iphone")
        renpy.hide_screen("vitya_in_vitya2_room")
        renpy.hide_screen("unitaz")
        renpy.hide_screen("dush")
        renpy.hide_screen("rakovina_bathroom")
        renpy.hide_screen("mirror")
        renpy.hide_screen("yaschik_bathroom")
        renpy.hide_screen("yaschik_vitya")
        renpy.hide_screen("door_to_masterskaya")
        renpy.hide_screen("back_arrow_to_masterskaya")
        renpy.hide_screen("chingis")
        renpy.hide_screen("bar_map_point")
        renpy.hide_screen("door_to_bar")
        renpy.hide_screen("back_arrow_to_vhod_bar")
        renpy.hide_screen("back_arrow_to_bar")
        renpy.hide_screen("to_slut")
        renpy.hide_screen("chess_players")
        renpy.hide_screen("slut")
        renpy.hide_screen("chess")
        renpy.hide_screen("back_arrow_to_slut")
        renpy.hide_screen("sportcar")
        renpy.hide_screen("door_to_casino")
        renpy.hide_screen("back_arrow_to_casino")
        renpy.hide_screen("door_kosti")
        renpy.hide_screen("door_ruletka")
        renpy.hide_screen("door_karti")
        renpy.hide_screen("back_arrow_to_casino_hall")
        renpy.hide_screen("back_arrow_to_casino_hall2")
        renpy.hide_screen("back_arrow_to_casino_hal3")
        renpy.hide_screen("odd")
        renpy.hide_screen("even")
        renpy.hide_screen("odintri")
        renpy.hide_screen("chetireshest")
        renpy.hide_screen("odin2")
        renpy.hide_screen("tri4")
        renpy.hide_screen("pyat6")
        renpy.hide_screen("odyn")
        renpy.hide_screen("dva")
        renpy.hide_screen("tri")
        renpy.hide_screen("chetire")
        renpy.hide_screen("pyat")
        renpy.hide_screen("shest")
        renpy.hide_screen("kost1")
        renpy.hide_screen("kost2")
        renpy.hide_screen("kost3")
        renpy.hide_screen("kost4")
        renpy.hide_screen("kost5")
        renpy.hide_screen("kost6")
        renpy.hide_screen("money")
        renpy.hide_screen("back_arrow_to_casino_hall_ruletka")
        renpy.hide_screen("cards")
        renpy.hide_screen("diller_1")
        renpy.hide_screen("start")
        renpy.hide_screen("higher")
        renpy.hide_screen("lower")
        renpy.hide_screen("inin")
        renpy.hide_screen("out")
        renpy.hide_screen("cherva")
        renpy.hide_screen("pika")
        renpy.hide_screen("trefa")
        renpy.hide_screen("buba")
        renpy.hide_screen("diller_2")
        renpy.hide_screen("dice_field")
        renpy.hide_screen("roulette")
        renpy.hide_screen("diller_3")
        renpy.hide_screen("roulette_field")
        renpy.hide_screen("roulette_ball")
        renpy.hide_screen("roulette36")
        renpy.hide_screen("roulette35")
        renpy.hide_screen("roulette34")
        renpy.hide_screen("roulette33")
        renpy.hide_screen("roulette32")
        renpy.hide_screen("roulette31")
        renpy.hide_screen("roulette30")
        renpy.hide_screen("roulette29")
        renpy.hide_screen("roulette28")
        renpy.hide_screen("roulette27")
        renpy.hide_screen("roulette26")
        renpy.hide_screen("roulette25")
        renpy.hide_screen("roulette24")
        renpy.hide_screen("roulette23")
        renpy.hide_screen("roulette22")
        renpy.hide_screen("roulette21")
        renpy.hide_screen("roulette20")
        renpy.hide_screen("roulette19")
        renpy.hide_screen("roulette18")
        renpy.hide_screen("roulette17")
        renpy.hide_screen("roulette16")
        renpy.hide_screen("roulette15")
        renpy.hide_screen("roulette14")
        renpy.hide_screen("roulette13")
        renpy.hide_screen("roulette12")
        renpy.hide_screen("roulette11")
        renpy.hide_screen("roulette10")
        renpy.hide_screen("roulette9")
        renpy.hide_screen("roulette8")
        renpy.hide_screen("roulette7")
        renpy.hide_screen("roulette6") 
        renpy.hide_screen("roulette5") 
        renpy.hide_screen("roulette4") 
        renpy.hide_screen("roulette3") 
        renpy.hide_screen("roulette2") 
        renpy.hide_screen("roulette1") 
        renpy.hide_screen("zero") 
        renpy.hide_screen("start_roulette") 
        renpy.hide_screen("roulette1_34")
        renpy.hide_screen("roulette2_35")
        renpy.hide_screen("roulette3_36")
        renpy.hide_screen("roulette_1st12")
        renpy.hide_screen("roulette_2nd12")
        renpy.hide_screen("roulette_3rd12")
        renpy.hide_screen("roulette_1to18")
        renpy.hide_screen("roulette_red")
        renpy.hide_screen("roulette_even")
        renpy.hide_screen("roulette_black")
        renpy.hide_screen("roulette_odd")
        renpy.hide_screen("roulette_19to36")
        renpy.hide_screen("shop_map_point")
        renpy.hide_screen("door_to_shop")
        renpy.hide_screen("shop_start")
        renpy.hide_screen("product1")
        renpy.hide_screen("product2")
        renpy.hide_screen("product3")
        renpy.hide_screen("product4")
        renpy.hide_screen("product5")
        renpy.hide_screen("product6")
        renpy.hide_screen("product7")
        renpy.hide_screen("product8")
        renpy.hide_screen("product9")
        renpy.hide_screen("product10")
        renpy.hide_screen("product11")
        renpy.hide_screen("product12")
        renpy.hide_screen("product13")
        renpy.hide_screen("product14")
        renpy.hide_screen("product15")
        renpy.hide_screen("product16")
        renpy.hide_screen("product17")
        renpy.hide_screen("ph")
        renpy.hide_screen("back_to_ya")
        renpy.hide_screen("buner")
        renpy.hide_screen("buner1")
        renpy.hide_screen("back_arrow_to_kitchen")
        renpy.hide_screen("plita")
        renpy.hide_screen("skovorodka")
        renpy.hide_screen("skovorodka_onion")
        renpy.hide_screen("skovorodka_carrot")
        renpy.hide_screen("skovorodka_meat")
        renpy.hide_screen("skovorodka_meat_salt")
        renpy.hide_screen("skovorodka_paper")
        renpy.hide_screen("skovorodka_ketchup")
        renpy.hide_screen("skovorodka_pasta")
        renpy.hide_screen("skovorodka_oil")
        renpy.hide_screen("skovorodka_muka")
        renpy.hide_screen("skovorodka_milk")
        renpy.hide_screen("skovorodka_salt")
        renpy.hide_screen("skovorodka_nuts")
        renpy.hide_screen("list1")
        renpy.hide_screen("meat")
        renpy.hide_screen("onion")
        renpy.hide_screen("carrot")
        renpy.hide_screen("ketchup")
        renpy.hide_screen("pasta")
        renpy.hide_screen("oil")
        renpy.hide_screen("muka")
        renpy.hide_screen("miska")
        renpy.hide_screen("miska_bolonieze")
        renpy.hide_screen("forma")
        renpy.hide_screen("forma_beshamel")
        renpy.hide_screen("forma_list")
        renpy.hide_screen("forma_bolonieze")
        renpy.hide_screen("forma_mini_cheese")
        renpy.hide_screen("terka")
        renpy.hide_screen("salt")
        renpy.hide_screen("paper")
        renpy.hide_screen("milk")
        renpy.hide_screen("nuts")
        renpy.hide_screen("knife")
        renpy.hide_screen("doska")
        renpy.hide_screen("cheese")
        renpy.hide_screen("mini_cheese")
        renpy.hide_screen("table")
        renpy.hide_screen("cut_onion")
        renpy.hide_screen("onion_on_board")
        renpy.hide_screen("cut_carrot")
        renpy.hide_screen("carrot_on_board")
        renpy.hide_screen("cut_nuts")
        renpy.hide_screen("nuts_on_board")
        renpy.hide_screen("duhovka")
        renpy.hide_screen("back_arrow_to_vitya_room")
        renpy.hide_screen("lock")
        renpy.hide_screen("locked_lock")
        renpy.hide_screen("ploskogubci")
        renpy.hide_screen("moovie_ticket")
        renpy.hide_screen("money_10_1")
        renpy.hide_screen("money_10_2")
        renpy.hide_screen("smartphone")
        renpy.hide_screen("money_10_3")
        renpy.hide_screen("glasses")
        renpy.hide_screen("gondon")
        renpy.hide_screen("flash_card")
        renpy.hide_screen("disk")
        renpy.hide_screen("gvozd")
        renpy.hide_screen("superkley")
        renpy.hide_screen("humer")
        renpy.hide_screen("masterskaya_browzer")
        renpy.hide_screen("sdat_button")
        renpy.hide_screen("messange_false")
        renpy.hide_screen("zvonok_ot_shluhi")
        renpy.hide_screen("zvonok_ot_shluhi_vzyat")
        renpy.hide_screen("rozetka")
        renpy.hide_screen("rozetka_night")
        renpy.hide_screen("sudoku_game")
        renpy.hide_screen("color")
        renpy.hide_screen("another_product")
        renpy.hide_screen("bluegen")
        renpy.hide_screen("emergene")
        renpy.hide_screen("snyat_button")
        renpy.hide_screen("snyat_button2")
        renpy.hide_screen("kupit")
        renpy.hide_screen("points")
        renpy.hide_screen("reed_button_1")
        renpy.hide_screen("reed_button_2")
        renpy.hide_screen("reed_button_3")
        renpy.hide_screen("reed_button_4")
        renpy.hide_screen("reed_button_5")
        renpy.hide_screen("reed_button_6")
        renpy.hide_screen("school_map_point")
        renpy.hide_screen("foto_map_point")
        renpy.hide_screen("fishman_map_point")
        renpy.hide_screen("river_map_point")
        renpy.hide_screen("door_to_school")
        renpy.hide_screen("door_to_piano")
        renpy.hide_screen("back_arrow_to_school")
        renpy.hide_screen("piano")
        renpy.hide_screen("piano_teacher")
        renpy.hide_screen("back_arrow_to_school_hall")
        renpy.hide_screen("piano_board")
        renpy.hide_screen("back_arrow_to_piano")
        renpy.hide_screen("back_arrow_to_school_room")
        renpy.hide_screen("door_to_foto")
        renpy.hide_screen("back_arrow_to_foto_studio_vhod")
        renpy.hide_screen("model")
        renpy.hide_screen("door_to_grim")
        renpy.hide_screen("door_to_photo")
        renpy.hide_screen("miror")
        renpy.hide_screen("back_arrow_to_grim_room")
        renpy.hide_screen("fishman")
        renpy.hide_screen("fishbook")
        renpy.hide_screen("zaton")
        renpy.hide_screen("deep")
        renpy.hide_screen("not_deep")
        renpy.hide_screen("ryaska")
        renpy.hide_screen("door_to_police")
        renpy.hide_screen("veshi_door")
        renpy.hide_screen("back_arrow_to_police_hall")
        renpy.hide_screen("box")
        renpy.hide_screen("main_ment_door")
        renpy.hide_screen("ment_door")
        renpy.hide_screen("ment")
        renpy.hide_screen("back_arrow_to_police")
        renpy.hide_screen("barmen")
        renpy.hide_screen("beer_glas")
        renpy.hide_screen("coconut_milk")
        renpy.hide_screen("cocteil_glas")
        renpy.hide_screen("cointreau")
        renpy.hide_screen("ice")
        renpy.hide_screen("lime_juice")
        renpy.hide_screen("mohito_glas")
        renpy.hide_screen("mors")
        renpy.hide_screen("myata")
        renpy.hide_screen("pina_colada_glas")
        renpy.hide_screen("salt_b")
        renpy.hide_screen("soda")
        renpy.hide_screen("sugar")
        renpy.hide_screen("teqila")
        renpy.hide_screen("vodka")
        renpy.hide_screen("white_rom") 
        renpy.hide_screen("shaker")
        renpy.hide_screen("german_beer")   
        renpy.hide_screen("krest")
        renpy.hide_screen("label1")
        renpy.hide_screen("label2")
        renpy.hide_screen("label3")
        renpy.hide_screen("label4")
        renpy.hide_screen("label5")
        renpy.hide_screen("label6")
        renpy.hide_screen("zona1")
        renpy.hide_screen("zona2")
        renpy.hide_screen("zona3")
        renpy.hide_screen("zona4")
        renpy.hide_screen("zona5")
        renpy.hide_screen("zona6")
        renpy.hide_screen("label1_zona")
        renpy.hide_screen("label2_zona")
        renpy.hide_screen("label3_zona")
        renpy.hide_screen("label4_zona")
        renpy.hide_screen("label5_zona")
        renpy.hide_screen("label6_zona")
        renpy.hide_screen("folder_sort_game")
        renpy.hide_screen("folder_sort_game_delete")
        renpy.hide_screen("ment_notebook")
        renpy.hide_screen("back_arrow_to_ment_room")
        renpy.hide_screen("song_play")
        renpy.hide_screen("listok")
        renpy.hide_screen("hud_lips")
        renpy.hide_screen("hud_eyes")
        renpy.hide_screen("miror_hair")
        renpy.hide_screen("miror_lips")
        renpy.hide_screen("miror_lins")
        renpy.hide_screen("miror_eyes")
        renpy.hide_screen("hair_pal")
        renpy.hide_screen("lips_pal")
        renpy.hide_screen("lins_pal")
        renpy.hide_screen("eyes_pal")
        renpy.hide_screen("work_map_point")
        renpy.hide_screen("emeregen_build")
        renpy.hide_screen("bluegen_build")
        renpy.hide_screen("back_arrow_to_street")
        renpy.hide_screen("turniket")
        renpy.hide_screen("sekretarsha")
        renpy.hide_screen("back_arrow_to_emeregen_vhod")
        renpy.hide_screen("emeregen_director_door")
        renpy.hide_screen("back_arrow_to_emeregen_hall")
        renpy.hide_screen("emeregen_director_door")
        renpy.hide_screen("emeregen_director")
        renpy.hide_screen("security")
        renpy.hide_screen("lift")
        renpy.hide_screen("bluegen_up")
        renpy.hide_screen("lift_button")
        renpy.hide_screen("bluegen_2nd_flat_up")
        renpy.hide_screen("bluegen_2nd_flat_down")
        renpy.hide_screen("bluegen_2nd_flat_door")
        renpy.hide_screen("bluegen_2nd_flat_doors_1")
        renpy.hide_screen("bluegen_2nd_flat_doors_2")
        renpy.hide_screen("bluegen_2nd_flat_doors_3")
        renpy.hide_screen("laborant_2")
        renpy.hide_screen("vesi")
        renpy.hide_screen("back_arrow_to_bluegen_2nd_flat_doors")
        renpy.hide_screen("ves_button")
        renpy.hide_screen("box_1")
        renpy.hide_screen("box_2")
        renpy.hide_screen("box_3")
        renpy.hide_screen("box_4")
        renpy.hide_screen("box_5")
        renpy.hide_screen("box_6")
        renpy.hide_screen("back_arrow_to_laborant2")
        renpy.hide_screen("back_arrow_to_bluegen_2nd_flat")
        renpy.hide_screen("bluegen_3rd_flat_down")
        renpy.hide_screen("bluegen_3rd_flat_door")
        renpy.hide_screen("bluegen_3rd_flat_doors_4")
        renpy.hide_screen("back_arrow_to_third_doors")
        renpy.hide_screen("it")
        renpy.hide_screen("bluegen_3rd_flat_doors_5")
        renpy.hide_screen("bluegen_3rd_flat_doors_main")
        renpy.hide_screen("back_arrow_to_bluegen_3rd_flat")
        renpy.hide_screen("laborant_5")
        renpy.hide_screen("mikroscop")
        renpy.hide_screen("tea_table")
        renpy.hide_screen("nachalnik")
        renpy.hide_screen("nachalnik_yaschik")
        renpy.hide_screen("vint_1")
        renpy.hide_screen("vint_2")
        renpy.hide_screen("back_arrow_to_bluegen_vhod")
        renpy.hide_screen("microscope")
        renpy.hide_screen("konec")
        renpy.hide_screen("back_arrow_to_microscope")
        renpy.hide_screen("sbros_button")
        renpy.hide_screen("resoult_button")
        renpy.hide_screen("show_ves_text")
        renpy.hide_screen("sugar_vesi")
        renpy.hide_screen("green_tea")
        renpy.hide_screen("black_tea")
        renpy.hide_screen("teapot")
        renpy.hide_screen("cup")
        renpy.hide_screen("coffe")
        renpy.hide_screen("nachalnik_yaschik_empty")
        renpy.hide_screen("emeregen_id")
        renpy.hide_screen("keys_2_lab")
        renpy.hide_screen("back_arrow_to_kabinet_nachalnika")
        renpy.hide_screen("edik_skaf")
        renpy.hide_screen("papka_1")
        renpy.hide_screen("papka_2")
        renpy.hide_screen("papka_3")
        renpy.hide_screen("papka_4")
        renpy.hide_screen("papka_5")
        renpy.hide_screen("papka_6")
        renpy.hide_screen("back_arrow_to_edik_room")
        renpy.hide_screen("vhod")
        renpy.hide_screen("vihod")
        renpy.hide_screen("miska_p")
        renpy.hide_screen("truba")
        renpy.hide_screen("truba_max")
        renpy.hide_screen("back_arrow_to_podval")
        renpy.hide_screen("blackmail_map_point")
        renpy.hide_screen("back_arrow_to_bathroom")
        renpy.hide_screen("kosmetik")

    def show_hud():
        renpy.show_screen("hud")
        renpy.show_screen("key_handler") 
        renpy.show_screen("inventory_bag") 
        renpy.show_screen("time_display")
        renpy.show_screen("iphone")
        renpy.show_screen("hud_lips")
        renpy.show_screen("hud_eyes")         
    
    
    
    # Функция для добавления предмета в инвентарь
    def add_item_to_inventory(item):
        global inventory_items
        for i in range(len(inventory_items)):
            if inventory_items[i] is None:
                inventory_items[i] = item
                return True
        return False  # Если инвентарь полный

    def remove_item_to_inventory(item):
        global inventory_items
        for i in range(len(inventory_items)):
            if inventory_items[i] == item:
                inventory_items[i] = None
                return True
        return False  # Если инвентарь полный

init python:
    style.dedication_line = Style(style.default)
    style.dedication_line.font = "fonts/Roboto-Light.ttf"
    style.dedication_line.size = 36
    style.dedication_line.color = "#FFFFFF"
    style.dedication_line.outlines = [(1, "#000000AA", 0, 0)]
    style.dedication_line.kerning = 2.0
    style.dedication_line.text_align = 0.5
    style.dedication_line.xalign = 0.5
    style.dedication_line.yalign = 0.5

define audio.dedication_music = "audio/intro.mp3"
image dedication_bg = Solid("#000000")
image production_bg = Solid("#000000")

image production_lines:
    contains:
        Text(
            "Production by Ivan Tambovcev",
            style="dedication_line",
            xalign=0.5, yalign=0.4
        )
        alpha 0.0
        linear 2.0 alpha 1.0

image dedication_lines:
    contains:
        Text(
            "Эта игра посвящается моему другу Виктору, который открыл мне мир программирования,",
            style="dedication_line",
            xalign=0.5, yalign=0.4
        )
        alpha 0.0
        linear 2.0 alpha 1.0

    contains:
        Text(
            "и его жене Виктории, которая делает его жизнь счастливее.",
            style="dedication_line",
            xalign=0.5, yalign=0.45
        )
        alpha 0.0
        pause 4.0
        linear 2.0 alpha 1.0

    contains:
        Text(
            "Спасибо вам за то что вдохновляете на такие проекты.",
            style="dedication_line",
            xalign=0.5, yalign=0.5
        )
        alpha 0.0
        pause 6.0
        linear 2.0 alpha 1.0

    contains:
        Text(
            "Живите и дальше так же счастливо.",
            style="dedication_line",
            xalign=0.5, yalign=0.55
        )
        alpha 0.0
        pause 8.0
        linear 2.0 alpha 1.0

    pause 10.0


screen dedication():
    add "dedication_bg"
    add "dedication_lines"

screen production():
    add "production_bg"
    add "production_lines"

image difficulty_bg = Solid("#000000")

screen difficulty_select():
    tag menu

    add "difficulty_bg"

    # Заголовок
    text "Выберите уровень сложности" style "difficulty_title" at fade_in_center

    # Эмблемы
    imagebutton:
        idle "easy_icon.png"
        hover "easy_icon.png"
        at fade_in_left
        xpos 0.25 ypos 0.5 anchor (0.5, 0.5)
        if block_ui == False:
            action [SetVariable("slojnost_igry", "easy"), Jump("head_family")]
        hovered SetVariable("hover_text", "easy")
        unhovered SetVariable("hover_text", None)

    imagebutton:
        idle "hard_icon.png"
        hover "hard_icon.png"
        at fade_in_right
        xpos 0.75 ypos 0.5 anchor (0.5, 0.5)
        if block_ui == False:
            action [SetVariable("slojnost_igry", "hard"), Jump("head_family")]
        hovered SetVariable("hover_text", "hard")
        unhovered SetVariable("hover_text", None)

    if block_ui == False:
        if hover_text == "easy":
            frame:
                background "#44444488"
                xalign 0.5
                yalign 0.85
                padding (20, 10)
                text "Это лёгкий уровень сложности — в нём доступны подсказки, более лёгкие головоломки, а также возможность повысить интеллект." style "tooltip_text"

        elif hover_text == "hard":
            frame:
                background "#44444488"
                xalign 0.5
                yalign 0.85
                padding (20, 10)
                text "Это сложный уровень — без подсказок, с более тяжёлыми головоломками. Повышение интеллекта недоступно." style "tooltip_text"

# Анимации
transform fade_in_center:
    alpha 0.0
    pause 1.5
    linear 1.0 alpha 1.0
    yalign 0.2

transform fade_in_left:
    alpha 0.0
    pause 3.0
    linear 1.0 alpha 1.0
    linear 0.5 xoffset 0

transform fade_in_right:
    alpha 0.0
    pause 4.5
    linear 1.0 alpha 1.0
    linear 0.5 xoffset 0

# Стили
init python:
    style.difficulty_title = Style(style.default)
    style.difficulty_title.font = "fonts/Roboto-Light.ttf"
    style.difficulty_title.size = 48
    style.difficulty_title.color = "#FFFFFF"
    style.difficulty_title.xalign = 0.5
    style.difficulty_title.yalign = 0.2

    style.tooltip_text = Style(style.default)
    style.tooltip_text.font = "fonts/Roboto-Light.ttf"
    style.tooltip_text.size = 24
    style.tooltip_text.color = "#FFFFFF"
    style.tooltip_text.xalign = 0.5
    style.tooltip_text.text_align = 0.5

# Переменная для подсказок
default hover_text = None


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5   # время автопромота в секундах
    $ renpy.invoke_in_thread(_afm_timer)
    show screen click_blocker
    show screen difficulty_select
    $ start_dialog()
    $ clicks_enabled = False
    $ block_ui = True
    pause 6.5
    $ stop_dialog()
    $ block_ui = False
    $ clicks_enabled = True
    call screen wait_for_click
    return

label head_family:
    

    if slojnost_igry == "easy":
        $ card_money = 2000
    else:
        $ card_money = 1825
    if slojnost_igry == "easy":
        $ sudoku_solution = [
            [4,7,9, 2,6,5, 1,8,3],
            [5,6,8, 7,1,3, 2,4,9],
            [2,1,3, 4,9,8, 5,6,7],

            [1,9,2, 5,7,4, 8,3,6],
            [3,4,5, 8,2,6, 9,7,1],
            [7,8,6, 9,3,1, 4,2,5],

            [6,2,1, 3,4,9, 7,5,8],
            [8,3,4, 1,5,7, 6,9,2],
            [9,5,7, 6,8,2, 3,1,4],
        ]

        # Переменная для отслеживания, решено ли судоку
        $ sudoku_proideno = False

        # Начальная сетка судоку: 0 — пустая клетка
        $ sudoku_puzzle = [
            [0,0,0, 2,0,5, 0,8,3],
            [0,0,8, 0,0,0, 2,0,9],
            [0,1,0, 0,9,0, 0,0,0],

            [0,0,2, 0,0,0, 0,3,0],
            [0,4,5, 0,2,6, 0,0,0],
            [0,8,0, 9,0,1, 4,0,0],

            [6,0,1, 0,0,0, 0,5,0],
            [8,0,4, 1,5,7, 6,0,2],
            [9,0,7, 0,8,2, 3,1,4],
        ]
        
        # Список для отслеживания стандартных цифр (чтобы не менять их)
        $ sudoku_puzzle_default = [
            [0,0,0, 2,0,5, 0,8,3],
            [0,0,8, 0,0,0, 2,0,9],
            [0,1,0, 0,9,0, 0,0,0],

            [0,0,2, 0,0,0, 0,3,0],
            [0,4,5, 0,2,6, 0,0,0],
            [0,8,0, 9,0,1, 4,0,0],

            [6,0,1, 0,0,0, 0,5,0],
            [8,0,4, 1,5,7, 6,0,2],
            [9,0,7, 0,8,2, 3,1,4],
        ]

    else:
        $ sudoku_solution = [
            [6, 1, 3, 5, 4, 9, 8, 2, 7],
            [9, 8, 4, 6, 7, 2, 5, 3, 1],
            [2, 5, 7, 8, 3, 1, 6, 4, 9],

            [7, 4, 5, 3, 9, 6, 2, 1, 8],
            [8, 3, 2, 1, 5, 7, 4, 9, 6],
            [1, 9, 6, 2, 8, 4, 7, 5, 3],

            [4, 2, 9, 7, 6, 3, 1, 8, 5],
            [3, 7, 8, 4, 1, 5, 9, 6, 2],
            [5, 6, 1, 9, 2, 8, 3, 7, 4]
        ]

        # Переменная для отслеживания, решено ли судоку
        $ sudoku_proideno = False

        # Начальная сетка судоку: 0 — пустая клетка
        $ sudoku_puzzle = [
            [0,0,0, 0,0,0, 0,2,7],
            [0,8,0, 0,0,0, 5,0,0],
            [0,0,0, 8,3,1, 0,0,0],

            [0,0,0, 0,9,0, 0,1,0],
            [0,0,0, 0,0,7, 0,9,0],
            [0,0,6, 2,8,0, 0,0,0],

            [4,0,0, 7,0,0, 1,8,0],
            [3,7,0, 4,0,5, 0,0,0],
            [0,0,0, 0,2,0, 0,0,0],
        ]
        
        # Список для отслеживания стандартных цифр (чтобы не менять их)
        $ sudoku_puzzle_default = [
            [0,0,0, 0,0,0, 0,2,7],
            [0,8,0, 0,0,0, 5,0,0],
            [0,0,0, 8,3,1, 0,0,0],

            [0,0,0, 0,9,0, 0,1,0],
            [0,0,0, 0,0,7, 0,9,0],
            [0,0,6, 2,8,0, 0,0,0],

            [4,0,0, 7,0,0, 1,8,0],
            [3,7,0, 4,0,5, 0,0,0],
            [0,0,0, 0,2,0, 0,0,0],
        ]
    $ clicks_enabled = False
    play music dedication_music fadein 3.0
    hide screen difficulty_select with fade
    pause 2.0
    $ start_dialog()
    show screen production
    pause 4.0
    hide screen production
    show screen dedication
    pause 12.0  # Общее время анимации
    hide screen dedication with Dissolve(3.0)    
    play movie "video/intro.webm" noloop
    pause 16.0
    stop music fadeout 3.0
    pause 2.0
    scene black
    scene bg_hall_night
    with fade
    pause 2.0
    show vika neutral at center
    with dissolve
    $ _preferences.afm_enable = True      # включаем автопромот
    voice "audio/voices/vika/1.mp3"
    Vika "Чёрт... Десять вечера, суббота, а я только с работы пришла."
    
    show vitya_neutral at right
    with dissolve
    show vika neutral at left
    with dissolve
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    voice "audio/voices/vika/2.mp3"  # Укажите ваш путь и формат файла
    Vika "Ты даже не вышел встретить. Я вся убитая!"
    voice "audio/voices/vitya/58.mp3"
    vitya "Я занят был. Решал кое-что по питону."
    voice "audio/voices/vika/3.mp3"
    Vika "По какому питону!? Я тут с ума схожу на этой биолаборатории!!!"
    voice "audio/voices/vika/4.mp3"
    Vika "Нас опять нагрузили клиническими данными, а зарплату не выдали! Начальник выносит мозг! коллеги пассивные! а работать всё мне!"
    voice "audio/voices/vitya/59.mp3"
    vitya "Представляешь, сегодня стажёр написал кучу циклов для создания списков, конечно же мне пришлось ему рассказать про list comprehension, с ним ведь код намного читаймее."
    voice "audio/voices/vika/5.mp3"
    Vika "...Что ты сейчас сказал!?"
    voice "audio/voices/vitya/60.mp3"
    vitya "Вместо итеративного аппенда через мутабел-обджект мы получаем чистый функциональный стиль с ленивой оценкой!"
    voice "audio/voices/vika/6.mp3"
    Vika "Стоп. Я вообще ни слова не поняла. Ты слышал, что я сказала?!"
    voice "audio/voices/vitya/61.mp3"
    vitya "Да-да, ты устала. Понимаю. Но ты бы видела, как элегантно всё заработало!"
    voice "audio/voices/vika/7.mp3"
    Vika "…Я пошла спать."
    $ clicks_enabled = True
    hide vitya_neutral
    $ add_item_to_inventory("pasport")
    $ add_item_to_inventory("phone")
    with dissolve
    jump mainroom

label mainroom:
    $ renpy.free_memory()
    $ hide_all_ui()
    if game_hour == 22:
        scene bg mainroom_night
        show screen tv_in_mainroom_night
        show screen pc_in_mainroom_night
        show screen bed_in_mainroom_night
        show screen door_in_mainroom_night
        show screen box_in_mainroom_night
        show screen rozetka_night
    else:
        scene bg mainroom
        show screen tv_in_mainroom
        show screen pc_in_mainroom
        show screen bed_in_mainroom
        show screen door_in_mainroom
        show screen box_in_mainroom
        show screen rozetka
    if day_index == 0 and messange_from_ment == False:
        $ renpy.music.set_pause(True)
        play sound "messange.mp3"
        pause 1.0
        show screen ment_messenge
        $ block_ui = True
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/vika/8.mp3"
        Vika "О нет! Кажется плакала моя поездка в питер! надо с этим разобраться."
        $ stop_dialog()
        $ i_know_casino = False
        play music "home_theme.mp3" fadeout 1
        $ block_ui = False
        $ messange_from_ment = True
        $ quest_list[17]["available"] = True
        hide screen ment_messenge
    elif day_index == 1 and messange_from_nachalnik == False:
        $ renpy.music.set_pause(True)
        play sound "zvonok.mp3"
        pause 0.5
        show screen nachalnik_contact_is_calling
        pause 2.5
        hide screen nachalnik_contact_is_calling
        show screen nachalnik_contact_call_photo
        $ clara_suck_now = False
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/nachalnik/1.mp3"
        nachalnik "Башкова!!! Почему тебя не было вчера на работе???"
        voice "audio/voices/vika/9.mp3"
        Vika "Вообще-то вы меня уволили!"
        voice "audio/voices/nachalnik/2.mp3"
        nachalnik "Когда?"
        voice "audio/voices/vika/10.mp3"
        Vika "В воскресенье"
        voice "audio/voices/nachalnik/3.mp3"
        nachalnik "Я был бухой?"
        voice "audio/voices/vika/11.mp3"
        Vika "Не знаю, наверное..."
        voice "audio/voices/nachalnik/4.mp3"
        nachalnik "Ясно, быстро на работу и сразу ко мне в кабинет"
        $ stop_dialog()
        $ quest_list[28]["available"] = True
        $ messange_from_nachalnik = True
        $ i_know_work = True
        play sound "sbros.mp3"
        hide screen nachalnik_contact_call_photo
        play music "home_theme.mp3" fadeout 1
    if game_hour == 22:
        jump tolate
    
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen ment_messenge:
    add "messedger_with_ment.png" xpos 750 ypos 150

screen ment_messenge_2:
    modal True
    add "messedger_with_ment.png" xpos 750 ypos 150

label tolate:
    $ block_ui = True
    $ renpy.music.set_pause(True)
    $ start_dialog()
    voice "audio/voices/vika/12.mp3"
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    Vika "Уже десять часов, пора ложиться спать..."
    $ stop_dialog()
    play music "night_music.mp3" fadeout 1
    $ block_ui = False
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen rozetka:
    imagebutton:
        idle "rozetka.png"        
        focus_mask True
        if not block_ui:
            hover "rozetka_hover.png"
            if rozetka_pochinena == False:
                action Jump("rozetka")
            else:
                action Jump("rozetka_pochinena")  # Показываем меню выбора

screen rozetka_night:
    imagebutton:
        idle "rozetka_night.png"        
        focus_mask True
        if not block_ui:
            hover "rozetka_night_hover.png"
            if rozetka_pochinena == False:
                action Jump("tolate")
            else:
                action Jump("tolate")  # Показываем меню выбора

label rozetka:
    $ renpy.free_memory()
    $ block_ui = True
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    $ start_dialog()
    voice "audio/voices/vika/13.mp3"
    $ renpy.music.set_pause(True)
    Vika "Витя уже пол года не может починить эту розетку, надо ему напомнить."
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    $ quest_list[5]["available"] = True
    $ rozetka_is_broken = True
    $ block_ui = False
    jump mainroom

label rozetka_pochinena:
    $ renpy.free_memory()
    $ block_ui = True
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    $ start_dialog()
    voice "audio/voices/vika/14.mp3"
    $ renpy.music.set_pause(True)
    Vika "Чингыс уже починил её."
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    $ block_ui = False
    call screen wait_for_click
    return

screen hud():
    zorder 100
    frame:
        xalign 0.01
        yalign 0.01
        background "#0008"
        padding (10, 10)
        vbox:
            spacing 6

            # Фото персонажа
            imagebutton:
                if hair_color == "default":
                    idle "photo_vika.png" 
                elif hair_color == "green":
                    idle "photo_vika_green.png"
                elif hair_color == "blue":
                    idle "photo_vika_blue.png" 
                elif hair_color == "white":
                    idle "photo_vika_white.png" 
                elif hair_color == "black":
                    idle "photo_vika_black.png"  
                focus_mask True
                if default_mouse == "black_colour" and hair_color != "black":
                    action Jump("black_colour")
                elif default_mouse == "white_colour" and hair_color != "white":
                    action Jump("white_colour")
                elif default_mouse == "green_colour" and hair_color != "green":
                    action Jump("green_colour")
                elif default_mouse == "blue_colour" and hair_color != "blue":
                    action Jump("blue_colour")
            # Характеристики
            text "Интеллект: [intellect]"
            text "Деньги: [money]₽"

screen hud_lips:
    zorder 100
    frame:
        xalign 0.01
        yalign 0.01
        background "#0000"
        padding (8, 9)
        vbox:
            spacing 6
            if lips_color == "1":
                add "makeup/hud/lips_1.png"
            elif lips_color == "2":
                add "makeup/hud/lips_2.png"
            elif lips_color == "3":
                add "makeup/hud/lips_3.png"
            elif lips_color == "4":
                add "makeup/hud/lips_4.png"
            elif lips_color == "5":
                add "makeup/hud/lips_5.png"
            elif lips_color == "6":
                add "makeup/hud/lips_6.png"
            elif lips_color == "7":
                add "makeup/hud/lips_7.png"

screen hud_eyes:
    zorder 100
    frame:
        xalign 0.01
        yalign 0.01
        background "#0000"
        padding (8, 9)
        vbox:
            spacing 6
            if eyes_color == "1":
                add "makeup/hud/eyes_1.png"
            elif eyes_color == "2":
                add "makeup/hud/eyes_2.png"
            elif eyes_color == "3":
                add "makeup/hud/eyes_3.png"
            elif eyes_color == "4":
                add "makeup/hud/eyes_4.png"
            elif eyes_color == "5":
                add "makeup/hud/eyes_5.png"
            elif eyes_color == "6":
                add "makeup/hud/eyes_6.png"
            elif eyes_color == "7":
                add "makeup/hud/eyes_7.png"

label black_colour: 
    $ hair_color = "black"
    hide screen inventory
    $ default_mouse = "default"
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    $ start_dialog()
    voice "audio/voices/vika/15.mp3"
    $ renpy.music.set_pause(True)
    Vika "Как круто я выгляжу! Надо запостить это в инстаграмм!"
    play sound "snimok.mp3"
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label white_colour: 
    $ hair_color = "white"
    hide screen inventory
    $ default_mouse = "default"
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    $ start_dialog()
    voice "audio/voices/vika/15.mp3"
    $ renpy.music.set_pause(True)
    Vika "Как круто я выгляжу, надо запостить это в инстаграмм"
    play sound "snimok.mp3"
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label blue_colour: 
    $ hair_color = "blue"
    hide screen inventory
    $ default_mouse = "default"
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    $ renpy.music.set_pause(True)
    $ start_dialog()
    voice "audio/voices/vika/15.mp3"
    Vika "Как круто я выгляжу, надо запостить это в инстаграмм"
    play sound "snimok.mp3"
    if uvolena == False:
        pause 2.0
        play sound "zvonok.mp3"
        pause 0.5
        show screen nachalnik_contact_is_calling
        pause 2.5
        hide screen nachalnik_contact_is_calling
        show screen nachalnik_contact_call_photo
        $ uvolena = True
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/nachalnik/5.mp3"
        nachalnik "Молодец башкова, ты главная патриотка компании, но премию не жди"
        play sound "sbros.mp3"
    hide screen nachalnik_contact_call_photo
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label green_colour: 
    $ hair_color = "green"
    hide screen inventory
    $ default_mouse = "default"
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    $ renpy.music.set_pause(True)
    $ start_dialog()
    voice "audio/voices/vika/15.mp3"
    Vika "Как круто я выгляжу, надо запостить это в инстаграмм"
    play sound "snimok.mp3"
    if uvolena == False:
        pause 2.0
        play sound "zvonok.mp3"
        pause 0.5
        show screen nachalnik_contact_is_calling
        pause 2.5
        hide screen nachalnik_contact_is_calling
        show screen nachalnik_contact_call_photo
        $ uvolena = True
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/nachalnik/6.mp3"
        nachalnik "Башкова!!! Как ты посмела покрасится в цвет конкурентов??? Ты уволена!!!"
        $ quest_list[9]["done"] = True
        $ intellect += 1
        $ game_hour += 1
        $ update_game_time()
        play sound "sbros.mp3"
    hide screen nachalnik_contact_call_photo
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen nachalnik_contact_is_calling:
    add "phone/nachalnik_contact_calling.png" xpos 750 ypos 150

screen key_handler():
    key "i" action ToggleScreen("inventory")

screen time_display():
    frame:
        xalign 0.99
        yalign 0.01
        background "#0008"
        padding (10, 5)
        has vbox
        spacing 2

        text "[day_name]" size 20 color "#FFFFFF"
        text "[game_time]" size 20 color "#FFD700"

screen inventory_bag:
    zorder 99
    imagebutton:
        idle "inventory_bag_idle.png"
        xpos 1700
        ypos 880
        focus_mask True
        at Transform(zoom=0.2)
        if not block_ui:
            hover "inventory_bag_hover.png"
            action ToggleScreen("inventory")

screen iphone:
    zorder 90
    imagebutton:
        idle "iphone_idle.png"
        xpos 100
        ypos 830
        focus_mask True
        at Transform(zoom=1.0)
        if not block_ui:
            hover "iphone_hover.png"
            if no_signal == True:
                action Jump("no_signal")
            else:
                if iphone_is_showed == False:
                    action [Show("big_iphone"), SetVariable("iphone_is_showed", True), Hide("ment_messenge_2")]
                else:
                    action [
                        Hide("big_iphone"), 
                        Hide("phone"), Hide("tinkoff"), 
                        Hide("photo"), Hide("wildberies"), 
                        Hide("ozon"), Hide("taxi"), 
                        Hide("zametki"), Hide("appstore"), 
                        Hide("messenger"),
                        Hide("photo_1"),
                        Hide("photo_2"),
                        Hide("photo_3"),
                        Hide("photo_4"),
                        Hide("photo_5"),
                        Hide("photo_6"),
                        Hide("photo_7"),
                        Hide("photo_8"),
                        Hide("photo_9"),
                        Hide("photo_10"),
                        Hide("photo_11"),
                        Hide("photo_12"),
                        Hide("photo_13"),
                        Hide("photo_14"),
                        Hide("photo_15"),
                        Hide("photo_16"),
                        Hide("photo_17"),
                        Hide("photo_18"),
                        Hide("work_contact"),                
                        Hide("vitya_contact"),
                        Hide("ruslan_contact"),
                        Hide("nachalnik_contact"),
                        Hide("my_number_contact"),
                        Hide("maker_contact"),
                        Hide("dyadya_sasha_contact"),
                        Hide("alisa_contact"),
                        Hide("chingis_contact"),
                        SetVariable("iphone_is_showed", False)
                    ]

label no_signal:
    $ block_ui = True
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    $ renpy.music.set_pause(True)
    $ start_dialog()
    voice "audio/voices/vika/16.mp3"
    Vika "Бесполезно, связи нет!"
    $ stop_dialog()
    $ block_ui = False
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen big_iphone:
    modal True
    add "big_iphone.png" xpos 750 ypos 150
    imagebutton:
        idle "phone_icon_idle.png"
        xpos 790
        ypos 860
        focus_mask True
        if not block_ui:
            hover "phone_icon_hover.png"
            action [Hide("big_iphone"), Show("phone")]
    imagebutton:
        idle "tinkof_icon_idle.png"        
        xpos 875
        ypos 860
        focus_mask True
        if not block_ui:
            hover "tinkof_icon_hover.png"
            action Show("tinkoff")
    imagebutton:
        idle "apstore_icon_idle.png"        
        xpos 959
        ypos 859
        focus_mask True
        if not block_ui:
            hover "apstore_icon_hover.png"
            action [Hide("big_iphone"), Show("appstore")]
    if sudoku_download == True:
        imagebutton:
            idle "sudoku_icon.png"        
            xpos 750 
            ypos 150
            focus_mask True
            if not block_ui:
                hover "sudoku_icon_hover.png"
                action [Hide("big_iphone"), Show("sudoku_game")]
    imagebutton:
        idle "messedger_icon_idle.png"        
        xpos 1045
        ypos 859
        focus_mask True
        if not block_ui:
            hover "messedger_icon_hover.png"
            action [Hide("big_iphone"), Show("messenger")]
    imagebutton:
        idle "yandex_taxi_icon_idle.png"        
        xpos 790
        ypos 238
        focus_mask True
        if not block_ui:
            hover "yandex_taxi_icon_hover.png"
            action [Hide("big_iphone"), Jump("taxi")]
    imagebutton:
        idle "perishko_icon_idle.png"        
        xpos 875
        ypos 238
        focus_mask True
        if not block_ui:
            hover "perishko_icon_hover.png"
            action [Hide("big_iphone"), Jump("perishko")]
    imagebutton:
        idle "wb_icon_idle.png"        
        xpos 961
        ypos 240
        focus_mask True
        if not block_ui:
            hover "wb_icon_hover.png"
            action Show("wildberies")
    imagebutton:
        idle "ozon_icon_idle.png"       
        xpos 1047
        ypos 240
        focus_mask True
        if not block_ui:
            hover "ozon_icon_hover.png"
            action Show("ozon")
    imagebutton:
        idle "photo_icon_idle.png"        
        xpos 790
        ypos 325
        focus_mask True
        if not block_ui:
            hover "photo_icon_hover.png"
            action [Hide("big_iphone"), Show("photo")]
    imagebutton:
        idle "zametki_icon_idle.png"        
        xpos 875
        ypos 325
        focus_mask True
        if not block_ui:
            hover "zametki_icon_hover.png"
            action [Hide("big_iphone"), Show("zametki")]
     
screen phone:
    modal True
    add "phone.png" xpos 750 ypos 150
    imagebutton:
        idle "back_to_big_phone_idle.png"
        xpos 750
        ypos 150
        focus_mask True
        if not block_ui:
            hover "back_to_big_phone_hover.png"
            action [Hide("phone"), Show("big_iphone")]
    if i_know_chingis == True:
        imagebutton:
            idle "phone/chingis_number.png"
            xpos 750 ypos 150
            focus_mask True
            if not block_ui:
                hover "phone/chingis_number_hover.png"
                action [Hide("phone"), Show("chingis_contact")]
    imagebutton:
        idle "phone/maker_number.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/maker_number_hover.png"
            action [Hide("phone"), Show("maker_contact")]
    imagebutton:
        idle "phone/my_number.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/my_number_hover.png"
            action [Hide("phone"), Show("my_number_contact")]
    imagebutton:
        idle "phone/nachalnik_number.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/nachalnik_number_hover.png"
            action [Hide("phone"), Show("nachalnik_contact")]
    imagebutton:
        idle "phone/vitya_number.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/vitya_number_hover.png"
            action [Hide("phone"), Show("vitya_contact")]
    imagebutton:
        idle "phone/work_number.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/work_number_hover.png"
            action [Hide("phone"), Show("work_contact")]

screen work_contact:
    modal True
    add "phone/work_contact.png" xpos 750 ypos 150
    imagebutton:
        idle "phone/back_to_contacts_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/back_to_contacts_button_hover.png"
            action [Hide("work_contact"), Show("phone")]
    imagebutton:
        idle "phone/call_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/call_button_hover.png"
            action [Hide("work_contact"), Jump("work_contact_call")]

label work_contact_call:
    $ renpy.free_memory()
    show screen work_contact_call_photo
    $ block_ui = True
    $ renpy.music.set_pause(True)
    $ start_dialog()
    pause 1.5
    play sound "long_phone_sound.mp3"
    pause 8.0
    stop sound
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    voice "audio/voices/operator/1.mp3"
    operator "Отдел кадров биологической компании 'BlueGen', слушаю."
    

label work_contact_call_menu:
    $ stop_dialog()
    menu:
        "Увольте меня" if i_ask_uvolnenie == False and i_know_quest_today == True:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/17.mp3"
            Vika "Я бы хотела уволиться."
            voice "audio/voices/operator/2.mp3"
            operator "Для этого вам надо в понедельник написать заявление на увольнение, в течении недели его рассмотрят и отдадут на подпись начальнику"
            voice "audio/voices/operator/3.mp3"
            operator "Далее надо дождаться пока начальник выйдет с отпуска и подпишет заявление, потом остается отработать только 2 недели и все, можете считать что вы уволены."
            voice "audio/voices/vika/18.mp3"
            Vika "Мне нужно уволится в течении нескольких дней!"
            voice "audio/voices/operator/4.mp3"
            operator "Как ваша фамилия?"
            voice "audio/voices/vika/19.mp3"
            Vika "Башкова"
            voice "audio/voices/operator/5.mp3"
            operator "Сейчас посмотрю..."
            voice "audio/voices/operator/6.mp3"
            operator "У вас ни одного опаздания, ни одного дисциплинарного взыскания и написано: 'Внешний вид всегда соответствует стандартам компании'."
            voice "audio/voices/operator/7.mp3"
            operator "Вас не за что увольнять в экстренном порядке. Вы можете поговорить с вашим начальником, это все что я могу вам подсказать."
            voice "audio/voices/vika/20.mp3"
            Vika "Ладно, спасибо"
            voice "audio/voices/operator/8.mp3"
            operator "Могу я еще чем-то помочь?"
            $ i_ask_uvolnenie = True
            jump work_contact_call_menu
        "До свидания":
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/21.mp3"
            Vika "До свидания!"
            voice "audio/voices/operator/9.mp3"
            operator "Рады были помочь"
            play sound "sbros.mp3"
    $ stop_dialog()
    $ block_ui = False
    hide screen work_contact_call_photo
    show screen work_contact
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen work_contact_call_photo:
    add "phone/work_contact_call.png" xpos 750 ypos 150

screen vitya_contact:
    modal True
    add "phone/vitya_contact.png" xpos 750 ypos 150
    imagebutton:
        idle "phone/back_to_contacts_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/back_to_contacts_button_hover.png"
            action [Hide("vitya_contact"), Show("phone")]
    imagebutton:
        idle "phone/call_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/call_button_hover.png"
            action [Hide("vitya_contact"), Jump("vitya_contact_call")]

label vitya_contact_call:
    $ renpy.free_memory()
    show screen vitya_contact_call_photo
    $ block_ui = True
    $ start_dialog()
    pause 1.5
    $ renpy.music.set_pause(True)
    if polojenie == "IT":
        play sound "sbros.mp3"
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/vika/22.mp3"
        Vika "У него не может быть занято, ему звонит жена!"
        pause 0.5
        $ block_ui = False
        hide screen vitya_contact_call_photo
        show screen vitya_contact
        $ renpy.music.set_pause(False)
        call screen wait_for_click
        return
    else:
        play sound "long_phone_sound.mp3"
        pause 8.0
        stop sound
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/vitya/10.mp3"
        vitya "Да?"
        jump vitya_contact_call_menu


label vitya_contact_call_menu:
    $ stop_dialog()
    menu:
        "Попросить помочь с питоном" if it_first_dialog == False and vitya_can_help == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/23.mp3"
            Vika "Мне нужна твоя помощь с этим вашим питоном."
            voice "audio/voices/vitya/62.mp3"
            vitya "Да ладно? И чем же я тебе помогу?"
            voice "audio/voices/vika/24.mp3"
            Vika "Мне нужно притвориться что я шарю за IT перед нашим сисадмином"
            voice "audio/voices/vika/25.mp3"
            Vika "Просто как на экзамене, через наушник в ухе будешь говорить мне что говорить"
            voice "audio/voices/vitya/63.mp3"
            vitya "У меня сейчас куча работы..."
            voice "audio/voices/vika/26.mp3"
            Vika "Да конечно! я знаю, что ты ничего не делаешь когда я ухожу на работу!"
            voice "audio/voices/vika/27.mp3"
            Vika "Ты мне сам говорил, что написал какую-то программу которая тыкает в мышку и печатает на клавиатуре, чтоб тебя не спалили"
            voice "audio/voices/vitya/64.mp3"
            vitya "Ну ладно, иди к своему сисадмину"
            voice "audio/voices/vika/28.mp3"
            Vika "Хорошо"
            $ stop_dialog()
            $ vitya_can_help = True
            $ block_ui = False
            hide screen vitya_contact_call_photo
            $ renpy.music.set_pause(False)
            call screen wait_for_click
            return
        "Мне прора идти":
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти!"
            voice "audio/voices/vitya/65.mp3"
            vitya "Давай"
            play sound "sbros.mp3"
            $ block_ui = False
            hide screen vitya_contact_call_photo
            show screen vitya_contact
            $ renpy.music.set_pause(False)
            $ stop_dialog()
            call screen wait_for_click
            return


screen vitya_contact_call_photo:
    add "phone/vitya_contact_call.png" xpos 750 ypos 150

screen ruslan_contact:
    modal True
    add "phone/ruslan_contact.png" xpos 750 ypos 150
    imagebutton:
        idle "phone/back_to_contacts_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/back_to_contacts_button_hover.png"
            action [Hide("ruslan_contact"), Show("phone")]
    imagebutton:
        idle "phone/call_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/call_button_hover.png"
            action [Hide("ruslan_contact"), Jump("ruslan_contact_call")]

label ruslan_contact_call:
    $ renpy.free_memory()
    show screen ruslan_contact_call_photo
    $ block_ui = True
    $ block_ui = False
    hide screen ruslan_call_photo
    show screen ruslan_contact
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen ruslan_contact_call_photo:
    add "phone/ruslan_contact_call.png" xpos 750 ypos 150

screen nachalnik_contact:
    modal True
    add "phone/nachalnik_contact.png" xpos 750 ypos 150
    imagebutton:
        idle "phone/back_to_contacts_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/back_to_contacts_button_hover.png"
            action [Hide("nachalnik_contact"), Show("phone")]
    imagebutton:
        idle "phone/call_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/call_button_hover.png"
            action [Hide("nachalnik_contact"), Jump("nachalnik_contact_call")]

label nachalnik_contact_call:
    $ renpy.free_memory()
    show screen nachalnik_contact_call_photo
    $ block_ui = True
    $ renpy.music.set_pause(True)
    $ start_dialog()
    pause 1.5
    play sound "long_phone_sound.mp3"
    pause 8.0
    stop sound
    if messange_from_nachalnik == False:
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/nachalnik/7.mp3"
        nachalnik "Башкова, ты нормальная? Не звони мне, я в отпуске"
    play sound "sbros.mp3"
    $ stop_dialog()
    $ block_ui = False
    hide screen nachalnik_contact_call_photo
    show screen nachalnik_contact
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen nachalnik_contact_call_photo:
    add "phone/nachalnik_contact_call.png" xpos 750 ypos 150

screen my_number_contact:
    modal True
    add "phone/my_number_contact.png" xpos 750 ypos 150
    imagebutton:
        idle "phone/back_to_contacts_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/back_to_contacts_button_hover.png"
            action [Hide("my_number_contact"), Show("phone")]
    imagebutton:
        idle "phone/call_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/call_button_hover.png"
            action [Hide("my_number_contact"), Jump("my_number_contact_call")]

label my_number_contact_call:
    $ renpy.free_memory()
    show screen my_number_contact_call_photo
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    pause 1.5
    play sound "short_phone_sound.mp3"
    pause 4.0
    stop sound
    $ clicks_enabled = False
    $ _preferences.afm_enable = True      # включаем автопромот
    $ _preferences.afm_time = 1.5
    voice "audio/voices/vika/29.mp3"
    Vika "Интересно, почему когда я звоню сама себе, постоянно занято?"
    $ block_ui = False
    $ stop_dialog()
    hide screen my_number_contact_call_photo
    show screen my_number_contact
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen my_number_contact_call_photo:
    add "phone/my_number_contact_call.png" xpos 750 ypos 150

screen maker_contact:
    modal True
    add "phone/maker_contact.png" xpos 750 ypos 150
    imagebutton:
        idle "phone/back_to_contacts_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/back_to_contacts_button_hover.png"
            action [Hide("maker_contact"), Show("phone")]
    imagebutton:
        idle "phone/call_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/call_button_hover.png"
            action [Hide("maker_contact"), Jump("maker_contact_call")]

label maker_contact_call:
    $ renpy.free_memory()
    show screen maker_contact_call_photo
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    pause 1.5
    play sound "long_phone_sound.mp3"
    pause 8.0
    stop sound
    if maker_first_call == True:
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/me/19.mp3"
        maker "Ало"
        voice "audio/voices/vika/30.mp3"
        Vika "Привет!"
        voice "audio/voices/me/20.mp3"
        maker "Привет, что хотела?"
        voice "audio/voices/me/21.mp3"
        maker "Погоди, дай угодаю, ты увидела у себя в телефоне контакт создателя и подумала что я создатель этой игры?"
        $ stop_dialog()
        menu:
            "Да":
                $ start_dialog()
                $ clicks_enabled = False
                $ _preferences.afm_enable = True      # включаем автопромот
                $ _preferences.afm_time = 1.5
                voice "audio/voices/me/22.mp3"
                maker "Ну да, я реально создатель игры"

            "Нет":
                $ start_dialog()
                $ clicks_enabled = False
                $ _preferences.afm_enable = True      # включаем автопромот
                $ _preferences.afm_time = 1.5
                voice "audio/voices/me/23.mp3"
                maker "Ну вообще-то, я реально создатель этой игры."
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/me/24.mp3"
        maker "Но ты же не думаешь что я буду помогать тебе?"
        voice "audio/voices/vika/31.mp3"
        Vika "Ну вообще-то было бы неплохо."
        voice "audio/voices/me/25.mp3"
        maker "Я делал эту игру месяцами не для того чтоб тебе помогать."
        voice "audio/voices/me/26.mp3"
        maker "Хотя подожди, я буду давать тебе подсказки"
        voice "audio/voices/me/27.mp3"
        maker "Но я как и любой разработчик хочу денег, поэтому за каждую подсказку я буду отнимать у тебя по 10р"
        voice "audio/voices/me/28.mp3"
        maker "Кроме того, твой интеллект будет снижаться каждый раз когда ты просишь у меня подсказку."
        voice "audio/voices/vika/32.mp3"
        Vika "Эмм... хорошо"
        voice "audio/voices/me/29.mp3"
        maker "Говори где ты застряла?"
        $ maker_first_call = False
        jump maker_menu
    else:
        $ clicks_enabled = False
        $ _preferences.afm_enable = True      # включаем автопромот
        $ _preferences.afm_time = 1.5
        voice "audio/voices/me/19.mp3"
        maker "Ало"
        jump maker_menu
    

label maker_menu:
    $ stop_dialog()
    menu:
        "Дай мне подсказку":
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/33.mp3"
            Vika "Можешь дать мне подсказку?"
            if slojnost_igry == "hard":
                voice "audio/voices/me/30.mp3"
                maker "Конечно могу, только сначала запусти игру заного, выбери легкий уровень сложности и перезвони."
                jump maker_menu
            elif money > 9:
                voice "audio/voices/me/31.mp3"
                maker "Могу"
                jump help
            else:
                voice "audio/voices/me/32.mp3"
                maker "Как только ты накопишь денег, сразу дам."
                jump maker_menu
        "Как у тебя дела?" if kak_dela_maker == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/34.mp3"
            Vika "Как у тебя дела?"
            voice "audio/voices/me/33.mp3"
            maker "Ты серьезно решила задать этот вопрос?"
            voice "audio/voices/me/34.mp3"
            maker "Ты же понимаешь, что я сейчас сижу перед ноутбуком и печатаю буквы в кавычках?"
            voice "audio/voices/me/35.mp3"
            maker "Я по сути сижу и общаюсь сам с собой, и ты хочешь чтоб я спросил сам у себя как дела???"
            voice "audio/voices/me/36.mp3"
            maker "Хорошо, я спрошу, как у тебя дела?"
            voice "audio/voices/me/37.mp3"
            maker "У меня? Все плохо, я общаюсь тут сам с собой и меня достает игрок бесполезным разговором."
            $ kak_dela_maker = True
            jump maker_menu
        "Зачем ты создал эту игру?" if why_are_you_make_game == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/35.mp3"
            Vika "Зачем ты создал эту игру?"
            voice "audio/voices/me/38.mp3"
            maker "Хороший вопрос, я сам не знаю"
            voice "audio/voices/me/39.mp3"
            maker "Возможно я хочу денег, ты кстати не спиратил эту игру? Если я узнаю что ты ее спиратил, то я сделаю все задачки в 100 раз сложнее"
            $ why_are_you_make_game = True
            jump maker_menu
        "Мне пора идти":
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/me/40.mp3"
            maker "Удачи"
            play sound "sbros.mp3"
            $ block_ui = False
            $ stop_dialog()
            hide screen maker_contact_call_photo
            show screen maker_contact
            $ renpy.music.set_pause(False)
            call screen wait_for_click
            return

label help:
    $ stop_dialog()
    menu:
        "Как мне попасть в эмерген?" if quest_list[37]["available"] == True and quest_list[37]["done"] == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/36.mp3"
            Vika "Как мне попасть в эмерген?"
            voice "audio/voices/me/41.mp3"
            maker "Подай резюме."
            voice "audio/voices/vika/37.mp3"
            Vika "Я серьезно, мне надо в их здание"
            voice "audio/voices/me/42.mp3"
            maker "А, ну у твоего босса есть пропуск, который он нашел, придумай как украсть его."
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как мне пройти тест сисадмина?" if quest_list[35]["available"] == True and quest_list[35]["done"] == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/38.mp3"
            Vika "Мне нужно проходить этот тест?"
            voice "audio/voices/me/43.mp3"
            maker "Да, у него отвертка которой ты лифт починишь, только сначала посмотри на кнопку, а то мне лень тригер разговора переделывать"
            voice "audio/voices/vika/39.mp3"
            Vika "И как же мне его пройти? Я в ваших питонах не шарю."
            voice "audio/voices/me/44.mp3"
            maker "А что ты меня то спрашиваешь, у тебя муж программист, у него и спрашивай"
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Какой напиток предпочитает босс" if quest_list[29]["available"] == True and quest_list[29]["done"] == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/40.mp3"
            Vika "Что за напиток пьёт мой босс?"
            voice "audio/voices/me/45.mp3"
            maker "Я то откуда знаю, это же твой босс, поспрашивай у коллег, может они вкурсе"
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Я не понимаю что мне делать в фотосалоне" if quest_list[25]["available"] == True and quest_list[25]["done"] == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/41.mp3"
            Vika "Я не понимаю как мне накраситься."
            voice "audio/voices/me/46.mp3"
            maker "У тебя на компьютере есть самоучитель по макияжу."
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как мне отмазаться от вечера" if quest_list[24]["available"] == True and quest_list[24]["done"] == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/42.mp3"
            Vika "Что мне сделать чтоб не спать с ментом?"
            voice "audio/voices/me/47.mp3"
            maker "Слушай, у тебя много новых знакомств, поищи среди них кого-нибудь, кто... ну незнаю..."
            voice "audio/voices/me/48.mp3"
            maker "Спит с людьми за деньги может быть..."
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Где тайник в школе?" if quest_list[22]["available"] == True and quest_list[22]["done"] == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/43.mp3"
            Vika "Где тайник в школе?"
            voice "audio/voices/me/49.mp3"
            maker "Тебе сначала нужно остаться одной в кабинете, найди способ выгнать её, и научись играть на пианино, пригодится"
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как поймать рыбу" if quest_list[19]["available"] == True and quest_list[19]["done"] == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/44.mp3"
            Vika "Не могу понять как ловить рыбу"
            voice "audio/voices/me/50.mp3"
            maker "Рыбак из тебя конечно никакой, попробуй поискать книжку какую-нибудь по рыбалке"
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Где мне взять пиво и рыбу?" if quest_list[18]["available"] == True and quest_list[18]["done"] == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/45.mp3"
            Vika "Что-то я не могу найти пиво и рыбу"
            voice "audio/voices/me/51.mp3"
            maker "Рыбу он тебе сам сказал где брать, так что езжай в рыбную лавку, а пиво..."
            voice "audio/voices/me/52.mp3"
            maker "Все самое лучшее пиво в баре конечно."
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Какой пароль от ящика?" if quest_list[8]["available"] == True and lock_is_locked == True and ask_pincode == False:
            $ start_dialog()
            $ clicks_enabled = False
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/46.mp3"
            Vika "Какой пароль от ящика?"
            voice "audio/voices/me/53.mp3"
            maker "Витя никогда не запоминает пароли, а замок шестизначный, по-любому это какая-то дата."
            $ intellect -= 1
            $ money -= 10
            $ ask_pincode = True
            jump maker_menu
        "Как мне найти деньги на переезд?" if quest_list[2]["available"] == True and quest_list[2]["done"] == False and ask_money == False:
            $ start_dialog()
            $ _preferences.afm_enable = True      # включаем автопромот
            $ _preferences.afm_time = 1.5
            voice "audio/voices/vika/47.mp3"
            Vika "Как мне найти деньги на переезд?"
            voice "audio/voices/me/54.mp3"
            maker "Тебе нужно 70к, зарабатывать ты их будешь долго поэтому тебе дорога в казино, а вот полагаться на удачу или на мозг это уже тебе решать."
            $ intellect -= 1
            $ money -= 10
            $ ask_money = True
            jump maker_menu
        "Как мне сготовить лазанью?" if quest_list[16]["available"] == True and quest_list[16]["done"] == False and ask_cook == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/48.mp3"
            Vika "Как мне сготовить лазанью?"
            voice "audio/voices/me/55.mp3"
            maker "Я мужик, а ты женщина, и ты спрашиваешь меня как готовить, я бы следовал рецепту и не отступал от него."
            $ ask_cook = True
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как мне уволиться с работы?" if quest_list[9]["available"] == True and quest_list[9]["done"] == False and ask_work == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/49.mp3"
            Vika "Как мне уволиться с работы?"
            voice "audio/voices/me/56.mp3"
            maker "Тебя на работе хвалят за твой внешний вид, испорти его как-нибудь."
            $ ask_work = True
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как мне попасть в витин ящик?" if quest_list[8]["available"] == True and quest_list[8]["done"] == False and ask_yaschik == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/50.mp3"
            Vika "Как мне попасть в витин ящик?"
            voice "audio/voices/me/57.mp3"
            maker "Просто выведи его из комнаты, заставь что-нибудь сделать"
            $ ask_yaschik = True
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Подскажи еще про продукты?" if quest_list[7]["available"] == True and quest_list[7]["done"] == False and ask_produkti == 2:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/51.mp3"
            Vika "Я все равно не могу купить продукты"
            voice "audio/voices/me/58.mp3"
            maker "А ты не жалеешь свой интеллект"
            voice "audio/voices/me/59.mp3"
            maker "Просто докинь все остальные продукты по рецепту красными, тебе хватит"
            $ ask_produkti = 3
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Все равно не могу купить продукты?" if quest_list[7]["available"] == True and quest_list[7]["done"] == False and ask_produkti == 1:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/51.mp3"
            Vika "Я все равно не могу купить продукты"
            voice "audio/voices/me/60.mp3"
            maker "После того как купила 3 синих, выбери еще 4 самых дорогих и купи их зелеными."
            $ ask_produkti = 2
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как мне купить продукты?" if quest_list[7]["available"] == True and quest_list[7]["done"] == False and ask_produkti == 0:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/52.mp3"
            Vika "Как мне купить продукты?"
            voice "audio/voices/me/61.mp3"
            maker "Берешь, да покупаешь, оплата картой, все просто. Если не знаешь что покупать, просто найди рецепт."
            if slojnost_igry == "easy":
                voice "audio/voices/vika/53.mp3"
                Vika "Но там только 2000р"
            else:
                voice "audio/voices/vika/54.mp3"
                Vika "Но там только 1825р"
            voice "audio/voices/me/62.mp3"
            maker "А это ты уже сама виновата, не надо было деньги на шмотки тратить"
            voice "audio/voices/vika/55.mp3"
            Vika "Вообще-то это ты написал это, так что чисто технически я не виновата."
            voice "audio/voices/me/63.mp3"
            maker "Справедливо. Ну ладно чтоб неплохо сэкономить купи три самых дорогих предмета синего цвета, и все, больше не трогай синий, а то скидка пойдет только на синие предметы"
            $ ask_produkti = 1
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Дай еще числа для судоку?" if quest_list[6]["available"] == True and quest_list[6]["done"] == False and ask_sudoku == 2:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/56.mp3"
            Vika "Подскажи еще несколько чисел"
            voice "audio/voices/me/64.mp3"
            maker "Тебе вообще не жалко свой интеллект, да? Ну ладно, вторая состоит из чисел: 5,6,8, 7,3,1, 2,4,9 Больше не подскажу."
            $ ask_sudoku = 3
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Все равно не получается решить судоку" if quest_list[6]["available"] == True and quest_list[6]["done"] == False and ask_sudoku == 1:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/57.mp3"
            Vika "Ты обещал подсказать несколько чисел"
            voice "audio/voices/me/65.mp3"
            maker "А у тебя хорошо получается тратить деньги и интеллект Ладно, пятая или же центральная строка состоит из чисел: 3,4,5, 8,2,6, 9,7,1"
            $ ask_sudoku = 2
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как мне решить судоку?" if quest_list[6]["available"] == True and quest_list[6]["done"] == False and ask_sudoku == 0:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/58.mp3"
            Vika "Я не могу решить судоку!"
            voice "audio/voices/me/66.mp3"
            maker "Прочитай книгу о том как решать судоку, если будет совсем туго, звони, я подскажу несколько чисел"
            $ ask_sudoku = 1
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как мне починить розетку?" if quest_list[5]["available"] == True and quest_list[5]["done"] == False and ask_rozetka == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/59.mp3"
            Vika "Подскажи как мне починить розетку."
            voice "audio/voices/me/67.mp3"
            maker "Оооо, с этим лучше не к вите, найди лучше мастера, будет намного быстрее"
            $ ask_rozetka = True
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как мне убрать банер?" if quest_list[4]["available"] == True and quest_list[4]["done"] == False and ask_buner == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/60.mp3"
            Vika "Подскажи как мне убрать банер."
            voice "audio/voices/me/68.mp3"
            maker "У тебя же мужик программист, попроси его, он за 2 секунды уберет"
            $ ask_buner = True
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как разблокировать компьютер?" if quest_list[1]["available"] == True and quest_list[1]["done"] == False and vitya_password == True and ask_pc2 == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/61.mp3"
            Vika "Подскажи как разблокировать компьютер."
            voice "audio/voices/me/69.mp3"
            maker "Учись разгадывать ребусы, погу подсказать только, что каждая запятая это минус буква в слове, и то что дом перевернут тоже важно."
            $ ask_pc2 = True
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Как разблокировать компьютер?" if quest_list[1]["available"] == True and quest_list[1]["done"] == False and vitya_password == False and ask_pc1 == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/61.mp3"
            Vika "Подскажи как разблокировать компьютер."
            voice "audio/voices/me/70.mp3"
            maker "Просто поговори со своим мужиком, это он что-то там навертел, он скажет тебе что делать."
            $ ask_pc1 = True
            $ intellect -= 1
            $ money -= 10
            jump maker_menu
        "Я передумала":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/478.mp3"
            Vika "Я передумала"
            jump maker_menu

screen maker_contact_call_photo:
    add "phone/maker_contact_call.png" xpos 750 ypos 150

screen dyadya_sasha_contact:
    modal True
    add "phone/dyadya_shasha_contact.png" xpos 750 ypos 150
    imagebutton:
        idle "phone/back_to_contacts_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/back_to_contacts_button_hover.png"
            action [Hide("dyadya_sasha_contact"), Show("phone")]
    imagebutton:
        idle "phone/call_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/call_button_hover.png"
            action [Hide("dyadya_sasha_contact"), Jump("dyadya_sasha_contact_call")]

label dyadya_sasha_contact_call:
    $ renpy.free_memory()
    show screen dyadya_sasha_contact_call_photo
    $ block_ui = True
    pause 1.5
    play sound "long_phone_sound.mp3"
    pause 8.0
    stop sound
    play sound "sbros.mp3"
    $ block_ui = False
    hide screen dyadya_sasha_contact_call_photo
    show screen dyadya_sasha_contact
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen dyadya_sasha_contact_call_photo:
    add "phone/dyadya_shasha_contact_call.png" xpos 750 ypos 150

screen alisa_contact:
    modal True
    add "phone/alisa_contact.png" xpos 750 ypos 150
    imagebutton:
        idle "phone/back_to_contacts_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/back_to_contacts_button_hover.png"
            action [Hide("alisa_contact"), Show("phone")]
    imagebutton:
        idle "phone/call_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/call_button_hover.png"
            action [Hide("alisa_contact"), Jump("alisa_contact_call")]

label alisa_contact_call:
    $ renpy.free_memory()
    show screen alisa_contact_call_photo
    $ block_ui = True
    $ block_ui = False
    hide screen alisa_contact_call_photo
    show screen alisa_contact
    call screen wait_for_click

    return

screen alisa_contact_call_photo:
    add "phone/alisa_contact_call.png" xpos 750 ypos 150

screen chingis_contact:
    modal True
    add "phone/chingis_contact.png" xpos 750 ypos 150
    imagebutton:
        idle "phone/back_to_contacts_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/back_to_contacts_button_hover.png"
            action [Hide("chingis_contact"), Show("phone")]
    imagebutton:
        idle "phone/call_button.png"
        xpos 750 ypos 150
        focus_mask True
        if not block_ui:
            hover "phone/call_button_hover.png"
            action [Hide("chingis_contact"), Jump("chingis_contact_call")]

label chingis_contact_call:
    $ renpy.free_memory()
    show screen chingis_contact_call_photo
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    pause 1.5
    play sound "long_phone_sound.mp3"
    pause 8.0
    stop sound
    $ _preferences.afm_enable = True 
    voice "audio/voices/chingis/1.mp3"
    chingis "Ало?"
    voice "audio/voices/vika/62.mp3"
    Vika "Привет Чингыс"
    voice "audio/voices/chingis/2.mp3"
    chingis "Приуэйт Викэ"

label chingis_contact_call_menu:
    $ stop_dialog()
    menu:
        "Можешь помочь с машиной?" if (polojenie == "casino_hall" or polojenie == "casino") and car_is_broken == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/63.mp3"
            Vika "Можешь помочь с машиной?"
            voice "audio/voices/chingis/3.mp3"
            chingis "Канэшна"
            voice "audio/voices/vika/64.mp3"
            Vika "Она стоит возле казино закрытая, а ключи внутри!"
            voice "audio/voices/chingis/4.mp3"
            chingis "Две минуты, турецкий"
            $ intellect += 1
            $ game_hour += 1
            $ update_game_time()
            $ car_is_broken = True
            play sound "sbros.mp3"
        "Пока":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/342.mp3"
            Vika "Пока"
            voice "audio/voices/chingis/5.mp3"
            chingis "Пока Викэ"
            play sound "sbros.mp3"
    $ block_ui = False
    $ stop_dialog()
    hide screen chingis_contact_call_photo
    show screen chingis_contact
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen chingis_contact_call_photo:
    add "phone/chingis_contact_call.png" xpos 750 ypos 150

screen appstore:
    modal True
    add "appstore.png" xpos 750 ypos 150
    if i_know_sudoku == True and sudoku_download == False:
        imagebutton:
            idle "sudoku_download.png"        
            xpos 750 
            ypos 150
            focus_mask True
            if not block_ui:
                hover "sudoku_download_hover.png"
                action SetVariable("sudoku_download", True)
    if sudoku_download == True:
        imagebutton:
            idle "sudoku_open.png"        
            xpos 750 
            ypos 150
            focus_mask True
            if not block_ui:
                hover "sudoku_open_hover.png"
                action [Hide("appstore"), Show("sudoku_game")]   
    imagebutton:
        idle "back_to_big_phone_idle.png"        
        xpos 750
        ypos 150
        focus_mask True
        if not block_ui:
            hover "back_to_big_phone_hover.png"
            action [Show("big_iphone"), Hide("appstore")]
screen wildberies:
    modal True
    add "wildberies.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "back_to_big_phone_idle.png"
            hover "back_to_big_phone_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action Hide("wildberies")

screen ozon:
    modal True
    add "ozon.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "back_to_big_phone_idle.png"
            hover "back_to_big_phone_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action Hide("ozon")
    
screen messenger:
    modal True
    if messange_from_ment == True:
        add "messedger_with_ment.png" xpos 750 ypos 150
    else:
        add "messedger.png" xpos 750 ypos 150
    imagebutton:
        idle "back_to_big_phone_idle.png"
        xpos 750
        ypos 150
        focus_mask True
        if not block_ui:
            hover "back_to_big_phone_hover.png"
            action [Hide("messenger"), Show("big_iphone")]     

screen tinkoff:
    modal True
    add "tinkoff.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "back_to_big_phone_idle.png"
            hover "back_to_big_phone_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action Hide("tinkoff")

screen iphone_perishko:
    add "big_iphone.png" xpos 750 ypos 150

screen zametki():
    modal True
    add "zametki.png" xpos 750 ypos 150
    imagebutton:
        idle "back_to_big_phone_idle.png"
        xpos 750
        ypos 150
        focus_mask True
        if not block_ui:
            hover "back_to_big_phone_hover.png"
            action [Show("big_iphone"), Hide("zametki")]

    frame:
        xpos 770
        ypos 290
        xsize 364
        ysize 580
        background None

        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:
                spacing 10

                for i, quest in enumerate(quest_list):
                    if quest["available"]:
                        hbox:
                            spacing 10

                            if quest["done"]:
                                imagebutton:
                                    idle ("phone/checkbox_on.png" if quest["checked"] else "phone/checkbox_off.png")
                                    if not block_ui:
                                        action If(not quest["checked"], SetDict(quest_list[i], "checked", True))
                            else:
                                imagebutton:
                                    idle "phone/checkbox_off.png"
                                    if not block_ui:
                                        action Jump("ne_sdelano")

                            text quest["text"] size 20 color "#ffffff"

screen zametki2():
    add "zametki.png" xpos 750 ypos 150
    imagebutton:
        idle "back_to_big_phone_idle.png"
        xpos 750
        ypos 150
        focus_mask True
        if not block_ui:
            hover "back_to_big_phone_hover.png"
            action [Show("big_iphone"), Hide("zametki")]

    frame:
        xpos 770
        ypos 290
        xsize 364
        ysize 580
        background None

        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:
                spacing 10

                for i, quest in enumerate(quest_list):
                    if quest["available"]:
                        hbox:
                            spacing 10

                            if quest["done"]:
                                imagebutton:
                                    idle ("phone/checkbox_on.png" if quest["checked"] else "phone/checkbox_off.png")
                                    if not block_ui:
                                        action If(not quest["checked"], SetDict(quest_list[i], "checked", True))
                            else:
                                imagebutton:
                                    idle "phone/checkbox_off.png"
                                    if not block_ui:
                                        action Jump("ne_sdelano")

                            text quest["text"] size 20 color "#ffffff"

label ne_sdelano:
    hide screen zametki
    show screen zametki2
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/65.mp3"
    Vika "Это я еще не сделала!!!"
    $ block_ui = False
    $ stop_dialog()
    hide screen zametki2
    show screen zametki
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label perishko:
    $ renpy.free_memory()
    show screen iphone_perishko
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/66.mp3"
    Vika "Сюда мне сейчас точно не надо!!!"
    $ block_ui = False
    $ stop_dialog()
    hide screen iphone_perishko
    show screen big_iphone
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return


label taxi:
    $ renpy.free_memory()
    show screen iphone_perishko
    $ block_ui = True
    $ start_dialog()
    voice "audio/voices/vika/67.mp3"
    $ renpy.music.set_pause(True)
    $ _preferences.afm_enable = True 
    Vika "О нет, я лучше пешком пойду, чем вызову поисковик такси."
    $ block_ui = False
    $ stop_dialog()
    hide screen iphone_perishko
    show screen big_iphone
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return


screen photo:
    modal True
    add "photo.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "back_to_big_phone_idle.png"
            hover "back_to_big_phone_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo"), Show("big_iphone")]
        imagebutton:
            idle "photo_1_idle.png"
            hover "photo_1_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo"), Jump("photo_1_fraza")]
        imagebutton:
            idle "photo_2_idle.png"
            hover "photo_2_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo"), Jump("photo_2_fraza")]
        imagebutton:
            idle "photo_3_idle.png"
            hover "photo_3_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_3"), Jump("photo_3_fraza")]
        imagebutton:
            idle "photo_4_idle.png"
            hover "photo_4_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_4"), Jump("photo_4_fraza")]
        imagebutton:
            idle "photo_5_idle.png"
            hover "photo_5_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_5"), Jump("photo_5_fraza")]
        imagebutton:
            idle "photo_6_idle.png"
            hover "photo_6_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_6"), Jump("photo_6_fraza")]
        imagebutton:
            idle "photo_7_idle.png"
            hover "photo_7_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_7"), Jump("photo_7_fraza")]
        imagebutton:
            idle "photo_8_idle.png"
            hover "photo_8_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_8"), Jump("photo_8_fraza")]
        imagebutton:
            idle "photo_9_idle.png"
            hover "photo_9_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_9"), Jump("photo_9_fraza")]
        imagebutton:
            idle "photo_10_idle.png"
            hover "photo_10_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_10"), Jump("photo_10_fraza")]
        imagebutton:
            idle "photo_11_idle.png"
            hover "photo_11_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_11"), Jump("photo_11_fraza")]
        imagebutton:
            idle "photo_12_idle.png"
            hover "photo_12_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_12"), Jump("photo_12_fraza")]
        imagebutton:
            idle "photo_13_idle.png"
            hover "photo_13_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_13"), Jump("photo_13_fraza")]
        imagebutton:
            idle "photo_14_idle.png"
            hover "photo_14_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_14"), Jump("photo_14_fraza")]
        imagebutton:
            idle "photo_15_idle.png"
            hover "photo_15_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_15"), Jump("photo_15_fraza")]
        imagebutton:
            idle "photo_16_idle.png"
            hover "photo_16_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_16"), Jump("photo_16_fraza")]
        imagebutton:
            idle "photo_17_idle.png"
            hover "photo_17_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_17"), Jump("photo_17_fraza")]
        imagebutton:
            idle "photo_18_idle.png"
            hover "photo_18_hover.png"
            xpos 750
            ypos 150
            focus_mask True
            action [Hide("photo_18"), Jump("photo_18_fraza")]

screen photo_1:
    modal True
    add "photo_1.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1088
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_1"), Show("photo")]

screen photo_1_1:
    add "photo_1.png" xpos 750 ypos 150

label photo_1_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_1_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_1_1
    show screen big_iphone
    show screen photo_1
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_2:
    modal True
    add "photo_2.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1088
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_2"), Show("photo")]        

screen photo_2_1:
    add "photo_2.png" xpos 750 ypos 150

label photo_2_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen photo_2
    hide screen big_iphone
    show screen photo_2_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_2_1
    show screen big_iphone
    show screen photo_2
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen photo_3:
    modal True
    add "photo_3.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1088
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_3"), Show("photo")]

screen photo_3_1:
    add "photo_3.png" xpos 750 ypos 150

label photo_3_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_3_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_3_1
    show screen big_iphone
    show screen photo_3
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_4:
    modal True
    add "photo_4.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1088
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_4"), Show("photo")]        

screen photo_4_1:
    add "photo_4.png" xpos 750 ypos 150

label photo_4_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_4_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_4_1
    show screen big_iphone
    show screen photo_4
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_5:
    modal True
    add "photo_5.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_5"), Show("photo")]

screen photo_5_1:
    add "photo_5.png" xpos 750 ypos 150

label photo_5_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_5_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_5_1
    show screen big_iphone
    show screen photo_5
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_6:
    modal True
    add "photo_6.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_6"), Show("photo")]    

screen photo_6_1:
    add "photo_6.png" xpos 750 ypos 150

label photo_6_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_6_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_6_1
    show screen big_iphone
    show screen photo_6
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_7:
    modal True
    add "photo_7.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1088
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_7"), Show("photo")]

screen photo_7_1:
    add "photo_7.png" xpos 750 ypos 150

label photo_7_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_7_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_7_1
    show screen big_iphone
    show screen photo_7
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_8:
    modal True
    add "photo_8.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_8"), Show("photo")]    

screen photo_8_1:
    add "photo_8.png" xpos 750 ypos 150

label photo_8_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_8_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_8_1
    show screen big_iphone
    show screen photo_8
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_9:
    modal True
    add "photo_9.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1088
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_9"), Show("photo")]

screen photo_9_1:
    add "photo_9.png" xpos 750 ypos 150

label photo_9_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_9_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_9_1
    show screen big_iphone
    show screen photo_9
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_10:
    modal True
    add "photo_10.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1088
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_10"), Show("photo")]

screen photo_10_1:
    add "photo_10.png" xpos 750 ypos 150

label photo_10_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_10_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_10_1
    show screen big_iphone
    show screen photo_10
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_11:
    modal True
    add "photo_11.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_11"), Show("photo")]

screen photo_11_1:
    add "photo_11.png" xpos 750 ypos 150

label photo_11_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_11_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_11_1
    show screen big_iphone
    show screen photo_11
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_12:
    modal True
    add "photo_12.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1088
            ypos 380
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_12"), Show("photo")]

screen photo_12_1:
    add "photo_12.png" xpos 750 ypos 150

label photo_12_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_12_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_12_1
    show screen big_iphone
    show screen photo_12
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_13:
    modal True
    add "photo_13.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_13"), Show("photo")]

screen photo_13_1:
    add "photo_13.png" xpos 750 ypos 150

label photo_13_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_13_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_13_1
    show screen big_iphone
    show screen photo_13
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_14:
    modal True
    add "photo_14.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_14"), Show("photo")]

screen photo_14_1:
    add "photo_14.png" xpos 750 ypos 150

label photo_14_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_14_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_14_1
    show screen big_iphone
    show screen photo_14
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_15:
    modal True
    add "photo_15.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_15"), Show("photo")]

screen photo_15_1:
    add "photo_15.png" xpos 750 ypos 150

label photo_15_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_15_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_15_1
    show screen big_iphone
    show screen photo_15
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_16:
    modal True
    add "photo_16.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_16"), Show("photo")]

screen photo_16_1:
    add "photo_16.png" xpos 750 ypos 150

label photo_16_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_16_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_16_1
    show screen big_iphone
    show screen photo_16
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_17:
    modal True
    add "photo_17.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_17"), Show("photo")]

screen photo_17_1:
    add "photo_17.png" xpos 750 ypos 150

label photo_17_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_17_1
    $ block_ui = True
    $ block_ui = False
    hide screen photo_17_1
    show screen big_iphone
    show screen photo_17
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen photo_18:
    modal True
    add "photo_18.png" xpos 750 ypos 150
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1048
            ypos 340
            focus_mask True
            at Transform(zoom=0.3)
            action [Hide("photo_18"), Show("photo")]


screen photo_18_1:
    add "photo_18.png" xpos 750 ypos 150

label photo_18_fraza:
    $ renpy.free_memory()
    hide screen photo
    hide screen big_iphone
    show screen photo_18_1
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/68.mp3"
    Vika "Это же наша свадьба!!! Самый лучший день в моей жизни! И в Витиной тоже!"
    $ block_ui = False
    $ stop_dialog()
    hide screen photo_18_1
    show screen big_iphone
    show screen photo_18
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen inventory():
    zorder 90
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        background "#222c"
        padding (20, 20)
        vbox:
            spacing 10
            text "Инвентарь" size 30 xalign 0.5

            grid 5 5 spacing 10:
                for i in range(25):
                    button:
                        background "#4448"
                        xsize 80
                        ysize 80
                        action NullAction()

                        # Показать картинку или текст в зависимости от предмета
                        if inventory_items[i] == "penguin":
                            add "penguin.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "penguin")]
                        elif inventory_items[i] == "tool":
                            add "icon/tool.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "tool")]
                        elif inventory_items[i] == "kosmetik":
                            add "icon/kosmetik.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "kosmetik")]
                        elif inventory_items[i] == "pasport":
                            add "icon/pasport.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "pasport")]
                        elif inventory_items[i] == "phone":
                            add "icon/phone.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "phone")]
                        elif inventory_items[i] == "project":
                            add "icon/project.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "project")]
                        elif inventory_items[i] == "propusk":
                            add "icon/propusk.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "propusk")]
                        elif inventory_items[i] == "keys_2_lab":
                            add "icon/keys_2_lab.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "keys_2_lab")]
                        elif inventory_items[i] == "napitok":
                            add "icon/napitok.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "napitok")]
                        elif inventory_items[i] == "sugars":
                            add "icon/sugars.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "sugars")]
                        elif inventory_items[i] == "viskey":
                            add "icon/viskey.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "viskey")]
                        elif inventory_items[i] == "izolenta":
                            add "icon/izolenta.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "izolenta")]
                        elif inventory_items[i] == "german_beer":
                            add "icon/german_beer.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "german_beer")]
                        elif inventory_items[i] == "keys":
                            add "icon/keys.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "keys")]
                        elif inventory_items[i] == "rebus":
                            if slojnost_igry == "easy":
                                add "rebus_easy_icon.png" size (80, 80)
                            else:
                                add "rebus_icon.png" size (80, 80)
                            action [Show("rebus_inventory"), Hide("inventory")]
                        elif inventory_items[i] == "blackmail":
                            add "icon/blackmail.png" size (80, 80)
                            action [Show("blackmail_inventory"), Hide("inventory"), Jump("o_net")]
                        elif inventory_items[i] == "krasnoperka":
                            add "icon/krasnoperka.png" size (80, 80)
                        elif inventory_items[i] == "najivka":
                            add "icon/najivka.png" size (80, 80)
                            action [Show("najivka"), Hide("inventory")]
                        elif inventory_items[i] == "casino_book":
                            add "icon/casino_book.png" size (80, 80)
                            action [Show("casino_book"), Hide("inventory")]
                        elif inventory_items[i] == "piano_book":
                            add "icon/piano_book.png" size (80, 80)
                            action [Show("piano_book"), Hide("inventory")]
                        elif inventory_items[i] == "glass":
                            add "icon/glass.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "glass")]
                            elif default_mouse == "beer":
                                action [
                                SetDict(inventory_items, i, "glass_of_beer"),
                                Function(set_inventory_without_items, ["glass", "beer"], "glass_of_beer"),
                                SetVariable("default_mouse", "default")
                            ]
                        elif inventory_items[i] == "glass_of_beer":
                            add "icon/glass_of_beer.png" size (80, 80)
                        elif inventory_items[i] == "card":
                            add "icon/card.png" size (80, 80)
                        elif inventory_items[i] == "lazania":
                            add "icon/lazania.png" size (80, 80)
                        elif inventory_items[i] == "listok":
                            add "icon/listok.png" size (80, 80)
                        elif inventory_items[i] == "dice":
                            add "icon/dice.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "dice")]
                        elif inventory_items[i] == "podshipnik":
                            add "icon/podshipnik.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "podshipnik")]
                            elif default_mouse == "humer":
                                action [
                                    SetDict(inventory_items, i, "ball_metall"),
                                    Function(set_inventory_without_items, ["podshipnik", "humer"], "ball_metall"),
                                    SetVariable("default_mouse", "default")
                                ]
                        elif inventory_items[i] == "ball_metall":
                            add "icon/ball_metall.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "ball_metall")]
                            elif default_mouse == "white_colour":
                                action [
                                    SetDict(inventory_items, i, "ball_white"),
                                    Function(set_inventory_without_items, ["ball_metall", "white_colour"], "ball_white"), 
                                    SetVariable("default_mouse", "default")
                                ]
                        elif inventory_items[i] == "ball_white":
                            add "icon/ball_white.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "ball_white")]
                        elif inventory_items[i] == "magnet_with_clay":
                            add "icon/magnet_with_clay.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "magnet_with_clay")]
                        elif inventory_items[i] == "dice_with_o":
                            add "icon/dice_with_o.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "dice_with_o")]
                            elif default_mouse == "gvozd":
                                action [
                                    SetDict(inventory_items, i, "dice_with_gvozd"),
                                    Function(set_inventory_without_items, ["dice_with_o", "gvozd"], "dice_with_gvozd"),
                                    SetVariable("default_mouse", "default")
                                ]
                        elif inventory_items[i] == "white_colour":
                            add "icon/white_colour.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "white_colour")]
                        elif inventory_items[i] == "dice_with_gvozd_colour":
                            add "icon/dice.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "dice_with_gvozd_colour")]
                        elif inventory_items[i] == "black_colour":
                            add "icon/black_colour.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "black_colour")]
                        elif inventory_items[i] == "blue_colour":
                            add "icon/blue_colour.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "blue_colour")]
                        elif inventory_items[i] == "green_colour":
                            add "icon/green_colour.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "green_colour")]
                        elif inventory_items[i] == "dice_with_gvozd":
                            add "icon/dice_with_gvozd.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "dice_with_gvozd")]
                            elif default_mouse == "black_colour":
                                action [
                                    SetDict(inventory_items, i, "dice_with_gvozd_colour"),
                                    Function(set_inventory_without_items, ["dice_with_gvozd", "black_colour"], "dice_with_gvozd_colour"),
                                    SetVariable("default_mouse", "default")
                                ]
                        elif inventory_items[i] == "produkti":
                            add "icon/produkti.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "produkti")]
                        elif inventory_items[i] == "magnet":
                            add "icon/magnet.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "magnet")]
                            elif default_mouse == "superkley":
                                action [
                                    SetDict(inventory_items, i, "magnet_with_clay"),
                                    Function(set_inventory_without_items, ["magnet", "superkley"], "magnet_with_clay"),
                                    SetVariable("default_mouse", "default")
                                ]
                        elif inventory_items[i] == "brush":
                            add "icon/brush.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "brush")]
                        elif inventory_items[i] == "beer":
                            add "icon/beer.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "beer")]
                        elif inventory_items[i] == "humer":
                            add "icon/humer.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "humer")]
                        elif inventory_items[i] == "superkley":
                            add "icon/superkley.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "superkley")]
                        elif inventory_items[i] == "gvozd":
                            add "icon/gvozd.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "gvozd")]
                        elif inventory_items[i] == "udochka":
                            add "icon/udochka.png" size (80, 80)
                            if default_mouse == "default":
                                action [SetDict(inventory_items, i, None), SetVariable("default_mouse", "udochka")]
                        elif inventory_items[i] == None:
                            if default_mouse == "penguin":
                                action [ 
                                SetDict(inventory_items, i, "penguin"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "tool":
                                action [ 
                                SetDict(inventory_items, i, "tool"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "kosmetik":
                                action [ 
                                SetDict(inventory_items, i, "kosmetik"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "pasport":
                                action [ 
                                SetDict(inventory_items, i, "pasport"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "phone":
                                action [ 
                                SetDict(inventory_items, i, "phone"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "project":
                                action [ 
                                SetDict(inventory_items, i, "project"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "propusk":
                                action [ 
                                SetDict(inventory_items, i, "propusk"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "keys_2_lab":
                                action [ 
                                SetDict(inventory_items, i, "keys_2_lab"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "napitok":
                                action [ 
                                SetDict(inventory_items, i, "napitok"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "sugars":
                                action [ 
                                SetDict(inventory_items, i, "sugars"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "viskey":
                                action [ 
                                SetDict(inventory_items, i, "viskey"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "izolenta":
                                action [ 
                                SetDict(inventory_items, i, "izolenta"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "german_beer":
                                action [ 
                                SetDict(inventory_items, i, "german_beer"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "keys":
                                action [ 
                                SetDict(inventory_items, i, "keys"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "glass":
                                action [ 
                                SetDict(inventory_items, i, "glass"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            if default_mouse == "podshipnik":
                                action [ 
                                SetDict(inventory_items, i, "podshipnik"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "ball_metall":
                                action [ 
                                SetDict(inventory_items, i, "ball_metall"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "ball_white":
                                action [ 
                                SetDict(inventory_items, i, "ball_white"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "magnet_with_clay":
                                action [ 
                                SetDict(inventory_items, i, "magnet_with_clay"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "dice":
                                action [ 
                                SetDict(inventory_items, i, "dice"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "dice_with_gvozd_colour":
                                action [ 
                                SetDict(inventory_items, i, "dice_with_gvozd_colour"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "white_colour":
                                action [ 
                                SetDict(inventory_items, i, "white_colour"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "black_colour":
                                action [ 
                                SetDict(inventory_items, i, "black_colour"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "blue_colour":
                                action [ 
                                SetDict(inventory_items, i, "blue_colour"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "green_colour":
                                action [ 
                                SetDict(inventory_items, i, "green_colour"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "dice_with_o":
                                action [ 
                                SetDict(inventory_items, i, "dice_with_o"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "dice_with_gvozd":
                                action [ 
                                SetDict(inventory_items, i, "dice_with_gvozd"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "magnet":
                                action [ 
                                SetDict(inventory_items, i, "magnet"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "brush":
                                action [ 
                                SetDict(inventory_items, i, "brush"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "beer":
                                action [ 
                                SetDict(inventory_items, i, "beer"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "humer":
                                action [ 
                                SetDict(inventory_items, i, "humer"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "superkley":
                                action [ 
                                SetDict(inventory_items, i, "superkley"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "gvozd":
                                action [ 
                                SetDict(inventory_items, i, "gvozd"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "produkti":
                                action [ 
                                SetDict(inventory_items, i, "produkti"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                            elif default_mouse == "udochka":
                                action [ 
                                SetDict(inventory_items, i, "udochka"),
                                SetVariable("default_mouse", "default")
                            
                            ]
                        elif default_mouse == "rebus":
                            add "empty_slot.png" size (80, 80)
                            action [ 
                                SetDict(inventory_items, i, "rebus"),
                                SetVariable("default_mouse", "default")
                            ]
                        else:
                            add "empty_slot.png" size (80, 80)
                            action NullAction()
screen wait_for_click():
    pass

init python:
    def set_inventory_without_items(items_to_remove, exclude=None):
        global inventory_items
        inventory_items = [
            item for item in inventory_items
            if (item not in items_to_remove) or (exclude is not None and item == exclude)
        ]

screen casino_book:
    add "casino_book.png"
    if not block_ui:
        imagebutton:
            idle "krest_book.png"
            focus_mask True
            action Hide("casino_book")

screen blackmail_inventory:
    add "blackmail_inventory.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:    
            action Hide("blackmail_inventory")

label o_net:
    if was_screem == False:
        $ block_ui = True
        $ start_dialog()
        $ _preferences.afm_enable = True 
        $ renpy.music.set_pause(True)
        voice "audio/voices/vika/69.mp3"
        Vika "О нет, кто-то был у нас ночью и украл мой паспорт!!!"
        $ quest_list[40]["available"] = True
        $ i_know_blackmail = True
        $ block_ui = False
        $ stop_dialog()
        $ was_screem = True
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen piano_book:
    add "piano_book.png"
    if not block_ui:
        imagebutton:
            idle "krest_book.png"
            focus_mask True
            action Hide("piano_book")

screen najivka:
    modal True
    add "ribalka/najivka_box.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("najivka")
    imagebutton:
            if selected_najivka == "chervi":
                idle "ribalka/chervi_hover.png"  
            else:
                idle "ribalka/chervi.png"
            focus_mask True
            if not block_ui:
                hover "ribalka/chervi_hover.png"
                action If(
                    selected_najivka == "chervi",
                    SetVariable("selected_najivka", None),
                    SetVariable("selected_najivka", "chervi")
                )
    imagebutton:
            if selected_najivka == "hleb":
                idle "ribalka/hleb_hover.png"  
            else:
                idle "ribalka/hleb.png"
            focus_mask True
            if not block_ui:
                hover "ribalka/hleb_hover.png"
                action If(
                    selected_najivka == "hleb",
                    SetVariable("selected_najivka", None),
                    SetVariable("selected_najivka", "hleb")
                )    
    imagebutton:
            if selected_najivka == "kukuruza":
                idle "ribalka/kukuruza_hover.png"  
            else:
                idle "ribalka/kukuruza.png"
            focus_mask True
            if not block_ui:
                hover "ribalka/kukuruza_hover.png"
                action If(
                    selected_najivka == "kukuruza",
                    SetVariable("selected_najivka", None),
                    SetVariable("selected_najivka", "kukuruza")
                )
    imagebutton:
            if selected_najivka == "Motil":
                idle "ribalka/Motil_hover.png"  
            else:
                idle "ribalka/Motil.png"
            focus_mask True
            if not block_ui:
                hover "ribalka/Motil_hover.png"
                action If(
                    selected_najivka == "Motil",
                    SetVariable("selected_najivka", None),
                    SetVariable("selected_najivka", "Motil")
                )
    imagebutton:
            if selected_najivka == "muha":
                idle "ribalka/muha_hover.png"  
            else:
                idle "ribalka/muha.png"
            focus_mask True
            if not block_ui:
                hover "ribalka/muha_hover.png"
                action If(
                    selected_najivka == "muha",
                    SetVariable("selected_najivka", None),
                    SetVariable("selected_najivka", "muha")
                )
    imagebutton:
            if selected_najivka == "oparish":
                idle "ribalka/oparish_hover.png"  
            else:
                idle "ribalka/oparish.png"
            focus_mask True
            if not block_ui:
                hover "ribalka/oparish_hover.png"
                action If(
                    selected_najivka == "oparish",
                    SetVariable("selected_najivka", None),
                    SetVariable("selected_najivka", "oparish")
                )
    imagebutton:
            if selected_najivka == "perlovka":
                idle "ribalka/perlovka_hover.png"  
            else:
                idle "ribalka/perlovka.png"
            focus_mask True
            if not block_ui:
                hover "ribalka/perlovka_hover.png"
                action If(
                    selected_najivka == "perlovka",
                    SetVariable("selected_najivka", None),
                    SetVariable("selected_najivka", "perlovka")
                )
    imagebutton:
            if selected_najivka == "testo":
                idle "ribalka/testo_hover.png"  
            else:
                idle "ribalka/testo.png"
            focus_mask True
            if not block_ui:
                hover "ribalka/testo_hover.png"
                action If(
                    selected_najivka == "testo",
                    SetVariable("selected_najivka", None),
                    SetVariable("selected_najivka", "testo")
                )      

screen tv_in_mainroom:
    if not block_ui:
        imagebutton:
            idle "tv_mainroom_idle.png"
            hover "tv_mainroom_hover.png"
            xpos 1048
            ypos 260
            focus_mask True
            if game_hour == 22:
                action Jump("ne_mogu_tolate")
            else:
                action Show("tv_menu_mainroom")  # Показываем меню выбора

screen tv_in_mainroom_night:
    if not block_ui:
        imagebutton:
            idle "tv_mainroom_night_idle.png"
            hover "tv_mainroom_night_hover.png"
            focus_mask True
            if game_hour == 22:
                action Jump("ne_mogu_tolate")
            else:
                action Show("tv_menu_mainroom")  # Показываем меню выбора

screen pc_in_mainroom:
    if not block_ui:
        imagebutton:
            idle "pc_mainroom_idle.png"
            hover "pc_mainroom_hover.png"
            xpos 587
            ypos 417
            focus_mask True
            if game_hour == 22:
                action Jump("ne_mogu_tolate")
            elif pc_is_unlocked == True:
                action Jump("pc_work_table")  # Показываем меню выбора
            else:
                action Jump("password") # На экран ввода пароля

screen pc_in_mainroom_night:
    if not block_ui:
        imagebutton:
            idle "pc_mainroom_night_idle.png"
            hover "pc_mainroom_night_hover.png"
            focus_mask True
            if game_hour == 22:
                action Jump("ne_mogu_tolate")
            elif pc_is_unlocked == True:
                action Jump("pc_work_table")  # Показываем меню выбора
            else:
                action Jump("password") # На экран ввода пароля

screen bed_in_mainroom:
    if not block_ui:
        imagebutton:
            idle "bed_mainroom_idle.png"
            hover "bed_mainroom_hover.png"
            xpos 1
            ypos 500
            focus_mask True
            action Show("bed_menu_mainroom")  # Показываем меню выбора

screen bed_in_mainroom_night:
    if not block_ui:
        imagebutton:
            idle "bed_mainroom_night_idle.png"
            hover "bed_mainroom_night_hover.png"
            focus_mask True
            action Show("bed_menu_mainroom")  # Показываем меню выбора

screen door_in_mainroom:
    if not block_ui:
        imagebutton:
            idle "door_mainroom_idle.png"
            hover "door_mainroom_hover.png"
            xpos 1490
            ypos 1
            focus_mask True
            if game_hour == 22:
                action Jump("ne_mogu_tolate")
            else:
                action Jump("hallway")

screen door_in_mainroom_night:
    if not block_ui:
        imagebutton:
            idle "door_mainroom_night_idle.png"
            hover "door_mainroom_night_hover.png"
            focus_mask True
            if game_hour == 22:
                action Jump("ne_mogu_tolate")
            else:
                action Jump("hallway")

label ne_mogu_tolate:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/70.mp3"
    Vika "Для этого уже слишком поздно, мне надо ложиться спать."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen box_in_mainroom:
    if not block_ui:
        imagebutton:
            idle "box_mainroom_idle.png"
            hover "box_mainroom_hover.png"
            xpos 1048
            ypos 568
            focus_mask True
            if game_hour == 22:
                action Jump("ne_mogu_tolate")
            else:
                action Jump("yaschik") 

screen box_in_mainroom_night:
    if not block_ui:
        imagebutton:
            idle "box_mainroom_night_idle.png"
            hover "box_mainroom_night_hover.png"
            focus_mask True
            if game_hour == 22:
                action Jump("ne_mogu_tolate")
            else:
                action Jump("yaschik") 


screen tv_menu_mainroom():
    tag menu  # позволяет убрать экран по Esc
    modal True
    frame:
        style "menu_frame"
        xalign 0.5
        yalign 0.5
        has vbox

        text "Что вы хотите посмотреть?" size 30

        textbutton "Посмотреть клипы BST":
            action [Hide("tv_menu_mainroom"), Jump("watch_bts")]

        textbutton "Посмотреть 'Битву магов'":
            action [Hide("tv_menu_mainroom"), Jump("Bitva_extasensov")]
        
        textbutton "Передумать":
            action Hide("tv_menu_mainroom")

screen bed_menu_mainroom():
    tag menu
    modal True

    frame:
        style "menu_frame"
        xalign 0.5
        yalign 0.5
        has vbox

        text "Что вы хотите делать?" size 30

        if game_time == "22:00":
            textbutton "Поспать":
                action [Hide("bed_menu_mainroom"), Jump("sleep_event")]
        else:
            textbutton "Поспать (вы ещё не устали)":
                action NullAction()
                sensitive False

        textbutton "Передумать":
            action Hide("bed_menu_mainroom")

label sleep_event:
    play music "dream.mp3"
    if day_index == 1:
        jump sleep_event4
    elif day_index == 5:
        jump sleep_event1
    elif day_index == 6:
        jump sleep_event2
    elif day_index == 0:
        jump sleep_event3



label sleep_event1:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ start_dialog()

    scene bg piter_night
    with dissolve

    

    show vika neutral at center
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/477.mp3"
    Vika "…Что за…"
    scene bg brige
    with fade
    show vika neutral at right
    pause 1
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/71.mp3"
    Vika "Это где я? Мосты... небо светлое…"
    scene bg piter2
    with fade
    show vika neutral at left
    pause 1
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/72.mp3"
    Vika "Это что, Питер?!"
    scene bg piter3
    with fade
    show vika neutral at right
    pause 1
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/73.mp3"
    Vika "Красиво... странно спокойно…"
    scene bg piter4
    with fade
    show vika neutral at right
    pause 1
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/74.mp3"
    Vika "Почему мне так хорошо тут?.."

    pause 1.5

    scene black
    with fade

    stop music fadeout 2.0

    $ next_day()
    $ game_hour = 10
    $ game_minute = 0
    $ update_game_time()
    scene bg mainroom
    $ _preferences.afm_enable = True
    $ renpy.music.set_pause(True) 
    voice "audio/voices/vika/75.mp3"
    Vika "Странный сон. Надо поговорить об этом с Витей."
    $ stop_dialog()
    play music "home_theme.mp3" fadeout 1
    $ quest_list[0]["available"] = True
    $ show_hud()

    jump mainroom

label sleep_event2:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ start_dialog()
    with dissolve  # убрать экраны плавно (если есть)
    scene bg sleep_event2 with Dissolve(2.5)

    play music "dreamy_city.ogg"
    show clara neutral_7 at center with Dissolve(1.0)
    $ _preferences.afm_enable = True 
    voice "audio/voices/girl/1.mp3"
    "Костюкова, я из-за тебя двойку получила!!!"
    voice "audio/voices/girl/2.mp3"
    "Почему ты не дала списать?"
    voice "audio/voices/girl/3.mp3"
    "Я тебе сейчас по башке тресну!!!"

    hide clara neutral_7 with Dissolve(1.0)
    scene black with Dissolve(1.5)
    stop music fadeout 2.0

    $ next_day()
    $ game_hour = 10
    $ game_minute = 0
    $ update_game_time()

    scene bg mainroom
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/76.mp3"
    Vika "Какая странная девочка, не помню чтоб она была у меня в классе."
    $ show_hud()

    jump mainroom

label sleep_event3:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ start_dialog()
    with dissolve  # убрать экраны плавно (если есть)
    scene bg sleep_event3 with Dissolve(2.5)

    play music "dreamy_city.ogg"
    show clara neutral_14 at center with Dissolve(1.0)
    $ _preferences.afm_enable = True 
    voice "audio/voices/girl/4.mp3"
    "Костюкова, как ты могла купить себе такие же кросовки!"
    voice "audio/voices/girl/5.mp3"
    "Это мой любимый цвет!"
    voice "audio/voices/girl/6.mp3"
    "Снимай их быстро!!!"

    hide clara neutral_14 with Dissolve(1.0)
    scene black with Dissolve(1.5)
    stop music fadeout 2.0

    $ next_day()
    $ game_hour = 10
    $ game_minute = 0
    $ update_game_time()

    scene bg mainroom
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/77.mp3"
    Vika "Опять эта девочка, какая-то она слишком капризная."
    $ show_hud()

    jump mainroom

label sleep_event4:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ start_dialog()
    with dissolve  # убрать экраны плавно (если есть)
    scene bg sleep_event4 with Dissolve(2.5)

    play music "dreamy_city.ogg"
    show clara neutral_17 at center with Dissolve(1.0)
    $ _preferences.afm_enable = True 
    voice "audio/voices/girl/7.mp3"
    "Костюкова, почему мой парень приглашает танцевать тебя???"

    hide clara neutral_17 with Dissolve(1.0)
    scene bg mainroom_night_with_siluet with Dissolve(1.0)
    scene bg sleep_event4 with Dissolve(1.5)
    show clara neutral_17 at center with Dissolve(1.0)
    $ _preferences.afm_enable = True 
    voice "audio/voices/girl/8.mp3"
    "Что значит он не знает, что он мой парень???"

    hide clara neutral_17 with Dissolve(1.0)
    scene bg mainroom_night_with_siluet2 with Dissolve(1.5)
    scene bg sleep_event4 with Dissolve(1.5)
    show clara neutral_17 at center with Dissolve(1.0)
    $ _preferences.afm_enable = True 
    voice "audio/voices/girl/9.mp3"
    "Вообще-то я его первая заметила!!!"

    hide clara neutral_17 with Dissolve(1.0)
    scene black with Dissolve(1.5)
    stop music fadeout 2.0
    $ remove_item_to_inventory("pasport")
    $ add_item_to_inventory("blackmail")

    $ next_day()
    $ game_hour = 10
    $ game_minute = 0
    $ update_game_time()

    scene bg mainroom
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/78.mp3"
    Vika "Последнее время мне снятся странные сны..."
    voice "audio/voices/vika/79.mp3"
    Vika "Я почти у цели! Самолет через несколько часов. Никакой сон не помешает мне улететь!!!"
    $ show_hud()
    $ stop_dialog()

    jump mainroom

label watch_bts:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ start_dialog()
    scene bts_01
    with perehod_diss
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/me/1.mp3"
    "Вы начали смотреть клипы BST. В комнате звучит музыка..."
    scene bts_02
    with perehod_diss
    $ _preferences.afm_enable = True
    voice "audio/voices/me/2.mp3" 
    "Вы чувствуете как вы тупеете..."
    scene bts_03
    with perehod_diss
    $ _preferences.afm_enable = True 
    voice "audio/voices/me/3.mp3"
    "Но вам уже все равно..."
    scene black
    with perehod_diss
    $ _preferences.afm_enable = True 
    voice "audio/voices/me/4.mp3"
    "Ваш интеллект снизился на 1 пункт"
    $ intellect = intellect - 1
    $ renpy.music.set_pause(False)
    $ stop_dialog()
    jump mainroom

label Bitva_extasensov:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ start_dialog()
    scene be_01
    with perehod_diss
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/me/5.mp3"
    "Вы начали смотреть Битву магов."
    scene be_02
    with perehod_diss
    $ _preferences.afm_enable = True 
    voice "audio/voices/me/6.mp3"
    "Вы чувствуете как магические силы наполняют вас"
    scene be_03
    with perehod_diss
    $ be_schet = be_schet - 1
    if be_schet > 0:
        $ _preferences.afm_enable = True 
        voice "audio/voices/me/7.mp3"
        "Еще [be_schet] cерий, и вы можете кастовать порчу на понос"
        scene black
        with perehod_diss
        $ _preferences.afm_enable = True 
        voice "audio/voices/me/8.mp3"
        "Все мы знаем, что она сразу полетит на Руслана"
    elif be_schet == 0:
        $ _preferences.afm_enable = True 
        voice "audio/voices/me/9.mp3"
        "Поздравляю, теперь вы можете кастовать почту на понос"
        scene black
        with perehod_diss
        $ _preferences.afm_enable = True 
        voice "audio/voices/me/10.mp3"
        "Руслан неожиданно пропал куда-то на час"
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/me/11.mp3"
        "Вы уже кастовали порчу на понос"
        scene black
        with perehod_diss
        $ _preferences.afm_enable = True 
        voice "audio/voices/me/12.mp3"
        "Пожалейте Руслана"
    $ renpy.music.set_pause(False)
    $ stop_dialog()
    jump mainroom

label yaschik:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene yaschik
    show screen back_arrow
    $ show_hud()

    if take_money_from_box_mainroom == False:    
        show screen money_mainroom
    if take_rebus_from_box_mainroom == False:    
        show screen rebus_mainroom    
    $ renpy.music.set_pause(False)
    call screen wait_for_click

screen money_mainroom:
    imagebutton:
        idle "money_idle.png" 
        xpos 400
        ypos 217
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "money_hover.png"
            if default_mouse == "default":
                action Show("taking_money_screen")  # Показываем меню выбора
            else:
                action Jump("eto_ne_suda")

label eto_ne_suda:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/80.mp3"
    Vika "Это точно не сюда!!!"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return



screen taking_money_screen():
    tag menu
    modal True

    frame:
        style "menu_frame"
        xalign 0.5
        yalign 0.5
        has vbox

        text "Что вы хотите делать?" size 30

        textbutton "Взять":
            action [Hide("taking_money_screen"), Jump("taking_money")]

        textbutton "Передумать":
            action Hide("taking_money_screen")



label taking_money:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/81.mp3"
    Vika "Эти деньги положил сюда Витя, значит они мои. (+100р)"
    $ block_ui = False
    $ stop_dialog()
    hide screen money_mainroom
    $ take_money_from_box_mainroom = True
    $ money = money + 100
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return



label hallway:
    $ renpy.free_memory()
    $ vitya_in_room = True
    scene bg mainhall
    play music "home_theme.mp3" fadeout 1
    $ hide_all_ui()
    show screen door_to_street
    show screen door_to_mainroom
    show screen door_to_vitya_room
    show screen door_to_toilet
    show screen door_to_kitchen
    $ travel(polojenie, "home")
    $ polojenie = "home"
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

label kitchen:
    $ renpy.free_memory()
    scene bg mainkitchen
    $ hide_all_ui()
    show screen back_arrow_to_hallway
    show screen plita
    
    
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen plita:
    imagebutton:
        idle "plita.png"
        focus_mask True
        if not block_ui:
            hover "plita_hover.png"
            if "produkti" in inventory_items:
                action Jump("cook")
            else:
                action Jump("net_piduktov") 

label net_piduktov:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/82.mp3"
    Vika "Мне пока не надо готовить"
    $ block_ui = False
    $ stop_dialog()
    jump kitchen

label cook:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg cook
    show screen table
    show screen back_arrow_to_kitchen
    show screen skovorodka
    show screen list1
    show screen meat
    show screen onion
    show screen carrot
    show screen ketchup
    show screen pasta
    show screen oil
    show screen muka
    show screen miska
    show screen forma
    show screen terka
    show screen salt
    show screen paper
    show screen milk
    show screen nuts
    show screen knife
    show screen doska
    show screen cheese
    show screen duhovka
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen skovorodka:
    imagebutton:
        idle "kitchen/skovoroda.png"        
        focus_mask True
        if default_mouse == "oil":
                action [Hide("skovorodka"), Play("sound", "kipit.mp3", loop=True), Show("skovorodka_oil"), SetVariable("default_mouse", "default")]
        elif default_mouse == "cut_onion":
                action [Hide("skovorodka"), Play("sound", "kipit.mp3", loop=True), Show("skovorodka_onion"), SetVariable("default_mouse", "default")]  

screen skovorodka_onion:
    imagebutton:
        idle "kitchen/skovoroda_onion.png"        
        focus_mask True
        if default_mouse == "cut_carrot":
                action [Hide("skovorodka_onion"), Show("skovorodka_carrot"), SetVariable("default_mouse", "default")] 

screen skovorodka_carrot:
    imagebutton:
        idle "kitchen/skovoroda_carrot.png"        
        focus_mask True
        if default_mouse == "meat":
                action [Hide("skovorodka_carrot"), Show("skovorodka_meat"), SetVariable("default_mouse", "default")] 

screen skovorodka_meat:
    imagebutton:
        idle "kitchen/skovoroda_meat.png"        
        focus_mask True
        if default_mouse == "salt":
                action [Hide("skovorodka_meat"), Show("skovorodka_meat_salt"), SetVariable("default_mouse", "default")]

screen skovorodka_meat_salt:
    imagebutton:
        idle "kitchen/skovoroda_meat.png"        
        focus_mask True
        if default_mouse == "paper":
                action [Hide("skovorodka_meat_salt"), Show("skovorodka_paper"), SetVariable("default_mouse", "default")]

screen skovorodka_paper:
    imagebutton:
        idle "kitchen/skovoroda_meat.png"        
        focus_mask True
        if default_mouse == "ketchup":
                action [Hide("skovorodka_paper"), Show("skovorodka_ketchup"), SetVariable("default_mouse", "default")]

screen skovorodka_ketchup:
    imagebutton:
        idle "kitchen/skovoroda_meat.png"        
        focus_mask True
        if default_mouse == "pasta":
                action [Hide("skovorodka_ketchup:"), Stop("sound"), Show("skovorodka_pasta"), SetVariable("default_mouse", "default")]

screen skovorodka_pasta:
    imagebutton:
        idle "kitchen/skovoroda_pasta.png"        
        focus_mask True
        if default_mouse == "default":
                action SetVariable("default_mouse", "bolonieze")

screen skovorodka_oil:
    imagebutton:
        idle "kitchen/skovoroda_oil.png"        
        focus_mask True
        if default_mouse == "muka":
                action [Hide("skovorodka_oil"), Show("skovorodka_muka"), SetVariable("default_mouse", "default")] 

screen skovorodka_muka:
    imagebutton:
        idle "kitchen/skovoroda_muka.png"        
        focus_mask True
        if default_mouse == "milk":
                action [Hide("skovorodka_muka"), Show("skovorodka_milk"), SetVariable("default_mouse", "default")] 

screen skovorodka_milk:
    imagebutton:
        idle "kitchen/skovoroda_milk.png"        
        focus_mask True
        if default_mouse == "salt":
                action [Hide("skovorodka_milk"), Show("skovorodka_salt"), SetVariable("default_mouse", "default")] 

screen skovorodka_salt:
    imagebutton:
        idle "kitchen/skovoroda_milk.png"        
        focus_mask True
        if default_mouse == "cut_nuts":
                action [Hide("skovorodka_salt"), Show("skovorodka_nuts"), SetVariable("default_mouse", "default")]

screen skovorodka_nuts:
    imagebutton:
        idle "kitchen/skovoroda_milk.png"        
        focus_mask True
        if not block_ui:
            action [Hide("skovorodka_nuts"), Stop("sound"), Show("skovorodka"), SetVariable("default_mouse", "beshamel")]

screen list1:
    imagebutton:
        idle "kitchen/list.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/list_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "list")  # Показываем меню выбора  

screen meat:
    imagebutton:
        idle "kitchen/meat.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/meat_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "meat")  # Показываем меню выбора  

screen onion:
    imagebutton:
        idle "kitchen/Onion.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/Onion_hover.png"
            if default_mouse == "default":
                action [Hide("onion"), SetVariable("default_mouse", "onion")]  # Показываем меню выбора  

screen carrot:
    imagebutton:
        idle "kitchen/carrot.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/carrot_hover.png"
            if default_mouse == "default":
                action [Hide("carrot"), SetVariable("default_mouse", "carrot")]  # Показываем меню выбора  

screen ketchup:
    imagebutton:
        idle "kitchen/ketchup.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/ketchup_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "ketchup")  # Показываем меню выбора  

screen pasta:
    imagebutton:
        idle "kitchen/pasta.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/pasta_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "pasta")  # Показываем меню выбора  

screen oil:
    imagebutton:
        idle "kitchen/oil.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/oil_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "oil") 

screen muka:
    imagebutton:
        idle "kitchen/muka.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/muka_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "muka") 

screen miska:
    imagebutton:
        idle "kitchen/miska.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "beshamel":
                action [Hide("miska"), Show("miska_bolonieze"), SetVariable("default_mouse", "default")]

screen miska_bolonieze:
    imagebutton:
        idle "kitchen/miska_bolonieze.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/miska_bolonieze_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "beshamel") 

screen forma:
    imagebutton:
        idle "kitchen/forma.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "beshamel":
                action [Hide("forma"), Show("forma_beshamel"), SetVariable("default_mouse", "default")]

screen forma_beshamel:
    imagebutton:
        idle "kitchen/forma_beshamel.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "list":
                action [Hide("forma_beshamel"), Show("forma_list"), SetVariable("default_mouse", "default")]

screen forma_list:
    imagebutton:
        idle "kitchen/forma_list.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "bolonieze":
                action [Hide("forma_list"), Show("forma_bolonieze"), SetVariable("default_mouse", "default")]

screen forma_bolonieze:
    imagebutton:
        idle "kitchen/forma_bolonieze.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "mini_cheese":
                action [Hide("forma_bolonieze"), Show("forma_mini_cheese"), SetVariable("default_mouse", "default")]

screen forma_mini_cheese:
    imagebutton:
        idle "kitchen/forma_mini_cheese.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/forma_mini_cheese_hover.png"
            if default_mouse == "default":
                action [Hide("forma_mini_cheese"), SetVariable("default_mouse", "fresh_lazania")]

screen terka:
    imagebutton:
        idle "kitchen/terka.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "cheese":
                action [Hide("cheese"), Play("sound", "terka.mp3"), Show("mini_cheese"), SetVariable("default_mouse", "default")]

screen salt:
    imagebutton:
        idle "kitchen/salt.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/salt_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "salt")   

screen paper:
    imagebutton:
        idle "kitchen/paper.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/paper_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "paper")  # Показываем меню выбора  

screen milk:
    imagebutton:
        idle "kitchen/milk.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/milk_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "milk")  

screen nuts:
    imagebutton:
        idle "kitchen/nuts.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/nuts_hover.png"
            if default_mouse == "default":
                action [Hide("nuts"), SetVariable("default_mouse", "nuts")]

screen knife:
    imagebutton:
        idle "kitchen/knife.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/knife_hover.png"
            if default_mouse == "default":
                action [Hide("knife"), SetVariable("default_mouse", "knife")]  

screen doska:
    imagebutton:
        idle "kitchen/doska.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "onion":
                action [Hide("doska"), Show("onion_on_board"), SetVariable("default_mouse", "default")]
            elif default_mouse == "carrot":
                action [Hide("doska"), Show("carrot_on_board"), SetVariable("default_mouse", "default")]
            elif default_mouse == "nuts":
                action [Hide("doska"), Show("nuts_on_board"), SetVariable("default_mouse", "default")]  

screen cheese:
    imagebutton:
        idle "kitchen/cheese.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/cheese_hover.png"
            if default_mouse == "default":
                action [Hide("cheese"), SetVariable("default_mouse", "cheese")]  # Показываем меню выбора

screen mini_cheese:
    imagebutton:
        idle "kitchen/mini_cheese.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/mini_cheese_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "mini_cheese")  # Показываем меню выбора

screen cut_onion:
    imagebutton:
        idle "kitchen/cut_onion.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/cut_onion_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "cut_onion")  # Показываем меню выбора

screen cut_carrot:
    imagebutton:
        idle "kitchen/cut_carrot.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/cut_carrot_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "cut_carrot") # Показываем меню выбора

screen cut_nuts:
    imagebutton:
        idle "kitchen/cut_nuts.png"        
        focus_mask True
        if not block_ui:
            hover "kitchen/cut_nuts_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "cut_nuts")

screen table:
    imagebutton:
        idle "kitchen/table.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "cheese":
                action [Show("cheese"), SetVariable("default_mouse", "default")] 
            elif default_mouse == "onion":
                action [Show("onion"), SetVariable("default_mouse", "default")] 
            elif default_mouse == "knife":
                action [Show("knife"), SetVariable("default_mouse", "default")]  
            elif default_mouse == "carrot":
                action [Show("carrot"), SetVariable("default_mouse", "default")]
            elif default_mouse == "nuts":
                action [Show("nuts"), SetVariable("default_mouse", "default")]
            elif default_mouse == "fresh_lazania":
                action [Show("forma_mini_cheese"), SetVariable("default_mouse", "default")]
            elif default_mouse == "cut_nuts":
                action SetVariable("default_mouse", "default")
            elif default_mouse == "oil":
                action SetVariable("default_mouse", "default")
            elif default_mouse == "muka":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "milk":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "salt":
                action SetVariable("default_mouse", "default")
            elif default_mouse == "beshamel":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "cut_onion":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "cut_carrot":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "meat":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "paper":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "ketchup":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "pasta":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "list":
                action SetVariable("default_mouse", "default")
            elif default_mouse == "bolonieze":
                action SetVariable("default_mouse", "default") 
            elif default_mouse == "mini_cheese":
                action SetVariable("default_mouse", "default")           

screen onion_on_board:
    imagebutton:
        idle "kitchen/onion_on_board.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "knife":
                action [Show("doska"), Play("sound", "narezka.mp3"), Show("knife"), Hide("onion_on_board"), Show("cut_onion"), SetVariable("default_mouse", "default")] 

screen carrot_on_board:
    imagebutton:
        idle "kitchen/carrot_on_board.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "knife":
                action [Show("doska"), Show("knife"), Play("sound", "narezka.mp3"), Hide("carrot_on_board"), Show("cut_carrot"), SetVariable("default_mouse", "default")]

screen nuts_on_board:
    imagebutton:
        idle "kitchen/nuts_on_board.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "knife":
                action [Show("doska"), Show("knife"), Play("sound", "narezka.mp3"), Hide("nuts_on_board"), Show("cut_nuts"), SetVariable("default_mouse", "default")]

screen duhovka:
    imagebutton:
        idle "kitchen/duhovka.png"        
        focus_mask True
        if not block_ui:
            if default_mouse == "fresh_lazania":
                action [SetVariable("default_mouse", "default"), Jump("cook_lazania_temp")]

label cook_lazania_temp:
    $ renpy.free_memory()
    menu:
        "Поставить на 170 градусов":
            $ lazania_temp = 170
            jump cook_lazania_time
        "Поставить на 180 градусов":
            $ lazania_temp = 180
            jump cook_lazania_time
        "Поставить на 190 градусов":
            $ lazania_temp = 190
            jump cook_lazania_time
        "Поставить на 200 градусов":
            $ lazania_temp = 200
            jump cook_lazania_time

label cook_lazania_time:
    $ renpy.free_memory()
    menu:    
        "Подождать 30 минут":
            $ lazania_time = 30
            jump cook_lazania
        "Подождать 40 минут":
            $ lazania_time = 40
            jump cook_lazania
        "Подождать 50 минут":
            $ lazania_time = 50
            jump cook_lazania
        "Подождать 60 минут":
            $ lazania_time = 60
            jump cook_lazania

label cook_lazania:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ start_dialog()
    scene black
    with perehod_diss
    pause 1.5
    scene bg cook
    if lazania_time == 40 and lazania_temp == 180:
        $ _preferences.afm_enable = True 
        $ renpy.music.set_pause(True)
        voice "audio/voices/vika/83.mp3"
        Vika "Ну вроде получилось!!!"
        $ quest_list[16]["done"] = True
        $ intellect += 1
        $ add_item_to_inventory("lazania")
        $ game_hour += 2
        $ update_game_time()
        $ remove_item_to_inventory("produkti")
        $ stop_dialog()
        jump kitchen
    else:
        $ _preferences.afm_enable = True 
        $ renpy.music.set_pause(True)
        voice "audio/voices/vika/84.mp3"
        Vika "Ну вот, не получилось, придется заново!"
        $ stop_dialog()
        jump kitchen




screen back_arrow_to_kitchen:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Show("exit")

screen exit:
    add "kitchen/exit.png"
    if not block_ui:
        imagebutton:
            idle "kitchen/yes.png"
            focus_mask True
            action [SetVariable("default_mouse", "default"), Hide("exit"), Jump("kitchen")]
    if not block_ui:
        imagebutton:
            idle "kitchen/no.png"
            focus_mask True
            action Hide("exit")


label vitya_room:
    $ renpy.free_memory()
    scene bg vitya_room
    $ store.input_code = ""
    $ hide_all_ui()
    show screen back_arrow_to_hallway
    if vitya_in_room == True:
        show screen vitya_in_vitya2_room
    show screen yaschik_vitya
    
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen vitya_in_vitya2_room:
    imagebutton:
        idle "vitya_in_vitya2_room.png"
        focus_mask True
        if not block_ui:
            hover "vitya_in_vitya2_room_hover.png"
            action Jump("vitya_dialog")  # Показываем меню выбора

label vitya_dialog:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    if first_dialog == True:
        $ _preferences.afm_enable = True 
        $ renpy.music.set_pause(True)
        voice "audio/voices/vitya/1.mp3"
        vitya "Проснулась?"
        voice "audio/voices/vika/85.mp3"
        Vika "Да"
        voice "audio/voices/vika/86.mp3"
        Vika "Слушай, мне надо с тобой поговорить, мне снился сон."
        voice "audio/voices/vitya/2.mp3"
        vitya "С питоном?"
        voice "audio/voices/vika/87.mp3"
        Vika "С Питером."
        voice "audio/voices/vitya/3.mp3"
        vitya "Паркером?" 
        voice "audio/voices/vika/88.mp3"
        Vika "Нет. Серьёзно. Я хочу уехать. В Питер. Найти работу. Начать заново."
        voice "audio/voices/vitya/4.mp3"
        vitya "Ты уверена?"
        voice "audio/voices/vika/89.mp3"
        Vika "Более чем."
        voice "audio/voices/vitya/5.mp3"
        vitya "У тебя в Орске не получилось. В Чапаевске не получилось. В Новом Уренгое — ну, ты сама знаешь. А в Питере, значит, всё получится, да?"

        pause 0.5
        voice "audio/voices/vika/90.mp3"
        Vika "Да. Именно там."
        voice "audio/voices/vitya/6.mp3"
        vitya "Ладно. Допустим. Но если ты всерьёз… Тогда вот что тебе надо сделать:"
        voice "audio/voices/vitya/7.mp3"
        vitya "Первое — купи билет. Без этого всё остальное — просто болтовня. Второе — сдай эту квартиру. Третье — найди жильё в Питере."
        voice "audio/voices/vitya/8.mp3"
        vitya "И четвёртое — уволиться. Не жаловаться, не ныть — а реально встать, собрать вещи и уйти. Если справишься — поедем, я не буду против."
        voice "audio/voices/vika/91.mp3"
        Vika "Ты думаешь, я не сделаю?"
        voice "audio/voices/vitya/9.mp3"
        vitya "Я думаю, ты часто начинаешь, но не заканчиваешь. А это не маршрутку выбрать — это жизнь перевернуть."

        pause 0.5
        voice "audio/voices/vika/92.mp3"
        Vika "Тогда смотри внимательно. Я начну — и закончу!"
        $ quest_list[0]["done"] = True
        $ quest_list[2]["available"] = True
        $ quest_list[3]["available"] = True
        $ quest_list[9]["available"] = True
        $ first_dialog = False
    else:
        $ renpy.music.set_pause(True)
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/10.mp3"
        vitya "Да?"
    jump vitya_menu

screen kamasutra:
    add "kamasutra.jpg" at Transform(xpos=800, ypos=300, zoom=1.3)

label trenirovka_kviz_1:
    show screen kamasutra
    $ _preferences.afm_enable = True 
    voice "audio/voices/vitya/11.mp3"
    vitya "Эмблема чемпионата мира по шахматам 2018 вызвала массу бурных обсуждений. И даже есть мнение, что её срисовали из НЕЁ."
    $ trenirovka1 = renpy.input("Введите ответ на вопрос:")
    if trenirovka1.lower() == "камасутра":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/14.mp3"
        vitya "Правильно, следующий вопрос"
        hide screen kamasutra
        jump trenirovka_kviz_2
    else:
        $ _preferences.afm_enable = True
        voice "audio/voices/vitya/15.mp3" 
        vitya "Неправильно, думай еще"
        jump trenirovka_kviz_1

label trenirovka_kviz_2:
    $ _preferences.afm_enable = True 
    voice "audio/voices/vitya/12.mp3"
    vitya "Известному советскому архитектору было дано задание за три дня спроектировать сооружение, в виде усеченной пирамиды для проведения важной церемонии." 
    voice "audio/voices/vitya/13.mp3"
    vitya "Он справился с задачей, было построено временное сооружение в виде усеченной пирамиды со ступенями. В последствии оно было заменено на постоянную каменную конструкцию. Что это за сооружение?"
    $ trenirovka2 = renpy.input("Введите ответ на вопрос:")
    if trenirovka2.lower() == "мавзолей":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/14.mp3"
        vitya "Правильно, следующий вопрос"
        jump trenirovka_kviz_3
    else:
        $ _preferences.afm_enable = True
        voice "audio/voices/vitya/15.mp3"  
        vitya "Неправильно, думай еще"
        jump trenirovka_kviz_2

label trenirovka_kviz_3:
    $ _preferences.afm_enable = True
    voice "audio/voices/vitya/16.mp3"  
    vitya "По мнению исследователей, прототипом сложнейшего музыкального инструмента стал обычный лук – точнее, несколько луков.  Назовите этот инструмент!" 
    $ trenirovka3 = renpy.input("Введите ответ на вопрос:")
    if trenirovka3.lower() == "арфа":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/17.mp3" 
        vitya "Правильно, ты молодец, теперь говори что ты там хотела"
        voice "audio/voices/vika/93.mp3"
        Vika "Уже ничего, поздно уже я пошла спать."
        $ quest_list[27]["done"] = True
        $ game_hour += 2
        $ update_game_time()
        $ block_ui = False
        $ stop_dialog()
        jump vitya_room
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/15.mp3" 
        vitya "Неправильно, думай еще"
        jump trenirovka_kviz_3

label vitya_menu:
    $ renpy.free_memory()
    $ stop_dialog()
    menu:
        "Тебя взяли на работу" if vitya_have_work == True and i_talk_about_work == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/94.mp3"
            Vika "Можешь начинать меня благодарить, я нашла тебе работу."
            voice "audio/voices/vitya/18.mp3" 
            vitya "У меня уже есть работа..."
            voice "audio/voices/vika/95.mp3"
            Vika "Ты получаешь на ней 200 тысяч рублей?"
            $ quest_list[39]["done"] = True
            voice "audio/voices/vitya/19.mp3"
            vitya "Нет..."
            voice "audio/voices/vika/96.mp3"
            Vika "Теперь получаешь, компания Эмерген, нужна модернизация системы безопасности, вроде как удаленка... или нет..."
            voice "audio/voices/vika/97.mp3"
            Vika "Ну в общем прилетим в питер, пойдем и узнаем. Благодарности принимаю в виде коробки чипсов"
            voice "audio/voices/vitya/20.mp3"
            vitya "Договорились, но только после квиза, собирайся."
            voice "audio/voices/vika/98.mp3"
            Vika "Я уже собрана."
            voice "audio/voices/vitya/21.mp3"
            vitya "Отлично."
            $ i_talk_about_work = True
            $ stop_dialog()
            jump quiz
        "Рассказать как прошел день" if day_index == 0 and game_hour == 20:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/99.mp3"
            Vika "У меня столько всего за день произошло!"
            voice "audio/voices/vitya/22.mp3"
            vitya "Погоди погоди, прежде чем ты опять начнешь рассказ на 2 часа о своих колбах и пробирках..."
            voice "audio/voices/vika/100.mp3"
            Vika "Ты охренел?? Вообще-то я уволилась!!!"
            voice "audio/voices/vitya/23.mp3"
            vitya "Да?, ну ладно ве равно подожди. Ты же помнишь что завтра квиз?"
            voice "audio/voices/vika/101.mp3"
            Vika "Ну да"
            voice "audio/voices/vitya/24.mp3"
            vitya "Это значит, что надо тренироваться, и начнем прямо сейчас"
            voice "audio/voices/vika/102.mp3"
            Vika "Ну неееет..."
            voice "audio/voices/vitya/25.mp3"
            vitya "Вот твой первый вопрос"
            jump trenirovka_kviz_1
        "Мы все-таки переезжаем в питер" if bileti_kupleni == True and kvartira_snyata == True and uvolena == True and bil_zvonok_shluhe == True and razgovor_pro_piter == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/103.mp3"
            Vika "Я купила билеты, решила вопрос с квартирами и уволилась с работы, теперь ты не отвертишься, мы переезжаем в питер!"
            voice "audio/voices/vitya/26.mp3"
            vitya "Чегооооо???"
            voice "audio/voices/vika/104.mp3"
            Vika "Да, квартира уже сдана"
            voice "audio/voices/vitya/27.mp3"
            vitya "Кому?"
            voice "audio/voices/vika/105.mp3"
            Vika "Не важно, собирай вещи прямо сейчас"
            voice "audio/voices/vitya/28.mp3"
            vitya "Сейчас не могу, уже 8 часов, у нас своя игра. Точно! если ты не выйграешь, переезд в питер анулируется"
            voice "audio/voices/vika/106.mp3"
            Vika "Так не честно!!!"
            voice "audio/voices/vitya/29.mp3"
            vitya "Ничего не знаю, выйграешь - точно едем."
            voice "audio/voices/vika/107.mp3"
            Vika "Ладно..."
            voice "audio/voices/vitya/30.mp3"
            vitya "Что-то еще?"
            $ quest_list[13]["available"] = True
            $ quest_list[12]["done"] = True
            $ razgovor_pro_piter = True
            $ sigame_is_available = True
            jump vitya_menu
        "Ты поставил пароль на компьютере?" if pc_is_unlocked == False and i_know_password == True and vitya_password == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/108.mp3"
            Vika "Ты поставил пароль на компьютере???"
            voice "audio/voices/vitya/31.mp3"
            vitya "Да"
            voice "audio/voices/vika/109.mp3"
            Vika "Зачем?"
            voice "audio/voices/vitya/32.mp3"
            vitya "Из соображений кибер безопасности конечно!!!"
            voice "audio/voices/vika/110.mp3"
            Vika "Киберчего??? Ладно, говори пароль?"
            voice "audio/voices/vitya/33.mp3"
            vitya "Я его забыл, но я записал его на листочке и положил в твой ящик."
            voice "audio/voices/vika/111.mp3"
            Vika "То есть ты из-за кибербезопасности поставил пароль, записал его и положил рядом с компьютером???"
            voice "audio/voices/vitya/34.mp3"
            vitya "Ну я же не дурак... Я его зашифровал"
            voice "audio/voices/vika/112.mp3"
            Vika "Ой ладно..."
            $ vitya_password = True
            jump vitya_menu
        "Попросить починить розетку" if rozetka_is_broken == True and vitya_rozetka == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/113.mp3"
            Vika "Шел 184ый день как у нас сломана розетка."
            voice "audio/voices/vitya/35.mp3"
            vitya "Я починю позже"
            voice "audio/voices/vika/114.mp3"
            Vika "Когда позже???"
            voice "audio/voices/vitya/36.mp3"
            vitya "Позже, я сейчас занят"
            voice "audio/voices/vika/115.mp3"
            Vika "Ты так уже пол года говоришь..."
            voice "audio/voices/vitya/37.mp3"
            vitya "Если тебе так срочно надо - просто найди мастера"
            voice "audio/voices/vika/116.mp3"
            Vika "Хорошо, я найду если тебе не стыдно."
            $ vitya_rozetka = False
            jump vitya_menu
        "Попросить убрать банер" if show_buner == 1 and kvest_na_lazanyu == "done":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/117.mp3"
            Vika "Можешь убрать банер?"
            voice "audio/voices/vitya/38.mp3"
            vitya "Опять?"
            voice "audio/voices/vika/118.mp3"
            Vika "Ну пожалуйста..."
            voice "audio/voices/vitya/39.mp3"
            vitya "Ладно..."
            $ show_buner = 0
            $ vitya_in_room = False
            $ block_ui = False
            $ stop_dialog()
            jump vitya_room

        "Ты убрал баннер?" if "lazania" not in inventory_items and kvest_na_lazanyu == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/119.mp3"
            Vika "Ты убрал банер?"
            voice "audio/voices/vitya/40.mp3"
            vitya "А ты принесла мне лазанью?"
            voice "audio/voices/vika/120.mp3"
            Vika "Нет("
            jump vitya_menu
        
        "Ты убрал баннер?" if ("lazania" in inventory_items and kvest_na_lazanyu):
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/119.mp3"
            Vika "Ты убрал банер?"
            voice "audio/voices/vitya/40.mp3"
            vitya "А ты принесла мне лазанью?"
            voice "audio/voices/vika/121.mp3"
            Vika "Да, вот она"
            $ quest_list[4]["done"] = True
            $ intellect += 1
            $ remove_item_to_inventory("lazania")
            voice "audio/voices/vitya/41.mp3"
            vitya "Ладно, сейчас уберу..."
            $ kvest_na_lazanyu = "done"
            $ show_buner = 0
            $ vitya_in_room = False
            $ block_ui = False
            $ stop_dialog()
            jump vitya_room

        "Попросить убрать банер" if show_buner == 1 and kvest_na_lazanyu == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/122.mp3"
            Vika "Мне нужна твоя помощь."
            voice "audio/voices/vitya/42.mp3"
            vitya "Что случилось?"
            voice "audio/voices/vika/123.mp3"
            Vika "В общем... Я случайно зашла на один сайт..."
            voice "audio/voices/vitya/43.mp3"
            vitya "И теперь на экране висит какая-то телка?"
            voice "audio/voices/vika/124.mp3"
            Vika "А ты откуда знаешь???"
            voice "audio/voices/vitya/44.mp3"
            vitya "Эмм... так тебе помочь убрать?"
            voice "audio/voices/vika/85.mp3"
            Vika "Да"
            voice "audio/voices/vitya/45.mp3"
            vitya "Мне сейчас некогда"
            voice "audio/voices/vika/125.mp3"
            Vika "Ну пожалуйста!!! она меня бесит и занимает пол экрана!!!"
            voice "audio/voices/vitya/46.mp3"
            vitya "Ну ладно, я уберу. Но только после того как ты приготовишь мне лазанью!"
            voice "audio/voices/vika/126.mp3"
            Vika "Лазанью??? У нас нет на нее продуктов!!!"
            voice "audio/voices/vitya/47.mp3"
            vitya "Сходи в магазин и купи. Возьми мою карту, там 8 тысяч, тебе хватит на продукты"
            $ game_hour += 1
            $ update_game_time()
            $ add_item_to_inventory("card")
            voice "audio/voices/vika/127.mp3"
            Vika "Эмм... Там уже не 8 тысяч... Я потратила почти все на шмотки..."
            voice "audio/voices/vitya/48.mp3"
            vitya "И сколько там осталось?"
            if slojnost_igry == "easy":
                voice "audio/voices/vika/128.mp3"
                Vika "2000 рублей..."
            else:
                voice "audio/voices/vika/129.mp3"
                Vika "1825 рублей..."
            voice "audio/voices/vitya/49.mp3"
            vitya "Тогда тебе придется быть очень экономной. В общем будет лазанья - не будет банера."
            voice "audio/voices/vika/107.mp3"
            Vika "Ладно..."
            voice "audio/voices/vitya/30.mp3"
            vitya "Что-то еще?"
            $ quest_list[7]["available"] = True
            $ kvest_na_lazanyu = True
            jump vitya_menu
        "Мне нужно идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            $ block_ui = False
            $ stop_dialog()
            $ renpy.music.set_pause(False)
            jump vitya_room

label quiz:
    $ hide_all_ui()
    scene black
    with dissolve
    pause 0.5
    scene bg quiz
    with dissolve
    jump quiz_1

label quiz_1:
    scene bg quiz
    $ _preferences.afm_enable = True 
    voice "audio/voices/veduschiy/1.mp3"
    veduschiy "И так, первый вопрос: В 1814 году этот европейский город был взят войсками коалиции, а его название навсегда стало символом поражения. О каком городе идёт речь?"
    $ quiz_1 = renpy.input("Введите ответ на вопрос:")
    if quiz_1.lower() == "париж":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/50.mp3"
        vitya "Точно"
        jump quiz_2
    else:
        $ _preferences.afm_enable = True
        voice "audio/voices/vitya/51.mp3" 
        vitya "Точно нет"
        jump quiz_1

label quiz_2:
    $ _preferences.afm_enable = True 
    scene bg quiz
    voice "audio/voices/veduschiy/2.mp3"
    veduschiy "Эта картина была написана в 1889 году, на ней изображено звёздное небо над небольшим городом. Как называется работа?"
    $ quiz_1 = renpy.input("Введите ответ на вопрос:")
    if quiz_1.lower() == "звездная ночь" or quiz_1.lower() == "звёздная ночь":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/50.mp3"
        vitya "Точно"
        jump quiz_3
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/51.mp3" 
        vitya "Точно нет"
        jump quiz_2

label quiz_3:
    $ _preferences.afm_enable = True 
    scene bg quiz
    voice "audio/voices/veduschiy/3.mp3"
    veduschiy "Этот орган человека способен вырастать в 4–5 раз от своего исходного размера, а затем возвращаться в прежнее состояние. Что это?"
    $ quiz_1 = renpy.input("Введите ответ на вопрос:")
    if quiz_1.lower() == "матка":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/50.mp3"
        vitya "Точно"
        jump quiz_4
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/51.mp3" 
        vitya "Точно нет"
        jump quiz_3

label quiz_4:
    $ _preferences.afm_enable = True 
    scene bg quiz
    voice "audio/voices/veduschiy/4.mp3"
    veduschiy "Если в космосе (в невесомости) надуть мыльный пузырь, какой формы он будет: круглой, плоской или кубической?"
    $ quiz_1 = renpy.input("Введите ответ на вопрос:")
    if quiz_1.lower() == "круглой":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/50.mp3"
        vitya "Точно"
        jump quiz_5
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/51.mp3" 
        vitya "Точно нет"
        jump quiz_4

label quiz_5:
    $ _preferences.afm_enable = True 
    scene bg quiz
    voice "audio/voices/veduschiy/5.mp3"
    veduschiy "Сколько цветов можно увидеть при рассмотрении картины квадрат Малевича"
    $ quiz_1 = renpy.input("Введите ответ на вопрос:")
    if quiz_1.lower() == "3"or quiz_1.lower() == "три":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/50.mp3"
        vitya "Точно"
        jump quiz_win
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vitya/51.mp3" 
        vitya "Точно нет"
        jump quiz_5

label quiz_win:
    $ start_dialog()
    $ _preferences.afm_enable = True 
    voice "audio/voices/vitya/52.mp3" 
    vitya "Ты молодец, можем ехать домой"
    $ game_hour += 1
    $ update_game_time()
    scene bg mainroom_night
    with dissolve
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    jump mainroom

screen yaschik_vitya:
    imagebutton:
        idle "yaschik_vitya_idle.png"
        focus_mask True
        if not block_ui:
            hover "yaschik_vitya_hover.png"
            if vitya_in_room == True:
                action Jump("ne_trogay_yashik")
            else: 
                action Jump("yaschik_vitya")   

label ne_trogay_yashik:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vitya/53.mp3"
    vitya "Не трогай мой ящик!!!"
    $ quest_list[8]["available"] = True
    $ block_ui = False
    $ stop_dialog()
    jump vitya_room

label yaschik_vitya:
    $ renpy.free_memory()
    $ quest_list[8]["available"] = True
    $ quest_list[8]["done"] = True
    $ intellect += 1
    $ hide_all_ui()
    scene bg yaschik_vitya
    show screen back_arrow_to_vitya_room
    if vitya_lock == "open":
        $ lock_is_locked = False
        show screen lock
    else:
        $ lock_is_locked = True
        show screen locked_lock


    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen lock:
    imagebutton:
        idle "lock.png"
        focus_mask True
        if not block_ui:
            hover "lock_hover.png"
            action Jump("opened_box_vitya")    

label opened_box_vitya:
    $ renpy.free_memory()
    hide screen lock
    scene bg opened_box_vitya
    show screen back_arrow_to_vitya_room
    show screen ploskogubci
    show screen moovie_ticket
    if money_10_1_taken == False:
        show screen money_10_1
    if money_10_2_taken == False:
        show screen money_10_2
    show screen smartphone
    if money_10_3_taken == False:
        show screen money_10_3
    show screen glasses
    show screen gondon
    show screen flash_card
    show screen disk
    if gvozd_taken == False:
        show screen gvozd
    if superkley_taken == False:
        show screen superkley
    if humer_taken == False:
        show screen humer
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen ploskogubci:
    imagebutton:
        idle "lock/ploskogubci.png"
        focus_mask True
        if not block_ui:
            hover "lock/ploskogubci_hover.png"
            action Jump("ploskogubci") 

label ploskogubci:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/130.mp3"
    Vika "Это плоскогупцы. Не пассатижи. Если назвать плоскогубцы пассатижами - можно получить плоскогубцами. В общем они мне не нужны."
    $ block_ui = False
    $ stop_dialog()
    jump opened_box_vitya

screen moovie_ticket:
    imagebutton:
        idle "lock/moovie_ticket.png"
        focus_mask True
        if not block_ui:
            hover "lock/moovie_ticket_hover.png"
            action Jump("moovie_ticket")

label moovie_ticket:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/131.mp3"
    Vika "Похоже мы скоро пойдем в кино. Круто!"
    $ block_ui = False
    $ stop_dialog()
    jump opened_box_vitya

screen money_10_1:
    imagebutton:
        idle "lock/money_10_1.png"
        focus_mask True
        if not block_ui:
            hover "lock/money_10_1_hover.png"
            action Jump("money_10_1")

label money_10_1:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/132.mp3"
    Vika "Это я могу взять, он не обидится."
    $ money_10_1_taken = True
    $ money += 10
    $ block_ui = False
    $ stop_dialog()
    hide screen money_10_1
    jump opened_box_vitya

screen money_10_2:
    imagebutton:
        idle "lock/money_10_2.png"
        focus_mask True
        if not block_ui:
            hover "lock/money_10_2_hover.png"
            action Jump("money_10_2")

label money_10_2:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/132.mp3"
    Vika "Это я могу взять, он не обидится"
    $ money_10_2_taken = True
    $ money += 10
    $ block_ui = False
    $ stop_dialog()
    hide screen money_10_2
    jump opened_box_vitya

screen smartphone:
    imagebutton:
        idle "lock/smartphone.png"
        focus_mask True
        if not block_ui:
            hover "lock/smartphone_hover.png"
            action Jump("smartphone")

label smartphone:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/133.mp3"
    Vika "Это мой старый телефон, пусть лежит тут, он всё равно не работает."
    $ block_ui = False
    $ stop_dialog()
    jump opened_box_vitya

screen money_10_3:
    imagebutton:
        idle "lock/money_10_3.png"
        focus_mask True
        if not block_ui:
            hover "lock/money_10_3_hover.png"
            action Jump("money_10_3")

label money_10_3:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/132.mp3"
    Vika "Это я могу взять, он не обидится"
    $ money_10_3_taken = True
    $ money += 10
    $ block_ui = False
    $ stop_dialog()
    hide screen money_10_3
    jump opened_box_vitya

screen glasses:
    imagebutton:
        idle "lock/glasses.png"
        focus_mask True
        if not block_ui:
            hover "lock/glasses_hover.png"
            action Jump("glasses")

label glasses:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/134.mp3"
    Vika "И зачем человеку очки в новом уренгое?"
    $ block_ui = False
    $ stop_dialog()
    jump opened_box_vitya

screen gondon:
    imagebutton:
        idle "lock/gondon.png"
        focus_mask True
        if not block_ui:
            hover "lock/gondon_hover.png"
            action Jump("gondon")

label gondon:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/135.mp3"
    Vika "Если я сейчас его возьму, Витя меня неправильно поймет."
    $ block_ui = False
    $ stop_dialog()
    jump opened_box_vitya

screen flash_card:
    imagebutton:
        idle "lock/flash_card.png"
        focus_mask True
        if not block_ui:
            hover "lock/flash_card_hover.png"
            action Jump("flash_card")

label flash_card:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/136.mp3"
    Vika "Там Витины проекты: Бункер, какие-то цитаты. В общем ничего полезного."
    $ block_ui = False
    $ stop_dialog()
    jump opened_box_vitya

screen disk:
    imagebutton:
        idle "lock/disk.png"
        focus_mask True
        if not block_ui:
            hover "lock/disk_hover.png"
            action Jump("disk")

label disk:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/137.mp3"
    Vika "Один терабайт, и весь забит каким-то кодом."
    $ block_ui = False
    $ stop_dialog()
    jump opened_box_vitya

screen gvozd:
    imagebutton:
        idle "lock/gvozd.png"
        focus_mask True
        if not block_ui:
            hover "lock/gvozd_hover.png"
            action Jump("gvozd")

label gvozd:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/138.mp3"
    Vika "Это может пригодиться."
    $ gvozd_taken = True
    $ add_item_to_inventory("gvozd")
    $ block_ui = False
    $ stop_dialog()
    hide screen gvozd   
    jump opened_box_vitya

screen superkley:
    imagebutton:
        idle "lock/superkley.png"
        focus_mask True
        if not block_ui:
            hover "lock/superkley_hover.png"
            action Jump("superkley")

label superkley:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/138.mp3"
    Vika "Это может пригодиться"
    $ superkley_taken = True
    $ add_item_to_inventory("superkley")
    $ block_ui = False
    $ stop_dialog()
    hide screen superkley  
    jump opened_box_vitya

screen humer:
    imagebutton:
        idle "lock/humer.png"
        focus_mask True
        if not block_ui:
            hover "lock/humer_hover.png"
            action Jump("humer")

label humer:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/138.mp3"
    Vika "Это может пригодиться"
    $ humer_taken = True
    $ add_item_to_inventory("humer")
    $ block_ui = False
    $ stop_dialog()
    hide screen humer
    jump opened_box_vitya

default input_code = ""

screen locked_lock:
    imagebutton:
        idle "lock/lock_1.png"
        hover "lock/lock_1_hover.png"
        focus_mask True
        action Function(add_digit, "1")

    imagebutton:
        idle "lock/lock_2.png"
        hover "lock/lock_2_hover.png"
        focus_mask True
        action Function(add_digit, "2")

    imagebutton:
        idle "lock/lock_3.png"
        hover "lock/lock_3_hover.png"
        focus_mask True
        action Function(add_digit, "3")

    imagebutton:
        idle "lock/lock_4.png"
        hover "lock/lock_4_hover.png"
        focus_mask True
        action Function(add_digit, "4")

    imagebutton:
        idle "lock/lock_5.png"
        hover "lock/lock_5_hover.png"
        focus_mask True
        action Function(add_digit, "5")

    imagebutton:
        idle "lock/lock_6.png"
        hover "lock/lock_6_hover.png"
        focus_mask True
        action Function(add_digit, "6")

    imagebutton:
        idle "lock/lock_7.png"
        hover "lock/lock_7_hover.png"
        focus_mask True
        action Function(add_digit, "7")

    imagebutton:
        idle "lock/lock_8.png"
        hover "lock/lock_8_hover.png"
        focus_mask True
        action Function(add_digit, "8")

    imagebutton:
        idle "lock/lock_9.png"
        hover "lock/lock_9_hover.png"
        focus_mask True
        action Function(add_digit, "9")

init python:
    def add_digit(digit):
        store.input_code += digit
        renpy.play("beep.mp3")
        if len(store.input_code) == 6:
            if store.input_code == "231124":
                store.vitya_lock = "open"
                renpy.play("unlock.mp3")
                renpy.jump("yaschik_vitya")
            else:
                renpy.play("wrong.mp3")
            store.input_code = "" 

screen back_arrow_to_vitya_room:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("vitya_room")  # Показываем меню выбора  

label toilet:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg mainbathroom
    show screen back_arrow_to_hallway
    show screen unitaz
    show screen dush
    show screen rakovina_bathroom
    show screen mirror
    show screen yaschik_bathroom
    
    
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen rakovina_bathroom:
    if not block_ui:
        imagebutton:
            idle "rakovina_bathroom_idle.png"
            hover "rakovina_bathroom_hover.png"
            focus_mask True
            action Jump("umitsya")

label umitsya:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ block_ui = True
    $ start_dialog()
    scene black
    with perehod_diss
    $ hair_color = "default"
    $ lips_color = "default"
    $ lins_color = "default"
    $ eyes_color = "default"
    $ makeup_level = 6
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/139.mp3"
    Vika "Фух, теперь можно снова запачкаться."
    pause 0.5
    $ block_ui = False
    $ stop_dialog()
    scene bg mainbathroom
    with perehod_diss
    jump toilet

screen yaschik_bathroom:
    if not block_ui:
        imagebutton:
            idle "yaschik_bathroom_idle.png"
            hover "yaschik_bathroom_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("bathroom_yaschik")  # Показываем меню выбора

label bathroom_yaschik:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg bathroom_yaschik
    show screen back_arrow_to_bathroom
    if kosmetik_is_taken == False:
        show screen kosmetik
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen back_arrow_to_bathroom:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("toilet")

screen kosmetik:
    imagebutton:
        idle "kosmetik.png"
        focus_mask True
        if not block_ui:
            hover "kosmetik_hover.png"
            action Jump("taken_kosmetik")

label taken_kosmetik:
    $ kosmetik_is_taken = True
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/140.mp3"
    Vika "Моя старая косметичка, только кисточки не хватает, все равно возьму."
    $ block_ui = False
    $ stop_dialog()
    hide screen kosmetik
    $ add_item_to_inventory("kosmetik")
    jump bathroom_yaschik

label ne_dodelano:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    Vika "Это место разработчик не доделал, лучше туда не лезть"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label main_ment_door_monolog:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/141.mp3"
    Vika "По центру обычно двери начальства, но встреча с начальником полиции мне сейчас не нужна."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return


label lift_monolog:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/142.mp3"
    Vika "Самый бесполезный лифт в мире, сделан только для солидности, и только в подвале."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen mirror:
    if not block_ui:
        imagebutton:
            idle "mirror_idle.png"
            hover "mirror_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("label_mirror")  # Показываем меню выбора

label label_mirror:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/143.mp3"
    Vika "Это моё зеркало перед которым я люблю краситься."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return
    

screen unitaz:
    if not block_ui:
        imagebutton:
            idle "toilen_bathroom_idle.png"
            hover "toilen_bathroom_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("pisat")  # Показываем меню выбора

label pisat:
    $ hide_all_ui()
    $ block_ui = True
    $ start_dialog()
    scene black
    with perehod_diss
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/144.mp3"
    Vika "Хмм... Интересно, а почему водопад назвали Виктория?"
    play sound "toilet_sound.mp3"
    pause 0.5
    $ block_ui = False
    $ stop_dialog()
    scene bg mainbathroom
    with perehod_diss
    jump toilet

screen dush:
    if not block_ui:
        imagebutton:
            idle "dush_idle.png"
            hover "dush_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("dush")  # Показываем меню выбора

label dush:
    $ hide_all_ui()
    $ block_ui = True
    $ start_dialog()
    scene black
    with perehod_diss
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    play sound "dush_sound.mp3"
    voice "audio/voices/vika/145.mp3"
    Vika "Шинин фру зе сити виз э литл фанк энд сол соу ама лайт ит ап лайк дайнамайт"
    stop sound 
    $ block_ui = False
    $ stop_dialog()
    scene bg mainbathroom
    with perehod_diss
    jump toilet


label street:
    play music "city.mp3" fadeout 1
    $ renpy.free_memory()
    scene bg nu_map
    $ hide_all_ui()
    show screen home_point
    if i_know_blackmail == True:
        show screen blackmail_map_point
    if i_know_casino == True:
        show screen casino_map_point
    show screen airport_map_point
    if messange_from_ment == True:
        show screen police_map_point
    if i_know_masterskaya == True:
        show screen masterskaya_map_point
    if i_know_bar == True:
        show screen bar_map_point
    show screen shop_map_point
    if i_know_school == True:
        show screen school_map_point
    if i_know_studio == True:
        show screen foto_map_point
    if i_know_fishstore == True:
        show screen fishman_map_point
    if i_know_work == True:
        show screen work_map_point
    if i_know_river == True:
        show screen river_map_point
    show screen time_display
    if vilojeno_obyavleniya == True and bil_zvonok_shluhe == False:
        jump zvonok_shluhe
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen blackmail_map_point:
    imagebutton:
        idle "blackmail_map_idle.png"
        xpos 450
        ypos 490
        focus_mask True
        at Transform(zoom=1.3)
        if not block_ui:
            hover "blackmail_map_hover.png"
            action Jump("podval_vhod")

label podval_vhod:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "blackmail")
    $ polojenie = "blackmail"
    play music "city.mp3" fadeout 1
    scene bg podval_vhod
    show screen back_arrow_to_map
    show screen vhod
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen vhod:
    imagebutton:
        idle "day_3/vhod.png"
        focus_mask True
        if not block_ui:
            hover "day_3/vhod_hover.png"
            action Jump("podval")

label podval:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg podval
    show screen vihod
    show screen miska_p
    show screen truba
    if clara_show == False:
        $ block_ui = True
        $ start_dialog()
        $ _preferences.afm_enable = True 
        $ renpy.music.set_pause(True)
        voice "audio/voices/clara/4.mp3"
        clara "Так так так... Ты все таки пришла..."
        show clara_neutral at center
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/146.mp3"
        Vika "Ты???"
        voice "audio/voices/clara/5.mp3"
        clara "Конечно же я!"
        voice "audio/voices/vika/147.mp3"
        Vika "Зачем ты взяла мой паспорт?"
        voice "audio/voices/clara/6.mp3"
        clara "Чтоб ты не уехала, я же тебе все написала..."
        voice "audio/voices/vika/148.mp3"
        Vika "Но зачем тебе чтоб я осталась в городе, тебе же нужно, чтоб я освободила квартиру?"
        voice "audio/voices/clara/7.mp3"
        clara "Я так и знала, что ты даже сейчас меня не вспомнишь. Ты мне всю жизнь мешаешь и даже не замечаешь этого..."
        voice "audio/voices/clara/8.mp3"
        clara "От тебя вечно одни проблемы, когда мы были детьми ты вечно была самая умная, на твоем фоне приходилось не сладко"
        voice "audio/voices/clara/9.mp3"
        clara "Моя репутация в классе была на минимуме только из-за тебя, даже парни которые со мной общались, полностью теряли интерес, когда ты появлялась рядом."
        voice "audio/voices/clara/10.mp3"
        clara "Из-за тебя я ничего добилась в орске и решила уехать к тетке в чапаевск, и первое что я увидела в маленьком городе - это тебя..."
        voice "audio/voices/clara/11.mp3"
        clara "И ты опять мне мешала, универ, работа, я всегда и везде видела тебя рядом, из-за тебя я не закончила универ и стала тем кем стала..."
        voice "audio/voices/clara/12.mp3"
        clara "Я попыталась уехать, думала надо бежать куда-нибудь подальше, и нашла идеальное место - самый северный город, до которого может доехать поезд"
        voice "audio/voices/clara/13.mp3"
        clara "Ты вообще не должна была сюда приехать, но ты познакомилась с мужиком отсюда и тоже двинулась сюда, я на столько тебя ненавижу, что прибить готова..."
        voice "audio/voices/clara/14.mp3"
        clara "Я думала, что надо уехать в большой город, в который ты даже если и приедешь, то я тебя не смогу там найти, я выбрала Санкт-Петербург"
        voice "audio/voices/clara/15.mp3"
        clara "И тут, я вижу что ты сдаешь квартиру, мне нужно было срочно узнать, куда ты едешь и я опять узнала, что мы будем в одном городе."
        voice "audio/voices/clara/16.mp3"
        clara "Как только я не пыталась тебя остановить, подговорила тебя обокрасть казино и натравила полицию, переспала с твоим боссом что бы он помешал тебе уехать..."
        voice "audio/voices/clara/17.mp3"
        clara "Но тебе вечно везет... Деньги достались легко, как только я переспала с ментом, его тут же уволили, а этот жирный погряз в каких-то судебных разбирательствах."
        voice "audio/voices/clara/18.mp3"
        clara "Но теперь ты точно никак не уйдешь от меня, ты останешься здесь навечно..."
        hide clara_neutral
        pause 1.0
        show screen no_signal
        pause 0.5
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/149.mp3"
        Vika "Блин, связи нету, надо как-то выбираться..."
        pause 0.5
        hide screen no_signal
        $ clara_show = True
        $ no_signal = True
        $ block_ui = False
        $ stop_dialog()
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen no_signal:
    add "day_3/no_signal.png" xpos 750 ypos 150

screen vihod:
    if not block_ui:
        imagebutton:
            idle "day_3/vihod.png"
            focus_mask True
            hover "day_3/vihod_hover.png"
            action Jump("zaperto")

label miska_p:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/150.mp3"
    Vika "Я не дура, что бы есть из миски"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen miska_p:
    imagebutton:
        idle "day_3/miska.png"
        focus_mask True
        if not block_ui:
            hover "day_3/miska_hover.png"
            action Jump("miska_p")

screen truba:
    imagebutton:
        idle "day_3/truba.png"
        focus_mask True
        if not block_ui:
            hover "day_3/truba_hover.png"
            action Jump("truba")

label truba:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg truba
    show screen truba_max
    show screen back_arrow_to_podval
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen truba_max:
    imagebutton:
        idle "day_3/truba_max.png"
        focus_mask True
        if not block_ui:
            hover "day_3/truba_max_hover.png"
            if default_mouse == "phone":
                action Jump("kontsovka")
            else:
                action Jump("and_how")

label kontsovka:
    $ block_ui = True
    $ start_dialog()
    pause 0.5
    $ default_mouse = "default"
    show screen have_signal
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/151.mp3"
    Vika "Связь появилась!!! Надо срочно звонить вите!!!"
    hide screen have_signal
    show screen vitya_contact_call_photo
    play sound "long_phone_sound.mp3"
    pause 0.5
    hide screen vitya_contact_call_photo with Dissolve(1.0)
    stop sound 
    $ hide_all_ui()
    scene black with Dissolve(1.0)
    scene bg podval_vhod with Dissolve(1.0)
    voice "audio/voices/me/13.mp3"
    "Витя достал Вику из подвала очень быстро, так что Клара даже не успела доехать до бара."
    scene bg final1 with Dissolve(1.0)
    voice "audio/voices/me/14.mp3"
    "Благодаря тому, что быстро удалось вызвать полицию, они взяли её прямо в такси."
    scene bg final2 with Dissolve(1.0)
    voice "audio/voices/me/15.mp3"
    "Клару осудили на 6 лет, теперь у нее будет время подумать о том, что происходит в ее жизни."
    scene bg final3 with Dissolve(1.0)
    voice "audio/voices/me/16.mp3"
    "Хотя с её профессией, ей придется не сладко."
    scene bg final4 with Dissolve(1.0)
    voice "audio/voices/me/17.mp3"
    "Директор компании Bluegen погряз в судебных разбирательствах и экстренно ликвидировал компанию"
    scene bg final5 with Dissolve(1.0)
    voice "audio/voices/me/18.mp3"
    "А Вика и Витя наконец-то улетели в культурную столицу"
    jump titri
    


screen have_signal:
    add "big_iphone.png" xpos 750 ypos 150

label and_how:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/152.mp3"
    Vika "И как мне это поможет выбраться?"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen back_arrow_to_podval:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("podval")  # Показываем меню выбора  

screen school_map_point:
    imagebutton:
        idle "school_map.png"
        xpos 1120
        ypos 400
        focus_mask True
        at Transform(zoom=1.3)
        if not block_ui:
            hover "school_map_hover.png"
            if makeup_level == 5:
                action Jump("need_bathroom")
            else:
                action Jump("school")  # Показываем меню выбора

label school:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "school")
    $ polojenie = "school"
    play music "city.mp3" fadeout 1
    scene bg school_build
    show screen back_arrow_to_map
    show screen door_to_school
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen door_to_school:
    imagebutton:
        idle "school/door_in_to_school.png"
        focus_mask True
        if not block_ui:
            hover "school/door_in_to_school_hover.png"
            action Jump("school_hall")  # Показываем меню выбора    

label school_hall:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg school_hall
    show screen back_arrow_to_school
    show screen door_to_piano
    play music "school.mp3" fadeout 1
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen door_to_piano:
    imagebutton:
        idle "school/door_to_piano.png"
        focus_mask True
        if not block_ui:
            hover "school/door_to_piano_hover.png"
            action Jump("piano_class")  # Показываем меню выбора 

screen back_arrow_to_school:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("school")  # Показываем меню выбора

label piano_class:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg piano_room
    show screen back_arrow_to_school_hall
    show screen piano
    play music "school_class.mp3" fadeout 1
    if masha_is_here == True:
        show screen piano_teacher
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen piano:
    imagebutton:
        idle "school/piano.png"
        focus_mask True
        if not block_ui:
            hover "school/piano_hover.png"
            action Jump("piano") 

label piano:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg piano
    show screen piano_board
    show screen back_arrow_to_school_room
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen piano_board:
    if not block_ui:
        imagebutton:
            idle "school/piano_board.png"
            hover "school/piano_board_hover.png"
            focus_mask True
            if masha_is_here == True:
                action Jump("dont_touch_piano")
            else:
                action Jump("piano_max")

label dont_touch_piano:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/teacher/1.mp3"
    teacher "Не трогайте пианино юная леди, оно не для делетантов!!!"
    $ block_ui = False
    $ stop_dialog()
    jump piano

label piano_max:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ store.input_song = ""
    scene bg piano_max
    show screen song_play
    show screen back_arrow_to_piano
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

default input_song = ""

screen song_play:
    imagebutton:
        idle "school/c1.png"
        hover "school/c1_hover.png"
        focus_mask True
        action [Play("sound", "c1.mp3"), Function(add_nota, "c1")]
    imagebutton:
        idle "school/c#1.png"
        hover "school/c#1_hover.png"
        focus_mask True
        action [Play("sound", "c#1.mp3"), Function(add_nota, "c#1")]
    imagebutton:
        idle "school/d1.png"
        hover "school/d1_hover.png"
        focus_mask True
        action [Play("sound", "d1.mp3"), Function(add_nota, "d1")]
    imagebutton:
        idle "school/d#1.png"
        hover "school/d#1_hover.png"
        focus_mask True
        action [Play("sound", "d#1.mp3"), Function(add_nota, "d#1")]
    imagebutton:
        idle "school/e1.png"
        hover "school/e1_hover.png"
        focus_mask True
        action [Play("sound", "e1.mp3"), Function(add_nota, "e1")]
    imagebutton:
        idle "school/f1.png"
        hover "school/f1_hover.png"
        focus_mask True
        action [Play("sound", "f1.mp3"), Function(add_nota, "f1")]
    imagebutton:
        idle "school/f#1.png"
        hover "school/f#1_hover.png"
        focus_mask True
        action [Play("sound", "f#1.mp3"), Function(add_nota, "f#1")]
    imagebutton:
        idle "school/g1.png"
        hover "school/g1_hover.png"
        focus_mask True
        action [Play("sound", "g1.mp3"), Function(add_nota, "g1")]
    imagebutton:
        idle "school/g#1.png"
        hover "school/g#1_hover.png"
        focus_mask True
        action [Play("sound", "g#1.mp3"), Function(add_nota, "g#1")]
    imagebutton:
        idle "school/a1.png"
        hover "school/a1_hover.png"
        focus_mask True
        action [Play("sound", "a1.mp3"), Function(add_nota, "a1")]
    imagebutton:
        idle "school/a#1.png"
        hover "school/a#1_hover.png"
        focus_mask True
        action [Play("sound", "a#1.mp3"), Function(add_nota, "a#1")]
    imagebutton:
        idle "school/b1.png"
        hover "school/b1_hover.png"
        focus_mask True
        action [Play("sound", "b1.mp3"), Function(add_nota, "b1")]
    imagebutton:
        idle "school/c2.png"
        hover "school/c2_hover.png"
        focus_mask True
        action [Play("sound", "c2.mp3"), Function(add_nota, "c2")]
    imagebutton:
        idle "school/c#2.png"
        hover "school/c#2_hover.png"
        focus_mask True
        action [Play("sound", "c#2.mp3"), Function(add_nota, "c#2")]
    imagebutton:
        idle "school/d2.png"
        hover "school/d2_hover.png"
        focus_mask True
        action [Play("sound", "d2.mp3"), Function(add_nota, "d2")]
    imagebutton:
        idle "school/d#2.png"
        hover "school/d#2_hover.png"
        focus_mask True
        action [Play("sound", "d#2.mp3"), Function(add_nota, "d#2")]
    imagebutton:
        idle "school/e2.png"
        hover "school/e2_hover.png"
        focus_mask True
        action [Play("sound", "e2.mp3"), Function(add_nota, "e2")]
    imagebutton:
        idle "school/f2.png"
        hover "school/f2_hover.png"
        focus_mask True
        action [Play("sound", "f2.mp3"), Function(add_nota, "f2")]
    imagebutton:
        idle "school/f#2.png"
        hover "school/f#2_hover.png"
        focus_mask True
        action [Play("sound", "f#2.mp3"), Function(add_nota, "f#2")]
    imagebutton:
        idle "school/g2.png"
        hover "school/g2_hover.png"
        focus_mask True
        action [Play("sound", "g2.mp3"), Function(add_nota, "g2")]
    imagebutton:
        idle "school/g#2.png"
        hover "school/g#2_hover.png"
        focus_mask True
        action [Play("sound", "g#2.mp3"), Function(add_nota, "g#2")]
    imagebutton:
        idle "school/a2.png"
        hover "school/a2_hover.png"
        focus_mask True
        action [Play("sound", "a2.mp3"), Function(add_nota, "a2")]
    imagebutton:
        idle "school/a#2.png"
        hover "school/a#2_hover.png"
        focus_mask True
        action [Play("sound", "a#2.mp3"), Function(add_nota, "a#2")]
    imagebutton:
        idle "school/b2.png"
        hover "school/b2_hover.png"
        focus_mask True
        action [Play("sound", "b2.mp3"), Function(add_nota, "b2")]
    

init python:
    def add_nota(nota):
        store.input_song += nota
        if piano_lock == "close":
            if len(store.input_song) == 48:
                if store.input_song == "g#2g#2f#2g#2a2b2a2e2f#2f#2f#2e2f#2g#2a2g#2f#2g#2":
                    store.piano_lock = "open"
                    renpy.play("listok.mp3")
                    renpy.jump("piano_down")
                store.input_song = "" 

label piano_down:
    $ hide_all_ui()
    scene bg piano_down
    $ quest_list[23]["available"] = True
    $ quest_list[22]["done"] = True
    show screen listok
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return 

screen listok:
    imagebutton:
        idle "school/listok.png"
        hover "school/listok_hover.png"
        focus_mask True
        action [Function(add_item_to_inventory, "listok"), Jump("piano")]    

screen back_arrow_to_piano:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("piano")  # Показываем меню выбора    

screen back_arrow_to_school_room:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("piano_class")  # Показываем меню выбора

screen piano_teacher:
    imagebutton:
        idle "school/piano_teacher.png"
        focus_mask True
        if not block_ui:
            hover "school/piano_teacher_hover.png"
            action Jump("piano_teacher_dialog")

label piano_teacher_dialog:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/teacher/2.mp3"
    teacher "Здравствуйте, я могу вам чем-то помочь?"
    jump piano_teacher_menu

label piano_teacher_menu:
    $ stop_dialog()
    menu:
        "Я хотела бы научиться играть на пианино" if i_want_piano_first_time == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/153.mp3"
            Vika "Я хотела бы научиться играть на пианино."
            voice "audio/voices/teacher/3.mp3"
            teacher "Девушка, это школа. школа это учереждение где учатся дети."
            voice "audio/voices/teacher/4.mp3"
            teacher "Я бы согласилась снизить ваш возраст в своих глазах, будь вы хоть немного интеллегентны. Но в любом случае вы не выглядите как завсегдатая этого заведения."
            voice "audio/voices/teacher/5.mp3"
            teacher "Вам больше подходит другое, например на таежной, где я видела вас вчера. Или в полицейском участке, где я видела вас сегодня."
            voice "audio/voices/teacher/6.mp3"
            teacher "В общем не знаю что вам нужно, но вы точно не собираетесь играть на пианино!"
            $ quest_list[21]["done"] = True
            $ quest_list[22]["available"] = True
            $ i_want_piano_first_time = False
            jump piano_teacher_menu
        "Рассказать правду про мента" if i_saw_telegramm == True and i_say_about_ment == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/154.mp3"
            Vika "Вы же Маша, верно?"
            voice "audio/voices/teacher/7.mp3"
            teacher "Для вас, Мария Александровна"
            voice "audio/voices/vika/155.mp3"
            Vika "Странно, а вот тот самый мент из полицейского участка обходится без отчества."
            voice "audio/voices/teacher/8.mp3"
            teacher "Какой мент???"
            voice "audio/voices/vika/156.mp3"
            Vika "А вы много их знаете???"
            voice "audio/voices/vika/157.mp3"
            Vika "Вообще я хотела вас предупредить, он вас использует и кроме как для этого вы ему не нужны."
            voice "audio/voices/teacher/9.mp3"
            teacher "Девочка, я намного опытнее тебя и уж я то разбираюсь в мужчинах. Ты просто не знаешь какой он со мной один на один, даже мой муж не такой..."
            voice "audio/voices/vika/158.mp3"
            Vika "Вы еще и замужем???"
            voice "audio/voices/teacher/10.mp3"
            teacher "Не тебе меня судить, в отличие от моего мужа, Максим самый внимательный и самый лучший любовник."
            voice "audio/voices/vika/159.mp3"
            Vika "Я и не собиралась вас судить, я просто предупреждаю"
            voice "audio/voices/teacher/11.mp3"
            teacher "Ладно, я это проверю, но если ты меня обманываешь, тебе лучше бежать куда подальше"
            voice "audio/voices/vika/160.mp3"
            Vika "Я и так пытаюсь..."
            voice "audio/voices/teacher/12.mp3"
            teacher "Что ты сказала?"
            voice "audio/voices/vika/161.mp3"
            Vika "Да так, ничего, скажите ему что больше не будете делать для него ничего, и он быстро потеряется!!!"
            voice "audio/voices/teacher/13.mp3"
            teacher "Ладно, я сейчас вернусь, не трогай тут ничего."
            $ quest_list[21]["done"] = True
            $ masha_is_here = False
            $ i_want_piano_first_time = False
            $ i_say_about_ment = True
            $ block_ui = False
            $ stop_dialog()
            jump piano_class
        "Спросить про мента" if clara_suck_now == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/162.mp3"
            Vika "Я слышала, что вы все-таки отказались работать на своего любовника."
            voice "audio/voices/teacher/14.mp3"
            teacher "Да, но ты была не права, ему от меня было нужно не только это, он нормально воспринял мои слова и согласился со мной."
            voice "audio/voices/teacher/15.mp3"
            teacher "Сейчас, я пару дней помучаю его, а потом снова приглашу его к себе, и у нас все будет как по новой."
            voice "audio/voices/vika/163.mp3"
            Vika "Он так говорит, потому что боится что вы пожалуетесь, своему мужу, то есть начальнику отдела полиции."
            voice "audio/voices/teacher/16.mp3"
            teacher "А ты откуда знаешь?"
            voice "audio/voices/vika/164.mp3"
            Vika "Я подслушала ваш разговор, когда сидела в этом кабинете."
            voice "audio/voices/teacher/17.mp3"
            teacher "Мда, надо было быть более осторожнее, в любом случае, мой муж тебе не поверит."
            voice "audio/voices/vika/165.mp3"
            Vika "Я не собираюсь сдавать вас вашему мужу, мне только нужно чтоб вы сейчас поехали со мной в полицию, я вам докажу, что ваш Максим вас обманывает."
            voice "audio/voices/teacher/18.mp3"
            teacher "Каким это образом???"
            voice "audio/voices/vika/166.mp3"
            Vika "Он прямо сейчас закрылся в комнате для вещдоков с проституткой"
            voice "audio/voices/teacher/19.mp3"
            teacher "Даже если и так, зачем тебе это нужно?"
            voice "audio/voices/vika/167.mp3"
            Vika "Он шантажирует меня, говорит что посадит за мошенничество в казино, если я не буду работать на него."
            voice "audio/voices/teacher/20.mp3"
            teacher "Подожди так это ты та девушка, которая мухлевала в казино?"
            voice "audio/voices/vika/85.mp3"
            Vika "Да"
            voice "audio/voices/teacher/21.mp3"
            teacher "Можешь расслабиться, у полиции на тебя ничего нет."
            voice "audio/voices/vika/168.mp3"
            Vika "Как?"
            voice "audio/voices/teacher/22.mp3"
            teacher "Мой муж рассказывал мне об этом деле, он обещал уволить Максима, если он не добудет камеры из казино."
            voice "audio/voices/teacher/23.mp3"
            teacher "Но ни одно казино в мире не признается, что у него можно смухлевать, поэтому он ничего не добился."
            voice "audio/voices/teacher/24.mp3"
            teacher "Так что ты можешь спокойно идти и не плести тут чушь."
            voice "audio/voices/vika/169.mp3"
            Vika "Но это правда!!! И чем быстрее вы пойдете, тем больше шансов, что они еще там!!!"
            voice "audio/voices/teacher/25.mp3"
            teacher "Ну хорошо, я пойду если ты правда права, то я добьюсь того, чтоб он получил по заслугам."
            voice "audio/voices/teacher/26.mp3"
            teacher "Но если нет, я расскажу мужу, что ты правда виновна, и тогда ты на самом деле отправишься в тюрьму."
            voice "audio/voices/vika/170.mp3"
            Vika "Идет!"
            jump ment_and_slut
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/teacher/27.mp3"
            teacher "Удачи"
            $ block_ui = False
            $ stop_dialog()
            jump piano_class

label ment_and_slut:
    $ hide_all_ui()
    $ show_hud()
    scene black
    with perehod_diss
    scene bg police_hall
    show masha neutral at Position(xalign=0.8, yalign=1.0)
    play music "zhenskie-stony.mp3" fadeout 1
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/171.mp3"
    Vika "Вот, слышите?"
    voice "audio/voices/teacher/28.mp3"
    teacher "Да, простите меня, я была не права. Я скажу мужу, чтоб посмотрел камеры в этот момент, и да, за шантаж можете не переживать."
    voice "audio/voices/teacher/29.mp3"
    teacher "Когда Максим будет уволен, он не сможет уже ничего сделать вам. Надеюсь он вообще больше ничего никому не сможет сделать."
    voice "audio/voices/teacher/30.mp3"
    teacher "Козел!"
    hide masha neutral
    pause 2.0
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/172.mp3"
    Vika "Это был тяжелый день, надо добраться домой и рассказать все Вите."
    $ polojenie = "police"
    $ quest_list[26]["done"] = True
    $ quest_list[27]["available"] = True
    $ intellect += 1
    $ game_hour += 1
    $ update_game_time()
    $ block_ui = False
    $ stop_dialog()
    jump police_hall



screen back_arrow_to_school_hall:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            if "listok" in inventory_items and masha_and_husband_dialog == False:
                action Jump("masha_and_husband")
            else:
                action Jump("school_hall")

label masha_and_husband:
    $ block_ui = True 
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/Voice1/1.mp3"
    Voice1 "Документы точно где-то тут, мне сообщили что курьер принес их сюда."
    voice "audio/voices/Voice2/1.mp3"
    Voice2 "Вова тут учатся дети, кому твой курьер мог их привести???" 
    voice "audio/voices/Voice1/2.mp3"
    Voice1 "Маша, я начальник полиции, я не могу ошибаться, если я говорю здесь значит здесь"
    voice "audio/voices/Voice2/2.mp3"
    Voice2 "Ты мой муж, ты говоришь своей жене, что кто-то из ее учеников связан с криминалом."
    voice "audio/voices/Voice1/3.mp3" 
    Voice1 "Не факт что ученики, это может быть кто угодно. Ладно, я вернусь сюда позже, когда будет больше информации."
    voice "audio/voices/vika/173.mp3"
    Vika "То есть она изменяет начальнику полиции с его подчиненным???"
    $ intellect += 1
    $ game_hour += 1
    $ update_game_time()
    $ ment_is_here = True
    $ masha_and_husband_dialog = True
    $ block_ui = False
    $ stop_dialog()
    jump piano_class



screen foto_map_point:
    imagebutton:
        idle "foto_map.png"
        xpos 800
        ypos 500
        focus_mask True
        at Transform(zoom=1.3)
        if not block_ui:
            hover "foto_map_hover.png"
            action Jump("foto_studio_vhod")  # Показываем меню выбора

label foto_studio_vhod:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "foto")
    $ polojenie = "foto"
    play music "city.mp3" fadeout 1
    scene bg photo_build
    show screen back_arrow_to_map
    show screen door_to_foto
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen door_to_foto:
    imagebutton:
        idle "foto_studio/door_to_foto.png"
        focus_mask True
        if not block_ui:
            hover "foto_studio/door_to_foto_hover.png"
            action Jump("foto_studio")

label foto_studio:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg foto
    show screen back_arrow_to_foto_studio_vhod
    show screen model
    stop music fadeout 1
    show screen door_to_grim
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen back_arrow_to_foto_studio_vhod:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("foto_studio_vhod")

screen model:
    imagebutton:
        idle "foto_studio/model.png"
        focus_mask True
        if not block_ui:
            hover "foto_studio/model_hover.png"
            if first_model_dialog == True:
                action Jump("model_dialog")
            else:
                action Jump("model_menu")

label model_dialog:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/model/1.mp3"
    model "Здравствуйте, чем я могу помочь?"
    voice "audio/voices/vika/174.mp3"
    Vika "Здравствуйте, я на съемку!"
    voice "audio/voices/model/2.mp3"
    model "Сейчас занято, через пару минут подойдет модель на съемку"
    voice "audio/voices/vika/175.mp3"
    Vika "Да, это я, Клара не сможет и попросила меня подменить её"
    voice "audio/voices/model/3.mp3"
    model "Странно, но окей, гриммерка прямо за моей спиной, можешь там накрасится, в первую очередь сделай что-то вампирское"
    voice "audio/voices/vika/28.mp3"
    Vika "Хорошо"
    $ makeup_level = 1
    $ first_model_dialog = False
    $ block_ui = False
    $ stop_dialog()
    jump foto_studio

label model_menu:
    $ renpy.music.set_pause(True)
    $ block_ui = True
    $ stop_dialog()
    menu:
        "Я накрасилась" if makeup_level == 1:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/176.mp3"
            Vika "Я готова к съемке."
            if hair_color == "black" and lips_color == "5" and eyes_color == "1" and lins_color == "2":
                voice "audio/voices/model/4.mp3"
                model "То что нужно, вставай на хромокей."
                jump syemka
            else:    
                voice "audio/voices/model/5.mp3"
                model "Нет, это не то, что нужно, мне нужен самый вампирский макияж на свете."
                jump model_menu
        "Я готова" if makeup_level == 2:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/176.mp3"
            Vika "Я готова к съемке."
            if hair_color == "green" and lips_color == "6" and eyes_color == "1" and lins_color == "4":
                voice "audio/voices/model/4.mp3"
                model "То что нужно, вставай на хромокей."
                
                jump syemka
            else:    
                voice "audio/voices/model/6.mp3"
                model "Нет, это не то, что нужно, мне нужна ведьма, а не это."
                jump model_menu
        "Я готова сниматься" if makeup_level == 3:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/176.mp3"
            Vika "Я готова к съемке."
            if hair_color == "white" and lips_color == "1" and eyes_color == "5" and lins_color == "3":
                voice "audio/voices/model/4.mp3"
                model "То что нужно, вставай на хромокей."
                
                jump syemka
            else:    
                voice "audio/voices/model/7.mp3"
                model "Нет, это не то, все еще слишком пошло, попробуй еще."
                jump model_menu
        "Готова к съемке" if makeup_level == 4:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/176.mp3"
            Vika "Я готова к съемке."
            if hair_color == "blue" and lips_color == "7" and eyes_color == "1" and lins_color == "1":
                voice "audio/voices/model/4.mp3"
                model "То что нужно, вставай на хромокей."
                
                jump syemka
            else:    
                voice "audio/voices/model/8.mp3"
                model "Нет, это не то, нужно хуже, попробуй еще."
                jump model_menu
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/model/15.mp3"
            model "Давай, буду ждать."
            $ block_ui = False
            $ stop_dialog()
            jump foto_studio

label syemka:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene black
    with perehod_diss
    play sound "snimok.mp3"
    pause 0.5
    play sound "snimok.mp3"
    pause 0.5
    play sound "snimok.mp3"
    pause 0.5
    play sound "snimok.mp3"
    pause 0.1
    play sound "snimok.mp3"
    pause 0.5
    jump next_foto

label next_foto:
    if makeup_level == 1:
        $ _preferences.afm_enable = True 
        voice "audio/voices/model/9.mp3"
        model "Отлично, теперь я хочу видеть в тебе ведьму, справишься?"
        voice "audio/voices/vika/177.mp3"
        Vika "Конечно"
        $ makeup_level = 2
        $ block_ui = False
        $ stop_dialog()
        jump foto_studio
    elif makeup_level == 2:
        $ _preferences.afm_enable = True 
        voice "audio/voices/model/10.mp3"
        model "Отлично, теперь я хочу видеть в тебе что-нибудь невинное, справишься?"
        voice "audio/voices/vika/177.mp3"
        Vika "Конечно"
        $ makeup_level = 3
        $ block_ui = False
        $ stop_dialog()
        jump foto_studio
    elif makeup_level == 3:
        $ _preferences.afm_enable = True 
        voice "audio/voices/model/11.mp3"
        model "Отлично, а теперь наоборот, сделай прям ужасно, как будто ты школьница которая не умеет красится, справишься?"
        voice "audio/voices/vika/177.mp3"
        Vika "Конечно"
        $ makeup_level = 4
        $ block_ui = False
        $ stop_dialog()
        jump foto_studio
    elif makeup_level == 4:
        $ _preferences.afm_enable = True 
        voice "audio/voices/model/12.mp3"
        model "Отлично, я тобой довольна, шикарные получились снимки, можешь умываться."
        voice "audio/voices/vika/178.mp3"
        Vika "А где тут у вас раковина?"
        voice "audio/voices/model/13.mp3"
        model "У нас ее нет, можешь воспользоваться жидкостью для снятия макияжа"
        voice "audio/voices/vika/179.mp3"
        Vika "Я всю потратила на съемку..."
        voice "audio/voices/model/14.mp3"
        model "Ну тогда ничем не могу помочь, придется идти так"
        voice "audio/voices/vika/180.mp3"
        Vika "Блин..."
        $ quest_list[25]["done"] = True
        $ quest_list[26]["available"] = True
        $ game_hour += 2
        $ update_game_time()
        $ masha_is_here = True
        $ ment_is_here = False
        $ clara_suck_now = True
        $ makeup_level = 5
        $ block_ui = False
        $ stop_dialog()
        jump foto_studio


screen door_to_grim:
    imagebutton:
        idle "foto_studio/door_to_grim.png"
        focus_mask True
        if not block_ui:
            hover "foto_studio/door_to_grim_hover.png"
            action Jump("grim_room")

label grim_room:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg grim
    show screen door_to_photo
    show screen miror
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen door_to_photo:
    imagebutton:
        idle "foto_studio/door_to_photo.png"
        focus_mask True
        if not block_ui:
            hover "foto_studio/door_to_photo_hover.png"
            action Jump("foto_studio")

screen miror:
    imagebutton:
        idle "foto_studio/miror.png"
        focus_mask True
        if not block_ui:
            hover "foto_studio/miror_hover.png"
            if "kosmetik" in inventory_items and "brush" in inventory_items:
                action Jump("miror")
            else:
                action Jump("no_kosmetik")

label no_kosmetik:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/181.mp3"
    Vika "Мне пока нечем краситься."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label miror:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg miror
    show screen back_arrow_to_grim_room
    show screen miror_hair
    show screen miror_lips
    show screen miror_lins
    show screen miror_eyes
    show screen hair_pal
    show screen lips_pal
    show screen lins_pal
    show screen eyes_pal
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen miror_hair:
    zorder 1
    if hair_color == "default":
        add "makeup/neutral_hair.png"
    elif hair_color == "black":
        add "makeup/black_hair.png"
    elif hair_color == "white":
        add "makeup/white_hair.png"
    elif hair_color == "green":
        add "makeup/green_hair.png"
    elif hair_color == "blue":
        add "makeup/blue_hair.png"

screen miror_lips:
    zorder 2
    if lips_color == "1":
        add "makeup/lips_1.png"
    elif lips_color == "2":
        add "makeup/lips_2.png"
    elif lips_color == "3":
        add "makeup/lips_3.png"
    elif lips_color == "4":
        add "makeup/lips_4.png"
    elif lips_color == "5":
        add "makeup/lips_5.png"
    elif lips_color == "6":
        add "makeup/lips_6.png"
    elif lips_color == "7":
        add "makeup/lips_7.png"

screen miror_lins:
    zorder 4
    if lins_color == "1":
        add "makeup/lins_1.png"
    elif lins_color == "2":
        add "makeup/lins_2.png"
    elif lins_color == "3":
        add "makeup/lins_3.png"
    elif lins_color == "4":
        add "makeup/lins_4.png"
    elif lins_color == "5":
        add "makeup/lins_5.png"
    elif lins_color == "6":
        add "makeup/lins_6.png"
    elif lins_color == "7":
        add "makeup/lins_7.png"

screen miror_eyes:
    zorder 3
    if eyes_color == "1":
        add "makeup/eyes_1.png"
    elif eyes_color == "2":
        add "makeup/eyes_2.png"
    elif eyes_color == "3":
        add "makeup/eyes_3.png"
    elif eyes_color == "4":
        add "makeup/eyes_4.png"
    elif eyes_color == "5":
        add "makeup/eyes_5.png"
    elif eyes_color == "6":
        add "makeup/eyes_6.png"
    elif eyes_color == "7":
        add "makeup/eyes_7.png"

screen hair_pal:
    add "makeup/hair_back.png"
    imagebutton:
        idle "makeup/hair_3.png"
        focus_mask True
        if not block_ui:
            if "black_colour" in inventory_items:
                action [Function(hide_all_hair, "black"), Function(remove_item_to_inventory, "black_colour")]
            else:
                action Jump("no_colour")
    imagebutton:
        idle "makeup/hair_4.png"
        focus_mask True
        if not block_ui:
            if "white_colour" in inventory_items:
                action [Function(hide_all_hair, "white"), Function(remove_item_to_inventory, "white_colour")]
            else:
                action Jump("no_colour")
    imagebutton:
        idle "makeup/hair_2.png"
        focus_mask True
        if not block_ui:
            if "blue_colour" in inventory_items:
                action [Function(hide_all_hair, "blue"), Function(remove_item_to_inventory, "blue_colour")]
            else:
                action Jump("no_colour")
    imagebutton:
        idle "makeup/hair_1.png"
        focus_mask True
        if not block_ui:
            if "green_colour" in inventory_items:
                action [Function(hide_all_hair, "green"), Function(remove_item_to_inventory, "green_colour")]
            else:
                action Jump("no_colour")

label no_colour:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/182.mp3"
    Vika "У меня нет такой краски!!!"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen lips_pal:
    add "makeup/lips_back.png"
    imagebutton:
        idle "makeup/pal_lips_1.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lips, "1")
    imagebutton:
        idle "makeup/pal_lips_2.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lips, "2")
    imagebutton:
        idle "makeup/pal_lips_3.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lips, "3")
    imagebutton:
        idle "makeup/pal_lips_4.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lips, "4")
    imagebutton:
        idle "makeup/pal_lips_5.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lips, "5")
    imagebutton:
        idle "makeup/pal_lips_6.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lips, "6")
    imagebutton:
        idle "makeup/pal_lips_7.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lips, "7")

screen lins_pal:
    add "makeup/lins_back.png"
    imagebutton:
        idle "makeup/pal_lins_1.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lins, "1")
    imagebutton:
        idle "makeup/pal_lins_2.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lins, "2")
    imagebutton:
        idle "makeup/pal_lins_3.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lins, "3")
    imagebutton:
        idle "makeup/pal_lins_4.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lins, "4")
    imagebutton:
        idle "makeup/pal_lins_5.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lins, "5")
    imagebutton:
        idle "makeup/pal_lins_6.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lins, "6")
    imagebutton:
        idle "makeup/pal_lins_7.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_lins, "7")

screen eyes_pal:
    add "makeup/eyes_back.png"
    imagebutton:
        idle "makeup/pal_eyes_1.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_eyes, "1")
    imagebutton:
        idle "makeup/pal_eyes_2.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_eyes, "2")
    imagebutton:
        idle "makeup/pal_eyes_3.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_eyes, "3")
    imagebutton:
        idle "makeup/pal_eyes_4.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_eyes, "4")
    imagebutton:
        idle "makeup/pal_eyes_5.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_eyes, "5")
    imagebutton:
        idle "makeup/pal_eyes_6.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_eyes, "6")
    imagebutton:
        idle "makeup/pal_eyes_7.png"
        focus_mask True
        if not block_ui:
            action Function(hide_all_eyes, "7")

python early:
    def hide_all_hair(colour_hair):
        global hair_color
        hair_color = colour_hair
        renpy.hide_screen("miror_hair")
        renpy.show_screen("miror_hair")

    def hide_all_lips(colour_lips):
        global lips_color
        lips_color = colour_lips
        renpy.hide_screen("miror_lips")
        renpy.show_screen("miror_lips")
    
    def hide_all_lins(colour_lins):
        global lins_color
        lins_color = colour_lins
        renpy.hide_screen("miror_lins")
        renpy.show_screen("miror_lins")
    
    def hide_all_eyes(colour_eyes):
        global eyes_color
        eyes_color = colour_eyes
        renpy.hide_screen("miror_eyes")
        renpy.show_screen("miror_eyes")


screen back_arrow_to_grim_room:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("grim_room")

screen back_arrow_to_street:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            if i_can_go_out == False:
                action Jump("ne_vihody")
            else:
                action Jump("work")

label ne_vihody:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/ohrana/1.mp3"
    ohrana "Ваш рабочий день ещё не закончен!"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen fishman_map_point:
    imagebutton:
        idle "fishman_map.png"
        xpos 800
        ypos 300
        focus_mask True
        at Transform(zoom=1.3)
        if not block_ui:
            hover "fishman_map_hover.png"
            if makeup_level == 5:
                action Jump("need_bathroom")
            else:
                action Jump("fishman")  # Показываем меню выбора

screen work_map_point:
    imagebutton:
        idle "work_map.png"
        xpos 1030
        ypos 440
        focus_mask True
        at Transform(zoom=1.3)
        if not block_ui:
            hover "work_map_hover.png"
            action Jump("work")  # Показываем меню выбора

label work:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "work")
    $ polojenie = "work"
    play music "city.mp3" fadeout 1
    scene bg work
    show screen emeregen_build
    show screen bluegen_build
    show screen back_arrow_to_map
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen bluegen_build:
    imagebutton:
        idle "day_3/bluegen.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_hover.png"
            action Jump("bluegen_vhod")

label bluegen_vhod:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg bluegen_vhod
    show screen security
    play music "work.mp3" fadeout 1
    if need_fix_lift == True:
        show screen lift
        show screen lift_button
    show screen bluegen_up
    show screen back_arrow_to_street
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label lift_button:
    $ renpy.free_memory()
    $ hide_all_ui()
    if lift_button_open == False:
        scene bg lift_button
        show screen vint_1
        show screen vint_2
    else:
        scene bg lift_button_open
        show screen konec
        if ohrana_say == False:
            $ block_ui = True
            $ start_dialog()
            $ _preferences.afm_enable = True 
            $ renpy.music.set_pause(True)
            voice "audio/voices/ohrana/2.mp3"
            ohrana "А, понятно, провод коротит, надо заизолировать!"
            $ ohrana_say = True
            $ block_ui = False
            $ stop_dialog()
    show screen back_arrow_to_bluegen_vhod
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen konec:
    imagebutton:
        idle "day_3/konec.png"
        focus_mask True
        if not block_ui and default_mouse == "izolenta":
            hover "day_3/konec_hover.png"
            action [SetVariable("lift_button_open", False), Jump("lift_button_Fixed")]

label lift_button_Fixed:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg lift_button
    $ need_fix_lift = False
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/ohrana/3.mp3"
    ohrana "Cпасибо Виктория, можете идти куда захотите, я вас прикрою если что..."
    $ quest_list[30]["done"] = True
    $ edik_in_emergen = True
    $ i_can_go_out = True
    scene bg viskey
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/183.mp3"
    Vika "А это что???"
    voice "audio/voices/ohrana/4.mp3"
    ohrana "Эмм... А это и есть то самое кое-что важное... Но вы же меня не сдадите?"
    voice "audio/voices/vika/184.mp3"
    Vika "Нет, Михаил Петрович, только есть одна просьба..."
    voice "audio/voices/ohrana/5.mp3"
    ohrana "Для вас все что угодно, Виктория"
    voice "audio/voices/vika/185.mp3"
    Vika "Можете отлить мне чуть-чуть этого вашего кое-что... Мне надо... Для опытов."
    voice "audio/voices/ohrana/6.mp3"
    ohrana "Не переживайте, Виктория, я все понимаю, работа у вас трудная... 'Опытов' много..."
    voice "audio/voices/vika/186.mp3"
    Vika "Спасибо большое"
    voice "audio/voices/ohrana/7.mp3"
    ohrana "Это вам спасибо, Виктория"
    $ quest_list[34]["done"] = True
    $ add_item_to_inventory("viskey")
    $ i_know_alcohol = True
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/187.mp3"
    Vika "Удачи вам, Михаил Петрович!!!"
    voice "audio/voices/ohrana/8.mp3"
    ohrana "И вам удачи, Виктория!"
    $ block_ui = False
    $ stop_dialog()
    $ default_mouse = "default"
    $ remove_item_to_inventory("tool")
    jump bluegen_vhod
    



screen back_arrow_to_bluegen_vhod:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("bluegen_vhod")

screen vint_1:
    imagebutton:
        idle "day_3/vint_1.png"
        focus_mask True
        if not block_ui and default_mouse == "tool":
            hover "day_3/vint_1_hover.png"
            action [SetVariable("lift_button_open", True), Jump("lift_button")]

screen vint_2:
    imagebutton:
        idle "day_3/vint_2.png"
        focus_mask True
        if not block_ui and default_mouse == "tool":
            hover "day_3/vint_2_hover.png"
            action [SetVariable("lift_button_open", True), Jump("lift_button")]

screen security:
    imagebutton:
        idle "day_3/security.png"
        focus_mask True
        if not block_ui:
            hover "day_3/security_hover.png"
            action Jump("security_dialog")

label security_dialog:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    if security_first_dialog == True and i_can_go_out == False:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/188.mp3"
        Vika "Здраствуйте Михаил Петрович"
        voice "audio/voices/ohrana/9.mp3"
        ohrana "Здравствуйте, Виктория!"
        voice "audio/voices/vika/189.mp3"
        Vika "Можно я выйду на минуточку?"
        voice "audio/voices/ohrana/10.mp3"
        ohrana "Исключено, Евгений Степанович строго настрого запретил выпускать вас по любому поводу"
        voice "audio/voices/ohrana/11.mp3"
        ohrana "Уж не знаю в чем вы провинились, но приказ есть приказ, поэтому извините, но придется вам подождать до вечера"
        $ security_first_dialog = False
        jump security_menu
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/ohrana/12.mp3"
        ohrana "Да?"
        jump security_menu

label security_menu:
    $ stop_dialog()
    menu:
        "Почему вы такой грустный?" if i_ask_about_sad == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/190.mp3"
            Vika "Вы что-то грустный какой-то, у вас что-то случилось?"
            voice "audio/voices/ohrana/13.mp3"
            ohrana "Да так... Лифт сломался"
            voice "audio/voices/vika/191.mp3"
            Vika "Он же и так не нужен, Евгений Степанович его сделал для 'солидности компании' он даже не едет никуда."
            voice "audio/voices/ohrana/14.mp3"
            ohrana "Я знаю..."
            voice "audio/voices/vika/192.mp3"
            Vika "Тем более он почти каждый день ломается, и его ночью чинят."
            voice "audio/voices/ohrana/15.mp3"
            ohrana "Я знаю, Виктория, я просто оставил в лифте кое-что важное, и оно заблокировалось..."
            voice "audio/voices/vika/193.mp3"
            Vika "Ну что вы, Михаил Петрович, достанем это ваше важное, мне только нужно сходить купить..."
            voice "audio/voices/ohrana/16.mp3"
            ohrana "Оооо, нет, Виктория, если вы почините лифт, можете идти куда хотите."
            voice "audio/voices/ohrana/17.mp3"
            ohrana "Но пока лифт закрыт даже не думайте, что сможете отсюда выйти"
            $ quest_list[30]["available"] = True
            $ need_fix_lift = True
            $ i_ask_about_sad = True
            jump security_menu
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/ohrana/18.mp3"
            ohrana "До свидания, Виктория"
            $ block_ui = False
            $ stop_dialog()
            jump bluegen_vhod


screen lift:
    imagebutton:
        idle "day_3/bluegen_lift.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_lift_hover.png"
            action Jump("lift_monolog")

screen lift_button:
    imagebutton:
        idle "day_3/bluegen_lift_button.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_lift_button_hover.png"
            action Jump("lift_button")

screen bluegen_up:
    imagebutton:
        idle "day_3/bluegen_up.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_up_hover.png"
            action Jump("bluegen_2nd_flat")

label bluegen_2nd_flat:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg bluegen_2nd_flat
    show screen bluegen_2nd_flat_up
    show screen bluegen_2nd_flat_down
    show screen bluegen_2nd_flat_door
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen bluegen_2nd_flat_up:
    imagebutton:
        idle "day_3/bluegen_2nd_flat_up.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_2nd_flat_up_hover.png"
            action Jump("bluegen_3rd_flat")

label bluegen_3rd_flat:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg bluegen_3rd_flat
    show screen bluegen_3rd_flat_down
    show screen bluegen_3rd_flat_door
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen bluegen_2nd_flat_down:
    imagebutton:
        idle "day_3/bluegen_2nd_flat_down.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_2nd_flat_down_hover.png"
            action Jump("bluegen_vhod")

screen bluegen_3rd_flat_down:
    imagebutton:
        idle "day_3/bluegen_3rd_flat_down.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_3rd_flat_down_hover.png"
            action Jump("bluegen_2nd_flat")

screen bluegen_2nd_flat_door:
    imagebutton:
        idle "day_3/bluegen_2nd_flat_door.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_2nd_flat_door_hover.png"
            action Jump("second_doors")

screen bluegen_3rd_flat_door:
    imagebutton:
        idle "day_3/bluegen_3rd_flat_door.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_3rd_flat_door_hover.png"
            action Jump("third_doors")

label third_doors:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ polojenie = "work"
    scene bg bluegen_3rd_flat_doors
    show screen bluegen_3rd_flat_doors_4
    show screen bluegen_3rd_flat_doors_5
    show screen bluegen_3rd_flat_doors_main
    show screen back_arrow_to_bluegen_3rd_flat
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen bluegen_3rd_flat_doors_4:
    imagebutton:
        idle "day_3/bluegen_3rd_flat_doors_4.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_3rd_flat_doors_4_hover.png"
            if nachalnik_first_dialog == True:
                action Jump("need_nachalnik")
            else:
                action Jump("it")

label it:
    $ renpy.free_memory()
    $ polojenie = "IT"
    $ hide_all_ui()
    scene bg it
    show screen it
    show screen back_arrow_to_third_doors
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen back_arrow_to_third_doors:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("third_doors")


screen it:
    imagebutton:
        idle "day_3/it.png"
        focus_mask True
        if not block_ui:
            hover "day_3/it_hover.png"
            action Jump("it_dialog")

label it_dialog:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    if it_first_dialog == True:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/30.mp3"
        Vika "Привет"
        voice "audio/voices/it/1.mp3"
        it "Привет."
        voice "audio/voices/vika/194.mp3"
        Vika "Ты кто? я тебя здесь раньше не видела."
        voice "audio/voices/it/2.mp3"
        it "Я сисадмин, весь интернет на мне, любое твое действие проходит через меня"
        voice "audio/voices/vika/195.mp3"
        Vika "Понятно почему я тебя тут раньше не видела, ты сидишь и смотришь что делают лаборанты за своими компами."
        voice "audio/voices/it/3.mp3"
        it "Да, и за твоими козинами в маркетплейсах на 3 мульта тоже."
        voice "audio/voices/vika/196.mp3"
        Vika "Чего???"
        voice "audio/voices/it/4.mp3"
        it "А нечего сидеть на работе и выбирать себе шмотки. Тем более через рабочий wi-fi."
        voice "audio/voices/vika/197.mp3"
        Vika "Насрать, в общем мне нужно от тебя кое-что. Ты не знаешь ничего о напитке который постоянно пьет босс?"
        voice "audio/voices/it/5.mp3"
        it "Мне некогда объяснять про напитки человеку, который просто принеси да подай, у меня своя работа есть."
        voice "audio/voices/vika/198.mp3"
        Vika "Я могу тебе помочь, босс сказал, чтоб я помогала всем, и принесла ему его любимый напиток."
        voice "audio/voices/it/6.mp3"
        it "Чем ты можешь мне помочь?"
        voice "audio/voices/vika/199.mp3"
        Vika "Да чем угодно!!!"
        voice "audio/voices/it/7.mp3"
        it "Вали ка ты отсюда, я меняю for на list comprehension для ускорения скрипта, а ты мне мешаешь..."
        voice "audio/voices/vika/200.mp3"
        Vika "Вот ты валенок, list comprehension нужен только для читаемости кода."
        voice "audio/voices/it/8.mp3"
        it "Да? Ты шаришь за питон?"
        voice "audio/voices/vika/201.mp3"
        Vika "Конечно, что там шарить, сидишь, заносишь карточки в базу данных бункера, ничего сложного"
        voice "audio/voices/it/9.mp3"
        it "Какой бункер, какие карточки?"
        voice "audio/voices/vika/202.mp3"
        Vika "Не важно, я пошла наливать напиток боссу, я же просто принеси - подай..."
        voice "audio/voices/it/10.mp3"
        it "Стой, он постоянно наливает виски в безалкогольные напитки, это все что я знаю"
        $ quest_list[34]["available"] = True
        voice "audio/voices/vika/203.mp3"
        Vika "И где мне взять виски?"
        voice "audio/voices/it/11.mp3"
        it "Сходи и купи, в чем проблема?"
        voice "audio/voices/vika/204.mp3"
        Vika "Меня не выпускают из здания..."
        voice "audio/voices/it/12.mp3"
        it "Ну у меня нету, но могу тебе дать отвертку, вырубишь охранника и свалишь..."
        voice "audio/voices/it/13.mp3"
        it "Только если ты реально докажешь, что шаришь за питон, просто поговори со мной немного..."
        voice "audio/voices/vika/205.mp3"
        Vika "Ага, сейчас, раньше я была тупой, а тут все, растаял, да и зачем мне твоя отвертка..."
        $ quest_list[35]["available"] = True
        $ it_first_dialog = False
        jump it_menu
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/it/14.mp3"
        it "Да?"
        jump it_menu

label it_menu:
    $ stop_dialog()
    menu:
        "Как ты влазил ко мне в телефон" if i_ask_about_clients == True and phone_is_brocken == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/206.mp3"
            Vika "Ты говорил, что ты влазил ко мне в телефон?"
            voice "audio/voices/it/15.mp3"
            it "Да, я ко всем влазил, но только ради прикола, никакую личную информацию я там не смотрел, честно"
            voice "audio/voices/vika/207.mp3"
            Vika "Да это не важно, там все равно ничего нет, мне интересно как ты это сделал?"
            voice "audio/voices/it/16.mp3"
            it "Легко, нашёл открытый порт — значит, включён ADB. Через эксплойт в Qualcomm-драйвере получил RCE."
            voice "audio/voices/vika/208.mp3"
            Vika "Понятно, а ты можешь в телефон к боссу залезть?"
            voice "audio/voices/it/17.mp3"
            it "Я в данный момент этим занят..."
            voice "audio/voices/vika/209.mp3"
            Vika "Серьезно? И что он там делает?"
            voice "audio/voices/it/18.mp3"
            it "В данный момент он ждет ответа от Марго Робби, которой отправил свои гениталии и написал..."
            voice "audio/voices/it/19.mp3"
            it "Приглашаю вас на съемки фильма 'Секс с уолл-стрит' и прилагаю фото главного актера."
            voice "audio/voices/vika/210.mp3"
            Vika "Хах, а что у него вообще на телефоне есть?"
            voice "audio/voices/it/20.mp3"
            it "Я не могу посмотреть, пока он пользуется своим телефоном, думаю он что-то заподозрит, если у него начнут закрываться и открываться приложения."
            voice "audio/voices/vika/211.mp3"
            Vika "Ну давай подождем."
            voice "audio/voices/it/21.mp3"
            it "Я бы не стал ждать пока она ему ответит."
            voice "audio/voices/vika/212.mp3"
            Vika "А ты можешь сделать так как будто ему кто-то написал?"
            voice "audio/voices/it/22.mp3"
            it "Легко!"
            voice "audio/voices/vika/213.mp3"
            Vika "+79215438968, пиши что-то типо, все время думаю о тебе с нашей встречи, приезжай прямо сейчас..."
            voice "audio/voices/it/23.mp3"
            it "Написал. Так. Подожди. тут уже есть от него сообщения, это номер проститутки? Откуда ты это знаешь?"
            voice "audio/voices/vika/214.mp3"
            Vika "Эмм, ну..."
            voice "audio/voices/it/24.mp3"
            it "Ты уже залезала к нему в телефон? Через что вскрывала?"
            voice "audio/voices/vika/215.mp3"
            Vika "Да так, не важно, все равно не смогла основательно залезть..."
            voice "audio/voices/it/25.mp3"
            it "Он ей ответил..."
            voice "audio/voices/vika/216.mp3"
            Vika "Что там?"
            voice "audio/voices/it/26.mp3"
            it "Говорит: 'Я еще не сделал то о чем ты просила, но если тебе не терпится рассчитаться, я сейчас приеду'"
            voice "audio/voices/vika/217.mp3"
            Vika "Странно, подожди, а она получит от него это сообщение?"
            voice "audio/voices/it/27.mp3"
            it "Нет, я успел заблокировать отправку."
            voice "audio/voices/vika/218.mp3"
            Vika "Хорошо, тогда как только сядет за руль можешь шариться, потом расскажешь что интересного нашел."
            voice "audio/voices/it/28.mp3"
            it "Хорошо!"
            $ game_hour += 1
            $ intellect += 1
            $ update_game_time()
            $ phone_is_brocken = True
            jump it_menu
        "Что ты там говорил про отвертку?" if need_fix_lift == True and vitya_can_help == True and i_take_tool == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/219.mp3"
            Vika "Что ты там говорил про отвертку?"
            voice "audio/voices/it/29.mp3"
            it "Просто поговоришь со мной и получишь!"
            voice "audio/voices/vika/220.mp3"
            Vika "Хорошо, только не долго."
            voice "audio/voices/it/30.mp3"
            it "Допустим, нужно сделать контекстный менеджер для SQL-транзакции. Как правильно его реализовать?"
            voice "audio/voices/vitya/54.mp3"
            vitya "Используй @contextmanager из contextlib"
            jump it_first_question
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/it/31.mp3"
            it "Заходи еще!"
            $ block_ui = False
            $ stop_dialog()
            jump it

label it_first_question:
    $ stop_dialog()
    menu:
        "from contextlib import context_manager":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/it/32.mp3"
            it "Неверно. похоже ты только вайбкодишь, приходи когда подучишься."
            $ block_ui = False
            $ stop_dialog()
            jump it

        "from contextlib import contextmanager":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/it/33.mp3"
            it "Хмм, ладно, тогда следующий вопрос."
            voice "audio/voices/it/34.mp3"
            it "Как правильно сделать декоратор для мемоизации функции?"
            voice "audio/voices/vitya/55.mp3"
            vitya "Используй functools.lru_cache"
            jump it_second_question
        
        "from contextlib import context":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/it/32.mp3"
            it "неверно, похоже ты только вайбкодишь, приходи когда подучишься"
            $ block_ui = False
            $ stop_dialog()
            jump it

label it_second_question:
    $ stop_dialog()
    menu:
        "from functools import lrucache":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/it/32.mp3"
            it "неверно, похоже ты только вайбкодишь, приходи когда подучишься"
            $ block_ui = False
            $ stop_dialog()
            jump it

        "from functools import lru_cache":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/it/33.mp3"
            it "Хмм, ладно, тогда следующий вопрос"
            voice "audio/voices/it/35.mp3"
            it "Как правильно объявить асинхронный генератор?"
            voice "audio/voices/vitya/56.mp3"
            vitya "Используй async def с yield"
            jump it_third_question

        "from functools import cache":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/it/32.mp3"
            it "неверно, похоже ты только вайбкодишь, приходи когда подучишься"
            $ block_ui = False
            $ stop_dialog()
            jump it

label it_third_question:
    $ stop_dialog()
    menu:
        "async def gen(): yield 1":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/it/36.mp3"
            it "Вот это да, первый раз вижу такую умную девушку, что тебе там надо было, отвертку?"
            voice "audio/voices/vika/221.mp3"
            Vika "Да, пора сделать что обещал."
            voice "audio/voices/it/37.mp3"
            it "Держи!"
            $ i_take_tool = True
            $ add_item_to_inventory("tool")
            $ quest_list[35]["done"] = True
            voice "audio/voices/it/38.mp3"
            it "Не хочешь остаться и заказать еду?"
            voice "audio/voices/vitya/57.mp3"
            vitya "Скажи ему чтоб шел куда подальше"
            voice "audio/voices/vika/222.mp3"
            Vika "Нет, спасибо, я замужем."
            voice "audio/voices/it/39.mp3"
            it "А, ну ладно, все равно, будет время, заходи поболтаем еще"
            voice "audio/voices/vika/223.mp3"
            Vika "Как нибудь... Может быть... Ладно, я пошла."
            $ intellect += 1
            $ game_hour += 1
            $ update_game_time()
            play sound "sbros.mp3"
            $ block_ui = False
            $ stop_dialog()
            jump it

        "def async gen(): yield 1":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/it/32.mp3"
            it "неверно, похоже ты только вайбкодишь, приходи когда подучишься"
            $ stop_dialog()
            jump it

        "async gen(): yield 1":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/it/32.mp3"
            it "неверно, похоже ты только вайбкодишь, приходи когда подучишься"
            $ stop_dialog()
            jump it


screen bluegen_3rd_flat_doors_5:
    imagebutton:
        idle "day_3/bluegen_3rd_flat_doors_5.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_3rd_flat_doors_5_hover.png"
            if nachalnik_first_dialog == True:
                action Jump("need_nachalnik")
            else:
                action Jump("laboratoria_5")

label laboratoria_5:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg kabinet_5
    show screen laborant_5
    show screen tea_table
    show screen back_arrow_to_third_doors
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen laborant_5:
    imagebutton:
        idle "day_3/laborant_5.png"
        focus_mask True
        if not block_ui:
            hover "day_3/laborant_5_hover.png"
            action Jump("laborant_5_dialog")

label laborant_5_dialog:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    if laborant_5_first_dialog == True:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/224.mp3"
        Vika "Привет, Артём!"
        voice "audio/voices/artem/1.mp3"
        artem "Привет Вик, я ждал когда ты зайдешь"
        voice "audio/voices/vika/225.mp3"
        Vika "Да, и почему же?"
        voice "audio/voices/artem/2.mp3"
        artem "Да просто задолбало все, от босса до айтишника, может ты мне поможешь?"
        voice "audio/voices/vika/226.mp3"
        Vika "Чем же?"
        voice "audio/voices/artem/3.mp3"
        artem "Ну босс уже всем разтрындел, что ты собираешься уйти в эмерген и я подумал, может ты поможешь мне, устроишь собеседование?"
        voice "audio/voices/vika/227.mp3"
        Vika "И ты туда же? Я понимаю что тут плохо, меня вон он вообще обвинил во всём чём только можно."
        voice "audio/voices/vika/228.mp3"
        Vika "Он даже заставил мне принести ему какой-то напиток, а что это за напиток он мне не сказал, я должна это узнать у тебя!"
        voice "audio/voices/vika/229.mp3"
        Vika "Но даже при этом я не перехожу в эмерген, я просто переезжаю в другой город, и уже там буду искать работу."
        voice "audio/voices/artem/4.mp3"
        artem "Меня просто уже все достало, этот айтишник по приказу босса сменил все пароли на наших компьютерах."
        voice "audio/voices/artem/5.mp3"
        artem "И ладно бы просто сменил и раздал пароли, вместо этого он написал задачку на стрикере и прикрепил к экрану"
        voice "audio/voices/artem/6.mp3"
        artem "Может ты поможешь мне, ты по-любому уже все решила, ведь ты умная"
        voice "audio/voices/vika/230.mp3"
        Vika "С чего это ты взял, что я умная?"
        voice "audio/voices/artem/7.mp3"
        artem "Ну была бы ты тупая, тебя бы не взяли в эмерген"
        voice "audio/voices/vika/231.mp3"
        Vika "Да не брали меня ни в какой эмерген, и не решала я никакие задачки, у меня ни то что компьютер, у меня целый кабинет отобрали!!!"
        voice "audio/voices/artem/8.mp3"
        artem "Ладно, не хочешь, не помогай, но тогда ты не узнаешь от меня ничего про напиток..."
        voice "audio/voices/vika/232.mp3"
        Vika "Я правда ни разу даже ни была в эмергене!!!"
        voice "audio/voices/artem/9.mp3"
        artem "Да, да, да, любимый напиток босса - вода из унитаза, можешь прямо сейчас нести"
        voice "audio/voices/vika/233.mp3"
        Vika "Ладно, давай я попробую посмотреть что у тебя с паролем."
        $ quest_list[31]["available"] = True
        $ stop_dialog()
        jump artem_password
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/artem/10.mp3"
        artem "Да?"
        jump laborant_5_dialog_menu


label artem_password:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg artem_pass
    $ artem_pass = renpy.input("Введите пароль:")
    if artem_pass == "024":
        jump correct_artem_pass
    else:
        $ _preferences.afm_enable = True 
        "Пароль неверный, попробуйте еще раз"
        jump artem_password

label correct_artem_pass:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg kabinet_5
    $ show_hud()
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/artem/11.mp3"
    artem "Ну вот, видишь, я же говорил что ты умная"
    $ quest_list[31]["done"] = True
    voice "audio/voices/artem/12.mp3"
    artem "Босс пьет чай."
    voice "audio/voices/vika/234.mp3"
    Vika "Какой?"
    voice "audio/voices/artem/13.mp3"
    artem "Не знаю, видимо оба, кофе он точно терпеть не может, у нас уже пол года стоит целый пакет"
    voice "audio/voices/artem/14.mp3"
    artem "Слушай, я если честно не верю, что ты воруешь у эдика проекты, скорее это он у тебя ворует"
    voice "audio/voices/vika/235.mp3"
    Vika "Лааадно, пускай будет так."
    $ intellect += 1
    $ game_hour += 1
    $ update_game_time()
    $ i_know_tea = True
    $ laborant_5_first_dialog = False
    jump laborant_5_dialog_menu

label laborant_5_dialog_menu:
    $ stop_dialog()
    menu:
        "Ты можешь починить лифт?" if lift_button_open == True and i_say_about_lift == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/236.mp3"
            Vika "Ты можешь починить лифт?"
            voice "audio/voices/artem/15.mp3"
            artem "Зачем он тебе? Он умеет только открывать и закрывать двери, он никуда не ездит."
            voice "audio/voices/vika/237.mp3"
            Vika "Это долго объяснять, а там все просто, я уже открыла крышку, осталось только заизолировать провод."
            voice "audio/voices/artem/16.mp3"
            artem "Это быстро, но если я буду отвлекаться на то чтоб помогать всем подряд, я не буду делать свою работу"
            voice "audio/voices/vika/238.mp3"
            Vika "Вообще-то это я постоянно всем помогаю и поэтому не успеваю со своей работой, и тебе я помогаю в том числе..."
            voice "audio/voices/artem/17.mp3"
            artem "Ну а я не хочу быть таким как ты..."
            voice "audio/voices/vika/239.mp3"
            Vika "Все, просто иди и чини лифт, я сделаю тут все за тебя, только скажи над чем ты работаешь."
            voice "audio/voices/artem/18.mp3"
            artem "Microswella congesta, надо их размножить..."
            voice "audio/voices/vika/240.mp3"
            Vika "Ясно, иди чини лифт, я сделаю."
            $ quest_list[32]["available"] = True
            $ i_say_about_lift = True
            $ block_ui = False
            $ stop_dialog()
            jump microscope
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/artem/19.mp3"
            artem "Заходи еще"
            $ block_ui = False
            $ stop_dialog()
            jump laboratoria_5

label microscope:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg microscope
    show screen microscope
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

init python:
    def add_bacteria(number):
        bacteria.append(number)
         


screen microscope:
    imagebutton:
        idle "day_3/microscope/microscope_button.png"
        focus_mask True
        if not block_ui:
            hover "day_3/microscope/microscope_button_hover.png"
            if default_mouse == "default":
                action Jump("bacterii")
            elif bacteri_number == 1:
                action [Function(add_bacteria, 1), SetVariable("default_mouse", "default")]
            elif bacteri_number == 2:
                action [Function(add_bacteria, 2), SetVariable("default_mouse", "default")]
            elif bacteri_number == 3:
                action [Function(add_bacteria, 3), SetVariable("default_mouse", "default")]
            elif bacteri_number == 4:
                action [Function(add_bacteria, 4), SetVariable("default_mouse", "default")]
            elif bacteri_number == 5:
                action [Function(add_bacteria, 5), SetVariable("default_mouse", "default")]
            elif bacteri_number == 6:
                action [Function(add_bacteria, 6), SetVariable("default_mouse", "default")]
    imagebutton:
        idle "day_3/microscope/table_button.png"
        focus_mask True
        if not block_ui:
            action SetVariable("default_mouse", "default")
    imagebutton:
        idle "day_3/microscope/bacteria_info_small.png"
        focus_mask True
        if not block_ui:
            hover "day_3/microscope/bacteria_info_small_hover.png"
            action Show("bacteria_info_big")
    imagebutton:
        idle "day_3/microscope/clear_button.png"
        focus_mask True
        if not block_ui:
            hover "day_3/microscope/clear_button_hover.png"
            action SetVariable("bacteria", [])
    imagebutton:
        idle "day_3/microscope/probirka_1.png"
        focus_mask True
        if not block_ui:
            hover "day_3/microscope/probirka_1_hover.png"
            action [SetVariable("default_mouse", "blue_bakteria"), SetVariable("bacteri_number", 1)]
    imagebutton:
        idle "day_3/microscope/probirka_2.png"
        focus_mask True
        if not block_ui:
            hover "day_3/microscope/probirka_2_hover.png"
            action [SetVariable("default_mouse", "green_bakteria"), SetVariable("bacteri_number", 2)]
    imagebutton:
        idle "day_3/microscope/probirka_3.png"
        focus_mask True
        if not block_ui:
            hover "day_3/microscope/probirka_3_hover.png"
            action [SetVariable("default_mouse", "orange_bakteria"), SetVariable("bacteri_number", 3)]
    imagebutton:
        idle "day_3/microscope/probirka_4.png"
        focus_mask True
        if not block_ui:
            hover "day_3/microscope/probirka_4_hover.png"
            action [SetVariable("default_mouse", "orange_bakteria"), SetVariable("bacteri_number", 4)]
    imagebutton:
        idle "day_3/microscope/probirka_5.png"
        focus_mask True
        if not block_ui:
            hover "day_3/microscope/probirka_5_hover.png"
            action [SetVariable("default_mouse", "red_bakteria"), SetVariable("bacteri_number", 5)]
    imagebutton:
        idle "day_3/microscope/probirka_6.png"
        focus_mask True
        if not block_ui:
            hover "day_3/microscope/probirka_6_hover.png"
            action [SetVariable("default_mouse", "red_bakteria"), SetVariable("bacteri_number", 6)]

screen bacteria_info_big:
    modal True
    add "day_3/microscope/bacteria_info_big.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("bacteria_info_big")

label bacterii:
    $ renpy.free_memory()
    $ hide_all_ui()
    if len(bacteria) == 1:
        if 1 in bacteria:
            scene bg samka_small
        elif 2 in bacteria:
            scene bg samec_small
        elif 3 in bacteria:
            scene bg samka_big
        elif 4 in bacteria:
            scene bg samec_big
        elif 5 in bacteria:
            scene bg samec_medium
        elif 6 in bacteria:
            scene bg samka_medium
    elif len(bacteria) == 2 and 6 in bacteria and 2 in bacteria:
        scene bg bacteria_win
        $ block_ui = True
        $ start_dialog()
        $ _preferences.afm_enable = True 
        $ renpy.music.set_pause(True)
        voice "audio/voices/vika/241.mp3"
        Vika "Ну вот мои родные, теперь вы - семья."
        voice "audio/voices/artem/20.mp3"
        artem "Я пытался починить твой лифт, но меня ударило током!!!"
        $ quest_list[32]["done"] = True
        jump i_do_microscope
    else:
        scene bg empty
        if len(bacteria) > 0:
            $ block_ui = True
            $ start_dialog()
            $ _preferences.afm_enable = True 
            $ renpy.music.set_pause(True)
            voice "audio/voices/vika/242.mp3"
            Vika "Ну вот, все умерли..."
            $ block_ui = False
            $ stop_dialog()
        $ bacteria = []
    show screen back_arrow_to_microscope
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label i_do_microscope:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg kabinet_5
    show screen laborant_5
    show screen tea_table
    show screen back_arrow_to_third_doors
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/243.mp3"
    Vika "Так я же тебе сказала, что его надо заизолировать..."
    voice "audio/voices/artem/21.mp3"
    artem "Я пытался, даже изоленту нашел, а когда обматывал, меня ударило"
    voice "audio/voices/vika/244.mp3"
    Vika "Ты не смог сделать простую вещь, в то время как я сделала за тебя всю работу, почти..."
    voice "audio/voices/artem/22.mp3"
    artem "Ну почти это не считается, так что мы квиты, а если тебе что-то не нравится, можешь пойти и сама попробовать"
    voice "audio/voices/vika/245.mp3"
    Vika "Лааааадно, тебе осталось только расселить их, давай сюда свою изоленту."
    $ add_item_to_inventory("izolenta")
    $ intellect += 1
    $ game_hour += 1
    $ update_game_time()
    $ _preferences.afm_enable = True 
    voice "audio/voices/artem/23.mp3"
    artem "Держи, только будь аккуратнее"
    voice "audio/voices/vika/246.mp3"
    Vika "Да да да..."
    $ block_ui = False
    $ stop_dialog()
    jump laboratoria_5


screen back_arrow_to_microscope:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("microscope")


screen tea_table:
    imagebutton:
        idle "day_3/tea_table.png"
        focus_mask True
        if not block_ui:
            hover "day_3/tea_table_hover.png"
            if quest_list[29]["done"] == True:
                if "napitok" in inventory_items:
                    action Jump("repeat_napitok")
                else:
                    action Jump("tea_table")
            else:
                action Jump("i_dont_know_recept")

label i_dont_know_recept:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/247.mp3"
    Vika "Я еще не знаю полный рецепт напитка."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return
    

label tea_table:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg teatable
    show screen green_tea
    show screen black_tea   
    show screen cup
    show screen coffe
    show screen teapot
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen coffe:
    imagebutton:
        idle "day_3/coffe.png"
        focus_mask True
        if not block_ui:
            hover "day_3/coffe_hover.png"
            if default_mouse == "default":
                action SetVariable("default_mouse", "cofe")

screen green_tea:
    imagebutton:
        idle "day_3/green_tea.png"
        focus_mask True
        if not block_ui:
            hover "day_3/green_tea_hover.png"
            if default_mouse == "default":    
                action SetVariable("default_mouse", "green_tea")

screen black_tea:
    imagebutton:
        idle "day_3/black_tea.png"
        focus_mask True
        if not block_ui:
            hover "day_3/black_tea_hover.png"
            if default_mouse == "default":        
                action SetVariable("default_mouse", "black_tea")

screen teapot:
    imagebutton:
        idle "day_3/teapot.png"
        focus_mask True
        if not block_ui:
            hover "day_3/teapot_hover.png"
            action [SetVariable("cup", "full"), Hide("cup"), Show("cup")]


label laboratoria_5_tea:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/248.mp3"
    Vika "Ну, вроде неплохой напиток получился"
    $ add_item_to_inventory("napitok")
    $ block_ui = False
    $ stop_dialog()
    jump laboratoria_5

label repeat_napitok:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/249.mp3"
    Vika "Пожалуй сделаю ка я напиток заного!"
    $ clear_napitok()
    $ block_ui = False
    $ stop_dialog()
    jump tea_table

label cup_is_empty:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/250.mp3"
    Vika "Чтобы нести напиток боссу, надо хотя бы налить туда воды!"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

init python:
    def napitok_Full(ingr):
        napitok.append(ingr)
        if ingr == "viskey":
            add_item_to_inventory("viskey")
        elif ingr == "sugars":
            add_item_to_inventory("sugars")
    
    def clear_napitok():
        global napitok, cup, inventory_items
        napitok = []
        cup = "empty"
        remove_item_to_inventory("napitok")

screen cup:
    imagebutton:
        if cup == "empty":
            idle "day_3/cup.png"
            focus_mask True
            if not block_ui:
                hover "day_3/cup_hover.png"
                if default_mouse == "default":
                    action Jump("cup_is_empty")
                elif default_mouse == "black_tea":
                    action [Function(napitok_Full, "black_tea"), SetVariable("default_mouse", "default")]
                elif default_mouse == "green_tea":
                    action [Function(napitok_Full, "green_tea"), SetVariable("default_mouse", "default")]
                elif default_mouse == "cofe":
                    action [Function(napitok_Full, "cofe"), SetVariable("default_mouse", "default")]
                elif default_mouse == "viskey":
                    action [Function(napitok_Full, "viskey"), SetVariable("default_mouse", "default")]
                elif default_mouse == "sugars":
                    action [Function(napitok_Full, "sugars"), SetVariable("default_mouse", "default")]
        else:
            idle "day_3/cup_full.png"
            focus_mask True
            if not block_ui:
                hover "day_3/cup_full_hover.png"
                if default_mouse == "default":
                    action Jump("laboratoria_5_tea")
                elif default_mouse == "black_tea":
                    action [Function(napitok_Full, "black_tea"), SetVariable("default_mouse", "default")]
                elif default_mouse == "green_tea":
                    action [Function(napitok_Full, "green_tea"), SetVariable("default_mouse", "default")]
                elif default_mouse == "cofe":
                    action [Function(napitok_Full, "cofe"), SetVariable("default_mouse", "default")]
                elif default_mouse == "viskey":
                    action [Function(napitok_Full, "viskey"), SetVariable("default_mouse", "default")]
                elif default_mouse == "sugars":
                    action [Function(napitok_Full, "sugars"), SetVariable("default_mouse", "default")]

screen bluegen_3rd_flat_doors_main:
    imagebutton:
        idle "day_3/bluegen_3rd_flat_doors_main.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_3rd_flat_doors_main_hover.png"
            if phone_is_brocken == True:
                action Jump("kabinet_nachalnika_empty")
            else:
                action Jump("kabinet_nachalnika")


label kabinet_nachalnika:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg kabinet_nachalnika
    show screen nachalnik
    show screen nachalnik_yaschik
    show screen back_arrow_to_third_doors
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label kabinet_nachalnika_empty:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg kabinet_nachalnika_empty
    show screen nachalnik_yaschik_empty
    show screen back_arrow_to_third_doors
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen nachalnik:
    imagebutton:
        idle "day_3/nachalnik.png"
        focus_mask True
        if not block_ui:
            hover "day_3/nachalnik_hover.png"
            action Jump("nachalnik_dialog")

label nachalnik_dialog:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    if nachalnik_first_dialog == True:
        $ _preferences.afm_enable = True 
        voice "audio/voices/nachalnik/8.mp3"
        nachalnik "Башкова Башкова..."
        voice "audio/voices/vika/251.mp3"
        Vika "Что?"
        voice "audio/voices/nachalnik/9.mp3"
        nachalnik "Не стыдно тебе?"
        voice "audio/voices/vika/252.mp3"
        Vika "За что? Вы сами меня уволили, я же сказала!"
        voice "audio/voices/nachalnik/10.mp3"
        nachalnik "Я все знаю, Башкова! Чем тебе не угодила наша компания? Мы чайный стол сотрудникам поставили, на работу по субботам довозим..."
        voice "audio/voices/vika/253.mp3"
        Vika "О чем вы вообще?"
        voice "audio/voices/nachalnik/11.mp3"
        nachalnik "А ты такую свинью подкладываешь, Эдик работал над этими проектами столько времени, а ты взяла и продала его..."
        voice "audio/voices/vika/254.mp3"
        Vika "Я не понимаю!!!"
        voice "audio/voices/nachalnik/12.mp3"
        nachalnik "Не придуривайся, я тебе сказал что все знаю"
        voice "audio/voices/nachalnik/13.mp3"
        nachalnik "Да, у нас зарплата чуть меньше чем у них, но зато у нас соц пакет есть, чай там, на работу по субботам там..."
        voice "audio/voices/nachalnik/14.mp3"
        nachalnik "В общем хрен ты будешь у них работать, хрен я подпишу твое заявление и к проектам ты теперь хрен подойдешь, будешь полы мыть..."
        voice "audio/voices/nachalnik/15.mp3"
        nachalnik "Кабинет я у тебя уже отобрал, сегодня с утра до вечера ты прислуживаешь всем, принеси и подай, и чтоб раньше 22:00 с работы не уходила"
        voice "audio/voices/nachalnik/16.mp3"
        nachalnik "Я лично сказал охраннику, чтоб он не выпускал тебя из здания, а после рабочего дня обыскивал прежде чем выпустить..."
        $ i_can_go_out = False
        voice "audio/voices/vika/255.mp3"
        Vika "Вы мне объясните вообще что тут происходит?"
        voice "audio/voices/nachalnik/17.mp3"
        nachalnik "Ты прекрасно знаешь, что любые проекты над которыми работает Эдик, перед самым выпуском эти зеленые твари выпускают открытие в мир в перед него..."
        voice "audio/voices/nachalnik/18.mp3"
        nachalnik "Я долго искал кто ворует, и наконец нашел..."
        voice "audio/voices/nachalnik/19.mp3"
        nachalnik "Сегодня утром я нашел на 2 этаже пропуск в эмерген..."
        voice "audio/voices/vika/256.mp3"
        Vika "На нем написано что это мой пропуск???"
        voice "audio/voices/nachalnik/20.mp3"
        nachalnik "Нееет, там какая-то другая бабёнка, но ты думаешь, что Евгений Степанович дурак... А я не дурак, я все знаю, Башкова!"
        if hair_color == "green":
            voice "audio/voices/nachalnik/21.mp3"
            nachalnik "Ты сидишь тут с зелеными волосами, это их цвет..."
        else:
            voice "audio/voices/nachalnik/22.mp3"
            nachalnik "Я видел как ты красилась в зеленый, это их цвет..."
        voice "audio/voices/nachalnik/23.mp3"
        nachalnik "Ты собралась переезжать в питер, в их главный офис??? Думаешь они возьмут тебя на работу? На должность главной воровки проектов???"
        voice "audio/voices/vika/257.mp3"
        Vika "Я не ворую никакие проекты, и вообще, откуда вы знаете про питер?"
        voice "audio/voices/nachalnik/24.mp3"
        nachalnik "Я все знаю, Башкова, все... Ты сама за все время работы не выпустила ни одного проекта..."
        voice "audio/voices/nachalnik/25.mp3"
        nachalnik "В общем пошла вон отсюда, и делай все, что тебе говорят, но сначала, принеси мне мой напиток"
        $ napitok_quest = True
        voice "audio/voices/vika/258.mp3"
        Vika "Какой еще напиток???"
        voice "audio/voices/nachalnik/26.mp3"
        nachalnik "МОЙ. ЛЮБИМЫЙ. НАПИТОК. Все в компании это знают, если бы ты не бегала так часто к этим зеленым придуркам, то тоже бы знала"
        voice "audio/voices/nachalnik/27.mp3"
        nachalnik "Я тебе больше ничего говорить не собираюсь, если не знаешь, иди и спрашивай у остальных, может тебе кто-то скажет"
        voice "audio/voices/nachalnik/28.mp3"
        nachalnik "Только на километр не подходи к кабинету Эдика, и к своему кабинету тоже... Прости, бывшему кабинету... А теперь пошла вон отсюда."
        $ quest_list[28]["done"] = True
        $ quest_list[36]["available"] = True
        $ quest_list[29]["available"] = True
        $ game_hour += 1
        $ update_game_time()
        $ nachalnik_first_dialog = False
        $ block_ui = False
        $ stop_dialog()
        jump kabinet_nachalnika
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/nachalnik/29.mp3"
        nachalnik "ДА!?"
        jump nachalnik_menu

label nachalnik_menu:
    $ stop_dialog()
    menu:
        "Я принесла вам напиток" if "napitok" in inventory_items:
            $ start_dialog()
            if len(napitok) == 3 and "black_tea" in napitok and "sugars" in napitok and "viskey" in napitok:
                $ _preferences.afm_enable = True 
                voice "audio/voices/vika/259.mp3"
                Vika "Я принесла вам напиток."
                voice "audio/voices/nachalnik/30.mp3"
                nachalnik "Давай посмотрим"
                $ remove_item_to_inventory("napitok")
                $ remove_item_to_inventory("viskey")
                $ remove_item_to_inventory("sugars")
                $ quest_list[36]["done"] = True
                voice "audio/voices/nachalnik/31.mp3"
                nachalnik "Ну вот Башкова, хоть на что-то ты годишься"
                voice "audio/voices/nachalnik/32.mp3"
                nachalnik "Что бы еще тебе приказать? Может ты девочку мне вызовешь? Хотя нет, это тебе нельзя доверять, пшла вон отсюда, займись чем-то полезным"
                $ intellect += 1
                $ game_hour += 1
                $ update_game_time()
                $ i_know_about_sluts = True
                $ block_ui = False
                $ stop_dialog()
                jump kabinet_nachalnika
            else:
                $ _preferences.afm_enable = True 
                voice "audio/voices/vika/259.mp3"
                Vika "Я принесла вам напиток"
                voice "audio/voices/nachalnik/30.mp3"
                nachalnik "Давай посмотрим"
                voice "audio/voices/nachalnik/33.mp3"
                nachalnik "Это отвратительно, никак не то, что я пью!!! Иди и принеси нормальный!"
                $ block_ui = False
                $ stop_dialog()
                jump kabinet_nachalnika
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/nachalnik/34.mp3"
            nachalnik "Иди."
            $ block_ui = False
            $ stop_dialog()
            jump kabinet_nachalnika

screen nachalnik_yaschik:
    imagebutton:
        idle "day_3/nachalnik_yaschik.png"
        focus_mask True
        if not block_ui:
            hover "day_3/nachalnik_yaschik_hover.png"
            action Jump("he_is_here")

label he_is_here:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/260.mp3"
    Vika "Я не могу сделать этого пока он тут."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return


screen nachalnik_yaschik_empty:
    imagebutton:
        idle "day_3/nachalnik_yaschik_empty.png"
        focus_mask True
        if not block_ui:
            hover "day_3/nachalnik_yaschik_empty_hover.png"
            action Jump("nachalnik_yaschik")

label nachalnik_yaschik:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg nachalnik_yaschik
    if keys_is_taken == False:
        show screen keys_2_lab
    if id_is_taken == False:
        show screen emeregen_id
    show screen back_arrow_to_kabinet_nachalnika
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen emeregen_id:
    imagebutton:
        idle "day_3/emeregen_id.png"
        focus_mask True
        if not block_ui:
            hover "day_3/emeregen_id_hover.png"
            action Jump("take_id")

screen keys_2_lab:
    imagebutton:
        idle "day_3/keys_2_lab.png"
        focus_mask True
        if not block_ui:
            hover "day_3/keys_2_lab_hover.png"
            action Jump("take_keys")

label take_keys:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/261.mp3"
    Vika "Эдик на столько мечтает о Сашином кабинете, что у него даже на брелке двойка!"
    $ add_item_to_inventory("keys_2_lab")
    $ block_ui = False
    $ stop_dialog()
    hide screen keys_2_lab
    $ keys_is_taken = True
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label take_id:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/262.mp3"
    Vika "Схожу хотя бы посмотрю что у вас там в этом эмергене!"
    $ add_item_to_inventory("propusk")
    $ block_ui = False
    $ stop_dialog()
    hide screen emeregen_id
    $ id_is_taken = True
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen back_arrow_to_kabinet_nachalnika:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("kabinet_nachalnika_empty")

label need_nachalnik:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/263.mp3"
    Vika "Сначала мне нужно к начальнику!"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label no_enter:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/264.mp3"
    Vika "Мне запретили сюда заходить!"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen back_arrow_to_bluegen_3rd_flat:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("bluegen_3rd_flat")


label second_doors:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg bluegen_2nd_flat_doors
    show screen bluegen_2nd_flat_doors_1
    show screen bluegen_2nd_flat_doors_2
    show screen bluegen_2nd_flat_doors_3
    show screen back_arrow_to_bluegen_2nd_flat
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen bluegen_2nd_flat_doors_1:
    imagebutton:
        idle "day_3/bluegen_2nd_flat_doors_1.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_2nd_flat_doors_1_hover.png"
            if nachalnik_first_dialog == True:
                action Jump("need_nachalnik")
            else:
                action Jump("no_enter")

screen bluegen_2nd_flat_doors_2:
    imagebutton:
        idle "day_3/bluegen_2nd_flat_doors_2.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_2nd_flat_doors_2_hover.png"
            if nachalnik_first_dialog == True:
                action Jump("need_nachalnik")
            else:
                action Jump("laboratoria_2")

label laboratoria_2:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg laboratoria_2
    show screen laborant_2
    show screen back_arrow_to_bluegen_2nd_flat_doors
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen laborant_2:
    imagebutton:
        idle "day_3/laborant_2.png"
        focus_mask True
        if not block_ui:
            hover "day_3/laborant_2_hover.png"
            action Jump("laborant_2_dialog")

label laborant_2_dialog:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    if laborant_2_dialog_first_time == True:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/265.mp3"
        Vika "Ариночка привет!!!"
        voice "audio/voices/arina/1.mp3"
        arina "Привет подставщица!!!"
        voice "audio/voices/vika/266.mp3"
        Vika "Почему подставщица?"
        voice "audio/voices/arina/2.mp3"
        arina "Ну из-за тебя же тут босс все перевернул вчера!"
        voice "audio/voices/vika/267.mp3"
        Vika "Да я сама в шоке, навалил на меня сегодня с утра всякого, вот теперь хожу всякой фигней занимаюсь"
        voice "audio/voices/arina/3.mp3"
        arina "Ну, так или иначе, наш с тобой секретный проект был экстренно уничтожен."
        voice "audio/voices/vika/268.mp3"
        Vika "Это ты про слеш фанфик про босса с эдиком?"
        voice "audio/voices/arina/4.mp3"
        arina "Именно!"
        voice "audio/voices/vika/269.mp3"
        Vika "Ничего страшного, все у меня в голове."
        voice "audio/voices/arina/5.mp3"
        arina "Как и у меня. Так же он перевернул весь кабинет, подпортил несколько рабочих проектов. В общем ничего важного."
        $ laborant_2_dialog_first_time = False
        jump laborant_2_menu
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/arina/23.mp3"
        arina "Да?"
        jump laborant_2_menu

label laborant_2_menu:
    $ stop_dialog()
    menu:
        "Что с моим кабинетом?" if i_say_about_kabinet == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/270.mp3"
            Vika "Ты была в моем кабинете? Там наверное все еще хуже?"
            voice "audio/voices/arina/6.mp3"
            arina "Да, там конечно нужно прибраться, но не переживай я тебе помогу, тем более он у тебя там ничего не нашел."
            voice "audio/voices/arina/7.mp3"
            arina "Он сразу ворвался как ворвался в кабинет, устроил там такой беспорядок, что сам в нем потерялся."
            voice "audio/voices/vika/271.mp3"
            Vika "Наверное мне не надо помогать с уборкой..."
            voice "audio/voices/arina/8.mp3"
            arina "Ты наврятли там сама справишься, тебе точно нужна помощь, так что не изображай вежливость!"
            voice "audio/voices/vika/272.mp3"
            Vika "Да я не об этом, если все и дальше так же пойдет, то у меня нет кабинета, он его отобрал"
            voice "audio/voices/vika/273.mp3"
            Vika "Так что пусть там убирается тот, кому достанется этот кабинет."
            voice "audio/voices/arina/9.mp3"
            arina "Это еще кому? На работу никто не устраивается, мы тут работаем в пятером, кому отдавать кабинет?"
            voice "audio/voices/vika/274.mp3"
            Vika "Не знаю..."
            voice "audio/voices/arina/10.mp3"
            arina "Так, подожди, а если так дальше не пойдет?"
            voice "audio/voices/vika/275.mp3"
            Vika "Ну тогда... Я уезжаю в питер..."
            voice "audio/voices/arina/11.mp3"
            arina "Так это правда, что толстяк про тебя говорил???"
            voice "audio/voices/vika/276.mp3"
            Vika "Нет, из всего того бреда только питер правда, честно."
            voice "audio/voices/arina/12.mp3"
            arina "А чего это тебя туда понесло?"
            voice "audio/voices/vika/277.mp3"
            Vika "Да задолбалась я в этом уренгое, каждый день что-то не так, муж в айти, ему все равно где жить, а я не хочу здесь больше оставаться."
            voice "audio/voices/arina/13.mp3"
            arina "Ясно. В общем кидаешь меня."
            voice "audio/voices/vika/278.mp3"
            Vika "Ну частично, я буду писать..."
            voice "audio/voices/arina/14.mp3"
            arina "Да ладно тебе, не бери в голову я единственная тут кто желает тебе счастья, так что живи спокойно."
            $ i_say_about_kabinet = True
            jump laborant_2_menu
        "Спросить про напиток" if i_know_sugar == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/279.mp3"
            Vika "Ты случайно не знаешь, что за такой особый напиток пьет наш босс?"
            voice "audio/voices/arina/15.mp3"
            arina "Толи чай то ли кофе, не знаю, но могу сказать, что он постоянно таскает у меня сахар."
            voice "audio/voices/vika/280.mp3"
            Vika "А можно я у тебя его тоже возьму?"
            voice "audio/voices/arina/16.mp3"
            arina "Мы же с тобой его вместе покупали, зачем ты спрашиваешь? Только есть одно но..."
            voice "audio/voices/vika/281.mp3"
            Vika "Какое?"
            voice "audio/voices/arina/17.mp3"
            arina "Когда босс тут все переворачивал, надписи с коробок послетали, теперь я не знаю где реагент, а где сахар."
            voice "audio/voices/arina/18.mp3"
            arina "Если угадаешь где из шести коробок сахар, то бери конечно, если не угадаешь, тоже бери."
            voice "audio/voices/vika/282.mp3"
            Vika "Добавить реагент в чай?"
            voice "audio/voices/arina/19.mp3"
            arina "Ну он не умрет конечно, но в туалет сбегать может, хотя с его весом я думаю, что ему для эффекта всю коробку надо съесть."
            voice "audio/voices/vika/283.mp3"
            Vika "А они прям вообще не отличаются?"
            voice "audio/voices/arina/20.mp3"
            arina "На вид ничем, только весом, реагент весит 2 грамма, а сахар - 3"
            voice "audio/voices/arina/21.mp3"
            arina "Там конечно есть весы, но после погрома не думаю, что они взвесят что-то больше одного раза, но можешь попробовать."
            voice "audio/voices/vika/284.mp3"
            Vika "Спасибо"
            $ quest_list[33]["available"] = True
            $ block_ui = False
            $ stop_dialog()
            jump sugar_boxes
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/arina/22.mp3"
            arina "Заглядывай!"
            $ block_ui = False
            $ stop_dialog()
            jump laboratoria_2

label sugar_boxes:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg vesi
    show screen ves_button
    show screen sbros_button
    show screen resoult_button
    show screen box_1
    show screen box_2
    show screen box_3
    show screen box_4
    show screen box_5
    show screen box_6
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

init python:
    sugar_positions = []  # Список для хранения позиций сахара
    max_sugar = 36
    ves_sugar = []        # Максимальное количество кусков
    
    def sugar_ves(number_box):
        if len(sugar_positions) >= max_sugar:
            renpy.jump("dostatochno")
            return
            
        if "Sugar" not in box_take:
            store.box_take[number_box] = True 
            if sum(store.box_take[1:7]) >= 3:       # Если все коробки 1-6 = True
                store.box_take[number_box] = "Sugar"
                store.correct_box = number_box
        
        # Рассчитываем позицию в сетке 6x6
        row = len(sugar_positions) // 6  # Номер строки (0-5)
        col = len(sugar_positions) % 6   # Номер колонки (0-5)
        
        # Базовые координаты и размеры
        start_x = 500
        start_y = 350
        spacing = 30  # Расстояние между кусками
        
        # Вычисляем позицию
        x_pos = start_x + col * spacing
        y_pos = start_y + row * spacing
        
        sugar_positions.append((x_pos, y_pos))
        ves_sugar.append(store.box_take[number_box])
        renpy.show_screen("sugar_vesi")
    
    def reset_box_take():
        store.box_take = [False] * len(store.box_take)
        store.sugar_positions = []
        store.ves_sugar = [] 
        store.correct_box = None
        store.can_ves = 0
        renpy.hide_screen("show_ves_text")
        renpy.show_screen("sugar_vesi")
    
    def vzvesit():
        store.can_ves = 1
        ves = 0  # Обнуляем вес перед расчетом
    
        for item in ves_sugar:
            if item == "Sugar":
                ves += 3
            else:
                ves += 2
    
    # Показываем текст с весом на экране
        renpy.show_screen(
            "show_ves_text",  # Название экрана для отображения текста
            text=f"Вес: {ves} г",  # Текст с рассчитанным весом
            xpos=500,  # Координата X (можно настроить)
            ypos=662   # Координата Y (можно настроить)
        )
        renpy.jump("ves")


label ves:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/285.mp3"
    Vika "Хммм и в какой же коробке сахар..."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return


        
screen show_ves_text(text, xpos, ypos):
    text text:
        xpos xpos
        ypos ypos
        size 42
        color "#000000"  # Белый цвет (можно изменить)
        outlines [(1, "#000000", 0, 0)]  # Черная обводка для лучшей читаемости

screen sugar_vesi():
    # Показываем все изображения сахара из сохраненных позиций
    for i, (x, y) in enumerate(sugar_positions):
        add "icon/sugar.png":
            xpos x
            ypos y
        
label dostatochno:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/286.mp3"
    Vika "уже слишком много кубиков, мне хватит одного"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen sbros_button:
    imagebutton:
        idle "day_3/sbros_button.png"
        focus_mask True
        if not block_ui:
            hover "day_3/sbros_button_hover.png"
            action Function(reset_box_take)

screen resoult_button:
    imagebutton:
        idle "day_3/resoult_button.png"
        focus_mask True
        if not block_ui:
            hover "day_3/resoult_button_hover.png"
            action Jump("resoult_menu")

label resoult_menu:
    $ block_ui = True
    menu:
        "Сахар в коробке номер 1":
            if store.correct_box == 1:
                jump win_sugar
            else:
                jump lose_sugar
        "Сахар в коробке номер 2":
            if store.correct_box == 2:
                jump win_sugar
            else:
                jump lose_sugar
        "Сахар в коробке номер 3":
            if store.correct_box == 3:
                jump win_sugar
            else:
                jump lose_sugar
        "Сахар в коробке номер 4":
            if store.correct_box == 4:
                jump win_sugar
            else:
                jump lose_sugar
        "Сахар в коробке номер 5":
            if store.correct_box == 5:
                jump win_sugar
            else:
                jump lose_sugar
        "Сахар в коробке номер 6":
            if store.correct_box == 6:
                jump win_sugar
            else:
                jump lose_sugar

label win_sugar:
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/287.mp3"
    Vika "Да, это 100%% сахар"
    $ quest_list[33]["done"] = True
    $ intellect += 1
    $ game_hour += 1
    $ update_game_time()
    $ add_item_to_inventory("sugars")
    $ i_know_sugar = True
    $ block_ui = False
    $ stop_dialog()
    jump laboratoria_2

label lose_sugar:
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/288.mp3"
    Vika "Нет, похоже что это не сахар"
    $ block_ui = False
    $ stop_dialog()
    jump sugar_boxes


screen ves_button:
    imagebutton:
        idle "day_3/ves_button.png"
        focus_mask True
        if not block_ui and store.can_ves != 1:
            hover "day_3/ves_button_hover.png"
            action Function(vzvesit)




screen box_1:
    imagebutton:
        idle "day_3/box_1.png"
        focus_mask True
        if not block_ui:
            hover "day_3/box_1_hover.png"
            action Function(sugar_ves, 1)

screen box_2:
    imagebutton:
        idle "day_3/box_2.png"
        focus_mask True
        if not block_ui:
            hover "day_3/box_2_hover.png"
            action Function(sugar_ves, 2)

screen box_3:
    imagebutton:
        idle "day_3/box_3.png"
        focus_mask True
        if not block_ui:
            hover "day_3/box_3_hover.png"
            action Function(sugar_ves, 3)

screen box_4:
    imagebutton:
        idle "day_3/box_4.png"
        focus_mask True
        if not block_ui:
            hover "day_3/box_4_hover.png"
            action Function(sugar_ves, 4)

screen box_5:
    imagebutton:
        idle "day_3/box_5.png"
        focus_mask True
        if not block_ui:
            hover "day_3/box_5_hover.png"
            action Function(sugar_ves, 5)

screen box_6:
    imagebutton:
        idle "day_3/box_6.png"
        focus_mask True
        if not block_ui:
            hover "day_3/box_6_hover.png"
            action Function(sugar_ves, 6)


screen back_arrow_to_laborant2:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("laboratoria_2")

screen back_arrow_to_bluegen_2nd_flat_doors:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("second_doors")




screen bluegen_2nd_flat_doors_3:
    imagebutton:
        idle "day_3/bluegen_2nd_flat_doors_3.png"
        focus_mask True
        if not block_ui:
            hover "day_3/bluegen_2nd_flat_doors_3_hover.png"
            if door_3_is_closet == True:
                if nachalnik_first_dialog == True:
                    action Jump("need_nachalnik")
                elif director_first_dialog == False:
                    if default_mouse == "keys_2_lab":
                        action [SetVariable("door_3_is_closet", False), SetVariable("default_mouse", "default"), Jump("edik_room")]
                    else:
                        action Jump("zaperto")                     
                else:
                    action Jump("no_enter")
            elif door_3_is_closet == False:
                action Jump("edik_room")

label edik_room:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg edik_room
    show screen edik_skaf
    show screen back_arrow_to_bluegen_2nd_flat_doors
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen edik_skaf:
    imagebutton:
        idle "day_3/edik_skaf.png"
        focus_mask True
        if not block_ui and "project" not in inventory_items:
            hover "day_3/edik_skaf_hover.png"
            action Jump("edik_skaf")

screen back_arrow_to_edik_room:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("edik_room")

init python:
    def take_project(number):
        global project_taken
        add_item_to_inventory("project")
        project_taken = number

screen papka_1:
    imagebutton:
        idle "day_3/papka_1.png"
        focus_mask True
        if not block_ui:
            hover "day_3/papka_1_hover.png"
            action [Function(take_project, 1), Jump("edik_room1")]

screen papka_2:
    imagebutton:
        idle "day_3/papka_2.png"
        focus_mask True
        if not block_ui:
            hover "day_3/papka_2_hover.png"
            action [Function(take_project, 2), Jump("edik_room1")]

screen papka_3:
    imagebutton:
        idle "day_3/papka_3.png"
        focus_mask True
        if not block_ui:
            hover "day_3/papka_3_hover.png"
            action [Function(take_project, 3), Jump("edik_room1")]

screen papka_4:
    imagebutton:
        idle "day_3/papka_4.png"
        focus_mask True
        if not block_ui:
            hover "day_3/papka_4_hover.png"
            action [Function(take_project, 4), Jump("edik_room1")]

screen papka_5:
    imagebutton:
        idle "day_3/papka_5.png"
        focus_mask True
        if not block_ui:
            hover "day_3/papka_5_hover.png"
            action [Function(take_project, 5), Jump("edik_room1")]

screen papka_6:
    imagebutton:
        idle "day_3/papka_6.png"
        focus_mask True
        if not block_ui:
            hover "day_3/papka_6_hover.png"
            action [Function(take_project, 6), Jump("edik_room1")]

label edik_room1:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/289.mp3"
    Vika "Надеюсь что это то что нужно"
    $ block_ui = False
    $ stop_dialog()
    jump edik_room


label edik_skaf:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg edik_skaf
    show screen papka_1
    show screen papka_2
    show screen papka_3
    show screen papka_4
    show screen papka_5
    show screen papka_6
    show screen back_arrow_to_edik_room
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return


label zaperto:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/290.mp3"
    Vika "Заперто"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return


screen back_arrow_to_bluegen_2nd_flat:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("bluegen_2nd_flat")

screen emeregen_build:
    imagebutton:
        idle "day_3/emeregen.png"
        focus_mask True
        if not block_ui:
            hover "day_3/emeregen_hover.png"
            if edik_in_emergen == True:
                action Jump("emeregen_vhod_with_edik")
            else:
                action Jump("emeregen_vhod")

label emeregen_vhod_with_edik:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg emeregen_vhod_with_edik
    $ show_hud()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/edik/1.mp3"
    edik "Да где же он..."
    voice "audio/voices/vika/291.mp3"
    Vika "Эдик???"
    voice "audio/voices/edik/2.mp3"
    edik "Вика??? Что ты тут делаешь?"
    voice "audio/voices/vika/292.mp3"
    Vika "А ты что тут делаешь?"
    voice "audio/voices/edik/3.mp3"
    edik "Я? эммм..."
    voice "audio/voices/vika/293.mp3"
    Vika "То есть я пол дня слушаю какая я плохая, как я у тебя проекты ворую!!! А ты стоишь тут возле их входа и даже не можешь внятно ответить что ты тут делаешь???"
    voice "audio/voices/edik/4.mp3"
    edik "Я никогда не говорил что ты воруешь у меня проекты."
    voice "audio/voices/vika/294.mp3"
    Vika "Я знаю что ты не говорил, этот придурок сам себе напридумывал все это!!!"
    voice "audio/voices/edik/5.mp3"
    edik "Тихо, я воровал эти проекты, только не ори так."
    voice "audio/voices/vika/295.mp3"
    Vika "Ты воровал проекты??? У себя? Что ты несешь?"
    voice "audio/voices/edik/6.mp3"
    edik "Да не у себя, а отсюда... У меня тут девушка работает..."
    voice "audio/voices/vika/296.mp3"
    Vika "Ага, а чего ты тогда здесь трешься а не к ней идешь..."
    voice "audio/voices/edik/7.mp3"
    edik "Потому что я ходил сюда по ее пропуску, а сейчас он куда-то делся, я его вчера в карман джинс клал..."
    voice "audio/voices/vika/297.mp3"
    Vika "Я правильно понимаю что ты воровал проекты в эмергене, но ты на столько никчемный, что не смог выпустить их быстрее?"
    voice "audio/voices/edik/8.mp3"
    edik "Да, да, все так, только не ори пожалуйста"
    voice "audio/voices/vika/298.mp3"
    Vika "И ты деже не знаешь где потерял свой пропуск?"
    voice "audio/voices/edik/9.mp3"
    edik "Да, я клал его в карман джинсов на работе, если я его там и выронил - это очень плохо..."
    voice "audio/voices/vika/299.mp3"
    Vika "Так ты его там и выронил, его босс уже нашел и теперь обвиняет меня в том что я не делала"
    voice "audio/voices/edik/10.mp3"
    edik "Все, это конец, у него есть ключи от моего кабинета, если он зайдет в туда, он все найдет..."
    voice "audio/voices/vika/300.mp3"
    Vika "Не бойся, не зайдет, он слишком сильно уверен в том что он прав. Пока..."
    voice "audio/voices/edik/11.mp3"
    edik "Но ты же меня не сдашь?"
    voice "audio/voices/vika/301.mp3"
    Vika "Я бы сдала, но для меня же это все равно ничего не решит, я придумаю что-нибудь другое..."
    voice "audio/voices/edik/12.mp3"
    edik "Ну хоть так, тогда просто скажи, что я заболел..."
    voice "audio/voices/vika/302.mp3"
    Vika "Какой чай он пьет?! Ты точно знаешь!"
    voice "audio/voices/edik/13.mp3"
    edik "Черный, черный, только прикрой меня!"
    $ quest_list[29]["done"] = True
    $ quest_list[37]["available"] = True
    $ game_hour += 1
    $ update_game_time()
    $ i_know_black_tea = True
    $ edik_in_emergen = False
    $ block_ui = False
    $ stop_dialog()
    jump emeregen_vhod


    

label emeregen_vhod:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg emeregen_vhod
    show screen turniket
    play music "work.mp3" fadeout 1
    show screen back_arrow_to_street
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen turniket:
    imagebutton:
        idle "day_3/turniket.png"
        focus_mask True
        if not block_ui:
            hover "day_3/turniket_hover.png"
            if default_mouse == "propusk":
                action Jump("can_enter")
            else:
                action Jump("need_id")

label need_id:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    $ _preferences.afm_enable = True 
    voice "audio/voices/turniket/1.mp3"
    turniket "Чтобы пройти, приложите пропуск"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label can_enter:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/turniket/2.mp3"
    turniket "Добро пожаловать в Эмерген, Анна"
    $ quest_list[37]["done"] = True
    $ add_item_to_inventory("propusk")
    $ block_ui = False
    $ stop_dialog()
    $ default_mouse = "default"
    jump emeregen_hall

label emeregen_hall:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg emeregen_hall
    show screen sekretarsha
    show screen back_arrow_to_emeregen_vhod
    if i_can_talk_with_director == True:
        show screen emeregen_director_door
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen sekretarsha:
    imagebutton:
        idle "day_3/sekretarsha.png"
        focus_mask True
        if not block_ui:
            hover "day_3/sekretarsha_hover.png"
            action Jump("sekretarsha_dialog")

label sekretarsha_dialog:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    if i_can_talk_with_director == False:
        $ _preferences.afm_enable = True 
        voice "audio/voices/sekretarsha/1.mp3"
        sekretarsha "Здраствуйте, вы находитесь в приемной директора компании Эмерген"
        voice "audio/voices/vika/303.mp3"
        Vika "Здраствуйте, мне нужно срочно к директору."
        voice "audio/voices/sekretarsha/2.mp3"
        sekretarsha "Алина Эдуардовна сейчас не принимает, вы можете записаться на послезавтра на..."
        voice "audio/voices/vika/304.mp3"
        Vika "Мне очень нужно, возможно это касается безопастности вашей компании!"
        voice "audio/voices/sekretarsha/3.mp3"
        sekretarsha "Ну хорошо, сейчас я спрошу."
        voice "audio/voices/alina/1.mp3"
        alina "Я все слышала, пусть заходит."
        voice "audio/voices/sekretarsha/4.mp3"
        sekretarsha "Проходите"
        $ i_can_talk_with_director = True
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/sekretarsha/5.mp3"
        sekretarsha "Вы можете спокойно проходить к директору."
    $ block_ui = False
    $ stop_dialog()
    jump emeregen_hall

screen back_arrow_to_emeregen_vhod:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("emeregen_vhod")

screen back_arrow_to_emeregen_hall:
    imagebutton:
        idle "back_idle.png"
        xpos 1700
        ypos 568
        focus_mask True
        at Transform(zoom=0.3)
        if not block_ui:
            hover "back_hover.png"
            action Jump("emeregen_hall")

screen emeregen_director_door:
    imagebutton:
        idle "day_3/emeregen_director_door.png"
        focus_mask True
        if not block_ui:
            hover "day_3/emeregen_director_door_hover.png"
            action Jump("emeregen_director")

label emeregen_director:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg emeregen_director
    show screen back_arrow_to_emeregen_hall
    show screen emeregen_director
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen emeregen_director:
    imagebutton:
        idle "day_3/emeregen_director.png"
        focus_mask True
        if not block_ui:
            hover "day_3/emeregen_director_hover.png"
            action Jump("director_dialog")

label director_dialog:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    if director_first_dialog == True:
        $ _preferences.afm_enable = True 
        voice "audio/voices/alina/2.mp3"
        alina "Здравствуйте, и что же такое угрожает моей компании?"
        voice "audio/voices/vika/305.mp3"
        Vika "Ну в общем у вас есть сотрудница, Анна Ковальски, её парень постоянно приходит к ней на работу, а заодно и ворует проекты над которыми работают ваши сотрудники."
        voice "audio/voices/alina/3.mp3"
        alina "Давайте по порядку, Анна Ковальски у нас работает, но откуда вам это известно?"
        voice "audio/voices/vika/306.mp3"
        Vika "Я работаю в компании вашего конкурента 'Bluegen'"
        voice "audio/voices/alina/4.mp3"
        alina "Конкурента? Ну ну, дальше"
        voice "audio/voices/vika/307.mp3"
        Vika "Ну так вот, мое руководство обвиняет меня в том, что я ворую проекты у своего коллеги и продаю вам."
        voice "audio/voices/vika/308.mp3"
        Vika "А на самом деле это он ворует их у вас, просто он на столько никчемный, что не успевает запатентовать его раньше чем ваша компания."
        voice "audio/voices/alina/5.mp3"
        alina "Вы же понимаете, что если это правда, то я уволю свою сотрудницу и подам в суд на компанию в которой вы работаете."
        voice "audio/voices/vika/309.mp3"
        Vika "Мне все равно на эту компанию, я до всей этой ситуации вообще увольнялась от них, а сейчас мой босс отказывается меня увольнять."
        voice "audio/voices/alina/6.mp3"
        alina "Ну хорошо, но мне для юристов, нужны хоть какие-то доказательства."
        voice "audio/voices/vika/310.mp3"
        Vika "Вот, у меня есть пропуск через ваш турникет!"
        voice "audio/voices/alina/7.mp3"
        alina "Пропуск это не улика против вашей компании, это улика против вас, потому что вы могли его украсть чтоб попасть на закрытую территорию"
        voice "audio/voices/alina/8.mp3"
        alina "Но можете оставить его пока себе, как соберете весомые доказательства, воспользуйтесь им так же как и сегодня"
        voice "audio/voices/vika/311.mp3"
        Vika "Хорошо, думаю я скоро уже вернусь."
        $ quest_list[38]["available"] = True
        $ game_hour += 1
        $ update_game_time()
        $ director_first_dialog = False
        jump director_menu
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/alina/9.mp3"
        alina "Да?"
        jump director_menu

label director_menu:
    $ stop_dialog()
    menu:
        "Я принесла доказательства" if "project" in inventory_items:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/312.mp3"
            Vika "Вот ваши доказательства!"
            if project_taken == 2:
                voice "audio/voices/alina/10.mp3"
                alina "Хммм, это действительно наш проект, Проект 'Феникс-X', тут все наши печати и даже моя подпись"
                voice "audio/voices/alina/11.mp3"
                alina "Ну чтож, спасибо вам, я думаю, что могу предложить вам место в нашей компании, мы ценим честных сотрудников"
                voice "audio/voices/vika/313.mp3"
                Vika "Я срадостью, но есть несколько проблем... Меня не хотят увольнять..."
                voice "audio/voices/alina/12.mp3"
                alina "За это не переживайте, я подниму видео с камер и передам юристам эти документы, ваш уже бывший начальник сделает так, как будто вы никогда там не работали"
                voice "audio/voices/vika/314.mp3"
                Vika "Но есть еще одна проблема, я завтра планировала переехать в Санкт-Петербург"
                voice "audio/voices/alina/13.mp3"
                alina "Это совершенно не проблема, у нас там главная лаборатория, так что с моей рекомендацией думаю вас туда устроят."
                voice "audio/voices/vika/315.mp3"
                Vika "Тогда я с радостью!!!"
                voice "audio/voices/alina/14.mp3"
                alina "И еще одна просьба..."
                voice "audio/voices/vika/316.mp3"
                Vika "Все что угодно."
                voice "audio/voices/alina/15.mp3"
                alina "Думаю что после этого проишествия мы должны признать, что у нас проблемы с безопасностью, но мы не можем просто нанять охранника."
                voice "audio/voices/alina/16.mp3"
                alina "Эмерген - это высокотехнологичная компания, так что не могли бы вы переманить вместе с вами вашего IT специалиста?"
                voice "audio/voices/vika/317.mp3"
                Vika "Думаю у меня есть идея получше..."
                voice "audio/voices/alina/17.mp3"
                alina "Ну если вы знаете другого человека, который мог бы решить эту проблему, то мы будем вам и ему благодарны."
                voice "audio/voices/alina/18.mp3"
                alina "200 тысяч рублей в месяц его устроят?"
                voice "audio/voices/vika/318.mp3"
                Vika "Вполне..."
                voice "audio/voices/alina/19.mp3"
                alina "Тогда мы свяжемся с вами через несколько дней, как вы обустроитесь, а ваш человек может обратиться в любой наш офис."
                voice "audio/voices/vika/319.mp3"
                Vika "Договорились!"
                $ quest_list[38]["done"] = True
                $ quest_list[39]["available"] = True
                $ intellect += 1
                $ game_hour += 1
                $ update_game_time()
                $ vitya_have_work = True
                $ remove_item_to_inventory("project")
                jump director_menu
            elif project_taken == 1:
                voice "audio/voices/alina/20.mp3"
                alina "У нас нет такого проекта, «ГМО-тараканы с Wi-Fi роутером»? Мда, не думала, что эта компания на столько плоха"
                voice "audio/voices/alina/21.mp3"
                alina "Потрудитесь найти хоть что-то похожее на нашу разработку."
                $ remove_item_to_inventory("project")
                jump director_menu
            elif project_taken == 3:
                voice "audio/voices/alina/22.mp3"
                alina "У нас нет такого проекта, «ДНК-редактирование для котов-хамелеонов»? Мда, не думала, что эта компания на столько плоха"
                voice "audio/voices/alina/21.mp3"
                alina "Потрудитесь найти хоть что-то похожее на нашу разработку"
                $ remove_item_to_inventory("project")
                jump director_menu
            elif project_taken == 4:
                voice "audio/voices/alina/23.mp3"
                alina "У нас нет такого проекта, «Биоразлагаемый алкоголь»? Мда, не думала, что эта компания на столько плоха"
                voice "audio/voices/alina/21.mp3"
                alina "Потрудитесь найти хоть что-то похожее на нашу разработку"
                $ remove_item_to_inventory("project")
                jump director_menu
            elif project_taken == 5:
                voice "audio/voices/alina/24.mp3"
                alina "У нас нет такого проекта, «Социальная сеть для растений»? Мда, не думала, что эта компания на столько плоха"
                voice "audio/voices/alina/21.mp3"
                alina "Потрудитесь найти хоть что-то похожее на нашу разработку"
                $ remove_item_to_inventory("project")
                jump director_menu
            elif project_taken == 6:
                voice "audio/voices/alina/25.mp3"
                alina "У нас нет такого проекта, «Гибрид медузы и кактуса»? Мда, не думала, что эта компания на столько плоха"
                voice "audio/voices/alina/21.mp3"
                alina "Потрудитесь найти хоть что-то похожее на нашу разработку"
                $ remove_item_to_inventory("project")
                jump director_menu
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/alina/26.mp3"
            alina "Буду ждать вас"
            $ block_ui = False
            $ stop_dialog()
            jump emeregen_director

label need_bathroom:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True
    $ renpy.music.set_pause(True) 
    voice "audio/voices/vika/320.mp3"
    Vika "Я не могу туда пойти в таком виде, мне нужно умыться!"
    $ block_ui = False
    $ stop_dialog()
    jump street

label another_deal:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/321.mp3"
    Vika "У меня сейчас есть другие дела!"
    $ block_ui = False
    $ stop_dialog()
    jump street

label fishman:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "fishman")
    $ polojenie = "fishman"
    play music "city.mp3" fadeout 1
    scene bg fish_store
    show screen fishman
    show screen fishbook
    show screen back_arrow_to_map
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen fishman:
    imagebutton:
        idle "fish_shop/fish_man.png"
        focus_mask True
        if not block_ui:
            hover "fish_shop/fish_man_hover.png"
            action Jump("fishman_dialog")

label fishman_dialog:
    $ renpy.music.set_pause(True)
    $ start_dialog()
    if fishman_first_dialog == True:
        $ block_ui = True
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/322.mp3"
        Vika "Здравствуйте, я бы хотела купить у вас Красноперку."
        voice "audio/voices/fishman/1.mp3"
        fishman "Девушка, вы посмотрите на эти идеально чистые полки, как думаете, я смогу продать вам красноперку?"
        voice "audio/voices/vika/323.mp3"
        Vika "Мне она очень она нужна может у вас осталась одна?"
        voice "audio/voices/fishman/2.mp3"
        fishman "А мне нужна моя газель с рыбой, которая так и не приехала. Так что пока не приедет машина, я не смогу продать вам даже чешую от рыбы."
        voice "audio/voices/vika/324.mp3"
        Vika "А когда приедет ваша машина?"
        voice "audio/voices/fishman/3.mp3"
        fishman "Думаю что не раньше завтрашнего утра."
        voice "audio/voices/vika/325.mp3"
        Vika "Может все-таки можно как-то это исправить?"
        voice "audio/voices/fishman/4.mp3"
        fishman "Ну ты можешь сама пойти искать машину по трассе или ловить рыбу, но тогда зачем тебе я если ты сама ее поймаешь?"
        voice "audio/voices/vika/326.mp3"
        Vika "У меня нечем ловить, а руками я буду ловить дольше чем будет ехать ваша машина"
        voice "audio/voices/fishman/5.mp3"
        fishman "Я могу дать тебе удочку и наживку, но только при одном условии."
        voice "audio/voices/vika/327.mp3"
        Vika "Я вас слушаю."
        voice "audio/voices/fishman/6.mp3"
        fishman "Ты наловишь мне еще немного рыбы, чтоб я торговал ей пока не приедет машина."
        voice "audio/voices/vika/319.mp3"
        Vika "Договорились."
        voice "audio/voices/fishman/7.mp3"
        fishman "Только мне нужна определенная рыба. Мне нужен пескарь, лещ, линь ну и красноперка для тебя, если клюнет что-то другое, тоже неси, я все продам."
        voice "audio/voices/fishman/8.mp3"
        fishman "Все это можно поймать на речке тут неподалеку."
        $ i_know_river = True
        voice "audio/voices/vika/28.mp3"
        Vika "Хорошо."
        $ quest_list[19]["available"] = True
        $ add_item_to_inventory("udochka")
        $ add_item_to_inventory("najivka")
        voice "audio/voices/fishman/9.mp3"
        fishman "Удачной ловли!"
        $ fishman_first_dialog = False
        jump fishman_menu
    else:
        $ block_ui = True 
        $ _preferences.afm_enable = True 
        voice "audio/voices/fishman/14.mp3"
        fishman "Да?"
        jump fishman_menu 

label fishman_menu:
    $ stop_dialog()
    menu:
        "Я наловила рыбы" if fish_quest_done == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/328.mp3"
            Vika "Я наловила рыбы!"
            voice "audio/voices/fishman/10.mp3"
            fishman "Давай посмотрим"
            if "lin" in coughted_fish and "krasnoperka" in coughted_fish and "lesh" in coughted_fish and "peskar" in coughted_fish:
                $ _preferences.afm_enable = True 
                voice "audio/voices/fishman/11.mp3"
                fishman "Ты молодец! Я заберу у тебя всю рыбу, а красноперку можешь оставить себе."
                $ intellect += 1
                $ fish_quest_done = True
                $ remove_item_to_inventory("udochka")
                $ remove_item_to_inventory("najivka")
                $ add_item_to_inventory("krasnoperka")
                $ quest_list[19]["done"] = True
                $ game_hour += 2
                $ update_game_time()
                jump fishman_menu
            else:
                $ _preferences.afm_enable = True 
                voice "audio/voices/fishman/12.mp3"
                fishman "Тут точно не хватает рыб которые я просил. Попробуй еще."
                jump fishman_menu 
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            $ block_ui = False
            $ stop_dialog()
            jump fishman


screen fishbook:
    imagebutton:
        idle "fish_shop/fish_book.png"
        focus_mask True
        if not block_ui and fishman_first_dialog == False:
            hover "fish_shop/fish_book_hover.png"
            action Jump("fishbook")

label fishbook:
    if first_fishbook == True:
        $ block_ui = True
        $ start_dialog()
        $ _preferences.afm_enable = True 
        $ renpy.music.set_pause(True)
        voice "audio/voices/vika/329.mp3"
        Vika "Что это за книга?"
        voice "audio/voices/fishman/13.mp3"
        fishman "Это книга с описанием рыб, можешь почитать если хочешь, только не забирай, она мне нужна."
        $ block_ui = False
        $ stop_dialog()
        $ first_fishbook = False
        show screen fish_book_page1
    else:
        show screen fish_book_page1
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen fish_book_page1:
    modal True
    add "books/fishbook/page1.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("fish_book_page1")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page1"), Show("fish_book_page2")]

screen fish_book_page2:
    modal True
    add "books/fishbook/page2.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("fish_book_page2")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page2"), Show("fish_book_page3")]
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page2"), Show("fish_book_page1")]

screen fish_book_page3:
    modal True
    add "books/fishbook/page3.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("fish_book_page3")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page3"), Show("fish_book_page4")]
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page3"), Show("fish_book_page2")]

screen fish_book_page4:
    modal True
    add "books/fishbook/page4.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("fish_book_page4")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page4"), Show("fish_book_page5")]
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page4"), Show("fish_book_page3")]

screen fish_book_page5:
    modal True
    add "books/fishbook/page5.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("fish_book_page5")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page5"), Show("fish_book_page6")]
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page5"), Show("fish_book_page4")]

screen fish_book_page6:
    modal True
    add "books/fishbook/page6.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("fish_book_page6")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page6"), Show("fish_book_page7")]
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page6"), Show("fish_book_page5")]

screen fish_book_page7:
    modal True
    add "books/fishbook/page7.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("fish_book_page7")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page7"), Show("fish_book_page8")]
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page7"), Show("fish_book_page6")]

screen fish_book_page8:
    modal True
    add "books/fishbook/page8.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("fish_book_page8")
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("fish_book_page8"), Show("fish_book_page7")]

screen river_map_point:
    imagebutton:
        idle "river_map.png"
        xpos 930
        ypos 180
        focus_mask True
        at Transform(zoom=1.3)
        if not block_ui:
            hover "river_map_hover.png"
            if makeup_level == 5:
                action Jump("need_bathroom")
            else:
                action Jump("river")  # Показываем меню выбора, "", "lin", "", "r"

label river:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "river")
    $ polojenie = "river"
    scene bg river
    show screen zaton
    show screen deep
    show screen back_arrow_to_map
    show screen not_deep
    show screen ryaska

    if selected_plase != "none":
        if selected_najivka == "testo" and selected_plase == "zaton":
            $ caught_fish = "lin"
        elif selected_najivka == "oparish" and selected_plase == "deep":
            $ caught_fish = "lesh"
        elif selected_najivka == "Motil" and selected_plase == "not_deep":
            $ caught_fish = "peskar"
        elif selected_najivka == "muha" and selected_plase == "ryaska":
            $ caught_fish = "krasnoperka"
        else:
            $ import random
            $ caught_fish = renpy.random.choice(fish_list)
        $ coughted_fish.append(caught_fish)
        show screen fish_caught(caught_fish)
    # Показываем экран с пойманной рыбой
    

    # Сброс значения selected_plase до показа экрана с рыбой
    $ selected_plase = "none"
    
    # Показ HUD
    $ show_hud()
    
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen fish_caught(caught_fish):
    modal True
    imagebutton:
        idle "ribalka/fish/[caught_fish].png"
        focus_mask True
        action Hide("fish_caught")  # Возврат без дополнительного действия

screen zaton:
    imagebutton:
        idle "river/zaton.png"
        focus_mask True
        if not block_ui and default_mouse == "udochka":
            hover "river/zaton_hover.png"
            action Jump("zaton")

label zaton:
    $ hide_all_ui()
    $ selected_plase = "zaton"
    scene bg zaton
    pause 1.0
    play sound "Poplavok_on.mp3"
    show screen zaton_poplavok
    pause 5.0
    play sound "Poplavok_off.mp3"
    hide screen zaton_poplavok
    pause 0.5
    jump river


screen zaton_poplavok:
    add "ribalka/zaton_poplavok.png"

screen deep:
    imagebutton:
        idle "river/deep.png"
        focus_mask True
        if not block_ui and default_mouse == "udochka":
            hover "river/deep_hover.png"
            action Jump("deep")

label deep:
    $ hide_all_ui()
    $ selected_plase = "deep"
    scene bg deep
    pause 1.0
    play sound "Poplavok_on.mp3"
    show screen deep_poplavok
    pause 5.0
    play sound "Poplavok_off.mp3"
    hide screen deep_poplavok
    pause 0.5
    jump river


screen deep_poplavok:
    add "ribalka/deep_poplavok.png"

screen not_deep:
    imagebutton:
        idle "river/not_deep.png"
        focus_mask True
        if not block_ui and default_mouse == "udochka":
            hover "river/not_deep_hover.png"
            action Jump("not_deep")

label not_deep:
    $ hide_all_ui()
    $ selected_plase = "not_deep"
    scene bg not_deep
    pause 1.0
    play sound "Poplavok_on.mp3"
    show screen not_deep_poplavok
    pause 5.0
    play sound "Poplavok_off.mp3"
    hide screen not_deep_poplavok
    pause 0.5
    jump river


screen not_deep_poplavok:
    add "ribalka/not_deep_poplavok.png"

screen ryaska:
    imagebutton:
        idle "river/ryaska.png"
        focus_mask True
        if not block_ui and default_mouse == "udochka":
            hover "river/ryaska_hover.png"
            action Jump("ryaska")

label ryaska:
    $ hide_all_ui()
    $ selected_plase = "ryaska"
    scene bg ryaska
    pause 1.0
    play sound "Poplavok_on.mp3"
    show screen ryaska_poplavok
    pause 5.0
    play sound "Poplavok_off.mp3"
    hide screen ryaska_poplavok
    pause 0.5
    jump river


screen ryaska_poplavok:
    add "ribalka/ryaska_poplavok.png"

label zvonok_shluhe:
    $ hide_all_ui()
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    play sound "zvuk-iphone.mp3"
    pause 1.0
    show screen zvonok_ot_shluhi
    pause 2.0
    stop sound
    hide screen zvonok_ot_shluhi
    show screen zvonok_ot_shluhi_vzyat
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/330.mp3"
    Vika "Ало."
    voice "audio/voices/clara/1.mp3"
    nobody "Здравствуйте, я нашла ваше объявление о сдаче квартиры, вы ее еще сдаете?"
    voice "audio/voices/vika/331.mp3"
    Vika "Да, еще сдаю. Хотите посмотреть?"
    voice "audio/voices/clara/2.mp3"
    nobody "Очень хочу. А можно прямо сейчас подъехать?"
    voice "audio/voices/vika/332.mp3"
    Vika "Да, конечно. Адрес я вам сейчас скину."
    voice "audio/voices/clara/3.mp3"
    nobody "Спасибо большое. Я скоро буду!"
    hide screen zvonok_ot_shluhi_vzyat

    scene black with fade
    pause 1
    $ _preferences.afm_enable = True 
    "Спустя 30 минут..."
    scene bg mainhall

    show clara_neutral at center
    $ _preferences.afm_enable = True 
    voice "audio/voices/clara/19.mp3"
    clara "Здравствуйте! Я Клара, звонила вам по поводу квартиры."
    voice "audio/voices/vika/333.mp3"
    Vika "Здравствуйте. Заходите, вот, смотрите — кухня, ванна, здесь 2 комнаты."
    scene bg vitya_room with fade
    show clara_neutral at right
    pause 1.0
    scene bg mainroom with fade
    show clara_neutral at right
    $ _preferences.afm_enable = True 
    voice "audio/voices/clara/20.mp3"
    clara "Ой, как хорошо, что здесь две двуспальных кровати…"
    voice "audio/voices/vika/334.mp3"
    Vika "...Вы с кем-то будете снимать?"
    voice "audio/voices/clara/21.mp3"
    clara "Да, я с подругой. Мы всё поровну делим. И кровати, и... всё остальное." 
    voice "audio/voices/vika/335.mp3"
    Vika "А, ясно. Вы работаете вместе?"
    voice "audio/voices/clara/22.mp3"
    clara "Ну... можно и так сказать. Мы с ней... фрилансеры." 
    voice "audio/voices/vika/336.mp3"
    Vika "Фрилансеры?"
    voice "audio/voices/clara/23.mp3"
    clara "Ну да. Гибкий график, сами выбираем клиентов… то есть, проекты. Много командировок…"
    voice "audio/voices/vika/337.mp3"
    Vika "Понятно... {i}почти{/i}. Главное, чтоб платили вовремя и не шумели ночью."
    voice "audio/voices/clara/24.mp3"
    clara "О, с этим вообще проблем не будет. Мы очень тихие…"
    voice "audio/voices/vika/338.mp3"
    Vika "Слушайте, вы проститутка, что ли?"
    voice "audio/voices/clara/25.mp3"
    clara "Ну… если прямо. Да. Но сейчас всё цивильно, без глупостей. Мы просто зарабатываем как можем. Аренду всегда вовремя, мы чистоплотные, не пьём… почти."
    voice "audio/voices/vika/339.mp3"
    Vika "Мне, если честно, всё равно. Мне главное — чтоб деньги были вовремя, и соседи не жаловались."
    voice "audio/voices/clara/26.mp3"
    clara "Вот и отлично! Тогда я передам подруге, что мы въезжаем. А когда мы можем въехать?"
    voice "audio/voices/vika/340.mp3"
    Vika "Думаю через 3 дня мы уже улетим в питер и вы сможете въехать. Ключи получишь после предоплаты."
    voice "audio/voices/clara/27.mp3"
    clara "Хорошо, если я буду нужна, я в свободное время в баре на Таёжной."
    voice "audio/voices/vika/341.mp3"
    Vika "Поняла."
    voice "audio/voices/clara/28.mp3"
    clara "Тогда до скорого."
    voice "audio/voices/vika/342.mp3"
    Vika "Пока."
    $ quest_list[3]["done"] = True
    $ i_know_bar = True
    $ vilojeno_obyavleniya = False
    $ bil_zvonok_shluhe = True
    $ block_ui = False
    $ stop_dialog()
    jump mainroom


screen zvonok_ot_shluhi:
    add "zvonok_ot_shluhi.png" xpos 750 ypos 150

screen zvonok_ot_shluhi_vzyat:
    add "zvonok_ot_shluhi_vzyat.png" xpos 750 ypos 150

screen shop_map_point:
    if not block_ui:
        imagebutton:
            idle "shop_map_idle.png"
            hover "shop_map_hover.png"
            xpos 1420
            ypos 330
            focus_mask True
            at Transform(zoom=1.3)
            if makeup_level == 5:
                action Jump("need_bathroom")
            else:
                action Jump("shop")  # Показываем меню выбора



screen click_blocker():
    if not clicks_enabled:
        # Прозрачный экран, перекрывающий весь экран и блокирующий клики
        frame:
            style "blank_frame"
            at truecenter
            background None
            xysize (config.screen_width, config.screen_height)
            key "mouseup_1" action NullAction()
            key "mousedown_1" action NullAction()
            key "K_RETURN" action NullAction()
            key "K_SPACE" action NullAction()
            key "K_TAB" action NullAction()
            key "K_LCTRL" action NullAction()
            key "K_RCTRL" action NullAction()
            key "mouseup_2" action NullAction()
            key "mousedown_4" action NullAction()  # Колесо вверх
            key "mousedown_5" action NullAction()  # Колесо вниз
            key "mouseup_3" action NullAction()
            key "mousedown_3" action NullAction()

label shop:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "shop")
    $ polojenie = "shop" 
    play music "city.mp3" fadeout 1
    scene bg shop
    show screen back_arrow_to_map
    show screen door_to_shop
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen door_to_shop:
    if not block_ui:
        imagebutton:
            idle "shop/door_to_shop.png"
            hover "shop/door_to_shop_hover.png"
            focus_mask True
            action Jump("shop_screen") # Показываем меню выбора  

label shop_screen:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg shop
    show screen shop_screen
    show screen shop_start
    $ renpy.music.set_pause(False)
    call pay_label from _call_pay_label
    call screen wait_for_click

    return

screen shop_start:
    add "shop/anons_sales.png"

init python:
    check_items = []

init python:
    def add_to_check(item_name, item_price, item_color):
    # Создаём товар с его именем, ценой и цветом
        item = {'name': item_name, 'price': item_price, 'color': item_color}
    
    # Проверяем, что товар ещё не добавлен в список
        if item not in check_items:
            check_items.append(item)

init python:
    def remove_from_check(index):
        if 0 <= index < len(check_items):
            check_items.pop(index)
    
    def get_total_price():
        total = 0

        # Копируем товары по цветам
        red_items = [item for item in check_items if item['color'] == 'red']
        yellow_items = [item for item in check_items if item['color'] == 'yellow']
        blue_items = [item for item in check_items if item['color'] == 'blue']
        green_items = [item for item in check_items if item['color'] == 'green']
        other_items = [item for item in check_items if item['color'] not in ('red', 'yellow', 'blue', 'green')]

        # Обрабатываем красные: скидка 30% на половину самых дешевых
        red_items.sort(key=lambda x: x['price'])
        half_count = len(red_items) // 2
        total += sum(item['price'] * 0.7 for item in red_items[:half_count]) + \
                sum(item['price'] for item in red_items[half_count:])

        # Жёлтые: скидка 50% на половину самых дешевых
        yellow_items.sort(key=lambda x: x['price'])
        half_count = len(yellow_items) // 2
        total += sum(item['price'] * 0.5 for item in yellow_items[:half_count]) + \
                sum(item['price'] for item in yellow_items[half_count:])

        # Синие: каждая третья — бесплатно (самая дешёвая)
        blue_items.sort(key=lambda x: x['price'])
        total += sum(item['price'] for item in blue_items[len(blue_items) // 3:])

        # Зелёные: каждая 4-я — бесплатно
        green_items.sort(key=lambda x: x['price'])
        total += sum(item['price'] for item in green_items[len(green_items) // 4:])

        # Остальные товары — без скидок
        for item in other_items:
            total += item['price']

        return int(total)

screen check_panel():
    frame:
        xpos 0.055
        ypos 0.322
        xsize 300
        ysize 460
        background "#ffffff00"
        padding (10, 10, 10, 10)

        has fixed

        # Прокручиваемая зона со списком товаров
        viewport:
            ysize 320
            scrollbars "vertical"
            mousewheel True
            draggable True
            vbox:
                spacing 4
                for i, item in enumerate(check_items):
                    hbox:
                        spacing 6
                        textbutton "✖":
                            action Function(remove_from_check, i)
                            background None
                            xminimum 18
                            xmaximum 18
                            text_size 14
                        text "[item['name']] — [item['price']]₽":
                            color "#000"
                            size 16

        # "Итого" — фиксированное положение
        text "[get_total_price()]":
            xpos 0.1
            ypos 405
            size 20
            color "#000"
            bold True

init python:
    def check_correct_items():
        required_items = [
            "Лист.лаз", "Фарш", "Лук", "Морковь", "Кетчуп",
            "Том. паста", "Слив.масло", "Мука", "Молоко",
            "Сыр", "Орехи", "Соль", "Перец"
        ]

        try:
            # Получаем названия товаров без "(цвет)"
            item_names = [item["name"].split(" (")[0] for item in check_items]
            
            # Отладка (пиши в log.txt)
            renpy.log("Список в чеке: " + str(item_names))
            renpy.log("Ожидается: " + str(required_items))
            
            # Сравниваем отсортированные списки
            return sorted(item_names) == sorted(required_items)

        except Exception as e:
            renpy.log("Ошибка в check_correct_items: " + str(e))
            return False
        

screen shop_screen:
    add "shop/shop.png"
    add "shop/chek.png"
    if not block_ui:
        imagebutton:
            idle "shop/exit_button.png"
            hover "shop/exit_button_hover.png"
            focus_mask True
            action Jump("shop")
    if not block_ui:
        imagebutton:
            if selected_otlata == "cash":
                idle "shop/cash_button_hover.png"  
            else:
                idle "shop/cash_button.png"
            hover "shop/cash_button_hover.png"
            focus_mask True
            action If(
                selected_otlata == "cash",
                SetVariable("selected_otlata", None),
                SetVariable("selected_otlata", "cash")
            )
    if not block_ui:
        imagebutton:
            if selected_otlata == "card":
                idle "shop/card_button_hover.png"  
            else:
                idle "shop/card_button.png"
            hover "shop/card_button_hover.png"
            focus_mask True
            action If(
                selected_otlata == "card",
                SetVariable("selected_otlata", None),
                SetVariable("selected_otlata", "card")
            )
    if not block_ui:
        if selected_otlata == "card" and "card" in inventory_items:
            if get_total_price() < card_money:
                if check_correct_items():
                    imagebutton:
                        idle "shop/pay_button.png"
                        hover "shop/pay_button_hover.png"
                        focus_mask True
                        action [
                            Function(check_items.clear),
                            Function(add_item_to_inventory, "produkti"),
                            SetVariable("pay_result", "ok"),
                            Return()
                        ]
                else:
                    imagebutton:
                        idle "shop/pay_button.png"
                        hover "shop/pay_button_hover.png"
                        focus_mask True
                        action [
                            SetVariable("pay_result", "no_full"),
                            Return()
                        ]
            else:
                imagebutton:
                    idle "shop/pay_button.png"
                    hover "shop/pay_button_hover.png"
                    focus_mask True
                    action [
                        SetVariable("pay_result", "no_money"),
                        Return()
                    ]
        elif selected_otlata == "card" and "card" not in inventory_items:
            imagebutton:
                idle "shop/pay_button.png"
                hover "shop/pay_button_hover.png"
                focus_mask True
                action [
                    SetVariable("pay_result", "no_card"),
                    Return()
                ]
        elif selected_otlata == "cash":
            if money >= get_total_price():
                imagebutton:
                    idle "shop/pay_button.png"
                    hover "shop/pay_button_hover.png"
                    focus_mask True
                    action [
                        SetVariable("pay_result", "kupila"),
                        Function(process_paints),
                        Function(check_items.clear),
                        Return()
                    ]
            else:
                imagebutton:
                    idle "shop/pay_button.png"
                    hover "shop/pay_button_hover.png"
                    focus_mask True
                    action [
                        SetVariable("pay_result", "no_money"),
                        Return()
                    ]
        else:
            imagebutton:
                idle "shop/pay_button.png"
                hover "shop/pay_button_hover.png"
                focus_mask True
                action [
                    SetVariable("pay_result", "no_rejim"),
                    Return()
                ]
    if not block_ui:
        imagebutton:
            idle "shop/product_button.png"
            hover "shop/product_button_hover.png"
            focus_mask True
            action [Hide("shop_start"), Hide("color"), Hide("another_product"), Show("product1"), Hide("product2"), Hide("product3"), Hide("product4"), Hide("product5"), Hide("product6"), Hide("product7"), Hide("product8"), Hide("product9"), Hide("product10"), Hide("product11"), Hide("product12"), Hide("product13"), Hide("product14"), Hide("product15"), Hide("product16"), Hide("product17")]
    if not block_ui:
        imagebutton:
            idle "shop/hoz_tov_button.png"
            hover "shop/hoz_tov_button_hover.png"
            focus_mask True
            action [Hide("shop_start"), Hide("another_product"), Show("color"), Hide("product1"), Hide("product2"), Hide("product3"), Hide("product4"), Hide("product5"), Hide("product6"), Hide("product7"), Hide("product8"), Hide("product9"), Hide("product10"), Hide("product11"), Hide("product12"), Hide("product13"), Hide("product14"), Hide("product15"), Hide("product16"), Hide("product17")]
    if not block_ui:
        imagebutton:
            idle "shop/another_button.png"
            hover "shop/another_button_hover.png"
            focus_mask True
            action [Hide("shop_start"), Show("another_product"), Hide("color"), Hide("product1"), Hide("product2"), Hide("product3"), Hide("product4"), Hide("product5"), Hide("product6"), Hide("product7"), Hide("product8"), Hide("product9"), Hide("product10"), Hide("product11"), Hide("product12"), Hide("product13"), Hide("product14"), Hide("product15"), Hide("product16"), Hide("product17")]
    use check_panel

init python:
    def process_paints():
        paints = {
            "Краска (чёрная)": "black_colour",
            "Краска (белая)": "white_colour",
            "Краска (зеленая)": "green_colour",
            "Краска (синяя)": "blue_colour",
        }
        another = {"Подшипник": "podshipnik",}

        for display_name, internal_name in paints.items():
            if any(item['name'] == display_name for item in check_items):
                renpy.store.money -= 31
                add_item_to_inventory(internal_name)

        for display_name, internal_name in another.items():
            if any(item['name'] == display_name for item in check_items):
                renpy.store.money -= 100
                add_item_to_inventory(internal_name)

label pay_label:
    $ renpy.free_memory()
    call screen shop_screen
    $ hide_all_ui() 
    show screen shop_screen
    show screen shop_start
    $ renpy.music.set_pause(True)
    $ start_dialog()
    if pay_result == "ok":
        voice "audio/voices/vika/479.mp3"
        "Вика" "Фуф, слава богу хватило"
        $ quest_list[7]["done"] = True
        $ intellect += 1
        $ quest_list[16]["available"] = True
        $ remove_item_to_inventory("card")
        hide screen shop_screen
        $ stop_dialog()
        jump shop
    elif pay_result == "no_money":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/343.mp3"
        "Вика" "Мне не хватит на это денег"
    elif pay_result == "no_card":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/344.mp3"
        "Вика" "У меня нету карты"
    elif pay_result == "no_full":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/345.mp3"
        "Вика" "Я еще не все купила"
    elif pay_result == "no_rejim":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/346.mp3"
        "Вика" "Я не выбрала чем платить."
    elif pay_result == "kupila":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/347.mp3"
        "Вика" "Как приятно делать покупки."
    $ stop_dialog()
    jump shop_screen
    return

screen another_product:
    zorder 92
    add "shop/another_product_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/podshipnik.png"
            hover "shop/podshipnik_hover.png"
            focus_mask True
            if "podshipnik" in inventory_items:
                action Jump("i_have_it")
            else:
                action Function(add_to_check, "Подшипник", 100, "gray")

screen color:
    zorder 92
    add "shop/color_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/color_black.png"
            hover "shop/color_black_hover.png"
            focus_mask True
            if "black_colour" in inventory_items:
                action Jump("i_have_it")
            else:
                action Function(add_to_check, "Краска (чёрная)", 31, "gray")
    if not block_ui:
        imagebutton:
            idle "shop/color_white.png"
            hover "shop/color_white_hover.png"
            focus_mask True
            if "white_colour" in inventory_items:
                action Jump("i_have_it")
            else:
                action Function(add_to_check, "Краска (белая)", 31, "gray")
    if not block_ui:
        imagebutton:
            idle "shop/color_blue.png"
            hover "shop/color_blue_hover.png"
            focus_mask True
            if "blue_colour" in inventory_items:
                action Jump("i_have_it")
            else:
                action Function(add_to_check, "Краска (синяя)", 31, "gray")
    if not block_ui:
        imagebutton:
            idle "shop/color_green.png"
            hover "shop/color_green_hover.png"
            focus_mask True
            if "green_colour" in inventory_items:
                action Jump("i_have_it")
            else:
                action Function(add_to_check, "Краска (зеленая)", 31, "gray")

label i_have_it:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/348.mp3"
    Vika "У меня уже есть это."
    $ block_ui = False
    $ stop_dialog()
    jump shop_screen


screen product1:
    zorder 92
    add "shop/meat_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/meat_red.png"
            hover "shop/meat_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Фарш (красный)", 600, "red")
    if not block_ui:
        imagebutton:
            idle "shop/meat_yellow.png"
            hover "shop/meat_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Фарш (желтый)", 800, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/meat_blue.png"
            hover "shop/meat_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Фарш (синий)", 600, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/meat_green.png"
            hover "shop/meat_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Фарш (зеленый)", 600, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product1"), Show("product2")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action[Hide("product1"), Show("product17")]

screen product2:
    zorder 92
    add "shop/list_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/list_red.png"
            hover "shop/list_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Лист.лаз (красный)", 440, "red")
    if not block_ui:
        imagebutton:
            idle "shop/list_yellow.png"
            hover "shop/list_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Лист.лаз (желтый)", 550, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/list_blue.png"
            hover "shop/list_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Лист.лаз (синий)", 440, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/list_green.png"
            hover "shop/list_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Лист.лаз (зеленый)", 440, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product2"), Show("product3")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product2"), Show("product1")]

screen product3:
    zorder 92
    add "shop/eggs_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/eggs_red.png"
            hover "shop/eggs_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Яйца (красный)", 49, "red")
    if not block_ui:
        imagebutton:
            idle "shop/eggs_yellow.png"
            hover "shop/eggs_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Яйца (желтый)", 75, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/eggs_blue.png"
            hover "shop/eggs_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Яйца (синий)", 150, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/eggs_green.png"
            hover "shop/eggs_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Яйца (зеленый)", 214, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product3"), Show("product4")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product3"), Show("product2")]

screen product4:
    zorder 92
    add "shop/onion_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/onion_red.png"
            hover "shop/onion_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Лук (красный)", 26, "red")
    if not block_ui:
        imagebutton:
            idle "shop/onion_yellow.png"
            hover "shop/onion_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Лук (желтый)", 30, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/onion_blue.png"
            hover "shop/onion_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Лук (синий)", 45, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/onion_green.png"
            hover "shop/onion_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Лук (зеленый)", 50, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product4"), Show("product5")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product4"), Show("product3")]

screen product5:
    zorder 92
    add "shop/carrot_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/carrot_red.png"
            hover "shop/carrot_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Морковь (красный)", 27, "red")
    if not block_ui:
        imagebutton:
            idle "shop/carrot_yellow.png"
            hover "shop/carrot_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Морковь (желтый)", 33, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/carrot_blue.png"
            hover "shop/carrot_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Морковь (синий)", 39, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/carrot_green.png"
            hover "shop/carrot_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Морковь (зеленый)", 46, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product5"), Show("product6")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product5"), Show("product4")]

screen product6:
    zorder 92
    add "shop/tomato_souse_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/tomato_souse_red.png"
            hover "shop/tomato_souse_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Кетчуп (красный)", 135, "red")
    if not block_ui:
        imagebutton:
            idle "shop/tomato_souse_yellow.png"
            hover "shop/tomato_souse_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Кетчуп (желтый)", 169, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/tomato_souse_blue.png"
            hover "shop/tomato_souse_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Кетчуп (синий)", 108, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/tomato_souse_green.png"
            hover "shop/tomato_souse_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Кетчуп (зеленый)", 135, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product6"), Show("product7")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product6"), Show("product5")]

screen product7:
    zorder 92
    add "shop/mayonnaise_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/mayonnaise_red.png"
            hover "shop/mayonnaise_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Майонез (красный)", 100, "red")
    if not block_ui:
        imagebutton:
            idle "shop/mayonnaise_yellow.png"
            hover "shop/mayonnaise_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Майонез (желтый)", 154, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/mayonnaise_blue.png"
            hover "shop/mayonnaise_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Майонез (синий)", 167, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/mayonnaise_green.png"
            hover "shop/mayonnaise_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Майонез (зеленый)", 219, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product7"), Show("product8")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product7"), Show("product6")]

screen product8:
    zorder 92
    add "shop/tomato_past_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/tomato_past_red.png"
            hover "shop/tomato_past_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Том. паста (красный)", 165, "red")
    if not block_ui:
        imagebutton:
            idle "shop/tomato_past_yellow.png"
            hover "shop/tomato_past_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Том. паста (желтый)", 207, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/tomato_past_blue.png"
            hover "shop/tomato_past_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Том. паста (синий)", 132, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/tomato_past_green.png"
            hover "shop/tomato_past_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Том. паста (зеленый)", 165, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product8"), Show("product9")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product8"), Show("product7")]

screen product9:
    zorder 92
    add "shop/oil_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/oil_red.png"
            hover "shop/oil_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Слив.масло (красный)", 240, "red")
    if not block_ui:
        imagebutton:
            idle "shop/oil_yellow.png"
            hover "shop/oil_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Слив.масло (желтый)", 300, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/oil_blue.png"
            hover "shop/oil_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Слив.масло (синий)", 192, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/oil_green.png"
            hover "shop/oil_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Слив.масло (зеленый)", 240, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product9"), Show("product10")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product9"), Show("product8")]

screen product11:
    zorder 92
    add "shop/sugar_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/sugar_red.png"
            hover "shop/sugar_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Сахар (красный)", 50, "red")
    if not block_ui:
        imagebutton:
            idle "shop/sugar_yellow.png"
            hover "shop/sugar_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Сахар (желтый)", 54, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/sugar_blue.png"
            hover "shop/sugar_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Сахар (синий)", 67, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/sugar_green.png"
            hover "shop/sugar_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Сахар (зеленый)", 219, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product11"), Show("product12")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product11"), Show("product10")]

screen product10:
    zorder 92
    add "shop/muka_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/muka_red.png"
            hover "shop/muka_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Мука (красный)", 25, "red")
    if not block_ui:
        imagebutton:
            idle "shop/muka_yellow.png"
            hover "shop/muka_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Мука (желтый)", 35, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/muka_blue.png"
            hover "shop/muka_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Мука (синий)", 43, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/muka_green.png"
            hover "shop/muka_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Мука (зеленый)", 50, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product10"), Show("product11")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product10"), Show("product9")]

screen product12:
    zorder 92
    add "shop/milk_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/milk_red.png"
            hover "shop/milk_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Молоко (красный)", 40, "red")
    if not block_ui:
        imagebutton:
            idle "shop/milk_yellow.png"
            hover "shop/milk_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Молоко (желтый)", 44, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/milk_blue.png"
            hover "shop/milk_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Молоко (синий)", 60, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/milk_green.png"
            hover "shop/milk_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Молоко (зеленый)", 70, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product12"), Show("product13")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product12"), Show("product11")]

screen product13:
    zorder 92
    add "shop/cheese_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/cheese_red.png"
            hover "shop/cheese_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Сыр (красный)", 450, "red")
    if not block_ui:
        imagebutton:
            idle "shop/cheese_yellow.png"
            hover "shop/cheese_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Сыр (желтый)", 600, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/cheese_blue.png"
            hover "shop/cheese_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Сыр (синий)", 450, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/cheese_green.png"
            hover "shop/cheese_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Сыр (зеленый)", 450, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product13"), Show("product14")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product13"), Show("product12")]

screen product14:
    zorder 92
    add "shop/nuts_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/nuts_red.png"
            hover "shop/nuts_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Орехи (красный)", 200, "red")
    if not block_ui:
        imagebutton:
            idle "shop/nuts_yellow.png"
            hover "shop/nuts_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Орехи (желтый)", 250, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/nuts_blue.png"
            hover "shop/nuts_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Орехи (синий)", 160, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/nuts_green.png"
            hover "shop/nuts_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Орехи (зеленый)", 200, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product14"), Show("product15")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product14"), Show("product13")]

screen product15:
    zorder 92
    add "shop/sunflower_oil_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/sunflower_oil_red.png"
            hover "shop/sunflower_oil_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Подс. масло (красный)", 53, "red")
    if not block_ui:
        imagebutton:
            idle "shop/sunflower_oil_yellow.png"
            hover "shop/sunflower_oil_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Подс. масло (желтый)", 51, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/sunflower_oil_blue.png"
            hover "shop/sunflower_oil_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Подс. масло (синий)", 64, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/sunflower_oil_green.png"
            hover "shop/sunflower_oil_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Подс. масло (зеленый)", 68, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product15"), Show("product16")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product15"), Show("product14")]

screen product16:
    zorder 92
    add "shop/salt_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/salt_red.png"
            hover "shop/salt_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Соль (красный)", 22, "red")
    if not block_ui:
        imagebutton:
            idle "shop/salt_yellow.png"
            hover "shop/salt_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Соль (желтый)", 27, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/salt_blue.png"
            hover "shop/salt_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Соль (синий)", 37, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/salt_green.png"
            hover "shop/salt_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Соль (зеленый)", 46, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product16"), Show("product17")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product16"), Show("product15")]

screen product17:
    zorder 92
    add "shop/paper_page.png"
    if not block_ui:
        imagebutton:
            idle "shop/paper_red.png"
            hover "shop/paper_red_hover.png"
            focus_mask True
            action Function(add_to_check, "Перец (красный)", 27, "red")
    if not block_ui:
        imagebutton:
            idle "shop/paper_yellow.png"
            hover "shop/paper_yellow_hover.png"
            focus_mask True
            action Function(add_to_check, "Перец (желтый)", 33, "yellow")
    if not block_ui:
        imagebutton:
            idle "shop/paper_blue.png"
            hover "shop/paper_blue_hover.png"
            focus_mask True
            action Function(add_to_check, "Перец (синий)", 44, "blue")
    if not block_ui:
        imagebutton:
            idle "shop/paper_green.png"
            hover "shop/paper_green_hover.png"
            focus_mask True
            action Function(add_to_check, "Перец (зеленый)", 51, "green")
    if not block_ui:
        imagebutton:
            idle "shop/next_page_button.png"
            hover "shop/next_page_button_hover.png"
            focus_mask True
            action [Hide("product17"), Show("product1")]
    if not block_ui:
        imagebutton:
            idle "shop/last_page_button.png"
            hover "shop/last_page_button_hover.png"
            focus_mask True
            action [Hide("product17"), Show("product16")]

screen home_point:
    if not block_ui:
        imagebutton:
            idle "home_idle.png"
            hover "home_hover.png"
            xpos 1500
            ypos 280
            focus_mask True
            at Transform(zoom=1.3)
            action Jump("hallway")  # Показываем меню выбора

screen casino_map_point:
    if not block_ui:
        imagebutton:
            idle "casino_map_idle.png"
            hover "casino_map_hover.png"
            xpos 980
            ypos 320
            focus_mask True
            at Transform(zoom=1.3)
            action Jump("casino")  # Показываем меню выбора

screen airport_map_point:
    if not block_ui:
        imagebutton:
            idle "airport_map_idle.png"
            hover "airport_map_hover.png"
            xpos 75
            ypos 470
            focus_mask True
            at Transform(zoom=1.3)
            action Jump("airport")  # Показываем меню выбора

label airport:
    $ start_dialog()
    if makeup_level == 5:
        jump need_bathroom
    elif clara_suck_now == True:
        jump another_deal
    elif bileti_kupleni == False:
        $ _preferences.afm_enable = True 
        $ renpy.music.set_pause(True)
        voice "audio/voices/vika/349.mp3"
        Vika "Зачем мне в аэропорт без билетов?"
    elif bileti_kupleni == True:
        $ renpy.music.set_pause(True)
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/350.mp3"
        Vika "Мой вылет еще не скоро, мне не надо в аэропорт."
    $ renpy.music.set_pause(False)
    $ stop_dialog()
    call screen wait_for_click
    return

screen masterskaya_map_point:
    if not block_ui:
        imagebutton:
            idle "masterskaya_map_idle.png"
            hover "masterskaya_map_hover.png"
            xpos 1210
            ypos 540
            focus_mask True
            at Transform(zoom=1.3)
            action Jump("masterskaya")  # Показываем меню выбора

label masterskaya:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "masterskaya")
    $ polojenie = "masterskaya"
    play music "city.mp3" fadeout 1
    scene bg masterskaya
    show screen back_arrow_to_map
    show screen door_to_masterskaya
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen door_to_masterskaya:
    if not block_ui:
        imagebutton:
            idle "door_to_masterskaya_idle.png"
            hover "door_to_masterskaya_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("masterskaya_inside")  # Показываем меню выбора    

label masterskaya_inside:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ show_hud()
    play music "masterskaya.mp3" fadeout 1
    scene bg masterskaya_inside
    show screen back_arrow_to_masterskaya
    show screen chingis
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen chingis:
    imagebutton:
        idle "chingis_idle.png"            
        xpos 0
        ypos 0
        focus_mask True
        if not block_ui:
            hover "chingis_hover.png"
            if default_mouse == "dice":
                action Jump("chingis_dice")
            else:
                action Jump("chingis_dialog")  # Показываем меню выбора

label chingis_dice:
    $ renpy.free_memory()
    $ block_ui = True
    $ renpy.music.set_pause(True)
    if sudoku_proideno == True:
        $ default_mouse = "default"
        $ start_dialog()
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/351.mp3"
        Vika "Слушай, а ты можешь просверлить этот кубик ровно в цифре 1?"
        voice "audio/voices/chingis/6.mp3"
        chingis "Конечно, мне это один плюнуть."
        hide screen chingis
        pause 1.0
        play sound "drel.mp3"
        pause 3.0
        show screen chingis
        $ _preferences.afm_enable = True 
        voice "audio/voices/chingis/7.mp3"
        chingis "Готово!"
        voice "audio/voices/vika/352.mp3"
        Vika "Как круто, ты молодец!"
        $ remove_item_to_inventory("dice")
        $ add_item_to_inventory("dice_with_o") 
        $ block_ui = False
        $ stop_dialog()
        jump masterskaya_inside
    else:
        $ start_dialog()
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/351.mp3"
        Vika "Слушай, а ты можешь просверлить этот кубик ровно в цифре 1?"
        voice "audio/voices/chingis/8.mp3"
        chingis "Я все магу! Только не сейчас, я занят!"
        $ block_ui = False
        $ stop_dialog()
        jump masterskaya_inside
        

    $ block_ui = False

label chingis_dialog:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    if chingis_dialog == 0:  # Знакомство с чингисом
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/353.mp3"
        Vika "Здравствуйте!"
        voice "audio/voices/chingis/9.mp3"
        chingis "Здраустуйтэ, чэм могу памочь?"
        voice "audio/voices/vika/354.mp3"
        Vika "ААААА!!! Чонгууууук!!!!!"
        voice "audio/voices/chingis/10.mp3"
        chingis "Я нэ чонгук, я Чингыс!!! Я авто-мэханик... плотник... токарь... забыл как это вся па руски..."
        voice "audio/voices/vika/355.mp3"
        Vika "Мастер?"
        voice "audio/voices/chingis/11.mp3"
        chingis "Да, мастэр"
        voice "audio/voices/vika/356.mp3"
        Vika "То есть вы не Чонгук?"
        voice "audio/voices/chingis/12.mp3"
        chingis "Нэт, я лучше, я Чингыс, на все руки токарь."
        voice "audio/voices/vika/355.mp3"
        Vika "Мастер?"
        voice "audio/voices/chingis/13.mp3"
        chingis "Да, да, мастэр, все могу в общэм."
        voice "audio/voices/vika/357.mp3"
        Vika "А я Вика."
        voice "audio/voices/chingis/14.mp3"
        chingis "Очэнь пруиятно, Уика"
        $ i_know_chingis = True
        $ chingis_dialog = 1
    elif chingis_dialog == 1:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/358.mp3"
        Vika "Привет Чугун!"
        voice "audio/voices/chingis/2.mp3"
        chingis "Приуэйт Викэ"
    jump chingis_menu

label chingis_menu:
    $ stop_dialog()
    $ renpy.free_memory()
    menu:
        "Ты умеешь играть на пианино?" if i_want_piano_first_time == False and i_ask_chingis_about_piano == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/359.mp3"
            Vika "Ты умеешь играть на пианино?"
            voice "audio/voices/chingis/15.mp3"
            chingis "Я уже гаварил я всо умейу!"
            voice "audio/voices/vika/360.mp3"
            Vika "Ты можешь научить меня?"
            voice "audio/voices/chingis/16.mp3"
            chingis "Нет, ты меня подставила, я пол часа объяснял полиции, что ни в чем не виноват!"
            voice "audio/voices/vika/361.mp3"
            Vika "Ты просто перепутал машину, я тоже объясняла это полиции!"
            voice "audio/voices/chingis/17.mp3"
            chingis "Все равно это все из-за тебя, я не буду тебе помогать!"
            voice "audio/voices/vika/118.mp3"
            Vika "Ну пожалуйста!"
            voice "audio/voices/chingis/18.mp3"
            chingis "Если тебе так надо, на, вот тебе книжка, сама учись"
            $ add_item_to_inventory("piano_book")
            $ i_ask_chingis_about_piano = True
            jump chingis_menu
        "Чем ты здесь занимаешься?" if Chingis_chem_zanyat == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/362.mp3"
            Vika "Чем ты здесь занимаешься?"
            voice "audio/voices/chingis/19.mp3"
            chingis "Я тут все делайу, чиню машины, пилю, режу, сверлю..."
            voice "audio/voices/chingis/20.mp3"
            chingis "Я мастэр своего дела, я один раз человеку дырку в волосе просверлил, а он сам цел остался!!!"
            voice "audio/voices/vika/363.mp3"
            Vika "Кто целый? Человек?"
            voice "audio/voices/chingis/21.mp3"
            chingis "Какой человек? Волос!"
            voice "audio/voices/vika/364.mp3"
            Vika "Что-то я не верю."
            voice "audio/voices/chingis/22.mp3"
            chingis "Не веришь? Давай сюда волосы, я покажу."
            voice "audio/voices/vika/365.mp3"
            Vika "Нет нет нет, мои волосы трогать не надо! Давай я тебе лучше что-то другое принесу."
            voice "audio/voices/chingis/23.mp3"
            chingis "Приноси. Что хочешь, все просверлю!"
            $ Chingis_chem_zanyat = True
            jump chingis_menu

        "Я прошла судоку" if i_know_sudoku == True and rozetka_is_broken == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/366.mp3"
            Vika "Я прошла судоку!!!"
            voice "audio/voices/chingis/24.mp3"
            chingis "Нука покажи"
            if sudoku_proideno == False:
                $ _preferences.afm_enable = True 
                voice "audio/voices/chingis/25.mp3"
                chingis "АХАХХААХ, это даже близко неправильно! Ты женщина, ты никогда не сможешь это сделать!"
                jump chingis_menu
            else:
                $ sudoku_proideno = True
                $ quest_list[6]["done"] = True
                $ intellect += 1
                $ _preferences.afm_enable = True 
                voice "audio/voices/chingis/26.mp3"
                chingis "Ты самый умный женщина, который я видел!!!"
                voice "audio/voices/vika/367.mp3"
                Vika "Ты обещал целый день делать то что я захочу!"
                voice "audio/voices/chingis/27.mp3"
                chingis "Да, конечно, что ты хочешь?"
                voice "audio/voices/vika/368.mp3"
                Vika "Иди ко мне домой и почини розетку!"
                voice "audio/voices/chingis/28.mp3"
                chingis "Хорошо!"
                hide screen chingis
                $ rozetka_is_broken = False
                $ game_hour += 1
                $ update_game_time()
                $ rozetka_pochinena = True
                $ quest_list[5]["done"] = True
                pause 3.0
                show screen chingis
                $ _preferences.afm_enable = True 
                voice "audio/voices/chingis/7.mp3"
                chingis "Готово"
                voice "audio/voices/vika/369.mp3"
                Vika "Так быстро?"
                voice "audio/voices/chingis/29.mp3"
                chingis "Да, я же говорил, что я мастер, что мне сделать еще?"
                jump chingis_menu


        "Ты можешь починить розетку?" if rozetka_is_broken == True and i_know_sudoku == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/370.mp3"
            Vika "Ты можешь починить розетку?"
            voice "audio/voices/chingis/30.mp3"
            chingis "Я все магу!"
            voice "audio/voices/vika/371.mp3"
            Vika "Тогда поехали со мной, я живу тут не далеко..."
            voice "audio/voices/chingis/31.mp3"
            chingis "Нэ нэ нэ, сейчас нэ магу"
            voice "audio/voices/vika/372.mp3"
            Vika "Но мне срочно надо!!!"
            voice "audio/voices/chingis/32.mp3"
            chingis "Нэ магу, минэ брат написал что я тупой, и что я нэ смогу пройти игру. Минэ надо пройти и скинуть ему скрэншот, пока не пройду, никуда нэ поеду!"
            voice "audio/voices/vika/373.mp3"
            Vika "А если я за тебя пройду?"
            voice "audio/voices/chingis/33.mp3"
            chingis "Как ты пройдешь? Ты же женщина. Там очень сложный игра! Мой брат очень умный, он дал мне то, что я не могу пройти уже 2 часа."
            voice "audio/voices/vika/374.mp3"
            Vika "Если я все-таки за тебя пройду, ты починишь розетку бесплатно?"
            voice "audio/voices/chingis/34.mp3"
            chingis "АХАХАХХАХА, ну тогда скачай с эпстора, игра называется судоку. Если ты пройдешь, я буду весь день делать все что ты попросишь!"
            voice "audio/voices/vika/319.mp3"
            Vika "Договорились!"
            $ quest_list[6]["available"] = True
            $ vitya_rozetka = False
            $ i_know_sudoku = True
            jump chingis_menu
        
        "Мне нужно идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/chingis/35.mp3"
            chingis "Заходи еще"
            $ block_ui = False
            $ stop_dialog()
            jump masterskaya_inside

        


screen back_arrow_to_masterskaya:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("masterskaya")  # Показываем меню выбора  

screen police_map_point:
    if not block_ui:
        imagebutton:
            idle "police_map_idle.png"
            hover "police_map_hover.png"
            xpos 1305
            ypos 400
            focus_mask True
            at Transform(zoom=1.3)
            if makeup_level == 5:
                action Jump("need_bathroom")
            else:
                action Jump("police")  # Показываем меню выбора

label police:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "police")
    $ polojenie = "police" 
    play music "city.mp3" fadeout 1
    scene bg police_build
    show screen back_arrow_to_map
    show screen door_to_police
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen door_to_police:
    imagebutton:
        idle "police/door_to_police.png"
        focus_mask True
        if not block_ui:
            hover "police/door_to_police_hover.png"
            action Jump("police_hall")

label police_hall:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg police_hall
    show screen back_arrow_to_police
    show screen veshi_door
    show screen main_ment_door
    show screen ment_door
    stop music fadeout 1
    if clara_suck_now == True:
        play music "zhenskie-stony.mp3" fadeout 1
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen veshi_door:
    imagebutton:
        idle "police/veshi_door.png"
        focus_mask True
        if not block_ui:
            hover "police/veshi_door_hover.png"
            if clara_suck_now == True:
                action Jump("stoni")
            else:
                if "keys" in inventory_items:
                    action Jump("veshdok")
                else:
                    action Jump("need_police")

label need_police:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/375.mp3"
    Vika "Туда лучше не заходить."
    $ block_ui = False
    $ stop_dialog()
    jump police_hall

label stoni:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/376.mp3"
    Vika "Клара уже работает, лучше ей не мешать."
    $ block_ui = False
    $ stop_dialog()
    jump police_hall

label veshdok:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg veshdok
    show screen back_arrow_to_police_hall
    if i_do_papki != "done":
        show screen box
    $ show_hud()
    if i_do_papki == "done" and i_say_done == False:
        $ _preferences.afm_enable = True 
        $ renpy.music.set_pause(True)
        $ start_dialog()
        voice "audio/voices/vika/377.mp3"
        Vika "Ну, вроде все правильно!"
        $ quest_list[20]["done"] = True
        $ intellect += 1
        $ game_hour += 1
        $ update_game_time()
        $ i_say_done = True
        $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen back_arrow_to_police_hall:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("police_hall") 

screen box:
    imagebutton:
        idle "police/box.png"
        focus_mask True
        if not block_ui:
            hover "police/box_hover.png"
            action Jump("folder_sort_game")

label folder_sort_game:
    $ hide_all_ui()
    $ show_hud()
    show screen folder_sort_game
    show screen folder_sort_game_delete
    show screen label1
    show screen label2
    show screen label3
    show screen label4
    show screen label5
    show screen label6
    show screen zona1
    show screen zona2
    show screen zona3
    show screen zona4
    show screen zona5
    show screen zona6
    show screen krest
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

init python:
    def check_all_papki_and_jump():
        global i_do_papki
        global ment_is_here
        if all([papka1, papka2, papka3, papka4, papka5, papka6]):
            ment_is_here = False
            i_do_papki = "done"
            renpy.jump("veshdok")

screen krest:
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Jump("veshdok")

screen folder_sort_game:
    add "box_with_folders.png"

screen folder_sort_game_delete:
    imagebutton:
        idle "box_with_folders_delete.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "label1":
                action [SetVariable("default_mouse", "default"), Show("label1")]
            if default_mouse == "label2":
                action [SetVariable("default_mouse", "default"), Show("label2")]
            if default_mouse == "label3":
                action [SetVariable("default_mouse", "default"), Show("label3")]
            if default_mouse == "label4":
                action [SetVariable("default_mouse", "default"), Show("label4")]
            if default_mouse == "label5":
                action [SetVariable("default_mouse", "default"), Show("label5")]
            if default_mouse == "label6":
                action [SetVariable("default_mouse", "default"), Show("label6")]
    

screen label1:
    imagebutton:
        idle "dela/label1_button.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "default":
                action [SetVariable("default_mouse", "label1"), Hide("label1")]

screen zona1:
    imagebutton:
        idle "dela/zona1.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "label1":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona1"),
                    Show("label1_zona", x=623, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label2":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona1"),
                    Show("label2_zona", x=623, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label3":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona1"),
                    Show("label3_zona", x=623, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label4":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona1"),
                    Show("label4_zona", x=623, y=620),
                    SetVariable("papka1", True),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label5":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona1"),
                    Show("label5_zona", x=623, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label6":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona1"),
                    Show("label6_zona", x=623, y=620),
                    Function(check_all_papki_and_jump)
                ]

screen zona2:
    imagebutton:
        idle "dela/zona2.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "label1":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona2"),
                    Show("label1_zona", x=737, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label2":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona2"),
                    Show("label2_zona", x=737, y=620),
                    SetVariable("papka2", True),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label3":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona2"),
                    Show("label3_zona", x=737, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label4":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona2"),
                    Show("label4_zona", x=737, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label5":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona2"),
                    Show("label5_zona", x=737, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label6":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona2"),
                    Show("label6_zona", x=737, y=620),
                    Function(check_all_papki_and_jump)
                ]

screen zona3:
    imagebutton:
        idle "dela/zona3.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "label1":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona3"),
                    Show("label1_zona", x=851, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label2":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona3"),
                    Show("label2_zona", x=851, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label3":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona3"),
                    Show("label3_zona", x=851, y=620),
                    SetVariable("papka3", True),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label4":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona3"),
                    Show("label4_zona", x=851, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label5":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona3"),
                    Show("label5_zona", x=851, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label6":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona3"),
                    Show("label6_zona", x=851, y=620),
                    Function(check_all_papki_and_jump)
                ]

screen zona4:
    imagebutton:
        idle "dela/zona4.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "label1":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona4"),
                    Show("label1_zona", x=965, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label2":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona4"),
                    Show("label2_zona", x=965, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label3":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona4"),
                    Show("label3_zona", x=965, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label4":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona4"),
                    Show("label4_zona", x=965, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label5":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona4"),
                    Show("label5_zona", x=965, y=620),
                    SetVariable("papka4", True),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label6":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona4"),
                    Show("label6_zona", x=965, y=620),
                    Function(check_all_papki_and_jump)
                ]

screen zona5:
    imagebutton:
        idle "dela/zona5.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "label1":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona5"),
                    Show("label1_zona", x=1079, y=620),
                    SetVariable("papka5", True),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label2":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona5"),
                    Show("label2_zona", x=1079, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label3":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona5"),
                    Show("label3_zona", x=1079, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label4":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona5"),
                    Show("label4_zona", x=1079, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label5":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona5"),
                    Show("label5_zona", x=1079, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label6":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona5"),
                    Show("label6_zona", x=1079, y=620),
                    Function(check_all_papki_and_jump)
                ]

screen zona6:
    imagebutton:
        idle "dela/zona6.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "label1":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona6"),
                    Show("label1_zona", x=1193, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label2":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona6"),
                    Show("label2_zona", x=1193, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label3":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona6"),
                    Show("label3_zona", x=1193, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label4":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona6"),
                    Show("label4_zona", x=1193, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label5":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona6"),
                    Show("label5_zona", x=1193, y=620),
                    Function(check_all_papki_and_jump)
                ]
            elif default_mouse == "label6":
                action [
                    SetVariable("default_mouse", "default"),
                    Hide("zona6"),
                    Show("label6_zona", x=1193, y=620),
                    SetVariable("papka6", True),
                    Function(check_all_papki_and_jump)
                ]

screen label1_zona(x=0, y=0):
    zorder 1
    imagebutton:
        idle "icon/label1.png"
        focus_mask True
        xpos x
        ypos y
        if not block_ui and default_mouse == "default":
            action [
                SetVariable("default_mouse", "label1"),
                Hide("label1_zona"),
                Show("zona1"),
                Show("zona2"),
                Show("zona3"),
                Show("zona4"),
                Show("zona5"),
                Show("zona6"),
                SetVariable("papka5", False)
            ]

screen label2_zona(x=0, y=0):
    zorder 1
    imagebutton:
        idle "icon/label2.png"
        focus_mask True
        xpos x
        ypos y
        if not block_ui and default_mouse == "default":
            action [
                SetVariable("default_mouse", "label2"),
                Hide("label2_zona"),
                Show("zona1"),
                Show("zona2"),
                Show("zona3"),
                Show("zona4"),
                Show("zona5"),
                Show("zona6"),
                SetVariable("papka2", False)  # или нужную зонуprint(papka1, papka2, papka3, papka4, papka5, papka6)
            ]

screen label3_zona(x=0, y=0):
    zorder 1
    imagebutton:
        idle "icon/label3.png"
        focus_mask True
        xpos x
        ypos y
        if not block_ui and default_mouse == "default":
            action [
                SetVariable("default_mouse", "label3"),
                Hide("label3_zona"),
                Show("zona1"),
                Show("zona2"),
                Show("zona3"),
                Show("zona4"),
                Show("zona5"),
                Show("zona6"),
                SetVariable("papka3", False)  # или нужную зону
            ]

screen label4_zona(x=0, y=0):
    zorder 1
    imagebutton:
        idle "icon/label4.png"
        focus_mask True
        xpos x
        ypos y
        if not block_ui and default_mouse == "default":
            action [
                SetVariable("default_mouse", "label4"),
                Hide("label4_zona"),
                Show("zona1"),
                Show("zona2"),
                Show("zona3"),
                Show("zona4"),
                Show("zona5"),
                Show("zona6"),
                SetVariable("papka1", False)
            ]

screen label5_zona(x=0, y=0):
    zorder 1
    imagebutton:
        idle "icon/label5.png"
        focus_mask True
        xpos x
        ypos y
        if not block_ui and default_mouse == "default":
            action [
                SetVariable("default_mouse", "label5"),
                Hide("label5_zona"),
                Show("zona1"),
                Show("zona2"),
                Show("zona3"),
                Show("zona4"),
                Show("zona5"),
                Show("zona6"),
                SetVariable("papka4", False)  # или нужную зону
            ]
screen label6_zona(x=0, y=0):
    zorder 1
    imagebutton:
        idle "icon/label6.png"
        focus_mask True
        xpos x
        ypos y
        if not block_ui and default_mouse == "default":
            action [
                SetVariable("default_mouse", "label6"),
                Hide("label6_zona"),
                Show("zona1"),
                Show("zona2"),
                Show("zona3"),
                Show("zona4"),
                Show("zona5"),
                Show("zona6"),
                SetVariable("papka6", False)  # или нужную зону
            ]

screen label2:
    imagebutton:
        idle "dela/label2_button.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "default":
                action [SetVariable("default_mouse", "label2"), Hide("label2")]

screen label3:
    imagebutton:
        idle "dela/label3_button.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "default":
                action [SetVariable("default_mouse", "label3"), Hide("label3")]

screen label4:
    imagebutton:
        idle "dela/label4_button.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "default":
                action [SetVariable("default_mouse", "label4"), Hide("label4")]

screen label5:
    imagebutton:
        idle "dela/label5_button.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "default":
                action [SetVariable("default_mouse", "label5"), Hide("label5")]

screen label6:
    imagebutton:
        idle "dela/label6_button.png"
        focus_mask True
        if not block_ui:
            if default_mouse == "default":
                action [SetVariable("default_mouse", "label6"), Hide("label6")]


screen main_ment_door:
    imagebutton:
        idle "police/main_ment_door.png"
        focus_mask True
        if not block_ui:
            hover "police/main_ment_door_hover.png"
            action Jump("main_ment_door_monolog")

screen ment_door:
    imagebutton:
        idle "police/ment_door.png"
        focus_mask True
        if not block_ui:
            hover "police/ment_door_hover.png"
            action Jump("ment_room")

label ment_room:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg ment_room
    show screen back_arrow_to_police_hall
    if ment_is_here == True:
        show screen ment
    else:
        show screen ment_notebook
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen ment_notebook:
    imagebutton:
        idle "police/ment_notebook.png"
        focus_mask True
        if not block_ui:
            hover "police/ment_notebook_hover.png"
            action Jump("ment_notebook")

label ment_notebook:
    $ hide_all_ui()
    scene bg telegramm
    show screen back_arrow_to_ment_room
    pause 2.0
    if i_saw_telegramm == False:
        $ renpy.music.set_pause(True)
        $ start_dialog()
        voice "audio/voices/vika/378.mp3"
        Vika "Хмм... Так эта женщина любит его, а он ее просто использует."
        $ stop_dialog()
        $ i_saw_telegramm = True
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen back_arrow_to_ment_room:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("ment_room") 

screen ment:
    imagebutton:
        idle "police/ment.png"
        focus_mask True
        if not block_ui:
            hover "police/ment_hover.png"
            action Jump("ment_dialog")

label ment_dialog:
    $ renpy.music.set_pause(True)
    $ block_ui = True
    $ start_dialog()
    if ment_first_dialog == True:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/379.mp3"
        Vika "Здравствуйте, мне пришло странное сообщение..."
        voice "audio/voices/ment/1.mp3"
        ment "А, Башкова ну проходи, садись. Тебе не говорили что мухлевать в казино плохо?" 
        voice "audio/voices/vika/380.mp3"
        Vika "Эмм, я не мухлевала в казино..."
        voice "audio/voices/ment/2.mp3"
        ment "Ага, прям так я и поверил, а если я обыщу тебя? Я найду там кубик из казино? Давай его сюда."
        $ remove_item_to_inventory("dice_with_gvozd_colour")
        voice "audio/voices/vika/381.mp3"
        Vika "Ладно держите."
        voice "audio/voices/ment/3.mp3"
        ment "Сама догадалась или помогли?"
        voice "audio/voices/vika/382.mp3"
        Vika "Сама..."
        voice "audio/voices/ment/4.mp3"
        ment "Хмм, а как же тот китаец, который 'перепутал машину' возле казино?"
        voice "audio/voices/vika/383.mp3"
        Vika "Не знаю я никакого китайца, возможно вы реально арестовали человека, который перепутал машину."
        voice "audio/voices/ment/5.mp3"
        ment "Ну тогда тебе надо поблагодарить его, потому что если бы он не отвлек нас, мы бы взяли тебя с поличным"
        voice "audio/voices/vika/384.mp3"
        Vika "Да пофигу на китайца, со мной то что?"
        voice "audio/voices/ment/6.mp3"
        ment "Ну тебе светит до двух лет, не слишком большой срок, но и его можно сократить"
        voice "audio/voices/vika/385.mp3"
        Vika "Да да да, год за хорошее поведение, я знаю."
        voice "audio/voices/ment/7.mp3"
        ment "Можно год за хорошее поведение, а можно вообще не сидеть за хорошее поведение..."
        voice "audio/voices/vika/386.mp3"
        Vika "Это как?"
        voice "audio/voices/ment/8.mp3"
        ment "Ну если ты будешь себя хорошо вести, то не только не отсидишь, но и вообще дела не будет."
        voice "audio/voices/ment/9.mp3"
        ment "А сейчас приниси ка мне пива немецкого в барном стакане и рыбы красноперки, Рыбу бери только в рыбной лавке в микрорайоне монтажников"
        voice "audio/voices/vika/387.mp3"
        Vika "Вы замнёте мне дело, за то что я куплю вам пиво и рыбу?"
        voice "audio/voices/ment/10.mp3"
        ment "Ах да и еще подпиши ка подписку о невыезде, чтоб не сбежала никуда."
        voice "audio/voices/vika/388.mp3"
        Vika "Эх, плакал мой питер..."
        voice "audio/voices/ment/11.mp3"
        ment "А теперь пшла вон отсюда, и без пива с рыбой не возвращайся."
        $ i_know_casino = False
        $ quest_list[17]["done"] = True
        $ quest_list[18]["available"] = True
        $ game_hour += 1
        $ update_game_time()
        $ ment_first_dialog = False
        $ i_know_fishstore = True
        jump ment_menu
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/ment/12.mp3"
        ment "Да?"
        jump ment_menu

label ment_menu:
    $ stop_dialog()
    menu:
        "Я сделала все что вы просили" if masha_and_husband_dialog == True and need_suck == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/389.mp3"
            Vika "Я сделала все что вы просили."
            voice "audio/voices/ment/13.mp3"
            ment "Молодец, слушай следующее задание"
            $ remove_item_to_inventory("keys")
            $ remove_item_to_inventory("listok")
            voice "audio/voices/vika/390.mp3"
            Vika "Может хватит уже?"
            voice "audio/voices/ment/14.mp3"
            ment "Здесь я решаю когда хватит! В общем та пианистка начала что-то подозревать и дала заднюю, теперь у меня ни бабы ни связей в школе!"
            voice "audio/voices/ment/15.mp3"
            ment "А так как ты тоже работаешь на меня, ты ее полностью заменишь"
            voice "audio/voices/vika/391.mp3"
            Vika "Как вы себе представляете чтоб я заменила ее в школе?"
            voice "audio/voices/ment/16.mp3"
            ment "При чем тут школа? Ты заменишь другую часть ее работы, сегодня вечером в комнате вещдоков"
            voice "audio/voices/vika/392.mp3"
            Vika "Вы в своем уме, вообще-то я замужем!!!"
            voice "audio/voices/ment/17.mp3"
            ment "Меня это мало волнует, делай что хочешь, но сегодня вечером кто-то должен поработать ртом. А теперь вали отсюда"
            $ quest_list[23]["done"] = True
            $ quest_list[24]["available"] = True
            $ need_suck = True
            $ block_ui = False
            $ stop_dialog()
            jump ment_room
        "Я принесла вам пиво и рыбу" if "krasnoperka" in inventory_items and "glass_of_beer" in inventory_items:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/393.mp3"
            Vika "Я принесла вам пиво и рыбу."
            voice "audio/voices/ment/18.mp3"
            ment "Хмм... Рыба и правда красноперка, а вот пиво... оно точно немецкое?"
            voice "audio/voices/vika/394.mp3"
            Vika "Точно"
            voice "audio/voices/ment/19.mp3"
            ment "А ну ка докажи, а то что-то оно очень на уренгойское похоже..."
            if "german_beer" in inventory_items:
                $ _preferences.afm_enable = True 
                voice "audio/voices/vika/395.mp3"
                Vika "Вот, у меня есть банка"
                voice "audio/voices/ment/20.mp3"
                ment "Ну ладно, значит и немецкое пиво совсем испортилось"
                $ intellect += 1
                $ remove_item_to_inventory("krasnoperka")
                $ remove_item_to_inventory("glass_of_beer")
                $ remove_item_to_inventory("german_beer")
                voice "audio/voices/ment/21.mp3"
                ment "Твое следующее задание, иди в вещдок комнату, найди коробку с документами и сложи их нормально, а то меня начальник задолбал своим порядком"
                voice "audio/voices/ment/22.mp3"
                ment "Когда закончишь, занесешь ключи сюда, меня не будет. Поэтому вот тебе сразу еще одно задание:"
                voice "audio/voices/ment/23.mp3"
                ment "Иди в музыкальную школу, и зайди в класс пианино, тебе надо отыскать там тайник, и принести мне то что там лежит"
                voice "audio/voices/vika/396.mp3"
                Vika "А почему вы сами не заберете?"
                voice "audio/voices/ment/24.mp3"
                ment "Во-первых это не твое дело... А во-вторых, там для меня его спрятала пианистка, и не хочет отдавать, потому что боится..."
                voice "audio/voices/ment/25.mp3"
                ment "Зачем я тебе вообще это рассказываю... Иди и выполняй!"
                $ quest_list[18]["done"] = True
                $ quest_list[20]["available"] = True
                $ quest_list[21]["available"] = True
                $ game_hour += 1
                $ update_game_time()
                $ i_know_school = True
                $ add_item_to_inventory("keys")
                $ block_ui = False
                $ stop_dialog()
                jump ment_room
            else:
                $ _preferences.afm_enable = True 
                voice "audio/voices/vika/397.mp3"
                Vika "Я не знаю как доказать."
                voice "audio/voices/ment/26.mp3"
                ment "Ты что думаешь, я обоссаное уренгойское пиво не узнаю, а ну быстро пошла и принесла мне нормальное"
                $ block_ui = False
                $ stop_dialog()
                jump ment_room
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/ment/27.mp3"
            ment "Иди"
            $ block_ui = False
            $ stop_dialog()
            jump ment_room


screen back_arrow_to_police:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("police")  

label casino:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ travel(polojenie, "casino")
    $ polojenie = "casino" 
    play music "city.mp3" fadeout 1
    scene bg casino
    show screen back_arrow_to_map
    show screen sportcar
    show screen door_to_casino
    $ show_hud()

    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen door_to_casino:
    if not block_ui:
        imagebutton:
            idle "door_to_casino_idle.png"
            hover "door_to_casino_hover.png"
            focus_mask True
            action Jump("casino_hall")  # Показываем меню выбора    

screen sportcar:
    if not block_ui:
        imagebutton:
            idle "sportcar_idle.png"
            hover "sportcar_hover.png"
            focus_mask True
            action Jump("Cool_car")  # Показываем меню выбора

label Cool_car:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/398.mp3"
    Vika "Крутая машина, интересно кому она принадлежит... Может быть хозяину казино?"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen bar_map_point:
    if not block_ui:
        imagebutton:
            idle "bar_map_idle.png"
            hover "bar_map_hover.png"
            xpos 510
            ypos 550
            focus_mask True
            at Transform(zoom=1.3)
            if makeup_level == 5:
                action Jump("need_bathroom")
            elif clara_suck_now == True:
                action Jump("another_deal")
            else:
                action Jump("vhod_v_bar")  # Показываем меню выбора

label casino_hall:
    $ renpy.free_memory()
    scene bg casino_hall
    $ hide_all_ui()
    show screen back_arrow_to_casino
    show screen door_kosti
    show screen door_ruletka
    show screen door_karti
    play music "casino.mp3" fadeout 1
    $ polojenie = "casino_hall"
    $ show_hud()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return


screen door_kosti:
    if not block_ui:
        imagebutton:
            idle "door_kosti_idle.png"
            hover "door_kosti_hover.png"
            focus_mask True
            action Jump("dice")  # Показываем меню выбора

label kosti:
    $ stop_dialog()
    $ renpy.free_memory()
    scene bg kosti
    $ hide_all_ui()
    show screen money
    show screen inventory_bag
    show screen back_arrow_to_casino_hall
    show screen odd
    show screen even
    show screen odintri
    show screen chetireshest
    show screen odin2
    show screen tri4
    show screen pyat6
    show screen odyn
    show screen dva
    show screen tri
    show screen chetire
    show screen pyat
    show screen shest
    if resoult_kosti == 6:
        show screen kost6
    elif resoult_kosti == 5:
        show screen kost5
    elif resoult_kosti == 4:
        show screen kost4
    elif resoult_kosti == 3:
        show screen kost3
    elif resoult_kosti == 2:
        show screen kost2
    elif resoult_kosti == 1:
        show screen kost1
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen money:
    text "Деньги: [money]₽"

init python:
    import random

    def get_random_dice():
        return random.randint(1, 6)


screen kost1:
    if not block_ui:
        imagebutton:
            idle "kosti/dice_1.png"
            hover "kosti/dice_1_hover.png"
            focus_mask True
            action Jump("igra_kosti")  # Показываем меню выбора    

screen kost2:
    if not block_ui:
        imagebutton:
            idle "kosti/dice_2.png"
            hover "kosti/dice_2_hover.png"
            focus_mask True
            action Jump("igra_kosti")  # Показываем меню выбора    

screen kost3:
    if not block_ui:
        imagebutton:
            idle "kosti/dice_3.png"
            hover "kosti/dice_3_hover.png"
            focus_mask True
            action Jump("igra_kosti")  # Показываем меню выбора    

screen kost4:
    if not block_ui:
        imagebutton:
            idle "kosti/dice_4.png"
            hover "kosti/dice_4_hover.png"
            focus_mask True
            action Jump("igra_kosti")  # Показываем меню выбора    

screen kost5:
    if not block_ui:
        imagebutton:
            idle "kosti/dice_5.png"
            hover "kosti/dice_5_hover.png"
            focus_mask True
            action Jump("igra_kosti")  # Показываем меню выбора    

screen kost6:
    if not block_ui:
        imagebutton:
            idle "kosti/dice_6.png"
            hover "kosti/dice_6_hover.png"
            focus_mask True
            action Jump("igra_kosti")  # Показываем меню выбора    

screen odd:
    if not block_ui:
        imagebutton:
            if selected_kosti == "odd":
                idle "kosti/odd_hover.png"  
            else:
                idle "kosti/odd_idle.png"
            hover "kosti/odd_hover.png"
            focus_mask True
            action If(
                selected_kosti == "odd",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "odd")
            )
screen even:
    if not block_ui:
        imagebutton:
            if selected_kosti == "even":
                idle "kosti/even_hover.png"  
            else:
                idle "kosti/even_idle.png"
            hover "kosti/even_hover.png"
            focus_mask True
            action If(
                selected_kosti == "even",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "even")
            )

screen odintri:
    if not block_ui:
        imagebutton:
            if selected_kosti == "odintri":
                idle "kosti/1-3_hover.png"  
            else:
                idle "kosti/1-3_idle.png"
            hover "kosti/1-3_hover.png"
            focus_mask True
            action If(
                selected_kosti == "odintri",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "odintri")
            )

screen chetireshest:
    if not block_ui:
        imagebutton:
            if selected_kosti == "chetireshest":
                idle "kosti/4-6_hover.png"  
            else:
                idle "kosti/4-6_idle.png"
            hover "kosti/4-6_hover.png"
            focus_mask True
            action If(
                selected_kosti == "chetireshest",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "chetireshest")
            )

screen odin2:
    if not block_ui:
        imagebutton:
            if selected_kosti == "odin2":
                idle "kosti/1,2_hover.png"  
            else:
                idle "kosti/1,2_idle.png"
            hover "kosti/1,2_hover.png"
            focus_mask True
            action If(
                selected_kosti == "odin2",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "odin2")
            )

screen tri4:
    if not block_ui:
        imagebutton:
            if selected_kosti == "tri4":
                idle "kosti/3,4_hover.png"  
            else:
                idle "kosti/3,4_idle.png"
            hover "kosti/3,4_hover.png"
            focus_mask True
            action If(
                selected_kosti == "tri4",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "tri4")
            )

screen pyat6:
    if not block_ui:
        imagebutton:
            if selected_kosti == "pyat6":
                idle "kosti/5,6_hover.png"  
            else:
                idle "kosti/5,6_idle.png"
            hover "kosti/5,6_hover.png"
            focus_mask True
            action If(
                selected_kosti == "pyat6",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "pyat6")
            )

screen odyn:
    if not block_ui:
        imagebutton:
            if selected_kosti == "odyn":
                idle "kosti/1_hover.png"  
            else:
                idle "kosti/1_idle.png"
            hover "kosti/1_hover.png"
            focus_mask True
            action If(
                selected_kosti == "odyn",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "odyn")
            )

screen dva:
    if not block_ui:
        imagebutton:
            if selected_kosti == "dva":
                idle "kosti/2_hover.png"  
            else:
                idle "kosti/2_idle.png"
            hover "kosti/2_hover.png"
            focus_mask True
            action If(
                selected_kosti == "dva",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "dva")
            )

screen tri:
    if not block_ui:
        imagebutton:
            if selected_kosti == "tri":
                idle "kosti/3_hover.png"  
            else:
                idle "kosti/3_idle.png"
            hover "kosti/3_hover.png"
            focus_mask True
            action If(
                selected_kosti == "tri",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "tri")
            )

screen chetire:
    if not block_ui:
        imagebutton:
            if selected_kosti == "chetire":
                idle "kosti/4_hover.png"  
            else:
                idle "kosti/4_idle.png"
            hover "kosti/4_hover.png"
            focus_mask True
            action If(
                selected_kosti == "chetire",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "chetire")
            )

screen pyat:
    if not block_ui:
        imagebutton:
            if selected_kosti == "pyat":
                idle "kosti/5_hover.png"  
            else:
                idle "kosti/5_idle.png"
            hover "kosti/5_hover.png"
            focus_mask True
            action If(
                selected_kosti == "pyat",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "pyat")
            )

screen shest:
    if not block_ui:
        imagebutton:
            if selected_kosti == "shest":
                idle "kosti/6_hover.png"  
            else:
                idle "kosti/6_idle.png"
            hover "kosti/6_hover.png"
            focus_mask True
            action If(
                selected_kosti == "shest",
                SetVariable("selected_kosti", None),
                SetVariable("selected_kosti", "shest")
            )

label igra_kosti:
    $ renpy.free_memory()
    $ renpy.music.set_pause(True)
    if money < 100:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/399.mp3"
        Vika "У меня недостаточно денег."
        jump kosti
    elif default_mouse == "dice_with_gvozd_colour" and money >= 2000:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/400.mp3"
        Vika "(У меня уже много денег, я рискую спалиться выбрасывая каждый раз одно и то же число, надо придумать как заработать еще)"
        jump kosti
    elif default_mouse == "dice_with_gvozd_colour" and selected_kosti != "shest":
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/401.mp3"
        Vika "(Я настроила кубик на шесть, выгоднее будет поставить только на шестерку)"
        jump kosti
    elif selected_kosti == None:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/402.mp3"
        Vika "Я не выбрала режим"
        jump kosti
    else:
        $ money -= 100
        $ block_ui = True
        if default_mouse == "dice_with_gvozd_colour":
            $ resoult_kosti = 6
            $ quest_list[10]["done"] = True
            $ intellect += 1
        else:
            $ resoult_kosti = get_random_dice()
        $ start_dialog()
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.1
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.1
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.1
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.1
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.1
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.1
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.1
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.3
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.3
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.3
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.3
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.5
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(show_dice) at truecenter
        pause 0.5
        hide expression "kosti/dice_{}.png".format(show_dice) at truecenter
        $ show_dice = get_random_dice()
        show expression "kosti/dice_{}.png".format(resoult_kosti) at truecenter
        pause 0.5
        if selected_kosti == "odd" and (resoult_kosti == 1 or resoult_kosti == 3 or resoult_kosti == 5):
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли!"
            $ money += 200
        elif selected_kosti == "even" and (resoult_kosti == 2 or resoult_kosti == 4 or resoult_kosti == 6): 
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 200  
        elif selected_kosti == "odintri" and (resoult_kosti == 1 or resoult_kosti == 2 or resoult_kosti == 3): 
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 200
        elif selected_kosti == "chetireshest" and (resoult_kosti == 4 or resoult_kosti == 5 or resoult_kosti == 6):
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли" 
            $ money += 200
        elif selected_kosti == "odin2" and (resoult_kosti == 1 or resoult_kosti == 2): 
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 300
        elif selected_kosti == "tri4" and (resoult_kosti == 3 or resoult_kosti == 4): 
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 300
        elif selected_kosti == "pyat6" and (resoult_kosti == 5 or resoult_kosti == 6): 
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 300
        elif selected_kosti == "odyn" and (resoult_kosti == 1): 
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 600
        elif selected_kosti == "dva" and (resoult_kosti == 2): 
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 600
        elif selected_kosti == "tri" and (resoult_kosti == 3):
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 600
        elif selected_kosti == "chetire" and (resoult_kosti == 4):
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 600
        elif selected_kosti == "pyat" and (resoult_kosti == 5): 
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 600
        elif selected_kosti == "shest" and (resoult_kosti == 6): 
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ money += 600
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/2.mp3"
            diller "Вы проиграли"
        if first_game_dice == True:
            $ first_game_dice = False
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/3.mp3"
            diller "За первую игру в кости в нашем клубе, вы получаете сувенирные кости."
            $ quest_list[10]["available"] = True
            $ add_item_to_inventory("dice")
        $ stop_dialog()
        $ block_ui = False
        jump kosti


screen back_arrow_to_casino_hall:
    if not block_ui:
        imagebutton:
            idle "back_arrow_to_casino_hall_idle.png"
            hover "back_arrow_to_casino_hall_hover.png"
            focus_mask True
            action Jump("dice")  # Показываем меню выбора

screen back_arrow_to_casino_hall2:
    if not block_ui:
        imagebutton:
            idle "back_arrow_to_casino_hall_idle.png"
            hover "back_arrow_to_casino_hall_hover.png"
            focus_mask True
            action Jump("ruletka")  # Показываем меню выбора               

screen back_arrow_to_casino_hal3:
    if not block_ui:
        imagebutton:
            idle "back_arrow_to_casino_hall_idle.png"
            hover "back_arrow_to_casino_hall_hover.png"
            focus_mask True
            action Jump("cards")  # Показываем меню выбора

screen door_ruletka:
    if not block_ui:
        imagebutton:
            idle "door_ruletka_idle.png"
            hover "door_ruletka_hover.png"
            focus_mask True
            action Jump("ruletka")  # Показываем меню выбора

label ruletka:
    $ hide_all_ui()
    $ show_hud()
    scene bg ruletka
    show screen back_arrow_to_casino_hall_ruletka
    show screen roulette
    if diller_is_here == True:
        show screen diller_3
    show screen roulette_field
    show screen roulette_ball
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return 

screen roulette:
    if not block_ui:
        imagebutton:
            idle "roulette/roulette.png"
            hover "roulette/roulette_hover.png"
            focus_mask True
            if default_mouse == "magnet_with_clay" and diller_is_here == False:
                action Jump("magnet_roulette")
            elif default_mouse == "magnet_with_clay" and diller_is_here == True:
                action Jump("diller_tut")
            else:
                action Jump("roulette")

label magnet_roulette:
    $ block_ui = True
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/403.mp3"
    Vika "Посталю ка я его под цифрой 21."
    $ remove_item_to_inventory("magnet_with_clay")
    $ default_mouse = "default"
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/404.mp3"
    Vika "Теперь он будет магнитить все металлическое."
    $ magnet_v_rouletke = True
    if ball_v_rouletke == True:
        pause 3.0
        $ diller_is_here = True
        $ _preferences.afm_enable = True 
        voice "audio/voices/diller/4.mp3"
        diller "Спасибо что сказала, там какойто узбек пытался вскрыть мою тачку!"
        voice "audio/voices/vika/405.mp3"
        Vika "Пожалуйста!"
    $ block_ui = False
    jump ruletka

label diller_tut:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/406.mp3"
    Vika "Я не смогу сделать это пока диллер тут."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return 

label roulette:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/407.mp3"
    Vika "Это рулетка, на нее бросают шарик."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen diller_3:
    imagebutton:
        idle "roulette/diller_3.png"
        focus_mask True
        if not block_ui:
            hover "roulette/diller_3_hover.png"
            action Jump("dialog_diller_3")

label dialog_diller_3:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    voice "audio/voices/diller/5.mp3"
    $ _preferences.afm_enable = True 
    diller "Хотите узнать правила игры?"
    $ stop_dialog()
    menu:
        "Да":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/6.mp3"
            diller "Все просто, выбираете режим и делаете ставку 2000р"
            voice "audio/voices/diller/7.mp3"
            diller "Цифры показывают диапазон или конкретно выпавшее число"
            voice "audio/voices/diller/8.mp3"
            diller "odd и even это нечетные и четные числа"
            voice "audio/voices/diller/9.mp3"
            diller "Красное и черное означает цвет клетки на которую падает шарик"
            voice "audio/voices/diller/10.mp3"
            diller "После сделанной ставки я раскручу рулетку и брошу на нее шарик"
            voice "audio/voices/diller/11.mp3"
            diller "Где он остановится, то число и считается выйгрышным"
            voice "audio/voices/diller/12.mp3"
            diller "Если выпадет зеро, то выйграют игроки которые поставили только на зеро."
        "Нет":
            pass
        "Вас позвал хозяин казино" if "ball_white" in inventory_items and "magnet_with_clay" in inventory_items:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/408.mp3"
            Vika "Вас позвал хозяин казино."
            voice "audio/voices/diller/13.mp3"
            diller "Скажите ему что я не могу подойти, я работаю."
        "Там кто-то трется у машины" if "ball_white" in inventory_items and "magnet_with_clay" in inventory_items and car_is_broken == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/409.mp3"
            Vika "Там кто-то трется у машины."
            voice "audio/voices/diller/14.mp3"
            diller "У моей ласточки??? Стой тут, и ничего не трогай, я сейчас вернусь"
            $ diller_is_here = False
    $ block_ui = False
    $ stop_dialog()
    jump ruletka 


screen roulette_field:
    if not block_ui:
        imagebutton:
            idle "roulette/roulette_field.png"
            hover "roulette/roulette_field_hover.png"
            focus_mask True
            action Jump("play_roulette")  # Показываем меню выбора

screen roulette_ball:
    if not block_ui:
        imagebutton:
            idle "roulette/roulette_ball.png"
            hover "roulette/roulette_ball_hover.png"
            focus_mask True
            if default_mouse == "ball_white" and diller_is_here == False:
                action Jump("ball_roulette")
            elif default_mouse == "ball_white" and diller_is_here == True:
                action Jump("diller_tut")
            else:
                action Jump("roulette_ball")  # Показываем меню выбора

label ball_roulette:
    $ block_ui = True
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/410.mp3"
    Vika "Поменяю ка я эти шарики, так будет лучше."
    $ remove_item_to_inventory("ball_white")
    $ default_mouse = "default"
    $ ball_v_rouletke = True
    if magnet_v_rouletke == True:
        pause 3.0
        $ diller_is_here = True
        $ _preferences.afm_enable = True 
        voice "audio/voices/diller/4.mp3"
        diller "Спасибо что сказала, там какойто узбек пытался вскрыть мою тачку"
        voice "audio/voices/vika/405.mp3"
        Vika "Пожалуйста!"
    $ block_ui = False
    jump ruletka

label roulette_ball:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/411.mp3"
    Vika "Это шарик который диллер кидает в рулетку."
    $ block_ui = False
    $ stop_dialog()
    jump ruletka

label play_roulette:
    $ quest_list[11]["available"] = True
    $ renpy.free_memory()
    $ hide_all_ui()
    show screen money
    show screen inventory_bag
    show screen back_arrow_to_casino_hall2
    show screen start_roulette
    show screen zero
    show screen roulette1
    show screen roulette2
    show screen roulette3
    show screen roulette4
    show screen roulette5
    show screen roulette6
    show screen roulette7
    show screen roulette8
    show screen roulette9
    show screen roulette10
    show screen roulette11
    show screen roulette12
    show screen roulette13
    show screen roulette14
    show screen roulette15
    show screen roulette16
    show screen roulette17
    show screen roulette18
    show screen roulette19
    show screen roulette20
    show screen roulette21
    show screen roulette22
    show screen roulette23
    show screen roulette24
    show screen roulette25
    show screen roulette26
    show screen roulette27
    show screen roulette28
    show screen roulette29
    show screen roulette30
    show screen roulette31
    show screen roulette32
    show screen roulette33
    show screen roulette34
    show screen roulette35
    show screen roulette36
    show screen roulette1_34
    show screen roulette2_35
    show screen roulette3_36
    show screen roulette_1st12
    show screen roulette_2nd12
    show screen roulette_3rd12
    show screen roulette_1to18
    show screen roulette_even
    show screen roulette_red
    show screen roulette_black
    show screen roulette_odd
    show screen roulette_19to36
    scene bg play_roulette
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return 

screen start_roulette:
    if not block_ui:
        imagebutton:
            idle "roulette/start.png"
            hover "roulette/start_hover.png"
            focus_mask True
            action Jump("igra_roulette")  # Показываем меню выбора

screen roulette1_34:
    if not block_ui:
        imagebutton:
            if selected_roulette == "1_34":
                idle "roulette/1-34_hover.png"  
            else:
                idle "roulette/1-34.png"
            hover "roulette/1-34_hover.png"
            focus_mask True
            action If(
                selected_roulette == "1_34",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "1_34")
            )

screen roulette2_35:
    if not block_ui:
        imagebutton:
            if selected_roulette == "2_35":
                idle "roulette/2-35_hover.png"  
            else:
                idle "roulette/2-35.png"
            hover "roulette/2-35_hover.png"
            focus_mask True
            action If(
                selected_roulette == "2_35",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "2_35")
            )

screen roulette3_36:
    if not block_ui:
        imagebutton:
            if selected_roulette == "3_36":
                idle "roulette/3-36_hover.png"  
            else:
                idle "roulette/3-36.png"
            hover "roulette/3-36_hover.png"
            focus_mask True
            action If(
                selected_roulette == "3_36",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "3_36")
            )

screen zero:
    if not block_ui:
        imagebutton:
            if selected_roulette == "zero":
                idle "roulette/zero_hover.png"  
            else:
                idle "roulette/zero.png"
            hover "roulette/zero_hover.png"
            focus_mask True
            action If(
                selected_roulette == "zero",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "zero")
            )

screen roulette1:
    if not block_ui:
        imagebutton:
            if selected_roulette == "1":
                idle "roulette/1_hover.png"  
            else:
                idle "roulette/1.png"
            hover "roulette/1_hover.png"
            focus_mask True
            action If(
                selected_roulette == "1",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "1")
            )

screen roulette2:
    if not block_ui:
        imagebutton:
            if selected_roulette == "2":
                idle "roulette/2_hover.png" 
            else:
                idle "roulette/2.png"
            hover "roulette/2_hover.png"
            focus_mask True
            action If(
                selected_roulette == "2",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "2")
            )

screen roulette3:
    if not block_ui:
        imagebutton:
            if selected_roulette == "3":
                idle "roulette/3_hover.png"  
            else:
                idle "roulette/3.png"
            hover "roulette/3_hover.png"
            focus_mask True
            action If(
                selected_roulette == "3",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "3")
            )

screen roulette4:
    if not block_ui:
        imagebutton:
            if selected_roulette == "4":
                idle "roulette/4_hover.png" 
            else:
                idle "roulette/4.png"
            hover "roulette/4_hover.png"
            focus_mask True
            action If(
                selected_roulette == "4",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "4")
            )

screen roulette5:
    if not block_ui:
        imagebutton:
            if selected_roulette == "5":
                idle "roulette/5_hover.png"
            else:
                idle "roulette/5.png"
            hover "roulette/5_hover.png"
            focus_mask True
            action If(
                selected_roulette == "5",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "5")
            )

screen roulette6:
    if not block_ui:
        imagebutton:
            if selected_roulette == "6":
                idle "roulette/6_hover.png"  
            else:
                idle "roulette/6.png"
            hover "roulette/6_hover.png"
            focus_mask True
            action If(
                selected_roulette == "6",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "6")
            )

screen roulette7:
    if not block_ui:
        imagebutton:
            if selected_roulette == "7":
                idle "roulette/7_hover.png"  
            else:
                idle "roulette/7.png"
            hover "roulette/7_hover.png"
            focus_mask True
            action If(
                selected_roulette == "7",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "7")
            )

screen roulette8:
    if not block_ui:
        imagebutton:
            if selected_roulette == "8":
                idle "roulette/8_hover.png"  
            else:
                idle "roulette/8.png"
            hover "roulette/8_hover.png"
            focus_mask True
            action If(
                selected_roulette == "8",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "8")
            )

screen roulette9:
    if not block_ui:
        imagebutton:
            if selected_roulette == "9":
                idle "roulette/9_hover.png" 
            else:
                idle "roulette/9.png"
            hover "roulette/9_hover.png"
            focus_mask True
            action If(
                selected_roulette == "9",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "9")
            )

screen roulette10:
    if not block_ui:
        imagebutton:
            if selected_roulette == "10":
                idle "roulette/10_hover.png" 
            else:
                idle "roulette/10.png"
            hover "roulette/10_hover.png"
            focus_mask True
            action If(
                selected_roulette == "10",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "10")
            )

screen roulette11:
    if not block_ui:
        imagebutton:
            if selected_roulette == "11":
                idle "roulette/11_hover.png"  
            else:
                idle "roulette/11.png"
            hover "roulette/11_hover.png"
            focus_mask True
            action If(
                selected_roulette == "11",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "11")
            )

screen roulette12:
    if not block_ui:
        imagebutton:
            if selected_roulette == "12":
                idle "roulette/12_hover.png"  
            else:
                idle "roulette/12.png"
            hover "roulette/12_hover.png"
            focus_mask True
            action If(
                selected_roulette == "12",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "12")
            )

screen roulette13:
    if not block_ui:
        imagebutton:
            if selected_roulette == "13":
                idle "roulette/13_hover.png"  
            else:
                idle "roulette/13.png"
            hover "roulette/13_hover.png"
            focus_mask True
            action If(
                selected_roulette == "13",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "13")
            )

screen roulette14:
    if not block_ui:
        imagebutton:
            if selected_roulette == "14":
                idle "roulette/14_hover.png" 
            else:
                idle "roulette/14.png"
            hover "roulette/14_hover.png"
            focus_mask True
            action If(
                selected_roulette == "14",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "14")
            )

screen roulette15:
    if not block_ui:
        imagebutton:
            if selected_roulette == "15":
                idle "roulette/15_hover.png"
            else:
                idle "roulette/15.png"
            hover "roulette/15_hover.png"
            focus_mask True
            action If(
                selected_roulette == "15",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "15")
            )

screen roulette16:
    if not block_ui:
        imagebutton:
            if selected_roulette == "16":
                idle "roulette/16_hover.png"
            else:
                idle "roulette/16.png"
            hover "roulette/16_hover.png"
            focus_mask True
            action If(
                selected_roulette == "16",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "16")
            )

screen roulette17:
    if not block_ui:
        imagebutton:
            if selected_roulette == "17":
                idle "roulette/17_hover.png" 
            else:
                idle "roulette/17.png"
            hover "roulette/17_hover.png"
            focus_mask True
            action If(
                selected_roulette == "17",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "17")
            )

screen roulette18:
    if not block_ui:
        imagebutton:
            if selected_roulette == "18":
                idle "roulette/18_hover.png"
            else:
                idle "roulette/18.png"
            hover "roulette/18_hover.png"
            focus_mask True
            action If(
                selected_roulette == "18",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "18")
            )

screen roulette19:
    if not block_ui:
        imagebutton:
            if selected_roulette == "19":
                idle "roulette/19_hover.png" 
            else:
                idle "roulette/19.png"
            hover "roulette/19_hover.png"
            focus_mask True
            action If(
                selected_roulette == "19",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "19")
            )

screen roulette20:
    if not block_ui:
        imagebutton:
            if selected_roulette == "20":
                idle "roulette/20_hover.png" 
            else:
                idle "roulette/20.png"
            hover "roulette/20_hover.png"
            focus_mask True
            action If(
                selected_roulette == "20",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "20")
            )

screen roulette21:
    if not block_ui:
        imagebutton:
            if selected_roulette == "21":
                idle "roulette/21_hover.png"  
            else:
                idle "roulette/21.png"
            hover "roulette/21_hover.png"
            focus_mask True
            action If(
                selected_roulette == "21",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "21")
            )

screen roulette22:
    if not block_ui:
        imagebutton:
            if selected_roulette == "22":
                idle "roulette/22_hover.png"  
            else:
                idle  "roulette/22.png"
            hover "roulette/22_hover.png"
            focus_mask True
            action If(
                selected_roulette == "22",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "22")
            )

screen roulette23:
    if not block_ui:
        imagebutton:
            if selected_roulette == "23":
                idle "roulette/23_hover.png"  
            else:
                idle "roulette/23.png"
            hover "roulette/23_hover.png"
            focus_mask True
            action If(
                selected_roulette == "23",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "23")
            )

screen roulette24:
    if not block_ui:
        imagebutton:
            if selected_roulette == "24":
                idle "roulette/24_hover.png" 
            else:
                idle "roulette/24.png"
            hover "roulette/24_hover.png"
            focus_mask True
            action If(
                selected_roulette == "24",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "24")
            )

screen roulette25:
    if not block_ui:
        imagebutton:
            if selected_roulette == "25":
                idle "roulette/25_hover.png" 
            else:
                idle "roulette/25.png"
            hover "roulette/25_hover.png"
            focus_mask True
            action If(
                selected_roulette == "25",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "25")
            )

screen roulette26:
    if not block_ui:
        imagebutton:
            if selected_roulette == "26":
                idle "roulette/26_hover.png" 
            else:
                idle "roulette/26.png"
            hover "roulette/26_hover.png"
            focus_mask True
            action If(
                selected_roulette == "26",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "26")
            )

screen roulette27:
    if not block_ui:
        imagebutton:
            if selected_roulette == "27":
                idle "roulette/27_hover.png"  
            else:
                idle "roulette/27.png"
            hover "roulette/27_hover.png"
            focus_mask True
            action If(
                selected_roulette == "27",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "27")
            )

screen roulette28:
    if not block_ui:
        imagebutton:
            if selected_roulette == "28":
                idle "roulette/28_hover.png"  
            else:
                idle "roulette/28.png"
            hover "roulette/28_hover.png"
            focus_mask True
            action If(
                selected_roulette == "28",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "28")
            )

screen roulette29:
    if not block_ui:
        imagebutton:
            if selected_roulette == "29":
                idle "roulette/29_hover.png"  
            else:
                idle "roulette/29.png"
            hover "roulette/29_hover.png"
            focus_mask True
            action If(
                selected_roulette == "29",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "29")
            )

screen roulette30:
    if not block_ui:
        imagebutton:
            if selected_roulette == "30":
                idle "roulette/30_hover.png" 
            else:
                idle "roulette/30.png"
            hover "roulette/30_hover.png"
            focus_mask True
            action If(
                selected_roulette == "30",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "30")
            )

screen roulette31:
    if not block_ui:
        imagebutton:
            if selected_roulette == "31":
                idle "roulette/31_hover.png"  
            else:
                idle "roulette/31.png"
            hover "roulette/31_hover.png"
            focus_mask True
            action If(
                selected_roulette == "31",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "31")
            )

screen roulette32:
    if not block_ui:
        imagebutton:
            if selected_roulette == "32":
                idle "roulette/32_hover.png" 
            else:
                idle "roulette/32.png"
            hover "roulette/32_hover.png"
            focus_mask True
            action If(
                selected_roulette == "32",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "32")
            )

screen roulette33:
    if not block_ui:
        imagebutton:
            if selected_roulette == "33":
                idle "roulette/33_hover.png"  
            else:
                idle "roulette/33.png"
            hover "roulette/33_hover.png"
            focus_mask True
            action If(
                selected_roulette == "33",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "33")
            )

screen roulette34:
    if not block_ui:
        imagebutton:
            if selected_roulette == "34":
                idle "roulette/34_hover.png" 
            else:
                idle "roulette/34.png"
            hover "roulette/34_hover.png"
            focus_mask True
            action If(
                selected_roulette == "34",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "34")
            )

screen roulette35:
    if not block_ui:
        imagebutton:
            if selected_roulette == "35":
                idle "roulette/35_hover.png"  
            else:
                idle "roulette/35.png"
            hover "roulette/35_hover.png"
            focus_mask True
            action If(
                selected_roulette == "35",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "35")
            )

screen roulette36:
    if not block_ui:
        imagebutton:
            if selected_roulette == "36":
                idle "roulette/36_hover.png" 
            else:
                idle "roulette/36.png"
            hover "roulette/36_hover.png"
            focus_mask True
            action If(
                selected_roulette == "36",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "36")
            )

screen roulette_1st12:
    if not block_ui:
        imagebutton:
            if selected_roulette == "1st12":
                idle "roulette/1-st-12-_hover.png"
            else:
                idle "roulette/1-st-12.png"
            hover "roulette/1-st-12-_hover.png"
            focus_mask True
            action If(
                selected_roulette == "1st12",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "1st12")
            )

screen roulette_2nd12:
    if not block_ui:
        imagebutton:
            if selected_roulette == "2nd12":
                idle "roulette/2-nd-12_hover.png"  
            else:
                idle "roulette/2-nd-12.png"
            hover "roulette/2-nd-12_hover.png"
            focus_mask True
            action If(
                selected_roulette == "2nd12",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "2nd12")
            )

screen roulette_3rd12:
    if not block_ui:
        imagebutton:
            if selected_roulette == "3rd12":
                idle "roulette/3-rd-12_hover.png" 
            else:
                idle "roulette/3-rd-12.png"
            hover "roulette/3-rd-12_hover.png"
            focus_mask True
            action If(
                selected_roulette == "3rd12:",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "3rd12")
            )

screen roulette_1to18:
    if not block_ui:
        imagebutton:
            if selected_roulette == "1to18":
                idle "roulette/1-to-18_hover.png"  
            else:
                idle "roulette/1-to-18.png"
            hover "roulette/1-to-18_hover.png"
            focus_mask True
            action If(
                selected_roulette == "1to18",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "1to18")
            )

screen roulette_even:
    if not block_ui:
        imagebutton:
            if selected_roulette == "even":
                idle "roulette/even_hover.png"  
            else:
                idle "roulette/even.png"
            hover "roulette/even_hover.png"
            focus_mask True
            action If(
                selected_roulette == "even",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "even")
            )

screen roulette_red:
    if not block_ui:
        imagebutton:
            if selected_roulette == "red":
                idle "roulette/red_hover.png" 
            else:
                idle "roulette/red.png"
            hover "roulette/red_hover.png"
            focus_mask True
            action If(
                selected_roulette == "red",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "red")
            )

screen roulette_black:
    if not block_ui:
        imagebutton:
            if selected_roulette == "black":
                idle "roulette/black_hover.png"  
            else:
                idle "roulette/black.png"
            hover "roulette/black_hover.png"
            focus_mask True
            action If(
                selected_roulette == "black",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "black")
            )

screen roulette_odd:
    if not block_ui:
        imagebutton:
            if selected_roulette == "odd":
                idle "roulette/odd_hover.png" 
            else:
                idle "roulette/odd.png"
            hover "roulette/odd_hover.png"
            focus_mask True
            action If(
                selected_roulette == "odd",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "odd")
            )

screen roulette_19to36:
    if not block_ui:
        imagebutton:
            if selected_roulette == "19to36":
                idle "roulette/19-to-36_hover.png"  
            else:
                idle "roulette/19-to-36.png"
            hover "roulette/19-to-36_hover.png"
            focus_mask True
            action If(
                selected_roulette == "19to36",
                SetVariable("selected_roulette", None),
                SetVariable("selected_roulette", "19to36")
            )

init python:
    roulette_field_number = [
        [0, "Зеро"],
        [1, "Красное"],
        [2, "Черное"],
        [3, "Красное"],
        [4, "Черное"],
        [5, "Красное"],
        [6, "Черное"],
        [7, "Красное"],
        [8, "Черное"],
        [9, "Красное"],
        [10, "Черное"],
        [11, "Красное"],
        [12, "Черное"],
        [13, "Красное"],
        [14, "Черное"],
        [15, "Красное"],
        [16, "Черное"],
        [17, "Красное"],
        [18, "Черное"],
        [19, "Красное"],
        [20, "Черное"],
        [21, "Красное"],
        [22, "Черное"],
        [23, "Красное"],
        [24, "Черное"],
        [25, "Красное"],
        [26, "Черное"],
        [27, "Красное"],
        [28, "Черное"],
        [29, "Красное"],
        [30, "Черное"],
        [31, "Красное"],
        [32, "Черное"],
        [33, "Красное"],
        [34, "Черное"],
        [35, "Красное"],
        [36, "Черное"],
    ]

    import random

    def get_random_roulette():
        return random.choice(roulette_field_number)


label igra_roulette:
    $ renpy.music.set_pause(True)
    $ start_dialog()
    if money < 2000:
        $ block_ui = True
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/399.mp3"
        Vika "У меня недостаточно денег"
        $ block_ui = False
        $ stop_dialog()
        jump play_roulette
    elif magnet_v_rouletke == True and ball_v_rouletke == True and selected_roulette != "21":
        $ block_ui = True
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/412.mp3"
        Vika "(Я поставила магнит под цифрой 21)"
        $ stop_dialog()
        $ block_ui = False
        jump play_roulette
    elif magnet_v_rouletke == True and ball_v_rouletke == True and money >= 72000:
        $ block_ui = True
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/413.mp3"
        Vika "(Мне уже хватает денег, надо валить отсюда)"
        $ block_ui = False
        $ stop_dialog()
        jump play_roulette
    elif selected_roulette == None:
        $ block_ui = True
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/414.mp3"
        Vika "Я не выбрала на что ставить."
        $ block_ui = False
        $ stop_dialog()
        jump play_roulette
    else:
        $ money -= 2000
        $ block_ui = True
        if magnet_v_rouletke == True and ball_v_rouletke == True:
            $ resoult_roulette = [21, "Красное"]
            $ quest_list[2]["done"] = True
            $ quest_list[11]["done"] = True
            $ intellect += 1
            $ quest_list[14]["available"] = True
            $ quest_list[15]["available"] = True
        else:
            $ resoult_roulette = get_random_roulette()
        play sound "roulette.ogg"
        pause 10.0
        stop sound
        if resoult_roulette[0] == 0:
            if selected_roulette == "zero":
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/15.mp3"
                diller "Выпало зеро! Поздравляю, ваша ставка увеличена в 36 раз."
                $ money += 72000
            else:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/16.mp3"
                diller "Выпало зеро. К сожалению, вы проиграли."
        else:
            if selected_roulette == "19to36" and resoult_roulette[0] >= 19:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/17.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 2 раза."
                $ money += 4000
            elif selected_roulette == "1to18" and 1 <= resoult_roulette[0] <= 18:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/17.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 2 раза."
                $ money += 4000
            elif selected_roulette == "even" and resoult_roulette[0] % 2 == 0:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/17.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 2 раза."
                $ money += 200
            elif selected_roulette == "odd" and resoult_roulette[0] % 2 == 1:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/17.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 2 раза."
                $ money += 4000
            elif selected_roulette == "black" and resoult_roulette[1] == "Черное":
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/17.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 2 раза."
                $ money += 4000
            elif selected_roulette == "red" and resoult_roulette[1] == "Красное":
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/17.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 2 раза."
                $ money += 4000
            elif selected_roulette == "3rd12" and 25 <= resoult_roulette[0] <= 36:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/18.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 3 раза."
                $ money += 6000
            elif selected_roulette == "2nd12" and 13 <= resoult_roulette[0] <= 24:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/18.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 3 раза."
                $ money += 6000
            elif selected_roulette == "1st12" and 1 <= resoult_roulette[0] <= 12:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/18.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 3 раза."
                $ money += 6000
            elif selected_roulette.isdigit() and int(selected_roulette) == resoult_roulette[0]:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/19.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 36 раз."
                $ money += 72000
            elif selected_roulette == "1_34" and resoult_roulette[0] % 3 == 1:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/18.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 3 раза."
                $ money += 6000
            elif selected_roulette == "2_35" and resoult_roulette[0] % 3 == 2:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/18.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 3 раза."
                $ money += 6000
            elif selected_roulette == "3_36" and resoult_roulette[0] % 3 == 0:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/18.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], поздравляю, ставка увеличена в 3 раза."
                $ money += 6000
            else:
                $ _preferences.afm_enable = True 
                voice "audio/voices/diller/20.mp3"
                diller "Выпало [resoult_roulette[0]] - [resoult_roulette[1]], к сожалению, вы проиграли."
        $ block_ui = False
        $ stop_dialog()
        jump play_roulette

label dice:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ show_hud()
    scene bg dice
    show screen back_arrow_to_casino_hall_ruletka
    show screen diller_2
    show screen dice_field
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return 

screen diller_2:
    if not block_ui:
        imagebutton:
            idle "diller_2_idle.png"
            hover "diller_2_hover.png"
            focus_mask True
            action Jump("rules_dice")  # Показываем меню выбора

label rules_dice:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/diller/5.mp3"
    diller "Хотите узнать правила игры?"
    $ stop_dialog()
    menu:
        "Да":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/21.mp3"
            diller "Вы выбираете режим и делаете ставку размером 100р."
            voice "audio/voices/diller/22.mp3"
            diller "Режим Odd означает, что ваша ставка сыграет, если на кубике выпадет нечетное число."
            voice "audio/voices/diller/23.mp3"
            diller "Режим Even наоборот, что ваша ставка сыграет, если на кубике выпадет четное число."
            voice "audio/voices/diller/24.mp3"
            diller "Режимы с цифрами показывают диапазон или конкретные числа выйгрышных значений."
            voice "audio/voices/diller/25.mp3"
            diller "Просто выберите режим, бросайте кубик и ждите выйгрыша"
            $ stop_dialog()
        "Нет":
            pass
    jump dice

screen dice_field:
    if not block_ui:
        imagebutton:
            idle "dice_field_idle.png"
            hover "dice_field_hover.png"
            focus_mask True
            action Jump("kosti")  # Показываем меню выбора

screen back_arrow_to_casino_hall_ruletka:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("casino_hall")  # Показываем меню выбора

screen door_karti:
    if not block_ui:
        imagebutton:
            idle "door_karti_idle.png"
            hover "door_karti_hover.png"
            focus_mask True
            action Jump("cards")  # Показываем меню выбора

label cards:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ show_hud()
    scene bg cards
    show screen back_arrow_to_casino_hall_ruletka
    show screen cards
    show screen diller_1
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen cards:
    if not block_ui:
        imagebutton:
            idle "cards/cards_idle.png"
            hover "cards/cards_hover.png"
            focus_mask True
            action Jump("play_cards")  # Показываем меню выбора

label play_cards:
    $ renpy.free_memory()
    scene bg play_cards
    $ hide_all_ui()
    show screen money
    show screen start
    show screen inventory_bag
    show screen back_arrow_to_casino_hal3
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return


screen start:
    if not block_ui:
        imagebutton:
            idle "cards/start_idle.png"
            hover "cards/start_hover.png"
            focus_mask True
            action Jump("show_random_card_1")

screen higher:
    if not block_ui:
        imagebutton:
            idle "cards/higher_idle.png"
            hover "cards/higher_hover.png"
            focus_mask True
            action [SetVariable("higher_pressed", True), Jump("show_random_card_2")]

screen lower:
    if not block_ui:
        imagebutton:
            idle "cards/lower_idle.png"
            hover "cards/lower_hover.png"
            focus_mask True
            action [SetVariable("lower_pressed", True), Jump("show_random_card_2")]

screen inin:
    if not block_ui:
        imagebutton:
            idle "cards/in_idle.png"
            hover "cards/in_hover.png"
            focus_mask True
            action [SetVariable("inin_pressed", True), Jump("show_random_card_3")]

screen out:
    if not block_ui:
        imagebutton:
            idle "cards/out_idle.png"
            hover "cards/out_hover.png"
            focus_mask True
            action [SetVariable("out_pressed", True), Jump("show_random_card_3")]

screen cherva:
    if not block_ui:
        imagebutton:
            idle "cards/cherva_idle.png"
            hover "cards/cherva_hover.png"
            focus_mask True
            action [SetVariable("mast", "H"), Jump("show_random_card_4")]

screen trefa:
    if not block_ui:
        imagebutton:
            idle "cards/trefa_idle.png"
            hover "cards/trefa_hover.png"
            focus_mask True
            action [SetVariable("mast", "T"), Jump("show_random_card_4")]

screen buba:
    if not block_ui:
        imagebutton:
            idle "cards/buba_idle.png"
            hover "cards/buba_hover.png"
            focus_mask True
            action [SetVariable("mast", "C"), Jump("show_random_card_4")]

screen pika:
    if not block_ui:
        imagebutton:
            idle "cards/pika_idle.png"
            hover "cards/pika_hover.png"
            focus_mask True
            action [SetVariable("mast", "Q"), Jump("show_random_card_4")]

init python:
    import random

    cards_list = [
        "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "11H", "12H", "13H", "14H",
        "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "11C", "12C", "13C", "14C",
        "2Q", "3Q", "4Q", "5Q", "6Q", "7Q", "8Q", "9Q", "10Q", "11Q", "12Q", "13Q", "14Q",
        "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "11T", "12T", "13T", "14T"
    ]

    def get_random_card():
        return random.choice(cards_list)

label show_random_card_1:
    $ renpy.music.set_pause(True)
    $ renpy.free_memory()
    $ start_dialog()
    if money < 100:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/415.mp3"
        Vika "У меня не хватает денег на ставку"
    else:
        hide screen start
        play sound "playing_cards.mp3"
        pause 1.5
        play sound "card_deal.mp3"
        show screen higher
        show screen lower
        $ money -= 100
        $ random_card_1 = get_random_card()

        show expression "cards/cards/{}.png".format(random_card_1) at Position(xpos=0.23, ypos=0.60)
    $ renpy.music.set_pause(False)
    $ stop_dialog()
    call screen wait_for_click
    return

label show_random_card_2:
    $ renpy.music.set_pause(True)
    $ renpy.free_memory()
    hide screen higher
    hide screen lower
    play sound "card_deal.mp3"
    show screen inin
    show screen out
    $ random_card_2 = get_random_card()

    show expression "cards/cards/{}.png".format(random_card_2) at Position(xpos=0.41, ypos=0.60)

    $ value_1 = int(random_card_1[:-1])
    $ value_2 = int(random_card_2[:-1])  # Берем число второй карты
    if higher_pressed:
        if value_1 <= value_2:
            $ money += 200
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ higher_pressed = False
            $ lower_pressed = False
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/2.mp3"
            diller "Вы проиграли"
            $ higher_pressed = False
            $ lower_pressed = False
            jump play_cards
    elif lower_pressed:
        if value_1 >= value_2:
            $ money += 200
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/1.mp3"
            diller "Вы выйграли"
            $ higher_pressed = False
            $ lower_pressed = False
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/2.mp3"
            diller "Вы проиграли"
            $ higher_pressed = False
            $ lower_pressed = False
            jump play_cards

    # Сбросим нажатые кнопки
    
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label show_random_card_3:
    $ renpy.free_memory()
    hide screen inin
    hide screen out
    $ renpy.music.set_pause(True)
    play sound "card_deal.mp3"
    show screen cherva
    show screen buba
    show screen trefa
    show screen pika
    $ random_card_3 = get_random_card()

    show expression "cards/cards/{}.png".format(random_card_3) at Position(xpos=0.59, ypos=0.60)
    # Извлекаем числовые значения карт
    $ value_1 = int(random_card_1[:-1])
    $ value_2 = int(random_card_2[:-1])
    $ value_3 = int(random_card_3[:-1])

    # Найдем минимальное и максимальное значение между value_1 и value_2
    $ low = min(value_1, value_2)
    $ high = max(value_1, value_2)

    if inin_pressed:
        if low <= value_3 <= high:
            $ money += 200
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/35.mp3"
            "Третья карта между первой и второй! Вы выиграли уже 400₽!"
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/36.mp3"
            "Не между. Вы проиграли."
            $ money -= 200
            jump play_cards
    elif out_pressed:
        if value_3 < low or value_3 > high:
            $ money += 200
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/37.mp3"
            "Третья карта вне диапазона! Вы выиграли уже 400₽!"
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/38.mp3"
            "Карта попала внутрь диапазона. Вы проиграли."
            $ money -= 200
            jump play_cards

    # Сброс флагов
    $ inin_pressed = False
    $ out_pressed = False
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label show_random_card_4:
    $ renpy.free_memory()
    $ renpy.music.set_pause(True)
    hide screen cherva
    hide screen buba
    hide screen trefa
    hide screen pika
    play sound "card_deal.mp3"
    show screen start
    $ random_card_4 = get_random_card()

    show expression "cards/cards/{}.png".format(random_card_4) at Position(xpos=0.77, ypos=0.60)
    $ value_4 = random_card_4[-1]
    if mast == value_4:
        $ money += 1600
        $ _preferences.afm_enable = True 
        voice "audio/voices/diller/26.mp3"
        diller "Поздравляю, джекпот ваш!"
        jump play_cards
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/diller/2.mp3"
        diller "Вы проиграли"
        $ money -= 400
        jump play_cards
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen diller_1:
    if not block_ui:
        imagebutton:
            idle "cards/diller_1_idle.png"
            hover "cards/diller_1_hover.png"
            focus_mask True
            action Jump("rules_cards")  # Показываем меню выбора

label rules_cards:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/diller/5.mp3"
    diller "Хотите узнать правила игры?"
    $ stop_dialog()
    menu:
        "Да":
            $ _preferences.afm_enable = True 
            voice "audio/voices/diller/27.mp3"
            diller "Вы делаете ставку размером 100р."
            voice "audio/voices/diller/28.mp3"
            diller "Я выдаю вам карту и жду ваше слово, вы говорите следующая карта будет больше или меньше."
            voice "audio/voices/diller/29.mp3"
            diller "Если вы угадали, то я удваиваю вашу ставку и вы решаете играть дальше или закончить."
            voice "audio/voices/diller/30.mp3"
            diller "Если вы не угадали, я забираю вашу ставку."
            voice "audio/voices/diller/31.mp3"
            diller "Далее вы делаете выбор будет третья карта между превыми двумя или она будет вне них."
            voice "audio/voices/diller/32.mp3"
            diller "Если вы опять угадываете, я учетверяю вашу первоначальную ставку и вы решаете играть ли дальше."
            voice "audio/voices/diller/33.mp3"
            diller "Последним ходом вы решаете, какая масть будет у четвертой карты."
            voice "audio/voices/diller/34.mp3"
            diller "Если вы снова угадываете то я отдаю вам вашу ставку помноженную на 20, и игра завершается."
        "Нет":
            pass
    $ stop_dialog()
    jump cards


screen back_arrow_to_casino:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("casino")  # Показываем меню выбора
           

label vhod_v_bar:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ show_hud()
    $ travel(polojenie, "bar")
    $ polojenie = "bar"
    play music "city.mp3" fadeout 1
    scene bg vhod_v_bar
    if i_sold_beer == True and i_take_beer == False:
        show screen german_beer
    show screen back_arrow_to_map
    show screen door_to_bar
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen german_beer:
    imagebutton:
        idle "bar/pustaya_banka.png"
        focus_mask True
        if not block_ui:
            hover "bar/pustaya_banka_hover.png"
            action Jump("take_beer")  # Показываем меню выбора 

label take_beer:
    $ add_item_to_inventory("german_beer")
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/416.mp3"
    Vika "Я продала единственное пиво человеку который им намусорил..."
    $ block_ui = False
    $ stop_dialog()
    $ i_take_beer = True
    jump vhod_v_bar


screen door_to_bar:
    if not block_ui:
        imagebutton:
            idle "door_to_bar_idle.png"
            hover "door_to_bar_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("bar")  # Показываем меню выбора 

label bar:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ show_hud()
    if day_index == 6:
        scene bg bar
    else:
        scene bg bar_with_barmen
        show screen barmen
    play music "bar_theme.mp3" fadeout 1
    show screen back_arrow_to_vhod_bar
    show screen to_slut
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen barmen:
    imagebutton:
        idle "barmen.png"
        focus_mask True
        if not block_ui:
            hover "barmen_hover.png"
            action Jump("barmen_dialog")

label barmen_dialog:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    if barmen_dialog_first_time == True:
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/417.mp3"
        Vika "Здравствуйте, вы бармен?"
        voice "audio/voices/barmen/1.mp3"
        barmen "Здравствуйте, да, что вы хотели?"
        voice "audio/voices/vika/418.mp3"
        Vika "Да так, ничего, просто вчера тут весь день никого не было"
        voice "audio/voices/barmen/2.mp3"
        barmen "Я часто отлучаюсь по просьбе начальства на склад... ну или еще куда-нибудь. Чем я могу вам помочь?"
        $ barmen_dialog_first_time = False
    elif zakaz == 5:
        $ _preferences.afm_enable = True 
        voice "audio/voices/barmen/3.mp3"
        barmen "Я вернулся, ну как ты тут справилась?"
        if zakaz_point == 4:
            $ _preferences.afm_enable = True 
            voice "audio/voices/barmen/4.mp3"
            barmen "Молодец! Можешь взять стакан."
            voice "audio/voices/barmen/5.mp3"
            barmen "Ты что продала пиво?"
            voice "audio/voices/vika/101.mp3"
            Vika "Ну да"
            voice "audio/voices/barmen/6.mp3"
            barmen "Оно было последнее, стакан можешь взять, а вот с пивом извини, было последнее."
            voice "audio/voices/vika/419.mp3"
            Vika "Блин, ладно, я что-нибудь придумаю."
            $ add_item_to_inventory("glass") 
            $ intellect += 1
            $ game_hour += 1
            $ update_game_time() 
            $ block_ui = False
            $ zakaz = 6
            $ stop_dialog()
            jump bar
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/barmen/7.mp3"
            barmen "Нет, так не годится, за такую работу я не могу тебе отдать стакан, пробуй еще."
            $ zakaz_point = 0
            $ zakaz = 0
            $ block_ui = False
            $ stop_dialog()
            jump barmen_work
    else:
        $ _preferences.afm_enable = True 
        voice "audio/voices/barmen/8.mp3"
        barmen "Да?"
    jump barmen_menu

label barmen_menu:
    $ stop_dialog()
    menu:
        "Можете налить мне немецкого пива?" if ment_first_dialog == False and i_ask_glass == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/420.mp3"
            Vika "Можете налить мне немецкого пива?"
            voice "audio/voices/barmen/9.mp3"
            barmen "Конечно, можете взять из холодильника"
            voice "audio/voices/vika/421.mp3"
            Vika "А можно налить его в стакан?"
            voice "audio/voices/barmen/10.mp3"
            barmen "Конечно, только потом верни его на бар, а то я один обслуживаю это заведение, очень тяжело бегать и собирать посуду."
            voice "audio/voices/vika/422.mp3"
            Vika "Если честно, я вообще не хочу его возвращать, могу я купить пиво вместе со стаканом?"
            voice "audio/voices/barmen/11.mp3"
            barmen "Нет, так не получится, меня начальство и так штрафует за то что меня постоянно нет на баре, а если посуда пропадать начнет..."
            voice "audio/voices/vika/423.mp3"
            Vika "Вы же сказали, что они сами вас отправляют на склад?"
            voice "audio/voices/barmen/12.mp3"
            barmen "Эмм... Так ты будешь брать пиво?"
            voice "audio/voices/vika/424.mp3"
            Vika "Мне не нужно пиво без стакана, давайте вы уйдете куда бы вам там не надо было, а я вас прикрою. А за это вы отдадите мне стакан немецкого пива."
            voice "audio/voices/barmen/13.mp3"
            barmen "Хмм, а это мысль. Встанешь за бар и будешь готовить коктейли, а я скоро вернусь."
            voice "audio/voices/vika/28.mp3"
            Vika "Хорошо"
            $ i_ask_glass = True
            $ block_ui = False
            $ stop_dialog()
            jump barmen_work
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/barmen/14.mp3"
            barmen "Заглядывай"
            $ block_ui = False
            $ stop_dialog()
            jump bar

label barmen_work:
    scene bg bar_table
    $ hide_all_ui()
    show screen beer_glas
    show screen coconut_milk
    show screen cocteil_glas
    show screen cointreau
    show screen ice
    show screen lime_juice
    show screen mohito_glas
    show screen mors
    show screen myata
    show screen pina_colada_glas
    show screen salt_b
    show screen soda
    show screen sugar
    show screen teqila
    show screen vodka
    show screen white_rom
    show screen shaker
    $ start_dialog()
    if zakaz == 0:
        $ block_ui = True
        $ _preferences.afm_enable = True 
        voice "audio/voices/barmen/15.mp3"
        barmen "Все просто, делай все по порядку как в рецепте"
        pause 2.0
        $ _preferences.afm_enable = True 
        voice "audio/voices/posetitel/1.mp3"
        posetitel "Здравствуйте, можно мне Мохито?"
        voice "audio/voices/vika/425.mp3"
        Vika "Да, конечно!"
        $ zakaz = 1
        $ block_ui = False
        $ stop_dialog()
        jump mohito
    elif zakaz == 1:
        $ _preferences.afm_enable = True 
        $ block_ui = True
        if cocteil == mohito:
            voice "audio/voices/posetitel/2.mp3"
            posetitel "Очень вкусно, спасибо"
            $ zakaz_point += 1
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/posetitel/3.mp3"
            posetitel "Это самое ужасное что я пила"
        $ cocteil.clear()
        pause 2.0
        $ _preferences.afm_enable = True 
        voice "audio/voices/posetitel/4.mp3"
        posetitel "Здравствуйте, можно мне Маргариту?"
        voice "audio/voices/vika/425.mp3"
        Vika "Да, конечно"
        $ zakaz = 2
        $ block_ui = False
        $ stop_dialog()
        jump margarita         
    elif zakaz == 2:
        $ block_ui = True
        if cocteil == margarita:
            $ _preferences.afm_enable = True 
            voice "audio/voices/posetitel/5.mp3"
            posetitel "Очень вкусно, спасибо"
            $ zakaz_point += 1
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/posetitel/6.mp3"
            posetitel "Это самое ужасное что я пила"
        $ cocteil.clear()
        pause 2.0
        $ _preferences.afm_enable = True 
        voice "audio/voices/posetitel/7.mp3"
        posetitel "Здравствуйте, можно мне Пина коладу?"
        voice "audio/voices/vika/425.mp3"
        Vika "Да, конечно"
        $ zakaz = 3
        $ block_ui = False
        $ stop_dialog()
        jump pina_colada 
    elif zakaz == 3:
        $ block_ui = True
        if cocteil == pina_colada:
            $ _preferences.afm_enable = True 
            voice "audio/voices/posetitel/8.mp3"
            posetitel "Очень вкусно, спасибо"
            $ zakaz_point += 1
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/posetitel/9.mp3"
            posetitel "Это самое ужасное что я пила"
        $ cocteil.clear()
        pause 2.0
        $ _preferences.afm_enable = True 
        voice "audio/voices/posetitel/10.mp3"
        posetitel "Здравствуйте, можно мне Космополитан?"
        voice "audio/voices/vika/425.mp3"
        Vika "Да, конечно"
        $ zakaz = 4
        $ block_ui = False
        $ stop_dialog()
        jump kosmopolitan
    elif zakaz == 4:
        $ block_ui = True
        if cocteil == kosmopolitan:
            $ _preferences.afm_enable = True 
            voice "audio/voices/posetitel/11.mp3"
            posetitel "Очень вкусно, спасибо"
            $ zakaz_point += 1
        else:
            $ _preferences.afm_enable = True 
            voice "audio/voices/posetitel/12.mp3"
            posetitel "Это самое ужасное что я пила"
        pause 2.0
        $ _preferences.afm_enable = True 
        voice "audio/voices/posetitel/13.mp3"
        posetitel "Здравствуйте, можно мне Немецкое пиво?"
        voice "audio/voices/vika/426.mp3"
        Vika "Да, конечно, возьмите в холодильнике"
        $ i_sold_beer = True
        $ cocteil.clear()
        $ zakaz = 5
        $ stop_dialog()
        jump barmen_dialog
    
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

init python:
    cocteil = [] 
    mohito = ["white_rom", "lime_juice", "sugar", "myata", "soda", "ice", "mohito_glas"]
    margarita = ["teqila", "cointreau", "lime_juice", "shaker", "ice", "salt", "cocteil_glas"]
    pina_colada = ["white_rom", "coconut_milk", "lime_juice", "shaker", "pina_colada_glas"]
    kosmopolitan = ["vodka", "cointreau", "mors", "lime_juice", "ice", "shaker", "cocteil_glas"]

    def add_to_cocteil(ingredient):
        cocteil.append(ingredient)

label mohito:
    show screen mohito_recept
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label margarita:
    show screen margarita_recept
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label pina_colada:
    show screen pina_colada_recept
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label kosmopolitan:
    show screen kosmopolitan_recept
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return


screen mohito_recept:
    add "bar/recept/mohito.png"
    imagebutton:
        idle "bar/recept/otdat_zakaz.png"        
        focus_mask True
        if not block_ui:
            hover "bar/recept/otdat_zakaz_hover.png"
            action [Hide("mohito_recept"), Jump("barmen_work")]


screen margarita_recept:
    add "bar/recept/margarita.png"
    imagebutton:
        idle "bar/recept/otdat_zakaz.png"        
        focus_mask True
        if not block_ui:
            hover "bar/recept/otdat_zakaz_hover.png"
            action [Hide("margarita_recept"), Jump("barmen_work")]

screen pina_colada_recept:
    add "bar/recept/pina_colada.png"
    imagebutton:
        idle "bar/recept/otdat_zakaz.png"        
        focus_mask True
        if not block_ui:
            hover "bar/recept/otdat_zakaz_hover.png"
            action [Hide("pina_colada_recept"), Jump("barmen_work")]

screen kosmopolitan_recept:
    add "bar/recept/kosmopolitan.png"
    imagebutton:
        idle "bar/recept/otdat_zakaz.png"        
        focus_mask True
        if not block_ui:
            hover "bar/recept/otdat_zakaz_hover.png"
            action [Hide("kosmopolitan_recept"), Jump("barmen_work")]

screen beer_glas:
    imagebutton:
        idle "bar/beer_glas.png"        
        focus_mask True
        if not block_ui:
            hover "bar/beer_glas_hover.png"
            action [Function(add_to_cocteil, "beer_glas"), Play("sound", "zvuk_glass_4.mp3")]

screen coconut_milk:
    imagebutton:
        idle "bar/coconut_milk.png"        
        focus_mask True
        if not block_ui:
            hover "bar/coconut_milk_hover.png"
            action [Function(add_to_cocteil, "coconut_milk"), Play("sound", "zvuk_soka.mp3")]

screen cocteil_glas:
    imagebutton:
        idle "bar/cocteil_glas.png"        
        focus_mask True
        if not block_ui:
            hover "bar/cocteil_glas_hover.png"
            action [Function(add_to_cocteil, "cocteil_glas"), Play("sound", "zvuk_glass_3.mp3")]

screen cointreau:
    imagebutton:
        idle "bar/cointreau.png"        
        focus_mask True
        if not block_ui:
            hover "bar/cointreau_hover.png"
            action [Function(add_to_cocteil, "cointreau"), Play("sound", "zvuk_alko_2.mp3")]

screen ice:
    imagebutton:
        idle "bar/ice.png"        
        focus_mask True
        if not block_ui:
            hover "bar/ice_hover.png"
            action [Function(add_to_cocteil, "ice"), Play("sound", "zvuk_ice.mp3")]

screen lime_juice:
    imagebutton:
        idle "bar/lime_juice.png"        
        focus_mask True
        if not block_ui:
            hover "bar/lime_juice_hover.png"
            action [Function(add_to_cocteil, "lime_juice"), Play("sound", "zvuk_soka.mp3")]

screen mohito_glas:
    imagebutton:
        idle "bar/mohito_glas.png"        
        focus_mask True
        if not block_ui:
            hover "bar/mohito_glas_hover.png"
            action [Function(add_to_cocteil, "mohito_glas"), Play("sound", "zvuk_glass_2.mp3")]

screen mors:
    imagebutton:
        idle "bar/mors.png"        
        focus_mask True
        if not block_ui:
            hover "bar/mors_hover.png"
            action [Function(add_to_cocteil, "mors"), Play("sound", "zvuk_soka.mp3")]

screen myata:
    imagebutton:
        idle "bar/myata.png"        
        focus_mask True
        if not block_ui:
            hover "bar/myata_hover.png"
            action [Function(add_to_cocteil, "myata"), Play("sound", "zvuk_myata.mp3")]

screen pina_colada_glas:
    imagebutton:
        idle "bar/pina_colada_glas.png"        
        focus_mask True
        if not block_ui:
            hover "bar/pina_colada_glas_hover.png"
            action [Function(add_to_cocteil, "pina_colada_glas"), Play("sound", "zvuk_glass_1.mp3")]

screen salt_b:
    imagebutton:
        idle "bar/salt.png"        
        focus_mask True
        if not block_ui:
            hover "bar/salt_hover.png"
            action [Function(add_to_cocteil, "salt"), Play("sound", "zvuk_salt.mp3")]

screen soda:
    imagebutton:
        idle "bar/soda.png"        
        focus_mask True
        if not block_ui:
            hover "bar/soda_hover.png"
            action [Function(add_to_cocteil, "soda"), Play("sound", "zvuk_gaz.mp3")]

screen sugar:
    imagebutton:
        idle "bar/sugar.png"        
        focus_mask True
        if not block_ui:
            hover "bar/sugar_hover.png"
            action [Function(add_to_cocteil, "sugar"), Play("sound", "zvuk_sugar.mp3")]

screen teqila:
    imagebutton:
        idle "bar/teqila.png"        
        focus_mask True
        if not block_ui:
            hover "bar/teqila_hover.png"
            action [Function(add_to_cocteil, "teqila"), Play("sound", "zvuk_alko_3.mp3")]

screen vodka:
    imagebutton:
        idle "bar/vodka.png"        
        focus_mask True
        if not block_ui:
            hover "bar/vodka_hover.png"
            action [Function(add_to_cocteil, "vodka"), Play("sound", "zvuk_alko_3.mp3")]

screen white_rom:
    imagebutton:
        idle "bar/white_rom.png"        
        focus_mask True
        if not block_ui:
            hover "bar/white_rom_hover.png"
            action [Function(add_to_cocteil, "white_rom"), Play("sound", "zvuk_alko_1.mp3")]

screen shaker:
    imagebutton:
        idle "bar/shaker.png"        
        focus_mask True
        if not block_ui:
            hover "bar/shaker_hover.png"
            action [Function(add_to_cocteil, "shaker"), Play("sound", "zvuk_shaker.mp3")]

screen to_slut:
    if not block_ui:
        imagebutton:
            idle "to_slut_idle.png"
            hover "to_slut_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("slut")  # Показываем меню выбора

screen back_arrow_to_vhod_bar:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("vhod_v_bar")  # Показываем меню выбора

label slut:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ show_hud()
    scene bg slut
    show screen chess_players
    show screen slut
    show screen back_arrow_to_bar
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen back_arrow_to_bar:
    zorder 10
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("bar")  # Показываем меню выбора

screen slut:
    if not block_ui:
        imagebutton:
            idle "slut_idle.png"
            hover "slut_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("slut_dialog")  # Показываем меню выбора

label slut_dialog:
    $ block_ui = True
    $ start_dialog()
    $ renpy.music.set_pause(True)
    $ _preferences.afm_enable = True 
    voice "audio/voices/clara/29.mp3"
    clara "Привет"
    voice "audio/voices/vika/30.mp3"
    Vika "Привет"
    jump clara_menu

label clara_menu:
    $ stop_dialog()
    menu:
        "Спросить про клиентов" if i_know_about_sluts == True and i_ask_about_clients == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/427.mp3"
            Vika "Слушай, а кто обычно твои клиенты?"
            voice "audio/voices/clara/30.mp3"
            clara "Оооо, подруга, тебе лучше поберечь свою психику, и не спрашивать об этом"
            voice "audio/voices/vika/428.mp3"
            Vika "Ну вообще я хотела спросить, не снимал ли тебя мой босс?"
            voice "audio/voices/clara/31.mp3"
            clara "Откуда же мне знать кто твой босс?"
            voice "audio/voices/vika/429.mp3"
            Vika "Ну он очень толстый..."
            voice "audio/voices/clara/32.mp3"
            clara "Ты же понимаешь, что ты описала 90 процентов моих клиентов"
            voice "audio/voices/vika/430.mp3"
            Vika "Ну он орет постоянно и очень придирается..."
            voice "audio/voices/clara/33.mp3"
            clara "Ну уже ближе, 89 процентов, может фотка есть?"
            voice "audio/voices/vika/431.mp3"
            Vika "Ну в общем он работает в компании Bluegen"
            voice "audio/voices/clara/34.mp3"
            clara "Вообще, мои клиенты мало что рассказывают о своей жизни, но..."
            voice "audio/voices/clara/35.mp3"
            clara "Если ты про синее здание где охранник пенсионер и большая дверь с надписью кабинет начальника, то да, я там была."
            voice "audio/voices/vika/432.mp3"
            Vika "Да, точно он."
            voice "audio/voices/clara/36.mp3"
            clara "Ну он не особо скрывается, вызвал на работу и даже заставил какого-то парнишку бежать для нас в аптеку."
            voice "audio/voices/clara/37.mp3"
            clara "А тот и рад был услужиться, но это наверное все что я могу тебе на него слить, тебе скорее всего нечем его шантажировать."
            voice "audio/voices/vika/433.mp3"
            Vika "Мне не надо его шантажировать, просто можешь выманить его из кабинета?"
            voice "audio/voices/clara/38.mp3"
            clara "Ну уж нет, ты один раз уже подкинула мне клиента, хватит, не надо тебе превращаться в моего сутенера."
            voice "audio/voices/vika/118.mp3"
            Vika "Ну пожалуйста..."
            voice "audio/voices/clara/39.mp3"
            clara "Нееет"
            $ game_hour += 1
            $ update_game_time()
            $ i_ask_about_clients = True
            jump clara_menu
        "Снять её" if need_suck == True and i_know_studio == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/434.mp3"
            Vika "У меня есть к тебе одна просьба."
            voice "audio/voices/clara/40.mp3"
            clara "Ты говоришь как каждый мой клиент, который хочет потерять девственность"
            voice "audio/voices/vika/435.mp3"
            Vika "Ну, ты не далеко от истины."
            voice "audio/voices/clara/41.mp3"
            clara "Тебя резко потянуло на девочек?"
            voice "audio/voices/vika/436.mp3"
            Vika "Нет, просто есть один человек, который меня шантажирует..."
            voice "audio/voices/clara/42.mp3"
            clara "И ты думаешь, если я с ним пересплю, то он перестанет это делать?"
            voice "audio/voices/vika/437.mp3"
            Vika "Нет, он точно не перестанет, но я что-нибудь придумаю, он просто требует сегодня вечером."
            voice "audio/voices/clara/43.mp3"
            clara "Сегодня вечером я занята, у меня съемка, и она уже оплачена."
            voice "audio/voices/vika/438.mp3"
            Vika "Я снимусь за тебя, только помоги пожалуйста!!!"
            voice "audio/voices/clara/44.mp3"
            clara "Ну хорошо, тогда тебе уже пора на фотостудию."
            $ quest_list[24]["done"] = True
            $ quest_list[25]["available"] = True
            voice "audio/voices/vika/439.mp3"
            Vika "А тебе в полицию."
            voice "audio/voices/clara/45.mp3"
            clara "В полицию???"
            voice "audio/voices/vika/440.mp3"
            Vika "Да, меня шантажирует полицейский."
            voice "audio/voices/clara/46.mp3"
            clara "Ну ты даешь, ладно разберемся."
            $ i_know_studio = True
            jump clara_menu
        "Почему тебя не пускают в казино?" if may_ask_about_casino == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/441.mp3"
            Vika "А почему тебя не пускают в казино?"
            voice "audio/voices/clara/47.mp3"
            clara "Да был один случай... Меня как эскортницу снял один парень и мы поехали в казино."
            voice "audio/voices/clara/48.mp3"
            clara "Выяснилось что он прочитал книгу 'как мухлевать в казино' и попытался применить что прочел"
            voice "audio/voices/vika/442.mp3"
            Vika "Ииии? Его посадили за мошенничество?"
            voice "audio/voices/clara/49.mp3"
            clara "Нет, он даже не сыграл ни одной игры, он просто выронил книгу и сказал что это я уронила. В итоге меня выгнали из казино"
            voice "audio/voices/vika/443.mp3"
            Vika "А где сейчас эта книга?"
            voice "audio/voices/clara/50.mp3"
            clara "У меня в сумке"
            voice "audio/voices/vika/444.mp3"
            Vika "Можешь отдать мне её?"
            voice "audio/voices/clara/51.mp3"
            clara "Без проблем, только не говори мне, что ты собралась обмануть казино."
            voice "audio/voices/vika/445.mp3"
            Vika "Нет... Просто интересно почитать..."
            voice "audio/voices/clara/52.mp3"
            clara "Ну хорошо, держи"
            $ add_item_to_inventory("casino_book") 
            $ may_ask_about_casino = False
            jump clara_menu
        "Почему ты сидишь тут?" if i_ask_about_work == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/446.mp3"
            Vika "Почему ты сидишь тут?"
            voice "audio/voices/clara/53.mp3"
            clara "А что мне еще делать? Моя подруга еще не приехала, работать мне негде, ты же мне еще не освободила квартиру."
            voice "audio/voices/clara/54.mp3"
            clara "Вот и остается сидеть и пить пиво в баре"
            voice "audio/voices/vika/447.mp3"
            Vika "А почему ты не сходишь куда-нибудь еще?"
            voice "audio/voices/clara/55.mp3"
            clara "Куда еще можно сходить в Новом Уренгое? Тут из развлечений только бар и казино. В казино меня не пускают, а в баре бармен может налить за красивые глазки."
            $ i_know_casino = True
            $ i_ask_about_work = True
            $ may_ask_about_casino = True
            jump clara_menu
        "Ты знакома с шахматистами?" if i_ask_about_chees_players == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/448.mp3"
            Vika "Ты знакома с шахматистами?"
            voice "audio/voices/clara/56.mp3"
            clara "Это самое скучное что я видела в своей жизни, они приходят раньше меня, а уходят позже, и все что они делают - это играют в шахматы"
            voice "audio/voices/clara/57.mp3"
            clara "Точнее играют - это сильно сказано, дед пол дня сидит и ждет пока второй тупит, а вторые пол дня орет на него, за то что он так долго тупит"
            voice "audio/voices/clara/58.mp3"
            clara "И то как он орет это самое веселое из всего этого."
            voice "audio/voices/vika/449.mp3"
            Vika "Может тебе стоило поиграть с ними чтоб тебе не было так скучно?"
            voice "audio/voices/clara/59.mp3"
            clara "Ты смеешься? Тот что помладше звал меня 'поиграть', но Во-первых я даже не знаю как это все называется ни одна фигура"
            voice "audio/voices/clara/60.mp3"
            clara "А во-вторых? А во-вторых знаю я такие игры, мне их и на работе хватает. В общем не играю я в шахматы"
            $ i_ask_about_chees_players = True
            jump clara_menu
        "Почему на баре никого нет" if i_ask_about_barmen == False and day_index == 6:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/450.mp3"
            Vika "А почему на баре никого нет?"
            voice "audio/voices/clara/61.mp3"
            clara "Да обычное дело. Ушел «проветриться» — а сам, скорее всего, к той новенькой официантке из соседнего бара подкатывает."
            voice "audio/voices/clara/62.mp3"
            clara "Говорит, они «просто общаются», но я-то вижу — парень конкретно клюнул."
            voice "audio/voices/vika/451.mp3"
            Vika "Почему ты так уверена?"
            voice "audio/voices/clara/63.mp3"
            clara "О, да я таких сразу вычисляю. Стоит мужику на пять секунд задержать взгляд на девушке — и уже всё понятно."
            voice "audio/voices/clara/64.mp3"
            clara "У этого аж потеть начинает, когда она рядом. Ну хоть не врёт, что «она мне как сестра» — это вообще любимая отмачка у женатиков."
            voice "audio/voices/vika/452.mp3"
            Vika "А она-то его как воспринимает?"
            voice "audio/voices/clara/65.mp3"
            clara "Пока терпит. Но если он ещё пару раз «случайно» заденет её руку, когда вино наливает — ей это или надоест, или…"
            voice "audio/voices/clara/66.mp3"
            clara "…ну, в общем, скоро либо скандал, либо свадьба."
            voice "audio/voices/clara/67.mp3"
            clara "Держу пари на сотку — он к закрытию приползёт обратно с глупой улыбкой и начнёт всем рассказывать, какой у него «просто продуктивный диалог получился»."
            $ i_ask_about_barmen = True
            jump clara_menu

        "Можешь подсказать как готовить соус Бешамель?" if kvest_na_lazanyu == True and i_ask_recept == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/clara/68.mp3"
            clara "Его ты должна сготовить в первую очередь"
            voice "audio/voices/clara/69.mp3"
            clara "Добавь в сковороду сливочное масло. Посыпь его мукой. Залей сковородку молоком."
            voice "audio/voices/clara/70.mp3"
            clara "Посоли, Добавь мускатный орех. Слей это все в миску. Вот и все, подсказать что-то еще?"
            jump clara_menu

        "Можешь подсказать как готовить соус Болоньезе?" if kvest_na_lazanyu == True and i_ask_recept == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/clara/71.mp3"
            clara "Кидаешь в сковородку нарезанный лук. Сверху засыпаешь мелко нарезанную морковь. Добавляешь фарш. Солишь. Перчишь"
            voice "audio/voices/clara/72.mp3"
            clara "Добавляешь кетчуп. Сверху томатную пасту. И оставляешь все это на сковородке, а сама приступаешь к сборке лазаньи. Вот и все, подсказать что-то еще?"
            jump clara_menu


        "Напомни как готовить лазанью" if kvest_na_lazanyu == True and i_ask_recept == True:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/clara/73.mp3"
            clara "Конечно. Кладешь в форму соус бешамель. Сверху кладешь лист для лазаньи. Потом соус болоньезе. И посыпаешь тертым сыром."
            voice "audio/voices/clara/74.mp3"
            clara "Запекаешь в духовке 40 минут про 180 градусах. Главное делать все в правильной последовательности. Вот и все, подсказать что-то еще?"
            jump clara_menu
            
        "Ты умеешь готовить?" if kvest_na_lazanyu == True and i_ask_recept == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            Vika "Ты умеешь готовить?"
            voice "audio/voices/clara/75.mp3"
            clara "Ну готовлю иногда, а что?"
            Vika "Ты случайно не знаешь как готовить лазанью?"
            voice "audio/voices/clara/76.mp3"
            clara "А, лазанью, ну это вообще просто. Кладешь в форму соус бешамель. Сверху кладешь лист для лазаньи. Потом соус болоньезе."
            voice "audio/voices/clara/77.mp3"
            clara "И посыпаешь тертым сыром. Запекаешь в духовке 40 минут про 180 градусах. Главное делать все в правильной последовательности. Вот и все, подсказать что-то еще?"
            $ i_ask_recept = True
            jump clara_menu
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/need_go.mp3"
            Vika "Мне пора идти"
            voice "audio/voices/clara/78.mp3"
            clara "Пока!"
            $ block_ui = False
            $ stop_dialog()
            jump slut

screen chess_players:
    if not block_ui:
        imagebutton:
            idle "chess_players_idle.png"
            hover "chess_players_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            if visit_chees_first_time == 1:
                action Jump("visit_chees_first_time")  # Показываем меню выбора
            if visit_chees_first_time == 2:
                action Jump("poprobovat_eshe")  # Показываем меню выбора

label visit_chees_first_time:
    $ start_dialog()
    $ renpy.free_memory()
    $ renpy.music.set_pause(True)
    scene bg slut_blur  # <-- размытый фон
    $ block_ui = True
    show ded angry at Position(xalign=0.8, yalign=1.0)
    $ _preferences.afm_enable = True 
    voice "audio/voices/shahmatist1/1.mp3"
    shahmatist1 "Ты задолбал!!! Как можно думать над одним ходом пол часа???"
    show shahmatist2 neutral at Position(xalign=0.2, yalign=1.0)
    $ _preferences.afm_enable = True 
    voice "audio/voices/shahmatist2/1.mp3"
    shahmatist2 "Ты сам дал мне подумать, теперь жди и пей свое выигранное пиво"
    voice "audio/voices/shahmatist1/2.mp3"
    shahmatist1 "Выигранное пиво я давно выпил и заказал себе новое, а ты ещё ни одну фигуру не подвинул!!!"
    hide shahmatist2 neutral
    show vika neutral at Position(xalign=0.2, yalign=1.0)
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/453.mp3"
    Vika "Кхм Кхм..."
    voice "audio/voices/shahmatist1/3.mp3"
    shahmatist1 "Ой, извините"    
    voice "audio/voices/vika/454.mp3"
    Vika "Что у вас происходит?"
    voice "audio/voices/shahmatist1/4.mp3"
    shahmatist1 "Мы каждый день играем тут в шахматы и каждый день я жду, когда он наконец сделает ход."
    voice "audio/voices/shahmatist1/5.mp3"
    shahmatist1 "В данный момент ему осталось два хода чтобы поставить мат."
    voice "audio/voices/shahmatist1/6.mp3"
    shahmatist1 "Зря я ему это сказал, он не закончит пока не найдет."
    voice "audio/voices/shahmatist1/7.mp3"
    shahmatist1 "Даже ты поставишь мне мат быстрее."
    jump predlagayet_poigrat
    

label predlagayet_poigrat:
    $ renpy.free_memory()
    $ _preferences.afm_enable = True 
    voice "audio/voices/shahmatist1/8.mp3"
    shahmatist1 "О, точно!"
    voice "audio/voices/shahmatist1/9.mp3"
    shahmatist1 "Давай сделаем так: ты сядешь доиграть партию вместо него."
    voice "audio/voices/shahmatist1/10.mp3"
    shahmatist1 "Ты умеешь играть?"
    $ stop_dialog()
    menu:
        "Да":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/shahmatist1/11.mp3"
            shahmatist1 "Тогда садись и покажи этому болвану, как играть в шахматы. Если выйграешь - можешь забрать приз вместо него."
            voice "audio/voices/vika/455.mp3"
            Vika "А на что вы играете?"
            voice "audio/voices/shahmatist1/12.mp3"
            shahmatist1 "На что придется, на всякие мелкие вещи, или на пару рублей. В общем выберешь что забрать, садись."
            $ visit_chees_first_time = 2
            $ block_ui = False
            $ stop_dialog()
            jump play_chess

        "Нет":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/shahmatist1/13.mp3"
            shahmatist1 "Очень жаль, но ты можешь пойти научиться. Если выйграешь - можешь забрать приз вместо него."
            voice "audio/voices/vika/455.mp3"
            Vika "А на что вы играете?"
            voice "audio/voices/shahmatist1/14.mp3"
            shahmatist1 "На что придется, на всякие мелкие вещи, или на пару рублей. В общем выберешь что забрать."
            voice "audio/voices/shahmatist1/15.mp3"
            shahmatist1 "Не волнуйся, ты не опоздаешь, быстрее ты выучишься, чем он найдет ход."
            $ visit_chees_first_time = 2
            $ block_ui = False
            $ stop_dialog()
            jump slut

label poprobovat_eshe:
    $ renpy.free_memory()
    $ renpy.music.set_pause(True)
    $ block_ui = True
    $ stop_dialog()
    menu:
        "Я хочу попробовать поставить мат.":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/456.mp3"
            Vika "Я хочу попробовать поставить мат."
            voice "audio/voices/shahmatist1/16.mp3"
            shahmatist1 "Садись"
            $ block_ui = False
            $ stop_dialog()
            jump play_chess
        "Мне пора идти":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/shahmatist1/17.mp3"
            shahmatist1 "Приходи, будем рады"
            $ block_ui = False
            $ stop_dialog()
            jump slut



label play_chess:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ show_hud()
    $ puzzle_data = get_random_puzzle()
    scene bg play_chess
    show screen chess
    show screen back_arrow_to_slut
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen back_arrow_to_slut:
    zorder 10
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("slut")  # Показываем меню выбора


screen chess:
    default original_puzzle = copy.deepcopy(puzzle_data["board"])
    default puzzle = copy.deepcopy(original_puzzle)
    default solution = puzzle_data["solution"]
    default selected_piece = None
    default move_index = 0
    default auto_move_timer = False

    if auto_move_timer:
        timer 0.8 action Function(do_auto_move_screen_logic)

    grid 8 8 spacing 1:
        xpos 615
        ypos 174
        for i in range(64):
            $ piece = puzzle[i]
            $ bg_color = "#5cf82c88" if selected_piece == i else "#44444400"

            button:
                xsize 94
                ysize 93
                background bg_color
                if not block_ui:
                    action Function(handle_click, i)

                if piece:
                    if i in range(0, 8) and piece == "pw":
                        add "chees/qw.png"
                    else:
                        add "chees/{}.png".format(piece)
                    if "b" in piece:
                        background "#44444400"
                    else:
                        background bg_color

init python:
    import copy

    def handle_click(index):
        #renpy.notify("Нажата клетка: {}".format(index))
        selected_piece = renpy.get_screen_variable("selected_piece")
        puzzle = renpy.get_screen_variable("puzzle")
        solution = renpy.get_screen_variable("solution")
        move_index = renpy.get_screen_variable("move_index")

        if selected_piece is None:
            if puzzle[index]:
                renpy.set_screen_variable("selected_piece", index)
                renpy.sound.play("player_chess.mp3")
        else:
            move = (selected_piece, index)
            expected_move = solution[move_index]

            if move == expected_move:
                # Ход игрока
                puzzle[index] = puzzle[selected_piece]
                puzzle[selected_piece] = ""
                renpy.set_screen_variable("puzzle", puzzle)
                renpy.set_screen_variable("selected_piece", None)
                move_index += 1
                renpy.set_screen_variable("move_index", move_index)

                if move_index < len(solution):
                    renpy.set_screen_variable("auto_move_timer", True)
                    renpy.sound.play("auto_chess.ogg")
                else:
                    original_puzzle = renpy.get_screen_variable("original_puzzle")
                    renpy.set_screen_variable("puzzle", copy.deepcopy(original_puzzle))
                    renpy.set_screen_variable("auto_move_timer", True)
                    renpy.sound.play("auto_chess.ogg")
                    renpy.jump("chess_win")
            else:
                renpy.set_screen_variable("selected_piece", None)

    def do_auto_move_screen_logic():
        puzzle = renpy.get_screen_variable("puzzle")
        solution = renpy.get_screen_variable("solution")
        move_index = renpy.get_screen_variable("move_index")

    # Добавляем защиту от выхода за границы
        if move_index >= len(solution):
            original_puzzle = renpy.get_screen_variable("original_puzzle")
            renpy.set_screen_variable("puzzle", copy.deepcopy(original_puzzle))
            return  # Обязательно выйти после jump

        from_auto, to_auto = solution[move_index]
        puzzle[to_auto] = puzzle[from_auto]
        puzzle[from_auto] = ""
        move_index += 1

        renpy.set_screen_variable("puzzle", puzzle)
        renpy.set_screen_variable("move_index", move_index)
        renpy.set_screen_variable("auto_move_timer", False)
        renpy.sound.play("auto_chess.ogg")

label chess_win:
    $ renpy.free_memory()
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/457.mp3"
    Vika "Ура, у меня получилось!!!"
    voice "audio/voices/shahmatist1/18.mp3"
    shahmatist1 "Молодец, можешь выбрать приз, по призам у нас не густо, они нам нужны только чтобы подогреть интерес"
    hide screen chess
    $ stop_dialog()
    menu:
        "Маленький магнит" if magnet_taken == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/shahmatist1/19.mp3"
            shahmatist1 "Хороший выбор, с магнитом можно делать очень многие вещи, держи!"
            $ add_item_to_inventory("magnet") 
            $ magnet_taken = True       
        "Кисточка" if brush_taken == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/shahmatist1/20.mp3"
            shahmatist1 "Я не художник, может тебе она пригодится"
            $ add_item_to_inventory("brush")
            $ brush_taken = True 
        "Банка пива" if beer_taken == False:
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/shahmatist1/21.mp3"
            shahmatist1 "Я думал ты выберешь что-то получше..."
            $ add_item_to_inventory("beer")
            $ beer_taken = True 
        "Десять рублей":
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/shahmatist1/22.mp3"
            shahmatist1 "За такой великолепный мат я бы дал тебе больше, но бюджет нашего турнира ограничен."
            $ money += 10    
    $ _preferences.afm_enable = True 
    voice "audio/voices/shahmatist1/23.mp3"
    shahmatist1 "Сыграем еще?"
    $ stop_dialog()
    jump poprobovat_eshe
    $ block_ui = False
    jump slut

screen door_to_street:
    if not block_ui:
        imagebutton:
            idle "door_1_idle.png"
            hover "door_1_hover.png"
            xpos 700
            ypos 200
            focus_mask True
            action Jump("street")  # Показываем меню выбора

screen door_to_mainroom:
    if not block_ui:
        imagebutton:
            idle "door_2_idle.png"
            hover "door_2_hover.png"
            xpos 60
            ypos 1
            focus_mask True
            action Jump("mainroom")  # Показываем меню выбора
    
screen door_to_vitya_room:
    if not block_ui:
        imagebutton:
            idle "door_3_idle.png"
            hover "door_3_hover.png"
            xpos 484
            ypos 115
            focus_mask True
            action Jump("vitya_room")  # Показываем меню выбора 

screen door_to_toilet:
    if not block_ui:
        imagebutton:
            idle "door_4_idle.png"
            hover "door_4_hover.png"
            xpos 1152
            ypos 103
            focus_mask True
            action Jump("toilet")  # Показываем меню выбора

screen door_to_kitchen:
    if not block_ui:
        imagebutton:
            idle "door_5_idle.png"
            hover "door_5_hover.png"
            xpos 1370
            ypos -10
            focus_mask True
            action Jump("kitchen")  # Показываем меню выбора      

label password:
    $ renpy.free_memory()
    $ hide_all_ui()
    $ renpy.music.set_pause(True)
    scene bg password
    show screen back_arrow

    if password_first_time_flag:
        $ block_ui = True
        $ start_dialog()
        $ i_know_password = True
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/458.mp3"
        Vika "Пароль? Я не ставила пароль. Надо с этим разобраться."
        $ quest_list[1]["available"] = True
        $ block_ui = False
        $ stop_dialog()
        $ password_first_time_flag = False

    while True:
        $ password = renpy.input("Введите пароль:")
        if slojnost_igry == "easy":
            $ correct_password = correct_easy_password
        if password == correct_password:
            $ block_ui = True
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/459.mp3"
            Vika "Кто вообще ставит пароль ребусами?"
            $ block_ui = False
            $ pc_is_unlocked = True
            $ game_hour += 1
            $ quest_list[1]["done"] = True 
            $ intellect += 1
            $ update_game_time()
            $ remove_item_to_inventory("rebus")
            $ stop_dialog()
            jump pc_work_table
        else:
            $ block_ui = True
            $ _preferences.afm_enable = True 
            "Неверный пароль... Попробуй ещё раз."
            $ block_ui = False

    return

screen back_arrow:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("mainroom")  # Показываем меню выбора  
    
screen back_arrow_to_hallway:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("hallway")  # Показываем меню выбора  

screen back_arrow_to_map:
    if not block_ui:
        imagebutton:
            idle "back_idle.png"
            hover "back_hover.png"
            xpos 1700
            ypos 568
            focus_mask True
            at Transform(zoom=0.3)
            action Jump("street")  # Показываем меню выбора
           
    
label pc_work_table:
    $ renpy.free_memory()
    scene bg windows
    $ hide_all_ui()
    show screen sigame_logo
    show screen back_arrow
    show screen yandex_browzer_logo
    if show_buner == 1:
        show screen buner1
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen sigame_logo:
    imagebutton:
        idle "si_game_idle.png"        
        xpos 50
        ypos 50
        focus_mask True
        if not block_ui:
            hover "si_game_hover.png"
            if day_index == 6 and game_hour == 20 and sigame_is_available == True:
                action Jump("sigame_event")
            elif day_index == 6 and game_hour == 20 and sigame_is_available == False:
                action Jump("go_to_vitya")
            else:
                action Jump("not_8_hour")

label go_to_vitya:
    $ _preferences.afm_enable = True 
    $ start_dialog()
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/460.mp3"
    Vika "Сначала мне нужно поговорить с Витей."
    $ renpy.music.set_pause(False)
    $ stop_dialog()
    call screen wait_for_click
    return

label sigame_event:
    $ hide_all_ui()
    show screen points
    scene bg sigame1
    pause 2.0
    $ question1 = renpy.input("Введите ответ на вопрос:")
    if question1.lower() == "плоскогубцы":
        $ vika_points += 800
    else:
        $ vika_points -= 800
    $ vitya_points += 400
    $ alexander_points += 600
    $ ruslan_points -= 200
    if intellect >= 12:
        scene bg sigame2_easy with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "голубой" or question2.lower() == "голубое" or question2.lower() == "голубого":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 12 and intellect >= 8:
        scene bg sigame2_med with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "1939":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 8 and intellect >= 4:
        scene bg sigame2 with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "амазонка":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 4:
        scene bg sigame2_hard with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "титан":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    $ vitya_points += 400
    $ alexander_points += 600
    $ ruslan_points -= 200
    if intellect >= 12:
        scene bg sigame3_easy with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "4":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 12 and intellect >= 8:
        scene bg sigame3_med with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "древняя греция" or question2.lower() == "греция":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 8 and intellect >= 4:
        scene bg sigame3 with fade 
        pause 2.0
        $ question3 = renpy.input("Введите ответ на вопрос:")
        if question3.lower().replace("ё", "е") == "федор достоевский":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 4:
        scene bg sigame3_hard with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "1991":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    $ vitya_points += 400
    $ alexander_points += 600
    $ ruslan_points -= 200
    if intellect >= 12:
        scene bg sigame4_easy with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "меркурий":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 12 and intellect >= 8:
        scene bg sigame4_med with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "оттава":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 8 and intellect >= 4:
        scene bg sigame4 with fade 
        pause 2.0
        $ question4 = renpy.input("Введите ответ на вопрос:")
        if question4.lower() == "кислород":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 4:
        scene bg sigame4_hard with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "чайковский" or question2.lower() == "петр чайковский" or question2.lower() == "петр ильич чайковский" :
            $ vika_points += 800
        else:
            $ vika_points -= 800
    $ vitya_points += 400
    $ alexander_points += 600
    $ ruslan_points -= 200
    if intellect >= 12:
        scene bg sigame5_easy with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "шрек":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 12 and intellect >= 8:
        scene bg sigame5_med with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "индийский" or question2.lower() == "индийский океан":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 8 and intellect >= 4:
        scene bg sigame5 with fade 
        pause 2.0
        $ question5 = renpy.input("Введите ответ на вопрос:")
        if question5.lower() == "нил армстронг":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    elif intellect < 4:
        scene bg sigame5_hard with fade 
        pause 2.0
        $ question2 = renpy.input("Введите ответ на вопрос:")
        if question2.lower() == "золото":
            $ vika_points += 800
        else:
            $ vika_points -= 800
    $ vitya_points += 400
    $ alexander_points += 600
    $ ruslan_points -= 200
    if vika_points == 4000:
        $ game_hour += 2
        $ update_game_time()
        $ _preferences.afm_enable = True 
        $ start_dialog()
        voice "audio/voices/vika/461.mp3"
        Vika "Ураааааа!!! Мы переезжаем в питер!!!"
        $ quest_list[13]["done"] = True
        $ stop_dialog()
        jump mainroom
    else:
        $ _preferences.afm_enable = True 
        $ start_dialog()
        voice "audio/voices/vika/462.mp3"
        Vika "Кажется не видать мне питера..."
        scene black
        $ stop_dialog()
        hide screen points
        $ vitya_points = 0
        $ alexander_points = 0
        $ ruslan_points = 0
        $ vika_points = 0
        jump loosemenu

label loosemenu:
    menu:
        "Перезапустить игру еще раз":
            $ _preferences.afm_enable = True 
            jump sigame_event
        "Отойти от компьютера":
            $ _preferences.afm_enable = True 
            jump mainroom

screen points:
    text "[vitya_points]" xpos 600 ypos 1014 xanchor 0.5 size 25
    text "[alexander_points]" xpos 1315 ypos 1014 xanchor 0.5 size 25
    text "[vika_points]" xpos 950 ypos 1014 xanchor 0.5 size 25
    text "[ruslan_points]" xpos 230 ypos 1014 xanchor 0.5 size 25

screen yandex_browzer_logo:
    imagebutton:
        idle "yandex_browzer_idle.png"
        xpos 50
        ypos 200
        focus_mask True
        if not block_ui:
            hover "yandex_browzer_hover.png"
            action Jump("yandex_browzer")

label yandex_browzer:
    $ renpy.free_memory()
    scene bg yandex_browzer
    $ hide_all_ui()
    show screen cian
    show screen aviasales
    show screen ph
    show screen casino_sochi
    show screen litres
    show screen back_ya_1
    show screen masterskaya_browzer
    show screen bluegen
    show screen emergene
    if show_buner == 1:
        show screen buner1
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen bluegen:
    imagebutton:
        idle "browzer/bluegen_button.png"
        focus_mask True
        if not block_ui:
            hover "browzer/bluegen_button_hover.png"
            action Jump("bluegen")

label bluegen:
    $ renpy.free_memory()
    scene bg bluegen
    $ hide_all_ui()
    show screen back_to_ya
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen emergene:
    imagebutton:
        idle "browzer/emergen_button.png"
        focus_mask True
        if not block_ui:
            hover "browzer/emergen_button_hover.png"
            action Jump("emergene")

label emergene:
    $ renpy.free_memory()
    scene bg emergene
    $ hide_all_ui()
    show screen back_to_ya
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen cian:
    if not block_ui:
        imagebutton:
            idle "cian_idle.png"
            hover "cian_hover.png"
            focus_mask True
            if vilojeno_obyavleniya == False:
                action Jump("kvartira_klik")
            else:
                action Jump("kvartira_klik1")

label kvartira_klik1:
    $ renpy.free_memory()
    $ vilojeno_obyavleniya = True
    $ hide_all_ui()
    scene bg kvartira_klik1
    show screen back_to_ya
    show screen snyat_button2
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label kvartira_klik:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg kvartira_klik
    show screen back_to_ya
    show screen sdat_button
    show screen snyat_button
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen sdat_button:
    imagebutton:
        idle "browzer/sdat_button.png"
        focus_mask True
        if not block_ui:
            hover "browzer/sdat_button_hover.png"
            if bil_zvonok_shluhe == False:
                action Jump("number")
            else:
                action Jump("ne_nado_sdavat")

screen snyat_button:
    imagebutton:
        idle "browzer/snyat_button.png"
        focus_mask True
        if not block_ui:
            hover "browzer/snyat_button_hover.png"
            if kvartira_snyata == True:
                action Jump("yje_snyala")
            elif money >= 30000:
                action Jump("snyala_kvartiru")
            else:
                action Jump("ne_hvataet")

screen snyat_button2:
    imagebutton:
        idle "browzer/snyat_button2.png"
        focus_mask True
        if not block_ui:
            hover "browzer/snyat_button2_hover.png"
            if kvartira_snyata == True:
                action Jump("yje_snyala")
            elif money >= 30000:
                action Jump("snyala_kvartiru")
            else:
                action Jump("ne_hvataet")

label yje_snyala:
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    $ start_dialog()
    voice "audio/voices/vika/463.mp3"
    Vika "Я уже сняла квартиру, нам не нужна вторая."
    $ renpy.music.set_pause(False)
    $ stop_dialog()
    call screen wait_for_click
    return

label snyala_kvartiru:
    $ renpy.music.set_pause(True)
    $ quest_list[15]["done"] = True
    if bileti_kupleni == True:
        $ quest_list[12]["available"] = True
    $ money -= 30000
    $ kvartira_snyata = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/464.mp3"
    Vika "Есть, квартира снята."
    $ game_hour += 1
    $ stop_dialog()
    $ update_game_time()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label ne_hvataet:
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/465.mp3"
    Vika "У меня не хватает денег, нужно 30000"
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label number:
    $ renpy.music.set_pause(True)
    while True:
        $ number = renpy.input("Введите свой номер в формате +7(ххх) ххх-хх-хх:")

        if number == "+7(943) 356-66-66" or number == "+7 943 356-66-66" or number == "+7943 356-66-66" or number == "+7(943) 3566666" or number == "+7 9433566666" or number == "+79433566666":
            $ block_ui = True
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/466.mp3"
            Vika "Можно считать что сдала квартиру."
            $ game_hour += 1
            $ update_game_time()
            $ block_ui = False
            $ stop_dialog()
            jump kvartira_klik1
        else:
            $ block_ui = True
            $ start_dialog()
            $ _preferences.afm_enable = True 
            voice "audio/voices/vika/467.mp3"
            Vika "С таким номером мне никто не позвонит."
            $ block_ui = False
            $ stop_dialog()

label ne_nado_sdavat:
    $ renpy.free_memory()
    $ _preferences.afm_enable = True 
    $ start_dialog()
    $ renpy.music.set_pause(True)
    voice "audio/voices/vika/468.mp3"
    Vika "Я уже сдала квартиру."
    $ stop_dialog()
    jump kvartira_klik

screen aviasales:
    imagebutton:
        idle "aviasales_idle.png"
        focus_mask True
        if not block_ui:
            hover "aviasales_hover.png"
            action Jump("fly")

label fly:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg fly
    show screen back_to_ya
    show screen kupit
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen kupit:
    imagebutton:
        idle "browzer/kupit.png"
        focus_mask True
        if not block_ui:
            hover "browzer/kupit_hover.png"
            if bileti_kupleni == True:
                action Jump("yje_kupila")
            elif money >= 40000:
                action Jump("kupila_bileti")
            else:
                action Jump("ne_hvataet_na_bileti")

label yje_kupila:
    $ _preferences.afm_enable = True 
    $ renpy.music.set_pause(True)
    $ start_dialog()
    voice "audio/voices/vika/469.mp3"
    Vika "Я уже купила 2 билета."
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label kupila_bileti:
    $ renpy.music.set_pause(True)
    $ quest_list[14]["done"] = True
    if kvartira_snyata == True:
        $ quest_list[12]["available"] = True
    $ money -= 40000
    $ bileti_kupleni = True
    $ _preferences.afm_enable = True 
    $ start_dialog()
    voice "audio/voices/vika/470.mp3"
    Vika "Есть, билеты куплены!"
    $ stop_dialog()
    $ game_hour += 1
    $ update_game_time()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

label ne_hvataet_na_bileti:
    $ renpy.music.set_pause(True)
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/471.mp3"
    Vika "У меня не хватает денег мне нужно 40000."
    $ block_ui = False
    $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen masterskaya_browzer:
    if not block_ui:
        imagebutton:
            idle "masterskaya_browzer_idle.png"
            hover "masterskaya_browzer_hover.png"
            focus_mask True
            action Jump("masterskaya_sait")  # Показываем меню выбора

label masterskaya_sait:
    $ renpy.free_memory()
    $ renpy.music.set_pause(True)
    $ hide_all_ui()
    scene bg masterskaya_browzer
    show screen back_to_ya
    if i_know_masterskaya == False:
        $ block_ui = True 
        $ start_dialog()
        pause 1.0
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/472.mp3"
        Vika "Судя по орфографии он хороший мастер."
        $ i_know_masterskaya = True
        $ block_ui = False 
        $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen casino_sochi:
    if not block_ui:
        imagebutton:
            idle "casino_idle.png"
            hover "casino_hover.png"
            focus_mask True
            action Jump("casino_browzer")  # Показываем меню выбора 

label casino_browzer:
    $ renpy.music.set_pause(True)
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg casino_browzer
    show screen back_to_ya
    if i_know_casino == False:
        $ block_ui = True 
        $ start_dialog()
        pause 1.0
        $ _preferences.afm_enable = True 
        voice "audio/voices/vika/473.mp3"
        Vika "Я не знала, что в Новом Уренгое есть казино."
        $ i_know_casino = True
        $ block_ui = False 
        $ stop_dialog()
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen litres:
    imagebutton:
        idle "litres_idle.png"        
        focus_mask True
        if not block_ui:
            hover "litres_hover.png"
            action Jump("litres_browzer")  # Показываем меню выбора 

label litres_browzer:
    $ renpy.free_memory()
    $ hide_all_ui()
    scene bg litres_browzer
    show screen back_to_ya
    show screen reed_button_1
    show screen reed_button_2
    show screen reed_button_3
    show screen reed_button_4
    show screen reed_button_5
    show screen reed_button_6
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen reed_button_1:
    imagebutton:
        idle "browzer/chees_read.png"        
        focus_mask True
        if not block_ui:
            hover "browzer/chees_read_hover.png"
            action Show("gp_book_page1")

screen gp_book_page1:
    modal True
    add "books/chees/page1.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("gp_book_page1")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("gp_book_page1"), Show("gp_book_page2")]

screen gp_book_page2:
    modal True
    add "books/chees/page2.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("gp_book_page2")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("gp_book_page2"), Show("gp_book_page3")]
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("gp_book_page2"), Show("gp_book_page1")]

screen gp_book_page3:
    modal True
    add "books/chees/page3.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("gp_book_page3")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("gp_book_page3"), Show("gp_book_page4")]
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("gp_book_page3"), Show("gp_book_page2")]

screen gp_book_page4:
    modal True
    add "books/chees/page4.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("gp_book_page4")
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("gp_book_page4"), Show("gp_book_page3")]

screen reed_button_2:
    imagebutton:
        idle "browzer/hp_read.png"        
        focus_mask True
        if not block_ui:
            hover "browzer/hp_read_hover.png"
            action Show("hp_book")

screen hp_book:
    modal True
    add "browzer/hp_book.png"
    imagebutton:
        idle "browzer/hide_book.png"        
        focus_mask True
        if not block_ui:
            action Hide("hp_book")

screen reed_button_3:
    imagebutton:
        idle "browzer/sudoku_read.png"        
        focus_mask True
        if not block_ui:
            hover "browzer/sudoku_read_hover.png"
            action Show("sudoku_book_page1")

screen sudoku_book_page1:
    modal True
    add "books/sudoku/page1.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("sudoku_book_page1")

screen reed_button_4:
    imagebutton:
        idle "browzer/shit_read.png"        
        focus_mask True
        if not block_ui:
            hover "browzer/shit_read_hover.png"
            action Show("shit_book")

screen shit_book:
    modal True
    add "browzer/shit_book.png"
    imagebutton:
        idle "browzer/hide_book.png"        
        focus_mask True
        if not block_ui:
            action Hide("shit_book")

screen reed_button_5:
    imagebutton:
        idle "browzer/colour_read.png"        
        focus_mask True
        if not block_ui:
            hover "browzer/colour_read_hover.png"
            action Show("hair_book_page1")

screen hair_book_page1:
    modal True
    add "books/hair/page1.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("hair_book_page1")

screen reed_button_6:
    imagebutton:
        idle "browzer/meikup_read.png"        
        focus_mask True
        if not block_ui:
            hover "browzer/meikup_read_hover.png"
            action Show("makeup_book_page1")

screen makeup_book_page1:
    modal True
    add "books/makeup/page1.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("makeup_book_page1")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("makeup_book_page1"), Show("makeup_book_page2")]

screen makeup_book_page2:
    modal True
    add "books/makeup/page2.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("makeup_book_page2")
    imagebutton:
        idle "books/fishbook/next_page.png"
        hover "books/fishbook/next_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("makeup_book_page2"), Show("makeup_book_page3")]
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("makeup_book_page2"), Show("makeup_book_page1")]

screen makeup_book_page3:
    modal True
    add "books/makeup/page3.png"
    imagebutton:
        idle "krest_book.png"
        focus_mask True
        if not block_ui:
            action Hide("makeup_book_page3")
    imagebutton:
        idle "books/fishbook/last_page.png"
        hover "books/fishbook/last_page_hover.png"
        focus_mask True
        if not block_ui:
            action [Hide("makeup_book_page3"), Show("makeup_book_page2")]

screen ph:
    imagebutton:
        idle "ph_idle.png"        
        focus_mask True
        if not block_ui:
            hover "ph_hover.png"
            action Jump("pornhub")  # Показываем меню выбора 

init:
    transform slide_up:
        ypos 1.0    # Начинаем за нижней границей
        linear 1.5 ypos 0.0  # Плавно поднимаемся к верхней

label pornhub:
    $ renpy.free_memory()
    $ renpy.music.set_pause(True)
    $ hide_all_ui()
    scene bg pornhub
    show screen back_to_ya
    if show_buner == 0:
        $ block_ui = True        
        show screen buner
        $ show_buner = 1
        $ quest_list[4]["available"] = True
        pause 2.0
        $ _preferences.afm_enable = True 
        $ start_dialog()
        voice "audio/voices/vika/474.mp3"
        Vika "О нет!!! Надо срочно убрать это отсюда!"
        $ block_ui = False 
        $ stop_dialog()
    elif show_buner == 1:
        show screen buner1
    $ renpy.music.set_pause(False)
    call screen wait_for_click

    return

screen buner:
    frame:
        at slide_up  # ← Применяем анимацию к контейнеру
        background None
        add "buner.png"

screen buner1:
    add "buner.png"

screen back_to_ya:
    if not block_ui:
        imagebutton:
            idle "back_ya_1_idle.png"
            hover "back_ya_1_hover.png"
            focus_mask True
            action Jump("yandex_browzer")  # Показываем меню выбора 

screen back_ya_1:
    if not block_ui:
        imagebutton:
            idle "back_ya_1_idle.png"
            hover "back_ya_1_hover.png"
            focus_mask True
            action Jump("pc_work_table")  # Показываем меню выбора 

label not_8_hour:
    $ renpy.free_memory()
    $ renpy.music.set_pause(True)
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/475.mp3"
    Vika "Игра проходит только в воскресенье в 8 часов"
    $ block_ui = False
    $ stop_dialog()
    jump pc_work_table    
    
screen rebus_mainroom:
    imagebutton:
        if slojnost_igry == "easy":
            idle "rebus_easy_idle.png"
        else:
            idle "rebus_idle.png"
        xpos 900
        ypos 217
        focus_mask True
        at Transform(zoom=0.1)
        if not block_ui:
            if slojnost_igry == "easy":
                hover "rebus_easy_hover.png"
            else:
                hover "rebus_hover.png"    
            action Jump("taking_rebus")  # Показываем меню выбора    

label taking_rebus:
    $ renpy.music.set_pause(True)
    $ block_ui = True
    $ start_dialog()
    $ _preferences.afm_enable = True 
    voice "audio/voices/vika/476.mp3"
    Vika "Вот нафига нам нужны эти ребусы???"
    $ block_ui = False
    $ stop_dialog()
    hide screen rebus_mainroom
    $ add_item_to_inventory("rebus")  # Добавляем ребус в инвентарь
    $ take_rebus_from_box_mainroom = True
    $ renpy.music.set_pause(False)
    call screen wait_for_click
    return

screen rebus_inventory:
    modal True
    if slojnost_igry == "easy":
        add "rebus_easy_idle.png" at Transform(zoom=0.6) xpos 350 ypos 200
    else:
        add "rebus_idle.png" at Transform(zoom=0.6) xpos 350 ypos 200
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1445
            ypos 132
            focus_mask True
            action Hide("rebus_inventory")  # Показываем меню выбора 


label psih_bolnitsa:
    $ renpy.free_memory()    
    scene bg psihushka
    show medsestra
    with perehod_diss
    $ block_ui = True
    $ _preferences.afm_enable = True 
    Medsestra "Ну вот, Вика, а ты боялась пить таблетки."

    Medsestra "Больше не рисуй экскриментами на стенах."
    $ block_ui = False
    hide medsestra

    menu:

        "Да.":
            jump choice1_yes

        "Нет.":
            jump choice1_no


init python:

    # Функция проверки правильности решения
    def check_solution():
        global sudoku_puzzle, sudoku_solution, sudoku_proideno, sudoku_puzzle_default

    # Проверяем, что все изменённые клетки соответствуют правильному решению
        for r in range(9):
            for c in range(9):
                # Игнорируем клетки, которые не были изменены (они должны быть такими, как в стандартной сетке)
                if sudoku_puzzle[r][c] != 0 and sudoku_puzzle[r][c] != sudoku_puzzle_default[r][c]:
                    if sudoku_puzzle[r][c] != sudoku_solution[r][c]:
                        sudoku_proideno = False  # Если хотя бы одно значение неверное, решение не найдено
                        return False  # Ранний выход, если решение неправильное

        # Если все клетки, которые были изменены, верны
        sudoku_proideno = True
        return True

    # Функция обработки нажатия на клетку
    def handle_cell(i):
        global selected_cell
        selected_cell = i

        # После каждого изменения сразу проверяем решение
        check_solution()

    # Функция обработки нажатия на цифру
    def handle_number(num):
        global selected_cell, sudoku_puzzle
        if selected_cell is not None:
            r = selected_cell // 9
            c = selected_cell % 9
            # Записываем цифру в выбранную клетку, если это не стандартное значение
            if sudoku_puzzle_default[r][c] == 0:
                sudoku_puzzle[r][c] = num
                # После изменения проверяем решение
                check_solution()

    # Функция очистки клетки
    def clear_cell():
        global selected_cell, sudoku_puzzle
        if selected_cell is not None:
            r = selected_cell // 9
            c = selected_cell % 9
            # Очищаем клетку, если она не является стандартной
            if sudoku_puzzle_default[r][c] == 0:
                sudoku_puzzle[r][c] = 0
                # После очистки проверяем решение
                check_solution()

screen sudoku_game:
    zorder 99
    modal True
    add "sudoku.png"
    if not block_ui:
        imagebutton:
            idle "krest_idle.png"
            xpos 1165
            ypos 22
            focus_mask True
            at Transform(zoom=0.6)
            action [Show("big_iphone"), Hide("sudoku_game")]

    tag sudoku
    
    # Левая панель с цифрами и очисткой
    hbox:
        vbox spacing 5 xpos 600 ypos 160:
            # Цифры 1–9
            for num in range(1, 10):
                button:
                    background Solid("#444444")
                    hover_background Solid("#666666")
                    xsize 40 ysize 40
                    action Function(handle_number, num)
                    text str(num) xalign 0.5 yalign 0.5 size 24 color "#fff"

            # Кнопка очистки
            button:
                background Solid("#ff4444")
                hover_background Solid("#ff6666")
                xsize 40 ysize 40
                action Function(clear_cell)
                text "C" xalign 0.5 yalign 0.5 size 24 color "#fff"

    # Основная 9×9 сетка
    grid 9 9 spacing 1:
        xpos 735
        ypos 163
        for i in range(81):
            $ r = i // 9
            $ c = i % 9
            $ val = sudoku_puzzle[r][c]
            $ bg = "#5cf82c88" if selected_cell == i else "#44444400"

            button:
                xsize 50 ysize 50
                background bg
                action Function(handle_cell, i)

                if val != 0:
                    text str(val) xalign 0.5 yalign 0.5 size 24 color "#000"

label titri:
    scene black with Fade(1.0, 1.0, 1.0)
    $ renpy.movie_cutscene("spoiler.webm")
    play music "outro.mp3" fadein 2.0  # Фоновая музыка

    # Показываем экран с титрами
    show screen scrolling_credits
    $ renpy.pause(315.0, hard=True)  # Ждём 15 секунд (регулируйте)
    hide screen scrolling_credits

    stop music fadeout 2.0
    $ MainMenu(confirm=False)()

screen scrolling_credits():
    zorder 100  # Поверх других элементов

    # Основной контейнер для титров (центрированный)
    frame:
        xalign 0.5
        yanchor 0.0
        ypos 1.0  # Начинаем снизу экрана
        xsize 1000
        ysize 8000  # Больше высоты экрана для прокрутки

        background None  # Прозрачный фон

        # Анимация подъёма
        at transform:
            linear 300.0 ypos -5.0  # 15 секунд до полной прокрутки

        # Содержимое титров
        vbox:
            spacing 30
            xalign 0.5

            # Пустое пространство в начале (чтобы текст появлялся снизу)
            null height 1100

            # Ваши титры
            text "{size=60}Head Family: Travel To SPB{/size}" xalign 0.5
            text "{size=30}Разработчик - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Гейм-дизайнер - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Автор идеи - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Продюсер - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Программист - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Сценарист - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Художник - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Композитор - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Звукорежиссер - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Тестировщик - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Дизайн уровней - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Дизайн интерфейса - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Маркетолог - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Менеджер сообщества - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Монтажёр - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Переводчик - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Оптимизатор - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Технический директор - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Креативный директор - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Главный нарративный дизайнер - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Дизайнер персонажей - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Концепт-артист - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Геймплей-программист - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Световой художник - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Дизайнер достижений - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Скрипт-райтер - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Генератор случайных идей - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Специалист по балансу - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Создатель атмосферы - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Хранитель лора - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Вдохновитель - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Босс багов - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Мастер Ctrl+C / Ctrl+V - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Тот, кто всё это придумал - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Директор по крикам в монитор - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Главный по прокрастинации - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Офисный кактус - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Человек-оркестр - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Властелин кода - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Повелитель геймдизайна - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Архитектор миров - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Верховный разработчик - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=30}Легенда одиночной разработки - Иван Тамбовцев{/size}" xalign 0.5
            text "{size=60}Роли озвучивали{/size}" xalign 0.5
            text "{size=30}Вика - Larisa Actrisa{/size}" xalign 0.5
            text "{size=30}Витя - Callum{/size}" xalign 0.5
            text "{size=30}Клара - Anna Sokolova{/size}" xalign 0.5
            text "{size=30}Алина - Nadia{/size}" xalign 0.5
            text "{size=30}Арина - Kate - Human{/size}" xalign 0.5
            text "{size=30}Артём - Arnav – Empathetic Voice{/size}" xalign 0.5
            text "{size=30}Бармен - Boy Advertising: Radio Ads & Audio{/size}" xalign 0.5
            text "{size=30}Чингыс - Kazım Emirhan Erdem{/size}" xalign 0.5
            text "{size=30}Диллер - Nikolay{/size}" xalign 0.5
            text "{size=30}Эдик - Boy Docu – Youthful Tagalog{/size}" xalign 0.5
            text "{size=30}Рыбак - Olivier D{/size}" xalign 0.5
            text "{size=30}Сисадмин - Denis - Russian male{/size}" xalign 0.5
            text "{size=30}Создатель - Chris{/size}" xalign 0.5
            text "{size=30}Мент - Leo Fioravante{/size}" xalign 0.5
            text "{size=30}Фотограф - Modulated French female voice{/size}" xalign 0.5
            text "{size=30}Начальник - Deok su{/size}" xalign 0.5
            text "{size=30}Охранник - Vasiliy{/size}" xalign 0.5
            text "{size=30}Оператор - Isla Skye{/size}" xalign 0.5
            text "{size=30}Секретарша - Julia - German female{/size}" xalign 0.5
            text "{size=30}Первый шахматист - Vasiliy{/size}" xalign 0.5
            text "{size=30}Второй шахматист - Galway man{/size}" xalign 0.5
            text "{size=30}Учитель - Elegant Russian Narrator {/size}" xalign 0.5
            text "{size=30}Турникет - ChatGPT{/size}" xalign 0.5
            text "{size=30}Ведущий - James - Calm & comforting male voice{/size}" xalign 0.5
            text "{size=30}Начальник полиции - Papazon - Japanese Comedy Villain{/size}" xalign 0.5
            text "{size=60}Спасибо за то что играли!{/size}" xalign 0.5
            



            # Пустое пространство в конце
            null height 800
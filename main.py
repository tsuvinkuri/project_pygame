import pygame
import random
import sys
WIDTH = 800
HEIGHT = 640
sec = 0
duration_game = 2000
game_points = 0
game_true_background = 0
game_true_button = 0
FPS = 30
max_game_points = 0
button_back_to_menu_pressed = False
button_pressed = False
game_play_now = False
index_background = random.randint(0, 2)
backgrounds = ["background_1.jpg", "background_2.jpg", "background_3.jpg"]
bg = pygame.image.load(backgrounds[index_background])
pygame.mixer.init()
pygame.mixer.music.load("game_music.wav")
pygame.mixer.music.play(-1)
different_ball = random.randint(0, 4)


class Black_Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.index_ball = random.randint(0, 4)
        image = pygame.image.load("black_ball.png")
        self.image = image
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 640), HEIGHT / 15)

    def update(self):
        self.rect.y += 15


class Green_Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.index_ball = random.randint(0, 4)
        image = pygame.image.load("lucky_ball.png")
        self.image = image
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 640), HEIGHT / 15)

    def update(self):
        self.rect.y += 20


class Red_Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.index_ball = random.randint(0, 4)
        image = pygame.image.load("red_ball.png")
        self.image = image
        self.image = pygame.transform.rotozoom(self.image, 0, 0.035)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 640), HEIGHT / 15)

    def update(self):
        self.rect.y += 20


class Blue_Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.index_ball = random.randint(0, 4)
        image = pygame.image.load("blue_ball.png")
        self.image = image
        self.image = pygame.transform.rotozoom(self.image, 0, 0.09)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 640), HEIGHT / 15)

    def update(self):
        self.rect.y += 15


class Brown_Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.index_ball = random.randint(0, 4)
        image = pygame.image.load("brown_ball.png")
        self.image = image
        self.image = pygame.transform.rotozoom(self.image, 0, 0.09)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 640), HEIGHT / 15)

    def update(self):
        self.rect.y += 20


class Boom(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__(all_sprites)
        image = pygame.image.load("boom.png")
        self.image = image
        self.k = 0
        self.image = pygame.transform.rotozoom(self.image, 0, 0.05)
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.time = None

    def update(self):
        self.k += 0.033
        if self.k > 0.15:
            all_sprites.remove(self)


class Background_button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        image = pygame.image.load("background_button.jpg")
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        global game_true_background
        if game_true_background > 0:
            all_sprites.remove(self)
            game_true_background = 0


class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        image = pygame.image.load("button_2.jpg")
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 15, HEIGHT / 2 + 35)

    def update(self):
        global game_true_button
        if game_true_button > 0:
            all_sprites.remove(self)
            game_true_button = 0


class Button_start_game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        image = pygame.image.load("button_start_game.jpg")
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 15, HEIGHT / 2 - 200)

    def dead(self):
        self.kill()


class Button_rules(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        image = pygame.image.load("button_settings.jpg")
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 15, HEIGHT / 2 - 50)

    def dead(self):
        self.kill()


class Button_exit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        image = pygame.image.load("button_exit.jpg")
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 15, HEIGHT / 2 + 100)

    def dead(self):
        self.kill()

class Button_rules_write(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        image = pygame.image.load("button_rules.jpg")
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def dead(self):
        self.kill()

class Button_exit_to_menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        image = pygame.image.load("button_exit_to_menu.jpg")
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (50, 20)



def start_game():
    global different_ball
    global FPS
    global sec
    global duration_game
    global game_points
    global game_true_background
    global game_true_button
    global bg
    global buttons_menu_sprites
    global button_pressed
    global max_game_points
    DISPLAY = (WIDTH, HEIGHT)
    lvl_speed = 0
    button_pressed = True
    clock.tick(FPS)
    pygame.font.init()
    screen = pygame.display.set_mode(DISPLAY)
    sec += 0.033
    duration_game -= 5
    if lvl_speed < 0.6:
        lvl_speed += 0.001
    if sec > 0.7 - lvl_speed:
        different_ball = random.randint(0, 4)
        if different_ball == 0:
            black_ball = Black_Ball()
            black_balls.append(black_ball)
        if different_ball == 1:
            lucky_ball = Green_Ball()
            green_balls.append(lucky_ball)
        if different_ball == 2:
            red_ball = Red_Ball()
            red_balls.append(red_ball)
        if different_ball == 3:
            blue_ball = Blue_Ball()
            blue_balls.append(blue_ball)
        if different_ball == 4:
            brown_ball = Brown_Ball()
            brown_balls.append(brown_ball)
        sec = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        game_true_background += 1
                        game_true_button += 1
                        game_points = 0
                        lvl_speed = 0
                        sec = 0
                        duration_game = 1000
                        background_button_1 = Background_button()
                        button_1 = Button()
                        button_1.kill()
                        background_button_1.kill()
                        button_sprites.remove(background_button_1)
                        button_sprites.remove(button_1)
                        for background_button in background_butt:
                            background_butt.remove(background_button)
                        buttons.remove(button)
                for black_ball in black_balls:
                    if black_ball.rect.collidepoint(event.pos):
                        boom = Boom(event.pos)
                        all_sprites.remove(black_ball)
                        black_balls.remove(black_ball)
                        black_ball.kill()
                        sound_boom = pygame.mixer.Sound("boom_sound.wav")
                        sound_boom.play()
                        all_sprites.add(boom)
                        if game_points > 0:
                            if game_points % 2 == 0:
                                game_points = game_points // 2
                            else:
                                game_points = (game_points - 1) // 2
                        booms.append(boom)
                for green_ball in green_balls:
                    if green_ball.rect.collidepoint(event.pos):
                        boom = Boom(event.pos)
                        all_sprites.remove(green_ball)
                        green_balls.remove(green_ball)
                        green_ball.kill()
                        sound_boom = pygame.mixer.Sound("boom_sound.wav")
                        sound_boom.play()
                        all_sprites.add(boom)
                        game_points = game_points * 2
                        booms.append(boom)
                for red_ball in red_balls:
                    if red_ball.rect.collidepoint(event.pos):
                        boom = Boom(event.pos)
                        all_sprites.remove(red_ball)
                        red_balls.remove(red_ball)
                        red_ball.kill()
                        sound_boom = pygame.mixer.Sound("boom_sound.wav")
                        sound_boom.play()
                        all_sprites.add(boom)
                        game_points += 10
                        booms.append(boom)
                for blue_ball in blue_balls:
                    if blue_ball.rect.collidepoint(event.pos):
                        boom = Boom(event.pos)
                        all_sprites.remove(blue_ball)
                        blue_balls.remove(blue_ball)
                        blue_ball.kill()
                        sound_boom = pygame.mixer.Sound("boom_sound.wav")
                        sound_boom.play()
                        all_sprites.add(boom)
                        if game_points >= 15:
                            game_points -= 15
                        else:
                            game_points = 0
                        booms.append(boom)
                for brown_ball in brown_balls:
                    if brown_ball.rect.collidepoint(event.pos):
                        boom = Boom(event.pos)
                        all_sprites.remove(brown_ball)
                        brown_balls.remove(brown_ball)
                        brown_ball.kill()
                        sound_boom = pygame.mixer.Sound("boom_sound.wav")
                        sound_boom.play()
                        all_sprites.add(boom)
                        game_points += 15
                        booms.append(boom)
    all_sprites.update()
    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)
    if duration_game <= 0:
        for i in all_sprites:
            all_sprites.remove(i)
        if sec >= 0:
            sec = -10
        background_button = Background_button()
        button = Button()
        button_sprites.add(background_button)
        button_sprites.add(button)
        buttons.append(button)
        background_butt.append(background_button)
        if game_points > max_game_points:
            max_game_points = game_points
        text_result = pygame.font.SysFont('Comic Sans MS', 30)
        text_new_start = pygame.font.SysFont('Comic Sans MS', 30)
        text_best_score = pygame.font.SysFont('Comic Sans MS', 21)
        text_best_score = text_best_score.render(f"Лучший счет: {max_game_points}", False, (0, 0, 0))
        text_result = text_result.render(f"Поздравляю, вы набрали {str(game_points)} очков", False, (0, 0, 0))
        text_new_start = text_new_start.render(f"Начать сначала?", False, (0, 0, 0))
        screen.blit(text_result, (170, 240))
        screen.blit(text_new_start, (295, 332))
        screen.blit(text_best_score, (325, 200))
    pygame.display.flip()

button_back_to_menu = False
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()
buttons_menu_sprites = pygame.sprite.Group()
button_rules_sprites = pygame.sprite.Group()
button_exit_to_menu_sprites = pygame.sprite.Group()
black_balls = []
green_balls = []
red_balls = []
blue_balls = []
brown_balls = []
booms = []
buttons = []
background_butt = []


def main():
    global button_back_to_menu
    global game_play_now
    global bg
    global button_pressed
    pygame.init()
    pygame.display.set_caption("Разноцветные шары")
    running = True
    DISPLAY = (WIDTH, HEIGHT)
    pygame.font.init()
    screen = pygame.display.set_mode(DISPLAY)
    screen.blit(bg, (0, 0))
    button_start_game = Button_start_game()
    button_rules = Button_rules()
    button_exit = Button_exit()
    buttons_menu_sprites.add(button_start_game)
    buttons_menu_sprites.add(button_rules)
    buttons_menu_sprites.add(button_exit)
    buttons_menu_sprites.update()
    buttons_menu_sprites.draw(screen)
    text_start_game = pygame.font.SysFont('Comic Sans MS', 30)
    text_rules = pygame.font.SysFont('Comic Sans MS', 30)
    text_exit = pygame.font.SysFont('Comic Sans MS', 30)
    text_start_game = text_start_game.render('Начать игру', False, (0, 0, 0))
    text_rules = text_rules.render('Правила', False, (0, 0, 0))
    text_exit = text_exit.render('Выйти', False, (0, 0, 0))
    screen.blit(text_start_game, (335, 95))
    screen.blit(text_rules, (355, 245))
    screen.blit(text_exit, (373, 395))
    while running:
        if game_play_now:
            start_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_start_game.rect.collidepoint(event.pos) and button_pressed is False:
                        for button_1 in button_rules_sprites:
                            button_1.kill()
                            button_rules_sprites.remove(button_1)
                        for button_2 in button_exit_to_menu_sprites:
                            button_2.kill()
                            button_exit_to_menu_sprites.remove(button_2)
                        screen.blit(bg, (0, 0))
                        game_play_now = True
                        for button in buttons_menu_sprites:
                            buttons_menu_sprites.remove(button)
                            button.kill()
                    if button_exit.rect.collidepoint(event.pos) and button_pressed is False:
                        sys.exit()
                    if button_rules.rect.collidepoint(event.pos) and button_pressed is False:
                        screen.blit(bg, (0, 0))
                        for button in buttons_menu_sprites:
                            button.kill()
                        button_pressed = True
                        pygame.display.update()
                        button_rules_write = Button_rules_write()
                        button_rules_sprites.add(button_rules_write)
                        button_rules_sprites.update()
                        button_rules_sprites.draw(screen)
                        text_rules_write_1 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_2 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_3 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_4 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_5 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_6 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_7 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_8 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_9 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_10 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_exit_to_menu_1 = pygame.font.SysFont('Comic Sans MS', 18)
                        text_rules_write_1 = text_rules_write_1.render('В данной игре нужно лопать шары, которые дают', False, (0, 0, 0))
                        text_rules_write_2 = text_rules_write_2.render('вам очки и стараться избегать те, которые отнимают.', False, (0, 0, 0))
                        text_rules_write_3 = text_rules_write_3.render('В конце игры вам покажут ваш результат и лучший', False, (0, 0, 0))
                        text_rules_write_4 = text_rules_write_4.render('Информация по поводу очков за лопание', False, (0, 0, 0))
                        text_rules_write_5 = text_rules_write_5.render('определенных шаров представлена ниже:', False, (0, 0, 0))
                        text_rules_write_6 = text_rules_write_6.render('Черный шар - уменьшает кол-во очков в 2 раза', False, (0, 0, 0))
                        text_rules_write_7 = text_rules_write_7.render('Зеленый шар - увеличивает кол-во очков в 2 раза', False, (0, 0, 0))
                        text_rules_write_8 = text_rules_write_8.render('Красный шар - увеличивает кол-во очков на 10', False, (0, 0, 0))
                        text_rules_write_9 = text_rules_write_9.render('Синий - уменьшает кол-во очков на 15', False, (0, 0, 0))
                        text_rules_write_10 = text_rules_write_10.render('Коричневый - увеличивает кол-во очков на 15', False,(0, 0, 0))
                        text_exit_to_menu = text_exit_to_menu_1.render('Назад', False, (0, 0, 0))
                        screen.blit(text_rules_write_1, (176, 180))
                        screen.blit(text_rules_write_2, (176, 205))
                        screen.blit(text_rules_write_3, (176, 230))
                        screen.blit(text_rules_write_4, (176, 255))
                        screen.blit(text_rules_write_5, (176, 280))
                        screen.blit(text_rules_write_6, (176, 325))
                        screen.blit(text_rules_write_7, (176, 350))
                        screen.blit(text_rules_write_8, (176, 375))
                        screen.blit(text_rules_write_9, (176, 400))
                        screen.blit(text_rules_write_10, (176, 425))
                        button_exit_to_menu = Button_exit_to_menu()
                        button_exit_to_menu_sprites.add(button_exit_to_menu)
                        button_exit_to_menu_sprites.draw(screen)
                        button_exit_to_menu_sprites.update()
                        screen.blit(text_exit_to_menu, (30, 10))
                        button_back_to_menu = True
                    if button_back_to_menu is True:
                        if event.pos[0] < 135 and event.pos[1] < 45:
                            button_pressed = False
                            screen.blit(bg, (0, 0))
                            button_start_game = Button_start_game()
                            button_rules = Button_rules()
                            button_exit = Button_exit()
                            buttons_menu_sprites.add(button_start_game)
                            buttons_menu_sprites.add(button_rules)
                            buttons_menu_sprites.add(button_exit)
                            buttons_menu_sprites.update()
                            buttons_menu_sprites.draw(screen)
                            text_start_game = pygame.font.SysFont('Comic Sans MS', 30)
                            text_rules = pygame.font.SysFont('Comic Sans MS', 30)
                            text_exit = pygame.font.SysFont('Comic Sans MS', 30)
                            text_start_game = text_start_game.render('Начать игру', False, (0, 0, 0))
                            text_rules = text_rules.render('Правила', False, (0, 0, 0))
                            text_exit = text_exit.render('Выйти', False, (0, 0, 0))
                            screen.blit(text_start_game, (335, 95))
                            screen.blit(text_rules, (355, 245))
                            screen.blit(text_exit, (373, 395))
                            button_back_to_menu = False
        pygame.display.flip()
    pygame.quit()


main()
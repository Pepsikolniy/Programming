import pygame
import random
import os
import time
import requests
import json
import sys

WIDTH = 1920 # Ширина всего окна
HEIGHT = 1080 # Высота всего окна
GAME_BORDER_LEFT = 648
GAME_BORDER_RIGHT = 1272
FPS = 60 # Частота кадров в секунду

# Константное время
TIME_TO_TILES = time.time()
TIME_TO_PIZZA = time.time()

# Цвета RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
sounds_folder = os.path.join(game_folder, 'sounds')

# Загружаем все необходимые картинки
bg_in_game = pygame.image.load(os.path.join(img_folder, 'bg_in_game.jpg'))
bg_in_menu = pygame.image.load(os.path.join(img_folder, 'bg_in_menu.jpg'))
help = pygame.image.load(os.path.join(img_folder, 'help.png'))
margin = pygame.image.load(os.path.join(img_folder, 'bg.png'))
pause = pygame.image.load(os.path.join(img_folder, 'pause.png'))
bg_event = pygame.image.load(os.path.join(img_folder, 'bg_event.png'))
bg_event_1 = pygame.image.load(os.path.join(img_folder, 'bg_event_1.png'))
pause_label = pygame.image.load(os.path.join(img_folder, 'pause_label.png'))
you_lose_label = pygame.image.load(os.path.join(img_folder, 'you_lose_label.png'))
rating_label = pygame.image.load(os.path.join(img_folder, 'rating_label.png'))
close_btn = pygame.image.load(os.path.join(img_folder, 'close_btn.png'))
face = pygame.image.load(os.path.join(img_folder, 'face.png'))
number_1 = pygame.image.load(os.path.join(img_folder, '1.png'))
number_2 = pygame.image.load(os.path.join(img_folder, '2.png'))
number_3 = pygame.image.load(os.path.join(img_folder, '3.png'))
number_4 = pygame.image.load(os.path.join(img_folder, '4.png'))
number_5 = pygame.image.load(os.path.join(img_folder, '5.png'))
drink_a_cup_of_tea = pygame.image.load(os.path.join(img_folder, 'drink_a_cup_of_tea.png'))
table = pygame.image.load(os.path.join(img_folder, 'table.png'))
table_2 = pygame.image.load(os.path.join(img_folder, 'table_2.png'))
menu = pygame.image.load(os.path.join(img_folder, 'menu.png'))
restart = pygame.image.load(os.path.join(img_folder, 'restart.png'))
play_2 = pygame.image.load(os.path.join(img_folder, 'play_2.png'))
play = pygame.image.load(os.path.join(img_folder, 'play.png'))
rating_2 = pygame.image.load(os.path.join(img_folder, 'rating_2.png'))
rating = pygame.image.load(os.path.join(img_folder, 'rating.png'))
about = pygame.image.load(os.path.join(img_folder, 'about.png'))
border = pygame.image.load(os.path.join(img_folder, 'border.png'))
close = pygame.image.load(os.path.join(img_folder, 'close.png'))
stars_0 = pygame.image.load(os.path.join(img_folder, 'stars_0.png'))
stars_1 = pygame.image.load(os.path.join(img_folder, 'stars_1.png'))
stars_2 = pygame.image.load(os.path.join(img_folder, 'stars_2.png'))
stars_3 = pygame.image.load(os.path.join(img_folder, 'stars_3.png'))
music_on = pygame.image.load(os.path.join(img_folder, 'music_on.png'))
music_off = pygame.image.load(os.path.join(img_folder, 'music_off.png'))
logo = pygame.image.load(os.path.join(img_folder, 'logo.png'))
input_label = pygame.image.load(os.path.join(img_folder, 'input_label.png'))
input_label_entry = pygame.image.load(os.path.join(img_folder, 'input_label_entry.png'))
input_label_reg = pygame.image.load(os.path.join(img_folder, 'input_label_reg.png'))
label_2 = pygame.image.load(os.path.join(img_folder, 'label_2.png'))
label_3 = pygame.image.load(os.path.join(img_folder, 'label_3.png'))
load = pygame.image.load(os.path.join(img_folder, 'load.png'))
tile_left_border = pygame.image.load(os.path.join(img_folder, 'tile31.png'))
tile_right_border = pygame.image.load(os.path.join(img_folder, 'tile30.png'))
tile = pygame.image.load(os.path.join(img_folder, 'tile32.png'))
tile_ground = pygame.image.load(os.path.join(img_folder, 'tile52.png'))
tile_ground_left_border = pygame.image.load(os.path.join(img_folder, 'tile55.png'))
tile_ground_right_border = pygame.image.load(os.path.join(img_folder, 'tile53.png'))
heart_img = pygame.image.load(os.path.join(img_folder, 'heart.png'))
pizza_img = pygame.image.load(os.path.join(img_folder, 'Pizza.png'))
walkRight = [pygame.image.load(os.path.join(img_folder, 'right_1.png')),
pygame.image.load(os.path.join(img_folder, 'right_2.png')), pygame.image.load(os.path.join(img_folder, 'right_3.png')),
pygame.image.load(os.path.join(img_folder, 'right_4.png')), pygame.image.load(os.path.join(img_folder, 'right_5.png')),
pygame.image.load(os.path.join(img_folder, 'right_6.png'))]
walkLeft = [pygame.image.load(os.path.join(img_folder, 'left_1.png')),
pygame.image.load(os.path.join(img_folder, 'left_2.png')), pygame.image.load(os.path.join(img_folder, 'left_3.png')),
pygame.image.load(os.path.join(img_folder, 'left_4.png')), pygame.image.load(os.path.join(img_folder, 'left_5.png')),
pygame.image.load(os.path.join(img_folder, 'left_6.png'))]
player_img = pygame.image.load(os.path.join(img_folder, 'idle.png'))

# Загружаем музыку
pygame.mixer.init()
sound_eating = pygame.mixer.Sound(os.path.join(sounds_folder,'eating.mp3'))
sound_damage = pygame.mixer.Sound(os.path.join(sounds_folder,'minecraft_damage.mp3'))

# Создаём спрайт игрового персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50,50))
        self.image = player_img
        self.image.set_colorkey(WHITE)
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.width = 48
        self.x = WIDTH/2
        self.y = 888
        self.rect.center = (self.x, self.y)

        # Прыжок
        self.is_jump = False
        self.jump_count = 10
        self.speed = 6

        #Гравитация
        self.gravitation_count = 0

        # Анимация
        self.right = False
        self.left = False
        self.animCount = 0

    def update(self):
        if not paused:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and self.rect.x < GAME_BORDER_RIGHT-60-15:
                self.right = True
                self.left = False
                if not move_is_blocked_right:
                    self.rect.x += self.speed
            elif keys[pygame.K_LEFT] and self.rect.x > GAME_BORDER_LEFT+15:
                self.right = False
                self.left = True
                if not move_is_blocked_left:
                    self.rect.x -= self.speed
            elif keys[pygame.K_UP]:
                self.rect.y -= 3

            else:
                self.right = False
                self.left = False
                self.animCount = 0
            '''if not(move_is_blocked_top):
                self.rect.y += 1'''


            #if not move_is_blocked_top:
            if not(self.is_jump):
                if not(move_is_blocked_top):
                    self.rect.y += (self.gravitation_count ** 2) / 4
                    self.gravitation_count += 1
                elif keys[pygame.K_SPACE]:
                    self.is_jump = True
        # Физика прыжка
            else:
                if self.jump_count > 0:
                    self.rect.y -= (self.jump_count ** 2) / 4
                    self.jump_count -= 1
                else:
                    self.jump_count = 10
                    self.is_jump = False
                    self.gravitation_count = 0

                '''if move_is_blocked_top:
                    self.is_jump = False
                    self.jump_count = 10'''

                '''if self.jump_count >= -10:
                    if self.jump_count < 0 and not(move_is_blocked_top):
                        self.rect.y += (self.jump_count ** 2) / 4
                    else:
                        self.rect.y -= (self.jump_count ** 2) / 4
                    self.jump_count -= 1
                else:
                    self.is_jump = False
                    self.jump_count = 10
                    self.rect.y += 5'''



            # Отображение анимаций
            if self.animCount + 1 >= 30:
                self.animCount = 0

            if self.left:
                self.image = walkLeft[self.animCount // 5]
                self.rect.width = 48
                self.animCount += 1
            elif self.right:
                self.image = walkRight[self.animCount // 5]
                self.rect.width = 48
                self.animCount += 1
            else:
                self.image = player_img
                self.rect.width = 48

class Pizza(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pizza_img
        self.image.set_colorkey(WHITE)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = speed

    def update(self):
        if not paused:
            self.rect.y += self.speed
            '''if self.rect.y > 890:
                self.kill()
            if self.rect.right > player.rect.left and \
               self.rect.left < player.rect.right and \
               self.rect.bottom > player.rect.top and \
               self.rect.top < player.rect.bottom:
                self.kill()
                all_sprites.remove(self)
                score += 1'''

class Tile(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = speed
        self.name = 'tile'
        self.is_fall = False

    def update(self):
        if not paused:
            self.rect.y += self.speed

            '''for tile in tiles:
                if self.rect.right > tile.rect.left and \
                   self.rect.left < tile.rect.right and \
                   self.rect.bottom > tile.rect.top and \
                   self.rect.top < tile.rect.bottom:
                    self.speed = 0
                    if self.rect.bottom < tile.rect.bottom:
                        if tile.rect.x == 672:
                            self.image = tile_left_border
                            tile.image = tile_ground_left_border
                        elif tile.rect.x == 1200:
                            self.image = tile_right_border
                            tile.image = tile_ground_right_border
                        else:
                            tile.image = tile_ground
                    #self.image = tile
                    tiles.add(self) '''

class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x,self.y)

'''def spawn_sprites_in_game(spawn): #spawn_sprites = True or False
    if spawn:
        # Создание спрайтов пола
        for i in range (0,12):
            if i==0: tile_ = Tile(tile_left_border, GAME_BORDER_LEFT+i*48+48,948, 0)
            elif i==11: tile_ = Tile(tile_right_border, GAME_BORDER_LEFT+i*48+48,948, 0)
            else: tile_ = Tile(tile, GAME_BORDER_LEFT+i*48+48,948, 0)
            tile_.is_fall = True
            all_sprites.add(tile_)
            tiles.add(tile_)

        pizza_score = Object(pizza_img, 1300, 128)
        pizza_score.image.set_colorkey(WHITE)
        all_sprites.add(pizza_score)'''


'''def in_game_window(pizza_spawn_time, tile_spawn_time, paused):
    global TIME_TO_PIZZA
    global TIME_TO_TILES
    global lifes, score, falled_pizza

    all_sprites.add(player)

    TIME_IN_GAME = time.time()
    PIZZA_SPAWN_TIME = pizza_spawn_time
    TILE_SPAWN_TIME = tile_spawn_time
    if not paused:
        # Каждые TILE_SPAWN_TIME рандомно появляется плитка
        if (TIME_IN_GAME - TIME_TO_TILES) >= TILE_SPAWN_TIME:
            tile1 = Tile(tile, 648+48*random.randrange(1,13), 0, 3)
            all_sprites.add(tile1)
            TIME_TO_TILES = TIME_IN_GAME

        # Каждые PIZZA_SPAWN_TIME рандомно появляется пицца
        if (TIME_IN_GAME - TIME_TO_PIZZA) >= PIZZA_SPAWN_TIME:
            pizza1 = Pizza(648+48*random.randrange(1,13), 0, 5)
            all_sprites.add(pizza1)
            pizzas.add(pizza1)
            TIME_TO_PIZZA = TIME_IN_GAME

        # Если спрайт плитки падает на игрока
        for sprite in all_sprites:
            if hasattr(sprite, 'is_fall'):
                if not sprite.is_fall:
                    if sprite.rect.right > player.rect.left and \
                       sprite.rect.left < player.rect.right and \
                       sprite.rect.bottom > player.rect.top and \
                       sprite.rect.top < player.rect.bottom:
                        sprite.kill()
                        all_sprites.remove(sprite)
                        lifes -= 1

        # Если тайл упал на другой тайл
                for i in tiles:
                    if sprite.rect.right > i.rect.left and \
                       sprite.rect.left < i.rect.right and \
                       sprite.rect.bottom > i.rect.top and \
                       sprite.rect.top < i.rect.bottom:
                           sprite.speed = 0
                           sprite.is_fall = True
                           tiles.add(sprite)
                           if sprite.rect.bottom < i.rect.bottom:
                               if i.rect.x == 672:
                                   sprite.image = tile_left_border
                                   i.image = tile_ground_left_border
                               elif i.rect.x == 1200:
                                   sprite.image = tile_right_border
                                   i.image = tile_ground_right_border
                               else:
                                   i.image = tile_ground

        # Если пицца упала на плитку и если пицца упала на игрока
        for i in pizzas:
            if i.rect.y > 890:
                i.kill()
                all_sprites.remove(i)
                pizzas.remove(i)
                falled_pizza += 1
                if falled_pizza == 3:
                    lifes -= 1
                    falled_pizza = 0
            if i.rect.right > player.rect.left and \
               i.rect.left < player.rect.right and \
               i.rect.bottom > player.rect.top and \
               i.rect.top < player.rect.bottom:
                i.kill()
                all_sprites.remove(i)
                pizzas.remove(i)
                score += 1
                falled_pizza = 0

        move_is_blocked = False
        collided_tiles = pygame.sprite.spritecollide(player, tiles, False)
        for collided in collided_tiles:
            if collided.rect.top < player.rect.bottom:
                move_is_blocked = True

    # Отрисовка
    screen.blit(bg_in_game, (0, 0))
    scoretext = myfont.render(" X "+str(score), 1, BLACK)
    falled_pizza_in_row = myfont.render("Falled pizza in row: "+str(falled_pizza), 1, BLACK)
    screen.blit(scoretext, (1320, 105))
    screen.blit(falled_pizza_in_row, (1275, 190))
    screen.blit(pause, (530, 110))
    screen.blit(margin, (653, 0))
    screen.blit(margin, (1253, 0))
    if lifes == 3:
        screen.blit(heart_img, (1275, 160))
        screen.blit(heart_img, (1309, 160))
        screen.blit(heart_img, (1343, 160))
    elif lifes == 2:
        screen.blit(heart_img, (1275, 160))
        screen.blit(heart_img, (1309, 160))
    elif lifes == 1:
        screen.blit(heart_img, (1275, 160))'''

'''def in_menu_window():
    screen.blit(bg_in_menu,(0,0))
    screen.blit(logo, (460,0))
    screen.blit(play, (590, 640))
    screen.blit(rating, (850, 640))
    screen.blit(about, (1110, 640))
    screen.blit(close, (1600,115))
    screen.blit(music_on, (1600,250))
    screen.blit(music_off, (1600,385))
    help_lable = myfont.render("hold RMB to help", 1, WHITE)
    screen.blit(help_lable, (1400, 900))'''

# Создание игры и окна
pygame.init()
#pygame.mixer.init() # Звук
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("My Game")
myfont = pygame.font.SysFont("serif", 40)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
tiles = pygame.sprite.Group()
pizzas = pygame.sprite.Group()
player = Player()

# Игровой цикл
running = True
in_game = False
in_menu = True
spawn = True
about_flag = False
paused = False
you_lose = False
rating_table = False
in_game_once = False
send_req = False

score = 0
lifes = 3
falled_pizza = 0

PIZZA_SPAWN_TIME = 1.0
TILE_SPAWN_TIME = 2.0
pizza_speed = 5
tile_speed = 3
speedUp = 0

login = ''
password = ''
input_loginRect = pygame.Rect(925,350,140,48)
input_passwordRect = pygame.Rect(925,475,140,48)
login_inputActive = False
password_inputActive = False
entry = True
access = False
access_surface = myfont.render("Input login and password", 1, WHITE)

while running:
    # Задаём ФПС для цикла
    clock.tick(FPS)
    # Обновление
    all_sprites.update()

    if in_game:
        if spawn:
            spawn = False
            in_game_once = True
            # Создание спрайтов пола
            for i in range (0,12):
                if i==0: tile_ = Tile(tile_left_border, GAME_BORDER_LEFT+i*48+48,948, 0)
                elif i==11: tile_ = Tile(tile_right_border, GAME_BORDER_LEFT+i*48+48,948, 0)
                else: tile_ = Tile(tile, GAME_BORDER_LEFT+i*48+48,948, 0)
                tile_.is_fall = True
                all_sprites.add(tile_)
                tiles.add(tile_)

            pizza_score = Pizza(1300, 128, 0)
            all_sprites.add(pizza_score)

            all_sprites.add(player)

        TIME_IN_GAME = time.time()
        if not paused:
            # Каждые TILE_SPAWN_TIME рандомно появляется плитка
            if (TIME_IN_GAME - TIME_TO_TILES) >= TILE_SPAWN_TIME:
                tile1 = Tile(tile, 648+48*random.randrange(1,13), 0, tile_speed)
                all_sprites.add(tile1)
                TIME_TO_TILES = TIME_IN_GAME

            # Каждые PIZZA_SPAWN_TIME рандомно появляется пицца
            if (TIME_IN_GAME - TIME_TO_PIZZA) >= PIZZA_SPAWN_TIME:
                pizza1 = Pizza(648+48*random.randrange(1,13), 0, pizza_speed)
                all_sprites.add(pizza1)
                pizzas.add(pizza1)
                TIME_TO_PIZZA = TIME_IN_GAME

            # Если спрайт плитки падает на игрока
            for sprite in all_sprites:
                if hasattr(sprite, 'is_fall'):
                    if not sprite.is_fall:
                        if sprite.rect.right > player.rect.left and \
                           sprite.rect.left < player.rect.right and \
                           sprite.rect.bottom > player.rect.top and \
                           sprite.rect.top < player.rect.bottom:
                            sprite.kill()
                            all_sprites.remove(sprite)
                            sound_damage.play()
                            lifes -= 1

            # Если тайл упал на другой тайл
                    for i in tiles:
                        if sprite.rect.right > i.rect.left and \
                           sprite.rect.left < i.rect.right and \
                           sprite.rect.bottom > i.rect.top and \
                           sprite.rect.top < i.rect.bottom:
                               sprite.speed = 0
                               sprite.is_fall = True
                               tiles.add(sprite)
                               if sprite.rect.bottom < i.rect.bottom:
                                   if i.rect.x == 672:
                                       sprite.image = tile_left_border
                                       i.image = tile_ground_left_border
                                   elif i.rect.x == 1200:
                                       sprite.image = tile_right_border
                                       i.image = tile_ground_right_border
                                   else:
                                       i.image = tile_ground

            # Если пицца упала на плитку и если пицца упала на игрока
            for i in pizzas:
                for j in tiles:
                    if i.rect.right > j.rect.left and \
                       i.rect.left < j.rect.right and \
                       i.rect.bottom > j.rect.top and \
                       i.rect.top < j.rect.bottom:
                        i.kill()
                        all_sprites.remove(i)
                        pizzas.remove(i)
                        falled_pizza += 1
                        if falled_pizza == 3:
                            lifes -= 1
                            falled_pizza = 0
                if i.rect.right > player.rect.left and \
                   i.rect.left < player.rect.right and \
                   i.rect.bottom > player.rect.top and \
                   i.rect.top < player.rect.bottom:
                    i.kill()
                    sound_eating.play()
                    all_sprites.remove(i)
                    pizzas.remove(i)
                    score += 1
                    falled_pizza = 0

            move_is_blocked_left = False
            move_is_blocked_right = False
            move_is_blocked_top = False
            collided_tiles = pygame.sprite.spritecollide(player, tiles, False)
            for collided in collided_tiles:
                if collided.rect.right < player.rect.right:
                    if not(move_is_blocked_top):
                        move_is_blocked_left = True
                if collided.rect.left > player.rect.left:
                    if not(move_is_blocked_top):
                        move_is_blocked_right = True
            for i in tiles:
                if i.rect.top-2 < player.rect.bottom and \
                   i.rect.right > player.rect.left+10 and \
                   i.rect.left+10 < player.rect.right and \
                   i.rect.bottom > player.rect.top:
                    move_is_blocked_top = True
                    player.rect.bottom = i.rect.top - 1
                    player.gravitation_count = 2
            if score >= speedUp+10:
                pizza_speed += 0.3
                tile_speed += 0.2
                PIZZA_SPAWN_TIME -= 0.05
                TILE_SPAWN_TIME -= 0.05
                speedUp += 10

        # Отрисовка
        screen.blit(bg_in_game, (0, 0))
        scoretext = myfont.render(" X "+str(score), 1, BLACK)
        falled_pizza_in_row = myfont.render("Falled pizza in row: "+str(falled_pizza), 1, BLACK)
        screen.blit(scoretext, (1320, 105))
        screen.blit(falled_pizza_in_row, (1275, 190))
        screen.blit(pause, (530, 110))
        screen.blit(margin, (653, 0))
        screen.blit(margin, (1253, 0))
        if lifes == 3:
            screen.blit(heart_img, (1275, 160))
            screen.blit(heart_img, (1309, 160))
            screen.blit(heart_img, (1343, 160))
        elif lifes == 2:
            screen.blit(heart_img, (1275, 160))
            screen.blit(heart_img, (1309, 160))
        elif lifes == 1:
            screen.blit(heart_img, (1275, 160))

        if lifes == 0:
            paused = True
            you_lose = True

    if in_menu:
        screen.blit(bg_in_menu,(0,0))
        screen.blit(logo, (460,0))
        screen.blit(play, (590, 640))
        screen.blit(rating, (850, 640))
        screen.blit(about, (1110, 640))
        screen.blit(close, (1600,115))
        screen.blit(music_on, (1600,250))
        screen.blit(music_off, (1600,385))
        if access:
            access_true_surface = myfont.render('You have successfully signed in to your account!', 1, BLACK)
            if not(pygame.time.get_ticks() > tick + 2000):
                screen.blit(access_true_surface, (580, 520))

    for event in pygame.event.get():
        # Если окно закрывается
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if in_game:
                # Если нажать на кнопку паузы
                if event.button == 1 and (event.pos[0] >= 520 and event.pos[1] >= 115 and event.pos[0] <= 640 and event.pos[1] <= 235):
                    paused = True

            if rating_table:
                if event.button == 1:
                    if event.pos[0] >= 1150 and event.pos[1] >= 220 and event.pos[0] <= 1200 and event.pos[1] <= 270:
                        rating_table = False
            if about_flag:
                if event.button == 1:
                    if event.pos[0] >= 1270 and event.pos[1] >= 170 and event.pos[0] <= 1320 and event.pos[1] <= 220:
                        about_flag = False

            if in_menu:
                    # Если нажать на кнопку play
                    if event.button == 1:
                        if event.pos[0] >= 1600 and event.pos[1] >= 115 and event.pos[0] <= 1720 and event.pos[1] <= 235:
                            running = False
                        if event.pos[0] >= 1600 and event.pos[1] >= 250 and event.pos[0] <= 1720 and event.pos[1] <= 370:
                            sound_eating.set_volume(1.0)
                            sound_damage.set_volume(1.0)
                        if event.pos[0] >= 1600 and event.pos[1] >= 385 and event.pos[0] <= 1720 and event.pos[1] <= 505:
                            sound_eating.set_volume(0.0)
                            sound_damage.set_volume(0.0)
                        if not(entry) and not(rating_table) and not(about_flag):
                            if event.pos[0] >= 595 and event.pos[1] >= 645 and event.pos[0] <= 805 and event.pos[1] <= 855:
                                about_flag = False
                                screen.fill(0)
                                spawn = True
                                score = 0
                                lifes = 3
                                in_menu = False
                                in_game = True
                            if event.pos[0] >= 855 and event.pos[1] >= 645 and event.pos[0] <= 1065 and event.pos[1] <= 855:
                                rating_table = True
                                send_req = True
                            if event.pos[0] >= 1115 and event.pos[1] >= 645 and event.pos[0] <= 1325 and event.pos[1] <= 855:
                                about_flag = True
            if entry:
                if input_loginRect.collidepoint(event.pos):
                    login_inputActive = True
                else:
                    login_inputActive = False
                if input_passwordRect.collidepoint(event.pos):
                    password_inputActive = True
                else:
                    password_inputActive = False

                if event.pos[0] >= 620 and event.pos[1] >= 700 and event.pos[0] <= 928 and event.pos[1] <= 807:
                    entry_str = {'login': login, 'password': password}
                    res = requests.post("http://localhost:5000/entry", data=json.dumps(entry_str))

                    res.encoding = res.apparent_encoding

                    print(res.text)
                    if res.text == 'Logged in':
                        access = True
                        entry = False
                        tick = pygame.time.get_ticks()
                        print(tick)
                    else:
                        access = False
                        access_surface = myfont.render(str(res.text), 1, WHITE)

                if event.pos[0] >= 960 and event.pos[1] >= 700 and event.pos[0] <= 1268 and event.pos[1] <= 807:
                    registration_str = {'login': login, 'password': password}
                    res = requests.post("http://localhost:5000/registration", data=json.dumps(registration_str))

                    res.encoding = res.apparent_encoding

                    print(res.text)
                    access_surface = myfont.render(str(res.text), 1, WHITE)

            if paused:
                    if event.button == 1:
                        if paused and not(you_lose) and event.pos[0] >= 745 and event.pos[1] >= 380 and event.pos[0] <= 865 and event.pos[1] <= 500:
                            paused = False
                            if you_lose:
                                you_lose = False
                            in_game = False
                            all_sprites.empty()
                            tiles.empty()
                            pizzas.empty()
                            screen.fill(0)
                            in_menu = True
                            player.x = WIDTH/2
                            player.y = 888
                            player.jump_count = 10
                            player.is_jump = False
                            player.rect.center = (player.x, player.y)
                        if paused and not(you_lose) and event.pos[0] >= 885 and event.pos[1] >= 380 and event.pos[0] <= 1005 and event.pos[1] <= 500:
                            paused = False
                            if you_lose:
                                you_lose = False
                            spawn = True
                            score = 0
                            lifes = 3
                            falled_pizza = 0
                            all_sprites.empty()
                            tiles.empty()
                            pizzas.empty()
                            player.x = WIDTH/2
                            player.y = 888
                            player.jump_count = 10
                            player.is_jump = False
                            player.rect.center = (player.x, player.y)
                        if you_lose and event.pos[0] >= 795 and event.pos[1] >= 380 and event.pos[0] <= 915 and event.pos[1] <= 500:
                            paused = False
                            if you_lose:
                                you_lose = False
                            in_game = False
                            all_sprites.empty()
                            tiles.empty()
                            pizzas.empty()
                            screen.fill(0)
                            in_menu = True
                            player.x = WIDTH/2
                            player.y = 888
                            player.jump_count = 10
                            player.is_jump = False
                            player.rect.center = (player.x, player.y)
                        if you_lose and event.pos[0] >= 995 and event.pos[1] >= 380 and event.pos[0] <= 1105 and event.pos[1] <= 500:
                            paused = False
                            if you_lose:
                                you_lose = False
                            spawn = True
                            score = 0
                            lifes = 3
                            falled_pizza = 0
                            all_sprites.empty()
                            tiles.empty()
                            pizzas.empty()
                            player.x = WIDTH/2
                            player.y = 888
                            player.jump_count = 10
                            player.is_jump = False
                            player.rect.center = (player.x, player.y)
                        if paused:
                            if event.pos[0] >= 1025 and event.pos[1] >= 380 and event.pos[0] <= 1165 and event.pos[1] <= 500:
                                paused = False


        if event.type == pygame.KEYDOWN:
            if entry:
                if event.key == pygame.K_BACKSPACE:
                    if login_inputActive:
                        login = login[:-1]
                    if password_inputActive:
                        password = password[:-1]
                elif (event.key >= 48 and event.key <= 57) or (event.key >= 65 and event.key <= 90) or (event.key >= 97 and event.key <= 122):
                    if login_inputActive and len(login) < 10:
                        login += event.unicode
                    if password_inputActive and len(password) < 10:
                        password += event.unicode

    all_sprites.draw(screen)

    # Если зажата правая кнопка мыши в меню
    if about_flag:
        screen.blit(help, (550,150))
        screen.blit(close_btn, (1270, 170))

    if rating_table:
        screen.blit(bg_event_1, (700,200))
        screen.blit(rating_label, (740, 160))
        screen.blit(close_btn, (1150, 220))
        screen.blit(face, (780, 300))
        screen.blit(face, (780, 420))
        screen.blit(face, (780, 540))
        screen.blit(face, (780, 660))
        screen.blit(face, (780, 780))
        screen.blit(number_1, (740, 320))
        screen.blit(number_2, (735, 440))
        screen.blit(number_3, (735, 560))
        screen.blit(number_4, (735, 680))
        screen.blit(number_5, (735, 800))
        if send_req:
            login_str = {'login': login}
            res = requests.post("http://localhost:5000/rating", data=json.dumps(login_str))
            rating_list = json.loads(res.text)
        send_req = False
        for i in range(0,5):
            rating_login = myfont.render('Name: '+rating_list[i]['login'], 1, WHITE)
            screen.blit(rating_login, (900, 290+i*120))
            rating_bestScore = myfont.render('Best score: '+str(rating_list[i]['bestScore']), 1, WHITE)
            screen.blit(rating_bestScore, (900, 330+i*120))
            rating_games = myfont.render('Games: '+str(rating_list[i]['games']), 1, WHITE)
            screen.blit(rating_games, (900, 370+i*120))
        your_bestScore = myfont.render('Your best score: '+str(rating_list[5]['bestScore']), 1, WHITE)
        your_games = myfont.render('Your games: '+str(rating_list[5]['games']), 1, WHITE)
        your_place = myfont.render('Your place: '+str(rating_list[5]['place']), 1, WHITE)
        screen.blit(your_bestScore, (750, 920))
        screen.blit(your_games, (1100, 920))
        screen.blit(your_place, (500, 920))

    if entry:
        screen.blit(border, (550, 150))
        input_login = myfont.render('Enter your login', 1, WHITE)
        screen.blit(input_login,(630, 350))
        input_password = myfont.render('Enter your password', 1, WHITE)
        screen.blit(input_password, (590, 475))
        pygame.draw.rect(screen, BLACK, input_loginRect, 2)
        pygame.draw.rect(screen, BLACK, input_passwordRect, 2)
        login_surface = myfont.render(login, 1, WHITE)
        password_surface = myfont.render(password, 1, WHITE)
        screen.blit(login_surface,(input_loginRect.x+5, input_loginRect.y+5))
        screen.blit(password_surface,(input_passwordRect.x+5, input_passwordRect.y+5))
        input_loginRect.width = max(100,login_surface.get_width() + 10)
        input_passwordRect.width = max(100,password_surface.get_width() + 10)
        screen.blit(input_label_entry, (620, 700))
        screen.blit(input_label_reg, (960, 700))
        screen.blit(load, (580, 590))
        screen.blit(access_surface, (600, 595))

    if paused:
        if not(you_lose):
            screen.blit(bg_event,(710,190))
            screen.blit(pause_label,(750, 190))
            screen.blit(table, (775, 580))
            screen.blit(drink_a_cup_of_tea,(795, 650))
            screen.blit(menu, (745, 380))
            screen.blit(restart, (885, 380))
            screen.blit(play_2, (1025, 380))

    if you_lose:
        screen.blit(bg_event,(710,190))
        screen.blit(you_lose_label,(750, 190))
        screen.blit(menu, (795, 380))
        screen.blit(restart, (985, 380))
        screen.blit(table_2, (775, 530))
        scoretext_when_lose = myfont.render("Your score: "+str(score), 1, BLACK)
        screen.blit(scoretext_when_lose, (830, 552))
        if score >= 20 and score <= 49:
            screen.blit(stars_1, (775, 630))
        elif score >= 50 and scroe <= 99:
            screen.blit(stars_2, (775, 630))
        elif score >= 100:
            screen.blit(stars_3, (775, 630))
        else:
            screen.blit(stars_0, (775, 630))
        if in_game_once:
            game_str = {'bestScore': score, 'game': 0, 'login': login, 'password': password}
            print(game_str)
            requests.post("http://localhost:5000/games", data=json.dumps(game_str))
        in_game_once = False

    # После отрисовки переворачиваем экран
    pygame.display.flip()

pygame.quit()

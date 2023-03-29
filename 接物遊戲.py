import pygame as pg
import datetime as dt
import random as rd


def produce():
    x = rd.randint(0, width - python_icon.get_width())

    y_step = rd.randint(40, 120)

    global falling
    falling += [[python_icon, x, 0, y_step]]

def check_and_remove():
    remove = []

    bar_rect = bar.get_rect()
    bar_rect.left = bar_pos[0]
    bar_rect.top = bar_pos[1]

    for i in range(len(falling)):
        rect = falling[i][0].get_rect()
        rect.left = falling[i][1]
        rect.top = falling[i][2]

        if rect.colliderect(bar_rect):
            remove += [i]
            global score
            score += 1
            print('catch')
            sound_catch.play()

        elif rect.top > 600:
            remove += [i]
            print('disappear')
            sound_disappear.play()

    for i in remove[::-1]:
        falling.pop(i)

pg.mixer.pre_init(22050, -16, 2, 1000)
pg.init()
width, height = 1122, 627
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Pygame遊戲程式')

background = pg.image.load('C:\\Users\\ROUSER6\\PycharmProjects\\Game\\venv\\image\\one.jfif')
python_icon = pg.image.load('C:\\Users\\ROUSER6\\PycharmProjects\\Game\\venv\\image\\python_icon.png')
python_icon = pg.transform.scale(python_icon, (50, 50))
bar = pg.image.load('C:\\Users\\ROUSER6\\PycharmProjects\\Game\\venv\\image\\bar.png')
bar = pg.transform.scale(bar, (125, 35))
bar_speed = 400

pg.mixer.init()
sound_catch = pg.mixer.Sound('C:\\Users\\ROUSER6\\PycharmProjects\\Game\\venv\\sound\\catch.wav')
sound_disappear = pg.mixer.Sound('C:\\Users\\ROUSER6\\PycharmProjects\\Game\\venv\\sound\\disappear.wav')
sound_catch.set_volume(1.5)
sound_disappear.set_volume(0.15)
pg.mixer.music.load('C:\\Users\\ROUSER6\\PycharmProjects\\Game\\venv\\sound\\BGM.mp3')
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play(-1)

font = pg.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 28, bold=True, italic=False)

score = 0

time_start = dt.datetime.now()

falling = []

bar_pos = [int(((width - bar.get_width()) / 2)), 570]
key_left_right = [False, False]

last_screen_update = None
last_produce =None

while True:
    screen.blit(background, (0, 0))
    now = dt.datetime.now()

    if not last_screen_update:
        last_screen_update = now
        last_produce = now
        produce()

    else:
        time_diff = now - last_screen_update
        print(time_from_start.total_seconds())

        for i in range(len(falling)):
            falling[i][2] += falling[i][3] * time_diff.total_seconds()

        for item in falling:
            screen.blit(item[0], (item[1], item[2]))

        if (now - last_produce).total_seconds() >= 1.5:
            last_produce = now
            produce()

        if key_left_right[0]:
            if bar_pos[0] > 0:
                bar_pos[0] -= time_diff.total_seconds() * bar_speed
        elif key_left_right[1]:
            if bar_pos[0] < 997:
                bar_pos[0] += time_diff.total_seconds() * bar_speed

        screen.blit(bar, bar_pos)

        last_screen_update = now

    time_from_start = now - time_start
    text_time = font.render('遊戲時間: ' + str(time_from_start.seconds) + ' 秒', True, (0, 0, 255))
    screen.blit(text_time, (900, 10))
    text_score = font.render('得  分: ' + str(score), True, (0, 0, 255))
    screen.blit(text_score, (900, 50))

    pg.display.flip()

    check_and_remove()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                key_left_right[0] = True
            elif event.key == pg.K_RIGHT:
                key_left_right[1] = True

        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                key_left_right[0] = False
            elif event.key == pg.K_RIGHT:
                key_left_right[1] = False



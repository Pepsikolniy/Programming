from tkinter import *
from PIL import Image, ImageTk
import random

def starting_game():
    global all_lbl
    global used_tiles
    global help1, help2, help3
    help1 = random.randint(0,6)
    help2 = random.randint(0,6)
    help3 = random.randint(0,6)
    used_tiles=[0]*81
    all_lbl=[]
    lbl_num=0
    for row in range(9):
        for col in range(9):
            lbl = Label(root, image=img_tile, borderwidth=0)
            lbl.row=col
            lbl.col=row
            lbl.tile=lbl_num
            lbl.color=-1
            lbl.bind("<Button-1>", ball_active)
            lbl.place(x=(col*70) + 10,
                      y=(row*70) + 10)
            all_lbl.append(lbl)
            lbl_num+=1

def restarting_game(event):
    global clicked
    global all_lbl
    all_lbl.clear()
    starting_game()
    set_balls()
    clicked=False

def new_game(event):
    global clicked
    global all_lbl
    global lbl_looser
    lbl_looser.destroy()
    all_lbl.clear()
    starting_game()
    set_balls()
    clicked=False

def check_lines_horizontal():
    global all_lbl

clicked=False
def ball_active(event):
    global clicked
    global used_tiles
    global number_ball_to_move
    global img_tile
    global all_lbl
    global active_tile_num
    global ball_active_color
    global img_blue_active, img_aqua_active, img_green_active, img_pink_active, img_red_active, img_violet_active, img_yellow_active
    ball_active=[img_blue_active,img_aqua_active,img_green_active,img_pink_active,img_red_active,img_violet_active,img_yellow_active]
    global img_blue, img_aqua, img_green, img_pink, img_red, img_violet, img_yellow
    balls = [img_blue, img_aqua, img_green, img_pink, img_red, img_violet, img_yellow]
    if clicked==False:
        if event.widget.color != -1:
            event.widget.config(image=ball_active[event.widget.color])
            active_tile_num = event.widget.tile
            ball_active_color = event.widget.color
            clicked = True
    if clicked==True:
        if event.widget.color == -1:
            used_tiles[event.widget.tile] = 1
            used_tiles[active_tile_num] = 0
            event.widget.config(image=balls[ball_active_color])
            event.widget.color=ball_active_color
            all_lbl[active_tile_num].config(image=img_tile)
            all_lbl[active_tile_num].color = -1
            clicked=False
            set_balls()
        else:
            if event.widget.tile != active_tile_num:
                all_lbl[active_tile_num].config(image=balls[ball_active_color])
                event.widget.config(image=ball_active[event.widget.color])
                active_tile_num = event.widget.tile
                ball_active_color = event.widget.color
def next_move(event):
    set_balls()
    
def set_img_tile_active(event):
    event.widget.config(image=img_tile_active)
    global x_score
    x_score += 1
    update_score()
    
def update_score():
    global score, x_score
    score.config(text=x_score)
    
used_tiles=[0]*81
def set_balls():
    global used_tiles
    global all_lbl
    global help1, help2, help3
    global lbl_looser
    global img_blue, img_aqua, img_green, img_pink, img_red, img_violet, img_yellow
    balls = [img_blue, img_aqua, img_green, img_pink, img_red, img_violet, img_yellow]
    bool=True
    random_color1, random_color2, random_color3 = random.randint(0,6),random.randint(0,6),random.randint(0,6)
    while(bool):
        random_tile1 = random.randint(0,80)
        random_tile2 = random.randint(0,80)
        random_tile3 = random.randint(0,80)
        if (used_tiles[random_tile1]==0) and (used_tiles[random_tile2]==0) and (used_tiles[random_tile3]==0) and (random_tile1!=random_tile2) and (random_tile1!=random_tile3) and (random_tile2!=random_tile3):
            bool=False
    x1 = all_lbl[random_tile1].row
    y1 = all_lbl[random_tile1].col
    x2 = all_lbl[random_tile2].row
    y2 = all_lbl[random_tile2].col
    x3 = all_lbl[random_tile3].row
    y3 = all_lbl[random_tile3].col
    all_lbl[random_tile1] = Label(root, image=balls[help1], borderwidth=0)
    all_lbl[random_tile1].color = help1
    all_lbl[random_tile1].row = x1
    all_lbl[random_tile1].col = y1
    all_lbl[random_tile1].tile = random_tile1
    all_lbl[random_tile1].bind("<Button-1>", ball_active)
    all_lbl[random_tile1].place(x=all_lbl[random_tile1].row*70 + 10,y=all_lbl[random_tile1].col*70 + 10)
    all_lbl[random_tile2] = Label(root, image=balls[help2], borderwidth=0)
    all_lbl[random_tile2].color = help2
    all_lbl[random_tile2].row = x2
    all_lbl[random_tile2].col = y2
    all_lbl[random_tile2].tile = random_tile2
    all_lbl[random_tile2].bind("<Button-1>", ball_active)
    all_lbl[random_tile2].place(x=all_lbl[random_tile2].row*70 + 10,y=all_lbl[random_tile2].col*70 + 10)
    all_lbl[random_tile3] = Label(root, image=balls[help3], borderwidth=0)
    all_lbl[random_tile3].color = help3
    all_lbl[random_tile3].row = x3
    all_lbl[random_tile3].col = y3
    all_lbl[random_tile3].tile = random_tile3
    all_lbl[random_tile3].bind("<Button-1>", ball_active)
    all_lbl[random_tile3].place(x=all_lbl[random_tile3].row*70 + 10,y=all_lbl[random_tile3].col*70 + 10)
    used_tiles[random_tile1]=1
    used_tiles[random_tile2]=1
    used_tiles[random_tile3]=1
    print( random_tile1,all_lbl[random_tile1].row, all_lbl[random_tile1].col)
    help1,help2,help3=random.randint(0,6),random.randint(0,6),random.randint(0,6)
    help1_lbl=Label(root,image=balls[help1], borderwidth=0)
    help1_lbl.place(x=650, y=290)
    help2_lbl=Label(root,image=balls[help2], borderwidth=0)
    help2_lbl.place(x=730, y=290)
    help3_lbl=Label(root,image=balls[help3], borderwidth=0)
    help3_lbl.place(x=810, y=290)
    sum=0
    for i in range(81):
        sum+=used_tiles[i]
        if sum >= 80:
            lbl_looser=Label(root, text="4el, ti...", font=("Arial", 26), bg="#414141", fg="white")
            lbl_looser.bind("<Button-1>", new_game)
            lbl_looser.place(x=650,y=600)
    #while(bool):
    #    random_x1, random_y1 = random.randint(0,8), random.randint(0,8)
    #    random_x2, random_y2 = random.randint(0,8), random.randint(0,8)
    #    random_x3, random_y3 = random.randint(0,8), random.randint(0,8)
    #    if (used_tiles[random_x1*random_y1]==0) and (used_tiles[random_x2*random_y2]==0) and (used_tiles[random_x3*random_y3]==0) and (random_x1*random_y1!=random_x2*random_y2) and (random_x1*random_y1!=random_x3*random_y3) and (random_x2*random_y2!=random_x3*random_y3):
    #        bool=False
    #all_lbl[random_x1*random_y1] = Label(root, image=balls[random_color1], borderwidth=0)
    #all_lbl[random_x1*random_y1].color = random_color1
    #all_lbl[random_x1*random_y1].row = random_x1
    #all_lbl[random_x1*random_y1].col = random_y1
    #all_lbl[random_x1*random_y1].bind("<Button-1>", ball_active)
    #all_lbl[random_x1*random_y1].place(x=random_x1*70 + 10,y=random_y1*70 + 10)
    #all_lbl[random_x2*random_y2] = Label(root, image=balls[random_color2], borderwidth=0)
    #all_lbl[random_x2*random_y2].color = random_color2
    #all_lbl[random_x2*random_y2].row = random_x2
    #all_lbl[random_x2*random_y2].col = random_y2
    #all_lbl[random_x2*random_y2].bind("<Button-1>", ball_active)
    #all_lbl[random_x2*random_y2].place(x=random_x2*70 + 10,y=random_y2*70 + 10)
    #all_lbl[random_x3*random_y3] = Label(root, image=balls[random_color3], borderwidth=0)
    #all_lbl[random_x3*random_y3].color = random_color3
    #all_lbl[random_x3*random_y3].row = random_x3
    #all_lbl[random_x3*random_y3].col = random_y3
    #all_lbl[random_x3*random_y3].bind("<Button-1>", ball_active)
    #all_lbl[random_x3*random_y3].place(x=random_x3*70 + 10,y=random_y3*70 + 10)
    #used_tiles[random_x1*random_y1]=1
    #used_tiles[random_x2*random_y2]=1
    #used_tiles[random_x3*random_y3]=1

root = Tk()
root.configure(bg="#414141")
root.geometry("900x646")

tileset = Image.open("cell-bgr.png")
img_tile = ImageTk.PhotoImage(tileset.crop((1, 0, 67, 66)))
img_tile_active = ImageTk.PhotoImage(tileset.crop((1, 69, 67, 135)))

lbl_name=Label(root, text="Бачаны 2", font=("Arial", 26), bg="#414141", fg="white")
lbl_name.place(x=650, y=25)
lbl_score=Label(root, text="Счёт: ", font=("Arial", 26), bg="#414141", fg="white")
lbl_score.place(x=650, y=90)
lbl_help=Label(root, text="Подсказка: ", font=("Arial", 16), bg="#414141", fg="white")
lbl_help.place(x=650, y=250)

x_score=0
score=Label(root, text=x_score, font=("Arial", 26), bg="#414141", fg="white")
score.place(x=750, y=90)

bgr_blue = Image.open("cell-bgr.png").convert('RGBA')
ball_blue = Image.open("ball-blue.png").convert('RGBA')
bgr_blue.paste(ball_blue,(6,5),ball_blue)
img_blue = ImageTk.PhotoImage(bgr_blue.crop((1, 0, 67, 66)))

bgr_aqua = Image.open("cell-bgr.png").convert('RGBA')
ball_aqua = Image.open("ball-aqua.png").convert('RGBA')
bgr_aqua.paste(ball_aqua,(6,5),ball_aqua)
img_aqua = ImageTk.PhotoImage(bgr_aqua.crop((1, 0, 67, 66)))

bgr_green = Image.open("cell-bgr.png").convert('RGBA')
ball_green = Image.open("ball-green.png").convert('RGBA')
bgr_green.paste(ball_green,(6,5),ball_green)
img_green = ImageTk.PhotoImage(bgr_green.crop((1, 0, 67, 66)))

bgr_pink = Image.open("cell-bgr.png").convert('RGBA')
ball_pink = Image.open("ball-pink.png").convert('RGBA')
bgr_pink.paste(ball_pink,(6,5),ball_pink)
img_pink = ImageTk.PhotoImage(bgr_pink.crop((1, 0, 67, 66)))

bgr_red = Image.open("cell-bgr.png").convert('RGBA')    
ball_red = Image.open("ball-red.png").convert('RGBA')
bgr_red.paste(ball_red,(6,5),ball_red)
img_red = ImageTk.PhotoImage(bgr_red.crop((1, 0, 67, 66)))

bgr_violet = Image.open("cell-bgr.png").convert('RGBA')
ball_violet = Image.open("ball-violet.png").convert('RGBA')
bgr_violet.paste(ball_violet,(6,5),ball_violet)
img_violet = ImageTk.PhotoImage(bgr_violet.crop((1, 0, 67, 66)))

bgr_yellow = Image.open("cell-bgr.png").convert('RGBA')
ball_yellow = Image.open("ball-yellow.png").convert('RGBA')
bgr_yellow.paste(ball_yellow,(6,5),ball_yellow)
img_yellow = ImageTk.PhotoImage(bgr_yellow.crop((1, 0, 67, 66)))

bgr_blue_active = Image.open("cell-bgr.png").convert('RGBA')
ball_blue_active = Image.open("ball-blue.png").convert('RGBA')
bgr_blue_active.paste(ball_blue_active,(6,74),ball_blue_active)
img_blue_active = ImageTk.PhotoImage(bgr_blue_active.crop((1, 69, 67, 135)))

bgr_aqua_active = Image.open("cell-bgr.png").convert('RGBA')
ball_aqua_active = Image.open("ball-aqua.png").convert('RGBA')
bgr_aqua_active.paste(ball_aqua_active,(6,74),ball_aqua_active)
img_aqua_active = ImageTk.PhotoImage(bgr_aqua_active.crop((1, 69, 67, 135)))

bgr_green_active = Image.open("cell-bgr.png").convert('RGBA')
ball_green_active = Image.open("ball-green.png").convert('RGBA')
bgr_green_active.paste(ball_green_active,(6,74),ball_green_active)
img_green_active = ImageTk.PhotoImage(bgr_green_active.crop((1, 69, 67, 135)))

bgr_pink_active = Image.open("cell-bgr.png").convert('RGBA')
ball_pink_active = Image.open("ball-pink.png").convert('RGBA')
bgr_pink_active.paste(ball_pink_active,(6,74),ball_pink_active)
img_pink_active = ImageTk.PhotoImage(bgr_pink_active.crop((1, 69, 67, 135)))

bgr_red_active = Image.open("cell-bgr.png").convert('RGBA')    
ball_red_active = Image.open("ball-red.png").convert('RGBA')
bgr_red_active.paste(ball_red_active,(6,74),ball_red_active)
img_red_active = ImageTk.PhotoImage(bgr_red_active.crop((1, 69, 67, 135)))

bgr_violet_active = Image.open("cell-bgr.png").convert('RGBA')
ball_violet_active = Image.open("ball-violet.png").convert('RGBA')
bgr_violet_active.paste(ball_violet_active,(6,74),ball_violet_active)
img_violet_active = ImageTk.PhotoImage(bgr_violet_active.crop((1, 69, 67, 135)))

bgr_yellow_active = Image.open("cell-bgr.png").convert('RGBA')
ball_yellow_active = Image.open("ball-yellow.png").convert('RGBA')
bgr_yellow_active.paste(ball_yellow_active,(6,74),ball_yellow_active)
img_yellow_active = ImageTk.PhotoImage(bgr_yellow_active.crop((1, 69, 67, 135)))

lbl_new_game = Label(root,text="Новая игра", font=("Arial", 26), bg="#414141", fg="white")
lbl_new_game.bind("<Button-1>", restarting_game)
lbl_new_game.place(x=650, y=370)

lbl_next_move=Label(root,text="Сделать ход", font=("Arial", 24), bg="#414141", fg="white")
lbl_next_move.bind("<Button-1>", next_move)
lbl_next_move.place(x=650, y=440)

starting_game()
set_balls()
root.mainloop()

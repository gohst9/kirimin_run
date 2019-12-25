#このプログラムを動かすにはpyxelをインストールする必要があります。
import pyxel
import math

WIDTH  = 160
HEIGHT = 120

#class Enemy:
#    def __init__(self):
#        self.pos = [0,0]
#        self.size = [10,10]
#    def update()

class Bullet:
    def __init__(self,x,y,dx=1,dy=0):
        #弾の初期配置
        self.x = x
        self.y = y
        #弾の移動する距離
        self.dx = dx
        self.dy = dy
    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        #画面端で反転する
        if self.x < 0 or self.x > WIDTH:
            self.dx = -self.dx
        if self.y < 0 or self.y > HEIGHT:
            self.dy = -self.dy
    def draw(self):
        pyxel.pix(round(self.x),round(self.y),10)


class App:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT,caption="Kirimin Run!")
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")
        self.kirimin_x,self.kirimin_y = 0,0 #きりみんちゃんの位置
        self.kirimin_move = False #きりみんちゃんが動いているか否か　アニメーションに影響
        self.is_ac = False
        self.bullet_lst = []

        #キーの初期化
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.space = False
        self.left_mouse = False


        pyxel.run(self.update,self.draw)


    def update(self):
        #きりみんちゃんの移動状態
        self.down  = pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S)
        self.up    = pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W)
        self.right = pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)
        self.left  = pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A)
        #スペースを押してしているかどうかの判定
        self.space = pyxel.btn(pyxel.KEY_SPACE)
        self.left_mouse = pyxel.btn(pyxel.MOUSE_LEFT_BUTTON)

        if self.down:
            self.kirimin_y += 1
            self.kirimin_move = True
        if self.up:
            self.kirimin_y -= 1
            self.kirimin_move = True
        if self.right:
            self.kirimin_x += 1
            self.kirimin_move = True
        if self.left:
            self.kirimin_x -= 1
            self.kirimin_move = True
        if self.left_mouse:
            self.shoot()
        if self.space:
            self.is_ac = True
        else:
            self.is_ac = False
        if not (self.up or self.down or self.left or self.right):
            self.kirimin_move = False

        for b in self.bullet_lst:
            b.update()



    def draw(self):
        pyxel.cls(0)

        img = 0
        x = self.kirimin_x
        y = self.kirimin_y
        frame = 0 if self.kirimin_move == False else pyxel.frame_count % 3 * 16
        pyxel.blt(x,y,img,frame,0,16,16,0)
        if self.is_ac:
            self.ac()
        for b in self.bullet_lst:
            b.draw()

    def ac(self):
        x = self.kirimin_x + 15
        y = self.kirimin_y + 5
        pyxel.text(x,y,"AC!",11)

    def shoot(self):
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        dx = x - self.kirimin_x
        dy = y - self.kirimin_y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        dx = dx / dist
        dy = dy / dist
        self.bullet_lst.append(Bullet(self.kirimin_x,self.kirimin_y,dx,dy))

App()


import pyxel
import sympy

WIDTH  = 160
HEIGHT = 120




class App:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT,caption="Kirimin Run!")
        pyxel.load("my_resource.pyxres")
        self.kirimin_x,self.kirimin_y = 0,0 #きりみんちゃんの位置
        self.kirimin_move = False #きりみんちゃんが動いているか否か　アニメーションに影響
        self.is_ac = False
        pyxel.run(self.update,self.draw)
    def update(self):
        #きりみんちゃんの位置
        down  = pyxel.btn(pyxel.KEY_DOWN)
        up    = pyxel.btn(pyxel.KEY_UP)
        right = pyxel.btn(pyxel.KEY_RIGHT)
        left  = pyxel.btn(pyxel.KEY_LEFT)
        space = pyxel.btn(pyxel.KEY_SPACE)

        if down:
            self.kirimin_y += 1
            self.kirimin_move = True
        if up:
            self.kirimin_y -= 1
            self.kirimin_move = True
        if right:
            self.kirimin_x += 1
            self.kirimin_move = True
        if left:
            self.kirimin_x -= 1
            self.kirimin_move = True
        if space:
            self.is_ac = True
        else:
            self.is_ac = False
        if not (up or down or left or right):
            self.kirimin_move = False



    def draw(self):
        pyxel.cls(0)

        img = 0
        x = self.kirimin_x
        y = self.kirimin_y
        frame = 0 if self.kirimin_move == False else pyxel.frame_count % 3 * 16
        pyxel.blt(x,y,img,frame,0,16,16,0)
        if self.is_ac:
            self.ac()

    def ac(self):
        x = self.kirimin_x + 15
        y = self.kirimin_y + 5
        pyxel.text(x,y,"AC!",11)

App()


import pyxel
from collections import deque
class App:
    def __init__(self,lst,start = (0,0)):
        self.start = start
        self.kirimin_x,self.kirimin_y = self.start
        self.kirimin_move = False
        self.is_ac = False
        self.lst = lst
        self.visited = [[False for _ in range(len(lst[0]))] for _ in range(len(lst))]
        self.room_width = 16
        self.room_height = 16
        self.width = len(lst[0])
        self.height = len(lst)
        self.visited = [[False for _ in range(len(lst[0]))] for _ in range(len(lst))]
        self.q = deque()
        pyxel.init(min(255,self.room_width * self.width),min(255,(self.room_height * self.height)))
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update,self.draw)
    def update(self):
        #きりみんちゃんの移動状態
        self.down  = pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S)
        self.up    = pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W)
        self.right = pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)
        self.left  = pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A)
        #スペースを押してしているかどうかの判定
        self.space = pyxel.btn(pyxel.KEY_SPACE)
        now_x = (self.kirimin_x + 8) // self.room_width
        now_y = (self.kirimin_y + 8) // self.room_height
        if not self.visited[now_y][now_x]:
            self.visited[now_y][now_x] = True
            self.q.append((now_y,now_x))

        if pyxel.btnp(pyxel.KEY_R):
            self.visited = [[False for _ in range(len(self.lst[0]))] for _ in range(len(self.lst))]
            self.kirimin_x,self.kirimin_y = self.start
            self.q = deque()





        if self.down:
            nxt = (self.kirimin_y+15+1) // self.room_height
            now_x = (self.kirimin_x + 8) // self.room_width
            #移動先が壁のときは何もしない
            if nxt >= self.height or self.lst[nxt][now_x] == 1:
                pass
            else:
                self.kirimin_y += 1
                self.kirimin_move = True
        if self.up:
            nxt = (self.kirimin_y - 1) // self.room_height
            now_x = (self.kirimin_x + 8) // self.room_width
            if nxt < 0 or self.lst[nxt][now_x] == 1:
                pass
            else:
                self.kirimin_y -= 1
                self.kirimin_move = True
        if self.right:
            nxt = (self.kirimin_x + 15 + 1) // self.room_width
            now_y = (self.kirimin_y + 8) // self.room_height
            if nxt >= self.width or self.lst[now_y][nxt] == 1:
                pass
            else:
                self.kirimin_x += 1
                self.kirimin_move = True
        if self.left:
            nxt = (self.kirimin_x - 1) // self.room_width
            now_y = (self.kirimin_y + 8) // self.room_height
            if nxt < 0 or self.lst[now_y][nxt] == 1:
                pass
            else:
                self.kirimin_x -= 1
                self.kirimin_move = True
        if self.space:
            self.is_ac = True
            #print("x:",(self.kirimin_x+8)//self.room_width,"y:",(self.kirimin_y+8)//self.room_height)
        else:
            self.is_ac = False
        if not (self.up or self.down or self.left or self.right):
            self.kirimin_move = False
        if pyxel.btnp(pyxel.KEY_Z):
            while self.q:
                y,x = self.q.pop()
                dxs = [1,0,-1,0]
                dys = [0,1,0,-1]
                flag = False
                for i in range(4):
                    nxt_x = dxs[i] + x
                    nxt_y = dys[i] + y
                    if nxt_x < 0 or nxt_x >= self.width or nxt_y <0 or nxt_y >= self.height:
                        continue
                    if self.lst[nxt_y][nxt_x] == 1:
                        continue
                    if self.visited[nxt_y][nxt_x]:
                        continue
                    flag = True
                    break


                if flag:
                    self.kirimin_x = x * self.room_width
                    self.kirimin_y = y * self.room_height
                    break

        if pyxel.btnp(pyxel.KEY_X):
            while self.q:
                y,x = self.q.popleft()
                dxs = [1,0,-1,0]
                dys = [0,1,0,-1]
                flag = False
                for i in range(4):
                    nxt_x = dxs[i] + x
                    nxt_y = dys[i] + y
                    if nxt_x < 0 or nxt_x >= self.width or nxt_y <0 or nxt_y >= self.height:
                        continue
                    if self.lst[nxt_y][nxt_x] == 1:
                        continue
                    if self.visited[nxt_y][nxt_x]:
                        continue
                    flag = True
                    break


                if flag:
                    self.kirimin_x = x * self.room_width
                    self.kirimin_y = y * self.room_height
                    break


    def draw(self):
        pyxel.cls(0)
        for y in range(self.height):
            for x in range(self.width):
                color = self.lst[y][x]
                if self.visited[y][x]:
                    color = 9
                pyxel.rect(x * self.room_width,y * self.room_height,self.room_width,self.room_height,color)
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
def main():
    lst = [[0,0,0,0,0,0,1,1,1],
           [0,0,0,1,0,0,1,1,1],
           [0,0,0,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1]]
    App(lst)

if __name__ == '__main__':
    main()

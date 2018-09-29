from maintable import *
from conveyor import *
from PIL import Image, ImageTk
from tkinter.messagebox import *

class App(Frame):
    def __init__(self, master, num):
        super(App, self).__init__()
        self.master = master
        self.num = num
        self.load_images()

        self.frame01 = Frame(self.master)
        self.frame01.pack()
        self.frame02 = Frame(self.master)
        self.frame02.pack()
        self.frame03 = Frame(self.master)
        self.frame03.pack()

        canvas = Canvas(self.frame01, width=700, height=10)
        canvas.pack()

        # TODO
        self.conveyor = Conveyor(self, self.resized_images, self.num)
        self.conveyor.pack()

        # TODO
        self.table = Maintable(self, self.figure_images, self.alphabet_images, self.num)
        # self.table.grid(row=0, column=0, pady=(10, 20))
        self.table.pack()
        
    def load_images(self):
        self.figure_images = list(Image.open("picture\\%d.JPG" % (i + 1)) for i in range(self.num * self.num))
        self.alphabet_images = list(PhotoImage(file="alphabet\\%d.GIF" % (i + 1)) for i in range(self.num * self.num))
        self.resized_images = list(ImageTk.PhotoImage(self.figure_images[i].resize((50, 50), Image.ANTIALIAS)) for i in range(self.num * self.num)) # conveyor쪽의 이미지
        self.figure_images = list(ImageTk.PhotoImage(self.figure_images[i]) for i in range(self.num * self.num))

    # TODO
    # MainTable에서 선택한 도형 이미지와 Conveyor에서 Marker가 현재 가리키는 이미지를 비교한 후 비교 결과에 따라 처리한다.
    def compare_images(self):
        if self.table.selected_image != self.conveyor.images[self.conveyor.cur_idx]:
            self.conveyor.wrong_match_config()
        else:
            self.conveyor.correct_match_config()
    
    # TODO
    # 종료 조건 만족 시 실행
    def finish(self, win):
        if win == True:
            showinfo("게임 종료", "성공하였습니다")
        else:
            showinfo("게임 종료", "실패하였습니다")

        self.conveyor.quit()
        self.table.quit()
        self.quit()

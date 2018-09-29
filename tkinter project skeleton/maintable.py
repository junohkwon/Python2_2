from imagebtn import *
from tkinter import *
from random import *
import time

class Maintable(Frame):
    # Maintable(self, self.resized_images, self.alphabet_images, self.num)
    def __init__(self, master, images, alphabet, width):
        super(Maintable, self).__init__()
        self.master = master
        self.width = width
        self.num = width * width
        self.images = images
        self.alphabet = alphabet
        self.selected_image = None
        self.shuffle()

        # TODO
        # 16개의 ImageButton 객체 생성 및 이벤트 핸들러 바인딩
        index = 0
        for i in range(0, self.width):
            for j in range(0, self.width):
                # 조심! 제출시에는 반드시 해당구문으로 제출할것
                # b = ImageButton(self.master, image=self.alphabet[index], hidden_image=self.images[self.imagelist[index]],
                #                 relief=SOLID, overrelief=RIDGE, borderwidth=1)
                b = ImageButton(self.master.frame02, image=self.alphabet[index], hidden_image=self.images[index],
                                relief=SOLID, overrelief=RIDGE, borderwidth=1)
                b.grid(column=j, row=i)
                index += 1
                b.bind("<Button-1>", self.show_hidden_image)
                b.bind("<ButtonRelease-1>", self.hide_image)

    # TODO
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.num), self.num)
        # print(self.imagelist)

    # TODO
    # 마우스 눌렀을 때 이벤트 처리.
    # 알파벳 이미지를 도형 이미지로 교체
    # event.widget.config 사용
    def show_hidden_image(self, event):
        event.widget.config(image=event.widget.hidden_image)

    # TODO
    # 마우스 release 이벤트 처리
    # 도형 이미지를 원래 알파벳 이미지로 교체
    def hide_image(self, event):
        self.selected_image = self.images.index(event.widget.hidden_image)
        event.widget.config(image=event.widget.alphabet)
        self.master.compare_images()


from tkinter import *
from random import *

class Conveyor(Frame):
    # self.conveyor = Conveyor(self.frame03, self.resized_images, self.num)
    def __init__(self, master, images, width):
        super(Conveyor, self).__init__()
        self.imagelist = []

        self.master = master
        self.width = width
        self.num = width * (width - 1) + 1
        self.images = images
        self.labels = []
        self.shuffle()

        # TODO
        # Label widget 생성
        for i in range(0, self.num):
            la = Label(self.master.frame03, image=self.images[i], borderwidth=1, relief=SOLID)
            # 조심! 제출시에는 반드시 해당구문으로 제출할것
            # la = Label(self.master, image=self.images[self.imagelist[i]], borderwidth=1, relief=SOLID)
            la.grid(column=i, row=1)
            self.labels.append(la)

        self.init_canvas()

    # TODO
    # Marker와 FINAL 글씨를 그리는 부분. tkinter canvas 사용
    def init_canvas(self):
        # Final 글씨 그리는 부분
        self.finalLabel = Label(self.master.frame03, text='FINAL', fg='red')
        self.finalLabel.grid(column=12, row=0)
        # Marker 생성 : 현재 index 설정 = 시작 위치 설정
        self.cur_idx = 9
        self.conveyor_canvas = Canvas(self.master.frame03, height=30, width=50)
        self.conveyor_canvas.grid(column=self.cur_idx, row=0)
        self.pointer = self.conveyor_canvas.create_polygon(10, 2, 40, 2, 25, 30, fill='yellow', outline='black', width=2)

    # TODO
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.width * self.width), self.num)

    # TODO
    # 현재 이미지와 일치하는 이미지를 선택했을 경우
    def correct_match_config(self):
        pass
        # FINAL 일 떄
        if self.cur_idx == self.num - 1:
            self.master.finish(True)
        # FINAL 바로 전 일 떄
        elif self.cur_idx == self.num - 2:
            self.conveyor_canvas.delete(self.pointer)
            self.cur_idx += 1
        # 그 외 일반적인 상황
        else:
            self.conveyor_canvas.grid(row=0, column=self.cur_idx + 1)
            self.cur_idx += 1

    # TODO
    # 현재 이미지와 일치하는 이미지를 선택하지 못했을 경우
    def wrong_match_config(self):
        pass
        # 마지막일 때
        if (self.cur_idx == 0):
            self.master.finish(False)
        # FINAL일 때
        elif self.cur_idx == self.num - 1:
            self.cur_idx -= 1
            self.pointer = self.conveyor_canvas.create_polygon(10, 2, 40, 2, 25, 30, fill='yellow', outline='black', width=2)
            self.finalLabel.destroy()
            self.finalLabel = Label(self, text='final', fg='red')
            self.finalLabel.grid(row=0, column=12)

            self.lshift_images(self.get_new_image())
        # 그 외 일반적인 상황
        else:
            self.conveyor_canvas.grid(row=0, column=self.cur_idx - 1)
            self.cur_idx -= 1

            self.lshift_images(self.get_new_image())

    # TODO
    # 오답 시 새로운 이미지를 추가하는 함수
    def get_new_image(self):
        while True:
            new_image = randint(0, self.width * self.width - 1)
            if new_image not in self.imagelist:
                break  # 랜덤 사진 뽑기해서 기존 사진에 없으면 새 이미지로 채택
        return new_image

    # TODO
    # 오답시 왼쪽으로 1칸씩 이동하고 새 이미지를 추가하는 함수
    def lshift_images(self, new_image):
        for i in range(0, self.num - 1):
            self.labels[i].config(image=self.images[self.imagelist[i + 1]])
            # 모든 레이블에 대해 그 뒤 레이블로 바꿔치기 한다.
            self.imagelist[i] = self.imagelist[i + 1]
            # 그림 숫자 리스트도 바꿔치기 한다
            # 새 이미지 추가
        self.imagelist[self.num - 1] = new_image  # 새이미지 리스트 끝에 새 번호를 넣는다
        self.labels[self.num - 1].config(image=self.images[self.imagelist[self.num - 1]])


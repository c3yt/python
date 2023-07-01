from tkinter import *
from random import *

# 승패 표시 함수
def game(com, user) :
    # 가위
    if user == 0 :
        if com == 0 : lbl_res['text'] = "Draw"                # 가위
        elif com == 1 : lbl_res['text'] = "Computer wins!"    # 바위
        else : lbl_res['text'] = "User wins!"                   # 보
    # 바위
    elif user == 1 :
        if com == 0 : lbl_res['text'] = "User wins!"           # 가위
        elif com == 1 : lbl_res['text'] = "Draw"              # 바위
        else : lbl_res['text'] = "Computer wins!"              # 보
    # 보
    else :
        if com == 0 : lbl_res['text'] = "Computer wins!"      # 가위
        elif com == 1 : lbl_res['text'] = "User wins!"         # 바위
        else : lbl_res['text'] = "Draw"                        # 보


        
# 컴퓨터, 사용자 손 모양 이미지 변경 함수
def change_img(user) :
    # 이미지 리스트
    List = ["scissors.png", "rock.png", "paper.png"]

    # 컴퓨터가 낼 손 결정
    com = randint(0, 2)
    
    # 컴퓨터, 사용자 이미지 경로 설정
    com_img = PhotoImage(file = List[com])
    user_img = PhotoImage(file = List[user])
   
    # 컴퓨터, 사용자 이미지 변경
    lbl_com['image'] = com_img
    lbl_com.image = com_img
    lbl_user['image'] = user_img
    lbl_user.image = user_img
    
    # 승패 결정 함수 호출 – game() 함수 정의 후 호출    
    game(com, user)


# 윈도 창 생성
win = Tk()
# 윈도 제목 설정
win.title("Rock Paper Scissors Game")


"""위젯 생성하기"""
# ‘Ready’ 이미지 경로 설정
basic_img = PhotoImage( file = "ready.png" )


# 컴퓨터, 사용자 손 표시할 레이블 - ‘Read’ 이미지로 생성
lbl_com = Label( win, image = basic_img, relief = "solid" )
lbl_user = Label( win, image = basic_img, relief = "solid")


# 승패 결과 문자열 표시 레이블 - 공백으로 생성
lbl_res = Label( win, text = '', width = 15, font = ("consolas", 20, "bold"), fg = "brown", bg = "lightyellow" )


# ‘Computer’, ‘User’ 문자열 표시할 레이블 각각 생성
lbl_name1 = Label( win, text = "Computer", font = ("consolas", 20) )
lbl_name2 = Label( win, text = "User", font = ("consolas", 20) )


# 가위, 바위, 보 버튼 각각 생성 (command 속성은 step2, 3 후에 추가)
btn_scissor = Button( win, text = "scissors", width = 15, font = ("consolas", 15), bg = "skyblue", command = lambda : change_img(0) )
btn_rock = Button( win, text = "rock", width = 15, font = ("consolas", 15), bg = "pink", command = lambda : change_img(1) ) 
btn_paper = Button( win, text = "paper", width = 15, font = ("consolas", 15), bg = "light green", command = lambda : change_img(2) )


"""위젯 배치하기"""
lbl_com.grid(row = 0, column = 0)
lbl_res.grid(row = 0, column = 1)
lbl_user.grid(row = 0, column = 2)
lbl_name1.grid(row = 1, column = 0)
lbl_name2.grid(row = 1, column = 2)
btn_scissor.grid(row = 2, column = 0)
btn_rock.grid(row = 2, column = 1)
btn_paper.grid(row = 2, column = 2)

win.mainloop()      

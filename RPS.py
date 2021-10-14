from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from random import randint


class Rps:
    # final winner in new window
    def winner(self, args):
        self.root3 = Toplevel()
        self.root3.title('Result display:')
        self.root3.geometry('450x350+550+130')
        self.root3.configure(bg='black')
        self.root3.focus_force()
        self.root3.grab_set()
        self.root2.destroy()
        Label(self.root3, text='Game Over', font=('times', 40, 'bold'), fg='Yellow', bg='black').place(x=85, y=50)
        Label(self.root3, text='Computer Score', font=('times', 15, 'bold'), fg='white', bg='black', bd=2,
              relief=RIDGE, padx=10).place(x=70, y=150, height=40, width=160)
        Label(self.root3, text='Player Score', font=('times', 15, 'bold'), fg='white', bg='black', bd=2,
              relief=RIDGE, padx=10).place(x=230, y=150, height=40, width=160)
        Label(self.root3, text=self.score, font=('times', 15, 'bold'), fg='white', bg='black', bd=2,
              relief=RIDGE, padx=10).place(x=70, y=190, height=40, width=160)
        Label(self.root3, text=self.p_score, font=('times', 15, 'bold'), fg='white', bg='black', bd=2,
              relief=RIDGE, padx=10).place(x=230, y=190, height=40, width=160)

        if args == 1:
            Label(self.root3, text='Computer won!!!', font=('times', 25, 'bold'), fg='white', bg='black').place(x=110, y=280)
        if args == 2:
            Label(self.root3, text='Player won!!!', font=('times', 25, 'bold'), fg='white', bg='black').place(x=110, y=280)

    # printing winning or losing message
    def update_message(self, msg):
        self.root2.message['text'] = msg

    # updating computer score
    def update_computer_score(self):
        self.score = int(self.root2.comp_score['text'])
        self.score = self.score + 1
        self.root2.comp_score['text'] = str(self.score)
        if int((int(self.var_rounds.get())) / 2) + 1 == self.score:
            self.winner(1)
            self.score = 0
            self.var_rounds.set("")

    # updating player score
    def update_player_score(self):
        self.p_score = int(self.root2.player_score['text'])
        self.p_score = self.p_score + 1
        self.root2.player_score['text'] = str(self.p_score)
        if int((int(self.var_rounds.get())) / 2) + 1 == self.p_score:
            self.winner(2)
            self.p_score = 0
            self.var_rounds.set("")

    # checking the winner
    def check_winner(self, computer, player):
        if computer == player:
            self.update_message("It's a tie...!!!")
        elif computer == 'rock':
            if player == 'paper':
                self.update_message('Player wins...!!!')
                self.update_player_score()
            else:
                self.update_message('Computer wins...!!!')
                self.update_computer_score()
        elif computer == 'paper':
            if player == 'rock':
                self.update_message('Computer wins...!!!')
                self.update_computer_score()
            else:
                self.update_message('Player wins...!!!')
                self.update_player_score()
        elif computer == 'scissors':
            if player == 'rock':
                self.update_message('Player wins...!!!')
                self.update_player_score()
            else:
                self.update_message('Computer wins...!!!')
                self.update_computer_score()
        else:
            pass

    # choices for changing images and calling checking winner function
    def update_choice(self, selection):
        choice = ['rock', 'paper', 'scissors']
        # computer choices:
        comp_choice = choice[randint(0, 2)]
        if comp_choice == 'rock':
            self.root2.comp_image.configure(image=self.root2.rock)
        elif comp_choice == 'paper':
            self.root2.comp_image.configure(image=self.root2.paper)
        else:
            self.root2.comp_image.configure(image=self.root2.scissors)

        # player choice
        if selection == 'rock':
            self.root2.player_image.configure(image=self.root2.player_rock)
        elif selection == 'paper':
            self.root2.player_image.configure(image=self.root2.player_paper)
        else:
            self.root2.player_image.configure(image=self.root2.player_scissors)

        self.check_winner(comp_choice, selection)

    def play_with_computer(self):
        if self.var_rounds.get() == "" or ((int(self.var_rounds.get())) % 2) != 1:
            messagebox.showinfo('Info', 'Please enter odd number of rounds you want to play to proceed!!', parent=self.root)
            self.var_rounds.set("")
            # return False
        # if ((int(self.var_rounds.get())) % 2) != 1:
        #     messagebox.showinfo('Info', 'Please enter odd number of rounds you want to play!!!', parent=self.root)
        else:
            self.root2 = Toplevel()
            self.root2.title('Playing with computer')
            self.root2.geometry('950x400+280+100')
            self.root2.configure(bg='black')
            self.root2.focus_force()
            self.root2.grab_set()

            # pictures
            self.root2.rock = ImageTk.PhotoImage(file="images/rock.png")
            self.root2.player_rock = ImageTk.PhotoImage(file="images/rock.png")
            self.root2.paper = ImageTk.PhotoImage(file="images/paper.png")
            self.root2.player_paper = ImageTk.PhotoImage(file="images/paper.png")
            self.root2.scissors = ImageTk.PhotoImage(file="images/scissors.png")
            self.root2.player_scissors = ImageTk.PhotoImage(file="images/scissors.png")

            # insert pictures
            self.root2.comp_image = Label(self.root2, image=self.root2.rock, bg='black')
            self.root2.comp_image.grid(row=1, column=0)
            self.root2.player_image = Label(self.root2, image=self.root2.player_rock, bg='black')
            self.root2.player_image.grid(row=1, column=4)

            # label
            comp_label = Label(self.root2, text='computer', font=('times', 15, 'bold'), fg='white', bg='black')
            comp_label.grid(row=0, column=1)
            player_label = Label(self.root2, text='player', font=('times', 15, 'bold'), fg='white', bg='black')
            player_label.grid(row=0, column=3)

            # messages
            self.root2.message = Label(self.root2, font=('times', 15, 'bold'), fg='white', bg='black')
            self.root2.message.grid(row=6, column=2)

            # label for scores
            self.root2.comp_score = Label(self.root2, text=0, font=('times', 25, 'bold'), fg='white', bg='black')
            self.root2.comp_score.grid(row=1, column=1)
            self.root2.player_score = Label(self.root2, text=0, font=('times', 25, 'bold'), fg='white', bg='black')
            self.root2.player_score.grid(row=1, column=3)

            # buttons
            rock_button = Button(self.root2, text='rock', font=('times', 15, 'bold'), bg='yellow', cursor='hand2',
                                 activebackground='yellow', command=lambda: self.update_choice('rock'), width=10)
            rock_button.grid(row=5, column=1, padx=10, pady=10)
            paper_button = Button(self.root2, text='paper', font=('times', 15, 'bold'), bg='pink', cursor='hand2',
                                  activebackground='pink', command=lambda: self.update_choice('paper'), width=10)
            paper_button.grid(row=5, column=2, padx=10, pady=10)
            scissors_button = Button(self.root2, text='scissors', font=('times', 15, 'bold'), bg='red', cursor='hand2',
                                     activebackground='red', command=lambda: self.update_choice('scissors'), width=10)
            scissors_button.grid(row=5, column=3, padx=10, pady=10)

    def __init__(self, root1):
        self.root = root1
        self.root.title('Rock Paper Scissor')
        self.root.geometry('1000x400+250+100')
        self.root.configure(bg='Purple')

        self.var_rounds = StringVar()
        self.score = 0
        self.p_score = 0

        canvas = Canvas(self.root, bg='Purple')
        canvas.create_text(500, 60, text='Welcome to Rock Paper Scissor game!!!', font=('times', 25, 'bold'))
        canvas.pack(fill='both', expand=True)

        #self.root.wm_iconbitmap('rps.ico')

        frame = Frame(self.root, bg='black', relief='sunken')
        frame.place(x=150, y=110, width=700, height=250)
        Label(frame, text='Number of rounds you want to play:', font=('times', 15, 'bold'), bg='black',
              fg='white').place(x=150, y=30)
        self.e_rounds = Entry(frame, font=('times', 15), justify='center', relief='ridge', textvariable=self.var_rounds)
        self.e_rounds.place(x=460, y=33, width=50)

        Label(frame, text='Choose number of players below:', font=('times', 15, 'bold'), bg='black',
              fg='white').place(x=200, y=100)
        Button(frame, text='Play with computer', font=('times', 15, 'bold'), command=self.play_with_computer,
               bg='green', cursor='hand2', activebackground='green', bd=10).place(x=250, y=150, width=200)
        # Button(frame, text='Two players', font=('times', 15, 'bold'), bg='Red',
        #        cursor='hand2', activebackground='red').place(x=360, y=150, width=200)


root = Tk()
obj = Rps(root)
root.mainloop()

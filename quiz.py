from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import time
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='exam')
cur=mydb.cursor()
index=0
def administration():
    return
def next():
    screen=Tk()
    screen.mainloop()
def history(prev_screen):
    prev_screen.destroy()
    screen=Tk()
    screen.title('History')
    screen.geometry('700x500')

    prog_bar=ttk.Progressbar(screen,orient='horizontal',length=100,maximum=100)
    prog_bar.place(x=300,y=10)
    l1 = Label(screen)
    l1.place(x=30, y=100)
    question=Label(screen,text='')
    question.place(x=80, y=100)
    v=IntVar()
    option1=Radiobutton(screen,value=1,variable=v)
    option2 = Radiobutton(screen, value=2, variable=v)
    option3 = Radiobutton(screen, value=3, variable=v)
    option4 = Radiobutton(screen, value=4, variable=v)
    option1.place(x=80,y=150)
    option2.place(x=80, y=200)
    option3.place(x=80, y=250)
    option4.place(x=80, y=300)
    query='SELECT * FROM pythontest'
    cur.execute(query)
    results=cur.fetchall()
    id = 1
    ans=[]
    rbs=[option1,option2,option3,option4]
    for row in results:
        v.set(0)
        prog_bar['value'] = 0
        x = 10
        l1.config(text='Q'+str(row[0]))
        question.config(text=row[1])
        option1.config(text=row[2])
        option2.config(text=row[3])
        option3.config(text=row[4])
        option4.config(text=row[5])
        id=id+1
        for i in range(11):
            screen.update()
            time.sleep(1)
            prog_bar['value']=x
            x=x+10
        ans.append(row[v.get()+1])

       # rbs[v.get()-1].deselect()

    print(ans)
    showinfo('Info','Thappu')
    screen.destroy()
    screen.mainloop()

def geography(prev_screen):
    prev_screen.destroy()
    screen = Tk()
    screen.title('Geography')
    screen.mainloop()

def cricket(prev_screen):
    prev_screen.destroy()
    screen = Tk()
    screen.title('Cricket')
    screen.mainloop()

def current_affairs(prev_screen):
    prev_screen.destroy()
    screen = Tk()
    screen.title('Current Affairs')
    screen.mainloop()

def mixed(prev_screen):
    prev_screen.destroy()
    screen = Tk()
    screen.title('Mixed')
    screen.mainloop()

def select_topic(data):
    topics = {1: history, 2: geography, 3: cricket, 4: current_affairs, 5: mixed}
    choice=data[0].get()
    if choice==0:
        showerror('Error', 'No topic selected, please select one')
    else:
        if askokcancel('Begin', 'There will be 10 question, 10 seconds for each question. Press ok to begin'):
           topics[choice](data[1])

def choice_screen(prev_screen):
    prev_screen.destroy()
    screen4=Tk()
    screen4.title('Welcome')
    screen4.geometry('700x700')
    screen4.wm_maxsize(width=700,height=700)
    screen4.wm_minsize(width=700, height=700)
    l1=Label(screen4,text='Welcome to GK testing platform')
    l1.config(font=('calibri',30,'bold'))
    l1.place(x=70,y=10)

    l2 = Label(screen4, text='Select your choice of topic')
    l2.config(font=('calibri', 20, 'bold'))
    l2.place(x=190, y=80)
    v=IntVar()

    rb1=Radiobutton(screen4,text='History',variable=v,indicator=0,value=1,font=('calibri',20,'bold'))
    rb1.config(bg='orange')
    rb2 = Radiobutton(screen4, text='Geography', variable=v,indicator=0, value=2,font=('calibri',20,'bold'))
    rb2.config(bg='orange')
    rb3 = Radiobutton(screen4, text='Cricket', variable=v,indicator=0, value=3,font=('calibri',20,'bold'))
    rb3.config(bg='orange')
    rb4 = Radiobutton(screen4, text='Current Affairs', variable=v,indicator=0, value=4,font=('calibri',20,'bold'))
    rb4.config(bg='orange')
    rb5 = Radiobutton(screen4, text='Mixed', variable=v, indicator=0, value=5, font=('calibri', 20, 'bold'))
    rb5.config(bg='orange')
    rb1.place(x=240,y=170,width=200)
    rb2.place(x=240, y=235,width=200)
    rb3.place(x=240, y=300,width=200)
    rb4.place(x=240,y=360,width=200)
    rb5.place(x=240, y=420, width=200)

    data=(v,screen4)

    b1=Button(screen4,text='Next',width=20,height=1,font=('calibri',20,'bold'),relief='solid',command=(lambda : select_topic(data)))
    b1.place(x=200,y=500)
    screen4.mainloop()

def candidate_register(variables):
    credentials=(variables[0].get(),variables[1].get())
    query='INSERT INTO user VALUES(%s,%s)'
    try:
        cur.execute(query,credentials)
    except mysql.connector.errors.IntegrityError:
        showerror('Error','Username already exist')
        variables[0].delete(0,END)
        variables[1].delete(0, END)
    else:
        showinfo('Register','Registered Successfully')
        mydb.commit()
        showinfo('Login','Press ok to Login')
        candidate_signin_screen(variables[2])

def candidate_login(variables):
    credentials=(variables[0].get(),variables[1].get())
    query='SELECT * FROM user'
    cur.execute(query)
    results=cur.fetchall()
    if credentials in results:
        showinfo('Login',"Login success")
        choice_screen(variables[2])
    else:
        showerror('Error',"Incorrect Credentials")
        variables[0].delete(0, END)
        variables[1].delete(0, END)

def candidate_signup_screen(prev_screen):
    prev_screen.destroy()
    screen3=Tk()
    screen3.geometry('300x300')
    screen3.title('SignUp')
    row1 = Frame(screen3)
    username = Label(row1, text='Username: ')
    entryu = Entry(row1, font=(15))
    #row1.pack(side=TOP, fill=X, padx=10, pady=10)
    row1.place(x=20, y=60)
    username.pack(side=LEFT)
    entryu.pack(side=RIGHT)

    row1 = Frame(screen3)
    password = Label(row1, text='Password: ')
    entryp = Entry(row1, font=(15))
    #row1.pack(side=TOP, fill=X, padx=10, pady=10)
    row1.place(x=20, y=120)
    password.pack(side=LEFT)
    entryp.pack(side=RIGHT)

    variables=(entryu,entryp,screen3)

    submit = Button(screen3, text='Register',command=(lambda:candidate_register(variables)))
    submit.config(width=10, height=2, relief='solid')
    submit.place(x=110,y=180)

    screen3.mainloop()

def candidate_signin_screen(prev_screen):
    prev_screen.destroy()
    screen2=Tk()
    screen2.title('SignIn')
    screen2.geometry('300x300')
    row1 = Frame(screen2)
    username = Label(row1, text='Username: ')
    entryu = Entry(row1, font=(15))
   # row1.pack(side=TOP, fill=X, padx=10, pady=10)
    row1.place(x=20,y=60)
    username.pack(side=LEFT)
    entryu.pack(side=RIGHT)

    row1 = Frame(screen2)
    password = Label(row1, text='Password: ')
    entryp = Entry(row1, font=(15))
    #row1.pack(side=TOP, fill=X, padx=10, pady=10)
    row1.place(x=20, y=120)
    password.pack(side=LEFT)
    entryp.pack(side=RIGHT)

    variables = (entryu, entryp,screen2)

    submit = Button(screen2, text='Login',command=(lambda:candidate_login(variables)))
    submit.config(width=10, height=2, relief='solid')
    submit.place(x=110,y=180)

    screen2.mainloop()
def candidate():
    start_screen.destroy()
    screen1=Tk()

    screen1.geometry('300x300')
    b1=Button(screen1,text='SignIn',command=(lambda: candidate_signin_screen(screen1)))
    b1.config(width=20,height=3,relief='solid')
    b2=Button(screen1,text='SignUp',command=(lambda: candidate_signup_screen(screen1)))
    b2.config(width=20, height=3, relief='solid')
    b1.place(x=80,y=50)
    b2.place(x=80,y=150)

    screen1.mainloop()
if __name__=='__main__':
    start_screen=Tk()

    start_screen.geometry('300x300')

    admin=Button(start_screen,text='Administration')
    admin.config(width='20',height='3',relief='solid',command=administration)
    candidate=Button(start_screen,text='Candidate',command=candidate)
    candidate.config(width='20', height='3',relief='solid')
    admin.place(x=80,y=50)
    candidate.place(x=80,y=150)
    start_screen.mainloop()

    #choice_screen()
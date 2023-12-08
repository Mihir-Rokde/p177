from tkinter import*
root=Tk()
root.title("encapsulation")
root.geometry("400x400")
n1=Label(root,text="Name : ")
n1.place(relx=0.3,rely=0.1,anchor=CENTER)
name=Entry(root)
name.place(relx=0.6,rely=0.1,anchor=CENTER)
p1=Label(root,text="Password : ")
p1.place(relx=0.3,rely=0.2,anchor=CENTER)
password=Entry(root)
password.place(relx=0.6,rely=0.2,anchor=CENTER)
c1=Label(root,text="Captcha : ")
c1.place(relx=0.3,rely=0.3,anchor=CENTER)
captcha=Entry(root)
captcha.place(relx=0.6,rely=0.3,anchor=CENTER)
sn=Label(root)
sn.place(relx=0.5,rely=0.7,anchor=CENTER)
sp=Label(root)
sp.place(relx=0.5,rely=0.8,anchor=CENTER)
sc=Label(root)
sc.place(relx=0.5,rely=0.9,anchor=CENTER)
class userdb():
    def __init__(self):
        self.__username="Mihir"
        self.__password="Rokde"
        self.captcha="abc"
    def showuser(self):
        sn["text"]="name : "+self.__username
        sp["text"]="password : "+self.__password
        sc["text"]="captcha : "+self.captcha
user=userdb()
def adduser():
    global user
    user.username=name.get()
    user.password=password.get()
    user.captcha=captcha.get()
    print("details updated")
btn=Button(root,text="Update Login Details",command=adduser)
btn.place(relx=0.3,rely=0.5)
btn1=Button(root,text="Show profile",command=user.showuser)
btn1.place(relx=0.7,rely=0.5)

root.mainloop()
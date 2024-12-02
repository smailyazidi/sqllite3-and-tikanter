from tkinter import *
import sqlite3 


fen = Tk()
fen.geometry("700x400")
fen.configure(bg="green")
fen.title("SQLite Interface")
db=sqlite3.connect("gestion.db")
cur=db.cursor()
def inserstion():  

    t=Titre.get()
    p=prix.get()
    donnes = (t, p)
    cur.execute("INSERT INTO produit (titre, prix) VALUES (?, ?)", donnes)
    db.commit()
    print("donnes inserted")

res=cur.execute("SELECT * FROM  produit")
for r in res:
    print(r)

titre = Label(fen, text="Python SQLite", fg="black", bg="green", font=("Arial", 16))
titre.place(x=280, y=20)


lt = Label(fen, text="Titre :", fg="black",  font=("Arial", 16),bg="green")
lt.place(x=50, y=100)

Titre = Entry(fen, bg="white", fg="black", width=30)
Titre.place(x=200, y=100)


lt2 = Label(fen, text="Prix :", fg="black",  font=("Arial", 16),bg="green")
lt2.place(x=50, y=150)

prix = Entry(fen, bg="white", fg="black", width=30)
prix.place(x=200, y=150)

btn =Button(fen,text="Registre", font=("Arial", 10),command=inserstion)
btn.place(x=300, y=200)





fen.mainloop()

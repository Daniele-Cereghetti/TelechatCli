# Minichat cli
import time
import curses
import threading
import sqlite3
from curses import wrapper


# funzione per scegliere il nome dell'utente
def welkome(stdscr):
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_BLACK = curses.color_pair(1)
    stdscr.addstr("Benvenuto in questa mini chat ;)", curses.A_STANDOUT)
    stdscr.addstr(1,0,"Attento, non ridimensionare la schermata pf", RED_BLACK)
    stdscr.addstr(2,0,"Inserisci il tuo username: ")

    chars = []
    while True:
        key = stdscr.getkey()
        if key == "\n":
            tmp = ''.join(chars)
            cur.execute(f"SELECT * FROM user WHERE name = '{tmp}'")
            if cur.fetchone() is None:
                cur.execute(f"INSERT INTO user VALUES ('{tmp}')")
                con.commit()
            global username
            username = tmp
            break
        else:
            chars.append(key)
    

# Funzione principale
def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    global rows, cols
    rows, cols = stdscr.getmaxyx()
    # creo finiestra messaggi e imput
    messages_win = curses.newpad(rows-3, cols-2)
    messages_win.clear()
    inputs_win = curses.newpad(1, cols-2)
    inputs_win.clear()
    # start threads (deamon muore quando termino programma)
    messThred = threading.Thread(target=threadMessages, args=(messages_win,), daemon=True)
    messThred.start()
    threadInputs(inputs_win)

# thread che si occupa di stampare i messaggi
def threadMessages(win):
    conThred = sqlite3.connect(DB_FILE_NAME)
    curThred = conThred.cursor()
    lastId = 0
    while True:
        i = 0
        curThred.execute("SELECT MAX(id) FROM message")
        max = curThred.fetchone()[0]
        if type(max) is int:
            if lastId < max:
                win.clear()
                for row in curThred.execute(f"SELECT * FROM message ORDER BY id DESC LIMIT {rows-3}"):
                    lastId = row[0]
                    win.addstr(i,0,f"{row[2]}> {row[1]}", curses.A_UNDERLINE)
                    win.refresh(0,0,1,1,rows-2,cols-2)
                    i += 1
        time.sleep(0.1)

# funzione che si occupa di leggere gli input utente
def threadInputs(win):
    fix = username + "> "
    chars = []
    win.addstr(0,0, fix, curses.A_STANDOUT)
    win.refresh(0,0,rows-1,1,rows-1,cols-1)
    while True:
        win.clear()
        key = win.getkey()
        if key == "\n":
            tmp = ''.join(chars)
            if tmp == "exit":
                exit()
            else:
                cur.execute(f"INSERT INTO message (text, username) VALUES ('{tmp}', '{username}')")
                con.commit()
            chars = []
        else:
            chars.append(key)
        win.addstr(0,0, fix+''.join(chars), curses.A_STANDOUT)
        win.refresh(0,0,rows-1,1,rows-1,cols-1)


DB_FILE_NAME = "hometelegram.db"
con = sqlite3.connect(DB_FILE_NAME) or exit("File db not found")
cur = con.cursor() or exit("Errore durante la connesione al db")

wrapper(welkome)
wrapper(main)


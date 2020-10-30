import sqlite3

def dbSetup():
    conn = sqlite3.connect('communitybot.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE levels (user text, id text, level real)''')
    conn.commit()

    c.execute('''INSERT INTO levels VALUES('sample', '000', 421)''')
    conn.commit()

    conn.close()

def userInsert(user, id, level):
    conn = sqlite3.connect('communitybot.db')
    c = conn.cursor()

    c.execute('INSERT INTO levels VALUES(?, ?, ?)', (user, id, level))
    conn.commit()
    conn.close()



def selectLevels(args):
    conn = sqlite3.connect('communitybot.db')
    c = conn.cursor()

    c.execute('SELECT level FROM levels WHERE id = ?', (args,))
    result = c.fetchone()

    conn.close()

    return result

def updateLevel(level, id):
    conn = sqlite3.connect('communitybot.db')
    c = conn.cursor()

    c.execute('UPDATE levels SET level = ? WHERE id = ?', (level, id))
    conn.commit()

    conn.close()

def selectXP(id):
    conn = sqlite3.connect('communitybot.db')
    c = conn.cursor()

    c.execute('SELECT level FROM levels WHERE id = ?', (id,))
    result = c.fetchone()

    conn.close()

    return result

def query(query):
    conn = sqlite3.connect('communitybot.db')
    c = conn.cursor()

    c.execute(query)
    conn.commit()

    conn.close()
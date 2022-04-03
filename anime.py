import sqlite3


def init():
	db = sqlite3.connect('database.db')
	c = db.cursor()

def add_anime(user_id, name):
	db = sqlite3.connect('database.db')
	c = db.cursor()
	if name not in anime_list(user_id):
		c.execute('INSERT INTO user_anime (user_id, anime, last_ser) VALUES (?, ?, 0)', (user_id, name))
		db.commit()

def get_users():
	db = sqlite3.connect('database.db')
	c = db.cursor()
	c.execute('SELECT DISTINCT user_id FROM user_anime')
	val = c.fetchall()
	table_list = [x[0] for x in val]
	return table_list

def anime_list(user_id):
	db = sqlite3.connect('database.db')
	c = db.cursor()
	c.execute('SELECT anime FROM user_anime WHERE user_id = ? ORDER BY user_id ', (user_id, ))
	val = c.fetchall()
	table_list = [x[0] for x in val]
	return table_list

def check_last_anime_ser(user_id, name):
	db = sqlite3.connect('database.db')
	c = db.cursor()
	c.execute('SELECT last_ser FROM user_anime WHERE user_id = ? AND anime = ?', (user_id, name, ))
	return int(c.fetchone()[0])

def update_last_anime_ser(name, number, user_id):
	db = sqlite3.connect('database.db')
	c = db.cursor()
	c.execute("UPDATE user_anime SET last_ser = ? WHERE anime = ? AND user_id = ?", (number, name, user_id ))
	db.commit()

def delete_anime(user_id, name):
	db = sqlite3.connect('database.db')
	c = db.cursor()
	c.execute('DELETE FROM user_anime WHERE anime = ? AND user_id = ?', (name, user_id, ))
	db.commit()

def add_voice(user_id, voice):
	db = sqlite3.connect('database.db')
	c = db.cursor()
	c.execute('UPDATE user_anime SET voice = ? WHERE user_id = ? AND id = (SELECT max(id) FROM user_anime WHERE user_id = ?)', (voice, user_id, user_id, ))
	db.commit()

def get_voice(user_id, name):
	db = sqlite3.connect('database.db')
	c = db.cursor()
	c.execute('SELECT voice FROM user_anime WHERE user_id = ? AND anime = ?', (user_id, name,))
	return c.fetchone()[0]


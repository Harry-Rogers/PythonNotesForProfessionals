# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:52:29 2020

@author: Harry
"""

import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS user")
c.execute("CREATE TABLE user (name text, age integer)")
c.execute("INSERT INTO user VALUES ('User A', 42)")
c.execute("INSERT INTO user VALUES ('User B', 43)")
conn.commit()
c.execute("SELECT * FROM user")
print(c.fetchall())
conn.close()

#More info on functions on pages 674,675,676,677,678,679
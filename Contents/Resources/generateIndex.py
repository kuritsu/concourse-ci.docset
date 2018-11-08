#!/usr/bin/env python

import os, re, sqlite3, io
import json

conn = sqlite3.connect('docSet.dsidx')
cur = conn.cursor()

try: cur.execute('DROP TABLE searchIndex;')
except: pass
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

index_path = 'Documents/search_index.json'
index_file = open(index_path)

index_doc = json.load(index_file)

for field in index_doc.keys():
    value = index_doc[field]
    name = value['title']
    path = value['location']
    if path != 'index.html':
        cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Category', path))
        print 'name: %s, path: %s' % (name, path)

conn.commit()
conn.close()
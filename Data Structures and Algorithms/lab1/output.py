##open specified file to read
from pdb import line_prefix
import pymysql

HOST = 'cse.unl.edu'
USER = 'ycheah'
PASSWD = 'mysqlPassword'
DB = 'ycheah'

db = pymysql.connect(host = HOST, user = USER, passwd = PASSWD, db = DB)
cur = db.cursor()

f = open ('sample.fasta', 'r')

#create empty dictionary object instance
o = {}
a = {}

for line in f: 
    ##ignore > symbol as signifies start of new protein
    if line[0] == '>':
        ##split by |
        m = line.split("|")
        o[m[1]] = m[2]
        c = m[1]
        a[c] = ''
    else:
        a[c] += line

f.close()

for key in o:
    print("ID: ",(key), "\n")
    print("Protein Information: ", o[key], "\n")
    print("Sequence:", a[key])
    
for i in o:
    cur.execute('INSERT INTO PROTEIN (description) VALUES (%s);', (i))
    db.commit()

for b in a:
    cur.execute('INSERT INTO PROTEIN (sequence) VALUES (%s);', (i))
    db.commit()

cur.close()




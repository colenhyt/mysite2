#encoding=utf-8
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

db=MySQLdb.connect(user='root',host="localhost",passwd="",charset='utf8')
cur=db.cursor()
cur.execute('use bighorse')
cur.execute('select * from bigdata limit 100')

f=file("item.txt",'w')

for i in cur.fetchall():
    print str(i)
    f.write(str(i))
    f.write(" ")

f.close()
cur.close()

from dpark import DparkContext
dpark = DparkContext()
count = dpark.accumulator(0)

def random_once(*args, **kwrgs):
    x = random() * 2 - 1
    y = random() * 2 - 1
    if x * x + y * y < 1:
        count.add(1)

dpark.parallelize(range(0, N), 10).foreach(random_once)
print 'PI is roughly', 4.0 * count.value / N

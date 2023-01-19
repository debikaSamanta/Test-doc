#from couchdb import Server
# localhost:5984/_utils/
# docker-compose stop
#sudo netstat -lpn |grep :5984
#sudo kill -9 2058
from couchdb import Server

s = Server('http://admin:adminpw@localhost:5984/')
db = s['mychannel_basic']
    # the since parameter defaults to 'last_seq' when using continuous feed
ch = db.changes(feed='continuous',heartbeat='1000',include_docs=True)

# print(ch)
for line in ch:
    doc = line['doc']
    if(str(doc).__contains__("'_id':'1'")) :
        print(doc)
    
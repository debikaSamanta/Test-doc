import couchdb
couch = couchdb.Server()

print(couch)

couch = couchdb.Server('http://localhost:5984/')
couch = couchdb.Server('https://admin:1234@localhost:5984/')

db = couch.create('test')
db = couch['mydb']
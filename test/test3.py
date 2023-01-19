#pip install pycouchdbpip ,install -i http://simple.crate.io/ pycouchdb
import pycouchdb
#server = pycouchdb.Server()
server = pycouchdb.Server("http://admin:1234@localhost:5984/")
print(server)

db = server.database("test")
print(db)
db.save({"author": "John", "content": "Blog"})
# map_func = "function(doc) { emit(doc.name, 1); }"
# db.temporary_query(map_func)
# list(db.temporary_query(map_func))
# def feed_reader(message, db):
#     print(message)

# db.changes_feed(feed_reader)
def feed_reader(message, db):
    print(message)

db.changes_feed(feed_reader)
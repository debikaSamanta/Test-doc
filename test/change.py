from pycouchdb.feedreader import BaseFeedReader
from pycouchdb.exceptions import FeedReaderExited
import pycouchdb
#server = pycouchdb.Server()
server = pycouchdb.Server("http://admin:1234@localhost:5984/")
#print(server)

db = server.database("test")
#print(db)

# db.changes_feed(feed_reader)
def feed_reader(message, db):
    print(message)

#db.changes_feed(feed_reader)

class MyReader(BaseFeedReader):
    def on_message(self, message):
     # self.db is a current Database instance
     # process message
        raise FeedReaderExited()

    def on_close(self):
         # This is executed after a exception
        # is raised on on_message method
        print("Feed reader end")

db.changes_feed(MyReader())
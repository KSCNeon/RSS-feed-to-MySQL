import feedparser
import mysql.connector

mydb = mysql.connector.connect(
    user='dbuser',
    password='dbpassword',
    host='dbhost',
    database='dbname')
mycursor = mydb.cursor()

RSS_URLS = [
    'https://www.spiegel.de/schlagzeilen/index.rss',
    'https://www.tagesschau.de/xml/rss2_https/',
    ]

feeds = []
for url in RSS_URLS:
    feeds.append(feedparser.parse(url))

for feed in feeds:
    for post in feed.entries:
        title = post.title
        description = post.description
        content = f"<code>{post.content}</code>"
        link = post.link
        published = post.published

        print(title)
        sqlFormula = "INSERT INTO tagesschau (title, description, content, link, published) VALUES (%s, %s, %s, %s, %s)"
        tagesschau = [(title, description, content, link, published)]
        mycursor.executemany(sqlFormula, tagesschau)
        mydb.commit()
        count = 0


    #print(description)
    #print(content)
    #print(link)

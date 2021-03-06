#!/usr/bin/env python
import web
from scrapymasters.common.ConfigFiles import ConfigFiles
from scrapymasters.common.MongoUtils import MongoUtils

urls = (
    '/articles/words/(.+)', 'WordsGetOne',
    '/articles', 'Articles',
    '/articles/words', 'Words',
)

app = web.application(urls, globals())


class Articles:
    def __init__(self):
        self.config = ConfigFiles.config()

    def GET(self):
        client = MongoUtils.create_client_from_config(self.config)
        db = client.scrape
        articles = MongoUtils.find_all_articles(db)
        client.close()
        return articles


class WordsGetOne:
    def __init__(self):
        self.config = ConfigFiles.config()

    def GET(self, word):
        client = MongoUtils.create_client_from_config(self.config)
        db = client.scrape
        articles = MongoUtils.find_article_by_word(db, word)
        client.close()
        return articles


class Words:
    def __init__(self):
        self.config = ConfigFiles.config()

    def GET(self):
        client = MongoUtils.create_client_from_config(self.config)
        db = client.scrape
        words = MongoUtils.find_all_words(db)
        client.close()
        return words

if __name__ == "__main__":
    app.run()

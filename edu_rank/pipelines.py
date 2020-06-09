# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import logging

from scrapy.utils.project import get_project_settings


class EduRankPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        MONGODB = settings.get('MONGODB')
        logging.debug('========================')
        logging.debug(MONGODB)
        logging.debug('========================')
        self._db = MONGODB.get('db')
        self._collection = MONGODB.get('collection')
        self._uri = MONGODB.get('host')

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self._uri)
        self.db = self.client.get_database(self._db)
        self.collection = self.db.get_collection(self._collection)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):

        result = self.collection.find_one({ 'site': item['site'], 'title': item['title']})
        if not result:
            result = self.collection.insert(dict(item))
        else:
            print 'exist'
        return item
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import json
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# fh = logging.FileHandler('test.log')
# fh.setLevel(logging.DEBUG)
class GeneraScrapyPipeline(object):
    def process_item(self, item, spider):
    #     logger.info(item["name"])
    #     logger.info(item["imgurl"])
    #     logger.info(item["imgherf"])
    #     logger.info(item["imgvisit"])
    #     logger.info(item["imglike"])
    #     logger.info(item["imgdiscrit"])
        conn = sqlite3.connect('/home/zxf/zz1806/zz1806/untitled6/db.sqlite3')
        cursor = conn.cursor()
        sql_insert = """insert into huaban (name, imgurl, imgherf, imgvisit, imglike, imgdiscrit) values (?,?,?,?,?,?)"""
        param = (item['name'], item['imgurl'], item['imgherf'], item['imgvisit'], item['imglike'],item['imgdiscrit'])
        cursor.execute(sql_insert, param)
        conn.commit()
        return item


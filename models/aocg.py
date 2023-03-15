from peewee import *


class Aocg(Model):

    id = AutoField()

    articleHost = TextField()

    articleUrl = TextField()

    articleTitle = TextField()

    articlePublishTime = DateTimeField()

    articleCrawlTime = DateTimeField()

    plainText = TextField()

    richText = TextField()
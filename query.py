from peewee import *


class Query:

    @staticmethod
    def select(Model,limit=None,keys=[]):
        database = Model._meta.database
        if database.is_closed():
            database.connection()
        result = []

        try:
            if limit:
                result = Model.select().where(*keys).limit(limit).dicts()
            else:
                result = Model.select().where(*keys).dicts()
            if result:
                result = list(result)

        except Exception as e:
            pass

        finally:
            if not database.is_closed():
                database.close()

        return result

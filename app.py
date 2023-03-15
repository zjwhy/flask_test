from flask import Flask,request,jsonify
import datetime
from query import Query
from models.aocg import Aocg
from db import sqldb
app = Flask(__name__)


@app.route('/aocg/result')
def aocg_result():
    count = int(request.args.get("count"))  if request.args.get("count",None) else None
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    publish_time = request.args.get("publishTime",now_time)
    Aocg.bind(sqldb)
    keys = [Aocg.articlePublishTime==publish_time]
    result = Query.select(Aocg,count,keys)
    for result_ in result:
        result_['articlePublishTime'] = result_['articlePublishTime'].strftime('%Y-%m-%d %H:%M:%S')

    return jsonify(result)


if __name__ == '__main__':
    app.run()

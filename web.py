from flask import Flask, redirect, request
from flask_cors import CORS, cross_origin
from get_util_fct import get_util
from get_graph_fct import get_graph
from flask import jsonify
app = Flask(__name__)
CORS(app)

@app.route("/capacity")
def hello():
    ip = request.args['ip']
    host = request.args['host']
    start = request.args['start']
    print "interface: %s , host : %s " %(ip,host)
    results = get_util(host,ip,start)
    return results
    #print jsonify({'entry': get_util(host,ip)})
    #return jsonify({'entry': get_util(host,ip)})
#    return "Hostname:%s and Inteface: %s" %(ip,host)

@app.route("/graph")
def graph():
    ip = request.args['ip']
    host = request.args['host']
    print "interface: %s , host : %s " %(ip,host)
    results = get_graph(host,ip)
    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded=True)

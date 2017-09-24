import cherrypy
import json
class vali(object):
    @cherrypy.expose
    def index(self):
        result = {}
        if 'X-Forwarded-For' in cherrypy.request.headers.keys():
            result['type'] = 0 #透明
        else:
            result['type'] = 2 #高匿
        return json.dumps(result)
def start_server():
    cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8088})
    cherrypy.quickstart(vali())

if __name__ == "__main__":
    start_server()
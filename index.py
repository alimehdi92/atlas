import cherrypy
import os
from mako.template import Template


class HelloWorld(object):
    def index(self):
        mytemplate = Template(filename='index.html')
        return mytemplate.render()
        
    index.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(HelloWorld())

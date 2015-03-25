import cherrypy
import os
from mongoengine import *
from mako.template import Template

class Blog(Document):
    text = StringField()
    author = StringField()

class HelloWorld(object):
    def index(self):
        mytemplate = Template(filename='index.html')
        return mytemplate.render()

    def add_stuff(self, text=None, author=None):
        if text and author:
            entry = Blog(text=text, author=author)
            return entry.save()

    def show_all(self):
        showTemplate = Template(filename='show.html')
        return showTemplate.render(blogs=Blog.objects())

    index.exposed = True
    add_stuff.exposed = True
    show_all.exposed = True


if __name__ == '__main__':
    conn = connect('heroku-app', host='ds031701.mongolab.com:31701',
                   username='admin', password='admin')
    conf = {
            '/': {
                 'tools.sessions.on': True,
                 'tools.staticdir.root': os.path.abspath(os.getcwd())
            },
            'global': {
                 'server.socket_host': '0.0.0.0',
                 'server.socket_port': int(os.environ.get('PORT', '5000'))
            },
            '/js': {
                 'tools.staticdir.on': True,
                 'tools.staticdir.dir': './js'
            }
        }

    cherrypy.quickstart(HelloWorld(), '/', conf)

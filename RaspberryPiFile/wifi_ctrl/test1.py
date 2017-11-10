#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
 
"""
__author__ = ''
__version__ = ''
 
import os
import RPi.GPIO as io
import tornado.ioloop
import tornado.web
 
 
class ControlHandler(tornado.web.RequestHandler):
    def put(self, *args, **kwargs):
        body = self.request.body.decode()
        if body == 'up':
            io.output(7, io.HIGH)
        elif body == 'down':
            io.output(7, io.LOW)
 
 
if __name__ == "__main__":
    try:
        io.setmode(io.BOARD)
        io.setup(7, io.OUT)
 
        #os.chdir(os.path.dirname(__file__))
        tornado.web.Application([
            ('/', tornado.web.RedirectHandler, dict(url='/web/index.html')),
            ('/web/(.*)', tornado.web.StaticFileHandler, dict(path='./web')),
            ('/control', ControlHandler),
        ]).listen(80)
        tornado.ioloop.IOLoop.instance().start()
    finally:
        io.cleanup()

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:13:33 2020

@author: Harry
"""

import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
 font_name='Times New Roman',
 font_size=36,
 x=window.width//2, y=window.height//2,
 anchor_x='center', anchor_y='center')

@window.event
def on_draw():
 window.clear()
 label.draw()
pyglet.app.run()


#for more check https://pyglet.readthedocs.io/en/latest/
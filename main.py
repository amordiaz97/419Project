

from google.appengine.api import users
#from google.appengine.api import ndb

import webapp2
import jinja2
import random
import json
import logging


env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))



class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template('login.html')
		user = users.get_current_user()
		if user:
			url = users.create_logout_url('/')
			data = {'url' : url}
		else:
			url = users.create_login_url('/home')
			data = {'url' : url}
		self.response.write(template.render(data))

class HomeHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template('homepage.html')
		self.response.write(template.render())

class MenardsHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template('menards.html')
		self.response.write(template.render())

class TargetHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template('target.html')
		self.response.write(template.render())

class CostcoHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template('costco.html')
		self.response.write(template.render())




app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/home', HomeHandler),
	('/target', TargetHandler),
	('/menards', MenardsSongHandler),
	('/costco', CostcoHandler)

], debug=True)

from rtmbot import Rtmbot
from rtmbot.core import Plugin
from secret import SLACK_TOKEN

class HelloPlugin(Plugin):
	def process_message(self,data):
		if "애란" in data["text"]:
			self.outputs.append([data["channel"],'불렀어?'])
		print(data)


config = {
	"SLACK_TOKEN" : SLACK_TOKEN
	"ACTIVE_PLUGINS" : ["main.HelloPlugin"]
}
bot = Rtmbot(config)
bot.start()


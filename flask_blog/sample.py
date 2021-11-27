from flask import Flask
ai = Flask(__name__)

@ai.route("/")
@ai.route("/home")
def home():
	return """
		<h1><center>Blue Sky Inc.</center></h1>
	"""

@ai.route("/about")
def about():
	return """

	<i>Employee no 1</i> : 9856234578<br>
	<i>Employee no 2</i> : 9856234544<br>
	<i>Employee no 3</i> : 9856234532<br>
	<i>Employee no 4</i> : 9856242752<br>
	"""
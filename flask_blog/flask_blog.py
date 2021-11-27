from flask import Flask, render_template, url_for
app = Flask(__name__)

post_list = [
	{
		'author' : 'Nishant kumbhar',
		'title'  : 'Blog Post 1',
		'content': 'First blog Content',
		'date_of_post' : 'April 10, 2021'
	},
	{
		'author' : 'Bucky Robert',
		'title'  : 'Blog Post 2',
		'content': 'Second blog Content',
		'date_of_post' : 'January 23, 2022'
	}	

]

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", post_arg = post_list)



@app.route("/about")
def about():
	return render_template("about.html", title_of_about='About : send from home')

@app.route("/contact")
@app.route("/help")
def contact():
	return render_template("contact.html")




if __name__ == '__main__':
	app.run(debug=True)

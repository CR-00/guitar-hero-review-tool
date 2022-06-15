import time
import random

from flask import Flask, jsonify
from flask_cors import CORS


def generate_random_input():
	"""Won't need this when you have a controller."""
	return [random.randrange(2) for _ in range(5)]


colors = ["blue", "red", "green", "purple", "brown"]

app = Flask(__name__)
CORS(app)

# Make these persist between requests.
app.config["rows"] = ""
app.config["controller_input"] = generate_random_input()



def render_circle(i):
	"""Render coloured circle, add hidden class if button isn't pressed."""
	if app.config["controller_input"][i]:
		color = colors[i]
	else:
		color = "#121212"
	return f'<span class="circle" style="background-color:{color};"></span>'


def generate_html():
	"""Generate rows for each turn."""
	html = f'<div class="button-display">'
	for i, _ in enumerate(app.config["controller_input"]):
		html += "<div>"
		html += render_circle(i)
		html += "</div>"
	html += "</div>"
	return html


@app.route("/render-input")
def render_input():
	"""Render coloured circles for each controller input."""
	app.config["controller_input"] = generate_random_input()
	app.config["rows"] += generate_html()
	return jsonify(app.config["rows"])


if __name__ == '__main__':
	app.run()
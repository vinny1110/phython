from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
	<form method="post">
		Enter a number: <input type="number" name="number" required>
		<input type="submit" value="Check">
	</form>
	{% if result %}
		<h2>{{ result }}</h2>
	{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def home():
	result = None
	if request.method == 'POST':
		try:
			num = int(request.form['number'])
			if num % 2 == 0:
				result = f"{num} is Even"
			else:
				result = f"{num} is Odd"
		except ValueError:
			result = "Invalid input!"
	return render_template_string(HTML_FORM, result=result)

if __name__ == '__main__':
	app.run(debug=True)


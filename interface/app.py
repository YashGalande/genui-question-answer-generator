from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Render index.html content as a string since we're keeping everything in the same folder
    with open('index.html', 'r') as file:
        content = file.read()
    return render_template_string(content)

if __name__ == '__main__':
    # Set Flask to run on port 3000
    app.run(debug=True, port=3000)

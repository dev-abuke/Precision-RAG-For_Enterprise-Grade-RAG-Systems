from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    description = request.form['description']
    scenarios = request.form['scenarios']
    # Here you will integrate the prompt generation algorithm
    generated_prompts = ["Prompt 1", "Prompt 2"]  # Placeholder for generated prompts
    return render_template('result.html', prompts=generated_prompts)

if __name__ == '__main__':
    app.run(debug=True)

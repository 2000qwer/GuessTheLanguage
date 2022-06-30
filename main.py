from flask import Flask ,render_template , request , url_for , redirect
import random

app = Flask(__name__)

guesses = ['Python','Java', 'C#', "Ruby", "C", "C++"]

questions = ['Is this compiled?', 'Does is run on VM?']

@app.route('/question/<int:id>', methods=['GET','POST'])
def question(id):
    if request.method == 'POST':
        if request.form['answer'] == 'yes':
            return redirect(url_for('question', id= id+1))
        else:
            return redirect(url_for('question', id=id))
    return render_template('question.html', question = questions[id])


@app.route('/question/<int:id>', methods=['GET','POST'])
def question(id):
    if request.method == 'POST':
        if request.form['answer'] == 'yes':
            return redirect(url_for('question', id= id+1))
        else:
            return redirect(url_for('question', id=id))
    return render_template('question.html', question = questions[id])



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_choice')
def random_guess():
    randoms = random.randint(0,5)
    return render_template('random_quess.html', random_guess = guesses[randoms])




@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess = guesses[id])








if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5001,debug=True)
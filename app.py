from flask import Flask, render_template, redirect, request
from apples_db import construct_db, query_db, add_to_db, update_db
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        phrase = request.form['phrase']
        add_to_db('phrase', phrase=phrase)
        return redirect('/enter')
    else:
        phrases = query_db('phrase')
        return render_template('enter.html')

@app.route('/answer', methods=['GET', 'POST'])
def answer():
        if request.method == 'POST':
            playername = request.form['playername']
            answer = request.form['answer']
            phrase_id = request.form['phrase_id']
            add_to_db('answer', phrase_id=phrase_id, answer=answer, playername=playername, votes=0)
            return redirect('/answer')
        else:
            phrases = query_db('phrase')
            if len(phrases) == 0:
                return render_template('no_phrases.html')   
            phrase = choice(phrases)
            return render_template('answer.html', phrase=phrase, flag=False)
        

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        phrase_id = request.form['phrase_id']
        phrase = query_db('phrase', id=phrase_id)
        try:
            answer_id = request.form['answer_id']
            votes = query_db('answer', id=answer_id)[0].votes
            votes += 1
            update_db('answer', 'votes', votes, id=answer_id)
        except:
            return redirect('/vote')
        return redirect('/vote')
    else:
        phrases = query_db('phrase')
        if len(phrases) == 0:
            return render_template('no_phrases.html', flag=True)
        else:
            phrase = choice(phrases)
            answers = query_db('answer', phrase_id=phrase.id)
            if len(answers) == 0:
                return render_template('no_answers.html')
            else:
                return render_template('vote.html', phrase=phrase, answers=answers)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    construct_db()
    app.run(debug=True)
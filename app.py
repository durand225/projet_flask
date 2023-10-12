from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def accueil():
    return render_template('/html/connexion.html')

@app.route('/aboute')
def about_us():
    return render_template('/html/index.html')


@app.route('/acceuil')
def acceuil():
    return render_template('/html/index.html')

@app.route('/profil', methods = ['GET', 'POST'])
def profil():
    return render_template('/html/profil.html')


if __name__ == '__main__':
    app.run(debug=True)





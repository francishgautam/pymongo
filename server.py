from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from helpers.MongoHelper import MongoHelper

app = Flask(__name__)
app.config['Mongo_URI'] = "mongodb+srv://dbUser:1234@cluster0.kihfc.mongodb.net/testDb?retryWrites=true&w=majority"

########################################################################################

if __name__ == "__main__":
    app.run(port=80, debug=TRUE)

#########################################################################################


@app.route('/')
def index():
    mongoHelper = MongoHelper()
    movies = mongoHelper.getAll()

    return render_template("index.html", moviesData=movies)


@app.route('/create', methods=["GET", "POST"])
def create():
    if(request.method == 'GET'):
  
        return render_template("create.html")
    else:
        movieName = request.form['movieName']
        genre = request.form['genre']
        director = request.form['director']

        mongoHelper = MongoHelper()

        movieObject = {"movie_name":movieName,"genre":genre,"director":director}
        mongoHelper.insert(movieObject)

        return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    mongoHelper = MongoHelper()

    print(mongoHelper.delete(id))

    return redirect(url_for('index'))

@app.route('/edit/<id>', methods=["GET", "POST"])
def edit(id):
    if(request.method == 'GET'):
        
        mongoHelper = MongoHelper()
        movieData = mongoHelper.get(id)

        return render_template("edit.html",movie=movieData)
    else:
        movieName = request.form['movieName']
        genre = request.form['genre']
        director = request.form['director']

        mongoHelper = MongoHelper()

        movieObject = {"movie_name":movieName,"genre":genre,"director":director}
        mongoHelper.insert(movieObject)

        return redirect(url_for('index'))



######################################################################################
# import url_for
# from flask_pymongo import pymongo

# app = Flask(__name__)
# app.config["MONGO_URI"] = ""
# mongo = PyMongo(app)


# @app.route("/")
# def index():
#     return '''
#         <form method="POST" action="/create" enctype="multipart/form-data">
#             <input type="text" name="movieName">
#             <input type="text" name="genre">
#             <input type="text" name="director">
#             <input type="submit">
#         </form>
#         '''

from flask import Flask, request, render_template, redirect, url_for
from cloudant.client import Cloudant 



app = Flask(__name__)



USERNAME = "2a3897c5-4813-4d4e-a46d-1075cbe1c9ca-bluemix"
APIKEY = "jt9RIMKSEUgXJLvbSivOhaQPbYG3UnOi1tmt_j2ycIIN"
CONNECT = True
DBNAME = "db"

client = Cloudant.iam(USERNAME, APIKEY, connect=CONNECT)
my_database = client.create_database(DBNAME)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods =['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form['username']
        passw = request.form['password']

        query = {'_id': {'$eq': user}, 'psw' : {'$eq' : passw}}
    
        docs = my_database.get_query_result(query)
        print(docs)
        print(len(docs.all()))
    
        if(len(docs.all())==0):
            return render_template('login.html', pred="The username is not found.")
        else:
            return redirect(url_for('prediction'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        x = [x for x in request.form.values()]
        print(x)
        data = {
            '_id': x[1], # Setting _id is optional
            'name': x[0],
            'psw':x[2]
        }
        print(data)

        query = {'_id': {'$eq': data['_id']}}
        docs = my_database.get_query_result(query)
        print(docs)
        print(len(docs.all()))
    
        if(len(docs.all())==0):
            url = my_database.create_document(data)
            #response = requests.get(url)
            return render_template('index.html')
        else:
            return render_template('register.html',)


@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(debug=True)
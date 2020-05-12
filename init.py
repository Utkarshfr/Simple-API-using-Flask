# Change the username and password while establishing a connection to the database if you have any
# make changes in every db.connect connection query

import flask
from flask import jsonify,request
import pymysql as db

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# sample data to test api without the use of database
data = [
    {'id': 0},
    {'title': 'A Fire Upon the Deep'},
    {'author': 'Vernor Vinge'},
    {'first_sentence': 'The coldsleep itself was dreamless.'},
    {'year_published': '1992'}
]


@app.route('/', methods=['GET'])
def home():
    return jsonify(data)


@app.route('/user/<int:key>', methods=['GET'])
def user(key):
    try:
        con = db.connect(host="localhost",database="test",user="root",password="")
        cursor = con.cursor()
        r = cursor.execute("select id,username,first_name,last_name,email from user WHERE id=%s",[key])
        if r>0:
            row = cursor.fetchone()
            x = dict()
            x['id']=row[0]
            x['username']=row[1]
            x['first_name']=row[2]
            x['last_name']=row[3]
            x['email']=[row[4]]
            r = cursor.execute("select alter_email from alternate_email WHERE id=%s",[key])
            if r>0:
                row = cursor.fetchall()
                for e in row:
                    x['email'].append(e)
            con.close()
            return jsonify(x)
        else:
            con.close()
            return jsonify({'status':'No data Found'})
    
    except Exception as e:
        return jsonify({'status':"Error connecting to database"})


@app.route('/add',methods=['POST'])
def users():
    username = request.form['username']
    if request.form['first_name']:
        first_name = request.form['first_name']
    else:
        first_name = ""
    
    if request.form['last_name']:
        last_name = request.form['last_name']
    else:
        last_name = ""

    if request.form['email']:
        email = request.form['email']
    else:
        email = ""
    
    password = request.form['password']
    data = [username,first_name,last_name,password,email]

    try:
        con = db.connect(host='localhost',database='test',user='root',password="")
        cursor = con.cursor()
        r = cursor.execute("insert into user(username,first_name,last_name,password,email) values (%s,%s,%s,%s,%s)",data)
        if r==0:
            con.close()
            return jsonify({'status':400})
        
        con.commit()
        con.close()
        return jsonify({'status':201})

    except Exception as e:
        return jsonify({'status':"Error connecting to database"})


@app.route('/update/user/<int:key>',methods=['POST'])
def update(key):
    try:
        con=db.connect(host='localhost',database='test',user='root',password="")
        cursor=con.cursor()
        r=cursor.execute("select * from user where id=%s",[key])
        
        if r>0:
            if request.form['username']:
                username = request.form['username']
                r=cursor.execute("UPDATE user SET username=%s WHERE id=%s",[username,key])

            if request.form['first_name']:
                first_name = request.form['first_name']
                r=cursor.execute("UPDATE user SET first_name=%s WHERE id=%s",[first_name,key])
            
            if request.form['last_name']:
                last_name = request.form['last_name']
                r=cursor.execute("UPDATE user SET last_name=%s WHERE id=%s",[last_name,key])

            if request.form['password']:
                password = request.form['password']
                r=cursor.execute("UPDATE user SET password=%s WHERE id=%s",[password,key])

            if request.form['email']:
                email = request.form['email']
                r=cursor.execute("UPDATE user SET password=%s WHERE id=%s",[email,key])
                
            con.commit()
            con.close()
            return jsonify({'status':200})

        else:
            con.commit()
            con.close()
            return jsonify({'status':'No Match Found'})


    except Exception as e:
        return jsonify({'status':"Error connecting to database"})



@app.route('/modify/user/<int:key>',methods=['POST'])
def modify(key):
    try:
        con=db.connect(host='localhost',database='test',user='root',password="")
        cursor=con.cursor()
        r=cursor.execute("select * from user where id=%s",[key])

        if r>0:
            if request.form['username']:
                username = request.form['username']
                r=cursor.execute("UPDATE user SET username=%s WHERE id=%s",[username,key])

            if request.form['first_name']:
                first_name = request.form['first_name']
                r=cursor.execute("UPDATE user SET first_name=%s WHERE id=%s",[first_name,key])
            
            if request.form['last_name']:
                last_name = request.form['last_name']
                r=cursor.execute("UPDATE user SET last_name=%s WHERE id=%s",[last_name,key])

            if request.form['password']:
                password = request.form['password']
                r=cursor.execute("UPDATE user SET password=%s WHERE id=%s",[password,key])

            if request.form['email']:
                email = request.form['email']
                r=cursor.execute("UPDATE user SET password=%s WHERE id=%s",[email,key])

            con.commit()
            con.close()
            return jsonify({'status':200})
        
        else:
            username = request.form['username']
            if request.form['first_name']:
                first_name = request.form['first_name']
            else:
                first_name = ""
            
            if request.form['last_name']:
                last_name = request.form['last_name']
            else:
                last_name = ""

            if request.form['email']:
                email = request.form['email']
            else:
                email = ""
            
            password = request.form['password']
            data = [key,username,first_name,last_name,password,email]
            r = cursor.execute("insert into user(id,username,first_name,last_name,password,email) values (%s,%s,%s,%s,%s,%s)",data)
            if r==0:
                con.close()
                return jsonify({'status':400})
            
            con.commit()
            con.close()
            return jsonify({'status':201})

    except Exception as e:
        return jsonify({'status':"Error connecting to database"})


@app.route('/email/add/<int:key>',methods=['POST'])
def email(key):
    try:
        con=db.connect(host='localhost',database='test',user='root',password="")
        cursor=con.cursor()
        r=cursor.execute("select * from user where id=%s",[key])

        if r>0:
            if request.form['email']:
                email = request.form['email']
                data = [key,email]
                r = cursor.execute("INSERT INTO alternate_email values (%s,%s)",data)

                if r>0:
                    con.commit()
                    con.close()
                    return jsonify({'status':201})

                else:
                    con.close()
                    return jsonify({'status':400})
            
        else:
            con.close()
            return jsonify({"status":"No data found"})

    except Exception as e:
        return jsonify({"status":"Error connecting to database"})

app.run()

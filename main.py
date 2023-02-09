from flask import Flask, request, jsonify, render_template,redirect,url_for
from authlib.integrations.flask_client import OAuth
import json
app = Flask(__name__)


data = {
    "users": [
        {
            "id": 0,
            "fName": "Om",
            "lName": "Patel",
            "email": "ompatel@gail.com",
            "password": "123456"
        },
        {
            "id": 1,
            "fName": "Jagrat",
            "lName": "Patel",
            "email": "jagratpatel@gail.com",
            "password": "987654"
        },
        {
            "id": 2,
            "fName": "Jaivin",
            "lName": "Barot",
            "email": "jaivinbarot@gail.com",
            "password": "123456"
        },
    ],
    "restaurant": [
        {
            "id": 0,
            "name": "Abc",
            "location": 1,
            "dishes": [0, 1]
        },
        {
            "id": 1,
            "name": "Def",
            "location": 1,
            "dishes": [0, 1, 2]
        },
        {
            "id": 2,
            "name": "Hij",
            "location": 0,
            "dishes": [0]
        },
        {
            "id": 3,
            "name": "Klm",
            "location": 2,
            "dishes": [1, 2]
        },
    ],
    "dishes": [
        {
            "id": 0,
            "name": "dish 1",
            "ingredient": ["ing1", "ing2", "ing3", "ing4"]
        },
        {
            "id": 1,
            "name": "dish 2",
            "ingredient": ["ing5", "ing2", "ing3", "ing4"]
        },
        {
            "id": 2,
            "name": "dish 3",
            "ingredient": ["ing6", "ing2", "ing4"]
        }
    ],
    "locations": [
        {
            "id": 0,
            "name": "Ahmedabad"
        },
        {
            "id": 1,
            "name": "Ahmedanagar"
        },
        {
            "id": 2,
            "name": "Gandhinagar"
        },
        {
            "id": 3,
            "name": "Gandhidham"
        },
        {
            "id": 4,
            "name": "Surat"
        }
    ]
}


'''@app.route('/')
def hello_world():
    dishes = data["dishes"]
    return render_template("index.html", dishes=dishes)'''

'''@app.route('/restaurant', methods=['GET','POST'])
def restaurantPage():
    data = {
        "name" : "Pizza house",
        "items": ["Pizza"],
        "address": "Ahmedabad",
        "time": "12:00 PM to 12:00 AM",
        "about": "Station Bar is a one-stop destination for people who want to have a fun time with their families and friends. The eye-catching colorful decor just does not ends there. We have a spectacular outdoor seating for romantic evenings."
    }
    return render_template("restaurant.html", restaurant=data)
'''
@app.route('/SignUp',methods=['GET','POST'])
def Signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        contact = request.form.get('contact')
        password = request.form.get('password')
        print(username,email)
        # listObj = []
        filename = 'Signup.json'
        with open(filename) as fp:
            listObj = json.load(fp)
        # if username in listObj['data']:
        #     print("hello world")
        #     return 'user already signed up'
            
        # else:
        #     listObj['data'].append({"Name": username,"Email": email,"Contact": contact,"Password": password})
        #     with open(filename, 'w') as json_file:
        #         # json.dump(listObj, json_file, indent=4,  separators=(',',': '))
        #         json_file.write(json.dumps(listObj))
        flag = 0
        userdata =  {}
        for user in listObj['data']:
            if username == user["Name"]:
                flag = 1
                userdata = user
        if flag == 1:
            return "user already exist"
        else:
            listObj['data'].append({"Name": username,"Email": email,"Contact": contact,"Password": password})
            with open(filename, 'w') as json_file:
                #json.dump(listObj, json_file, indent=4,  separators=(',',': '))
                json_file.write(json.dumps(listObj))
                
        
            
                
                
            
        # with open('Login.json', 'w') as f:
        #     f.write(json.dumps([{"username":username, "password":password}]))
        return render_template('Home.html')
    
    return render_template('SignUp.html')
 
@app.route('/SignIn',methods=['GET','POST'])
def Signin():
    if request.method == 'POST':
        username = request.form.get('username')
        # email = request.form.get('email')
        # contact = request.form.get('contact')
        password = request.form.get('password')
        print(username,password)
        # listObj = []
        filename = 'Signup.json'
        with open(filename) as fp:
            listObj = json.load(fp)
        
        
        flag = 0
        userdata =  {}
        for user in listObj['data']:
            if username == user["Name"]:
                flag = 1
                userdata = user
        if flag == 1:
            if username == user["Name"] and  password == user["Password"]:
                print("Login successful")
                return render_template('Home.html')
                    
            elif username == user["Name"] and  password != user["Password"]:
                print("User and pass dont match")
                return "username and password don't match"
            else:
                print("Authentication error")
                return "Authenticatin error"
            
        
        else:
            print("user not exist")
            return "user doesn't exist, please signup first"
        
        return render_template('Home.html')
    
    return render_template('SignIn.html')
     
    

@app.route('/users', methods=['GET', 'POST'])
def userFetch():
    if(request.method == 'GET'):
        user_Id = request.args.get('userId')
        userArr = [user if user["id"] ==
                   int(user_Id) else 0 for user in data["users"]]
        user = {}
        for i in userArr:
            if i != 0:
                user = i
        return jsonify(user)


@app.route('/location', methods=['GET', 'POST'])
def locationFetch():
    if(request.method == 'GET'):
        loc_name = request.args.get('name')
        locArr = [loc if loc_name.lower() in loc["name"].lower()
                  else 0 for loc in data["locations"]]
        loc = {"data": []}
        for i in locArr:
            if i != 0:
                loc["data"].append(i)
        return jsonify(loc)
    

with open('restaurant.json', 'r') as json_file:
	json_load = json.load(json_file)
 
restaurant1 = json_load['restaurant1']
restaurant2 = json_load['restaurant2']
restaurant3 = json_load['restaurant3']
restaurant4 = json_load['restaurant4']
restaurant5 = json_load['restaurant5']



@app.route('/empDetails')
def method_name():
	return jsonify(restaurant1)



@app.route('/res1')
def res1():
    return render_template('restaurant.html',restaurant=restaurant1)

@app.route('/res2')
def res2():
    return render_template('restaurant.html',restaurant=restaurant2)

@app.route('/res3')
def res3():
    return render_template('restaurant.html',restaurant=restaurant3)

@app.route('/res4')
def res4():
    return render_template('restaurant.html',restaurant=restaurant4)  

@app.route('/res5')
def res5():
    return render_template('restaurant.html',restaurant=restaurant5) 

    
@app.route('/', methods=['GET', 'POST'])
def Home():
    return render_template("Home.html")

@app.route('/Offer', methods=['GET', 'POST'])
def Offer():
    return render_template("Offer.html")

@app.route('/Search', methods=['GET', 'POST'])
def Search():
    return render_template("Search.html")

@app.route('/Blog', methods=['GET', 'POST'])
def Blog():
    return render_template("Blog.html")
# @app.route('/SignUp', methods=['GET', 'POST'])
# def SignUp():
#     return render_template("SignUp.html")
    


if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = 8000)

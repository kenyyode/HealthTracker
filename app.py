from flask import Flask, jsonify, request, render_template 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

class User (db.Model):
    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column (db.String(20), unique=False)
    weight = db.Column(db.Integer(), unique=False)
    height = db.Column (db.Integer(), unique=False)
    Bmi = db.Column (db.Integer(), unique=False)
    
    def __repr__(self):
        return f"<weight {self.name}>"
    
@app.route("/")
def home():
    return jsonify(message="Welcome to the Health tracker backend")
@app.route("/api/weights", methods=["POST", "GET"])
def add_weight ():
    if request.method == "POST":
        data = request.get_json()
    
        if "name" in data and "weight" in data and "height" in data:
            name = data["name"]
            weight = data["weight"]
            height = data["height"]
            Bmi = weight / (height * height)
            user_data = User(weight=weight, name=name, height=height, Bmi=Bmi)
            db.session.add(user_data)
            db.session.commit()
            return jsonify(message="User added sucessfully")
        
    
        else: 
            return jsonify(message="User data was not succesfully added")
    if request.method == "GET":
        users = User.query.all()
        user_data = [{"name": user.name, "weight": user.weight, "height": user.height, "Bmi":user.Bmi} for user in users]
        return jsonify(users=user_data)
    else: 
        return jsonify (message="No User Data Found")
    
    

if __name__ ==  "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port= 9090)

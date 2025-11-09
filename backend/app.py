# Backend REST API for Mood Input, Recipe Retrieval, Feedback Submission
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = 'SimpleCache'
cache = Cache(app)
db = SQLAlchemy(app)

# Database Models
class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mood_id = db.Column(db.Integer, db.ForeignKey('mood.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/moods', methods=['GET'])
@cache.cached(timeout=60)
def get_moods():
    moods = Mood.query.all()
    return jsonify([{'id': m.id, 'name': m.name} for m in moods])

@app.route('/recipes/<int:mood_id>', methods=['GET'])
@cache.cached(timeout=60)
def get_recipes_by_mood(mood_id):
    recipes = Recipe.query.filter_by(mood_id=mood_id).all()
    return jsonify([{'id': r.id, 'name': r.name, 'description': r.description} for r in recipes])

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    if not data or 'recipe_id' not in data or 'rating' not in data:
        return jsonify({'error': 'Invalid feedback data'}), 400
    feedback = Feedback(recipe_id=data['recipe_id'], rating=data['rating'], comment=data.get('comment'))
    db.session.add(feedback)
    db.session.commit()
    return jsonify({'message': 'Feedback submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')

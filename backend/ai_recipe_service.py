# AI-driven personalized recipe generation service - SCRUM-165

from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Dummy recipes database
recipes = [
    {'id': 1, 'name': 'Spaghetti Bolognese', 'base': 'pasta'},
    {'id': 2, 'name': 'Mango Smoothie', 'base': 'smoothie'},
    {'id': 3, 'name': 'Avocado Salad', 'base': 'salad'},
    {'id': 4, 'name': 'Chicken Curry', 'base': 'curry'}
]

@app.route('/ai_recipe', methods=['POST'])
def ai_recipe():
    data = request.json
    mood = data.get('mood')
    user_preferences = data.get('preferences', {})

    # Simplistic AI mock: pick random recipe influenced by mood
    random.seed(mood)  # Deterministic for demo
    selected = random.choice(recipes)
    
    personalized_recipe = {
        'name': selected['name'],
        'description': f"A personalized {selected['base']} recipe for mood: {mood}"
    }

    return jsonify(personalized_recipe)

if __name__ == '__main__':
    app.run(debug=True)

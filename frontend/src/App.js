import React, { useState, useEffect } from 'react';

function App() {
  const [moods, setMoods] = useState([]);
  const [selectedMood, setSelectedMood] = useState(null);
  const [recipes, setRecipes] = useState([]);
  const [feedbacks, setFeedbacks] = useState({});

  useEffect(() => {
    async function fetchMoods() {
      const res = await fetch('/moods');
      const data = await res.json();
      setMoods(data);
    }
    fetchMoods();
  }, []);

  useEffect(() => {
    async function fetchRecipes() {
      if (selectedMood) {
        const res = await fetch(`/recipes/${selectedMood}`);
        const data = await res.json();
        setRecipes(data);
      } else {
        setRecipes([]);
      }
    }
    fetchRecipes();
  }, [selectedMood]);

  const handleSubmitFeedback = async (recipeId, rating, comment) => {
    await fetch('/feedback', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({recipe_id: recipeId, rating, comment})
    });
    setFeedbacks({...feedbacks, [recipeId]: {rating, comment}});
  };

  return (
    <div>
      <h1>Mood-Based Recipe Recommendations</h1>
      <section>
        <h2>Choose your mood:</h2>
        {moods.map(mood => (
          <button key={mood.id} onClick={() => setSelectedMood(mood.id)}>{mood.name}</button>
        ))}
      </section>
      <section>
        <h2>Recipes:</h2>
        {recipes.length === 0 && <p>Select a mood to see recipes.</p>}
        {recipes.map(recipe => (
          <div key={recipe.id} style={{border: '1px solid black', margin: 5, padding: 5}}>
            <h3>{recipe.name}</h3>
            <p>{recipe.description}</p>
            <FeedbackForm recipeId={recipe.id} onSubmit={handleSubmitFeedback} feedback={feedbacks[recipe.id]}/>
          </div>
        ))}
      </section>
    </div>
  );
}

function FeedbackForm({recipeId, onSubmit, feedback}) {
  const [rating, setRating] = useState(feedback ? feedback.rating : 1);
  const [comment, setComment] = useState(feedback ? feedback.comment : '');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(recipeId, rating, comment);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Rating:
        <select value={rating} onChange={e => setRating(parseInt(e.target.value))}>
          {[1,2,3,4,5].map(n => <option key={n} value={n}>{n}</option>)}
        </select>
      </label>
      <br />
      <label>
        Comments:
        <input type="text" value={comment} onChange={e => setComment(e.target.value)} />
      </label>
      <br />
      <button type="submit">Submit Feedback</button>
    </form>
  );
}

export default App;

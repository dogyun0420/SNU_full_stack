from flask import Flask, render_template, request
import pandas as pd

df = pd.read_csv('netflix_titles.csv')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/About")
def about():
    return render_template("about.html", title="Hello")

# @app.route("/api")
# def api():
#     return {"message": "Hello"}

@app.route("/api")
def api():
    # Get query parameters with defaults
    year = request.args.get('release_year', type=int)
    rating = request.args.get('rating', type=str)
    content_type = request.args.get('type', type=str)
    
    # Start with the full dataset
    filtered_df = df
    
    # Apply filters if parameters are provided
    if year is not None:
        filtered_df = filtered_df[filtered_df['release_year'] == year]
    
    if rating is not None:
        filtered_df = filtered_df[filtered_df['rating'] == rating]
    
    if content_type is not None:
        filtered_df = filtered_df[filtered_df['type'] == content_type]
    
    # Convert the filtered results to a list of dictionaries
    results = filtered_df.to_dict('records')
    
    return {
        "count": len(results),
        "titles": results
    }
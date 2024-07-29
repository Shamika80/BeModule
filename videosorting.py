from flask import Flask, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]


@app.route('/videos/sorted', methods=['GET'])
def get_sorted_videos():
    sorted_titles = video_titles.copy()  
    "merge_sort"(sorted_titles)
    return jsonify({"sorted_videos": sorted_titles})


if __name__ == '__main__':
    app.run(debug=True)
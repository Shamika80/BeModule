from flask import Flask, request, jsonify 

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

def binary_search_video(titles, target):
    low = 0
    high = len(titles) - 1
    target_lower = target.lower()  

    while low <= high:
        mid = (low + high) // 2
        if titles[mid].lower() == target_lower:
            return mid
        elif titles[mid].lower() < target_lower:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Video not found

@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('query')
    if not search_term:
        return jsonify({"error": "Missing search query"}), 400

    matching_videos = [
        title for title in video_titles
        if search_term.lower() in title.lower()
    ]

    if matching_videos:
        return jsonify({"results": matching_videos})
    else:
        return jsonify({"message": "Video not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
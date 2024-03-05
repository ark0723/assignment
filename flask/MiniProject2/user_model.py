from flask import jsonify
users = [
    {
        "username": "leo",
        "posts": [{"title": "Town House", "likes": 120}]
    },
    {
        "username": "alex",
        "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]
    },
    {
        "username": "kim",
        "posts": [{"title": "Delicious Ramen", "likes": 230}]
    }
]

def add_user(data):
    new_user = {
                    "username": data['username'],
                    "posts":[]
                }
    
    users.append(new_user)
    return jsonify({"msg": f"{new_user['username']} has been created"}), 201

def add_post(username, data):
    for user in users:
        if user['username'] == username:
            new_post = {"title": data['title'], "likes": 0}
            user['posts'].append(new_post)
            return new_post, 201
    
    return jsonify({"msg": "Invalid User Name"}), 404

def get_posts(username):
    for user in users:
        if user['username'] == username:
            return jsonify({"posts": user['posts']})
    
    return jsonify({"msg": "Invalid User Name"}), 404

def like_post(username, title):
    for user in users:
        if user['username'] == username:
            selected_post = next((post for post in user['posts'] if post['title'] == title), None)
            if selected_post:
                selected_post['likes'] += 1
                return selected_post, 200
            
            else:
                return jsonify({"msg": "post not found"}), 404
            
    return jsonify({"msg": "User not found"}), 404


def delete_post(username, title):
    for user in users:
        if user['username']==username:
            delete_post = next((post for post in user['posts'] if post['title'] == title), None)
            if delete_post:
                user['posts'].remove(delete_post)
            else:
                return jsonify({"msg": "post not found"}), 404
            
    return jsonify({"msg": "user not found"}), 404

def delete_user(username):
    for user in users:
        if user['username'] == username:
            users.remove(user)
            return jsonify({"msg": f"{username} has been deleted successfully"}), 200
    return jsonify({"msg": "user not found"}), 404
    



# empty set for collecting payload of JWT
jwt_blocklist = set()

def add_to_blocklist(jti):
    jwt_blocklist.add(jti)

def remove_from_blocklist(jti):
    jwt_blocklist.discard(jti)
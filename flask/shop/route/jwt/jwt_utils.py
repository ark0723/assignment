from flask_jwt_extended import JWTManager
from shop.route.jwt.blocklist import jwt_blocklist
from flask import jsonify
import yaml

jwt = JWTManager()

def configure_jwt(app, key):
    app.config["JWT_SECRET_KEY"] = key
    jwt.init_app(app)

    # token expire time setting
    freshness_in_minutes = 1
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = freshness_in_minutes*10 # 10 min
    jwt.init_app(app)

    # 추가적인 정보를 토큰에 넣고 싶을 때 사용
    # In this app, additional_claims = {"is_admin": Boolean}
    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}
    
    # 토큰이 blocklist에 있는지 확인하는 함수, blocklist에 있으면,해당 토큰이 유효하지 않다고 판단
    # The decorated function must take two arguments.
    # The first argument is a dictionary containing the header data of the JWT.
    # The second argument is a dictionary containing the payload data of the JWT.
    # The decorated function must be return True if the token has been revoked, False otherwise.
    @jwt.token_in_blocklist_loader
    def check_token_revoked(jwt_header, jwt_payload: dict):
        return jwt_payload['jti'] in jwt_blocklist
    
    # callback function for returning a custom response when an expired JWT is encountered.
    @jwt.expired_token_loader
    def response_to_expired_token(jwt_header, jwt_payload: dict):
        return jsonify({"msg": "Token is already expired"}), 401

    # 유효하지 않은 토큰이 사용되었을 때 실행되는 함수
    # 토큰의 서명이나 구조가 유효하지 않을 때 실행됩니다. 주로 토큰 자체의 문제로 발생하는 경우에 해당합니다.
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"message": "Invalid token", "error": "invalid_token"}), 401
    
    # 해당 토큰으로 접근 권한이 없는 경우
    # The argument is a string that explains why the JWT could not be found.
    @jwt.unauthorized_loader
    def unauthorized_token_callback(error):
        return jsonify({"msg": "accessible token is required"}), 401
    
    # fresh한 토큰이 필요한데 fresh하지 않은 토큰이 사용되었을 때 실행되는 함수를 정의합니다. 
    # 해당 응답을 반환하여 fresh한 토큰이 필요하다는 메시지를 전달
    # JWT_ACCESS_TOKEN_EXPIRES으로 토큰 만료 시간 조정
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "Token is not fresh.", "error": "fresh_token_required"}
            ),
            401,
        )

    # 토큰이 폐기되었을 때 실행되는 함수를
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "Token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )



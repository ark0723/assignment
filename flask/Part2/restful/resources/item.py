from flask_restful import Resource
from flask import request

items = [{'name': "ruler", 'price': 500}, {'name': "pen", 'price': 1000}] # 간단 db

class Item(Resource):
    # 특정 아이템 조회
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'msg': 'item has not been found'}, 404
    
    # 아이템 생성
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {'msg': 'item already exists'}
            
        data = request.get_json()
        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)

        return new_item

    
    # 아이템 수정
    def put(self, name):
        data = request.get_json()

        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item
        # 만약 update하고자 하는 아이템 데이터가 없다면 -> 

    
    # 아이템 삭제
    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]

        return {'msg': 'item deleted'}

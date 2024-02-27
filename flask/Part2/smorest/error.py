from flask import Flask, abort

app = Flask(__name__)

@app.route("/example")
def example():
    # 어떤 조건에서 오류발생시키고 처리
    error_condition = True

    if error_condition:
        abort(500, description = "An error has been raised")

    #정상
    return "Success!"

if __name__ == "__main__":
    app.run(debug= True)
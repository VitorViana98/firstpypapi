from flask import Flask, request
from main import insertUser

app = Flask("YoutTube")


@app.route('/helloWorld', methods=['GET'])
def helloWorld():
    return {'hello': 'world'}


@app.route('/registerUser', methods=['GET'])
def register_user():

    # body = request.get_json()
    body = {}
    body['name']="nome"
    body['email']="e-mail"
    body['password']="senha"
    print("aqui",body)
    if ('name' not in body):
        return {'status': 400, 'message': 'O parametro faltando.'}

    user = insertUser(body['name'], body['email'], body['password'])

    print('user', user)

    return getResponse(200, 'User created', 'user', user)


def getResponse(status, message, content_name=False, content=False):
    response = {}
    response['status'] = status
    response['message'] = message

    if (content_name and content):
        response['content_name'] = content_name
        response['content'] = content

    return response


app.run()

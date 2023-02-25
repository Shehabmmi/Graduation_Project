import json

from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# localhost:8000/login
# POST Method

def login(request):
    if request.method != "POST":
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)

    # to convert from Json to Dictionary.
    request_body = json.loads(request.body.decode('utf-8'))

    # Validation Process
    if 'password' not in request_body:
        return JsonResponse({'message': "Password field is required"}, status=400)

    if 'email' not in request_body:
        return JsonResponse({'message': "Email field is required"}, status=400)

    # If the email is not ending with @o6u.edu.eg => Validation
    if not request_body['email'].endswith("@o6u.edu.eg"):
        return JsonResponse({'message': "Email must ending with @o6u.edu.eg"}, status=400)

    if not len(request_body['password']) > 8:
        return JsonResponse({'message': "Password field must be more than 7 letters and less than 32 letters"},
                            status=400)

    if not len(request_body['password']) < 32:
        return JsonResponse({'message': "Password field must be more than 7 letters and less than 32 letters"},
                            status=400)

    return JsonResponse({
        'message': 'successful',
        'email': request_body['email'],
        'password': request_body['password']
    })


def users(request):
    if request.method not in ["GET", "POST"]:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)

    # Getting all Users
    if request.method == 'GET':
        return JsonResponse({
            'message': "successfully",
            'data': [
                {"id": 1, "name": "Devien George"},
                {"id": 2, "name": "Shehab Mohamed"},
                {"id": 3, "name": "Ahmed"},
            ]
        })

    # Making a new User
    elif request.method == 'POST':
        # to convert from Json to Dictionary.
        request_body = json.loads(request.body.decode('utf-8'))

        return JsonResponse({
            'message': "successfully",
            'data': {
                'id': 1234,
                'email': request_body['email'],
                'password': request_body['password']
            }
        }, status=201)


def single_user(request, id):
    if request.method not in ["GET", "DELETE", 'PUT']:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)

    # Get A single User
    if request.method == "GET":
        return JsonResponse({
            'message': "successfully",
            'data': {"id": id, "name": "Devien George"},
        })

    # Deleting A User
    elif request.method == "DELETE":
        return JsonResponse({
            'message': "successfully deleted",
            'data': {
                'id': 1234,
                'email': "devo@gmail.com",
                'password': "1345678"
            }
        }, status=201)

    # Update an existing User
    elif request.method == "PUT":
        # to convert from Json to Dictionary.
        request_body = json.loads(request.body.decode('utf-8'))

        return JsonResponse({
            'message': "successfully updated",
            'data': {
                'id': id,
                'email': request_body['email'],
                'password': request_body['password']
            }
        }, status=201)

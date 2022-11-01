from app.services.helpers import HttpResponse, HttpError, HttpStatus, HttpRequest


def test_http_response():
    http_reponse = HttpResponse(status_code=200)
    http_reponse_repr = http_reponse.__repr__()
    assert http_reponse_repr == 'HttpResponse (status_code=200, body=None)'
    assert http_reponse.status_code == 200


def test_http_error():
    http_error = HttpError(status_code=400)
    http_error_repr = http_error.__repr__()
    assert http_error_repr == 'HttpError (status_code=400, message=Internal Server Error)'
    assert http_error


def test_http_status_200_ok():
    http_status = HttpStatus()
    response = http_status.ok_200(body={})
    assert response.status_code == 200


def test_http_request():
    http_request = HttpRequest()
    assert http_request.__repr__() == 'HttpRequest (header={}, body={}, query={})'
    assert http_request.body == {}
    assert http_request.header == {}
    assert http_request.query == {}

#!/usr/bin/env python3

from werkzeug.wrappers import Request, Response

@Request.application  # tells it to run any code inside the function in the browser at the location we specify in the development server ~ run_simple()
def application(request):
    print(f"This web server is running at {request.remote_addr}")
    return Response("WSGI generated this response")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple(
        hostname="localhost", 
        port=5555,
        application=application
    )
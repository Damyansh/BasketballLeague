class VisitCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        if 'visit_count' not in request.session:
            request.session['visit_count'] = 0
        request.session['visit_count'] += 1
        request.session.modified = True

        return self.get_response(request)

class LastVisitedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin'):
            request.session['last_page'] = request.path

        return self.get_response(request)


class BlockAnonymousPostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if(
            request.method == 'POST'
            and not request.user.is_authenticated
            and not request.path.startswith('/accounts/login')
            and not request.path.startswith('/accounts/register')
        ):
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("You must be logged in.")

        return self.get_response(request)

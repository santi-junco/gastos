import jwt

from django.conf import settings
from django.http.response import JsonResponse

def get_token(request):
    token = request.headers['Authorization'].split()[1]
    token_decode = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

    return token_decode


class UserPermission(object):
    """Corrobora que se este editando, obteniendo o eliminando el mismo usuario que el del token
    """
    def dispatch(self, request, *args, **kwargs):
        token = get_token(request)
        if token['user_id'] != kwargs['pk']:
            return JsonResponse({'detail':"Pagina no encontrada"}, status=404)
        
        return super().dispatch(request, *args, **kwargs)
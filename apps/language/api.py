from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.authorization import Authorization
from language.models import Language

class UserAuthorization(Authorization):
    def apply_limits(self, request, object_list):
        if request and hasattr(request, 'user'):
            return object_list.filter(username=request.user.username)
        return obejct_list.none()

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authentication = BasicAuthentication()
        authorization = UserAuthorization()

class LanguageAuthorization(Authorization):
    def apply_limits(self, request, object_list):
        if request and hasattr(request, 'user'):
            return object_list.filter(creator__username = request.user.username)
        return object_list.none()

class LanguageResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'creator')
    class Meta:
        queryset = Language.objects.all().order_by('name')
        resource_name = 'language'
        authentication = BasicAuthentication()
        authorization = LanguageAuthorization()


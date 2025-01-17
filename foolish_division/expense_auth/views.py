from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.response import Response

from foolish_division.expense_auth.serializers import NewUserSerializer, UserSerializer
from foolish_division.profiles.models import ExpenseProfile
from foolish_division.settings import DJANGO_AUTH_TOKEN_MAX_AGE_SECONDS


# Create your views here.
class UserAuthenticationViewSet(viewsets.ViewSet):

    @action(methods=["POST"], detail=False, url_name="login")
    def login(self, request):
        # FIXME push validation to serializer
        user = self.request.user
        if user and not user.is_anonymous:
            raise PermissionDenied(f"You cannot log in while logged in!")

        username = request.data.get("username")
        if not username:
            raise ValidationError("Username is required")

        password = request.data.get("password")
        if not password:
            raise ValidationError("Password is required")

        user = User.objects.get(username=username)
        is_correct_password = user.check_password(password)

        if is_correct_password:
            token, created = Token.objects.get_or_create(user=user)

        data = dict(
            token=token.key,
            **UserSerializer(user).data
        )

        res = Response(data=data)
        res.set_cookie("auth_token", token.key, max_age=DJANGO_AUTH_TOKEN_MAX_AGE_SECONDS)

        return res

    @action(methods=["POST"], detail=False, url_name="logout")
    def logout(self, request):
        # FIXME push validation to serializer
        user = self.request.user
        if user or user.is_anonymous:
            raise PermissionDenied(f"You cannot log out if not logged in!")

        token = Token.objects.get(user=user)
        token.delete()

        data = dict(
            msg="Logged out",
        )
        res = Response(data=data)
        res.set_cookie("auth_token", "LOGGED_OUT", max_age=DJANGO_AUTH_TOKEN_MAX_AGE_SECONDS)

        return Response(data=data)

    @action(methods=["POST"], detail=False, url_name="signup")
    def signup(self, request):
        user = self.request.user
        if user and not user.is_anonymous:
            raise PermissionDenied("You cannot create an account while logged in!")

        slzr = NewUserSerializer(data=request.data)
        slzr.is_valid(raise_exception=True)

        new_user = User.objects.create_user(
            username=slzr.data["username"],
            email=slzr.data["username"],
            password=slzr.data["password"],
            first_name=slzr.data["first_name"],
            last_name=slzr.data["last_name"],
        )

        default_profile = ExpenseProfile.objects.create(
            owner=new_user,
            name=f"{new_user.first_name} {new_user.last_name}",
            bio="I'm a new user!",
            primary=True,
        )

        token = Token.objects.create(user=new_user)

        data = dict(
            token=token.key,
            **UserSerializer(new_user).data
        )

        res = Response(data=data)
        res.set_cookie("auth_token", token.key, max_age=DJANGO_AUTH_TOKEN_MAX_AGE_SECONDS)

        return res

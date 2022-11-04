from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets, mixins
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.filters import SearchFilter
from reviews.models import Category, Genre, Review, Title, User

from .permissions import (AdminPermission, ModeratorPermission,
                          ReadOnlyPermission, UserIsAuthor)
from .serializers import SignupSerializer, TokenSerializer



class ModelMixinSet(CreateModelMixin, ListModelMixin,
                    DestroyModelMixin, GenericViewSet):
    pass


class CreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass




class ModelMixinSet(CreateModelMixin, ListModelMixin,
                    DestroyModelMixin, GenericViewSet):
    pass


class CreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass



class Signup(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        username = serializer.validated_data['username']
        try:
            user, _ = User.objects.get_or_create(
                email=email,
                username=username,
            )
        except IntegrityError:
            return Response(
                (
                    'Проблема в аутентификации:'
                    'Пользователь с таким username или email уже используется.'
                ),
                status=status.HTTP_400_BAD_REQUEST
            )
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            'Вы зарегистрировались на ресурсе.',
            f'Ваш код-подтверждение: {confirmation_code}',
            settings.DEFAULT_FROM_EMAIL,
            (email,),
            fail_silently=False,
        )
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class Token(APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        confirmation_code = serializer.validated_data['confirmation_code']
        user = get_object_or_404(User, username=username)
        if user.confirmation_code != confirmation_code:
            return Response(
                'Неверный код подтверждения',
                status=status.HTTP_400_BAD_REQUEST
            )
        refresh = RefreshToken.for_user(user)
        token_data = {'token': str(refresh.access_token)}
        return Response(token_data, status=status.HTTP_200_OK)




class CategoryViewSet(ModelMixinSet):
    queryset = Category.objects.all()
    serializer_class = ''' Сюда сериализатор для "категорий" '''
    permission_classes = (''' IsAdminUserOrReadOnly мои друзья питонисты используют его
                            В сливах вроде так же, проверь пожалуйста ''',)
    filter_backends = (SearchFilter, )
    search_fields = ('name', )
    lookup_field = 'slug'


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (''' Тут возможно так же как и в категориях, глянь пожалуйста''')
    filter_backends = (SearchFilter, )


class GenreViewSet(ModelMixinSet):
    queryset = Genre.objects.all()
    serializer_class = ''' Сюда сериализатор для "Жанров" '''
    permission_classes = (''' Тут возможно так же как и в категориях, глянь пожалуйста''')
    filter_backends = (SearchFilter,)
    search_fields = ('name', )
    lookup_field = 'slug'


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = ''' Сюда сериализатор для "Комментов" '''
    permission_classes = (AdminPermission, UserIsAuthor)
    '''Дим глянь пожалуйста свежим взглядом правильный ли пермишин'''

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'))
        return review.comments.all()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ''' Сюда сериализатор '''
    permission_classes = (AdminPermission, UserIsAuthor)
    '''И тут тоже посмотри пжлст'''

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        return title.reviews.all()
from django.contrib.auth.backends import ModelBackend, UserModel
from django.core.signing import Signer
from django.db.models import Q
from re import findall
from .models import Post, Image, Tag, User
from django.conf import settings



class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None


def save_image_to_post(post, images):
    for image_file in images:
        if image_file:
            Image.objects.create(post=post, image=image_file)


def save_tags_to_post(post, text):
    tags = [tag.lower() for tag in findall(r'#[\w\d_]+', text)]
    for tag in tags:
        tag_in_base, _ = Tag.objects.get_or_create(name=tag)
        post.tags.add(tag_in_base)
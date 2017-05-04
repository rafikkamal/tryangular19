from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from posts.models import Post
from accounts.api.serializers import UserDetailSerializer


class PostCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]


class PostDetailSerializer(ModelSerializer):

    #user = SerializerMethodField()
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'image',
            'title',
            'content',
            'updated',
            'timestamp',
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


post_detail_url = HyperlinkedIdentityField(view_name='posts-api:detail', lookup_field='id')


class PostListSerializer(ModelSerializer):

    url = post_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content',
            'updated',
            'timestamp',
        ]

    def get_user(self, obj):
        return str(obj.user.username)


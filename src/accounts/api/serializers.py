from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, EmailField,\
    ValidationError, CharField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


User = get_user_model()


class UserCreateSerializer(ModelSerializer):

    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'password']

        extra_kwargs = {'password': {'write_only': True}}

    # def validate(self, data):
    #
    #     email = data['email']
    #     user_qs = User.objects.filter(email)
    #
    #     if user_qs.exists():
    #         raise ValidationError("This Email is already registered")
    #
    #     return data

    def validate_email(self, value):

        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value

        user_qs = User.objects.filter(email=email2)

        if user_qs.exists():
            raise ValidationError("This Email is already registered")

        if email1 != email2:
            raise ValidationError("Emails Must Match")
        return value

    def create(self, validated_data):

        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()

        return validated_data


class UserLoginSerializer(ModelSerializer):

    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):

        user_obj = None

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not email and not username:
            raise ValidationError("A username or email is required to login.")

        user = User.objects.filter(Q(email=email) | Q(username=username)).distinct()
        #user = user.exclude(email__isnull=True).exclude(email__iexact='')

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect Password, Try again")

        data['token'] = "SOME RANDOM TOKEN"
        return data


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']

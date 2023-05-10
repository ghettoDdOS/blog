from rest_framework import serializers

from api.models import Author, Blog, Comment


class AuthorSerializer(serializers.ModelSerializer):
    registration_date = serializers.CharField(
        source="date_joined",
        read_only=True,
    )
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Check that password_confirmation is equals password_confirmation.
        """

        password = data.get("password", None)
        if password is not None and password != data["password_confirmation"]:
            raise serializers.ValidationError("Введенные пароли не совпадают")

        if "password_confirmation" in data.keys():
            del data["password_confirmation"]

        return data

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        password = validated_data.get("password", None)
        if password is not None:
            user.set_password(password)
            user.save()
        return user

    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "password_confirmation",
            "phone",
            "registration_date",
        ]
        extra_kwargs = {"password": {"write_only": True}}


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = [
            "author",
            "title",
            "content",
            "created_at",
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "author",
            "blog",
            "content",
            "created_at",
        ]

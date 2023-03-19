from datetime import date

from rest_framework import serializers

from comments.models import Post


class TextValidator:
    def __call__(self, value):
        blocked_words = ['ерунда', 'глупость', 'чепуха']
        for word in blocked_words:
            if word in value.lower():
                raise serializers.ValidationError('Запрещенные слова: ерунда, глупость, чепуха')


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[TextValidator()])

    def create(self, validated_data):
        if birthday := validated_data['author'].birthday:
            today = date.today()
            age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
            print(age)
            if age >= 18:
                return super().create(validated_data)

        raise serializers.ValidationError("Автор поста должен быть не моложе 18 лет!")

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at']

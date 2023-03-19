from datetime import date

from rest_framework import serializers

from comments.models import Post


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(validators=[AgeValidator()])

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

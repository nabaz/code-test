from rest_framework import serializers
from api.models.difference import Difference
import datetime

class DifferenceSerializer(serializers.Serializer):
    created_at = serializers.CharField(required=False)
    value = serializers.IntegerField()
    number = serializers.IntegerField(required=False)
    occurences = serializers.IntegerField(required=False)

    class Meta:
        model = Difference

    def create(self, validated_data):
        number = validated_data.pop('value')
        value = self.square_of_sum(number) - self.sum_of_square(number)
        occurences = self.occurences_count(number)
        created_at = datetime.datetime.now()

        print(validated_data)
        return Difference.objects.create(value=value, number=number, occurences=occurences)


    def update(self, instance, validated_data):
        pass

    def sum_of_square(self, number):
        return sum([i**2 for i in range(1, number+1)])

    def square_of_sum(self, number):
        return sum(range(1, number+1)) ** 2

    def occurences_count(self, number):
        count_occurences = 0
        count_result = Difference.objects.filter(number = number).count()
        if count_result > 0 :
            count_occurences = count_result + 1
        else:
            count_occurences += 1

        return count_occurences

    def validate(self, data):
        """
        Check that number between 1-100.
        """
        if data['value'] < 1 or data['value'] > 100:
            raise serializers.ValidationError("number must be between 1-100")
        return data

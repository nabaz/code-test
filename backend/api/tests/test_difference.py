from django.test import TestCase
from api.models import Difference
from api.serializers import DifferenceSerializer
import datetime
from django.db import IntegrityError
from django.db import DataError
from django.core.exceptions import ValidationError

class DifferenceTestCase(TestCase):
    def setUp(self):
        d_s = DifferenceSerializer()
        number = 11
        value = d_s.square_of_sum(number) - d_s.sum_of_square(number)
        occurences = d_s.occurences_count(number)
        created_at = datetime.datetime.now()
        Difference.objects.create(value=value, number=number, occurences=occurences)

    def test_difference_calculation_of_square_of_sum_and_sum_of_square(self):
        """check square_of_sum and sume of squares"""
        number = Difference.objects.get(number = 11)
        self.assertEqual(number.value, 3850)


    def test_all_field_need_to_be_filled_in(self):
        """all fields need to be filled in"""
        d_s = DifferenceSerializer()
        number = 11
        value = d_s.square_of_sum(number) - d_s.sum_of_square(number)
        occurences = d_s.occurences_count(number)

        with self.assertRaises(IntegrityError):
            Difference.objects.create(value=value, number=number)

    def test_number_should_be_between_1_100(self):
        d_s = DifferenceSerializer()
        number = 2000 # out of range 1-100
        value = d_s.square_of_sum(number) - d_s.sum_of_square(number)
        occurences = d_s.occurences_count(number)
        with self.assertRaises(DataError):
            Difference.objects.create(value=value, number=number, occurences=occurences)

from django.test import TestCase
# from rest_framework.test import APIRequestFactory
# Create your tests here.


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+1, 3)


# factory = APIRequestFactory()
# request = factory.post('')

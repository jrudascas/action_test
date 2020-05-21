from django.test import TestCase
#from ...app.models import ClassRoom


class TestCase1(TestCase):

 #   def setUp(self):
 #       ClassRoom.objects.create(name='Noveno Grado')
 #       ClassRoom.objects.create(name='Decimo Grado')

    def test_class_room_model(self):

  #      class_room_1 = ClassRoom.objects.get(name='Noveno Grado')
  #      class_room_2 = ClassRoom.objects.get(name='Decimo Grado')

        self.assertEqual(1, 1)

    def test_hola(self):
        self.assertEqual('Hola Mundo', 'Hola Mundo')

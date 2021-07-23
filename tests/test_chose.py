from django.test import TestCase
from django.urls import reverse
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from pokemon.models import Pokemon

User = get_user_model()

class BaseTestCasePokemon(TestCase):

    def setUp(self) -> None:
        self.created_user = User.objects.create(
                                email='test@mail.ru', username='username_test',
                                password=make_password('password', None, 'md5')
                                            )
    
        self.post = Pokemon.objects.create(
                user=self.created_user,
                pokemon="pikachu"
                )

        self.my_profile_url = reverse("profile", args=[str(self.created_user.id)])
        self.doesnt_exist_profile_url = reverse("profile", args=[str(6)])
        # self.my_profile_url = f"http://localhost:8000/my/profile/{self.created_user.id}/"

class PokemonChoseTest(BaseTestCasePokemon):

    def test_can_access_page(self):
        response = self.client.get(self.my_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'pokemon/profile.html')

    def test_chose_pokemon_success(self):
        response = self.client.get(self.my_profile_url+"?pokemon=ditto")
        self.assertEqual(response.status_code, 200)
    
    def test_chose_with_taken_pokemon(self):
        self.client.get(self.my_profile_url+"?pokemon=ditto")
        response = self.client.get(self.my_profile_url+"?pokemon=wobbuffet")
        self.assertEqual(response.status_code, 200)

    def test_profile_doesnt_exists(self):
        try:
            response = self.client.get(self.doesnt_exist_profile_url+"?pokemon=wobbuffet")
        except User.DoesNotExist: # Exception on response
            return True
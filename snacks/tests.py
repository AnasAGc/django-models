from django.test import TestCase
from django.urls import reverse
from .models import Drinks ,Snacks
from django.contrib.auth.models import User
import tempfile
# Create your tests here.
class snaksTests(TestCase):

    def test_home_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_templete(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_Detail_page(self):
        url = reverse('drinklist')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    

    
    def setUp(self):
        # Ceate  user and object for detail  Test 
        self.user=User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.image = tempfile.NamedTemporaryFile(suffix=".jpg").name
       
        self.snack=Snacks.objects.create(
            name="apple pie",
            description=" Well cooked apple pie ",
            purchaser=self.user
        )

        self.drink=Drinks.objects.create(
            name="tea",
            pruchaser=self.user,
            image=self.image ,

        )

    def test_drinks_template_page(self):

       url=reverse('drinklist')
       response=self.client.get(url)
       self.assertTemplateUsed(response, 'drinks_list.html')
       self.assertTemplateUsed(response, 'base.html')
   
    def test_drinks_detail_page(self):

        url=reverse("drinkDetail",kwargs={"pk":self.drink.pk})
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    
    def test_Snacks_detail_page(self):

        url=reverse('snack_detail',kwargs={"pk":self.snack.pk})
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_snack_detail_template(self):
        url=reverse('snack_detail',kwargs={"pk":self.snack.pk})
        response=self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_drink_detail_template(self):
        url=reverse('drinkDetail',kwargs={"pk":self.drink.pk})
        response=self.client.get(url)
        self.assertTemplateUsed(response,'drinks_detail.html')
        self.assertTemplateUsed(response, 'base.html')

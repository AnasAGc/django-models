from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class thingsTests(TestCase):
    def test_home_page_status_code(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_templete(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks_list.html')
        self.assertTemplateUsed(response, 'base.html')
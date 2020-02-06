from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        firstItem = Item()
        firstItem.text = 'The first list item'
        firstItem.save()

        secondItem = Item()
        secondItem.text = 'Item the second'
        secondItem.save()

        savedItems = Item.objects.all()
        self.assertEqual(savedItems.count(), 2)

        firstSavedItem = savedItems[0]
        secondSavedItem = savedItems[1]
        self.assertEqual(firstSavedItem.text, 'The first list item')
        self.assertEqual(secondSavedItem.text, 'Item the second')


class ListViewTest(TestCase):

    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/onlylist/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_uses_list_template(self):
        response = self.client.get('/lists/onlylist/')
        self.assertTemplateUsed(response, 'list.html')


class NewListTest(TestCase):
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/lists/new', data={'item_text': "A new list item"})

        self.assertEqual(Item.objects.count(), 1)
        newItem = Item.objects.first()
        self.assertEqual(newItem.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': "A new list item"})
        self.assertRedirects(response, '/lists/onlylist/')

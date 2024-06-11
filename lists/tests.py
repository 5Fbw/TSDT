from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item,List
# Create your tests here.
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)
class HomePageTest(TestCase):
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func,home_page)

    # def test_home_page_return_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>',html)
    #     self.assertTrue(html.endswith('</html>'))
    def test_use_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    # def test_can_save_a_POST_request(self):
    #     response = self.client.post('/',data={'item_text': 'A new list item'})
    #
    #     self.assertEqual(Item.objects.count(),1)
    #     new_item = Item.objects.first()
    #     self.assertEqual(new_item.text,"A new list item")
    #
    # def test_redirect_after_POST(self):
    #     response = self.client.post('/', data={'item_text': 'A new list item'})
    #     # self.assertIn('A new list item',response.content.decode())
    #     # self.assertTemplateUsed(response, 'home.html')
    #     self.assertEqual(response.status_code,302)
    #     self.assertEqual(response['location'],'/lists/the-new-page/')

    # def test_only_save_items_when_necessary(self):
    #     self.client.get('/')
    #     self.assertEqual(Item.objects.count(),0)

    # def test_display_all_list_items(self):
    #     Item.objects.create(text='item 1')
    #     Item.objects.create(text='item 2')
    #     response = self.client.get('/')
    #     self.assertIn('item 1',response.content.decode())
    #     self.assertIn('item 2', response.content.decode())
class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_user = List()
        list_user.save()

        first_item = Item()
        first_item.text = 'The First list item'
        first_item.list = list_user
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_user
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_user)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text,'The First list item')
        self.assertEqual(first_saved_item.list,list_user)
        self.assertEqual(second_saved_item.text,'Item the second')
        self.assertEqual(second_saved_item.list, list_user)

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response =  self.client.get('/lists/the-new-page/')
        self.assertTemplateUsed(response,'list.html')
    def test_display_all_list_items(self):
        list_user = List.objects.create()
        Item.objects.create(text='itemey 1',list=list_user)
        Item.objects.create(text='itemey 2',list=list_user)

        response = self.client.get('/lists/the-new-page/')

        self.assertContains(response,'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post('/lists/new',data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,"A new list item")

    def test_redirect_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        # self.assertIn('A new list item',response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')
        self.assertRedirects(response,'/lists/the-new-page/')
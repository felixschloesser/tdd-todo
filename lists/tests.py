from django.test import TestCase
from lists.models import Item, List


class HomeViewTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")


class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post("/lists/new", data={"item_text": "Another new list item"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "Another new list item")

    def test_redirects_after_POST(self):
        response = self.client.post(
            "/lists/new", data={"item_text": "Another new list item"}
        )
        self.assertRedirects(response, "/lists/the-only-list-in-the-world/")


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get("/lists/the-only-list-in-the-world/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_all_list_items(self):
        mylist = List.objects.create()
        Item.objects.create(text="Itemy 1", list=mylist)
        Item.objects.create(text="Itemy 2", list=mylist)
        response = self.client.get("/lists/the-only-list-in-the-world/")
        self.assertContains(response, "Itemy 1")
        self.assertContains(response, "Itemy 2")


class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        mylist = List()
        mylist.save()

        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.list = mylist
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.list = mylist
        second_item.save()

        saved_list = List.objects.get()
        self.assertEqual(saved_list, mylist)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(first_saved_item.list, mylist)
        self.assertEqual(second_saved_item.text, "Item the second")
        self.assertEqual(second_saved_item.list, mylist)

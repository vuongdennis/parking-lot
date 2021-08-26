from .models import History, Space
from .time import Time
from .ticketprice import TicketPrice
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import time

class TicketPriceTest(APITestCase):
    def test_ticket_price(self):
        self.assertEquals(TicketPrice.calculate(0), 1)
        self.assertEquals(TicketPrice.calculate(1), 2)
        self.assertEquals(TicketPrice.calculate(2), 3)
        self.assertEquals(TicketPrice.calculate(3), 4)

class TimeTests(APITestCase):
    def test_get_current_time(self):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        self.assertEquals(Time.current_time(), currentTime)     

    def test_convert_time_to_minutes(self):
        self.assertEqual(Time.time_difference_minutes('02:02:03', '2:10:59'), 8)
        self.assertEqual(Time.time_difference_minutes('12:02:03', '23:10:59'), 668)
        self.assertEqual(Time.time_difference_minutes('12:02:03', '14:10:59'), 128)
        self.assertEqual(Time.time_difference_minutes('02:02:03', '2:2:59'), 0)

class HistoryTests(APITestCase):
    def test_get_history_endpoint(self):
        url = reverse('history-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SpaceTests(APITestCase):
    def test_get_spaces_endpoint(self):
        url = reverse('spaces-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_space_post_endpoint(self):
        url = reverse('spaces-list')
        data = {'space_number': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['space_number'], 12345)

    def test_space_post_updates_history(self):
        url = reverse('spaces-list')
        data = {'space_number': '12345'}

        #should be 0 objects in history
        self.assertEqual(History.objects.count(), 0)

        response = self.client.post(url, data, format='json')

        #now there should be an object after posting to spaces
        self.assertEqual(History.objects.count(), 1)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['space_number'], 12345)

    def test_space_delete_endpoint(self):
        url = reverse('spaces-list')
        data = {'space_number': '123'}
        response = self.client.post(url, data, format='json')
        #make sure object created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Space.objects.count(), 1)

        url = reverse('spaces-detail', kwargs={'pk': response.json()['id']})
        response = self.client.delete(url)

        #check to see if deleted
        self.assertEquals(Space.objects.count(), 0)

    def test_space_put_endpoint(self):
        url = reverse('spaces-list')
        data = {'space_number': '123'}
        response = self.client.post(url, data, format='json')
        #make sure object created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Space.objects.count(), 1)

        url = reverse('spaces-detail', kwargs={'pk': response.json()['id']})
        response = self.client.put(url)
        self.assertEqual(response.json()['time_out'], Time.current_time())
        
        
        

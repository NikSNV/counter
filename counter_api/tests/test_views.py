from django.test import TestCase


class CounterViewTest(TestCase):
    def test_view_url_Countres(self):
        resp = self.client.get('/api/counters/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_CountresFilter(self):
        resp = self.client.get('/api/counters/2020-10-14/2021-10-15/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_CountresFilterclicks(self):
        resp = self.client.get('/api/counters/2020-10-14/2021-10-15/clicks')
        self.assertEqual(resp.status_code, 301)
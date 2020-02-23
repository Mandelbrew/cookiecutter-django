from django.core import mail
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.


class WadminSmokeTest(TestCase):
    def test_wadmin_returns_301(self):
        response = self.client.get('/wadmin')
        self.assertEqual(response.status_code, 301)

    def test_wadmin_redirects_to_200(self):
        response = self.client.get('/wadmin', follow=True)
        self.assertEqual(response.status_code, 200)


class BaristaSmokeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='barista',
                                                  email='barista@localhost.com',
                                                  password='secret')

    def test_login(self):
        self.assertTrue(self.client.login(username='barista', password='secret'))


class DadminSmokeTest(TestCase):
    def test_dadmin_returns_301(self):
        response = self.client.get('/dadmin')
        self.assertEqual(response.status_code, 301)

    def test_dadmin_redirects_to_200(self):
        response = self.client.get('/dadmin', follow=True)
        self.assertEqual(response.status_code, 200)


class AssetsSmokeTest(TestCase):
    def test_main_js_returns_200(self):
        response = self.client.get('/static/js/main.js')
        self.assertEqual(response.status_code, 200)

    def test_main_css_returns_200(self):
        response = self.client.get('/static/css/main.css')
        self.assertEqual(response.status_code, 200)


class EmailSmokeTest(TestCase):
    def test_send_email(self):
        mail.send_mail('Subject', 'Message', 'from@localhost.com', ['to@localhost.com'], fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject')


class HomePageTest(TestCase):
    def test_home_page_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_returns_html5(self):
        response = self.client.get('/')
        self.assertTrue(response.content.startswith(b'<!DOCTYPE HTML>'))

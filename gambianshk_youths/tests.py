from django.urls import reverse
from django.test import TestCase, LiveServerTestCase
from django.contrib.auth import get_user_model
from .models import Member, Contribution, Community, Event
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest

class AdminSiteTests(TestCase):
    def setUp(self):
        # Create a superuser for testing and log them in
        User = get_user_model()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password123'
        )
        self.client.login(username='admin', password='password123')

        # Create sample data for testing: a member and a contribution
        self.member = Member.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            phone_number='1234567890',
            gender='M'
        )
        self.contribution = Contribution.objects.create(
            member=self.member,
            contribution_type='Monthly Dues',
            amount=100.00,
            description='Monthly contribution',
            verified=True,
            published=True  # Set published to True for admin tests
        )

    def test_add_member(self):
        # Test that the admin can access the add member page
        response = self.client.get(reverse('admin:gambianshk_youths_member_add'))
        self.assertEqual(response.status_code, 200)

    def test_add_contribution(self):
        # Test that the admin can access the add contribution page
        response = self.client.get(reverse('admin:gambianshk_youths_contribution_add'))
        self.assertEqual(response.status_code, 200)

    def test_change_member(self):
        # Test that the admin can access the change member page
        response = self.client.get(reverse('admin:gambianshk_youths_member_change', args=[self.member.id]))
        self.assertEqual(response.status_code, 200)

    def test_change_contribution(self):
        # Test that the admin can access the change contribution page
        response = self.client.get(reverse('admin:gambianshk_youths_contribution_change', args=[self.contribution.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_member(self):
        # Test that the admin can delete a member
        response = self.client.post(reverse('admin:gambianshk_youths_member_delete', args=[self.member.id]), follow=True)
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertFalse(Member.objects.filter(id=self.member.id).exists())

    def test_delete_contribution(self):
        # Test that the admin can delete a contribution
        response = self.client.post(reverse('admin:gambianshk_youths_contribution_delete', args=[self.contribution.id]), follow=True)
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertFalse(Contribution.objects.filter(id=self.contribution.id).exists())
class PublicURLTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.member = Member.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            phone_number='1234567890',
            gender='M'
        )
        cls.published_contribution = Contribution.objects.create(
            member=cls.member,
            contribution_type='Donation',
            amount=50.00,
            published=True
        )
        cls.unpublished_contribution = Contribution.objects.create(
            member=cls.member,
            contribution_type='Gift',
            amount=25.00,
            published=False
        )

    def test_home_page(self):
    # Test that the CMS home page is accessible
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_member_list(self):
        response = self.client.get(reverse('gambianshk_youths:member_list'))
        self.assertEqual(response.status_code, 200)

    def test_contribution_list(self):
        response = self.client.get(reverse('gambianshk_youths:contribution_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.published_contribution.contribution_type)
        self.assertNotContains(response, self.unpublished_contribution.contribution_type)

    def test_search_results(self):
        # Test that search results are accessible
        response = self.client.get(reverse('gambianshk_youths:search_results'), {'q': 'John'})
        self.assertEqual(response.status_code, 200)

class EventTests(TestCase):
    def setUp(self):
        # Create a community and an event for testing
        self.community = Community.objects.create(
            name='Local Community',
            description='A community for local events.'
        )
        self.event = Event.objects.create(
            title='Community Gathering',
            date='2025-05-01',
            community=self.community
        )

    def test_event_creation(self):
        # Test that an event can be created successfully
        self.assertIsInstance(self.event, Event)
        self.assertEqual(self.event.title, 'Community Gathering')

class UserWorkflowsTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the Selenium WebDriver for live server tests
        super().setUpClass()
        cls.driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

    @classmethod
    def tearDownClass(cls):
        # Quit the WebDriver after tests are done
        cls.driver.quit()
        super().tearDownClass()

    def test_registration(self):
        # Test the user registration workflow
        driver = self.driver
        driver.get(f"{self.live_server_url}/register/")
        #driver.get(f"{self.live_server_url}/registration/")
        try:
            # Fill out the registration form
            driver.find_element(By.NAME, "username").send_keys("testuser")
            driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
            driver.find_element(By.NAME, "phone_number").send_keys("1234567890")
            driver.find_element(By.NAME, "gender").send_keys("Male")
            driver.find_element(By.NAME, "password").send_keys("testpassword")
            driver.find_element(By.NAME, "password2").send_keys("testpassword")
            driver.find_element(By.ID, "register-button").click()
            # driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
            # driver.find_element(By.NAME, "password").send_keys("testpassword")


            # Wait for confirmation message
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Registration successful')]"))
            )
            self.assertIn("Registration successful", driver.page_source)

        except Exception as e:
            print(f"Error during registration: {e}")
            self.fail("Registration test failed.")

    def test_login(self):
        # Test the user login workflow
        driver = self.driver
        driver.get(f"{self.live_server_url}/login/")
        try:
            # Fill out the login form
            driver.find_element(By.NAME, "username").send_keys("testuser")
            driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
            driver.find_element(By.NAME, "phone_number").send_keys("1234567890")
            driver.find_element(By.NAME, "gender").send_keys("M")  # Use value, not label
            driver.find_element(By.NAME, "password1").send_keys("testpassword")
            driver.find_element(By.NAME, "password2").send_keys("testpassword")

            # Wait for login confirmation
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome')]"))
            )
            self.assertIn("Welcome", driver.page_source)

        except Exception as e:
            print(f"Error during login: {e}")
            self.fail("Login test failed.")

    def test_contribution_submission(self):
        # Test the contribution submission workflow
        driver = self.driver
        driver.get(self.live_server_url + "/contributions/")  # Navigate to the contributions page
        try:
            # Fill out the contribution form
            driver.find_element(By.NAME, "amount").send_keys("100")
            driver.find_element(By.NAME, "contribution_type").send_keys("Donation")
            driver.find_element(By.ID, "submit-contribution").click()

            # Wait for submission confirmation
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Contribution submitted')]"))
            )
            self.assertIn("Contribution submitted", driver.page_source)

        except Exception as e:
            print(f"Error during contribution submission: {e}")
            self.fail("Contribution submission test failed.")

if __name__ == "__main__":
    unittest.main()

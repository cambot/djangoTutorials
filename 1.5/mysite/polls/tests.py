import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Poll

class PollMethodTests(TestCase):

	def test_was_published_recently_with_old_poll(self):
		# poll was published more than 1 day ago
		old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
		self.assertEqual(old_poll.was_published_recently(), False)

	def test_was_published_recently_with_recent_poll(self):
		# poll was published within the last day
		recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
		self.assertEqual(recent_poll.was_published_recently(), True)

	def test_was_published_recently_with_future_poll(self):
		# poll was published in the future
		future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_poll.was_published_recently(), False)


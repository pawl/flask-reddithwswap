import unittest
from unittest.mock import Mock

from praw.models import Submission

from heckingoodboys.media import Media


class TestMedia(unittest.TestCase):
    def test_media(self):
        submission = Mock(spec=Submission)
        submission.id = 'coh6dn'
        submission.permalink = '/r/aww/comments/coh6dn/move_mums_home/'
        submission.url = 'https://i.imgur.com/jQabPxc.gifv'
        submission.title = '"move, mums home!"'

        # TEST: media with the same title aren't allowed in a set
        media = Media(submission)
        media_2 = Media(submission)
        self.assertEqual(len({media, media_2}), 1)

        # TEST: imgur gifv is converted to mp4
        self.assertEqual(media.video_url, 'https://i.imgur.com/jQabPxc.mp4')
        self.assertIsNone(media.image_url)
        self.assertEqual(media.title, submission.title)
        self.assertEqual(media.permalink, submission.permalink)

        # TEST: imgur jpg uses thumbnail
        submission.url = 'https://imgur.com/X5Jl2xd'
        media = Media(submission)
        self.assertEqual(media.image_url, 'http://i.imgur.com/X5Jl2xdh.jpg')
        self.assertIsNone(media.video_url)

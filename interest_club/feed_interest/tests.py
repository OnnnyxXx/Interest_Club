from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import Interest_Group, GroupPost

class InterestGroupModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_interest_group_creation(self):
        """Test creating an Interest_Group instance."""
        group_picture = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        group = Interest_Group.objects.create(
            group_name='Test Group',
            group_picture=group_picture,
            group_author=self.user,
            group_info='This is a test group.'
        )
        self.assertEqual(group.group_name, 'Test Group')
        self.assertEqual(group.group_author, self.user)
        self.assertEqual(group.group_info, 'This is a test group.')
        self.assertIsNotNone(group.created_at)

    def test_interest_group_str(self):
        """Test the string representation of Interest_Group."""
        group = Interest_Group(group_name='Test Group', group_author=self.user)
        self.assertEqual(str(group), 'Test Group')


class GroupPostModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.group = Interest_Group.objects.create(
            group_name='Test Group',
            group_picture=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
            group_author=self.user
        )

    def test_group_post_creation(self):
        """Test creating a GroupPost instance."""
        post_image = SimpleUploadedFile("test_post_image.jpg", b"file_content", content_type="image/jpeg")
        post = GroupPost.objects.create(
            group=self.group,
            author=self.user,
            text='This is a test post.',
            image=post_image
        )
        self.assertEqual(post.group, self.group)
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.text, 'This is a test post.')
        self.assertIsNotNone(post.created_at)

    def test_group_post_str(self):
        """Test the string representation of GroupPost."""
        post = GroupPost(text='This is a test post.', author=self.user, group=self.group)
        self.assertEqual(str(post), 'This is a test post.')

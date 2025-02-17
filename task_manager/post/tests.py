from .serializers import PostSerializer
from django.test import TestCase, RequestFactory
from rest_framework.test import APIClient
from .models import Post


class PostSerializerTest(TestCase):
    def test_valid_serializer(self):
        post_data = {
            'title': 'Заголовок поста',
            'description': 'Описание поста',
            'author': 'Автор поста',
            'likes': 10
        }
        serializer = PostSerializer(data=post_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer_title_too_long(self):
        post_data = {
            'title': 'a' * 201,
            'description': 'Описание поста',
            'author': 'Автор поста',
            'likes': 10
        }
        serializer = PostSerializer(data=post_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_invalid_serializer_empty_title(self):
        post_data = {
            'title': '',
            'description': 'Описание поста',
            'author': 'Автор поста',
            'likes': 10
        }
        serializer = PostSerializer(data=post_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_invalid_serializer_empty_description(self):
        post_data = {
            'title': 'Заголовок поста',
            'description': '',
            'author': 'Автор поста',
            'likes': 10
        }
        serializer = PostSerializer(data=post_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('description', serializer.errors)

    def test_invalid_serializer_negative_likes(self):
        post_data = {
            'title': 'Заголовок поста',
            'description': 'Описание поста',
            'author': 'Автор поста',
            'likes': -1
        }
        serializer = PostSerializer(data=post_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('likes', serializer.errors)


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()
        self.post = Post.objects.create(
            title='Заголовок поста',
            description='Описание поста',
            author='Автор поста',
            likes=10
        )

    def test_get_post(self):
        response = self.client.get(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_put_post(self):
        updated_data = {
            'title': 'Новый заголовок',
            'description': 'Новое описание',
            'author': 'Новый автор',
            'likes': 15
        }
        response = self.client.put(f'/posts/{self.post.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Новый заголовок')
        self.assertEqual(self.post.description, 'Новое описание')
        self.assertEqual(self.post.author, 'Новый автор')
        self.assertEqual(self.post.likes, 15)

    def test_delete_post(self):
        response = self.client.delete(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())


class PostTestCase(TestCase):
    def setUp(self):
        author = 'Test Author'
        self.post = Post.objects.create(
            title='Test Post',
            description='Test Description',
            author=author,
            likes=0
        )

    def test_post_title(self):
        self.assertEqual(self.post.title, 'Test Post')

    def test_post_description(self):
        self.assertEqual(self.post.description, 'Test Description')

    def test_post_author(self):
        self.assertEqual(self.post.author, 'Test Author')

    def test_post_likes(self):
        self.assertEqual(self.post.likes, 0)

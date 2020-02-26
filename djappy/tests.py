import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Article


def create_article(test_title, test_content):

    now = timezone.now()
    article = Article(
        title=test_title,
        content=test_content,
        image="article_images/dawn.jpg",
        author_id=1,
        category_id=1,
        created_at=now,
        updated_at=now,
    )


class ArticleModelTests(TestCase):

    pass
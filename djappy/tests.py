import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Article, Category
from django.contrib.auth.models import User


def new_category(test_name):
    category= Category(
        name=test_name,
    )
    return category


def new_user(test_username, test_password):
    user = User(
      username=test_username,
      password=test_password,
    )
    return user


def new_article(test_title, test_content):

    user = new_user("testuser", "test1234")
    user.save()
    category = new_category("テストカテゴリ")
    category.save()
    now = timezone.now()
    article = Article(
        title=test_title,
        content=test_content,
        image="article_images/dawn.jpg",
        author_id=user.pk,
        category_id=category.pk,
        created_at=now,
        updated_at=now,
    )
    return article


class ArticleModelTests(TestCase):

    def test_article_can_be_saved_with_all_column_filled(self):
        """
        全てのカラムが埋まっていれば登録できる
        """
        test_title = "こんにちは"
        test_content = "よろしくお願いします"
        article = new_article(test_title, test_content)
        article.save()
        latest_article = Article.objects.latest("created_at")
        self.assertEqual(article.title, latest_article.title)

    def test_article_can_be_saved_with_title_under_255_words(self):
        """
        titleが255文字以下なら登録できる
        """
        test_title = "1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcde"
        test_content = "よろしくお願いします"
        article = new_article(test_title, test_content)
        article.save()
        latest_article = Article.objects.latest("created_at")
        self.assertEqual(article.title, latest_article.title)

    def test_article_can_not_be_saved_with_title_over_256_words(self):
        """
        titleが256文字以上だと登録できない
        """
        test_title = "1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcded"
        test_content = "よろしくお願いします"
        article = new_article(test_title, test_content)
        try:
          article.save()
        except Exception:
          self.assertTrue(True)
        else:
          self.assertTrue(False)
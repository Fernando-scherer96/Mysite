import pytest

from blog.models.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title = 'pystest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pystest with factory'
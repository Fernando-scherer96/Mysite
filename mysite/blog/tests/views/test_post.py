import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

    #import pdb; pdb.set_trace() #pdb biblioteca para debunhar o  codigo em python, para ver o que aconteceu

    #response = json.loads(response.content)

    assert response.content == b'Hello World'

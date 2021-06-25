import logging
import requests

from backend.celery import app
from django.dispatch import receiver
from django.db.models.signals import post_save

from blog.models import EntryEnvelope
from blog.serializers import EntrySerializer


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.task(name="publish_entries_if_scheduled")
def publish_entries_if_scheduled():
    entries = EntryEnvelope.objects.filter(should_publish_in_future=True)
    for entry in entries:
        now = datetime.datetime.now()
        if entry.future_publish_date < now:
            entry.published = True
            entry.publish_date = now
            entry.future_publish_processed_on = now
            entry.save()


@app.task(name="sync_to_the_code_blogs")
def sync_to_the_code_blogs(entry_envelope_id):
    ee = EntryEnvelope.objects.get(pk=entry_envelope_id)
    token = ee.author.profile.token
    data = EntrySerializer(instance=ee)

    serializer = EntrySerializer(ee)

    if ee.author.profile.url:
        headers = {'Authorization': 'Token ' + token}
        r = requests.post(ee.author.profile.url + '/api/entries/', json=serializer.data, headers=headers)

        logger.info('Saved %s to TheCodeBlogs.com', str(ee.id))
    else:
        logger.info('No URL. Did not save %s to TheCodeBlogs.com', str(ee.id))



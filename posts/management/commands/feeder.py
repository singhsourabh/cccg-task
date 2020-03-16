from django.core.management.base import BaseCommand
import xml.etree.ElementTree as ET
import os
from posts.models import Post
from itertools import islice
from django.utils.timezone import make_aware
from pytz import timezone
from datetime import datetime


class Command(BaseCommand):
    help = 'Feed the xml file in database'

    def get_ts(self, time_string):
        if not time_string:
            return None
        return make_aware(
            datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S.%f"),
            timezone=timezone('UTC'))

    def handle(self, *args, **options):
        batch_size = 100
        path = os.path.join(os.path.dirname(os.path.realpath(
            __file__)), 'data/bioinformatics_posts_se.xml')

        tree = ET.parse(path)
        root = tree.getroot()
        x = {'OwnerDisplayName', 'CreationDate', 'AcceptedAnswerId', 'Tags', 'Id',
             'AnswerCount', 'LastEditorUserId', 'LastActivityDate',
             'OwnerUserId', 'Title', 'ClosedDate', 'PostTypeId', 'ViewCount',
             'CommentCount', 'LastEditDate', 'Body', 'ParentId', 'Score', 'FavoriteCount'}

        objs = (Post(
            post_id=row.get('Id'),
            post_type_id=row.get('PostTypeId'),
            score=row.get('Score'),
            comment_count=row.get('CommentCount'),
            creation_date=self.get_ts(row.get('CreationDate')),
            last_activity_date=self.get_ts(row.get('LastActivityDate')),
            body=row.get('Body'),
            owner_user_id=row.get('OwnerUserId'),
            owner_display_name=row.get('OwnerDisplayName'),
            accepted_answer_id=row.get('AcceptedAnswerId'),
            tags=row.get('Tags'),
            answer_count=row.get('AnswerCount'),
            last_edit_user_id=row.get('LastEditorUserId'),
            title=row.get('Title'),
            closed_date=self.get_ts(row.get('ClosedDate')),
            view_count=row.get('ViewCount'),
            last_edit_date=self.get_ts(row.get('LastEditDate')),
            parent_id=row.get('ParentId'),
            favorite_count=row.get('FavoriteCount')
        ) for row in root.findall('row'))

        while True:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            Post.objects.bulk_create(batch, batch_size)

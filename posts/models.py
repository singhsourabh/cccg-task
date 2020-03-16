from django.db import models


class Post(models.Model):
    """
    required fields
    """
    post_id = models.IntegerField(primary_key=True)
    post_type_id = models.IntegerField()
    score = models.IntegerField()
    comment_count = models.IntegerField()
    creation_date = models.DateTimeField()
    last_activity_date = models.DateTimeField()
    body = models.TextField()
    owner_user_id = models.IntegerField()

    """
    optional fields
    """
    owner_display_name = models.CharField(max_length=100, null=True)
    accepted_answer_id = models.IntegerField(null=True)
    tags = models.TextField(null=True)
    answer_count = models.IntegerField(null=True)
    last_edit_user_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    closed_date = models.DateTimeField(null=True)
    view_count = models.IntegerField(null=True)
    last_edit_date = models.DateTimeField(null=True)
    parent_id = models.IntegerField(null=True)
    favorite_count = models.IntegerField(null=True)

    def __str__(self):
        return self.body[:32]

    class Meta:
        ordering = ['post_id']

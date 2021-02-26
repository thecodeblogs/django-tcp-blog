from django.db.models import QuerySet, Manager, Q

class EntriesQuerySet(QuerySet):
    def only_published(self):
        return self.filter(Q(is_published=True))
    def for_author(self, handle):
        return self.filter(author__handle=handle)
    def with_tags(self, tags):
        return self.filter(tag_set__in=tags)


class DefaultEntriesManager(Manager):
    def only_published(self):
        return self.get_queryset().only_published()

    def for_author(self, handle):
        return self.get_queryset().for_author(handle)

    def with_tags(self, tags):
        return self.get_queryset().with_tags(tags)


class CommentQuerySet(QuerySet):
    def public(self):
        return self.filter(user__profile__comments_public=True)
    # TODO: Add comment approval workflow for individual comments
    def approved(self):
        return self


class DefaultCommentManager(Manager):
    def public(self):
        return self.get_queryset().public();

    def approved(self):
        return self.get_queryset().approved();

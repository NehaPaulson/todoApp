from django.db import models


class Singer(models.Model):
    singer_name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    years_of_experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "singer"


    @staticmethod
    def create(singer_name, age, years_of_experience):
        return Singer.objects.create(
            singer_name=singer_name,
            age=age,
            years_of_experience=years_of_experience
        )

    @staticmethod
    def get_all():
        return Singer.objects.all()

    @staticmethod
    def get_one(singer_id):
        return Singer.objects.filter(id=singer_id).first()

    @staticmethod
    def get_by_name(singer_name):
        return Singer.objects.filter(singer_name=singer_name).first()

    @staticmethod
    def update(singer_id, **kwargs):
        singer = Singer.objects.filter(id=singer_id).first()
        if not singer:
            return None
        for k, v in kwargs.items():
            if v is not None:
                setattr(singer, k, v)
        singer.save()
        return singer

    @staticmethod
    def delete_one(singer_id):
        singer = Singer.objects.filter(id=singer_id).first()
        if not singer:
            return False
        singer.delete()
        return True

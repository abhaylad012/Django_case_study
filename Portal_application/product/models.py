from django.db import models


# Create your models here.
class product_details(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_cr_by = models.CharField(max_length=100)
    prod_name = models.CharField(max_length=100)
    prod_short = models.CharField(max_length=100)
    prod_desc = models.CharField(max_length=1000)
    prod_topic = models.CharField(max_length=100)
    prod_logo = models.ImageField(upload_to="logos")
    prod_vote = models.IntegerField(default=0)


    # prod_doc = models.FileField(upload_to="docs")
    def __str__(self):
        return self.prod_name + ": " + str(self.prod_id)

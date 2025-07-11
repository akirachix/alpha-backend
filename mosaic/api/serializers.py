from rest_framework import serializers
from transaction.models import Transaction
from design_review.models import DesignReview
class  TransactionSerializer(serializers.ModelSerializer):
      class Meta:
             model=Transaction
             fields="__all__"
class  DesignReviewSerializer(serializers.ModelSerializer):
      class Meta:
             model=DesignReview
             fields="__all__"
from catalogue.models import Design
class DesignSerializer(serializers.ModelSerializer):
       class Meta:
              model=Design
              fields="__all__"



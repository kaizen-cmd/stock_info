from rest_framework.serializers import SerializerMethodField, HyperlinkedModelSerializer
from api.models import CompanyScrip


class CompanyScripSerializer(HyperlinkedModelSerializer):

    url = SerializerMethodField()

    class Meta:

        model = CompanyScrip
        fields = ("company_name", "scrip_codes", "url")
    
    def get_url(self, company):
        url = f"/company/{company.scrip_codes}"
        return url
from rest_framework.response import Response
from bsedata.bse import BSE
from bs4 import BeautifulSoup
from string import ascii_lowercase
import requests
from api.models import CompanyScrip
from django.db.models import Q
from api.serilaizer import CompanyScripSerializer
from rest_framework.decorators import api_view

def company_scraper():
    alpha = ascii_lowercase
    base_url = "https://money.rediff.com/companies/{}"
    url_list = [base_url.format(letter) for letter in alpha]

    company_scrip_list = []

    for url in url_list:

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        res = soup.find_all("table", class_="dataTable")
        for i in res:
            z = i.find_all("td")
            for k in range(len(z)):
                j = k + 1
                if j % 3 == 1:
                    company_name = z[k].find("a").text.strip()
                    d = {company_name: ""}
                if j % 3 == 2:
                    scrip_code = z[k].text.strip()
                    d[company_name] = scrip_code
                    company_scrip_list.append(d)
    
    for pair in company_scrip_list:

        for company in pair:

            CompanyScrip.objects.create(company_name=company, scrip_codes=pair[company])

@api_view(["GET"])
def get_info(request, query):
    queries = query.split()
    queryset = CompanyScrip.objects.filter(company_name__contains=queries[0])
    serialized_scrip_codes = CompanyScripSerializer(queryset, many=True)
    return Response(serialized_scrip_codes.data)

@api_view(["GET"])
def get_stats(request, scrip_code):

    b = BSE()
    return Response(b.getQuote(str(scrip_code)))
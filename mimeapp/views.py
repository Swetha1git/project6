from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
data="""<table>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>1000$</td>
  </tr>
</table>
"""
class HtmlView(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")
class XmlView(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")
class ExcelView(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/vmd.ms-excel")
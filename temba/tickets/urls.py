from django.conf.urls import include, url

from .models import Ticketer, TicketFolder
from .views import TicketCRUDL, TicketerCRUDL

# build up all the type specific urls
service_urls = []
for ticketer_type in Ticketer.get_types():
    urls = ticketer_type.get_urls()
    for u in urls:
        u.name = "tickets.types.%s.%s" % (ticketer_type.slug, u.name)

    if urls:
        service_urls.append(url("^%s/" % ticketer_type.slug, include(urls)))

urlpatterns = [
    url(r"^", include(TicketCRUDL().as_urlpatterns())),
    url(r"^", include(TicketerCRUDL().as_urlpatterns())),
    url(r"^tickets/types/", include(service_urls)),
    url(rf"^ticket/(?P<folder>{'|'.join(TicketFolder.all().keys())})/$", TicketCRUDL.List.as_view()),
    url(
        rf"^ticket/(?P<folder>{'|'.join(TicketFolder.all().keys())})/(?P<status>open|closed)/$",
        TicketCRUDL.List.as_view(),
    ),
    url(
        rf"^ticket/(?P<folder>{'|'.join(TicketFolder.all().keys())})/(?P<status>open|closed)/(?P<uuid>[a-z0-9\-]+)/$",
        TicketCRUDL.List.as_view(),
    ),
]

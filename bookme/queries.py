from posts.models import Host, Traveller, Apartment, Roomtype, Rent

bulk = Apartment(name='The Tiras Scandinavian Apartment', help_text='Scandi')
bulk.save()

bulk = Apartment(name='Renovated Loft in the City Center', help_text='Loft')
bulk.save()

bulk = Apartment(name='Renovated Odessa Apartment', help_text='Loft')
bulk.save()

Apartment.summary.filter(headline__startswith='Center')



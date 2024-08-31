from django.utils import timezone
from .models import Visitor, VisitorCount
import geoip2.database
from geoip2.errors import AddressNotFoundError, GeoIP2Error
import os
from django.conf import settings

class VisitorCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Utilisation du chemin dynamique pour le fichier GeoIP
        db_path = os.path.join(settings.BASE_DIR, 'GeoLite2-City.mmdb')
        self.reader = geoip2.database.Reader(db_path)

    def __call__(self, request):
        if not request.session.get('counted'):
            ip_address = self.get_client_ip(request)
            today = timezone.now().date()

            country, city = self.get_geo_info(ip_address)

            Visitor.objects.create(ip_address=ip_address, country=country, city=city)

            visitor_count, created = VisitorCount.objects.get_or_create(date=today)
            visitor_count.count += 1
            visitor_count.save()

            request.session['counted'] = True

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_geo_info(self, ip_address):
        try:
            response = self.reader.city(ip_address)
            country = response.country.name
            city = response.city.name
            return country, city
        except AddressNotFoundError:
            return None, None
        except GeoIP2Error as e:
            # Log the error or handle it as needed
            print(f"GeoIP2 error: {e}")
            return None, None

    def __del__(self):
        self.reader.close()

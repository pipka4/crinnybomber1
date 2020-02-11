from service import Service


class OnTaxi(Service):
    async def run(self):        
        await self.post(
            "https://ontaxi.com.ua/api/v2/web/client",
            json={
                "country": self.country_codes[self.phone_code].upper(),
                "phone": self.phone,
            },
        )

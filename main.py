from fastapi import FastAPI, Request
import httpx

app = FastAPI()

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1377242254309331024/PJJG2LeXaSyN9Z5oWNNA-nwk9g1p4jODfOW5a4UHaDjp8ngLT5wYltv_3-deLX6jcr3j"

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("value1")  # IFTTT domyślnie wysyła jako value1/value2/value3

    async with httpx.AsyncClient() as client:
        # Tłumaczenie przez LibreTranslate
        res = await client.post("https://libretranslate.de/translate", json={
            "q": message,
            "source": "auto",
            "target": "pl",
            "format": "text"
        })
        translated = res.json()["translatedText"]

        # Wysyłanie na Discord
        await client.post(DISCORD_WEBHOOK_URL, json={"content": translated})

    return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI()

OUTLOOKS = [
    {
        "title": "CYRUSFX COMMUNITY | WEEKLY OUTLOOK",
        "message": "A NEW WEEK. A FRESH BATTLEFIELD. Stay disciplined. Stay patient. TRADING IS AN ART."
    }
]

TRADES = [
    {
        "pair": "GBPNZD",
        "direction": "LONG",
        "status": "Triggered",
        "sl": "2.27898",
        "tp1": "2.30000",
        "tp2": "2.30856",
        "analysis": "Price reacted from the Previous Week's Low (PWL) with bullish confluence."
    }
]


@app.get("/")
def home():
    return {
        "project": "CYRUSFX Backend",
        "status": "running"
    }


@app.get("/outlooks")
def outlooks():
    return OUTLOOKS


@app.get("/trades")
def trades():
    return TRADES

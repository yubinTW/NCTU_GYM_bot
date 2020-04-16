# NCTU GYM bot
Telegram bot for query NCTU GYM count

## Before you run this bot

### Setup env

* Install Python 3
* Install `pipenv`
```
$ pip install pipenv
```
* Install deps
```
$ pipenv install
```

### set token
```
cp config.json.sample config.json
vim config.json
# paste your bot token
```

### Run the bot

```
$ pipenv run python3 ./app/main.py
```

## Run with docker
```
cd TTR06_bot
docker build -t team6-server .
docker run --name team6-server -d team6-server
```

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

### Set Token
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
cd NCTU_GYM_bot
docker build -t nctu_gym_bot .
docker run --name nctu_gym_bot -d nctu_gym_bot
```

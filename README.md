# Google Play Crawler

A crawler that crawls all applications' data from the Google Play and save it to MongoDB.

## Requirements
- Python 3
- MongoDB
  Please Follow the [MongoDB Manual](https://docs.mongodb.com/manual/installation/)

## Usage

```
git clone https://github.com/yaoandy107/google_play_crawler.git
cd google_play_crawler
pip3 install -r requirements.txt
scrapy crawl google
```

> If you want to switch the language of Google Play, you could go to change the `Accept-Language` in `setting.py`.
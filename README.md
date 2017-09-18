### news

scrapy demo

```bash
$ scrapy startproject news
$ cd news
$ scrapyd
$ scrapyd-deploy dp-news -p news
```

list deployed spiders

```bash
$ curl http://localhost:6800/listspiders.json?project=news
```

output -> {"spiders": ["baidu", "qq", "wangyi"], "status": "ok", "node_name": "bogon"}

run spider

```bash
$ curl http://localhost:6800/schedule.json -d project=news -d spider=baidu
```

output -> {"jobid": "442f265e9c6411e7b39df079600a9c58", "status": "ok", "node_name": "bogon"}
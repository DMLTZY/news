### news

$ scrapy startproject news
$ cd news
$ scrapyd
$ scrapyd-deploy dp-news -p news

查看部署的spiders
$ curl http://localhost:6800/listspiders.json?project=news
{"spiders": ["baidu", "qq", "wangyi"], "status": "ok", "node_name": "bogon"}

启动spider
$ curl http://localhost:6800/schedule.json -d project=news -d spider=baidu
{"jobid": "442f265e9c6411e7b39df079600a9c58", "status": "ok", "node_name": "bogon"}
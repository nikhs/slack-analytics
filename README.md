## Simple Slack Analytics

Analyses slack user list and generates a simple [GeoChart](https://developers.google.com/chart/interactive/docs/gallery/geochart) showing users from different timezones. 

Will need to be redesigned since it's just a hack-job. Was created to checkout Slack API and requests package.

###Dependencies

* SQLite3
* Python requests package

```bash
pip install requests
```
###Usage

* Obtain Slack token for your team. (Available [here](https://api.slack.com/web))
* Create an SQLite3 database with the given schema.

```bash
sqlite3 <db_name>  < slack_schema.sql
``` 

* Create config.py based on sample_config.py with your token and db name.
* Run main.py

### TODO
1. Redesign
2. TEST
3. Implement as a webapp, possibly with FLASK or DJANGO
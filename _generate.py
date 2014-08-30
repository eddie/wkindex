# -*- coding: utf-8 -*-
import json
from jinja2 import Environment, FileSystemLoader
import logging

log = logging.getLogger(__name__)

with open("api/full.json", 'r') as f:
  apps = json.loads(f.read())

env = Environment(loader=FileSystemLoader('_templates'))

for app in apps:
  _platforms_parsed = []
  _platforms = ["ios", "android", "windows-phone", "windows", "osx", "linux"]

  if "browser" in app['platform']:
    _platforms_parsed.append("firefox")
    _platforms_parsed.append("chrome")
    _platforms_parsed.append("opera")
    _platforms_parsed.append("safari")
    _platforms_parsed.append("ie")
  else:
    _platforms.append("firefox")
    _platforms.append("chrome")
    _platforms.append("opera")
    _platforms.append("safari")
    _platforms.append("ie")

  for platform in _platforms:
    if platform in app['platform'].keys():
      _platforms_parsed.append(platform)

  app['_platforms_parsed'] = _platforms_parsed

index = env.get_template('index.html').render(apps=apps).encode("utf-8")

with open("index.html", 'w') as f:
  f.write(index)

app_template = env.get_template('app.html')

for app in apps:
  page = app_template.render(app=app).encode("utf-8")
  with open("apps/%s.html" % app['id'], 'w') as f:
    f.write(page)

about = env.get_template('about.html').render().encode("utf-8")
with open("about.html", 'w') as f:
  f.write(about)
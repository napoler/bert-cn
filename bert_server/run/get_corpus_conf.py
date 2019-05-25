# coding: utf-8

# Define buildargs for cse api

BUILDARGS = {
  'serviceName': 'customsearch',
  'version': 'v1',
  'developerKey': 'AIzaSyBqjfgcWEdMse4ghRYrbib8qv7avHFrp2Y'
}

# Define cseargs for search
CSEARGS = {
  'q': '柯基犬',
  'cx': '007397120899702103013:roufggcacti',
#   'num': 30
}
PROXIES = [{
      'http': '127.0.0.1:43285',
      'https': '127.0.0.1:43285',
}]
PATH="/home/terry/pan/github/bert/book/"
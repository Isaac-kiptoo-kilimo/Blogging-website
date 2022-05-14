import urllib.request,json
from .models import Quote
# Getting api key
api_key = None

base_url = None

def configure_request(app):
    global api_key,base_url
    api_key=app.config['BLOG_API_KEY']
    base_url = app.config['BLOG_API_BASE_URL']


def get_blogs():
    get_blogs_url=base_url
    print("base",get_blogs_url)
    try:
        with urllib.request.urlopen(get_blogs_url) as url:
            get_blogs_data = url.read()
            # print(get_blogs_data)
            get_blogs_respone =json.loads(get_blogs_data)

            # print(get_blogs_respone)
            blogs_results = None
            if get_blogs_respone: 
                blogs_results = process(get_blogs_respone)
            return blogs_results

    except urllib.error.URLError as e:
        print("HTTP ERROR: ", e)
    

def process(blogs_list):
    blogs_results = []
    for blogs_item in blogs_list:
        id = blogs_item.get('id')
        author = blogs_item.get('author')
        quote=blogs_item.get('quote')
        permalink=blogs_item.get('permalink')
        blogs_object =Quote(id,author,quote,permalink)
        blogs_results.append(blogs_object)
    return blogs_results

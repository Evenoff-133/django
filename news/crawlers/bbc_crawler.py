from datetime import datetime
from slugify import slugify
from requests_html import HTMLSession
from django.utils.timezone import make_aware
from concurrent.futures import ThreadPoolExecutor
from news.models import Article, Author, Category


# BBC Author in DB = 3
author = Author.objects.get(id=3)
# articles = []


def crawl_one(url):
    with HTMLSession() as session:
        response = session.get(url)

    name = response.html.xpath('//h1')[0].text
    content = response.html.xpath('//article//p')
    image_url = response.html.xpath('//figure//img/@src')[0]
    pub_date = response.html.xpath('//time/@datetime')
    cats = response.html.xpath('//*[@id="main-content"]/div[5]/div/div[1]/article/section[1]/div/div[2]/ul/li')

    my_content = ''
    short_description = ''

    for element in content:
        my_content += f'<{element.tag}>' + element.text + f'<{element.tag}>'
        if len(short_description) < 200:
            short_description += element.text + ' '

    image_name = slugify(name)
    img_type = image_url.split('.')[-1]
    img_path = f'images/{image_name}.{img_type}'

    with open(f'media/{img_path}', 'wb') as f:
        with HTMLSession() as session:
            response = session.get(image_url)
            f.write(response.content)

    pub_date = datetime.strptime(pub_date[0][0:10], '%Y-%m-%d')
    categories = []

    for cat in cats:
        categories.append(
            {
                'name': cat.text.strip(),
                'slug': slugify(cat.text)
            }
        )

    article = {
        'name': name,
        'slug': slugify(name),
        'content': my_content,
        'short_description': short_description.strip(),
        'main_image': image_url,
        'pub_date': make_aware(pub_date),
        'author': author,
    }

    # article = Article(**article)
    # articles.Append(article)

    article, created = Article.objects.get_or_create(**article)

    for category in categories:
        cat, created = Category.objects.get_or_create(**category)
        article.categories.add(cat)

    print(article)


def get_fresh_news():
    base_url = 'https://www.bbc.com/news/technology'
    with HTMLSession() as session:
        response = session.get(base_url)

    links = response.html.absolute_links

    fresh_news = []

    for link in links:
        try:
            if link.split('-')[-1].isdigit():
                fresh_news.append(link)
        except:
            pass

    return fresh_news


def run():
    # Article.objects.all().delete()
    fresh_news = get_fresh_news()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(crawl_one, fresh_news)

    # Article.objects.bulk_create(articles, ignore_conflicts=True)


if __name__ == '__main__':
    run()


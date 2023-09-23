from facebook_scraper import get_posts

for post in get_posts('pfbid02CtmzYj3xUkWyQkTYnLK2sAj91FLPGJ1q3mh2ckhkqTjBbVpBmcdUcsxXfX3nmsLal', pages=100):
    print(post['text'][:50])

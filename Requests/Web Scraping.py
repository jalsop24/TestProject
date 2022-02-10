import requests


r = requests.get('https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/others_3/kirby_30th_anniversary/H2x1_Kirby30thAnniversary_image500w.jpg')

with open('kirby.png', 'wb') as f:
    f.write(r.content)


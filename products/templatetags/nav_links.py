from django import template

register = template.Library()

@register.simple_tag
def get_nav_links():
    links = [
        # ('/bags','Bags'),
        ('jansport','Jansport'),
        ('sprayground','Sprayground'),
        ('accessories','Accessories'),
        ('luggage','Luggage'),
        ('other','Other Products'),
        ('findus','Find Us'),

    ]
    return links

@register.simple_tag()
def get_sub_brands():
    sub_links = [
            ('big-student', 'Big Student'),
            ('black-label', 'Black Label'),
            ('superbreak', 'Superbreak'),
            ('high-stakes', 'High Stakes'),
            ('digibreak', 'DigiBreak'),
            ('exposed', 'Exposed'),
            ('super-fx', 'Super FX'),
            ('right-pack', 'Right Pack'),
            ('bento-box', 'Bento Box')
    ]

    return sub_links

@register.simple_tag()
def get_types():
    types = [
        ('TR', 'Trolley Bags'),
        ('PB', 'Pencil Cases'),
        ('TB', 'Tote Bags'),
        ('MB', 'Messenger Bags'),
        ('DF', 'Duffle Bags'),
    ]

    return types

@register.simple_tag()
def get_brands():
    brands = [
        ('SL', 'Slazenger'),
        ('AL', 'Alentino'),
        ('SS', 'Samsonite'),
        ('HS', 'High Sierra'),
        ('WI', 'Wilson'),
    ]

    return brands

@register.simple_tag()
def get_insta_photos():
    photos = [
        ('https://www.instagram.com/p/BnpTuFkFTgM/', 'main/jansport_gaffati.jpg'),
        ('https://www.instagram.com/p/BrOGmpKBRW_/', 'main/sprayground1.jpg'),
        ('https://www.instagram.com/p/Bj5P9iYhPn9/', 'main/jansport1.jpg'),
        ('https://www.instagram.com/p/BiXV2arBUeX', 'main/jansport2.jpg'),
        ('https://www.instagram.com/p/BSTt9PGFodE/', 'main/easter.jpg'),
        ('https://www.instagram.com/p/BrOpj-7htrF/', 'main/sprayground2.jpg'),
        ('https://www.instagram.com/p/BGwenUjt30B/', 'main/jansport3.jpg'),
        ('https://www.instagram.com/p/BrOpuWdBk_h/', 'main/sprayground3.jpg'),

    ]

    return photos
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:08:51 2018

@author: carol
"""
# from model_utils import Choices


CATEGORY = (
    ('Accesories', (
            ('sheets', 'Sheets'),
            ('sponge', 'Sponge'),
            )),
    ('Skin Care', (
            ('bodycream', 'Body cream'),
            ('bodyscrub', 'Body scrub'),
            ('bodywash', 'Body wash'),
            ('eyecream', 'Eye cream'),
            ('facecream', 'Face cream'),
            ('faceprimer', 'Face primer'),
            ('facescrub', 'Face scrub'),
            ('handcream', 'Hand cream'),
            ('lipbalm', 'Lip balm'),
            ('makeupremover', 'Makeup remover'),
            ('mask', 'Mask'),
            ('serum', 'Serum'),
            ('shampoo', 'Shampoo'),
            ('soap', 'Soap'),
            ('sunblock', 'Sun block'),
            ('thermalwater', 'Thermal water'),
            ('toninglotion', 'Toning lotion'),
            )),
    ('Nail Polish', (
            ('basecoat', 'Base coat'),
            ('color', 'Color'),
            ('topcoat', 'Top coat'),
            )),
    ('Make Up', (
            ('blush', 'Blush'),
            ('bronzer', 'Bronzer'),
            ('brow', 'Brow'),
            ('concealer', 'Concealer'),
            ('eyeliner', 'Eye liner'),
            ('eyeprimer', 'Eye primer'),
            ('eyeshadowpds', 'Eye shadow palette Drugstore'),
            ('eyeshadowphe', 'Eye shadow palette High end'),
            ('eyeshadowsds', 'Eye shadow single Drugstore'),
            ('eyeshadowshe', 'Eye shadow single High end'),
            ('foundation', 'Foundation'),
            ('gloss', 'Gloss'),
            ('highlighter', 'Highlighter'),
            ('lipliner', 'Lip liner'),
            ('lipstick', 'Lipstick'),
            ('mascara', 'Mascara'),
            ('paletteds', 'Palette Drugstore'),
            ('palettehe', 'Palette High end'),
            ('powder', 'Powder'),
            ('tint', 'Tint'),
            )),
    ('Parfum', (
            ('bodysplash', 'Body splash'),
            ('toilette', 'Eau de Toilette'),
            ('parfum', 'Eau de Parfum'),
            )),
)

#CAT = Choices(
#        ('Accesories', ['Sheets',
#                        'Sponge']),
#        ('Skin Care', ['Body cream',
#                       'Body scrub',
#                       'Body wash',
#                       'Eye cream',
#                       'Face cream',
#                       'Face primer',
#                       'Face scrub',
#                       'Hand cream',
#                       'Lip balm',
#                       'Makeup remover',
#                       'Mask',
#                       'Serum',
#                       'Shampoo',
#                       'Soap',
#                       'Sun block',
#                       'Thermal water',
#                       'Toning lotion']),
#        ('Nail Polish', ['Color',
#                         'Base coat',
#                         'Top coat']),
#        ('Make Up', ['Blush',
#                     'Bronzer',
#                     'Brow',
#                     'Concealer',
#                     'Eye liner',
#                     'Eye primer',
#                     'Eye shadow palette Drugstore',
#                     'Eye shadow palette High end',
#                     'Eye shadow single Drugstore',
#                     'Eye shadow single High end',
#                     'Foundation',
#                     'Gloss',
#                     'Highlighter',
#                     'Lip liner',
#                     'Lipstick',
#                     'Mascara',
#                     'Palette Drugstore',
#                     'Palette High end',
#                     'Powder',
#                     'Tint']),
#        ('Parfum', ['Body splash',
#                    'Eau de toilette',
#                    'Eau de parfum']),
#
#        )

FINISH = (
    ('crack', 'Crack'),
    ('creme', 'Creme'),
    ('cremeglitter', 'Creme glitter'),
    ('duochrome', 'Duochrome'),
    ('flakies', 'Flakies'),
    ('glassflecks', 'Glass flecks'),
    ('glitter', 'Glitter'),
    ('holographic', 'Holographic'),
    ('jelly', 'Jelly'),
    ('matte', 'Matte'),
    ('metal', 'Metal'),
    ('mirror', 'Mirror'),
    ('neon', 'Neon'),
    ('pearl', 'Pearl'),
    ('sandy', 'Sandy'),
    ('satin', 'Satin'),
    ('shimmer', 'Shimmer'),
)

COLOR = (
    ('beige', 'Beige'),
    ('black', 'Black'),
    ('blue', 'Blue'),
    ('bordeaux', 'Bordeaux'),
    ('brown', 'Brown'),
    ('clear', 'Clear'),
    ('copper', 'Copper'),
    ('gold', 'Gold'),
    ('green', 'Green'),
    ('grey', 'Grey'),
    ('lightblue', 'Lightblue'),
    ('mix', 'Mix'),
    ('orange', 'Orange'),
    ('pink', 'Pink'),
    ('red', 'Red'),
    ('silver', 'Silver'),
    ('violet', 'Violet'),
    ('white', 'White'),
    ('yellow', 'Yellow')
)

CURRENCY = (
    ('ARS', 'Argentina Peso'),
    ('BRL', 'Brazil Real'),
    ('CLP', 'Chilean Peso'),
    ('USD', 'United States Dollar'),
    ('UYU', 'Uruguay Peso')
)

QUALITY = (
    ('5', 'Excellent'),
    ('4', 'Really good'),
    ('3', 'Good'),
    ('2', 'Poor'),
    ('1', 'Awful')
)

STATUS = (
    ('1', 'Published'),
    ('0', 'Draft')
)

ACCESORIES = [x[0] for x in CATEGORY[0][1]]
SKINCARE = [x[0] for x in CATEGORY[1][1]]
NAILPOLISH = [x[0] for x in CATEGORY[2][1]]
MAKEUP = [x[0] for x in CATEGORY[3][1]]
PARFUM = [x[0] for x in CATEGORY[4][1]]

GENERIC_LIST = ['beautyblogger',
                'beautyblog',
                'beauty',
                'bblogger'
                ]

ACCESORIES_LIST = ['accesories',
                   'accesorios']

SKINCARE_LIST = ['skincare',
                 'face',
                 'hautpflege',
                 'skincareroutine',
                 'moisturizer']

NAILPOLISH_LIST = ['nailpolish',
                   'esmalte',
                   'swatch',
                   'nails',
                   'notd',
                   'npa',
                   'nagel',
                   'nageln',
                   'polishaholic',
                   'instanails',
                   'nailjunkie',
                   'nailstagram',
                   'nailswag',
                   'nailporn',
                   'nailsoftheday',
                   'nailgasm',
                   'nagellack',
                   'nailpro',
                   'nails2inspire',
                   'nailsdone']

MAKEUP_LIST = ['makeup',
               'maquillaje',
               'makeupaddict',
               'makeupjunkie',
               'mua',
               'makeuplover',
               'makeupaholic',
               'makeupcollection',
               'makeupporn']

PARFUM_LIST = ['parfum',
               'perfume',
               'fragance']

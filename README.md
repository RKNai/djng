djng
====

Práctica 1

Django web aplication.

- Adrià Martí Olivart
- Iván Merola Teixidó

Public REPO: https://github.com/adriamarti/djng

This database contains and distribute the different relations between all the characters desired in the book series A Song of Ice and Fire, by George RR Martin.

Implemented in REST model, every user can easily find any character, place, castle or house in this DB, and any registered user can CREATE/MODIFY/DELETE any of these.

By implementing REST, every URL, like .../characters/,  contain every single character created in the DB, as if .../characters/character.id contains information about that specific character, house, place or castle.

2.0:

We added some user modifications, such as the possibility to only delete/modify any of the models that that user created, not any user.

We added an autocomplete option in the civil state of a character, which we pick'em up from a local JSON file.

We added too another autocomplete field in the real place from users. This time we obtain remotely the possible options from an extern web service.



Last database admin user: 

    User: admin
    Pass: 1234


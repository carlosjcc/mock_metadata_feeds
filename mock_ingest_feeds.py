"""
How to run
$ export FLASK_APP=fake_netflix_feed export FLASK_ENV=development flask run
"""

from flask import Flask, request, Response

import json

app = Flask(__name__)

prime_meta_data = [
    # episode
    {
        "episodeInfo":{
            "seasonId":"amzn1.dv.gti.1fe0b28d-d646-4936-a0c9-6f1270a5ef25:AU",
            "episodeNumber":2,
            "seasonNumber":1,
            "seriesId":"amzn1.dv.gti.397a0b0e-391a-4257-95b7-9b26e43df1d2:AU",
            "isVam":False
        },
        "ratings":[
            {
                "system":"amr",
                "value":"all"
            },
            {
                "system":"ncs",
                "value":"g"
            }
        ],
        "externalIds":[
            {
                "type":"gti",
                "value":"amzn1.dv.gti.5c1b6a20-8bba-4e75-bf83-bc7bf6d47199"
            },
            {
                "marketplace":331021,
                "type":"asin",
                "value":"B09HWYQ2N7"
            },
            {
                "marketplace":331051,
                "type":"asin",
                "value":"B09HXHJXGD"
            },
            {
                "marketplace":1367890,
                "type":"asin",
                "value":"B09HWXJ9CZ"
            },
            {
                "marketplace":151232,
                "type":"asin",
                "value":"B09HWWS5MC"
            }
        ],
        "contentType":"episode",
        "countriesOfOrigin":[
            
        ],
        "title":[
            {
                "locale":"en-US",
                "value":"     "
            }
        ],
        "isAdultContent":False,
        "colorSpace":[
            "SDR"
        ],
        "genres":[
            "av_genre_documentary"
        ],
        "longDescription":[
            
        ],
        "releaseDate":"2018-01-01",
        "credits":[
            {
                "locale":"en-US",
                "role":"director",
                "name":"Warwick Thornton"
            }
        ],
        "playableProperties":{
            "runtime":57,
            "subtitleLanguages":[
                
            ],
            "audioLanguages":[
                "en"
            ],
            "originalLanguages":[
                "en"
            ]
        },
        "studios":[
            {
                "locale":"en-US",
                "value":"ABC Commercial"
            }
        ],
        "images":[
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/5ba9afbe8bd0effd68d119226a1656d8ff62a0eb446f27c75ed7c3a61e4e787d.jpg",
                "type":"boxart",
                "locales":[
                    "en-US"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/43bad03af9df48d3353e84c83b1c4e4f67a86a0ba2e2ee07e8714c40945ca7e0.jpg",
                "type":"background",
                "locales":[
                    "en-US"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/6753bd0753bddfecaf152845c5fdb3f1e24f19bcf01b8eb07ff1a8cfde43f0d0.png",
                "type":"cover",
                "locales":[
                    "en-US"
                ]
            }
        ],
        "territory":"AU",
        "shortDescription":[
            {
                "locale":"en-US",
                "value":"A school principal joins forces with musical experts and best-selling musician, Guy Sebastian on a mission to transform the lives of disadvantaged Aussie kids through the power of music."
            }
        ],
        "id":"amzn1.dv.gti.5c1b6a20-8bba-4e75-bf83-bc7bf6d47199:AU"
    },
    # movie_item
    {
        "ratings":[
            {
                "system":"amr",
                "value":"16+"
            },
            {
                "system":"ncs",
                "value":"m"
            }
        ],
        "externalIds":[
            {
                "type":"gti",
                "value":"amzn1.dv.gti.9ebba2b2-ab7a-2ada-7741-ebee11a0e24f"
            },
            {
                "type":"imdb",
                "value":"tt10016180"
            },
            {
                "marketplace":331021,
                "type":"asin",
                "value":"B08V6J1P5H"
            },
            {
                "marketplace":331051,
                "type":"asin",
                "value":"B08V6WX7KS"
            },
            {
                "marketplace":771770,
                "type":"asin",
                "value":"B093XXV37P"
            },
            {
                "marketplace":526970,
                "type":"asin",
                "value":"B092Q1R2D1"
            },
            {
                "marketplace":151232,
                "type":"asin",
                "value":"B08V6ZFN4Y"
            },
            {
                "marketplace":7,
                "type":"asin",
                "value":"B08VCLSQWZ"
            },
            {
                "marketplace":35691,
                "type":"asin",
                "value":"B08Y633CCP"
            },
            {
                "marketplace":1367890,
                "type":"asin",
                "value":"B08V7HXLVY"
            },
            {
                "marketplace":5,
                "type":"asin",
                "value":"B08WYK6L79"
            },
            {
                "marketplace":328451,
                "type":"asin",
                "value":"B08YNMB47Y"
            },
            {
                "marketplace":44571,
                "type":"asin",
                "value":"B0B5VVSHKG"
            },
            {
                "marketplace":111172,
                "type":"asin",
                "value":"B08YXHPQ23"
            },
            {
                "marketplace":44551,
                "type":"asin",
                "value":"B08YMHLPGT"
            }
        ],
        "contentType":"movie",
        "countriesOfOrigin":[
            "US"
        ],
        "title":[
            {
                "locale":"it-IT",
                "value":"Fino all\u2019Ultimo Indizio"
            },
            {
                "locale":"nl-NL",
                "value":"The Little Things"
            },
            {
                "locale":"en-US",
                "value":"     "
            },
            {
                "locale":"en-CA",
                "value":"     "
            },
            {
                "locale":"pt-BR",
                "value":"Os Pequenos Vest\\xedgios"
            },
            {
                "locale":"es-ES",
                "value":"Peque\\xf1os detalles"
            },
            {
                "locale":"en-AU",
                "value":"     "
            },
            {
                "locale":"fr-FR",
                "value":"Une affaire de d\\xe9tails"
            },
            {
                "locale":"fr-CA",
                "value":"The Little Things"
            },
            {
                "locale":"es-419",
                "value":"Peque\\xf1os Secretos"
            }
        ],
        "isAdultContent":False,
        "colorSpace":[
            "SDR",
            "HDR10"
        ],
        "genres":[
            "av_genre_suspense",
            "av_genre_drama"
        ],
        "longDescription":[
            {
                "locale":"it-IT",
                "value":"Il Vice Sceriffo della Kern County, Joe \u201cDeke\u201d Deacon (Washington) viene mandato a Los Angeles per quello che doveva essere un veloce incarico di raccolta di prove. Al contrario, si trova coinvolto nella caccia al killer che sta terrorizzando la citt\\xe0. A guidare l\u2019indagine, il sergente Jim Baxter (Malek) che, colpito dall\u2019istinto di Deke, richiede il suo aiuto non ufficiale. Ma mentre danno la caccia al killer, Baxter ignora che l\u2019indagine sta riportando a galla alcune situazioni vissute in passato da Deke, svelando segreti scomodi che potrebbero mettere a repentaglio molto pi\\xf9 che il suo caso."
            },
            {
                "locale":"nl-NL",
                "value":"Hulpsheriff Joe 'Deke' Deacon (Washington) van Kern County wordt naar Los Angeles gestuurd voor wat een snelle opdracht had moeten zijn om bewijs te verzamelen. In plaats daarvan raakt hij verstrikt in de zoektocht naar een seriemoordenaar die de stad terroriseert. Het onderzoek wordt geleid door sergeant Jim Baxter (Malek) van het bureau in Los Angeles. Hij is onder de indruk van het instinct van Deke en betrekt hem onofficieel bij de jacht. Maar terwijl ze jacht maken op de moordenaar, realiseert Baxter zich niet dat het onderzoek het verleden van Deke weer bovenhaalt, inclusief verontrustende geheimen die meer kunnen bedreigen dan alleen deze zaak."
            },
            {
                "locale":"en-US",
                "value":"Kern County Deputy Sheriff Joe \u201cDeke\u201d Deacon (Washington) is sent to Los Angeles for what should have been a quick evidence\u2010gathering assignment. Instead, he becomes embroiled in the search for a serial killer who is terrorizing the city. Leading the hunt, L.A. Sheriff Department Sergeant JimBaxter (Malik), impressed with Deke\u2019s cop instincts, unofficially engages his help. But as they track the killer, Baxter is unaware that the investigation is dredging up echoes of Deke\u2019s past, uncovering disturbing secrets that could threaten more than his case."
            },
            {
                "locale":"en-CA",
                "value":"Deputy Sheriff Joe \u201cDeke\u201d Deacon (Washington) is on a search for a serial killer with Sergeant Jim Baxter (Malik), who is unaware that the investigation is dredging up Deke\u2019s past."
            },
            {
                "locale":"pt-BR",
                "value":"O delegado adjunto do condado de Kern, Joe \u201cDeke\u201d Deacon (Washington), \\xe9 enviado a Los Angeles para o que seria apenas um r\\xe1pido trabalho de recolha de provas. Em vez disso, ele acaba envolvido na busca por um serial killer que est\\xe1 aterrorizando a cidade. Liderando a busca est\\xe1 o delegado do Departamento de Pol\\xedcia de L.A., Jim Baxter (Malek), que ao se impressionar com os instintos de Deke, resolve pedir sua ajuda de forma extraoficial. Mas enquanto eles seguem os rastros do assassino, Baxter n\\xe3o sabe que a investiga\\xe7\\xe3o est\\xe1 trazendo o passado de Deke \\xe0 tona, revelando segredos perturbadores que podem amea\\xe7ar muito mais do que somente esse caso."
            },
            {
                "locale":"es-ES",
                "value":"El sheriff adjunto del condado de Kern, Joe \u201cDeke\u201d Deacon (Washington), es enviado a Los Angeles para lo que deber\\xeda ser un caso r\\xe1pido de recopilaci\\xf3n de evidencias. Sin embargo, se ve involucrado en la b\\xfasqueda de un asesino en serie que aterroriza la ciudad. Encabezando la investigaci\\xf3n se encuentra el sargento del departamento del sheriff de Los Angeles, Jim Baxter (Malek), que, impresionado por el instinto de polic\\xeda de Deke, le ayuda de manera extraoficial. Pero mientras siguen la pista al asesino, Baxter desconoce que la investigaci\\xf3n desentierra partes del pasado de Deke que sacan a la luz secretos m\\xe1s peligrosos que el propio caso."
            },
            {
                "locale":"en-AU",
                "value":"Kern County Deputy Sheriff Joe \u201cDeke\u201d Deacon (Washington) is sent to Los Angeles for what should have been a quick evidence\u2010gathering assignment. Instead, he becomes embroiled in the search for a serial killer who is terrorizing the city. Leading the hunt, L.A. Sheriff Department Sergeant JimBaxter (Malik), impressed with Deke\u2019s cop instincts, unofficially engages his help. But as they track the killer, Baxter is unaware that the investigation is dredging up echoes of Deke\u2019s past, uncovering disturbing secrets that could threaten more than his case."
            },
            {
                "locale":"fr-FR",
                "value":"Le sh\\xe9rif adjoint du comt\\xe9 de Kern, Joe \\xabDeke\\xbb Deacon (Washington) se rend \\xe0 Los Angeles pour ce qui aurait d\\xfb \\xeatre une mission rapide de collecte de preuves. Il se retrouve plut\\xf4t impliqu\\xe9 dans la recherche d'un tueur en s\\xe9rie qui terrorise la ville. Menant l'enqu\\xeate, le sergent Jim Baxter (Malek), impressionn\\xe9 par l'instinct policier de Deke, lui demande officieusement son aide. Mais alors qu'ils traquent le tueur, Baxter ignore que l'enqu\\xeate d\\xe9terre le pass\\xe9 de Deke, r\\xe9v\\xe9lant des secrets troublants qui pourraient menacer plus que son enqu\\xeate."
            },
            {
                "locale":"fr-CA",
                "value":"Le sh\\xe9rif adjoint Joe \"Deke\" Deacon (Washington) est \\xe0 la recherche d\\'un tueur en s\\xe9rie avec le sergent Jim Baxter (Malek), qui ne sait pas que l\\'enqu\\xeate r\\xe9v\\xe8le le pass\\xe9 de Deke."
            },
            {
                "locale":"es-419",
                "value":"Joe \"Deke\" Deacon (Washington), ayudante del sheriff del condado de Kern, es enviado a Los \\xc1ngeles para lo que deber\\xeda haber sido una r\\xe1pida recopilaci\\xf3n de pruebas. Pero en lugar de ello se ve envuelto en la b\\xfasqueda de un asesino en serie que aterroriza a la ciudad. El sargento del departamento del alguacil de Los \\xc1ngeles, Jim Baxter (Malek), quien encabeza la averiguaci\\xf3n, solicita la ayuda de \"Deke\" de manera extraoficial, por sus instintos policiales. Pero mientras siguen al asesino, Baxter no se da cuenta de que la investigaci\\xf3n est\\xe1 sacando a la luz ecos del pasado de \"Deke\", al revelar secretos inquietantes que podr\\xedan amenazar m\\xe1s que su caso."
            }
        ],
        "releaseDate":"2021-02-18",
        "credits":[
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"it-IT",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"it-IT",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"it-IT",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"it-IT",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"it-IT",
                "role":"producer",
                "name":"Mark Johnson"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"nl-NL",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"nl-NL",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"nl-NL",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"nl-NL",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"nl-NL",
                "role":"producer",
                "name":"Mark Johnson"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"en-US",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"en-US",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"en-US",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Mark Johnson"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"en-CA",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"en-CA",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"en-CA",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"en-CA",
                "role":"producer",
                "name":"Mark Johnson"
            },
            {
                "locale":"en-CA",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"pt-BR",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"pt-BR",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"pt-BR",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"pt-BR",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"pt-BR",
                "role":"producer",
                "name":"Mark Johnson"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"es-ES",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"es-ES",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"es-ES",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"es-ES",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"es-ES",
                "role":"producer",
                "name":"Mark Johnson"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"en-AU",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"en-AU",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"en-AU",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"en-AU",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"en-AU",
                "role":"producer",
                "name":"Mark Johnson"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"fr-FR",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"fr-FR",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"fr-FR",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"fr-FR",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"fr-FR",
                "role":"producer",
                "name":"Mark Johnson"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"fr-CA",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"fr-CA",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"fr-CA",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"fr-CA",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"fr-CA",
                "role":"producer",
                "name":"Mark Johnson"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Denzel Washington"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Rami Malek"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Jared Leto"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Chris Bauer"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Michael Hyatt"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Terry Kinney"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Natalie Morales"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Isabel Arraiza"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Joris Jarsky"
            },
            {
                "locale":"es-419",
                "role":"actor",
                "name":"Glenn Morshower"
            },
            {
                "locale":"es-419",
                "role":"writer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"es-419",
                "role":"director",
                "name":"John Lee Hancock"
            },
            {
                "locale":"es-419",
                "role":"producer",
                "name":"John Lee Hancock"
            },
            {
                "locale":"es-419",
                "role":"producer",
                "name":"Mark Johnson"
            }
        ],
        "playableProperties":{
            "runtime":127,
            "subtitleLanguages":[
                "es-419",
                "fr-fr",
                "es-es",
                "en-us",
                "nl-nl",
                "pt-br",
                "it-it"
            ],
            "audioLanguages":[
                "es-es",
                "it-it",
                "es-419",
                "en-us",
                "pt-br",
                "fr-fr"
            ],
            "audioFormats":[
                "5.1"
            ],
            "originalLanguages":[
                "en-US"
            ]
        },
        "studios":[
            {
                "locale":"en-US",
                "value":"Warner Bros."
            }
        ],
        "images":[
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/6f5b3ea6722981f4caf62b253156ed643681ba3ad466b83dd3937f4c1f9ad873.png",
                "type":"background",
                "locales":[
                    "en-US"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/0286361ff2663ac523939c9a1c0cd582673e4da27b23d391b33419125338d6b0.jpg",
                "type":"boxart",
                "locales":[
                    "fr-FR"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/104347781af760b494f89007c37a5454db402fd16058f2e51900bf30e6b71d9a.jpg",
                "type":"boxart",
                "locales":[
                    "pt-BR"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/92e91dc709c60c23969a9ff7b442a642eec7f38a6022a1580f2b11bab4cd8021.jpg",
                "type":"boxart",
                "locales":[
                    "es-419"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/d245ab16e2beade6702587ce2ed9d5b7c7a602d51e23fbc718243d193264d64a.jpg",
                "type":"boxart",
                "locales":[
                    "en-US",
                    "en-CA",
                    "en-AU",
                    "fr-CA"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/d63bdb6b3528075c35ef1d4b6cb52cba654f5f316b33ab0287ff78a07c9fe76d.jpg",
                "type":"boxart",
                "locales":[
                    "es-ES"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/5e6f7b0a1d9e9750bb64689d6fefb84e293b4bf9868ca68443c8bf7ccf517d42.jpg",
                "type":"cover",
                "locales":[
                    "es-ES"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/981a24c95244dc6d3c96789febd356b3b916cdd0df929c7e5ecb2aae48c5be8d.jpg",
                "type":"cover",
                "locales":[
                    "en-US",
                    "en-AU"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/99f9810355d6b658efa255015924f2f2b201f0bbae60d00dfc9df22cdd2f6762.jpg",
                "type":"cover",
                "locales":[
                    "pt-BR"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/bb5f3db9800c111a621b02216605abc65586e6a955e6dc5921b5c42257e3836f.jpg",
                "type":"cover",
                "locales":[
                    "nl-NL"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/d2933678af7c092b19b33237fc50f11881df64f2e1cfc2174c01e639d8f57011.jpg",
                "type":"cover",
                "locales":[
                    "es-419"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/d96630eca2c60afcf98c845f2b509d9d98cd14ac27f06052cce7a6f536f6e691.jpg",
                "type":"cover",
                "locales":[
                    "fr-FR"
                ]
            }
        ],
        "territory":"AU",
        "shortDescription":[
            {
                "locale":"it-IT",
                "value":"Il Vice Sceriffo Joe \"Deke\" Deacon (Washington) \\xe8 sulle tracce di un serial killer con il sergente Jim Baxter (Malek). Ma le indagini portano alla luce un segreto del passato di Deke."
            },
            {
                "locale":"nl-NL",
                "value":"Hulpsheriff Joe 'Deke' Deacon (Washington) jaagt samen met sergeant Jim Baxter (Malek) op een seriemoordenaar. Baxter realiseert zich alleen niet dat Deke's verleden zo weer bovenkomt."
            },
            {
                "locale":"en-US",
                "value":"Deputy Sheriff Joe \u201cDeke\u201d Deacon (Washington) is on a search for a serial killer with Sergeant Jim Baxter (Malik), who is unaware that the investigation is dredging up Deke\u2019s past."
            },
            {
                "locale":"en-CA",
                "value":"Deputy Sheriff Joe \u201cDeke\u201d Deacon (Washington) is on a search for a serial killer with Sergeant Jim Baxter (Malik), who is unaware that the investigation is dredging up Deke\u2019s past."
            },
            {
                "locale":"pt-BR",
                "value":"O delegado adjunto Joe \u201cDeke\u201d Deacon (Washington) procura por um serial killer com o delegado Jim Baxter (Malek), que n\\xe3o sabe que a investiga\\xe7\\xe3o est\\xe1 trazendo o passado de Deke \\xe0 tona."
            },
            {
                "locale":"es-ES",
                "value":"El sheriff adjunto Joe \u201cDeke\u201d Deacon (Washington) y el sargento Jim Baxter (Malek) investigan a un asesino en serie. Baxter no sabe que el caso est\\xe1 relacionado con el pasado de Deke."
            },
            {
                "locale":"en-AU",
                "value":"Deputy Sheriff Joe \u201cDeke\u201d Deacon (Washington) is on a search for a serial killer with Sergeant Jim Baxter (Malik), who is unaware that the investigation is dredging up Deke\u2019s past."
            },
            {
                "locale":"fr-FR",
                "value":"Le sh\\xe9rif adjoint Joe \"Deke\" Deacon (Washington) est \\xe0 la recherche d\\'un tueur en s\\xe9rie avec le sergent Jim Baxter (Malek), qui ne sait pas que l\\'enqu\\xeate r\\xe9v\\xe8le le pass\\xe9 de Deke."
            },
            {
                "locale":"fr-CA",
                "value":"Le sh\\xe9rif adjoint Joe \"Deke\" Deacon (Washington) est \\xe0 la recherche d\\'un tueur en s\\xe9rie avec le sergent Jim Baxter (Malek), qui ne sait pas que l\\'enqu\\xeate r\\xe9v\\xe8le le pass\\xe9 de Deke."
            },
            {
                "locale":"es-419",
                "value":"El ayudante del sheriff, Joe \"Deke\" Deacon (Washington), busca a un asesino junto con el sargento Jim Baxter (Malek), quien ignora que la investigaci\\xf3n revelar\\xe1 el pasado de Deacon."
            }
        ],
        "id":"amzn1.dv.gti.9ebba2b2-ab7a-2ada-7741-ebee11a0e24f:AU"
    },
    # season_item
    {
        "ratings":[
            {
                "system":"amr",
                "value":"18+"
            },
            {
                "system":"ncs",
                "value":"m"
            }
        ],
        "externalIds":[
            {
                "type":"gti",
                "value":"amzn1.dv.gti.20d22792-ca6d-40b6-8892-d291c6e2efa8"
            },
            {
                "marketplace":331021,
                "type":"asin",
                "value":"B09MZNVPWT"
            },
            {
                "marketplace":331051,
                "type":"asin",
                "value":"B09MZQCPR5"
            },
            {
                "marketplace":151232,
                "type":"asin",
                "value":"B09MZP33BK"
            },
            {
                "marketplace":7,
                "type":"asin",
                "value":"B09MZX6J4G"
            },
            {
                "marketplace":35691,
                "type":"asin",
                "value":"B09MZWYQCC"
            },
            {
                "marketplace":1367890,
                "type":"asin",
                "value":"B09MZN19WN"
            },
            {
                "marketplace":704403121,
                "type":"asin",
                "value":"B09X4R3TWJ"
            },
            {
                "marketplace":5,
                "type":"asin",
                "value":"B09MZXGBPF"
            },
            {
                "marketplace":328451,
                "type":"asin",
                "value":"B09MZVT2TF"
            },
            {
                "marketplace":44571,
                "type":"asin",
                "value":"B09RDYS98Y"
            },
            {
                "marketplace":111172,
                "type":"asin",
                "value":"B09MZWZXG4"
            },
            {
                "marketplace":44551,
                "type":"asin",
                "value":"B09MZVC7MJ"
            }
        ],
        "contentType":"season",
        "countriesOfOrigin":[
            
        ],
        "title":[
            {
                "locale":"en-US",
                "value":"     "
            }
        ],
        "isAdultContent":False,
        "colorSpace":[
            "SDR"
        ],
        "genres":[
            "av_genre_unscripted",
            "av_subgenre_unscripted_crime"
        ],
        "longDescription":[
            
        ],
        "releaseDate":"2021-12-03",
        "credits":[
            
        ],
        "studios":[
            {
                "locale":"en-US",
                "value":"O2"
            }
        ],
        "images":[
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/1abc79fac66a7e6b4bdb42a0e00a03f70c44c1243c750f767fd85bc9844d6d6e.jpg",
                "type":"background",
                "locales":[
                    "en-US"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/a0e9b17c752476d8379316fe3cea2b0ba1e52f105ea8254049e3ec52b5933240.jpg",
                "type":"boxart",
                "locales":[
                    "en-US"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/3fecb864365861a4003ae81590c72e631e0832dc280f41779e8651a9b3fcefc6.jpg",
                "type":"cover",
                "locales":[
                    "en-US"
                ]
            }
        ],
        "territory":"AU",
        "shortDescription":[
            {
                "locale":"en-US",
                "value":"Family Massacre is a gripping and powerful exploration of some of the most ruthless murders ever committed. This series follows the true and gruesome tales of the unthinkable."
            }
        ],
        "id":"amzn1.dv.gti.20d22792-ca6d-40b6-8892-d291c6e2efa8:AU",
        "seasonInfo":{
            "seriesId":"amzn1.dv.gti.5625faae-13c0-4986-8906-e45a89f2cf0e:AU",
            "seasonNumber":1
        }
    },
    # series_item
    {
        "ratings":[
            {
                "system":"amr",
                "value":"18+"
            }
        ],
        "externalIds":[
            {
                "type":"gti",
                "value":"amzn1.dv.gti.d8b9fe5e-9ecc-252c-a64a-3b617e5e699a"
            },
            {
                "type":"imdb",
                "value":"tt6059298"
            },
            {
                "marketplace":331021,
                "type":"asin",
                "value":"B08G1V1BV1"
            },
            {
                "marketplace":331051,
                "type":"asin",
                "value":"B08G1TRKHT"
            },
            {
                "marketplace":1367890,
                "type":"asin",
                "value":"B08G1R5Z7H"
            },
            {
                "marketplace":151232,
                "type":"asin",
                "value":"B08G1WD43N"
            }
        ],
        "contentType":"series",
        "countriesOfOrigin":[
            
        ],
        "title":[
            {
                "locale":"de-DE",
                "value":"Rob & Chyna"
            },
            {
                "locale":"en-US",
                "value":"     "
            },
            {
                "locale":"en-GB",
                "value":"     "
            }
        ],
        "isAdultContent":False,
        "colorSpace":[
            "SDR"
        ],
        "genres":[
            "av_genre_unscripted",
            "av_genre_documentary",
            "av_subgenre_documentary_art_entertainment_and_culture",
            "av_genre_kids",
            "av_subgenre_kids_family"
        ],
        "longDescription":[
            {
                "locale":"en-GB",
                "value":"He\\'s the famous brother of Kim, Kourtney and Khlo\\xe9. She\\'s a high-profile model, music video performer and entrepreneur. Since they began dating in early 2016, their budding romance has made headlines around the world. Now, Rob Kardashian and Black Chyna are engaged, expecting their first child, and offering viewers a look inside their relationship in a revealing docuseries. \"Rob & Chyna\" follows the celebrity couple as they begin their life together and get ready to welcome a new addition to the Kardashian family."
            }
        ],
        "releaseDate":"2016-09-11",
        "credits":[
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Benton Bohannon"
            },
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Chris Conway"
            },
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Pam Daniels"
            },
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Farnaz Farjam"
            },
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Sunny Franklin"
            },
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Jeff Jenkins"
            },
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Kris Jenner"
            },
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Kim Kardashian"
            },
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Khlo\\xe9 Kardashian"
            },
            {
                "locale":"de-DE",
                "role":"producer",
                "name":"Kourtney Kardashian"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Benton Bohannon"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Chris Conway"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Pam Daniels"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Farnaz Farjam"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Sunny Franklin"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Jeff Jenkins"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Kris Jenner"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Kim Kardashian"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Khlo\\xe9 Kardashian"
            },
            {
                "locale":"en-US",
                "role":"producer",
                "name":"Kourtney Kardashian"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Benton Bohannon"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Chris Conway"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Pam Daniels"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Farnaz Farjam"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Sunny Franklin"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Jeff Jenkins"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Kris Jenner"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Kim Kardashian"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Khlo\\xe9 Kardashian"
            },
            {
                "locale":"en-GB",
                "role":"producer",
                "name":"Kourtney Kardashian"
            }
        ],
        "studios":[
            {
                "locale":"en-US",
                "value":"E!"
            },
            {
                "locale":"en-GB",
                "value":"NBCUniversal"
            }
        ],
        "images":[
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/90a294bedaaad647d933e976dccf85fc90a404ddcf85a2866f73e32df149cd2d.jpg",
                "type":"background",
                "locales":[
                    "en-US"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/ba31ccd93c698bc1dfc643fc76e75f540dad82a071967affbb4df6986b102d48.jpg",
                "type":"background",
                "locales":[
                    "en-GB"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/2d3b89420297f3063065ffadcc94bad1f72459f41162d857107721289c2fd397.jpg",
                "type":"boxart",
                "locales":[
                    "en-GB"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/532f40877d3b52aa45a242f537f2170728c34462f526b8d8fa0cfb3501ffe0bc.jpg",
                "type":"boxart",
                "locales":[
                    "en-US"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/df007e569e23e090e35661c77326c700c39d5434de017bb94a6a3fe854cc96c9.jpg",
                "type":"boxart",
                "locales":[
                    "de-DE"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/3cc9e0797cbe826ae9f7008fc28997fceb24acb7d33e9d83f1a2991ed8f0e5a6.jpg",
                "type":"cover",
                "locales":[
                    "de-DE"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/47401f6a53d9e9cbe5dc43bb0dfe93e7e15f774abde8d73d9a94a9c14ea0bbef.jpg",
                "type":"cover",
                "locales":[
                    "en-US"
                ]
            },
            {
                "url":"https://m.media-amazon.com/images/S/pv-target-images/a50a17927585f77ade0cae7781baaf0c98b8336d9a6e5190f7a9c96b45a964cc.jpg",
                "type":"cover",
                "locales":[
                    "en-GB"
                ]
            }
        ],
        "territory":"AU",
        "shortDescription":[
            {
                "locale":"de-DE",
                "value":"Follow the whirlwind romance of Rob Kardashian and Blac Chyna, from their engagement to Chyna's pregnancy, and everything in between."
            },
            {
                "locale":"en-US",
                "value":"Follow the whirlwind romance of Rob Kardashian and Blac Chyna, from their engagement to Chyna's pregnancy, and everything in between."
            },
            {
                "locale":"en-GB",
                "value":"Follow the whirlwind romance of Rob Kardashian and Blac Chyna, from their engagement to Chyna's pregnancy, and everything in between."
            }
        ],
        "id":"amzn1.dv.gti.d8b9fe5e-9ecc-252c-a64a-3b617e5e699a:AU"
    }
]

prime_offers_data = [
]

amazon_feed_data = {
    "metadata": ["http://127.0.0.1:5000/prime/meta"],
    "offers": ["http://127.0.0.1:5000/prime/offers"]
}


tenaa_data = {
    "action": "queryVideoFeed",
    "resultSize": 1000,
    "itemCount": 0,
    "itemList": [
        {
            # bad episode | No title
            "seriesTitle": "The Late Show with Stephen Colbert",
            "cbsShowId": 61456254,
            "genre": "Talk",
            "rating": "",
            "brand": "CBS",
            "seasonNum": "8",
            "episodeNum": "1",
            "contentId": "3lW2IJ59bQGal9VsDQ9eksQ5BRFhGGB4",
            "title": "    ",
            "description": "Among the classified documents seized by the F.B.I. at Mar-a-Lago was material on a foreign nation's nuclear capabilities, and former presidential advisor Steve Bannon is facing state indictment in New York. #Colbert #Comedy #Monologue ",
            "duration": 611,
            "thumbnailSet": [
                {
                    "url": "https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2022/09/08/2070200899657/COLBERT_1304_CLIP2_EARLYMONO_2CH_MEZZ_MPX_CAN_1622294_1920x1080.jpg",
                    "assetType": "Thumbnail",
                    "width": 1920,
                    "height": 1080
                },
                {
                    "url": "https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2022/09/08/2070200899657/COLBERT_1304_CLIP2_EARLYMONO_2CH_MEZZ_MPX_CAN_1622295_vr_cs_224x126_7_88.jpg",
                    "assetType": "ThumbSheet",
                    "width": 19712,
                    "height": 126
                }
            ],
            "airDate": 1662608100000,
            "deepLinkUrl": "pplusintl://shows/the-late-show-with-stephen-colbert/video/3lW2IJ59bQGal9VsDQ9eksQ5BRFhGGB4/how-do-we-explain-this-to-our-allies-justice-is-coming-for-steve-bannon?campaign=",
            "url": "http://www.paramountplus.com/video/rNUlnuJSfMKnuZ9Pm9LkXk5zV0E3MnE_",
            "mediaId": 2070241347519,
            "fetchShowLogo": "http://wwwimage-intl.pplusstatic.com/base/files/show_asset/10/91/49/show_asset_2e99c06a-78e2-47f3-a573-418bef73e6aa.jpg",
        },
        {
            # bad episode | No SeriesTitle
            "seriesTitle": "   ",
            "cbsShowId": 61456254,
            "genre": "Talk",
            "rating": "",
            "brand": "CBS",
            "seasonNum": "8",
            "episodeNum": "1",
            "contentId": "3lW2IJ59bQGal9VsDQ9eksQ5BRFhGGB4",
            "title": "How Do We Explain This To Our Allies? | Justice Is Coming For Steve Bannon",
            "description": "Among the classified documents seized by the F.B.I. at Mar-a-Lago was material on a foreign nation's nuclear capabilities, and former presidential advisor Steve Bannon is facing state indictment in New York. #Colbert #Comedy #Monologue ",
            "duration": 611,
            "thumbnailSet": [
                {
                    "url": "https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2022/09/08/2070200899657/COLBERT_1304_CLIP2_EARLYMONO_2CH_MEZZ_MPX_CAN_1622294_1920x1080.jpg",
                    "assetType": "Thumbnail",
                    "width": 1920,
                    "height": 1080
                },
                {
                    "url": "https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2022/09/08/2070200899657/COLBERT_1304_CLIP2_EARLYMONO_2CH_MEZZ_MPX_CAN_1622295_vr_cs_224x126_7_88.jpg",
                    "assetType": "ThumbSheet",
                    "width": 19712,
                    "height": 126
                }
            ],
            "airDate": 1662608100000,
            "deepLinkUrl": "pplusintl://shows/the-late-show-with-stephen-colbert/video/3lW2IJ59bQGal9VsDQ9eksQ5BRFhGGB4/how-do-we-explain-this-to-our-allies-justice-is-coming-for-steve-bannon?campaign=",
            "url": "http://www.paramountplus.com/video/rNUlnuJSfMKnuZ9Pm9LkXk5zV0E3MnE_",
            "mediaId": 2070241347519,
            "fetchShowLogo": "http://wwwimage-intl.pplusstatic.com/base/files/show_asset/10/91/49/show_asset_2e99c06a-78e2-47f3-a573-418bef73e6aa.jpg",
        },
        {
            # good episode
            "seriesTitle":"The Bridge Australia",
            "cbsShowId":62466547,
            "genre":"",
            "rating":"m l",
            "brand":"",
            "seasonNum":"1",
            "episodeNum":"5",
            "contentId":"Iaf51bsRspR_pZGQa0KXqW9PDmPxhy8O",
            "title":"The Bridge Australia - The Betrayal",
            "description":"As the ten remaining builders struggle to finish the bridge, a betrayal happens and the bridge... goes up in flames. Who was it? Why did they do it? Where was the opportunity for sabotaging the bridge? (M - L-Coarse language)",
            "duration":3242,
            "thumbnailSet":[
                {
                    "url":"https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2022/08/12/2061278275897/PPPAR_BRIDGEAUTHE_105_1583924_1920x1080.jpg",
                    "assetType":"Thumbnail",
                    "width":1920,
                    "height":1080
                },
                {
                    "url":"https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2022/08/12/2061278275897/PPPAR_BRIDGEAUTHE_105_1583929_vr_cs_224x126_15_217.jpg",
                    "assetType":"ThumbSheet",
                    "width":48608,
                    "height":126
                }
            ],
            "airDate":1662091200000,
            "deepLinkUrl":"pplusintl://shows/the-bridge-australia/video/Iaf51bsRspR_pZGQa0KXqW9PDmPxhy8O/the-bridge-australia-the-betrayal?campaign=",
            "url":"shows/the-bridge-australia/video/Iaf51bsRspR_pZGQa0KXqW9PDmPxhy8O/the-bridge-australia-the-betrayal",
            "mediaId":2061290051624,
            "fetchShowLogo":"http://wwwimage-intl.pplusstatic.com/base/files/show_asset/63/83/98/show_asset_7301857e-4013-43b5-b5ad-fce72066826a.jpg",
        },
        {
            # bad movie
            # "title": "American Gigolo | SHOWTIME Original | Official Trailer",
            "title": "   ",
            "genre": "",
            "rating": "",
            "description": "American Gigolo, a present-day reimagining of the iconic 1980 film, follows Julian Kaye (Jon Bernthal) after his wrongful conviction release from 15 years in prison as he navigates his complicated relationships with his former lover Michelle (Gretchen Mol), his troubled mother, and the people who betrayed him. While Julian struggles to reconcile the escort he was in the past and the man he is today, Detective Sunday (Rosie O'Donnell) seeks the truth about the murder that sent Julian to prison all those years ago, unearthing a much larger conspiracy along the way. ",
            "duration": 420,
            "thumbnailSet": [
                {
                    "url": "https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2022/09/07/2070014019883/B22-43799-ADV01_2590_1620819_1920x1080.jpg",
                    "assetType": "Thumbnail",
                    "width": 1920,
                    "height": 1080
                },
                {
                    "url": "https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2022/09/07/2070014019883/B22-43799-ADV01_1620820_vr_cs_224x126_7_16.jpg",
                    "assetType": "ThumbSheet",
                    "width": 3584,
                    "height": 126
                }
            ],
            "contentId": "rNUlnuJSfMKnuZ9Pm9LkXk5zV0E3MnE_",
            "cbsShowId": -1,
            "url": "movies/last-bus/nNu5EAJnT30DWrWtTV3x3Je2kw9h41uz",
            "airDate":1630033200000,
        },
        {
            # good movie
            "title":"The Last Bus",
            "genre":"",
            "rating":"m a",
            "description":"Heart-warming tale of an old man whose wife has just passed away.  With his free local bus pass he travels to the other end of the UK, where they originally moved from, on a nostalgic trip but also carrying his wife's ashes in a small suitcase. (M - A-Adult themes and/or dangerous stunts)",
            "duration":5157,
            "contentId":"nNu5EAJnT30DWrWtTV3x3Je2kw9h41uz",
            "thumbnailSet":[
                {
                    "url":"https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2021/11/30/1979175491914/PPPAR_LASTBUS_MOVIE_1057288_1920x1080.jpg",
                    "assetType":"Thumbnail",
                    "width":1920,
                    "height":1080
                },
                {
                    "url":"https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2021/11/30/1979175491914/PPPAR_LASTBUS_MOVIE_1057293_vr_cs_224x126_30_172.jpg",
                    "assetType":"ThumbSheet",
                    "width":38528,
                    "height":126
                }
            ],
            "deepLinkUrl":"pplusintl://movies/last-bus/nNu5EAJnT30DWrWtTV3x3Je2kw9h41uz?campaign=",
            "airDate":1630033200000,
            "mediaId":1979262531539,
            "cbsShowId":-1,
            "url": "movies/last-bus/nNu5EAJnT30DWrWtTV3x3Je2kw9h41uz"
        }

    ]
}

tenaa_data['itemCount'] = len(tenaa_data["itemList"])

netflix_check_feed = {
    "data": [
        {
            'etag': 'xxx',
            'url': "http://127.0.0.1:5000/netflix/data",
            'name': 'en-AU.json'
        }
    ]
}


netflix_data_feed = [
    {
        'is_original': False,
        'locale': 'en-AU',
        'originalTitle': 'Death Becomes Her',
        'pvid': '0o6CfLly08rZdmknvIoJew==',
        'release_year': 1992,
        'seasonCount': 0,
        'seasons': [],
        # 'title': 'Death Becomes Her',
        'title': '   ',
        'type': 'MOVIE'},
    {
        'is_original': False,
        'locale': 'en-AU',
        'originalTitle': "Chappelle's Show",
        'pvid': 'mnOVjhip5fLqzT2pFd/Ptg==',
        'release_year': 2003,
        'seasonCount': 2,
        'seasons': [
            {
                'episodeCount': 12,
                'seasonName': 'Season 1',
                'seasonNumber': 1
            },
            {
                'episodeCount': 12,
                'seasonName': 'Season 2',
                'seasonNumber': 2
            }
        ],
        'title': "    ",
        'type': 'SHOW'
    }
]


@app.route('/netflix/feed', methods=['GET', 'POST'])
def netflix_feed():

    if request.method == 'GET':
        return Response(json.dumps(netflix_check_feed))

@app.route('/netflix/data', methods=['GET', 'POST'])
def netflix_data():

    if request.method == 'GET':
        return Response(json.dumps(netflix_data_feed))


@app.route('/tenaa/feed', methods=['GET', 'POST'])
def tenaa_feed():
    count = request.args['count']
    start_index = request.args['startIndex']

    if request.method == 'GET':
        return Response(json.dumps(tenaa_data))


@app.route('/prime/feed', methods=['GET', 'POST'])
def prime_feed():

    if request.method == 'GET':
        return Response(json.dumps(amazon_feed_data))


@app.route('/prime/meta', methods=['GET', 'POST'])
def prime_meta():

    if request.method == 'GET':
        prime_meta_data_string = '\n'.join([json.dumps(json_string) for json_string in prime_meta_data])
        return Response(prime_meta_data_string)


@app.route('/prime/offers', methods=['GET', 'POST'])
def prime_offers():

    if request.method == 'GET':
        prime_offers_string = '\n'.join([json.dumps(json_string) for json_string in prime_offers_data])
        return Response(prime_offers_string)

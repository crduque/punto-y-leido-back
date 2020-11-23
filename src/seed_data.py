data = {
    "reader": [
        {
            "id": 1,
            "is_active": True,
            "username": "crduque",
            "email": "crduque@gmail.com",
            "password": "123456",
            "name": "Cristina",
            "description": "Soy una lectora empedernida de fantasía",
        },
        {
            "id": 2,
            "is_active": True,
            "username": "manuneufeld",
            "email": "manuneufeld@gmail.com",
            "password": "123456",
            "name": "Manuela",
            "description": "Me gusta leer novelas históricas",
        },
        {
            "id": 3,
            "is_active": True,
            "username": "jancarlo",
            "email": "jancarlo@gmail.com",
            "password": "123456",
            "name": "Jan Carlo",
            "description": "Seguidor aférrimo de Stephen King",
        },
        {
            "id": 4,
            "is_active": True,
            "username": "alexandrito",
            "email": "alexandrito@gmail.com",
            "password": "123456",
            "name": "Alexander",
            "description": "Marvel power!",
        },
        {
            "id": 5,
            "is_active": True,
            "username": "victorcito",
            "email": "victorcito@gmail.com",
            "password": "123456",
            "name": "Víctor",
            "description": "Me encantan las novelas de romance",
        },
        {
            "id": 6,
            "is_active": True,
            "username": "gongon",
            "email": "gongon@gmail.com",
            "password": "123456",
            "name": "Gonzalo",
            "description": "Forofo de los grandes clásicos",
        },
        {
            "id": 7,
            "is_active": True,
            "username": "jimenita",
            "email": "jimenita@gmail.com",
            "password": "123456",
            "name": "Jimena",
            "description": "Novela juvenil te invoco a ti",
        }
    ],
    "book": [
        {
            "id": 1,
            "image": "data:image/jpeg;base64,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",
            "title": "Yo, Julia",
            "synopsis": "192 d.C. Varios hombres luchan por un imperio, pero Julia, hija de reyes, madre de césares y esposa de emperador, piensa en algo más ambicioso: una dinastía. Roma está bajo el control de Cómodo, un emperador loco. El Senado se conjura para terminar con el tirano y los gobernadores militares más poderosos podrían dar un golpe de Estado: Albino en Britania, Severo en el Danubio o Nigro en Siria. Cómodo retiene a sus esposas para evitar su rebelión y Julia, la mujer de Severo, se convierte así en rehén. De pronto, Roma arde. Un incendio asola la ciudad. ¿Es un desastre o una oportunidad? Cinco hombres se disponen a luchar a muerte por el poder. Creen que la partida está a punto de empezar. Pero para Julia la partida ya ha empezado. Sabe que solo una mujer puede forjar una dinastía.",
            "format_type": "Tapa dura",
            "genre": "Histórica",
            "price": 22.90    
        },
        {
            "id": 21,
            "image": "data:image/jpeg;base64,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",
            "title": "Yo, Julia",
            "synopsis": "192 d.C. Varios hombres luchan por un imperio, pero Julia, hija de reyes, madre de césares y esposa de emperador, piensa en algo más ambicioso: una dinastía. Roma está bajo el control de Cómodo, un emperador loco. El Senado se conjura para terminar con el tirano y los gobernadores militares más poderosos podrían dar un golpe de Estado: Albino en Britania, Severo en el Danubio o Nigro en Siria. Cómodo retiene a sus esposas para evitar su rebelión y Julia, la mujer de Severo, se convierte así en rehén. De pronto, Roma arde. Un incendio asola la ciudad. ¿Es un desastre o una oportunidad? Cinco hombres se disponen a luchar a muerte por el poder. Creen que la partida está a punto de empezar. Pero para Julia la partida ya ha empezado. Sabe que solo una mujer puede forjar una dinastía.",
            "format_type": "Ebook",
            "genre": "Histórica",
            "price": 22.90    
        },
        {
            "id": 12
            "image": "https://images-na.ssl-images-amazon.com/images/I/717awSisirL.jpg",
            "title": "Orgullo y prejuicio",
            "synopsis": "Publicada originalmente en 1813, Orgullo y prejuicio es una de las obras maestras de la literatura inglesa de todos los tiempos. A lo largo de una trama que discurre con gran ritmo y precisión, Jane Austen reúene una galería de personajes característicos de toda una época: la dama empeñada en casar a sus hijas con el mejor partido de la región, las hermanas que se debaten con sus vaivenes sentimentales, el clérigo adulador que peca de oportunista... El estudio de caracteres y el análisis de las relaciones humanas basadas en la costumbre, elementos esenciales de la narrativa de la autora, alcanzan en Orgullo y prejuicio cotas de maestría insuperable. La presente edición incluye una detallada cronología de la autora.",
            "format_type": "Ilustrado",
            "genre": "Clásicos",
            "price": 16.90    
        },
        {
            "id": 14,
            "image": "https://images-na.ssl-images-amazon.com/images/I/41E6BToW6CL._SX319_BO1,204,203,200_.jpg",
            "title": "Las venas abiertas de América Latina",
            "synopsis": "Historia del saqueo de América Latina que muestra cómo funcionan los mecanismos actuales del despojo: los tecnócratas en jet, herederos de los conquistadores en carabela; Hernán Cortés y los infantes de marina; los corregidores del reino y las misiones del Fondo Monetario Internacional; los dividendos del tráfico de esclavos y las ganancias de la General Motors. El tiempo presente ha sido presentido y engendrado por las contradicciones del pasado.",
            "format_type": "Bolsillo",
            "genre": "Histórica",
            "price": 18.95    
        },
        {
            "id": 18,
            "image": "https://cdn.grupoelcorteingles.es/SGFM/dctm/MEDIA03/201807/05/00106520608552____7__640x640.jpg",
            "title": "El imperio final (Nacidos de la bruma I)",
            "synopsis": "Durante mil años han caído cenizas del cielo. Durante mil años nada ha florecido. Durante mil años los skaa han sido esclavizados y viven en la miseria, sumidos en un miedo inevitable. Durante mil años el Lord Legislador ha reinado con poder absoluto, dominando gracias al terror, a sus poderes y a su inmortalidad, ayudado por «obligadores» e «inquisidores», junto a la poderosa magia de la alomancia. Pero los nobles a menudo han tenido trato sexual con jóvenes skaa y, aunque la ley lo prohíbe, algunos de sus bastardos han sobrevivido y heredado los poderes alománticos: son los «nacidos de la bruma» (mistborn). Ahora, Kelsier, el «superviviente», el único que ha logrado huir de los Pozos de Hathsin, ha encontrado a Vin, una pobre chica skaa con mucha suerte... Tal vez los dos, con el mejor equipo criminal jamás reunido, unidos a la rebelión que los skaa intentan desde hace mil años, logren cambiar el mundo y acabar con la atroz mano de hierro del Lord Legislador. Pero, ¿qué pasa si el héroe de la profecía falla?",
            "format_type": "Tapa dura",
            "genre": "Ciencia ficción y fantasía",
            "price": 12.95    
        },
        {
            "id": 19,
            "image": "https://m.media-amazon.com/images/I/511PjVMPctL.jpg",
            "title": "El pozo de la ascensión (Nacidos de la bruma II)",
            "synopsis": "Durante mil años han caído cenizas del cielo. Durante mil años nada ha florecido. Durante mil años los skaa han sido esclavizados y viven en la miseria, sumidos en un miedo inevitable. Durante mil años el Lord Legislador ha reinado con poder absoluto, dominando gracias al terror, a sus poderes y a su inmortalidad, ayudado por «obligadores» e «inquisidores», junto a la poderosa magia de la alomancia. Pero los nobles a menudo han tenido trato sexual con jóvenes skaa y, aunque la ley lo prohíbe, algunos de sus bastardos han sobrevivido y heredado los poderes alománticos: son los «nacidos de la bruma» (mistborn). Ahora, Kelsier, el «superviviente», el único que ha logrado huir de los Pozos de Hathsin, ha encontrado a Vin, una pobre chica skaa con mucha suerte... Tal vez los dos, con el mejor equipo criminal jamás reunido, unidos a la rebelión que los skaa intentan desde hace mil años, logren cambiar el mundo y acabar con la atroz mano de hierro del Lord Legislador. Pero, ¿qué pasa si el héroe de la profecía falla?",
            "format_type": "Tapa dura",
            "genre": "Ciencia ficción y fantasía",
            "price": 12.95    
        },
        {
            "id": 20,
            "image": "https://m.media-amazon.com/images/I/51h10D+bP1L.jpg",
            "title": "El Héroe de las Eras (Nacidos de la bruma III)",
            "synopsis": "Durante mil años han caído cenizas del cielo. Durante mil años nada ha florecido. Durante mil años los skaa han sido esclavizados y viven en la miseria, sumidos en un miedo inevitable. Durante mil años el Lord Legislador ha reinado con poder absoluto, dominando gracias al terror, a sus poderes y a su inmortalidad, ayudado por «obligadores» e «inquisidores», junto a la poderosa magia de la alomancia. Pero los nobles a menudo han tenido trato sexual con jóvenes skaa y, aunque la ley lo prohíbe, algunos de sus bastardos han sobrevivido y heredado los poderes alománticos: son los «nacidos de la bruma» (mistborn). Ahora, Kelsier, el «superviviente», el único que ha logrado huir de los Pozos de Hathsin, ha encontrado a Vin, una pobre chica skaa con mucha suerte... Tal vez los dos, con el mejor equipo criminal jamás reunido, unidos a la rebelión que los skaa intentan desde hace mil años, logren cambiar el mundo y acabar con la atroz mano de hierro del Lord Legislador. Pero, ¿qué pasa si el héroe de la profecía falla?",
            "format_type": "Tapa dura",
            "genre": "Ciencia ficción y fantasía",
            "price": 12.95    
        }
    ],
    "author": [
        {
            "id": 1,
            "name": "Jane Austen",
            "biography": "Jane Austen (Steventon, 16 de diciembre de 1775-Winchester, 18 de julio de 1817) fue una novelista británica que vivió durante la época georgiana. La ironía que emplea para dotar de comicidad a sus novelas hace que Jane Austen sea considerada entre los clásicos de la novela inglesa, a la vez que su recepción va, incluso en la actualidad, más allá del interés académico, siendo sus obras leídas por un público más amplio.",
            "image" : "data:image/jpeg;base64,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"
        },
        {
            "id": 8,
            "name": "Eduardo Galeano",
            "biography": "Eduardo Germán María Hughes Galeano (Montevideo, Uruguay; 3 de septiembre de 1940-ibidem, 13 de abril de 2015)1​ fue un periodista y escritor uruguayo, considerado uno de los escritores más influyentes de la izquierda latinoamericana. Sus libros más conocidos, Las venas abiertas de América Latina (1971) y Memoria del fuego (1986), han sido traducidos a veinte idiomas. Sus trabajos trascienden géneros ortodoxos y combinan documental, ficción, periodismo, análisis político e historia.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Eduardo_Galeano_ltk_%28cropped%29.jpg/330px-Eduardo_Galeano_ltk_%28cropped%29.jpg"
        },
        {
            "id": 13,
            "name": "Santiago Posteguillo",
            "biography": "Santiago Posteguillo nació en Valencia, España, en 1967. Estudió Literatura Creativa en la Universidad de Denison, en Granville (Ohio), Estados Unidos y lingüística y traducción en Gran Bretaña. Es profesor titular de Lengua y Literatura Inglesa en la Universitat Jaume I en Castellón. Fue director del Instituto Interuniversitario de Filología Valenciana.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Santiago_Posteguillo.jpg"
        },
        {
            "id": 15,
            "name": "Brandon Sanderson",
            "biography": "Brandon Sanderson es un escritor nacido en Nebraska, Estados Unidos, el 19 de diciembre de 1975. Es un conocido escritor de literatura fantástica, cuyas obras le han llevado a ser nominado dos veces al Premio John W. Campbell. Parte de su éxito llega por haberse hecho cargo del libro final de una saga ajena, La rueda del tiempo. Este hecho ocurrió justo después de la muerte de Robert Jordan, autor original de los libros anteriores, ante lo cual su propia mujer (Harriet McDougal) escogió a Sanderson como escritor del final de la saga de su difunto marido. Harriet le escogió tras quedar sorprendida por la calidad de los libros de este autor.",
            "image": "https://momoko.es/images/author-avatar/sanderson-bio_thumbnail_1_563px_741px.jpg"
        },
    ],
    "written_by": [
        {
            "id_author": 13,
            "id_book": 1
        },
        {
            "id_author": 13,
            "id_book": 21
        },
        {
            "id_author": 1,
            "id_book": 12
        },
        {
            "id_author": 8,
            "id_book": 14
        },
        {
            "id_author": 15,
            "id_book": 18
        },
        {
            "id_author": 15,
            "id_book": 19
        },
        {
            "id_author": 15,
            "id_book": 20
        },
    ],
    "review": [
        {
            "id": 1,
            "id_reader": 1,
            "id_book": 18,
            "stars": "5",
            "date": (2019, 10, 25),
            "review": "Primero de una de mis trilogías de fantasía preferida. Es una maravilla, tanto cómo se desarrollan los personajes los personajes como el desarrollo de la historia en los tres libros. Totalmente recomendado.",
        },
        {
            "id": 2,
            "id_reader": 6,
            "id_book": 1,
            "stars": "4",
            "date": (2019, 12, 5),
            "review": "Trepidante novela histórica que te hace admirar a una mujer que fue muy poderosa en un momento de la historia en el que parecía imposible que esto sucediera. También es destacable la narrativa de las batallas.",
        },
        {
            "id": 3,
            "id_reader": 2,
            "id_book": 14,
            "stars": "5",
            "date": (2020, 1, 9),
            "review": "Novela histórica que transmite la verdadera esencia de América Latina sin tener la necesidad de viajar hasta allí. Recomendada 100%.",
        },
        {
            "id": 4,
            "id_reader": 7,
            "id_book": 12,
            "stars": "4",
            "date": (2020, 3, 30),
            "review": "Historia adelantada a su época, con una autora pionera en la escritura sagaz.",
        },
    ]
}
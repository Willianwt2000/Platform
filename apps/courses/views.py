from django.shortcuts import render


# Create your views here.


def course_list(request):
    courses = [
        {
            'id': 1,
            'level': 'Clase A',
            'rating': 4.5,
            'course_title': 'JavaScript: fundamentos',
            'instructor': 'Soon Jin Woo',
            'course_image': 'https://sgimage.netmarble.com/images/netmarble/sololv/20240318/fxbt1710761341766.jpg',
            'instructor_image': 'https://culturedvultures.com/wp-content/uploads/2022/11/image_2022-11-01_112512251.jpg',
        },
        {
            'id': 2,
            'level': 'Clase S',
            'rating': 4.8,
            'course_title': 'Python avanzado',
            'instructor': 'Gojo Satoru',
            'course_image': 'https://img.anmosugoi.com/file/media-sugoi/2023/07/jujutsu-kaisen-satoru-gojo-rojo.jpg',
            'instructor_image': 'https://w0.peakpx.com/wallpaper/666/961/HD-wallpaper-anime-jujutsu-kaisen-satoru-gojo.jpg',
        },
        {
            'id': 3,
            'level': 'Clase B',
            'rating': 4.6,
            'course_title': 'HTML y CSS desde cero',
            'instructor': 'Naruto Uzumaki',
            'course_image': 'https://4kwallpapers.com/images/wallpapers/naruto-uzumaki-action-power-3840x2743-6493.jpg',
            'instructor_image': 'https://img.goodfon.com/wallpaper/big/7/bd/naruto-uzumaki-naruto-paren-sila.webp',
        },
        {
            'id': 4,
            'level': 'Clase A',
            'rating': 4.7,
            'course_title': 'React para principiantes',
            'instructor': 'Eren Yeager',
            'course_image': 'https://cdna.artstation.com/p/assets/images/images/073/789/164/original/justg0ldenn_j2-eren-jaeger-justg0ldenn222.gif?1710471591',
            'instructor_image': 'https://cdn.mxj.myanimelist.net/web/bpart/submissions/100009.jpg',
        }
    ]
    return render(request, "courses/courses.html", {
        'courses': courses
    })


def course_detail(request):
    course = {
        'course_title': 'JavaScript: fundamentos',
        'course_link': 'course_lessons',
        'course_author': 'https://makerworld.bblmw.com/makerworld/model/US28861ea471fdca/design/2024-01-06_a1b1fb2777cf3.jpg?x-oss-process=image/resize,w_1000/format,webp',
        'course_banner': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT5cEj8YHGfoQpSpubw5dWhd3_m_XJHHgDjg&s',
        'info_course': {
            'lessons': 79,
            'duration': 8,
            'instructor': 'Ricardo Doe'
        },
        'course_content': [
            {
                'id': 1,
                'name': 'Introducción al curso',
                'lessons': [
                    {
                        'name': '¿Qué aprenderás en este curso?',
                        'type': 'video'
                    },
                    {
                        'name': 'Como usar la plataforma?',
                        'type': 'article'
                    }
                ]
            },
            {
                'id': 2,
                'name': 'El Sistema de Cazadores y Rangos',
                'lessons': [
                    {
                        'name': 'Clasificación de Gremios y Rangos (E a S)',
                        'type': 'video'
                    },
                    {
                        'name': 'Anatomía de una Mazmorra: Portales y Jefes',
                        'type': 'article'
                    },
                    {
                        'name': 'Reglas de supervivencia en una Double Dungeon',
                        'type': 'video'
                    }
                ]
            },
            {
                'id': 3,
                'name': 'El Camino del Monarca de las Sombras',
                'lessons': [
                    {
                        'name': 'Misiones diarias: El secreto de la fuerza de Jin-woo',
                        'type': 'video'
                    },
                    {
                        'name': 'Extracción de Sombras: ¡Levántate!',
                        'type': 'video'
                    },
                    {
                        'name': 'Gestión del inventario y puntos de habilidad',
                        'type': 'article'
                    }
                ]
            }
        ]

    }

    return render(request, 'courses/course_detail.html', {'course': course})


def course_lessons(request):
    lesson = {
        'course_title': 'Django Aplicaciones',
        'progress': 30,
        'course_content': [
            {
                'id': 1,
                'name': 'Introducción al curso',
                'total_lessons': 6,
                'complete_lessons': 3,
                'lessons': [
                    {
                        'name': '¿Qué aprenderás en este curso?',
                        'type': 'video'
                    },
                    {
                        'name': 'Como usar la plataforma?',
                        'type': 'article'
                    }
                ]
            },
            {
                'id': 2,
                'name': 'El Sistema de Cazadores y Rangos',
                'total_lessons': 8,
                'complete_lessons': 3,
                'lessons': [
                    {
                        'name': 'Clasificación de Gremios y Rangos (E a S)',
                        'type': 'video'
                    },
                    {
                        'name': 'Anatomía de una Mazmorra: Portales y Jefes',
                        'type': 'article'
                    },
                    {
                        'name': 'Reglas de supervivencia en una Double Dungeon',
                        'type': 'video'
                    }
                ]
            },
            {
                'id': 3,
                'name': 'El Camino del Monarca de las Sombras',
                'total_lessons': 4,
                'complete_lessons': 3,
                'lessons': [
                    {
                        'name': 'Misiones diarias: El secreto de la fuerza de Jin-woo',
                        'type': 'video'
                    },
                    {
                        'name': 'Extracción de Sombras: ¡Levántate!',
                        'type': 'video'
                    },
                    {
                        'name': 'Gestión del inventario y puntos de habilidad',
                        'type': 'article'
                    }
                ]
            }
        ]

    }

    return render(request, 'courses/course_lessons.html', {
        'lesson': lesson
    })

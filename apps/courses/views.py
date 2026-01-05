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
    return render(request, 'courses/course_detail.html')


def course_lessons(request):
    return render(request,'courses/course_lessons.html')

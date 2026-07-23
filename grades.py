import random

SUBJECTS = {

    "علوم": [

        ("اللغة العربية",80,45),
        ("اللغة الأجنبية الأولى",60,25),
        ("الأحياء",60,20),
        ("الكيمياء",60,20),
        ("الفيزياء",60,20)

    ],

    "رياضة":[

        ("اللغة العربية",80,45),
        ("اللغة الأجنبية الأولى",60,25),
        ("الرياضيات",60,20),
        ("الكيمياء",60,20),
        ("الفيزياء",60,20)

    ],

    "أدبي":[

        ("اللغة العربية",80,45),
        ("اللغة الأجنبية الأولى",60,25),
        ("التاريخ",60,20),
        ("الجغرافيا",60,20),
        ("علم النفس والاجتماع",60,20)

    ]

}


def generate_result(seat, section):

    random.seed(int(seat))

    grades=[]

    total=0

    full=0

    for subject,max_degree,min_degree in SUBJECTS[section]:

        degree=random.randint(min_degree,max_degree)

        grades.append({

            "subject":subject,

            "degree":degree,

            "max":max_degree

        })

        total+=degree
        full+=max_degree

    percent=round((total/full)*100,2)

    if percent>=50:
        status="ناجح"
    else:
        status="راسب"

    return grades,total,full,percent,status
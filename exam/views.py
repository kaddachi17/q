from django.core.mail import send_mail
from django.shortcuts import render, redirect

from Dashboard.models import Yard
from .models import Question, Exam, one_answer, Free_text, Multi_choice_answer, Reponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from random import *
from Authentification.models import UserP, UserS
from django.contrib import messages


def index(request):
    if 'id' in request.session:
        all_exam = Exam.objects.all()
        template = loader.get_template('exam/index.html')
        context = {
            'all_exam': all_exam,
        }
        return HttpResponse(template.render(context, request))


def edit(request, exam_id):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        exam = Exam.objects.get(pk=exam_id)
        if request.method == "POST":
            examName = request.POST['examName']
            ExamDesc = request.POST['ExamDesc']
            category = request.POST['category']
            logo = request.FILES['logo']

            exam.name = examName
            exam.description = ExamDesc
            exam.category = category
            exam.logo = logo
            exam.save()
            return redirect('/exam/')
        template = loader.get_template('exam/edit.html')
        context = {
            'examen_id': exam_id,
            'examen': exam,

        }

        return HttpResponse(template.render(context, request))


def detail(request, exam_id):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        exam = Exam.objects.get(pk=exam_id)
        template = loader.get_template('exam/les_questions.html')
        context = {
            'examen_id': exam_id,
            'examen': exam,

        }

        return HttpResponse(template.render(context, request))


def editone(request, Quest_id):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        question = Question.objects.get(pk=Quest_id)
        if 'id' in request.session:
            if request.method == 'POST':
                Description = request.POST['Description']
                Header_text = request.POST['Header_text']
                Footer_text = request.POST['Footer_text']
                Success_msg = request.POST['Success_msg']
                Fail_msg = request.POST['Fail_msg']
                points = request.POST['points']
                question.description = Description
                question.header_text = Header_text
                question.footer_text = Footer_text
                question.success_msg = Success_msg
                question.fail_msg = Fail_msg
                question.points = points
                question.save()
                ID1 = request.POST['id1']
                ID2 = request.POST['id2']
                ID3 = request.POST['id3']
                ans1 = one_answer.objects.get(pk=ID1)
                ans2 = one_answer.objects.get(pk=ID2)
                ans3 = one_answer.objects.get(pk=ID3)

                answer_variant = request.POST['answer_variant1']
                answer_description = request.POST['answer_description1']
                pointsAns = request.POST['points1']
                answer_variant2 = request.POST['answer_variant2']
                answer_description2 = request.POST['answer_description2']
                pointsAns2 = request.POST['points2']
                answer_variant3 = request.POST['answer_variant3']
                answer_descriptio3 = request.POST['answer_description3']
                pointsAn3 = request.POST['points3']

                ans1.answer_variant = answer_variant
                ans1.answer_description = answer_description
                ans1.points = pointsAns
                ans1.save()
                ans2.answer_variant = answer_variant2
                ans2.answer_description = answer_description2
                ans2.points = pointsAns2
                ans2.save()
                ans3.answer_variant = answer_variant3
                ans3.answer_description = answer_descriptio3
                ans3.points = pointsAn3
                ans3.save()

                return redirect("/exam/")
            else:
                template = loader.get_template('exam/editOneAnser.html')
                context = {
                    'question': question,

                }

                return HttpResponse(template.render(context, request))


def editmulti(request, Quest_id):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        question = Question.objects.get(pk=Quest_id)
        if 'id' in request.session:
            if request.method == 'POST':
                Description = request.POST['Description']
                Header_text = request.POST['Header_text']
                Footer_text = request.POST['Footer_text']
                Success_msg = request.POST['Success_msg']
                Fail_msg = request.POST['Fail_msg']
                points = request.POST['points']
                question.description = Description
                question.header_text = Header_text
                question.footer_text = Footer_text
                question.success_msg = Success_msg
                question.fail_msg = Fail_msg
                question.points = points
                question.save()
                ID1 = request.POST['id1']
                ID2 = request.POST['id2']
                ID3 = request.POST['id3']
                ans1 = Multi_choice_answer.objects.get(pk=ID1)
                ans2 = Multi_choice_answer.objects.get(pk=ID2)
                ans3 = Multi_choice_answer.objects.get(pk=ID3)

                answer_variant = request.POST['answer_variant1']
                answer_description = request.POST['answer_description1']
                pointsAns = request.POST['points1']
                answer_variant2 = request.POST['answer_variant2']
                answer_description2 = request.POST['answer_description2']
                pointsAns2 = request.POST['points2']
                answer_variant3 = request.POST['answer_variant3']
                answer_descriptio3 = request.POST['answer_description3']
                pointsAn3 = request.POST['points3']

                ans1.multi_variant = answer_variant
                ans1.multi_description = answer_description
                ans1.points = pointsAns
                ans1.save()
                ans2.multi_variant = answer_variant2
                ans2.multi_description = answer_description2
                ans2.points = pointsAns2
                ans2.save()
                ans3.multi_variant = answer_variant3
                ans3.multi_description = answer_descriptio3
                ans3.points = pointsAn3
                ans3.save()

                return redirect("/exam/")
            else:
                template = loader.get_template('exam/EditMulti.html')
                context = {
                    'question': question,

                }

                return HttpResponse(template.render(context, request))


def editfree(request, Quest_id):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        question = Question.objects.get(pk=Quest_id)
        if 'id' in request.session:
            if request.method == 'POST':
                Description = request.POST['Description']
                Header_text = request.POST['Header_text']
                Footer_text = request.POST['Footer_text']
                Success_msg = request.POST['Success_msg']
                Fail_msg = request.POST['Fail_msg']
                points = request.POST['points']
                question.description = Description
                question.header_text = Header_text
                question.footer_text = Footer_text
                question.success_msg = Success_msg
                question.fail_msg = Fail_msg
                question.points = points
                question.save()
                id = request.POST['id']
                freeText = Free_text.objects.get(pk=id)
                text = request.POST['text']
                freeText.text = text
                freeText.save()
                return redirect("/exam/")
            else:
                template = loader.get_template('exam/EditFreeText.html')
                context = {
                    'question': question,

                }

                return HttpResponse(template.render(context, request))


def reponse(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    template = loader.get_template('exam/valider.html')

    try:
        choice = one_answer.objects.get(pk=request.POST['choice'])


    except(KeyError):

        exam.total = 0
        exam.save()
        context = {
            'exam': exam,
            'exam_id': exam_id,
            'message': 'choix non valide',

        }
        return HttpResponse(template.render(context, request))
    else:
        exam.total = choice.note
        exam.save()
        context = {
            'exam': exam,
            'exam_id': exam_id,

        }
        return HttpResponse(template.render(context, request))


def create_view(request):
    if 'id' in request.session:
        return render(request, 'exam/createExam.html')


def createExam(request):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        if 'id' in request.session:
            if request.method == 'POST' and request.POST['examName']:
                examName = request.POST['examName']
                ExamDesc = request.POST['ExamDesc']
                category = request.POST['category']
                logo = request.FILES['logo']

                exam = Exam()
                exam.name = examName
                exam.description = ExamDesc
                exam.category = category
                exam.logo = logo
                exam.save()
                request.session['id'] = exam.id
                # print(request.session['id'])

                context = {
                    'exam_id': exam.id,
                }
                return render(request, 'exam/createQuest.html', context)


def secondeQuest(request):
    if 'id' in request.session:
        if request.method == 'POST':
            Description = request.POST['Description']
            Header_text = request.POST['Header_text']
            Footer_text = request.POST['Footer_text']
            Success_msg = request.POST['Success_msg']
            Fail_msg = request.POST['Fail_msg']
            points = request.POST['points']
            type = request.POST['type']

            question = Question()
            exam = Exam.objects.get(pk=request.session['id'])
            question.examen = exam
            question.description = Description
            question.header_text = Header_text
            question.footer_text = Footer_text
            question.success_msg = Success_msg
            question.fail_msg = Fail_msg
            question.points = points

            question.save()

            if type == 'one':
                answer_variant = request.POST['answer_variant1']
                answer_description = request.POST['answer_description1']
                pointsAns = request.POST['points1']
                answer_variant2 = request.POST['answer_variant2']
                answer_description2 = request.POST['answer_description2']
                pointsAns2 = request.POST['points2']
                answer_variant3 = request.POST['answer_variant2']
                answer_descriptio3 = request.POST['answer_description2']
                pointsAn3 = request.POST['points2']
                ans = one_answer()
                ans.question = question
                ans.answer_variant = answer_variant
                ans.answer_description = answer_description
                ans.points = pointsAns
                ans.save()
                ans2 = one_answer()
                ans2.question = question
                ans2.answer_variant = answer_variant2
                ans2.answer_description = answer_description2
                ans2.points = pointsAns2
                ans2.save()
                ans3 = one_answer()
                ans3.question = question
                ans3.answer_variant = answer_variant3
                ans3.answer_description = answer_descriptio3
                ans3.points = pointsAn3
                ans3.save()

            elif type == 'free':
                text = request.POST['text']
                free = Free_text()
                free.question = question
                free.text = text
                free.save()
            else:
                answer_variant = request.POST['answer_variant1m']
                answer_description = request.POST['answer_description1m']
                pointsAns = request.POST['points1m']
                answer_variant2 = request.POST['answer_variant2m']
                answer_description2 = request.POST['answer_description2m']
                pointsAns2 = request.POST['points2m']
                answer_variant3 = request.POST['answer_variant3m']
                answer_description3 = request.POST['answer_description3m']
                pointsAns3 = request.POST['points3m']
                multi = Multi_choice_answer()
                multi.question = question
                multi.multi_variant = answer_variant
                multi.multi_description = answer_description
                multi.points = pointsAns
                multi.save()
                multi2 = Multi_choice_answer()
                multi2.question = question
                multi2.multi_variant = answer_variant2
                multi2.multi_description = answer_description2
                multi2.points = pointsAns2
                multi2.save()
                multi3 = Multi_choice_answer()
                multi3.question = question
                multi3.multi_variant = answer_variant3
                multi3.multi_description = answer_description3
                multi3.points = pointsAns3
                multi3.save()

            return render(request, 'exam/createQuest.html')
        else:
            return render(request, 'exam/createQuest.html')


def add_to_yard(request, pk, selected_id):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        selected_yard = Yard.objects.get(pk=pk)
        selected_student = UserS.userManagerS.getOneUser(selected_id)
        if selected_student not in selected_yard.student.all():
            selected_yard.student.add(selected_student)
        else:
            return redirect("/exam")
        return redirect("/exam")


def addStudent(request, pk):
    if request.session['is_prof'] is True:
        professor = UserP.userManagerP.getOneUser(request.session['id'])
        all_my_students = professor.student.all()
        all_yard = professor.yard_set.all()
        context = {
            'all_my_students': all_my_students,
            'all_students': UserS.userManagerS.getAllUsers(),
            'professor': UserP.userManagerP.getOneUser(request.session['id']),
            'is_prof': request.session['is_prof'],
        }
        return render(request, "exam/Yard_student.html", context)
    if request.session['is_prof'] == False:
        return redirect("/exam/")


def assigne_classroom(request, pk):
    if request.session['is_prof'] is True:
        professor = UserP.userManagerP.getOneUser(request.session['id'])
        selected_student = UserS.userManagerS.getOneUser(pk)
        all_yard = professor.yard_set.all()
        context = {
            'all_yard': all_yard,
            'professor': professor,
            'selected_student': selected_student,
        }
        return render(request, 'exam/assign_classroom.html', context)
    if request.session['is_prof'] == False:
        return redirect("/exam/")


def addQuest(request, exam_id):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        if 'id' in request.session:
            if request.method == 'POST':
                Description = request.POST['Description']
                Header_text = request.POST['Header_text']
                Footer_text = request.POST['Footer_text']
                Success_msg = request.POST['Success_msg']
                Fail_msg = request.POST['Fail_msg']
                points = request.POST['points']
                type = request.POST['type']

                question = Question()
                exam = Exam.objects.get(pk=exam_id)
                question.examen = exam
                question.description = Description
                question.header_text = Header_text
                question.footer_text = Footer_text
                question.success_msg = Success_msg
                question.fail_msg = Fail_msg
                question.points = points

                question.save()

                if type == 'one':
                    answer_variant = request.POST['answer_variant1']
                    answer_description = request.POST['answer_description1']
                    pointsAns = request.POST['points1']
                    answer_variant2 = request.POST['answer_variant2']
                    answer_description2 = request.POST['answer_description2']
                    pointsAns2 = request.POST['points2']
                    answer_variant3 = request.POST['answer_variant2']
                    answer_descriptio3 = request.POST['answer_description2']
                    pointsAn3 = request.POST['points2']
                    ans = one_answer()
                    ans.question = question
                    ans.answer_variant = answer_variant
                    ans.answer_description = answer_description
                    ans.points = pointsAns
                    ans.save()
                    ans2 = one_answer()
                    ans2.question = question
                    ans2.answer_variant = answer_variant2
                    ans2.answer_description = answer_description2
                    ans2.points = pointsAns2
                    ans2.save()
                    ans3 = one_answer()
                    ans3.question = question
                    ans3.answer_variant = answer_variant3
                    ans3.answer_description = answer_descriptio3
                    ans3.points = pointsAn3
                    ans3.save()

                elif type == 'free':
                    text = request.POST['text']
                    free = Free_text()
                    free.question = question
                    free.text = text
                    free.save()
                else:
                    answer_variant = request.POST['answer_variant1m']
                    answer_description = request.POST['answer_description1m']
                    pointsAns = request.POST['points1m']
                    answer_variant2 = request.POST['answer_variant2m']
                    answer_description2 = request.POST['answer_description2m']
                    pointsAns2 = request.POST['points2m']
                    answer_variant3 = request.POST['answer_variant3m']
                    answer_description3 = request.POST['answer_description3m']
                    pointsAns3 = request.POST['points3m']
                    multi = Multi_choice_answer()
                    multi.question = question
                    multi.multi_variant = answer_variant
                    multi.multi_description = answer_description
                    multi.points = pointsAns
                    multi.save()
                    multi2 = Multi_choice_answer()
                    multi2.question = question
                    multi2.multi_variant = answer_variant2
                    multi2.multi_description = answer_description2
                    multi2.points = pointsAns2
                    multi2.save()
                    multi3 = Multi_choice_answer()
                    multi3.question = question
                    multi3.multi_variant = answer_variant3
                    multi3.multi_description = answer_description3
                    multi3.points = pointsAns3
                    multi3.save()

                return redirect('/exam/')
            else:
                return render(request, 'exam/addQuestion.html')


def deleteEXam(request, exam_id):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        exam = Exam.objects.get(id=exam_id)
        exam.delete()
        return redirect("/exam/")


def deleteQuest(request, question_id):
    if request.session['is_prof'] is True:
        question = Question.objects.get(id=question_id)
        question.delete()
        return redirect("/exam/")
    if request.session['is_prof'] == False:
        return redirect("/exam/")


l = []
liste = []
listevider = []
first = 0
timerr = ""


def mode(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    if request.POST:

        if "test" in request.POST:
            choix = request.POST['test']
            if choix == "Train":
                timer = request.POST['timer']
                if timer == "TT":

                    exam.mode = "TT"
                else:
                    exam.mode = "T"
            elif choix == "One":
                timer = request.POST['timer']
                if timer == "Certifie":
                    exam.mode = "OC"
                else:
                    exam.mode = "O"


    else:
        exam.mode = "T"
    exam.save()
    return render(request, "exam/mode_exam.html", {'exam': exam})


def passe(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)

    global l
    global liste
    global first
    global listevider
    global timerr
    timerr = ""

    first = 0
    l =[]
    liste =[]
    listevider =[]

    liste += Question.objects.filter(examen=exam)
    shuffle(liste)
    for var in liste:
        listevider.append(var.id)
    context = {
        'examen_id': exam_id,
        'examen': exam,
        'firstid': liste[0].id

    }
    return render(request, "exam/passeExam.html", context)


i = 1


def inc_i():
    global i
    i += 1


def passeQuest(request, exam_id, Quest_id):
    global liste
    global timerr
    global first
    global listevider
    global l
    global i

    if request.POST:

        listeSession = []

        # print(listeSession)
        id = request.POST['id']
        exam = Exam.objects.get(pk=exam_id)

        quest = Question.objects.get(pk=Quest_id)
        if int(id) in listevider:
            l.append(int(id))

        if "radios" in request.POST:
            choix = request.POST['radios']
            request.session[id] = int(choix)

        elif "radiosM" in request.POST:
            choix = request.POST.getlist('radiosM')
            request.session[id] = choix

        else:
            text = request.POST['text']
            request.session[id] = text

        if int(id) in listevider:
            listevider.remove(int(id))
        length = len(liste)
        inc_i()

        if first == 1:
            timerr = request.POST['timerr']
            first += 1
        if int(Quest_id) in l:
            exist = True
        else:
            exist = False
        for ques in liste:
            if str(ques.id) in request.session:
                listeSession.append([ques.id, request.session[str(ques.id)]])
        context = {
            'examen_id': exam_id,
            'examen': exam,
            'quest_id': Quest_id,
            'quest': quest,
            'liste': liste,
            'i': i,
            'id': id,
            'l': l,
            'length': length,
            'listevider': listevider,
            'first': first,
            'timerr': timerr,
            'exist': exist,
            'listeSession': listeSession,

        }
        return render(request, "exam/QuestionExam.html", context)
    else:

        exam = Exam.objects.get(pk=exam_id)
        quest = Question.objects.get(pk=Quest_id)

        listeSession = []
        for ques in liste:
            if str(ques.id) in request.session:
                listeSession.append([ques.id, request.session[str(ques.id)]])
        first += 1
        if int(Quest_id) in l:
            exist = True
        else:
            exist = False
        length = len(liste)
        i = 1
        print(exist)

        context = {
            'examen_id': exam_id,
            'examen': exam,
            'quest_id': Quest_id,
            'quest': quest,
            'liste': liste,
            'i': i,
            'length': length,
            'listevider': listevider,
            'l': l,
            'first': first,
            'timerr': timerr,
            'exist': exist,
            'listeSession': listeSession,
        }

        return render(request, "exam/QuestionExam.html", context)


def result(request, exam_id):
    score = 0
    listeScore = []
    exam = Exam.objects.get(pk=exam_id)
    listeScore += Question.objects.filter(examen=exam)
    for question in listeScore:

        if str(question.id) in request.session:
            if type(request.session[str(question.id)]) is list:
                for choixia in request.session[str(question.id)]:
                    print('liste')
                    print(choixia)
                    rep = Reponse()
                    if request.session['is_prof'] is True:
                        rep.userP = UserP.userManagerP.getOneUser(request.session['id'])
                    else:
                        rep.userS = UserS.userManagerS.getOneUser(request.session['id'])
                    rep.exam = exam
                    Mans = Multi_choice_answer.objects.get(pk=choixia)
                    # one = one_answer()
                    # one.id = 0
                    # rep.One_answer = one
                    rep.multi_choice_answer = Mans
                    rep.score_question = Mans.points
                    rep.save()
            elif type(request.session[str(question.id)]) is int:
                rep = Reponse()
                if request.session['is_prof'] is True:
                    rep.userP = UserP.userManagerP.getOneUser(request.session['id'])
                elif request.session['is_prof'] is False:
                    rep.userS = UserS.userManagerS.getOneUser(request.session['id'])

                rep.exam = exam
                ans = one_answer.objects.get(pk=int(request.session[str(question.id)]))
                # mult = Multi_choice_answer()
                # mult.id = 0
                # rep.multi_choice_answer = mult
                rep.One_answer = ans
                rep.score_question = ans.points
                rep.save()
            elif type(request.session[str(question.id)]) is str:
                rep = Reponse()
                if request.session['is_prof'] is True:
                    rep.userP = UserP.userManagerP.getOneUser(request.session['id'])
                else:
                    rep.userS = UserS.userManagerS.getOneUser(request.session['id'])
                rep.exam = exam
                # one = one_answer()
                # one.id = 0
                # rep.One_answer = one
                # mult = Multi_choice_answer()
                # mult.id = 0
                # rep.multi_choice_answer = mult
                rep.free_text = request.session[str(question.id)]
                rep.save()
            del request.session[str(question.id)]
    if request.session['is_prof'] is True:
        listeRep = Reponse.objects.filter(exam=exam, userP=UserP.userManagerP.getOneUser(request.session['id']))
    else:
        listeRep = Reponse.objects.filter(exam=exam, userS=UserS.userManagerS.getOneUser(request.session['id']))
    for res in listeRep:
        score += res.score_question

    if request.session['is_prof'] is True:
        # rep.user = UserP.userManagerP.getOneUser(request.session['id'])

        context = {
            'username': UserP.userManagerP.getOneUser(request.session['id']),
            'examen_id': exam_id,
            'exam': exam,
            'score': score,
        }
    else:
        context = {
            'username': UserS.userManagerS.getOneUser(request.session['id']),
            'examen_id': exam_id,
            'exam': exam,
            'score': score,
        }

    return render(request, "exam/result.html", context)


def sendmail(request):
    if request.session['is_prof'] == False:
        return redirect("/exam/")
    if request.session['is_prof'] is True:
        if request.method == 'POST':
            email = request.POST['emaill']
            professor = UserP.userManagerP.getOneUser(request.session['id'])

            subject = 'Exam invitation from GTA platform'
            message = 'dear student you have been invited by ' + str(
                professor.first_name) + ' to join his online classroom pls click the link below to register http://127.0.0.1:8000/register '
            from_email = 'quiz@ghazelatc.com'
            to_list = [email, 'mouhebpp@gmail.com', 'kaddachihassib@gmail.com', 'kaddachihassib@gmail.com',
                       'test@gmail.com', 'iuhjik@gmail.com', 'hghjk@gmail.com', 'ghjkl@gmail.com', 'guhjkl@gmail.com',
                       'ijnk@gmail.com', 'tyui@gmail.com', 'hjklm@gmail.com', 'ghjklm@gmail.com']
            send_mail(subject, message, from_email, to_list)
            return redirect("/exam/sendmail/")
        else:
            professor = UserP.userManagerP.getOneUser(request.session['id'])
            template = loader.get_template('exam/sendmail.html')
            context = {
                'prefessor': professor,

            }

            return HttpResponse(template.render(context, request))

from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import QuestionForm
# Create your views here.

def index(request):
    questions = Question.objects.all()
    first_question = Question.objects.get(id=1)
    prof_question = Question.objects.get(id=6)

    context = {
        'questions': questions,
        'q_id': first_question.id,
        'pq': prof_question,
    }

    return render(request, 'index.html', context)

def question(request, q_id):
    question = Question.objects.get(id=q_id)
    
    context = {
        'question': question,
        'q_id' : question.id,
        'option1_per': question.option1_per,
        'option2_per': question.option2_per,
    }

    return render(request, 'question.html', context)

def next_question(request, q_id, user_id, bool):
    # 같은 user가 같은 question에 대해 answer을 남긴 기록이 있다면 불러오고, 아니면 answer 생성
    try:
        answer = Answer.objects.get(question_id=q_id,user_id=user_id)
        if bool == 1:
            answer.option = True
        else:
            answer.option = False
        answer.save(update_fields=['option'])
    except:
        answer = Answer()
        answer.user = request.user
        answer.question = Question.objects.get(id=q_id)
        if bool == 1:
            answer.option = True
        else:
            answer.option = False
        answer.save()
    # q_id에 해당하는 question에 percentage 업데이트
    question = Question.objects.get(id=q_id)
    answer_cnt = question.answer_set.count()
    option1_cnt = Answer.objects.filter(option=True, question_id=q_id).count()
    option2_cnt = Answer.objects.filter(option=False, question_id=q_id).count()
    if answer_cnt == 0:
        pass
    else:
        question.option1_per = int(option1_cnt/answer_cnt * 100)
        question.option2_per = int(option2_cnt/answer_cnt * 100)
        question.save(update_fields=['option1_per', 'option2_per'])
    # 다음 question이 있다면 다음 question 페이지로, 없다면 결과창으로
    try:
        next_question = Question.objects.get(id=q_id+1)
        return redirect(f'/QnA/{next_question.id}/')
    except:
        return redirect('QnA:result')
    
def result(request):
    answerset = request.user.answer_set.all().order_by('question_id')
    context = {
        'answerset': answerset,
    }
    return render(request,'result.html',context)
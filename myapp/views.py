from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def articles(request):
    return HttpResponse("articles")


def archive(request):
    return HttpResponse("<h1>archive</h1>")


def users(request, user_number=''):
    if user_number:
        return HttpResponse(f'user_number={user_number}')
    else:
        return HttpResponse('users')


def article(request, article_number='', slug_text=''):
    if slug_text:
        return HttpResponse(f'{article_number} + slug_text= {slug_text}')
    elif article_number:
        return HttpResponse(f'article_number = {article_number}')
    else:
        return HttpResponse(article_number)


def regular(request):
    return HttpResponse('regular')

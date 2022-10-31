from django.shortcuts import render

def post_list(request): ## 수정함
    return render(request, 'blog/post_list.html', {})

from django.shortcuts import redirect


def is_login(func):
    def decorated(request, *args, **kwargs):

        session = request.session.get('labeler')

        # 세션 여부 체크
        if session:  # 있다면 통과
            return func(request, *args, **kwargs)
        else:  # 세션 없다면, 로그인 창으로 return
            return redirect('/')

    return decorated

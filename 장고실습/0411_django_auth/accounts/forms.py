from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model #보이지 않는 유저클래스를 임포트해줌

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        password = None #깔끔해지긴 하지만 비밀번호 변경 링크를 추가로 만들어줘야함
        model = get_user_model() #user
        fields = ('email', 'first_name', 'last_name',) #보여주고 싶은것만!

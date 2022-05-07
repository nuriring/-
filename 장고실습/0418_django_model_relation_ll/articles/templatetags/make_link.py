from django import template

register = template.Library()

# {{ article.content|hashtag_link }}
@register.filter
def hashtag_link(word):
    #article의 content가 word에 들어있다. -> article 자체로 변경
    #해시태그를 공백 기준으로 나눠서 #으로 쪼개서 쓸것이다보니
    # 맨 마지막에 빈 문자열 하나 추가해 줘야함
    content = word.content + ' '
    # 해당 article이 가지고 있는 모든 해시태그 정보 가져오기
    hashtags = word.hashtags.all()

    #해시 태그 하나씩 꺼내서
    for hashtag in hashtags:
        #기존의 content 본문에서
        #내가 원하는 부분만 바꿀 것이다.
        '''
        test
        #django
        #python
        ---
        test
        <a href="/articles/5/hashtag">#django</a>
        <a href="/articles/5/hashtag">#python</a>
        '''
        link = f'<a href="/articles/{hashtag.pk}/hashtag">{hashtag.content}</a>'
        content = content.replace(hashtag.content + ' ', link)
    return content
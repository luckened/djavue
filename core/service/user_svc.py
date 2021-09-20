from core.models import User, Tweet, Seguindo


def get_details(logged_user, username):
    user = User.objects.get(username=username)
    q = Tweet.objects.filter(user=user).order_by('-created_at')

    last_tweet = ''
    if q.count() > 0:
        last_tweet = q[0].content

    is_following = False
    if logged_user:
        is_following = Seguindo.objects.filter(de=logged_user, para=user).count() > 0

    return {
        'username': user.username,
        'author_avatar': 'todo',
        'last_tweet': last_tweet,
        'is_following': is_following
    }
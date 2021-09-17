from core.models import Seguindo, Tweet, User
from django.db.models import Q


def toggle_follow(user, username, value):
    userpara = User.objects.get(username=username)

    if value:
        if Seguindo.objects.filter(de=user, para=userpara).count() == 0:
            Seguindo.objects.create(de=user, para=userpara)
    else:
        Seguindo.objects.filter(de=user, para=userpara).delete()


def tweet(user, content):
    tweet = Tweet.objects.create(user=user, content=content)
    return tweet.to_dict_json()


def list_tweets(logged_user, username):
    if username:
        tweets = Tweet.objects.filter(user__username=username)
    else:
        if logged_user:
            tweets = Tweet.objects.filter(
                Q(user__in=User.objects.filter(seguindo_para__de=logged_user)) |
                Q(user=logged_user)
            )
        else:
            tweets = Tweet.objects.all()
    tweets = tweets.order_by('-created_at')
    return [t.to_dict_json() for t in tweets]

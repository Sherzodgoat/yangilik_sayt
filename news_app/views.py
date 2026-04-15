from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from .forms import ContactForm

# ko'rilhanlar sonini sanash
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin


from .forms import  CommentForm
from .models import News, Category, Comment

from yangiliklar_sayti.custom_permission import OnlyLoginSuperUser


def news_list_view(request):
    news_list_slade = News.published.all()
    latest_news_5 = News.published.all()[:5]
    iqtisodiy_news_one = News.published.filter(category__nomi='Iqtisodiy')[0]
    iqtisodiy_news_4 = News.published.filter(category__nomi='Iqtisodiy')[1:5]
    mahalliy_news = News.published.filter(category__nomi='Mahalliy')[0:5]
    texnologiya_news = News.published.filter(category__nomi='Texnalogiya')[:5]
    siyosiy_news_one = News.published.filter(category__nomi='Siyosiy')[0]
    siyosiy_news_4 = News.published.filter(category__nomi='Siyosiy')[1:5]
    sport_news = News.published.filter(category__nomi='Sport')[:5]
    uz_news = News.published.filter(category__nomi='O\'zbekiston')[:5]



    context = {
        'news_list': news_list_slade,
        'latest_news_5': latest_news_5,
        'iqtisodiy_news_one': iqtisodiy_news_one,
        'iqtisodiy_news_4': iqtisodiy_news_4,
        'mahalliy_news': mahalliy_news,
        'texnologiya_news': texnologiya_news,
        'siyosiy_news_one': siyosiy_news_one,
        'siyosiy_news_4': siyosiy_news_4,
        'sport_news': sport_news,
        'uz_news': uz_news,
    }

    return render(request, template_name='index.html', context=context)




def news_detail_view(request, slug):

    news_list_slade = News.published.all()
    news_detail = News.published.get(slug=slug)
    context = {}
    hit_count = get_hitcount_model().objects.get_for_object(news_detail)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits


    # news = News.published.get(slug = slug)

    form = CommentForm()
    comments = Comment.objects.filter(news=news_detail)
    # comments = news_detail.comments.filter(active=True)
    yaqin_news = News.objects.filter(category__nomi=news_detail.category )[:3]

    context = {
        'news_detail': news_detail,
        'yaqin_news': yaqin_news,
        'comments' : comments,
        'form' : form,
        'news_list': news_list_slade,
    }
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse("Iltimos, avval login qiling")

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_detail
            comment.user = request.user
            comment.save()
            return render(request, template_name='single_page.html', context=context)

    return render(request, template_name='single_page.html', context=context)



def texno_news_view(request):
    news_list = News.published.filter(category__nomi='Texnalogiya')
    latest_news_5 = News.published.all()[:5]

    context = {
        'news_list': news_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='texno.html', context=context)


def sport_news_view(request):
    news_list = News.published.filter(category__nomi='Sport')
    latest_news_5 = News.published.all()[:5]

    context = {
        'news_list': news_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='sport.html', context=context)


def uz_news_view(request):
    news_list = News.published.filter(category__nomi='O\'zbekiston')
    latest_news_5 = News.published.all()[:5]

    context = {
        'news_list': news_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='uz.html', context=context)


def siyosiy_news_view(request):
    news_list = News.published.filter(category__nomi='Siyosiy')
    latest_news_5 = News.published.all()[:5]

    context = {
        'news_list': news_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='siyosi.html', context=context)


def iqtisodiy_news_view(request):
    news_list = News.published.filter(category__nomi='Iqtisodiy')
    latest_news_5 = News.published.all()[:5]

    context = {
        'news_list': news_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='iqtisodiy.html', context=context)





def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Xabaringiz yuborildi")
        else:
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


class NewsUpdateView(OnlyLoginSuperUser, UpdateView):
    model = News
    template_name = 'crud/update.html'
    fields = ['title', 'body', 'category', 'slug', 'image', 'status']


class NewsDeleteView(OnlyLoginSuperUser,DeleteView):
    model = News
    success_url = reverse_lazy('home_page')
    template_name = 'crud/delete.html'


class NewsCreateView(OnlyLoginSuperUser,CreateView):
    model = News
    fields = ['title', 'body', 'category', 'slug', 'image', 'status']
    template_name = 'crud/create.html'
    success_url = reverse_lazy('home_page')

from django.shortcuts import render
# import time

# from apscheduler.schedulers.background import BackgroundScheduler
# import feedparser
# from .models import Feed

# from django.views import View
# # Create your views here.

# scheduler = BackgroundScheduler()

# def job_function():
#     feed = feedparser.parse('http://www.zone-h.org/rss/specialdefacements')
#     entries = []
#     for entry in feed.entries:
#         entries.append({
#             'title' : entry.title,
#             'link' : entry.link,
#             'published' : entry.published
#         })
#     print('task is running')


# scheduler.add_job(job_function, 'interval', seconds=60*2)

# scheduler.start()

# def feed_view(request):
#     feed = feedparser.parse('http://www.zone-h.org/rss/specialdefacements')
#     entries = []
#     for entry in feed.entries:
#         entries.append({
#             'title' : entry.title,
#             'link' : entry.link,
#             'published' : entry.published
#         })
#     context = {'data' : entries}
#     return render(request, 'Function/feed.html', context)

from apscheduler.schedulers.background import BackgroundScheduler
import feedparser

scheduler = BackgroundScheduler()

class JobScheduler:
    jobs = {}

    @classmethod
    def add_job(cls, url, interval):
        job = scheduler.add_job(cls.job_function, 'interval', seconds=interval, args=[url])
        cls.jobs[url] = job

    @classmethod
    def remove_job(cls, url):
        if url in cls.jobs:
            job = cls.jobs.pop(url)
            job.remove()

    @staticmethod
    def job_function(url):
        feed = feedparser.parse(url)
        entries = []
        for entry in entries:
            entries.append({
                'title' : entry.title,
                'link' : entry.link,
                'published' : entry.published
            })
        print('Task is running for' , url)

JobScheduler.add_job('http://www.zone-h.org/rss/specialdefacements', 120)
JobScheduler.add_job('http://example.com/rss', 180)



def feed_view(request):
    feed = feedparser.parse('http://www.zone-h.org/rss/specialdefacements')
    entries = []
    for entry in feed.entries:
        entries.append({
            'title' : entry.title,
            'link' : entry.link,
            'published' : entry.published
        })
    context = {'data' : entries}
    return render(request, 'Function/search.html', context)

scheduler.start()
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from markdown2 import Markdown

from . import util


# define the forms we will use in this project
class SearchForm(forms.Form):
    q = forms.CharField(label="")
    q.widget.attrs.update({'class': 'search'})
    q.widget.attrs.update(placeholder='Search Encyclopedia')


class NewPageForm(forms.Form):
    title = forms.CharField(label="", max_length=100, min_length=1)
    title.widget.attrs.update({'class': 'new_page_title'})
    title.widget.attrs.update(placeholder='title to be included page list')
    entry = forms.CharField(label="", widget=forms.Textarea, min_length=24)
    entry.widget.attrs.update({'class': 'textarea'})
    entry.widget.attrs.update(placeholder='# ADD PAGE TITLE HERE, after #, with article to follow on a new line.')


# define a global var for the markdown converter
markdowner = Markdown()


# define some view functions to render our pages, as follows
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "SearchForm": SearchForm()
    })


def article(request, entry_name):
    # lets get the content for this entry
    content = util.get_entry(entry_name)

    # we will assume there is an entry and attempt to get it
    # if, instead, we get None, there is no such entry
    is_entry = True
    if content is None:
        is_entry = False
        content = ""

    # rendor the article page
    return render(request, "encyclopedia/article.html", {
        "is_entry": is_entry,
        "entry_name": entry_name.upper(),
        "content": markdowner.convert(content),
        "SearchForm": SearchForm()
    })


def find(request):
    if request.method == "POST":
        # let's get the query term from the form and find out if we have such an entry
        # if so, we'll redirect to that page
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data["q"]
            entries = util.list_entries()
            for entry in entries:
                if q.lower() == entry.lower():
                    return HttpResponseRedirect(reverse('article', kwargs={'entry_name': q}))

            # if we are here, the article is not in the encyclopedia. instead of
            # redirecting to the article, we will provide the user with a list of
            # possible alternative entries
            similar_entries = []
            for entry in entries:
                if q.lower().strip() in entry.lower():
                    similar_entries.append(entry)

            return render(request, "encyclopedia/find.html", {
                "q": q.upper(),
                "entries": similar_entries,
                "SearchForm": SearchForm()
            })


def add(request):
    if request.method == "POST":
        # if we are submitting a new article, check for duplicates
        # if it is a duplicate, send error message to the user
        # FUTURE ADD: DJANGO FORM ERROR MESSAGES HERE
        form = NewPageForm(request.POST)
        is_duplicate = False
        if form.is_valid():
            titles = util.list_entries()
            for title in titles:
                if title.lower() == form.cleaned_data["title"].lower().strip():
                    is_duplicate = True

                    # if we have duplicate. submit the error back to the user
                    # with the original form data
                    return render(request, "encyclopedia/add.html", {
                        "NewPageForm": form,
                        "is_duplicate": is_duplicate
                    })

            # if we are here, we have a new valid entry. save it to entries, then take
            # the user to their new article
            util.save_entry(form.cleaned_data["title"].capitalize(), form.cleaned_data["entry"])
            return HttpResponseRedirect(reverse('article', kwargs={'entry_name': form.cleaned_data["title"]}))
    else:
        # render the page with the empty form
        return render(request, "encyclopedia/add.html", {
            "NewPageForm": NewPageForm(),
            "SearchForm": SearchForm()
        })


def edit(request, entry_name):
    if request.method == "POST":
        # submit the changes to the encyclopedia, so long as we have
        # a valid form
        form = NewPageForm(request.POST)
        if form.is_valid():
            util.save_entry(form.cleaned_data["title"].capitalize(), form.cleaned_data["entry"])
            return HttpResponseRedirect(reverse('article', kwargs={'entry_name': form.cleaned_data["title"]}))
    else:
        # let's bind the current entry to the form and hide the title
        # since we will not allow the user to change it
        form = NewPageForm({"title": entry_name, "entry": util.get_entry(entry_name)})
        form.fields["title"].widget = forms.HiddenInput()

        return render(request, "encyclopedia/edit.html", {
            "entry_name": entry_name,
            "NewPageForm": form,
            "SearchForm": SearchForm()
        })


def r_article(request):
    # get a random title from the title list and then redirect to the article url
    return HttpResponseRedirect(reverse('article', kwargs={'entry_name': util.get_random()}))

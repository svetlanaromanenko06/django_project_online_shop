from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'date_of_creation', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_bl = form.save()
            new_bl.slug = slugify(new_bl.title)
            new_bl.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'date_of_creation', 'is_published')
    #success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_bl = form.save()
            new_bl.slug = slugify(new_bl.title)
            new_bl.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
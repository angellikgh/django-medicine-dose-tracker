from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import (list, edit)
from django.views.generic.base import TemplateResponseMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Medicine
from .forms import MedicineEditForm


def home_view(request):
    return render(request, 'home.html', {})


class ListCreateView(edit.BaseCreateView, list.BaseListView, TemplateResponseMixin):
    template_name = 'medicines/list_create.html'
    model = Medicine
    form_class = MedicineEditForm
    success_url = reverse_lazy('medicines:list')

    def get_queryset(self):
        qs = super(ListCreateView, self).get_queryset()
        qs = qs.filter(user=self.request.user).order_by('-created_at')
        return qs

    def get(self, request, *args, **kwargs):
        formView = edit.BaseCreateView.get(self, request, *args, **kwargs)
        listView = list.BaseListView.get(self, request, *args, **kwargs)
        formData = formView.context_data['form']
        listData = listView.context_data['object_list']
        return render(request, 'medicines/list_create.html', {'form': formData, 'track_list': listData})

    def post(self, request, *args, **kwargs):
        form = MedicineEditForm(data=request.POST)
        if form.is_valid():
            medicine = form.save()
            medicine.user.add(request.user)
            messages.success(
                request, f'Added medicine successfully.', extra_tags='alert alert-success alert-dismissible fade show')
            return self.form_valid(form)
        else:
            messages.error(
                request, f'Failed to add medicine.', extra_tags='alert alert-error alert-dismissible fade show')
            return self.form_invalid(form)


class EditView(edit.UpdateView):
    model = Medicine
    template_name = 'medicines/edit.html'
    form_class = MedicineEditForm
    success_url = reverse_lazy('medicines:list')

    def post(self, request, *args, **kwargs):
        form = MedicineEditForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Updated medicine successfully.', extra_tags='alert alert-success alert-dismissible fade show')
            return self.form_valid(form)
        else:
            messages.error(
                request, f'Failed to update medicine.', extra_tags='alert alert-error alert-dismissible fade show')
            return self.form_invalid(form)


class DeleteView(edit.DeleteView):
    model = Medicine
    success_url = reverse_lazy('medicines:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object is not None:
            messages.success(request, f'Deleted medicine successfully',
                             extra_tags='alert alert-success alert-dismissible fade show')
            return super(DeleteView, self).delete(request, *args, **kwargs)
        else:
            raise Http404("Object you are looking for doesn't exist")

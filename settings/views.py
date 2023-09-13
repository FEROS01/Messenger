from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages

from settings.forms import ProfileForm, InfoForm


@login_required
def settings(request):
    return render(request, "settings/setting.html")


@login_required
def edit_prof(request):
    info = request.user.info
    if request.method != "POST":
        prof_form = ProfileForm(instance=request.user)
        info_form = InfoForm(instance=info)
    else:
        prof_form = ProfileForm(
            request.POST, request.FILES, instance=request.user)
        info_form = InfoForm(request.POST, request.FILES, instance=info)
        if prof_form.is_valid() and info_form.is_valid():
            prof_form.save()
            info_form.save()
            messages.success(request, "Profile updated")
            return redirect("messengers:user_bio", user_id=request.user.id)
    context = {"prof_form": prof_form, "info_form": info_form}
    return render(request, "settings/edit_prof.html", context)


@login_required
def edit_pass(request):
    if request.method != "POST":
        form = PasswordChangeForm(request.user)
    else:
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password change succesful")
            return redirect("settings:setting")
    context = {"form": form}
    return render(request, "settings/edit_pass.html", context)

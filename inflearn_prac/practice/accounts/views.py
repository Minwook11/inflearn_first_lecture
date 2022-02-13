from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from .forms import ProfileForm
from .models import Profile

@login_required
def profile(request):
	return render(request, 'accounts/profile_form.html')

#class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#	model = Profile
#	form_class = ProfileForm
#
#profile_edit = ProfileUpdateView.as_view()

@login_required
def profile_edit(request):
	try:
		profile = request.user.profile
	except Profile.DoesNotExist:
		profile = None

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid:
			form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('profile')
	else:
		form = ProfileForm(instance=profile)
	return render(request, 'accounts/profile_edit.html',
		{'form' : form
	})


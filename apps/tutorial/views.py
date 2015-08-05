import subprocess
import json      
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class TutorialView(TemplateView):
    template_name = "tutorial/index.html"

    def get(self,request, *args, **kwargs):
    	cmd = self.request.GET.get('cmd', None)
    	git_output = None
    	if cmd:
    		git_output = subprocess.check_output(cmd.split(" "), stderr=subprocess.STDOUT)
    		return HttpResponse(json.dumps({'output': git_output}))
    	return render(self.request, self.template_name)
        

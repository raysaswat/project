from django.shortcuts import render
from app.models import App
import requests, ast

# Create your views here.
def fun(request):
  resp = requests.get("http://3.13.9.182:8081/cb/get_top_keywords")
  keydata = resp.text
  respcontext = requests.get("http://3.13.9.182:8082/cb/get_chat_context")
  contextdata = respcontext.text
  respquestion = requests.get("http://3.13.9.182:8081/cb/get_top_questions")
  questiondata = respquestion.text
  question_dict = ast.literal_eval(questiondata)
  output_question = question_dict['top_questions']
  q0 = output_question[0]
  q1 = output_question[1]
  q2 = output_question[2]
  q3 = output_question[3]
  q4 = output_question[4]
  q5 = output_question[5]
  q6 = output_question[6]
  q7 = output_question[7]
  q8 = output_question[8]
  q9 = output_question[9]
  respavgtime = requests.get("http://3.13.9.182:8081/cb/get_avg_conv_time")
  avgtime = respavgtime.text
  avgtime_dict = ast.literal_eval(avgtime)
  output_avgtime = avgtime_dict['avg_conversation_time']
  resprating = requests.get("http://3.13.9.182:8081/cb/get_avg_rating")
  avgrating = resprating.text
  avgrating_dict = ast.literal_eval(avgrating)
  output_avgrating = avgrating_dict['avg_rating']
  resplocation = requests.get("http://3.13.9.182:8081/cb/get_top_locations")
  locdata = resplocation.text
  loc_dict = ast.literal_eval(locdata)
  output_loc = loc_dict['top_locations']
  p0 = output_loc[0]
  p1 = output_loc[1]
  p2 = output_loc[2]
  p3 = output_loc[3]
  p4 = output_loc[4]
  p5 = output_loc[5]
  p6 = output_loc[6]
  p7 = output_loc[7]
  p8 = output_loc[8]
  p9 = output_loc[9]
  return render(request, 'home.html',{'keydata':keydata, 'contextdata':contextdata, 'q0':q0, 'q1':q1, 'q2':q2, 'q3':q3,'q4':q4, 'q5':q5, 'q6':q6, 'q7':q7, 'q8': q8, 'q9':q9, 'output_avgtime':output_avgtime, 'output_avgrating': output_avgrating, 'p0':p0, 'p1':p1, 'p2':p2, 'p3':p3,'p4':p4, 'p5':p5, 'p6':p6, 'p7':p7, 'p8': p8, 'p9':p9})
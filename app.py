from flask import Flask, render_template, jsonify, request, make_response
from database import load_profile_questions_from_db, load_survey_questions_from_db, add_profile_to_db, add_survey_to_db

from generate_radom_survey import generate_random_survey, num_element_per_vignette

import time

app = Flask(__name__)


@app.route("/")
def hello():
  return render_template("home.html")


@app.route("/survey")
def hello_mind():
  survey_questions = generate_random_survey()
  return render_template("survey.html",
                         survey_questions=survey_questions,
                         N=num_element_per_vignette)


@app.route("/survey/submit", methods=['post'])
def submit_survey():

  survey_questions = generate_random_survey()

  data = request.get_json()
 

  # r_time = float(data.get('elapsed_time', 0))
  # if the 'elapsed_time' field is not present in the form data, return a default value of 0

  #add_survey_to_db(data, r_time)

  return render_template("survey_submitted.html",
                        data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

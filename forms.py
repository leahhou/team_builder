from wtforms import Form, RadioField, SelectMultipleField, SubmitField, validators
from wtforms_components import IntegerSliderField

class ProfileForm(Form):
    position = RadioField(u'Which position do you prefer working in?', choices=[("be", "Back-end"), ("fe", "Front-end"), ("fs", "Full-stack")], validators=[validators.input_required("Input is required")], coerce=str)
    languages = SelectMultipleField(u'Which languages do you know?', choices=[("py", "Python"), ("ry", "Ruby"), ("java", "Java"), ("js", "Javasript"), ("c", "C"), ("ch", "C#"), ("cpp", "C++"), ("php", "PHP"), ("http", "HTML"), ("css", "CSS"), ("perl", "Perl"), ("swift", "Swift")], validators=[validators.input_required("Input is required")], coerce=str)
    experience = RadioField(u'What is your experience level', choices=[("<1", "Under 1 year"), ("1-3", "1-3 years"), ("3-5", "3-5 years"), ("5+", "5+ years")], validators=[validators.input_required("Input is required")])
    objective = RadioField(u'What is your objective in this Hackathon?', choices=[("win", "Winning a prize"), ("learn", "Learning new things"), ("network", "Networking")], validators=[validators.input_required("Input is required")])
    ideas = IntegerSliderField(u'How passionate are you about your idea?', validators=[validators.number_range(0, 10), validators.input_required("Input is required")])
    submit = SubmitField(u"Submit")
    cancel = SubmitField(u"Cancel")
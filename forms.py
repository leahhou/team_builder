from wtforms import Form, RadioField, SelectMultipleField, DecimalRangeField, validators

class ProfileForm(Form):
    position = RadioField(u'Which position do you prefer working in?', choices=["Back-end", "Front-end", "Full-stack"])
    languages = SelectMultipleField(u'Which languages do you know?', choices=["Python","Ruby","Java","Javasript", "C", "C#","C++","PHP",
    "HTML","CSS","Perl","Swift"])
    experience = RadioField(u'What is your experience level', choices=["Under 1 year", "1-3 years", "3-5 years", "5+ years"])
    objective = RadioField(u'What is your objective in this Hackathon?', choices=["Winning a prize","Learning new things", "Networking"])
    ideas = RadioField(u'How passionate are you about your idea?')
import datetime
import random
from flask import Flask, render_template

app = Flask(__name__)

weekday_tag = datetime.datetime.today().weekday() + 1
today = datetime.datetime.now().strftime("%B %d, %Y")


@app.route('/')
def front():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/tasks')
def tasks():
    return render_template("tasks.html")


def weekday():
    motivational_weekdays = ['Mindful Monday', 'Transformation Tuesday', 'Wisdom Wednesday', 'Thoughtful Thursday',
                             'Friday Focus', 'Magical Saturday', "Spotlight Sunday"]
    if weekday_tag == 1:
        return motivational_weekdays[0]
    elif weekday_tag == 2:
        return motivational_weekdays[1]
    elif weekday_tag == 3:
        return motivational_weekdays[2]
    elif weekday_tag == 4:
        return motivational_weekdays[3]
    elif weekday_tag == 5:
        return motivational_weekdays[4]
    elif weekday_tag == 6:
        return motivational_weekdays[5]
    elif weekday_tag == 7:
        return motivational_weekdays[6]


@app.route('/motivation')
def motivation():
    day = weekday()
    motivational_quotes = ['The best way to get started is to quit talking and begin doing.',
                           'The pessimist sees difficulty in every opportunity. '
                           'The optimist sees opportunity in every difficulty.',
                           'Don\'t let yesterday take up too much of today.',
                           'You learn more from failure than from success. Dont let it stop you. '
                           'Failure builds character.',
                           'Its not whether you get knocked down, its whether you get up.',
                           'If you are working on something that you really care about, you dont have to be pushed. '
                           'The vision pulls you.',
                           'People who are crazy enough to think they can change the world, are the ones who do.',
                           'Failure will never overtake me if my determination to succeed is strong enough.',
                           'Entrepreneurs are great at dealing with uncertainty and also very good at minimizing risk. '
                           'That\'s the classic entrepreneur.',
                           'We may encounter many defeats but we must not be defeated.']
    quote = random.choice(motivational_quotes)
    story_of_the_day = random.randint(0, 9)
    motivational_story_headings = ['Laziness won’t get you anywhere', 'Don’t say something you regret out of anger',
                                   'Stop wasting your time complaining', 'Damaged souls still have worth',
                                   'Never let one failure from the past hold you back in the future',
                                   'Struggling will make you stronger',
                                   'Your reaction matters more than what happens to you',
                                   'Don’t insult the things you wish you could have',
                                   'Be kind to others even if it hurts you', 'Ignore the haters']
    story_heading = motivational_story_headings[story_of_the_day]
    with open(f'motivational_stories/{story_of_the_day + 1}.txt', encoding="utf8") as story_chosen:
        story = story_chosen.read()
    return render_template("motivation.html", quote=quote, day=day, story_heading=story_heading, story=story, date=today)


@app.route('/success_story')
def success_story():
    story_of_the_day = random.randint(0, 9)
    successful_people = ['Steve Jobs', 'Bill Gates', 'Albert Einstein', 'Abraham Lincoln', 'J.K.Rowling',
                         'Michael Jordan', 'Walt Disney', 'Vincent Van Gogh', 'Stephen King', 'Steven Spielberg']
    person = successful_people[story_of_the_day]
    with open(f'success_stories/{story_of_the_day + 1}.txt', encoding="utf8") as success:
        story = success.read()
    return render_template('generic.html', person=person, success_story=story, date=today)


if __name__ == "__main__":
    app.run(debug=True)

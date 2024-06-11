from flask import Blueprint, render_template, request, flash
from weather_app.weather import get_weather
from weather_app.forms import WeatherForm
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = WeatherForm()
    data = None
    if form.validate_on_submit():
        city = form.city.data
        state = form.state.data
        country = form.country.data
        data = get_weather(city, state, country)
        if data == None:
            flash('Location not found', 'danger')

    return render_template('index.html', data=data, form=form)

##### Rehotsauce controller_"hotsauce" to be in line with project #####

from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.model_hotsauce import Hotsauce##### Rehotsauce to match model file #####
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    all_hotsauces = Hotsauce.get_all()
    return render_template('index.html', all_hotsauces = all_hotsauces)



# C **************************************************
# C **************************************************
# C **************************************************


@app.route('/ferment/new') 
def new_ferment():
    return render_template('/ferment_new.html')

# @app.route('/hotsauce/new') 
# def new_hotsauce():
#     return render_template('/')

@app.route('/ferment/create', methods=['POST'])
def create_ferment():
    ferment_data = {
        **request.form
    }

    is_valid = Hotsauce.validate_ferment(request.form)
    
    if not is_valid:
        return redirect('/ferment/new')

    Hotsauce.create_ferment(ferment_data)
    return redirect('/dashboard')

# @app.route('/hotsauce/create', methods=['POST'])
# def create_hotsauce():
#     return redirect('/')


# R **************************************************
# R **************************************************
# R **************************************************


# @app.route('/hotsauce/show_all')
# def get_all_hotsauce():
#     return 'get all hotsauce'

@app.route('/hotsauce/<int:id>')
def get_one(id):
    context = {
        'hotsauce' : Hotsauce.get_one({'id':id}),

    }
    print(context['hotsauce'].ferment_start)
    return render_template ('hotsauce_view.html', **context)



# U **************************************************
# U **************************************************
# U **************************************************

@app.route('/ferment/<int:id>/process')
def ferment_process(id):
    # context = {
    #     'hotsauce' : Hotsauce.get_one({id:id})
    # }
    return render_template('/ferment_process.html', id = id)

@app.route('/hotsauce/<int:id>/edit')
def edit_hotsauce(id):
    context = {
        'hotsauce' : Hotsauce.get_one({'id':id})
    }
    return render_template('/hotsauce_edit.html',**context)

@app.route('/ferment/<int:id>/update', methods=['POST'])
def update_one(id):
    hotsauce_data = {
        **request.form,
        'id' : id
    }
    
    is_valid = Hotsauce.validate_process(request.form)
    
    if not is_valid:
        return redirect(f'/ferment/{id}/process')

    Hotsauce.update_one(hotsauce_data)
    return redirect('/dashboard')

@app.route('/hotsauce/<int:id>/update', methods=['POST'])
def update_hotsauce(id):
    hotsauce_data = {
        **request.form,
        'id' : id
    }

    Hotsauce.update_hotsauce(hotsauce_data)
    return redirect('/dashboard')

# D **************************************************
# D **************************************************
# D **************************************************


@app.route('/hotsauce/<int:id>/delete')
def delete_one_hotsauce(id):
    Hotsauce.delete_one_hotsauce({'id':id})
    return redirect('/dashboard')
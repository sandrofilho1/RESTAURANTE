from flask import redirect, render_template, url_for, flash, request
from .forms import Addprodutos
from sistema import db, app
from .models import Prato, Categoria


@app.route('/addprato', methods=['GET','POST'])
def addprato():
    if request.method == 'POST':
        getprato = request.form.get('prato')
        prato = Prato(name=getprato)
        db.session.add(prato)
        flash(f'O prato {getprato} foi cadastrado com sucesso','success')
        db.session.commit()
        return redirect(url_for('addprato'))
    return render_template('/produtos/addprato.html', pratos='pratos')


@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if request.method == 'POST':
        getcat = request.form.get('categoria')
        cat = Categoria(name=getcat)
        db.session.add(cat)
        flash(f'O categoria {getcat} foi cadastrado com sucesso','success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('/produtos/addprato.html')

@app.route('/addproduto', methods=['GET','POST'])
def addproduto():
    form = Addprodutos(request.form)
    return render_template('produtos/addproduto.html',title='Cadastrar produtos',form=form)
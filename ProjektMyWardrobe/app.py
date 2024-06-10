from flask import Flask, render_template, request, redirect, url_for, jsonify

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///garderoba.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class GarderobaItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(20), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    style = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    breadcrumb = [('Home', url_for('home'))]
    return render_template('home.html', breadcrumb=breadcrumb)

@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    breadcrumb = [
        ('Home', url_for('home')),
        ('Dodaj', url_for('dodaj'))
    ]
    if request.method == 'POST':
        new_item = GarderobaItem(
            category=request.form['category'],
            color=request.form['color'],
            size=request.form['size'],
            season=request.form['season'],
            brand=request.form['brand'],
            style=request.form['style']
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('popis'))
    return render_template('dodaj.html', breadcrumb=breadcrumb)

@app.route('/popis', methods=['GET', 'POST'])
def popis():
    breadcrumb = [
        ('Home', url_for('home')),
        ('Popis', url_for('popis'))
    ]
    if request.method == 'POST':
        category_filter = request.form.get('category')
        brand_filter = request.form.get('brand')
        season_filter = request.form.get('season')
        size_filter = request.form.get('size')
        style_filter = request.form.get('style')
        color_filter = request.form.get('color')
        query = GarderobaItem.query
        if category_filter:
            query = query.filter_by(category=category_filter)
        if brand_filter:
            query = query.filter_by(brand=brand_filter)
        if season_filter:
            query = query.filter_by(season=season_filter)
        if size_filter:
            query = query.filter_by(size=size_filter)
        if style_filter:
            query = query.filter_by(style=style_filter)
        if color_filter:
            query = query.filter_by(color=color_filter)
        garderoba = query.all()
    else:
        garderoba = GarderobaItem.query.all()

    categories = db.session.query(GarderobaItem.category).distinct().all()
    categories = [category[0] for category in categories]

    brands = db.session.query(GarderobaItem.brand).distinct().all()
    brands = [brand[0] for brand in brands]

    seasons = db.session.query(GarderobaItem.season).distinct().all()
    seasons = [season[0] for season in seasons]

    sizes = db.session.query(GarderobaItem.size).distinct().all()
    sizes = [size[0] for size in sizes]

    styles = db.session.query(GarderobaItem.style).distinct().all()
    styles = [style[0] for style in styles]

    colors = db.session.query(GarderobaItem.color).distinct().all()
    colors = [color[0] for color in colors]

    return render_template('popis.html', garderoba=garderoba, categories=categories, brands=brands, seasons=seasons, sizes=sizes, styles=styles, colors=colors, breadcrumb=breadcrumb)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    item = GarderobaItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('popis'))

@app.route('/uredi/<int:id>', methods=['GET', 'POST'])
def uredi(id):
    breadcrumb = [
        ('Home', url_for('home')),
        ('Popis', url_for('popis')),
        ('Uredi', url_for('uredi', id=id))
    ]
    item = GarderobaItem.query.get_or_404(id)
    if request.method == 'POST':
        item.category = request.form['category']
        item.color = request.form['color']
        item.size = request.form['size']
        item.season = request.form['season']
        item.brand = request.form['brand']
        item.style = request.form['style']
        db.session.commit()
        return redirect(url_for('popis'))
    return render_template('uredi.html', item=item, breadcrumb=breadcrumb)

@app.route('/vizualizacija')
def vizualizacija():
    breadcrumb = [
        ('Home', url_for('home')),
        ('Vizualizacija', url_for('vizualizacija'))
    ]
    return render_template('vizualizacija.html', breadcrumb=breadcrumb)

@app.route('/api/odjevni_predmeti')
def api_odjevni_predmeti():
    garderoba = GarderobaItem.query.all()
    data = [
        {
            'id': item.id,
            'kategorija': item.category,
            'boja': item.color,
            'velicina': item.size,
            'sezona': item.season,
            'brend': item.brand,
            'stil': item.style
        }
        for item in garderoba
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

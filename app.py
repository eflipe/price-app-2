import os
from flask import Flask, render_template
from models.item import Dolar
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.item import item_blueprint
from views.users import user_blueprint

#url = 'http://rava.com/empresas/perfil.php?e=MERVAL'
#tag_name = "span[class='fontsize6']"

#item = Dolar(url, tag_name)
#print(item.buscar_precio())
#item.save_to_mongo()
#print(item.buscar_precio())

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

@app.route('/')
def home():
    return render_template('home.html')

app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(item_blueprint, url_prefix="/items")
app.register_blueprint(user_blueprint, url_prefix="/users")
if __name__ == '__main__':
    app.run(debug=True)


#from models.alert import Alert



#alert = Alert("dcd8abfae46e4588a83591f885ab0065", 62)
#alert.save_to_mongo()




#buscar_item = Dolar.all()
#print(buscar_item)
#print(buscar_item[0].buscar_precio())



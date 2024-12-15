from flask import Flask
import random

app = Flask(__name__)
liste = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.","2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."]
@app.route("/")
def hello_world():
    return f'<p>{"Selam, Hadi şuradaki tuşa bas ve teknoloji bağımlıları ile alakalı bir kaç bilgi öğren(bilgiyi değiştirmek için sayfayı yenile)"}</p><ul> <li><a href="/rastgele_gercek">Rastgele Gerçek</a></li> <li><a href="/yazi_tura">Yazı-Tura</a></li> </ul> '
@app.route("/rastgele_gercek")
def random_gercek():
    return f'<p>{random.choice(liste)}</p><a href="/">Ana Sayfa</a>'
@app.route("/yazi_tura")
def yazi_tura():
    return f'<p>{random.choice(["yazı","tura"])}</p>'

app.run(debug=True)

import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def heimasida():
    return """
        <h2> Verkefni 3</h2>
        <p>
        <a href="/lidur1"> Liður 1 </a> --
        <a href="/lidur2"> Liður 2 </a> 
        </p>
        """

@app.route("/lidur1")
def kennitolusida():
    return  render_template("default.html")

frettir = [
    ["0", "Flugfargjöld lækkað á nýjan leik","Flugfargjöld til útgjalda sem undirliður í vísitölu neysluverðs lækkuðu í bæði júlí og ágúst eftir að hafa hækkað þrjá mánuði í röð í kjölfar gjaldþrots WOW air. Áður en WOW air lenti í síðasta sinn höfðu flugfargjöld lækkað 42 mánuði eða frá október 2015. Þetta var meðal þess sem kom fram í ferðaþjónustuúttekt Arion banka sem kom út í gær. ", "ritstjorn@vb.is"],
    ["1", "Vendingar á hlutabréfamörkuðum", "Á yfirborðin virðist allt með kyrrum kjörum á hlutabréfamörkuðum þessa dagana en Financial Times greinir frá því að undir niðri hafi miklar sviptingar átt sér stað. Þrátt fyrir að FTSE heimsvístalan (e. All-World equity index) hafi hækkað um nær 3% það sem af er septembermánuði hafi mikil sala verið í vinsælum hlutabréfum í vikunni. Svo mikil að tala megi um hrun sem miðlarar hafa nú þegar gefið nafnið “stundar hrunið” (e.momentum crash). ", "Ritstjórnritstjorn@vb.is"],
    ["2", "Tekjur Hafnarfjarðar tæpir 14 milljarðar", "Rekstrarniðurstaða Hafnarfjarðarbæjar á fyrri hluta ársins 2019 var jákvæð um 123 milljónir króna en áætlun gerði ráð fyrir að rekstrarafgangur yrði 469 milljónir króna. Helstu frávik eru að framlög jöfnunarsjóðs voru undir áætlun um 116 milljónir króna, aðrar tekjur voru um 102 milljónum króna umfram áætlun og annar rekstrarkostnaður var um 289 milljónum króna hærri en áætlun gerði ráð fyrir.  ", "ritstjorn@vb.is"],
    ["3", "20 tilboð bárust í útboði Landsbankans","Samtals bauð Landsbankinn út fjóra flokka sértryggðra skuldabréfa og bárust 20 tilboð fyrir samtals 3.480 milljónir króna að nafnverði. " , "ritstjorn@vb.is"]
]

@app.route("/sida/<kt>")
def page(kt):
    summa = 0
    for item in kt:
        summa = summa + int(item)

    return render_template("kt_summa.html", kt=kt, summa=summa)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True)
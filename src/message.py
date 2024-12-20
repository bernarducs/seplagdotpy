MSG = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Email Content</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;            
        }
       .body__ {
            background-color: #f5f5f5; /* Light grey */
       }
       .banner {
            width: 100%;
            text-align: center;
            padding: 20px 0;
        }
       .banner img {
            max-width: 100%;
            height: auto;
        }
       .container {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: white;
        }
        h1, h2 {
            color: #333;
        }
        ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        .msg {
            font-size:1.25rem;
        }
        .footer {
            background-color: #f5f5f5;
            color: blue;
            text-align: center;
            padding: 3rem;
            font-size:0.75em;
        }
        .grey {
            background-color: #c0c0c0;
        }
    </style>
</head>
<body>
<div class="body__">
    <div class="banner">
        <img src="cid:header_img" alt="Banner Image" width="600" height="300">
    </div>

    <div class="container">
        <p>(Quase) Toda terça, 8h30 da manhã</p>
        <h1>🐍 Encontro 11</h1>
        <div class="msg">
            <h3>Já é amanhã!</h3>
            <p>Vamos falar de <a href="https://pandas.pydata.org/">pandas!</a></p>
            <p><b>5 de Novembro, às 8 e 30 da manhã! Será no 1o andar, sala 6.</b></p>
            <p>Como eu carrego uma conjunto de dados em CSV?</p>
            <p>Como vejo a estrutura geral desse conjunto?</p>
            <p>Como agrupo os dados baseado em um grupo de dimensões?</p>
            <p>Como criar novas colunas ou um novo conjunto de dados a partir dele?</p>
            <p>E como exportar esses dados?</p>
            <p>Até lá!</p>
            <img src="https://geo-python-site.readthedocs.io/en/latest/_images/pandas_logo.png" alt="Imagem carregada" width="600" height="300" />
        </div>
    </div>

    <div class="footer">
        © 2024 - IG/Seplag.py
    </div>    
</div>
</body>
</html>
"""

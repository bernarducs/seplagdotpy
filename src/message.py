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
        <del>Toda</del> terça, 8h30 da manhã
        <h1>🐍 Encontros 9 e 10</h1>
        <div class="msg">
            <h3>Voltamos!</h3>
            <img src="https://media.tenor.com/qdg13PqYbxMAAAAM/yes-baby.gif" alt="yes" width="600" height="350" />
            <p>Já temos sala reservada para os próximos encontros:</p>
            <p><b>17 e 24 de setembro. Às 8 e 30 da manhã!</b></p>
            <p>No dia 17 (terça), iremos montar uma pequena <a href="https://imdbpy.readthedocs.io/en/latest/usage/quickstart.html">base</a> de dados;</p>
            <p>E, na outra terça, vamos usar essa base para apredermos a mais famosa <a href="https://pandas.pydata.org/">biblioteca</a> de análise de dados da linguagem.</p>
            <img src="https://vejasp.abril.com.br/wp-content/uploads/2016/12/cinema-com-os-minions.gif" alt="Imagem carregada" width="600" height="300" />
        </div>
    </div>

    <div class="footer">
        © 2024 - IG/Seplag.py
    </div>    
</div>
</body>
</html>
"""

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
            background-color: #0094FF;
            color: white;
            text-align: center;
            padding: 0.3rem;
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
        <del>Toda terça, 8h30 da manhã</del>
        <h1>🐍 Encontro 8 - 8/8/2024</h1>
        <div class="msg">
            <h3>Feito! Amanhã já podemos nos reunir!</h3>
            <h3>Vamos dar continuidade com os modelos de IA do hugging face com uma atividade prática!</h3>
            <img src="https://c.tenor.com/eTmkE9KZQO4AAAAC/tenor.gif" alt="Imagem carregada" width="600" height="500" />
        </div>
        <div class="footer">
            © 2024 - IG/Seplag.py
        </div>
    </div>
</div>

</body>
</html>
"""

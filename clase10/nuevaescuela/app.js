//Ryan Dhal
//console.log("Este es mi proyecto javascript")

const fs = require('fs')
//console.log(fs)
const folderName = process.argv[2] || 'project'

fs.mkdirSync(folderName)
fs.mkdirSync(`${folderName}/img`)
fs.writeFileSync(
  `${folderName}/index.html`,
  `
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ecomerce</title>
    <link rel="stylesheet" href="style.css">
    <script src="mainjs" defer></script>
</head>
<body>
    <h1>Titulo</h1>
    <h2>slogan de la pagina</h2>
    <nav>
        <ul>
            <li><a href="">item1</a></li>
            <li><a href="">item2</a></li>
            <li><a href="">item3</a></li>
            <li><a href="">item4</a></li>
            <li><a href="">item5</a></li>
        </ul>
    </nav>
</body>
</html>
    `
);
fs.writeFileSync(
  `${folderName}/style.css`,
  `
body {
    background-color: aquamarine;
}

    `
);
fs.writeFileSync(`${folderName}/main.js`, `alert("hola mundo")`);

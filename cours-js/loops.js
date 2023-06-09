// la première déclaration de valeur d'une variable s'appelle initialisation (compteur ou index) (exemple : [let i = 0]
// [i < 10] correspond à la comparaison
// [i++] correspond à un auto incrémment ou décrémemnt
// boucle for classique
for (let i = 0; i < 10; i++) {
    console.log("i = " + i)
}
//boucle for à rebours
for (let i = 10; i > 0; i--){
    console.log("i = " + i);
}

// boucle foreach
let users = ['foo','bar','baz']

// le mot clé "of" permet de récupérer l'élément.
for (let user of users) {
    console.log(user);
}


//le mot clé "in" permet de récupérer l'index de l'élément
for (let i in users) {
    let user = users[i];
    console.log(`i = ${i}, user = ${user}`);
}

// méthode forEach (asynchrone)
users.forEach(
    function(i, user, list){
        console.log(`i = ${i}, user = ${user}`);
    }
);

//syntaxe alternative
users.forEach(
    (i, user, list) => {
        console.log(`i = ${i}, user = ${user}`);
    }
)


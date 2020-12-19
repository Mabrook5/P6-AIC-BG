# P6-AIC-BG

### Script Python de reformatage de texte (ajout-suppression-modification) depuis un fichier .csv ou .txt

Le script est codé en python et permet à un utilisateur via une suite d'action demandée par le script de reformater les lignes d'une colonne d'un fichier .csv ou les lignes d'un fichier .txt

- Menu principal ["def menu()"]
Le menu principal permet de choisir le type de fichier à travailler

- Choix du fichier ["def etapecsv()"] et ["def etapetxt()"]
Une fenêtre s'ouvre afin de choisir le fichier qui est restreint suivant l'extension choisie (.csv ou .txt).
Un fichier tampon est alors créé afin de reformater le contenu.

  - Choix de la colonne du tableau csv [def etapecsvbis()]
Pour le .csv une étape supplémentaire est requise afin de choisir la colonne et ainsi en extraire le contenu.

- Choix du délimiteur [def etape2()]
L'utilisateur doit choisir une valeur (un caractère ou suite de caractères) qui servira de délimiteur pour le reformatage.

- Choix du type de reformatage [def etape3()]
L'utilisateur a le choix d'ajouter, supprimer ou modifier du contenu.

  - Choix du contenu à ajouter [def etape3a()]
Si le choix est d'ajouter du contenu, l'utilisateur définit ce qu'il souhaite ajouter.

  - Inclusion ou non du délimiteur [def etape3b()]
Si le choix est de supprimer du contenu, l'utilisateur définit d'inclure ou non le délimiteur dans la suppression.

- Modification de contenu [def etape3c()]
Si le choix est de modifier du contenu, l'utilisateur définit ce qu'il souhaite modifier puis le nom du nouveau fichier qui contiendra les nouvelles valeurs.
Suppression du fichier tampon
FIN DU SCRIPT (demande à l'utilisateur s'il souhaite reformater un nouveau fichier ou quitter le script)

- Ajout/Suppression de contenu : Choix du sens de reformatage - Ajout de contenu :[def etape4a()] , Suppression incluant le délimiteur :[def etape4b()] , Suppression en conservant le délimiteur :[def etape4c()]

Suite de l'étape 3a et 3b, l'utilisateur défini le sens du reformatage, avant ou après le délimiteur puis le nom du nouveau fichier qui contiendra les nouvelles valeurs.
Suppression du fichier tampon
FIN DU SCRIPT (demande à l'utilisateur s'il souhaite reformater un nouveau fichier ou quitter le script)

Note : 
Un message particulier "Vous avez quitté volontairement le script !" est affiché quand l'utilisateur ferme volontairement le script (exemple : CTRL+C) et le fichier tampon est alors supprimé s'il a été créé durant le script non abouti.

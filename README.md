# P6-AIC-BG

### Script Python de reformatage de texte (ajout-suppression-modification) depuis un fichier .csv ou .txt

Le script est codé en python et permet à un utilisateur via une suite d'action demandée par le script de reformater les lignes d'une colonne d'un fichier .csv ou les lignes d'un fichier .txt

## Menu principal <strong>["def menu()"]</strong>

Le menu principal permet de choisir le type de fichier à travailler

## Choix du fichier <strong>["def etapecsv()"]</strong> et <strong>["def etapetxt()"]</strong>

Une fenêtre s'ouvre afin de choisir le fichier qui est restreint suivant l'extension choisie (.csv ou .txt).
Un fichier tampon est alors créé afin de reformater le contenu.

- Choix de la colonne du tableau csv <strong>[def etapecsvbis()]</strong>
  
  Pour le .csv une étape supplémentaire est requise afin de choisir la colonne et ainsi en extraire le contenu.

## Choix du délimiteur <strong>[def etape2()]</strong>

L'utilisateur doit choisir une valeur (un caractère ou suite de caractères) qui servira de délimiteur pour le reformatage.

## Choix du type de reformatage <strong>[def etape3()]</strong>

L'utilisateur a le choix d'ajouter, supprimer ou modifier du contenu.

  - Choix du contenu à ajouter <strong>[def etape3a()]</strong>

Si le choix est d'ajouter du contenu, l'utilisateur définit ce qu'il souhaite ajouter.

  - Inclusion ou non du délimiteur <strong>[def etape3b()]</strong>

Si le choix est de supprimer du contenu, l'utilisateur définit d'inclure ou non le délimiteur dans la suppression.

- Modification de contenu <strong>[def etape3c()]</strong>

Si le choix est de modifier du contenu, l'utilisateur définit ce qu'il souhaite modifier puis le nom du nouveau fichier qui contiendra les nouvelles valeurs.

Suppression du fichier tampon

FIN DU SCRIPT (demande à l'utilisateur s'il souhaite reformater un nouveau fichier ou quitter le script)

## Choix du sens de reformatage 

- Ajout de contenu :<strong>[def etape4a()] </strong>

L'utilisateur défini le sens du reformatage, avant ou après le délimiteur puis le nom du nouveau fichier qui contiendra les nouvelles valeurs.

Suppression du fichier tampon

FIN DU SCRIPT (demande à l'utilisateur s'il souhaite reformater un nouveau fichier ou quitter le script)

- Suppression incluant le délimiteur :<strong>[def etape4b()] </strong>

L'utilisateur défini le sens du reformatage, avant ou après le délimiteur puis le nom du nouveau fichier qui contiendra les nouvelles valeurs.

Suppression du fichier tampon

FIN DU SCRIPT (demande à l'utilisateur s'il souhaite reformater un nouveau fichier ou quitter le script)

- Suppression en conservant le délimiteur :<strong>[def etape4c()]</strong>

L'utilisateur défini le sens du reformatage, avant ou après le délimiteur puis le nom du nouveau fichier qui contiendra les nouvelles valeurs.

Suppression du fichier tampon

FIN DU SCRIPT (demande à l'utilisateur s'il souhaite reformater un nouveau fichier ou quitter le script)

## Note : 
Un message particulier "Vous avez quitté volontairement le script !" est affiché quand l'utilisateur ferme volontairement le script (exemple : CTRL+C) et le fichier tampon est alors supprimé s'il a été créé durant le script non abouti.

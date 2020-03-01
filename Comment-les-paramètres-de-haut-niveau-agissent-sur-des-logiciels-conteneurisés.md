---
layout: default
title : Modèle de chapitre pour 2020
date:   2020-01-03 22:00:00 +0100
---

---

> **Date de rendu finale : Mars 2020 au plus tard**
> - Respecter la structure pour que les chapitres soient bien indépendants
> - Remarques :
>>    - Les titres peuvent changer pour etre en adéquation avec votre étude.
>>    - De même il est possible de modifier la structure, celle qui est proposée ici est là pour vous aider.
>>    - Utiliser des références pour justifier votre argumentaire, vos choix etc.

---

**_janvier 2020_**

## Authors

Nous somme quatre étudiants en dernière année d'architecture logicielle à Polytech Nice-Sophia : 

* BENAZET-LACARRE Laurent-Jérôme&lt;laurent-jerome.benazet-lacarre@etu.univ-cotedazur.fr&gt;
* FRERE Baptiste &lt;baptiste.frere@etu.univ-cotedazur.fr&gt;
* MENARD Noé &lt;noe.menard@etu.univ-cotedazur.fr&gt;
* SALORD Florian &lt;florian.salord@etu.univ-cotedazur.fr&gt;

## I. Research context /Project

Docker est un logiciel libre permettant de lancer des applications dans des conteneurs logiciels(def wikipeida ...). C'est un logiciel récent, sa première version open source date de mars 2013. En l'espace de sept ans, il c'est imposé comme un standard de l'industrie. Son succès provient de plusieurs aspects tels que : 
* La flexibilité et la portabilité qu'il offre à une application.
* La paramétrisation qu'il offre à l'utilisateur
* Sa facilité de mise en oeuvre.
* j'ai pas d'autre idées parler de docker compose ?


Nous avons choisi de nous pencher sur l'étude de docker pour plusieurs raisons : 

* D’une part, c’est une question qui nous parle. Nous avons déjà réalisé des projets d'architecture logicielle par le passé que cela soit dans le cadre scolaire ou extra-scolaire. Durant ces projets la question d’avoir une solution paramétrable revient souvent, que cela soit pour séparer un environnement de développement et de production, ou pour livrer un produit qui soit adapté aux attentes d’un client. 
Ce sujet nous a alors paru intéressant car il nous permet de voir concrètement comment différentes solutions répondent à cette problématique, et ainsi d’être plus apte à mettre en place correctement une solution paramétrable dans la suite de notre parcours professionnelle.

* D’autre part, c’est un sujet d’actualité. De plus en plus, les applications sont conteneurisées et ont besoins d’être paramétrées à différents niveaux. 




![Figure 1: Logo UCA](../assets/model/UCAlogoQlarge.png){:height="50px" }


## II. Observations/General question

Dans ce projet nous nous focaliserons sur la question : Comment les paramètres de haut niveau agissent sur des logiciels conteneurisés ?

C'est une question très vaste, en analysant des projets utilisant docker, on se rend compte que les mêmes paramètres peuvent être définis à différents niveaux. La même variable peut être définis au niveau d'un dockerFile, d'un dockerCompose ou dans le fichier de configuration d'une application. On est alors amené à se demander : À quels niveaux peut-on définir théoriquement chaque paramètres et concrètement, à quels niveaux sont-ils réellement définis ?  

Cette question reste encore très vaste, on ne peut pas analyser tout les paramètres qui existent. Pour réaliser notre étude, nous avons ainsi décidé de nous focaliser sur des paramètres fréquemment utilisés dans des applications. Ces paramètres sont :
* Chaîne de connection
* ...
* 
* 

Nous avons aussi décidé de restreindre l'analyse aux projets utilisant docker et le framework Spring. Nous avons choisi ce framework car  c'est un framework que nous connaissons bien et que l'ensemble de la paramétrisation se fait dans un fichier app.config. On pourra ainsi très facilement automatiser nos expériences avec ce framework.

1. Commencez par formuler une question sur quelque chose que vous observez ou constatez ou encore une idée émergente. Attention pour répondre à cette question vous devrez être capable de quantifier vos réponses.
2. Préciser bien pourquoi cette question est intéressante de votre point de vue et éventuellement en quoi la question est plus générale que le contexte de votre projet \(ex: Choisir une libraire de code est un problème récurrent qui se pose très différemment cependant en fonction des objectifs\)

Cette première étape nécessite beaucoup de réflexion pour se définir la bonne question afin de poser les bonnes bases pour la suit.

## III. information gathering

Dans un premier temps, nous avons effectué des recherches afin de savoir où et comment les différents paramètres qui nous interessent pouvaient (orthographe ent ?) être définis. Par la suite nous avons selectionnés un échantillon de projets sur github afin de réaliser nos expériences. Ces projets devaient contenir à la fois le tag 'Docker' et le tag 'Spring'. Nous avons seléctionné les 1000 projets répondant à ses caractéristiques qui possédaient le plus d'étoiles sur github. Une étape de pre-processing était ensuite effectué afin de s'assurer que les projets retenus comportaient bien au moins un dockerFile ou un dockerCompose et un fichier de configuration spring.  
Toute ce processus de selection du dataset a été automatisé grâce aux outils BLABLA (cf partie florian) 

Une fois le dataset constitué, il faut anlyser chaque projet individuellement. Dans un premier temps il faut déterminer si un paramètre a été utilisé et si c'est le cas, à quel niveau à t-il été défini. parler exactement de comment on fait avec mots associés à un tag, dire les limites : qu'on peut avoir oublier / mal defini des params, qu'il aurait été intéressant pour aller plus loin de faire de l'analyse dynamque en linkant le code aux paramètres mais ce que c'est beaucoups plus compliqué à faire. 

Préciser vos zones de recherches en fonction de votre projet,

1. les articles ou documents utiles à votre projet
2. les outils
 
## IV. Hypothesis & Experiences
Nous partions de l'hypothèse que certains paramètres étaient plus utilisés à certains niveaux (mettre tableau de nos hypothèse ...).  L'object était ainsi de voir si nos hypothèses étaient correct ou pas.
Nous avons obtenues les résultats suivants : 

1. Il s'agit ici d'énoncer sous forme d' hypothèses ce que vous allez chercher à démontrer. Vous devez définir vos hypothèses de façon à pouvoir les _mesurer facilement._ Bien sûr, votre hypothèse devrait être construite de manière à v_ous aider à répondre à votre question initiale_.Explicitez ces différents points.
2. Test de l’hypothèse par l’expérimentation. 1. Vos tests d’expérimentations permettent de vérifier si vos hypothèses sont vraies ou fausses. 2. Il est possible que vous deviez répéter vos expérimentations pour vous assurer que les premiers résultats ne sont pas seulement un accident.
3. Explicitez bien les outils utilisés et comment.
4. Justifiez vos choix

## V. Result Analysis and Conclusion

1. Analyse des résultats & construction d’une conclusion : Une fois votre expérience terminée, vous récupérez vos mesures et vous les analysez pour voir si votre hypothèse tient la route. 

## VI. Tools \(facultatif\)

Précisez votre utilisation des outils ou les développements \(e.g. scripts\) réalisés pour atteindre vos objectifs. Ce chapitre doit viser à \(1\) pouvoir reproduire vos expériementations, \(2\) partager/expliquer à d'autres l'usage des outils.

## VI. References

1. ref1
1. ref2

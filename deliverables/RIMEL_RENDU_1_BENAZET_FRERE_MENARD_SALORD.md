# RIMEL - Rendu n°1 - Sujet n°3 : docker

## Question générale et raison de l'intérêt

### Comment les paramètres de haut niveau agissent sur des logiciels conteneurisés ?

Nous avons choisi de nous pencher sur cette étude pour plusieurs raisons : 

D'une part, c'est une question qui nous parle. En effet, nous avons déjà réalisé des projets d'architecture logicielle par le passé, et durant ces projets la question d'avoir une solution paramétrable revient souvent. Que ce soit pour séparer des environnements de développement et de production, ou pour livrer un produit qui soit adapté aux attentes d'un client.  
Ce sujet nous permet de voir concrètement comment différentes solutions répondent à cette problématique, et ainsi être plus apte à mettre en place correctement une solution paramétrable dans la suite de notre parcours professionnel.

D'autre part, c'est un sujet d'actualité. De plus en plus d'applications sont conteneurisées et ont besoins d'être paramétrées à différents niveaux, afin d'être déployée dans des environnements qui ne sont pas contrôlés directement par l'utilisateur comme un service cloud.

## Décomposition en sous-questions et métriques/KPI/outils **envisagés** pour y répondre

Nous avons choisi de nous concentrer sur un point précis de la problématique énoncée ci-dessus : 
### À quel niveau ces paramètres peuvent-ils être définis ?

Cela reste une question très vague qui va tendre à évoluer au fil de nos recherches et analyses.

Pour pouvoir y répondre, plusieurs aspects devront être étudiés :  
D'une part, nous allons devoir identifier quels sont les paramètres de haut niveaux possible, où et comment ils sont déclarés.  
D'autre part nous devrons ensuite analyser leur impact sur l'application.  

Nous avons envisagé plusieurs pistes à ce niveau là :  
Certaines métriques sont explicites et ciblent un point précis de l'application, comme l'url d'une base de données, ou le port à utiliser par un serveur.  
Pour d'autres métriques plus implicites, nous pourrons essayer de corréler leur mise en place / modification avec des modifications dans l'application. Par exemple, si une métrique et une classe sont modifiées dans le même *commit*.

## Démarche prévue 

Pour mettre en place tout cela, nous allons avoir besoin d'outils. 
Il faudra dans un premier temps automatiser le clonage des dépôts, puis vérifier que l'échantillon de données est pertinent par rapport à notre problématique. Les dépôts devront ainsi posséder un ou plusieurs dockerfile et éventuellement un docker-compose, ou autre document servant au déployement du projet en question. 

Pour réaliser cela, nous avons penser à utiliser l'outil [octonode](https://github.com/pksunkara/octonode) qui est une bibliothèque Node.js permettant d'accéder à l'api de [github](https://developer.github.com/v3/).

Une fois l'échantillon de données cloné, vient l'analyse. Pour ce faire nous pensons utiliser [pydriller](https://github.com/ishepard/pydriller) qui est un framework python capable de miner des dépôts logiciels.


## Sources

Les deux sources que nous pensons retenir pour cette étude sont les suivantes : 

- [Who Broke the Build? Automatically Identifying Changes That Induce Test Failures In Continuous Integration at Google Scale](https://research.google/pubs/pub45794/)
- [The Impact of Continuous Integration on Other Software Development Practices: A Large-Scale Empirical Study](https://web.cs.ucdavis.edu/~filkov/papers/CI_adoption.pdf)

Nous comptons nous baser principalement sur le premier article.
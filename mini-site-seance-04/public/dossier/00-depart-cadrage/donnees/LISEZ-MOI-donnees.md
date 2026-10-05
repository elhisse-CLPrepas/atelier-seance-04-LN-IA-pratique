# Données de la session fictive

Deux sources : `cas-coach.json` pour les faits du scénario et `evaluations-session-simulee.csv` pour les six évaluations inventées. Les données ne décrivent aucune formation réellement tenue.

Le CSV est en UTF-8, séparé par des virgules. Six inscrits et six présents sont prévus dans le scénario. Chaque personne possède une seule ligne, de P01 à P06.

| Champ | Signification |
| --- | --- |
| participant_id | Identifiant fictif, unique |
| score_avant_sur_5 | Autoévaluation avant, entier de 1 à 5 |
| score_apres_sur_5 | Autoévaluation après, même échelle |
| satisfaction_sur_5 | Satisfaction simulée, entier de 1 à 5 |
| plan_complet | oui ou non selon le critère du cas |
| retour_fictif | Phrase inventée pour l’exercice de synthèse |

Autoévaluation : 1 = je ne sais pas encore planifier ma semaine, 5 = je peux le faire seul.
Satisfaction : 1 = peu satisfait, 5 = très satisfait.
Plan complet : trois priorités, des créneaux et une marge pour un imprévu.

Calculer les moyennes sur les six réponses. Le gain est la moyenne des différences après moins avant. Ce n’est pas un pourcentage. Le taux de plans complets est le nombre de « oui » divisé par six, multiplié par 100.

Arrondir les moyennes à deux décimales et les pourcentages à une décimale au moment de les afficher. Ces données servent au calcul et à la rédaction. Elles ne démontrent pas l’efficacité d’une formation réelle.

# e4-api-backend

Résultat du walkthrough du cours **E4 Full Stack Back - Advanced**. Ce repository sera mis a jours sur toute la durée du cours, libre a vous de l'utiliser pour réparer/implémenter des fonctionnalités sur votre projet. Vous pouvez également [fork](https://github.com/faraan-estiam/e4-api-backend/fork) ou clonner le projet pour pouvoir suivre le cours en cas de problème sur votre copie.

## 🔰 Mise en place du projet

Pour que le projet fonctionne il faudra configurer le `.env` avec vos clés firebase et stripe, voici la démarche a suivre :

### 🗄️ Google Firebase
  
Allez sur [firebase](https://firebase.google.com), connectez vous et cliquez en haut a droite sur `Go to console`. Cliquez sur votre api *(ou créez en une nouvelle si vous n'en avez pas)*  
  
Si vous n'avez pas de clé privé **Firebase_Admin** :  
Cliquez en haut a gauche sur `⚙️` -> `Paramètres du projet` -> `Comptes de service` -> `Génerer une nouvelle clé privée`  
Complétez `FIREBASE_SERVICE_ACCOUNT_KEY`  

Si vous n'avez pas de configuration firebase :  
Cliquez en haut a gauche sur `⚙️` -> `Paramètres du projet` -> `Paramètres généraux` -> `Vos applications`  
*(créez une application web si vous n'en avez pas déjà)*  
Complétez `FIREBASE_CONFIG` à partir du bloc de code *(sauf databaseURL)*  
  
Si vous n'avez p'as d'URL de base de données :  
Cliquez a gauche sur `Créer` -> `Realtime Database`  
*(créez une base de donée si vous n'en avez pas déjà)*  
Dans l'onglet `Données`, copiez l'URL de la base de donée en cliquant sur le `🔗`  
Complétez `FIREBASE_CONFIG`  
  
#### 🔐Authentication
Vous n'en avez pas besoin pour la configuration mais celà reste nécéssaire pour faire tourner le projet.  
Si vous n'avez pas d'authentication configuré :  
Cliquez a gauche sur `Créer` -> `Authentication` -> `Commencer`  
Choisissez Adresse e-mail/Mot de passe  
Enregistrer
  
### 💵 Stripe
  
Allez sur [stripe](https://stripe.com/fr), connectez vous ou créez un compte et une application puis cliquez en haut a droite sur `Dashboard`
  
Si vous n'avez pas d'Id produit :  
Cliquez a gauche sur `Plus +` -> `Catalogue de produits`  
Créez ou selectionnez un produit puis copiez son ID
  
Cliquez en haut a droite sur `Développeurs` -> `Clés API`  
Copiez vos clés publiques et privées
  
Si vous ne l'avez pas déjà, [installez et configurez stripeCLI](https://stripe.com/docs/stripe-cli?locale=fr-FR)  
Lancez la commande  
```PowerShell
stripe listen --forward-to http://localhost:8000/stripe/webhook
```
Copiez le webhook secret.  
  
Complétez `STRIPE_CONFIG`

## 💻 Lancement de l'API

Lorsque vous importez le projet il faudra tout d'abord initialiser l'environnement.  

### 📂 Initialisation du projet

Dans Visual Studio Code, faites `ctrl`+`p` et tappez `>Python: Create Environment`  
Sélectionnez `Venv`  
Puis `requirements.txt`

Dans un terminal, lancez la commande :  
```Powershell
pip install -r requirements.txt
```

### 🚀 Lancement du projet

Stripe API
Ouvrez un terminal et lancez Stripe API avec la commande suivante :  
```Powershell
stripe listen --forward-to http://localhost:8000/stripe/webhook
```

Student API
Ouvrez un terminal et lancez le projet avec la commande suivante :  
```Powershell
uvicorn main:api --reload
```

## 🌐 Déploiment sur render.com
J'y ai perdu trop d'heures, bon courage à vous  
![](https://i.ytimg.com/vi/fFMWvF3mbzE/mqdefault.jpg)

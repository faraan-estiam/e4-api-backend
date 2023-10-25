# ATTENTION POUR LANCER LE PROJET !
Le router de l'api s'appelle `api` et non `app` !<br>
Pour lancer l'application utilisez :
```Sh
uvicorn main:api --reload
```
Pensez également à ajouter votre dossier `configs/` et de modifier le fichier `database/firebase.py` en conséquence.

Ajoutez un fichier `stripe_config.py` dans le dossier configs et le remplir de la façon suivante :
```Python
stripe_config = {
    'public_key' : '_votre_clé_publique_',
    'secret_key' : '_votre_clé_privée',
    'price_id' : '_votre_price_id_',
    'webhook_secret' : '_votre_webhook_secret_'
}
```
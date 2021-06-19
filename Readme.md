# Databage - Projet MasterCamp Efrei 2020-2021 - GRP 239
Dans le cadre du mastercamp, nous avons décidé de réaliser une application qui permet de détecter les déchets sur différents support. Dans un premier temps nous avons décider de réaliser
la détection des déchets sur une image.

Les catégories prisent en compte sont :
  - Metal
  - Paper
  - Plastique
  - Cartboard
  - Trash

## Installation du programme sur votre ordinateur

### Note
  Toutes les commandes sont à faire dans le même invite de commande ( par sécurité qui sera en mode administrateur )

### 1. Requis
  - Système Window
  - Python 3.9.x 
    - Pour vérifier votre version taper sur le terminal :
      <pre>python --version</pre>
    - Télécharger python 3.9.x : https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe
  - Git
    - Tester cette commande pour vérifier qu'il est bien installé : (vous devriez voir la version de git installé sur votre PC)
      <pre>git --version</pre>
    - Télécharger git : https://git-scm.com/
     
### 2. Étape d'installation

#### 2.1. Télécharge ce dépôt :
  - Ouvrez un terminal dans un dossier où vous voulez mettre l'application
  - Executez cette commande dans ce terminal
  <pre>git clone https://github.com/WVaihau/Databage.git</pre>

<br />

#### 2.2. Configure un nouvel environnement virtuel :
 Execute sur ton terminal ces commandes l'une à la suite des autres : <br/>
  - Installation :<br /> 
  <pre>cd Databage\code && python -m venv dtb</pre>
  - Activation de l'environnement
  <pre>dtb\Scripts\activate</pre>
  (Vous devriez voir "(dtb)" apparaître au début de ligne de votre terminal) 
  - Ajout des modules python :
  <pre>pip install streamlit matplotlib pyyaml opencv-python</pre>
<br />

#### 2.3. Lancement de la configuration de l'application (il faut que l'environnement soit activé)
<pre>python setup.py</pre>
<br />

#### 2.4. Vérification de l'installation
  - Lancer cette commande pour vérifier que l'installation s'est bien déroulé (vous devriez voir un "OK (skipped=1)" à la fin de l'execution)
<pre>cd .. && python documents\Tensorflow_API\models\research\object_detection\builders\model_builder_tf2_test.py</pre>
  - Si des modules manques il faut les installer avec :
<pre>pip install nom_module</pre>
Veuillez vérifier sur internet si le nom du module lors de la commande pip install n'est pas reconnue
<br />

#### 2.5. Lancer l'application ( l'environnement doit être activé -- voir 2.2)
<pre>streamlit run main.py</pre>

Pour arrêter le programme fermer la fenêtre cmd

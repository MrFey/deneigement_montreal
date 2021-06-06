#! /bin/bash
#-- all rights: @Les enfants Sauvages --#
#-- bash-version: 3  --#

export PATH=$PATH:~/.local/bin
echo " - - - - Projet ERO: Deneigement intelligent de Montréal - - - -"
echo "[+] Lancement de Jupyter"
(jupyter-notebook --browser=firefox 1> /dev/null 2> /dev/null &)

echo "[*] Attente du lancement"
sleep 10
echo "[*] Vous devriez maintenant voir le notebook jupyter dans votre navigateur"

echo "[*] Lancement de la demo sur la partie Drone"
firefox "localhost:8888/tree/Demo/project_appero_drone.ipynb"


echo "[*] Lancement de la demo sur la partie Deneigement"
firefox "localhost:8888/tree/Demo/project_appero_deneigeuse.ipynb"


echo "[*] Lancement de l'Application sur la partie Drone"
firefox "localhost:8888/tree/Application/project_appero_drone.ipynb"


echo "[*] Lancement de l'Application sur la partie Deneigement"
firefox "localhost:8888/tree/Application/project_appero_deneigeuses.ipynb"

echo "[!] Vous pouvez maintenant acceder dans votre navigateur à notre projet."
echo "[?] On vous conseille de regarder les scripts dans l'ordre suivant: Demo Drone -> Application Drone -> Demo deneigeuses -> Application deneigeuses"

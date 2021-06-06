#! /bin/bash
#-- all rights:  --#
#-- bash: 3.*  --#


echo "[*] Mise à jour de pip"
python3 -m pip install --upgrade pip

echo "[*] Installation des packages necessaires"
python3 -m pip install --user -r requirement.txt

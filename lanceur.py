import subprocess
from subprocess import Popen

# Modele de carte RueDuCommerce
rdc3080 = "https://www.rueducommerce.fr/rayon/composants-16/nvidia-geforce-rtx-3080-124303?gamme=rue-du-commerce"
rdc3070 = "https://www.rueducommerce.fr/rayon/composants-16/nvidia-geforce-rtx-3070-124296?gamme=rue-du-commerce"

test = "https://www.rueducommerce.fr/rayon/peripheriques-reseaux-et-wifi-73/souris-6246/i-tec"
test2 = "https://www.rueducommerce.fr/rayon/composants-16/nvidia-geforce-rtx-3070-124296"
testsolo = "https://www.rueducommerce.fr/rayon/peripheriques-reseaux-et-wifi-73/souris-6246?fournisseur=bg"
# Modele de carte Fnac

# Lancer recherche carte dispo RDC

#subprocess.Popen( ["python", "rdc.py", rdc3070, "3070"])
#subprocess.Popen( ["python", "rdc.py", rdc3080, "3080"]) 

# Lancer recherche carte dispo Fnac

#subprocess.Popen(["python", "fnac.py"])



subprocess.Popen( ["python", "rdc.py", testsolo, "3070"])

# Module Imports
import mysql.connector 
import sys
import subprocess
import time

# subprocess package
from subprocess import Popen

# argument
url = ( sys.argv[1] )
modele = ( sys.argv[2] )
prix = ( sys.argv[3] )
site = ( sys.argv[4] )

# Connect to MariaDB Platform
try:
    conn = mysql.connector.connect(
        user="fulrox",
        password="Maximum-34",
        host="54.37.157.139",
        port=3306,
        database="RTX",
    )

except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

if site == "rdc":

    if modele == "3070": 
        prixmax = "PRIXMAX3070"
        commande = "SELECT ID, PRIXMAX3070, RDC, RTX3070, CREDIT, IDRDC, MDPRDC, IDPAYPAL, MDPPAYPAL FROM info"
      

    if modele == "3080": 
        prixmax = "PRIXMAX3080"
        commande = "SELECT ID, PRIXMAX3080, RDC, RTX3080, CREDIT, IDRDC, MDPRDC, IDPAYPAL, MDPPAYPAL FROM info"

cur.execute(commande)
rows = cur.fetchall()
for row in rows:
    iduser = row[0]
    prixmax = row[1]
    prixmax = str(prixmax)
    siteval = row[2]
    modeleval = row[3]
    credit = row[4]
    RDCMAIL = row[5]
    RDCMDP = row[6]
    PAYPALMAIL = row[7]
    PAYPALMDP = row[8]
    if siteval ==  "1":
        if modeleval == "1":
            if prixmax >= prix:
                if credit != "0":
                    subprocess.Popen( ["python", "achatrdc.py", url, RDCMAIL, RDCMDP, PAYPALMAIL, PAYPALMDP, credit, iduser])
                    time.sleep(2)
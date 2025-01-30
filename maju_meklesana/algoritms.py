import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

bildes = []
label = []

bilzu_adrese = "maju_meklesana/bildes/"

#sarakstu sataisīšana
for nosaukums in os.listdir(bilzu_adrese):
    image = Image.open(os.path.join(bilzu_adrese,nosaukums)).resize((200,200),Image.Resampling.NEAREST)
    bildes.append(np.array(image))
    if "maja" in nosaukums:
        label.append(1)
    else:
        label.append(0)

#skaitlu sarakstu salabosana

bildes = np.array(bildes)
label = np.array(label)

bildes = bildes/255.0
bildes = bildes.reshape(bildes.shape[0], -1)
# print(bildes)

#datu sadalīšana
X_train, x_test, Y_train, y_test = train_test_split(bildes, label, test_size=0.2)

modelis = RandomForestClassifier()

modelis.fit(X_train, Y_train)

rezultats = modelis.predict(x_test)

precizitate = accuracy_score(rezultats, y_test)

print(precizitate)

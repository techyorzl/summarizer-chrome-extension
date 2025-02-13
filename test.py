import requests

url = "http://127.0.0.1:8000/generate_summary"

data = {
    "text": "Therizinosaurus was a colossal therizinosaurid that could grow up to 9–10 m (30–33 ft) long and 4–5 m (13–16 ft) tall, and weigh possibly over 5 t (5.5 short tons). Like other therizinosaurids, it would have been a slow-moving, long-necked, high browser equipped with a rhamphotheca (horny beak) and a wide torso for food processing. Its forelimbs were particularly robust and had three fingers that bore unguals which, unlike other relatives, were very stiffened, elongated, and only had significant curvatures at the tips. Therizinosaurus had the longest known manual unguals of any land animal, reaching above 50 cm (20 in) in length. Its hindlimbs ended in four functionally weight-bearing toes differing from other theropod groups in which the first toe was reduced to a dewclaw and also resembling the very distantly related sauropodomorphs.It was one of the last and the largest representative of its unique group, the Therizinosauria (formerly known as Segnosauria; the segnosaurs). During and after its original description in 1954, Therizinosaurus had rather complex relationships due to the lack of complete specimens and relatives at the time. Maleev thought the remains of Therizinosaurus to belong to a large turtle-like reptile, and also named a separate family for the genus: Therizinosauridae. Later on, with the discovery of more complete relatives, Therizinosaurus and kin were thought to represent some kind of Late Cretaceous sauropodomorphs or transitional ornithischians, even though at some point it was suggested that it may have been a theropod. After years of taxonomic debate, nevertheless, they are now placed in one of the major dinosaur clades, Theropoda, specifically as maniraptorans. Therizinosaurus is widely recovered within Therizinosauridae by most analyses."
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Summary:", response.json())
else:
    print("Error:", response.text)
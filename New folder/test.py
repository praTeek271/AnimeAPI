from firebase_admin import firestore, initialize_app, credentials

cred = credentials.Certificate("./api/anime-666-firebase-adminsdk-2zsba-1f461c39e0.json")
app = initialize_app(cred)

db = firestore.client()

def create_animename(anime_name):
    # Read the existing data from the file
    with open('./series.json', 'r') as f:
        data = f.read()
    
    # Process the data
    data = data.split('+')
    animeno = f"ame{data.count('@')}"
    
    # Write the new data to the file
    with open('./series.json', 'a') as f:
        f.write('@+')
    
    # Create the new anime name in Firestore
    anime_doc = db.collection('AnimeName').document(animeno)
    anime_doc.set({
        'name': anime_name
    })

    print('Anime Name Created')

    return anime_doc

create_animename('One Piece')
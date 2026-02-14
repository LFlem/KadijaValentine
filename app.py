import streamlit as st
import random

# ============================================================================
# CONFIGURATION STREAMLIT
# ============================================================================
st.set_page_config(
    page_title="Guess The Movie – Valentine Edition",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS pour un design mignon et cute
st.markdown("""
    <style>
    @keyframes floatUp {
        0% { transform: translateY(0); opacity: 0.7; }
        50% { transform: translateY(-6px); opacity: 1; }
        100% { transform: translateY(0); opacity: 0.7; }
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .main {
        background: linear-gradient(135deg, #fff5f7 0%, #f0e6ff 100%);
        padding: 2rem;
    }
    
    .title {
        text-align: center;
        color: #d63384;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 0.5rem;
        animation: pulse 3s ease-in-out infinite;
    }
    
    .subtitle {
        text-align: center;
        color: #6c757d;
        font-size: 1.1em;
        margin-bottom: 1rem;
    }

    .float-hearts {
        text-align: center;
        font-size: 1.4em;
        margin-top: 0.5rem;
        animation: floatUp 3.5s ease-in-out infinite;
    }
    
    .question-container {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 15px rgba(214, 51, 132, 0.1);
        margin: 1rem 0;
        border-left: 5px solid #d63384;
        animation: fadeIn 0.6s ease-in-out;
    }
    
    .hint-text {
        text-align: center;
        font-size: 3em;
        margin: 1rem 0;
        color: #d63384;
        animation: pulse 2.5s ease-in-out infinite;
    }
    
    .score-container {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(214, 51, 132, 0.1);
        margin: 1rem 0;
        animation: fadeIn 0.6s ease-in-out;
    }
    
    .button-container {
        text-align: center;
        margin-top: 2rem;
    }
    
    .final-message {
        text-align: center;
        font-size: 1.3em;
        color: #d63384;
        font-weight: bold;
        margin: 2rem 0;
        animation: pulse 3s ease-in-out infinite;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# BASE DE DONNÉES DES QUESTIONS - 20 FILMS VARIÉS
# ============================================================================
MOVIES = [
    {
        "id": 1,
        "title": "Psycho",
        "hint": "🧼🔪🚿👁️",
        "description": "Nuit cauchemardesque à l'hôtel avec une douche inoubliable",
        "options": ["Psycho", "The Shining", "Se7en"],
    },
    {
        "id": 2,
        "title": "Dracula (1992)",
        "hint": "🧛‍♂️🩸📖🌙",
        "description": "L'amour selon celui qui abhorre la lumière",
        "options": ["Dracula (1992)", "Nosferatu", "Twilight"],
    },
    {
        "id": 3,
        "title": "Titanic",
        "hint": "🚢🧊🎻💔",
        "description": "Romance sur une baignoire qui coule",
        "options": ["Titanic", "Master and Commander", "The Abyss"],
    },
    {
        "id": 4,
        "title": "Le Seigneur des Anneaux",
        "hint": "🧙‍♂️💍🔥🌋",
        "description": "Une petite créature marche longtemps pour se débarrasser d'un bijou",
        "options": ["Le Seigneur des Anneaux", "Harry Potter", "Willow"],
    },
    {
        "id": 5,
        "title": "Inception",
        "hint": "🌀💤🏙️",
        "description": "Un homme se promène dans les rêves",
        "options": ["Inception", "Interstellar", "Shutter Island"],
    },
    {
        "id": 6,
        "title": "Before Sunrise",
        "hint": "🌅🚂💬",
        "description": "Deux inconnus parlent toute la nuit dans une ville",
        "options": ["Before Sunrise", "Lost in Translation", "Midnight in Paris"],
    },
    {
        "id": 7,
        "title": "The Apartment",
        "hint": "🏢🎺🚪",
        "description": "Un homme découvre que son appartement est plus populaire que lui",
        "options": ["The Apartment", "Rear Window", "Her"],
    },
    {
        "id": 8,
        "title": "Seul au Monde",
        "hint": "🏝️⚽🔨",
        "description": "Un homme parle à un ballon pendant beaucoup trop longtemps",
        "options": ["Seul au Monde", "Into the Wild", "The Martian"],
    },
    {
        "id": 9,
        "title": "Joker",
        "hint": "🤡😈💄",
        "description": "Un clown qui ne fait rire personne",
        "options": ["Joker", "It", "The Mask"],
    },
    {
        "id": 10,
        "title": "Interstellar",
        "hint": "👨‍👧🌌📡🪐",
        "description": "Un père traverse l'espace pour sa fille",
        "options": ["Interstellar", "Gravity", "Ad Astra"],
    },
    {
        "id": 11,
        "title": "A Clockwork Orange",
        "hint": "👁️🥛",
        "description": "Un œil et un verre de lait symbolisent la violence",
        "options": ["A Clockwork Orange", "The Lighthouse", "The Shining"],
    },
    {
        "id": 12,
        "title": "Forrest Gump",
        "hint": "🍫📫",
        "description": "Une boîte de chocolat remplie de destinées",
        "options": ["Forrest Gump", "Chocolat", "Amélie"],
    },
    {
        "id": 13,
        "title": "Le Ballon Rouge",
        "hint": "🎈",
        "description": "Un ballon rouge flottant seul dans les airs",
        "options": ["Le Ballon Rouge", "It", "Up"],
    },
    {
        "id": 14,
        "title": "2001: A Space Odyssey",
        "hint": "⬛🚀🤖♾️",
        "description": "Un monolithe noir sur fond rouge préhistorique",
        "options": ["2001: A Space Odyssey", "Blade Runner", "Arrival"],
    },
    {
        "id": 15,
        "title": "Spirited Away",
        "hint": "👧🎪🐉",
        "description": "Une fille se perd dans un monde magique",
        "options": ["Spirited Away", "Kiki's Delivery Service", "Princess Mononoke"],
    },
    {
        "id": 16,
        "title": "The Shining",
        "hint": "🏨❄️🪓🔪",
        "description": "Ici Johnny, coincé dans un hôtel l'hiver",
        "options": ["The Shining", "Psycho", "American Psycho"],
    },
    {
        "id": 17,
        "title": "Fight Club",
        "hint": "👊🥊💥",
        "description": "Un club secret où les hommes se battent",
        "options": ["Fight Club", "American History X", "Drive"],
    },
    {
        "id": 18,
        "title": "Kung Fu Panda",
        "hint": "🐼🥋🥚",
        "description": "Un panda maladroit devient maître du Kung Fu",
        "options": ["Kung Fu Panda", "Madagascar", "Shrek"],
    },
    {
        "id": 19,
        "title": "L'Avventura",
        "hint": "🏝️😕🌊",
        "description": "Une femme disparaît sur une île, personne n'a vraiment l'air concerné",
        "options": ["L'Avventura", "Titanic", "Le Seigneur des Anneaux"],
    },
    {
        "id": 20,
        "title": "Amélie",
        "hint": "💚✨🎪🎨",
        "description": "Une fille secrètement magique arrange les vies des autres",
        "options": ["Amélie", "The Artist", "Midnight in Paris"],
    },
    {
        "id": 21,
        "title": "Se7en",
        "hint": "🔪😈📚",
        "description": "Deux flics chassent un tueur qui aime les chiffres",
        "options": ["Se7en", "Zodiac", "The Silence of the Lambs"],
    },
    {
        "id": 22,
        "title": "Nosferatu",
        "hint": "🧛‍♂️🌗👻",
        "description": "Un vampire classique qui rentre dans les maisons",
        "options": ["Nosferatu", "Dracula", "Fright Night"],
    },
    {
        "id": 23,
        "title": "The Sixth Sense",
        "hint": "👻😨🔮",
        "description": "Un enfant voit les morts qui l'entourent",
        "options": ["The Sixth Sense", "The Others", "Insidious"],
    },
    {
        "id": 24,
        "title": "Blade Runner",
        "hint": "🤖👁️🏙️",
        "description": "Des androïdes se font chasser dans le futur",
        "options": ["Blade Runner", "Total Recall", "Minority Report"],
    },
    {
        "id": 25,
        "title": "Vertigo",
        "hint": "🌀😵👀",
        "description": "Un détective acrophobe poursuivi par une femme énigmatique",
        "options": ["Vertigo", "Psycho", "Marnie"],
    },
    {
        "id": 26,
        "title": "Mulholland Drive",
        "hint": "🛣️🎬😵",
        "description": "Deux femmes et une route qui tout change à L'A",
        "options": ["Mulholland Drive", "Sunset Boulevard", "In a Lonely Place"],
    },
    {
        "id": 27,
        "title": "Donnie Darko",
        "hint": "🕳️😈👁️",
        "description": "Un adolescent voit des créatures étranges",
        "options": ["Donnie Darko", "The Butterfly Effect", "The Sixth Sense"],
    },
    {
        "id": 28,
        "title": "Taxi Driver",
        "hint": "🚖🌙😠",
        "description": "Un taxi la nuit dans une ville chaotique",
        "options": ["Taxi Driver", "Raging Bull", "Mean Streets"],
    },
    {
        "id": 29,
        "title": "Pulp Fiction",
        "hint": "💼💣💥",
        "description": "Histoires entrecroisées dans une ville de gangsters",
        "options": ["Pulp Fiction", "Kill Bill", "Inglorious Basterds"],
    },
    {
        "id": 30,
        "title": "Requiem for a Dream",
        "hint": "💊😵🎭",
        "description": "Quatre personnes sombrent dans l'addiction",
        "options": ["Requiem for a Dream", "Trainspotting", "Drugstore Cowboy"],
    },
    {
        "id": 31,
        "title": "Harry Potter",
        "hint": "👨‍🦱⚡🪄",
        "description": "Un jeune magicien avec une cicatrice en éclair",
        "options": ["Harry Potter", "Percy Jackson", "The Chronicles of Narnia"],
        "image": "https://cdn.shopify.com/s/files/1/1943/7257/files/Harry-Potter_large_0dad831f-4b4a-4db5-b0eb-f96e70436102_large.jpg?v=1514443105",
    },
    {
        "id": 32,
        "title": "Forrest Gump",
        "hint": "👨🏃‍♂️🍫💙",
        "description": "Un homme simple mais bienveillant qui traverse l'Amérique",
        "options": ["Forrest Gump", "The Pursuit of Happyness", "Life is Beautiful"],
        "image": "https://blog.99casting.com/wp-content/uploads/2024/05/forest-2.jpg",
    },
    {
        "id": 33,
        "title": "Terminator",
        "hint": "🤖💪😠",
        "description": "Un cyborg musclé venu du futur",
        "options": ["Terminator", "RoboCop", "Johnny 5"],
        "image": "https://occ-0-8407-92.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABZsNp0mb-SiRRk6z_mYLs4j18GiNiq3PxSa4knQM0lCTvTrdBcwvCS35_qGFAdh8rgq1Xm_zdnhO6Mv4nr8bEALUgedvY5tZxAjs.jpg?r=913",
    },
    {
        "id": 34,
        "title": "Rocky",
        "hint": "🥊💪🐢",
        "description": "Un boxeur maladroit des rues de Philadelphie",
        "options": ["Rocky", "Raging Bull", "Million Dollar Baby"],
        "image": "https://m.media-amazon.com/images/I/51QtoraeDNL._AC_UF1000,1000_QL80_.jpg",
    },
    {
        "id": 35,
        "title": "Indiana Jones",
        "hint": "🧭🪶🎒",
        "description": "Un archéologue adventurier avec un chapeau iconic",
        "options": ["Indiana Jones", "The Mummy", "National Treasure"],
        "image": "https://www.leparisien.fr/resizer/xcuNMts5B_corVphe8vGdTuy1NA=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/lpguideshopping/MDPTEWTLO5E3DGLEAS5UJU6X44.jpg",
    },
    {
        "id": 36,
        "title": "Rambo",
        "hint": "💣🪲🏜️",
        "description": "Un vétéran solitaire et vengeur",
        "options": ["Rambo", "John Wick", "The Equalizer"],
        "image": "https://sm.ign.com/t/ign_fr/blogroll/s/stallone-n/stallone-not-involved-with-rambo-tv-series_5t77.1280.jpg",
    },
    {
        "id": 37,
        "title": "V for Vendetta",
        "hint": "😷💣👑",
        "description": "Un homme masqué qui défie le régime",
        "options": ["V for Vendetta", "Watchmen", "The Dark Knight"],
        "image": "https://www.critikat.com/wp-content/uploads/2006/04/v-pour-vendetta.jpg",
    },
    {
        "id": 38,
        "title": "The Silence of the Lambs",
        "hint": "🎭🔪😈",
        "description": "Un tueur en série cultivé et terrifiant",
        "options": ["The Silence of the Lambs", "Hannibal", "Red Dragon"],
        "image": "https://occ-0-2256-92.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABTxdA1oR1ZZiN982fostNiqrdUjH3JfoZp-jD35E5Yd27wDNUsgeZboCcOMhdljA9cYIh4y6ooUqmysq4KyJW6AzdvMrc19lDgGe.jpg?r=bdf",
    },
    {
        "id": 39,
        "title": "Back to the Future",
        "hint": "🚗⚡🕐",
        "description": "Un adolescent voyage dans une machine temporelle en voiture",
        "options": ["Back to the Future", "The Time Machine", "Looper"],
        "image": "https://www.visitlondon.com/-/media/images/london/visit/whats-on/theatre/back-to-the-future-adelphi/back-to-the-future-1920.jpg?rev=d9ccc16063234947b3c4a74bc4cc176e",
    },
    {
        "id": 40,
        "title": "The Matrix",
        "hint": "🎮❤️💊",
        "description": "Un hacker découvre que la réalité est une simulation",
        "options": ["The Matrix", "Inception", "Dark City"],
        "image": "https://media.vanityfair.fr/photos/60d3765b05c33897d1bd3ef0/16:9/w_2560%2Cc_limit/cover_vf_6650.jpeg",
    },
]

# ============================================================================
# INITIALISATION SESSION STATE
# ============================================================================
if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.questions = []
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.flowers = 0
    st.session_state.chocolates = 0
    st.session_state.answers = []
    st.session_state.game_finished = False

# ============================================================================
# FONCTION: Initialiser le quiz
# ============================================================================
def start_quiz():
    # Sélectionner 20 questions aléatoires parmi les 30 disponibles
    selected_questions = random.sample(MOVIES, 20)
    
    # Mélanger les questions
    random.shuffle(selected_questions)
    
    st.session_state.questions = selected_questions
    
    # Mélanger les options pour chaque question
    for question in st.session_state.questions:
        random.shuffle(question["options"])
    
    st.session_state.game_started = True
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.flowers = 0
    st.session_state.chocolates = 0
    st.session_state.answers = []
    st.session_state.game_finished = False

# ============================================================================
# FONCTION: Réinitialiser le jeu
# ============================================================================
def reset_game():
    st.session_state.game_started = False
    st.session_state.questions = []
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.flowers = 0
    st.session_state.chocolates = 0
    st.session_state.answers = []
    st.session_state.game_finished = False

# ============================================================================
# FONCTION: Calculer le score
# ============================================================================
def update_score():
    st.session_state.flowers = st.session_state.score
    st.session_state.chocolates = st.session_state.score // 3

# ============================================================================
# PAGE: ACCUEIL
# ============================================================================
def display_home():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="title">🎬 Guess The Movie</div>', unsafe_allow_html=True)
        st.markdown('<div class="title" style="color: #d63384; font-size: 1.8em;">Pour Kadija  💝</div>', unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("""
        <div class="subtitle">
        Chaque bonne réponse = 1 fleur 🌸
        <br/>
        Chaque 3 bonnes réponses = 1 chocolat 🍫
        <br/>
        <br/>
        <em>Kadija, prête à montrer ce que tu sais des grands classiques du cinéma ?</em>
        </div>
        <div class="float-hearts">💖 💗 💞 💖</div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
        with col_btn2:
            if st.button("🎬 Commencer le quiz", use_container_width=True, key="start_btn"):
                start_quiz()
                st.rerun()

# ============================================================================
# PAGE: QUIZ
# ============================================================================
def display_quiz():
    current_idx = st.session_state.current_question_index
    total_questions = len(st.session_state.questions)
    
    # Barre de progression
    progress = current_idx / total_questions
    st.progress(progress, text=f"Question {current_idx + 1}/{total_questions}")
    
    # Afficher le score en temps réel
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div style='text-align: center; font-size: 1.2em;'>Fleurs: 🌸 × {st.session_state.flowers}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align: center; font-size: 1.2em;'>Chocolats: 🍫 × {st.session_state.chocolates}</div>", unsafe_allow_html=True)
    
    st.divider()
    
    question = st.session_state.questions[current_idx]
    
    # Afficher le hint
    st.markdown(f'<div class="hint-text">{question["hint"]}</div>', unsafe_allow_html=True)
    
    # Afficher l'image si disponible
    if "image" in question and question["image"]:
        col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
        with col_img2:
            st.image(question["image"], use_container_width=True, caption="Qui est ce personnage ?")
    
    # Afficher la description
    st.markdown(f"""
    <div class="question-container">
    <p style="font-size: 1.1em; color: #6c757d; text-align: center;">
    <em>{question["description"]}</em>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### C'est quel film ?")
    
    # Créer les boutons pour chaque option
    selected_answer = None
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button(question["options"][0], use_container_width=True, key=f"option_0_{current_idx}"):
            selected_answer = question["options"][0]
    
    with col2:
        if st.button(question["options"][1], use_container_width=True, key=f"option_1_{current_idx}"):
            selected_answer = question["options"][1]
    
    with col3:
        if st.button(question["options"][2], use_container_width=True, key=f"option_2_{current_idx}"):
            selected_answer = question["options"][2]
    
    # Traiter la réponse
    if selected_answer:
        is_correct = selected_answer == question["title"]
        st.session_state.answers.append({
            "question": question["title"],
            "answer": selected_answer,
            "correct": is_correct
        })
        
        if is_correct:
            st.success(f"🎉 Bravo ! C'était bien {question['title']} !", icon="✅")
            st.session_state.score += 1
            update_score()
        else:
            st.error(f"❌ Oups ! C'était {question['title']}, pas {selected_answer}.", icon="❌")
        
        st.session_state.current_question_index += 1
        
        # Vérifier si c'est la fin du quiz
        if st.session_state.current_question_index >= total_questions:
            st.session_state.game_finished = True
        
        # Bouton pour la prochaine question
        st.divider()
        col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
        with col_btn2:
            if st.button("➡️ Question suivante", use_container_width=True, key="next_btn"):
                st.rerun()

# ============================================================================
# PAGE: ÉCRAN FINAL
# ============================================================================
def display_final():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="title">🎉 Bravo !</div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Afficher le score final
        st.markdown(f"""
        <div class="score-container">
            <h2 style="color: #d63384;">Ton résultat : {st.session_state.score}/20</h2>
            <h1 style="font-size: 3em; margin: 1rem 0;">
                🌸 × {st.session_state.flowers} 
                <br/>
                🍫 × {st.session_state.chocolates}
            </h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Message final cute
        st.markdown("""
        <div class="final-message">
            💝 Kadija, voici ce que tu as gagné pour notre premier date 💝
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Résumé des réponses
        with st.expander("📋 Voir tes réponses"):
            for i, answer in enumerate(st.session_state.answers, 1):
                status = "✅" if answer["correct"] else "❌"
                st.write(f"{status} Q{i}: **{answer['question']}** → {answer['answer']}")
        
        st.divider()
        
        col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
        with col_btn2:
            if st.button("🔄 Rejouer", use_container_width=True, key="replay_btn"):
                reset_game()
                st.rerun()

# ============================================================================
# LOGIQUE PRINCIPALE
# ============================================================================
if not st.session_state.game_started:
    display_home()
elif st.session_state.game_finished:
    display_final()
else:
    display_quiz()

# DATA
akun = {
    "admin" : {"password" : "admin123", "role" : "Admin"},
    "astra" : {"password" : "astra", "role" : "User"},
    "rejam" : {"password" : "rejam", "role" : "User"},
    "paimon" : {"password" : "asmoday", "role" : "User"}
}

genshin_characters = {
    'Venti': 'Anemo', 'Jean': 'Anemo', 'Xiao': 'Anemo', 'Kaedehara Kazuha': 'Anemo', 'Wanderer': 'Anemo', 'Xianyun': 'Anemo', 'Chasca': 'Anemo', 'Lan Yan': 'Anemo', 'Sucrose': 'Anemo', 'Sayu': 'Anemo', 'Shikanoin Heizou': 'Anemo', 'Faruzan': 'Anemo', 'Lynette': 'Anemo', 'Yumemizuku': 'Anemo', 'Varka': 'Anemo', 'Prune': 'Anemo', 'Ifa': 'Anemo', 'Jahoda': 'Anemo',
    'Zhongli': 'Geo', 'Albedo': 'Geo', 'Arataki Itto': 'Geo', 'Navia': 'Geo', 'Chiori': 'Geo', 'Xilonen': 'Geo', 'Ningguang': 'Geo', 'Noelle': 'Geo', 'Gorou': 'Geo', 'Yun Jin': 'Geo', 'Kachina': 'Geo', 'Linnea': 'Geo', 'Illuga': 'Geo', 'Zibai': 'Geo',
    'Raiden Shogun': 'Electro', 'Yae Miko': 'Electro', 'Cyno': 'Electro', 'Keqing': 'Electro', 'Clorinde': 'Electro', 'Fischl': 'Electro', 'Beidou': 'Electro', 'Razor': 'Electro', 'Lisa': 'Electro', 'Kujou Sara': 'Electro', 'Kuki Shinobu': 'Electro', 'Dori': 'Electro', 'Sethos': 'Electro', 'Ororon': 'Electro', 'Iansan': 'Electro', 'Flins': 'Electro', 'Ineffa': 'Electro', 'Varesa': 'Electro',
    'Nahida': 'Dendro', 'Alhaitham': 'Dendro', 'Tighnari': 'Dendro', 'Baizhu': 'Dendro', 'Emilie': 'Dendro', 'Kinich': 'Dendro', 'Collei': 'Dendro', 'Yaoyao': 'Dendro', 'Kaveh': 'Dendro', 'Kirara': 'Dendro', 'lauma': 'Dendro', 'Never': 'Dendro', 
    'Furina': 'Hydro', 'Neuvillette': 'Hydro', 'Yelan': 'Hydro', 'Tartaglia': 'Hydro', 'Kamisato Ayato': 'Hydro', 'Nilou': 'Hydro', 'Sangonomiya Kokomi': 'Hydro', 'Mualani': 'Hydro', 'Mona': 'Hydro', 'Barbara': 'Hydro', 'Xingqiu': 'Hydro', 'Candace': 'Hydro', 'Sigewinne': 'Hydro','Dahlia': 'Hydro', 'Aino': 'Hydro', 'Columbina': 'Hydro',
    'Hu Tao': 'Pyro', 'Yoimiya': 'Pyro', 'Lyney': 'Pyro', 'Arlecchino': 'Pyro', 'Klee': 'Pyro', 'Diluc': 'Pyro', 'Dehya': 'Pyro', 'Mavuika': 'Pyro', 'Xiangling': 'Pyro', 'Bennett': 'Pyro', 'Thoma': 'Pyro', 'Yanfei': 'Pyro', 'Xinyan': 'Pyro', 'Amber': 'Pyro', 'Chevreuse': 'Pyro', 'Gaming': 'Pyro', 'Nicole': 'Pyro', 'Durin': 'Pyro',
    'Kamisato Ayaka': 'Cryo', 'Ganyu': 'Cryo', 'Shenhe': 'Cryo', 'Wriothesley': 'Cryo', 'Eula': 'Cryo', 'Qiqi': 'Cryo', 'Aloy': 'Cryo', 'Citlali': 'Cryo', 'Diona': 'Cryo', 'Rosaria': 'Cryo', 'Chongyun': 'Cryo', 'Kaeya': 'Cryo', 'Layla': 'Cryo', 'Mika': 'Cryo', 'Freminet': 'Cryo', 'Charlotte': 'Cryo', 'Lohen': 'Cryo', 'Escoffier': 'Cryo','Skirk': 'Cryo', 'Sandrone': 'Cryo',
    'Traveler': {'Anemo', 'Geo', 'Electro', 'Dendro', 'Hydro', 'Pyro', 'Cryo'},
}

preset = {
    1: {
        "nama": "Abyss Floor 12",
        "deskripsi": "Target level 100, energi penuh saat mulai, "
                    "pengujian langsung dimulai "
                    "energy drop every 2,5 million damage delt."
    },
    2: {
        "nama": "Stygian Onslaught - Fearless",
        "deskripsi": "Target level 105, tanpa energi sejak awal, "
                    "hitungan mundur 3 detik sebelum pengujian dimulai."
    },
    3: {
        "nama": "Stygian Onslaught - Dire",
        "deskripsi": "Target level 110, tanpa energi sejak awal, "
                    "hitungan mundur 3 detik sebelum pengujian dimulai."
    }
}

dummy = {
    1: {
        "nama": "Standard Enemy",
        "kategori": "Standard",
        "deskripsi": "they are general purpose passive targets dasigned for single target damage testing."
    },
    2: {
        "nama": "Boss Target",
        "kategori": "Boss",
        "deskripsi": "they are the best used to simmulate the endgame performance of freezee team against enemies that cannot be frozen."
    },
    3: {
        "nama": "Multi-target Group",
        "kategori": "Multi-target",
        "deskripsi": "multi terge dummnies are designed for AoE damage testing and display both DPS and DPT."
    }
}
kategori_dummy = {"Standard", "Boss", "Multi-target"}
team = [
    # --- AKUN: astra ---
    {
        "id": 1042,
        "username": "astra",
        "nama_tim": "Flins Lunar",
        "karakter": ["Flins", "Ineffa", "Sucrose", "Columbina"],
        "elemen": {
            "Flins": "Electro",
            "Ineffa": "Electro",
            "Sucrose": "Anemo",
            "Columbina": "Hydro"
        }
    },
    {
        "id": 2891,
        "username": "astra",
        "nama_tim": "Mavuika Melt",
        "karakter": ["Mavuika", "Citlali", "Xilonen", "Bennett"],
        "elemen": {
            "Mavuika": "Pyro",
            "Citlali": "Cryo",
            "Xilonen": "Geo",
            "Bennett": "Pyro"
        }
    },
    # --- AKUN: rejam ---
    {
        "id": 4175,
        "username": "rejam",
        "nama_tim": "Neuvillette Hyper",
        "karakter": ["Neuvillette", "Furina", "Kaedehara Kazuha", "Xilonen"],
        "elemen": {
            "Neuvillette": "Hydro",
            "Furina": "Hydro",
            "Kaedehara Kazuha": "Anemo",
            "Xilonen": "Geo"
        }
    },
    {
        "id": 5630,
        "username": "rejam",
        "nama_tim": "Skirk Freeze",
        "karakter": ["Skirk", "Escoffier", "Furina", "Shenhe"],
        "elemen": {
            "Skirk": "Cryo",
            "Escoffier": "Cryo",
            "Furina": "Hydro",
            "Shenhe": "Cryo"
        }
    },
    # --- AKUN: paimon ---
    {
        "id": 7319,
        "username": "paimon",
        "nama_tim": "Arlecchino Overload",
        "karakter": ["Arlecchino", "Chevreuse", "Fischl", "Bennett"],
        "elemen": {
            "Arlecchino": "Pyro",
            "Chevreuse": "Pyro",
            "Fischl": "Electro",
            "Bennett": "Pyro"
        }
    },
    {
        "id": 8904,
        "username": "paimon",
        "nama_tim": "Varesa Plunge",
        "karakter": ["Varesa", "Xianyun", "Furina", "Iansan"],
        "elemen": {
            "Varesa": "Electro",
            "Xianyun": "Anemo",
            "Furina": "Hydro",
            "Iansan": "Electro"
        }
    }
]

build = [
    # --- AKUN: astra ---
    {
        "id": 1583,
        "username": "astra",
        "nama_build": "Flins Hypercarry",
        "id_team": 1042,
        "nama_tim": "Flins Lunar",
        "karakter_build": [
            {"karakter": "Flins", "elemen": "Electro", "senjata": "pjws", "artefak": "NotSu"},
            {"karakter": "Ineffa", "elemen": "Electro", "senjata": "Engulfing", "artefak": "Aubade"},
            {"karakter": "Sucrose", "elemen": "Anemo", "senjata": "ttds", "artefak": "Viri"},
            {"karakter": "Columbina", "elemen": "Hydro", "senjata": "Favonius Codex", "artefak": "Silken"}
        ]
    },
    {
        "id": 3490,
        "username": "astra",
        "nama_build": "Mavuika Obsidian",
        "id_team": 2891,
        "nama_tim": "Mavuika Melt",
        "karakter_build": [
            {"karakter": "Mavuika", "elemen": "Pyro", "senjata": "A Thousand Blazing Suns", "artefak": "Obsidian Codex"},
            {"karakter": "Citlali", "elemen": "Cryo", "senjata": "Starcaller's Watch", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Peak Patrol Song", "artefak": "Archaic Petra"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Aquila Favonia", "artefak": "Noblesse Oblige"}
        ]
    },
    # --- AKUN: rejam ---
    {
        "id": 4921,
        "username": "rejam",
        "nama_build": "Neuvillette Abyss",
        "id_team": 4175,
        "nama_tim": "Neuvillette Hyper",
        "karakter_build": [
            {"karakter": "Neuvillette", "elemen": "Hydro", "senjata": "Tome of the Eternal Flow", "artefak": "Marechaussee Hunter"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Splendor of Tranquil Waters", "artefak": "Golden Troupe"},
            {"karakter": "Kaedehara Kazuha", "elemen": "Anemo", "senjata": "Freedom-Sworn", "artefak": "Viridescent Venerer"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Favonius Sword", "artefak": "Scroll of the Hero of Cinder City"}
        ]
    },
    {
        "id": 6284,
        "username": "rejam",
        "nama_build": "Skirk Boss Killer",
        "id_team": 5630,
        "nama_tim": "Skirk Freeze",
        "karakter_build": [
            {"karakter": "Skirk", "elemen": "Cryo", "senjata": "Azurelight", "artefak": "Finale of the Deep Galleries"},
            {"karakter": "Escoffier", "elemen": "Cryo", "senjata": "Symphonist of Scents", "artefak": "Golden Troupe"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Fleuve Cendre Ferryman", "artefak": "Golden Troupe"},
            {"karakter": "Shenhe", "elemen": "Cryo", "senjata": "Calamity Queller", "artefak": "Noblesse Oblige"}
        ]
    },
    # --- AKUN: paimon ---
    {
        "id": 7842,
        "username": "paimon",
        "nama_build": "Arlecchino Whimsy",
        "id_team": 7319,
        "nama_tim": "Arlecchino Overload",
        "karakter_build": [
            {"karakter": "Arlecchino", "elemen": "Pyro", "senjata": "Crimson Moon's Semblance", "artefak": "Fragment of Harmonic Whimsy"},
            {"karakter": "Chevreuse", "elemen": "Pyro", "senjata": "Dialogues of the Desert Sages", "artefak": "Noblesse Oblige"},
            {"karakter": "Fischl", "elemen": "Electro", "senjata": "The Stringless", "artefak": "Golden Troupe"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Skyward Blade", "artefak": "Instructor"}
        ]
    },
    {
        "id": 9415,
        "username": "paimon",
        "nama_build": "Varesa Long Night",
        "id_team": 8904,
        "nama_tim": "Varesa Plunge",
        "karakter_build": [
            {"karakter": "Varesa", "elemen": "Electro", "senjata": "Vivid Notions", "artefak": "Long Night's Oath"},
            {"karakter": "Xianyun", "elemen": "Anemo", "senjata": "Crane's Echoing Call", "artefak": "Viridescent Venerer"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Festering Desire", "artefak": "Golden Troupe"},
            {"karakter": "Iansan", "elemen": "Electro", "senjata": "Tamayuratei no Ohanashi", "artefak": "Scroll of the Hero of Cinder City"}
        ]
    }
]

riwayat = [
    {
        "id": 1127,
        "username": "astra",
        "id_team": 1042,
        "id_build": 1583,
        "nama_tim": "Flins Lunar",
        "nama_build": "Flins Hypercarry",
        "karakter_build": [dict(data) for data in build[0]["karakter_build"]],
        "id_preset": 1,
        "id_dummy": 1,
        "dps": 145739,
        "waktu": "22-11-2026 14:15:20"
    },
    {
        "id": 2654,
        "username": "astra",
        "id_team": 2891,
        "id_build": 3490,
        "nama_tim": "Mavuika Melt",
        "nama_build": "Mavuika Obsidian",
        "karakter_build": [dict(data) for data in build[1]["karakter_build"]],
        "id_preset": 3,
        "id_dummy": 2,
        "dps": 192450,
        "waktu": "22-11-2026 14:22:11"
    },
    {
        "id": 4812,
        "username": "rejam",
        "id_team": 4175,
        "id_build": 4921,
        "nama_tim": "Neuvillette Hyper",
        "nama_build": "Neuvillette Abyss",
        "karakter_build": [dict(data) for data in build[2]["karakter_build"]],
        "id_preset": 1,
        "id_dummy": 3,
        "dps": 128600,
        "waktu": "22-11-2026 14:30:45"
    },
    {
        "id": 6093,
        "username": "rejam",
        "id_team": 5630,
        "id_build": 6284,
        "nama_tim": "Skirk Freeze",
        "nama_build": "Skirk Boss Killer",
        "karakter_build": [dict(data) for data in build[3]["karakter_build"]],
        "id_preset": 2,
        "id_dummy": 2,
        "dps": 164820,
        "waktu": "22-11-2026 14:41:08"
    },
    {
        "id": 7508,
        "username": "paimon",
        "id_team": 7319,
        "id_build": 7842,
        "nama_tim": "Arlecchino Overload",
        "nama_build": "Arlecchino Whimsy",
        "karakter_build": [dict(data) for data in build[4]["karakter_build"]],
        "id_preset": 1,
        "id_dummy": 1,
        "dps": 115300,
        "waktu": "22-11-2026 14:50:33"
    },
    {
        "id": 9186,
        "username": "paimon",
        "id_team": 8904,
        "id_build": 9415,
        "nama_tim": "Varesa Plunge",
        "nama_build": "Varesa Long Night",
        "karakter_build": [dict(data) for data in build[5]["karakter_build"]],
        "id_preset": 2,
        "id_dummy": 3,
        "dps": 98450,
        "waktu": "22-11-2026 15:05:50"
    }
]

elemen_karakter_valid = ("Anemo", "Geo", "Electro", "Dendro", "Hydro", "Pyro", "Cryo")
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
    # ==================== AKUN: astra (5 Tim) ====================
    {
        "id": 1042,
        "username": "astra",
        "nama_tim": "Flins Lunar",
        "karakter": ["Flins", "Ineffa", "Sucrose", "Columbina"],
        "elemen": {"Flins": "Electro", "Ineffa": "Electro", "Sucrose": "Anemo", "Columbina": "Hydro"}
    },
    {
        "id": 2891,
        "username": "astra",
        "nama_tim": "Mavuika Melt",
        "karakter": ["Mavuika", "Citlali", "Xilonen", "Bennett"],
        "elemen": {"Mavuika": "Pyro", "Citlali": "Cryo", "Xilonen": "Geo", "Bennett": "Pyro"}
    },
    {
        "id": 1934,
        "username": "astra",
        "nama_tim": "Clorinde Aggravate",
        "karakter": ["Clorinde", "Fischl", "Nahida", "Kaedehara Kazuha"],
        "elemen": {"Clorinde": "Electro", "Fischl": "Electro", "Nahida": "Dendro", "Kaedehara Kazuha": "Anemo"}
    },
    {
        "id": 2417,
        "username": "astra",
        "nama_tim": "Navia Double Pyro",
        "karakter": ["Navia", "Xilonen", "Xiangling", "Bennett"],
        "elemen": {"Navia": "Geo", "Xilonen": "Geo", "Xiangling": "Pyro", "Bennett": "Pyro"}
    },
    {
        "id": 3108,
        "username": "astra",
        "nama_tim": "Chasca Rainbow",
        "karakter": ["Chasca", "Furina", "Ororon", "Bennett"],
        "elemen": {"Chasca": "Anemo", "Furina": "Hydro", "Ororon": "Electro", "Bennett": "Pyro"}
    },

    # ==================== AKUN: rejam (5 Tim) ====================
    {
        "id": 4175,
        "username": "rejam",
        "nama_tim": "Neuvillette Hyper",
        "karakter": ["Neuvillette", "Furina", "Kaedehara Kazuha", "Xilonen"],
        "elemen": {"Neuvillette": "Hydro", "Furina": "Hydro", "Kaedehara Kazuha": "Anemo", "Xilonen": "Geo"}
    },
    {
        "id": 5630,
        "username": "rejam",
        "nama_tim": "Skirk Freeze",
        "karakter": ["Skirk", "Escoffier", "Furina", "Shenhe"],
        "elemen": {"Skirk": "Cryo", "Escoffier": "Cryo", "Furina": "Hydro", "Shenhe": "Cryo"}
    },
    {
        "id": 4420,
        "username": "rejam",
        "nama_tim": "Alhaitham Quickbloom",
        "karakter": ["Alhaitham", "Nahida", "Furina", "Kuki Shinobu"],
        "elemen": {"Alhaitham": "Dendro", "Nahida": "Dendro", "Furina": "Hydro", "Kuki Shinobu": "Electro"}
    },
    {
        "id": 5192,
        "username": "rejam",
        "nama_tim": "Mualani Vape",
        "karakter": ["Mualani", "Xilonen", "Xiangling", "Nahida"],
        "elemen": {"Mualani": "Hydro", "Xilonen": "Geo", "Xiangling": "Pyro", "Nahida": "Dendro"}
    },
    {
        "id": 5874,
        "username": "rejam",
        "nama_tim": "Kinich Burning",
        "karakter": ["Kinich", "Emilie", "Xiangling", "Bennett"],
        "elemen": {"Kinich": "Dendro", "Emilie": "Dendro", "Xiangling": "Pyro", "Bennett": "Pyro"}
    },

    # ==================== AKUN: paimon (5 Tim) ====================
    {
        "id": 7319,
        "username": "paimon",
        "nama_tim": "Arlecchino Overload",
        "karakter": ["Arlecchino", "Chevreuse", "Fischl", "Bennett"],
        "elemen": {"Arlecchino": "Pyro", "Chevreuse": "Pyro", "Fischl": "Electro", "Bennett": "Pyro"}
    },
    {
        "id": 8904,
        "username": "paimon",
        "nama_tim": "Varesa Plunge",
        "karakter": ["Varesa", "Xianyun", "Furina", "Iansan"],
        "elemen": {"Varesa": "Electro", "Xianyun": "Anemo", "Furina": "Hydro", "Iansan": "Electro"}
    },
    {
        "id": 7053,
        "username": "paimon",
        "nama_tim": "Hu Tao Plunge",
        "karakter": ["Hu Tao", "Furina", "Yelan", "Xianyun"],
        "elemen": {"Hu Tao": "Pyro", "Furina": "Hydro", "Yelan": "Hydro", "Xianyun": "Anemo"}
    },
    {
        "id": 8146,
        "username": "paimon",
        "nama_tim": "Raiden National",
        "karakter": ["Raiden Shogun", "Xingqiu", "Xiangling", "Bennett"],
        "elemen": {"Raiden Shogun": "Electro", "Xingqiu": "Hydro", "Xiangling": "Pyro", "Bennett": "Pyro"}
    },
    {
        "id": 8532,
        "username": "paimon",
        "nama_tim": "Xiao FFXX",
        "karakter": ["Xiao", "Faruzan", "Furina", "Xianyun"],
        "elemen": {"Xiao": "Anemo", "Faruzan": "Anemo", "Furina": "Hydro", "Xianyun": "Anemo"}
    }
]

build = [
    # ==================== AKUN: astra ====================
    # --- Tim: Flins Lunar (3 Build) ---
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
        "id": 1694,
        "username": "astra",
        "nama_build": "Flins Lunar-Charged",
        "id_team": 1042,
        "nama_tim": "Flins Lunar",
        "karakter_build": [
            {"karakter": "Flins", "elemen": "Electro", "senjata": "Staff of Homa", "artefak": "Thundering Fury"},
            {"karakter": "Ineffa", "elemen": "Electro", "senjata": "Favonius Lance", "artefak": "Gilded Dreams"},
            {"karakter": "Sucrose", "elemen": "Anemo", "senjata": "Sacrificial Fragments", "artefak": "Viridescent Venerer"},
            {"karakter": "Columbina", "elemen": "Hydro", "senjata": "Prototype Amber", "artefak": "Tenacity"}
        ]
    },
    {
        "id": 1728,
        "username": "astra",
        "nama_build": "Flins Burst Nuke",
        "id_team": 1042,
        "nama_tim": "Flins Lunar",
        "karakter_build": [
            {"karakter": "Flins", "elemen": "Electro", "senjata": "Staff of the Scarlet Sands", "artefak": "NotSu"},
            {"karakter": "Ineffa", "elemen": "Electro", "senjata": "Engulfing", "artefak": "Aubade"},
            {"karakter": "Sucrose", "elemen": "Anemo", "senjata": "Wandering Evenstar", "artefak": "Viridescent Venerer"},
            {"karakter": "Columbina", "elemen": "Hydro", "senjata": "Tome of the Eternal Flow", "artefak": "Silken"}
        ]
    },

    # --- Tim: Mavuika Melt (5 Build) ---
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
    {
        "id": 3512,
        "username": "astra",
        "nama_build": "Mavuika Wolf Gravestone",
        "id_team": 2891,
        "nama_tim": "Mavuika Melt",
        "karakter_build": [
            {"karakter": "Mavuika", "elemen": "Pyro", "senjata": "Wolf's Gravestone", "artefak": "Obsidian Codex"},
            {"karakter": "Citlali", "elemen": "Cryo", "senjata": "TTDS", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Favonius Sword", "artefak": "Archaic Petra"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Mistsplitter Reforged", "artefak": "Noblesse Oblige"}
        ]
    },
    {
        "id": 3644,
        "username": "astra",
        "nama_build": "Mavuika Verdict",
        "id_team": 2891,
        "nama_tim": "Mavuika Melt",
        "karakter_build": [
            {"karakter": "Mavuika", "elemen": "Pyro", "senjata": "Verdict", "artefak": "Obsidian Codex"},
            {"karakter": "Citlali", "elemen": "Cryo", "senjata": "Starcaller's Watch", "artefak": "Instructor"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Peak Patrol Song", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Aquila Favonia", "artefak": "Noblesse Oblige"}
        ]
    },
    {
        "id": 3789,
        "username": "astra",
        "nama_build": "Mavuika Serpent R5",
        "id_team": 2891,
        "nama_tim": "Mavuika Melt",
        "karakter_build": [
            {"karakter": "Mavuika", "elemen": "Pyro", "senjata": "Serpent Spine", "artefak": "Crimson Witch"},
            {"karakter": "Citlali", "elemen": "Cryo", "senjata": "Sacrificial Fragments", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Flute of Ezpitzal", "artefak": "Archaic Petra"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Skyward Blade", "artefak": "Noblesse Oblige"}
        ]
    },
    {
        "id": 3821,
        "username": "astra",
        "nama_build": "Mavuika F2P Tidal",
        "id_team": 2891,
        "nama_tim": "Mavuika Melt",
        "karakter_build": [
            {"karakter": "Mavuika", "elemen": "Pyro", "senjata": "Tidal Shadow", "artefak": "Obsidian Codex"},
            {"karakter": "Citlali", "elemen": "Cryo", "senjata": "TTDS", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Favonius Sword", "artefak": "Instructor"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Sapwood Blade", "artefak": "Noblesse Oblige"}
        ]
    },

    # --- Tim: Clorinde Aggravate (2 Build) ---
    {
        "id": 2105,
        "username": "astra",
        "nama_build": "Clorinde Whimsy",
        "id_team": 1934,
        "nama_tim": "Clorinde Aggravate",
        "karakter_build": [
            {"karakter": "Clorinde", "elemen": "Electro", "senjata": "Absolution", "artefak": "Fragment of Harmonic Whimsy"},
            {"karakter": "Fischl", "elemen": "Electro", "senjata": "The Stringless", "artefak": "Golden Troupe"},
            {"karakter": "Nahida", "elemen": "Dendro", "senjata": "A Thousand Floating Dreams", "artefak": "Deepwood Memories"},
            {"karakter": "Kaedehara Kazuha", "elemen": "Anemo", "senjata": "Freedom-Sworn", "artefak": "Viridescent Venerer"}
        ]
    },
    {
        "id": 2248,
        "username": "astra",
        "nama_build": "Clorinde Thundering",
        "id_team": 1934,
        "nama_tim": "Clorinde Aggravate",
        "karakter_build": [
            {"karakter": "Clorinde", "elemen": "Electro", "senjata": "Finale of the Deep", "artefak": "Thundering Fury"},
            {"karakter": "Fischl", "elemen": "Electro", "senjata": "Alley Hunter", "artefak": "Golden Troupe"},
            {"karakter": "Nahida", "elemen": "Dendro", "senjata": "Sacrificial Fragments", "artefak": "Gilded Dreams"},
            {"karakter": "Kaedehara Kazuha", "elemen": "Anemo", "senjata": "Iron Sting", "artefak": "Viridescent Venerer"}
        ]
    },

    # --- Tim: Navia Double Pyro (4 Build) ---
    {
        "id": 2501,
        "username": "astra",
        "nama_build": "Navia Nighttime",
        "id_team": 2417,
        "nama_tim": "Navia Double Pyro",
        "karakter_build": [
            {"karakter": "Navia", "elemen": "Geo", "senjata": "Verdict", "artefak": "Nighttime Whispers"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Peak Patrol Song", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "The Catch", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Aquila Favonia", "artefak": "Noblesse Oblige"}
        ]
    },
    {
        "id": 2619,
        "username": "astra",
        "nama_build": "Navia Serpent",
        "id_team": 2417,
        "nama_tim": "Navia Double Pyro",
        "karakter_build": [
            {"karakter": "Navia", "elemen": "Geo", "senjata": "Serpent Spine", "artefak": "Nighttime Whispers"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Favonius Sword", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "Engulfing Lightning", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Skyward Blade", "artefak": "Noblesse Oblige"}
        ]
    },
    {
        "id": 2733,
        "username": "astra",
        "nama_build": "Navia Golden Troupe",
        "id_team": 2417,
        "nama_tim": "Navia Double Pyro",
        "karakter_build": [
            {"karakter": "Navia", "elemen": "Geo", "senjata": "Wolf's Gravestone", "artefak": "Golden Troupe"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Flute of Ezpitzal", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "Favonius Lance", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Alley Flash", "artefak": "Noblesse Oblige"}
        ]
    },
    {
        "id": 2845,
        "username": "astra",
        "nama_build": "Navia F2P Melusine",
        "id_team": 2417,
        "nama_tim": "Navia Double Pyro",
        "karakter_build": [
            {"karakter": "Navia", "elemen": "Geo", "senjata": "Ultimate Overlord's Mega Magic Sword", "artefak": "2pc Petra 2pc Glad"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Favonius Sword", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "The Catch", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Sapwood Blade", "artefak": "Noblesse Oblige"}
        ]
    },

    # --- Tim: Chasca Rainbow (1 Build) ---
    {
        "id": 3296,
        "username": "astra",
        "nama_build": "Chasca Obsidian",
        "id_team": 3108,
        "nama_tim": "Chasca Rainbow",
        "karakter_build": [
            {"karakter": "Chasca", "elemen": "Anemo", "senjata": "Astral Vulture's Crimson Plumage", "artefak": "Obsidian Codex"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Splendor of Tranquil Waters", "artefak": "Golden Troupe"},
            {"karakter": "Ororon", "elemen": "Electro", "senjata": "Favonius Warbow", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Aquila Favonia", "artefak": "Noblesse Oblige"}
        ]
    },

    # ==================== AKUN: rejam ====================
    # --- Tim: Neuvillette Hyper (4 Build) ---
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
        "id": 4955,
        "username": "rejam",
        "nama_build": "Neuvillette Sac Jade",
        "id_team": 4175,
        "nama_tim": "Neuvillette Hyper",
        "karakter_build": [
            {"karakter": "Neuvillette", "elemen": "Hydro", "senjata": "Sacrificial Jade", "artefak": "Marechaussee Hunter"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Splendor of Tranquil Waters", "artefak": "Golden Troupe"},
            {"karakter": "Kaedehara Kazuha", "elemen": "Anemo", "senjata": "Freedom-Sworn", "artefak": "Viridescent Venerer"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Peak Patrol Song", "artefak": "Scroll of the Hero of Cinder City"}
        ]
    },
    {
        "id": 4988,
        "username": "rejam",
        "nama_build": "Neuvillette Proto Amber",
        "id_team": 4175,
        "nama_tim": "Neuvillette Hyper",
        "karakter_build": [
            {"karakter": "Neuvillette", "elemen": "Hydro", "senjata": "Prototype Amber", "artefak": "Marechaussee Hunter"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Fleuve Cendre Ferryman", "artefak": "Golden Troupe"},
            {"karakter": "Kaedehara Kazuha", "elemen": "Anemo", "senjata": "Xiphos' Moonlight", "artefak": "Viridescent Venerer"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Flute of Ezpitzal", "artefak": "Scroll of the Hero of Cinder City"}
        ]
    },
    {
        "id": 5012,
        "username": "rejam",
        "nama_build": "Neuvillette Lost Prayer",
        "id_team": 4175,
        "nama_tim": "Neuvillette Hyper",
        "karakter_build": [
            {"karakter": "Neuvillette", "elemen": "Hydro", "senjata": "Lost Prayer", "artefak": "Heart of Depth"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Festering Desire", "artefak": "Golden Troupe"},
            {"karakter": "Kaedehara Kazuha", "elemen": "Anemo", "senjata": "Iron Sting", "artefak": "Viridescent Venerer"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Favonius Sword", "artefak": "Scroll of the Hero of Cinder City"}
        ]
    },

    # --- Tim: Skirk Freeze (3 Build) ---
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
    {
        "id": 6319,
        "username": "rejam",
        "nama_build": "Skirk Marechaussee",
        "id_team": 5630,
        "nama_tim": "Skirk Freeze",
        "karakter_build": [
            {"karakter": "Skirk", "elemen": "Cryo", "senjata": "Mistsplitter Reforged", "artefak": "Marechaussee Hunter"},
            {"karakter": "Escoffier", "elemen": "Cryo", "senjata": "Symphonist of Scents", "artefak": "Golden Troupe"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Splendor of Tranquil Waters", "artefak": "Golden Troupe"},
            {"karakter": "Shenhe", "elemen": "Cryo", "senjata": "Favonius Lance", "artefak": "Noblesse Oblige"}
        ]
    },
    {
        "id": 6377,
        "username": "rejam",
        "nama_build": "Skirk Blizzard",
        "id_team": 5630,
        "nama_tim": "Skirk Freeze",
        "karakter_build": [
            {"karakter": "Skirk", "elemen": "Cryo", "senjata": "Finale of the Deep", "artefak": "Blizzard Strayer"},
            {"karakter": "Escoffier", "elemen": "Cryo", "senjata": "Deathmatch", "artefak": "Golden Troupe"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Favonius Sword", "artefak": "Tenacity"},
            {"karakter": "Shenhe", "elemen": "Cryo", "senjata": "Skyward Spine", "artefak": "2pc Glad 2pc Shime"}
        ]
    },

    # --- Tim: Alhaitham Quickbloom (2 Build) ---
    {
        "id": 4510,
        "username": "rejam",
        "nama_build": "Alhaitham Gilded",
        "id_team": 4420,
        "nama_tim": "Alhaitham Quickbloom",
        "karakter_build": [
            {"karakter": "Alhaitham", "elemen": "Dendro", "senjata": "Light of Foliar Incision", "artefak": "Gilded Dreams"},
            {"karakter": "Nahida", "elemen": "Dendro", "senjata": "A Thousand Floating Dreams", "artefak": "Deepwood Memories"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Festering Desire", "artefak": "Golden Troupe"},
            {"karakter": "Kuki Shinobu", "elemen": "Electro", "senjata": "Xiphos' Moonlight", "artefak": "Flower of Paradise Lost"}
        ]
    },
    {
        "id": 4599,
        "username": "rejam",
        "nama_build": "Alhaitham Marechaussee",
        "id_team": 4420,
        "nama_tim": "Alhaitham Quickbloom",
        "karakter_build": [
            {"karakter": "Alhaitham", "elemen": "Dendro", "senjata": "Light of Foliar Incision", "artefak": "Marechaussee Hunter"},
            {"karakter": "Nahida", "elemen": "Dendro", "senjata": "Wandering Evenstar", "artefak": "Deepwood Memories"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Splendor of Tranquil Waters", "artefak": "Golden Troupe"},
            {"karakter": "Kuki Shinobu", "elemen": "Electro", "senjata": "Iron Sting", "artefak": "Gilded Dreams"}
        ]
    },

    # --- Tim: Mualani Vape (3 Build) ---
    {
        "id": 5241,
        "username": "rejam",
        "nama_build": "Mualani Surf's Up",
        "id_team": 5192,
        "nama_tim": "Mualani Vape",
        "karakter_build": [
            {"karakter": "Mualani", "elemen": "Hydro", "senjata": "Surf's Up", "artefak": "Obsidian Codex"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Peak Patrol Song", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "Favonius Lance", "artefak": "Archaic Petra"},
            {"karakter": "Nahida", "elemen": "Dendro", "senjata": "A Thousand Floating Dreams", "artefak": "Instructor"}
        ]
    },
    {
        "id": 5289,
        "username": "rejam",
        "nama_build": "Mualani Widsith",
        "id_team": 5192,
        "nama_tim": "Mualani Vape",
        "karakter_build": [
            {"karakter": "Mualani", "elemen": "Hydro", "senjata": "The Widsith", "artefak": "Obsidian Codex"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Favonius Sword", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "The Catch", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Nahida", "elemen": "Dendro", "senjata": "Sacrificial Fragments", "artefak": "Gilded Dreams"}
        ]
    },
    {
        "id": 5334,
        "username": "rejam",
        "nama_build": "Mualani Ring Yaxche",
        "id_team": 5192,
        "nama_tim": "Mualani Vape",
        "karakter_build": [
            {"karakter": "Mualani", "elemen": "Hydro", "senjata": "Ring of Yaxche", "artefak": "Obsidian Codex"},
            {"karakter": "Xilonen", "elemen": "Geo", "senjata": "Flute of Ezpitzal", "artefak": "Scroll of the Hero of Cinder City"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "Favonius Lance", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Nahida", "elemen": "Dendro", "senjata": "Magic Guide", "artefak": "Instructor"}
        ]
    },

    # --- Tim: Kinich Burning (1 Build) ---
    {
        "id": 5916,
        "username": "rejam",
        "nama_build": "Kinich Fang",
        "id_team": 5874,
        "nama_tim": "Kinich Burning",
        "karakter_build": [
            {"karakter": "Kinich", "elemen": "Dendro", "senjata": "Fang of the Mountain King", "artefak": "Obsidian Codex"},
            {"karakter": "Emilie", "elemen": "Dendro", "senjata": "Lumidouce Elegy", "artefak": "Unfinished Reverie"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "Favonius Lance", "artefak": "Deepwood Memories"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Aquila Favonia", "artefak": "Noblesse Oblige"}
        ]
    },

    # ==================== AKUN: paimon ====================
    # --- Tim: Arlecchino Overload (4 Build) ---
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
        "id": 7885,
        "username": "paimon",
        "nama_build": "Arlecchino Gladiator",
        "id_team": 7319,
        "nama_tim": "Arlecchino Overload",
        "karakter_build": [
            {"karakter": "Arlecchino", "elemen": "Pyro", "senjata": "Staff of Homa", "artefak": "Gladiator's Finale"},
            {"karakter": "Chevreuse", "elemen": "Pyro", "senjata": "Rightful Reward", "artefak": "Song of Days Past"},
            {"karakter": "Fischl", "elemen": "Electro", "senjata": "Alley Hunter", "artefak": "Golden Troupe"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Aquila Favonia", "artefak": "Noblesse Oblige"}
        ]
    },
    {
        "id": 7921,
        "username": "paimon",
        "nama_build": "Arlecchino Deathmatch",
        "id_team": 7319,
        "nama_tim": "Arlecchino Overload",
        "karakter_build": [
            {"karakter": "Arlecchino", "elemen": "Pyro", "senjata": "Deathmatch", "artefak": "Fragment of Harmonic Whimsy"},
            {"karakter": "Chevreuse", "elemen": "Pyro", "senjata": "Black Tassel", "artefak": "Noblesse Oblige"},
            {"karakter": "Fischl", "elemen": "Electro", "senjata": "The Stringless", "artefak": "Golden Troupe"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Sapwood Blade", "artefak": "Instructor"}
        ]
    },
    {
        "id": 7964,
        "username": "paimon",
        "nama_build": "Arlecchino White Tassel",
        "id_team": 7319,
        "nama_tim": "Arlecchino Overload",
        "karakter_build": [
            {"karakter": "Arlecchino", "elemen": "Pyro", "senjata": "White Tassel", "artefak": "Gladiator's Finale"},
            {"karakter": "Chevreuse", "elemen": "Pyro", "senjata": "Black Tassel", "artefak": "2pc Tenacity 2pc Vourukasha"},
            {"karakter": "Fischl", "elemen": "Electro", "senjata": "Favonius Warbow", "artefak": "Golden Troupe"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Sapwood Blade", "artefak": "Noblesse Oblige"}
        ]
    },

    # --- Tim: Varesa Plunge (2 Build) ---
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
    },
    {
        "id": 9462,
        "username": "paimon",
        "nama_build": "Varesa Obsidian",
        "id_team": 8904,
        "nama_tim": "Varesa Plunge",
        "karakter_build": [
            {"karakter": "Varesa", "elemen": "Electro", "senjata": "Vivid Notions", "artefak": "Obsidian Codex"},
            {"karakter": "Xianyun", "elemen": "Anemo", "senjata": "Crane's Echoing Call", "artefak": "Viridescent Venerer"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Splendor of Tranquil Waters", "artefak": "Golden Troupe"},
            {"karakter": "Iansan", "elemen": "Electro", "senjata": "Engulfing Lightning", "artefak": "Scroll of the Hero of Cinder City"}
        ]
    },

    # --- Tim: Hu Tao Plunge (3 Build) ---
    {
        "id": 7124,
        "username": "paimon",
        "nama_build": "Hu Tao Marechaussee",
        "id_team": 7053,
        "nama_tim": "Hu Tao Plunge",
        "karakter_build": [
            {"karakter": "Hu Tao", "elemen": "Pyro", "senjata": "Staff of Homa", "artefak": "Marechaussee Hunter"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Splendor of Tranquil Waters", "artefak": "Golden Troupe"},
            {"karakter": "Yelan", "elemen": "Hydro", "senjata": "Aqua Simulacra", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Xianyun", "elemen": "Anemo", "senjata": "Crane's Echoing Call", "artefak": "Viridescent Venerer"}
        ]
    },
    {
        "id": 7188,
        "username": "paimon",
        "nama_build": "Hu Tao Crimson Witch",
        "id_team": 7053,
        "nama_tim": "Hu Tao Plunge",
        "karakter_build": [
            {"karakter": "Hu Tao", "elemen": "Pyro", "senjata": "Staff of Homa", "artefak": "Crimson Witch"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Festering Desire", "artefak": "Golden Troupe"},
            {"karakter": "Yelan", "elemen": "Hydro", "senjata": "Favonius Warbow", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Xianyun", "elemen": "Anemo", "senjata": "Oathsworn Eye", "artefak": "Viridescent Venerer"}
        ]
    },
    {
        "id": 7245,
        "username": "paimon",
        "nama_build": "Hu Tao Shimenawa",
        "id_team": 7053,
        "nama_tim": "Hu Tao Plunge",
        "karakter_build": [
            {"karakter": "Hu Tao", "elemen": "Pyro", "senjata": "Dragon's Bane", "artefak": "Shimenawa's Reminiscence"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Fleuve Cendre Ferryman", "artefak": "Golden Troupe"},
            {"karakter": "Yelan", "elemen": "Hydro", "senjata": "Favonius Warbow", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Xianyun", "elemen": "Anemo", "senjata": "Favonius Codex", "artefak": "Song of Days Past"}
        ]
    },

    # --- Tim: Raiden National (2 Build) ---
    {
        "id": 8210,
        "username": "paimon",
        "nama_build": "Raiden Engulfing",
        "id_team": 8146,
        "nama_tim": "Raiden National",
        "karakter_build": [
            {"karakter": "Raiden Shogun", "elemen": "Electro", "senjata": "Engulfing Lightning", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Xingqiu", "elemen": "Hydro", "senjata": "Sacrificial Sword", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "The Catch", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Aquila Favonia", "artefak": "Noblesse Oblige"}
        ]
    },
    {
        "id": 8279,
        "username": "paimon",
        "nama_build": "Raiden The Catch",
        "id_team": 8146,
        "nama_tim": "Raiden National",
        "karakter_build": [
            {"karakter": "Raiden Shogun", "elemen": "Electro", "senjata": "The Catch", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Xingqiu", "elemen": "Hydro", "senjata": "Favonius Sword", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Xiangling", "elemen": "Pyro", "senjata": "Dragon's Bane", "artefak": "Emblem of Severed Fate"},
            {"karakter": "Bennett", "elemen": "Pyro", "senjata": "Sapwood Blade", "artefak": "Noblesse Oblige"}
        ]
    },

    # --- Tim: Xiao FFXX (1 Build) ---
    {
        "id": 8607,
        "username": "paimon",
        "nama_build": "Xiao Vermillion",
        "id_team": 8532,
        "nama_tim": "Xiao FFXX",
        "karakter_build": [
            {"karakter": "Xiao", "elemen": "Anemo", "senjata": "Primordial Jade Winged-Spear", "artefak": "Vermillion Hereafter"},
            {"karakter": "Faruzan", "elemen": "Anemo", "senjata": "Favonius Warbow", "artefak": "Tenacity"},
            {"karakter": "Furina", "elemen": "Hydro", "senjata": "Splendor of Tranquil Waters", "artefak": "Golden Troupe"},
            {"karakter": "Xianyun", "elemen": "Anemo", "senjata": "Crane's Echoing Call", "artefak": "Noblesse Oblige"}
        ]
    }
]

# Susun riwayat otomatis dari referensi ID build agar data tim/build/snapshot selalu sinkron
_build_by_id = {item["id"]: item for item in build}
_data_tes_awal = [
    # Format: (id_riwayat, id_build, id_preset, id_dummy, dps, waktu)
    # --- astra (15 tes) ---
    (1127, 1583, 1, 1, 145739, "22-11-2026 14:15:20"),
    (1248, 1694, 2, 1, 138420, "22-11-2026 14:18:05"),
    (1359, 1728, 3, 2, 151890, "22-11-2026 14:20:42"),
    (2654, 3490, 3, 2, 192450, "22-11-2026 14:22:11"),
    (2711, 3512, 2, 2, 176800, "22-11-2026 14:24:30"),
    (2783, 3644, 3, 2, 184320, "22-11-2026 14:26:19"),
    (2839, 3789, 1, 1, 169540, "22-11-2026 14:28:47"),
    (2905, 3821, 1, 1, 155100, "22-11-2026 14:31:02"),
    (1842, 2105, 1, 1, 134900, "22-11-2026 14:33:15"),
    (1917, 2248, 2, 3, 129650, "22-11-2026 14:35:40"),
    (2314, 2501, 2, 2, 142300, "22-11-2026 14:38:12"),
    (2388, 2619, 1, 2, 136750, "22-11-2026 14:40:25"),
    (2452, 2733, 1, 1, 127400, "22-11-2026 14:42:51"),
    (2536, 2845, 1, 1, 118900, "22-11-2026 14:45:18"),
    (3174, 3296, 3, 2, 148600, "22-11-2026 14:48:03"),

    # --- rejam (13 tes) ---
    (4812, 4921, 1, 3, 128600, "22-11-2026 14:50:45"),
    (4867, 4955, 2, 3, 135400, "22-11-2026 14:53:10"),
    (4903, 4988, 1, 3, 114250, "22-11-2026 14:55:29"),
    (4949, 5012, 1, 1, 122900, "22-11-2026 14:57:54"),
    (6093, 6284, 2, 2, 164820, "22-11-2026 15:00:08"),
    (6148, 6319, 3, 2, 159400, "22-11-2026 15:02:33"),
    (6215, 6377, 1, 1, 147150, "22-11-2026 15:04:49"),
    (4318, 4510, 1, 1, 131800, "22-11-2026 15:07:15"),
    (4392, 4599, 2, 2, 138250, "22-11-2026 15:09:40"),
    (5116, 5241, 3, 2, 171600, "22-11-2026 15:12:04"),
    (5179, 5289, 2, 2, 158300, "22-11-2026 15:14:27"),
    (5263, 5334, 1, 1, 143750, "22-11-2026 15:16:51"),
    (5741, 5916, 2, 2, 149500, "22-11-2026 15:19:16"),

    # --- paimon (12 tes) ---
    (7508, 7842, 1, 1, 115300, "22-11-2026 15:21:33"),
    (7562, 7885, 2, 1, 111450, "22-11-2026 15:23:58"),
    (7619, 7921, 1, 2, 106800, "22-11-2026 15:26:20"),
    (7684, 7964, 1, 1,  96200, "22-11-2026 15:28:44"),
    (9186, 9415, 2, 3,  98450, "22-11-2026 15:31:09"),
    (9247, 9462, 2, 3, 108700, "22-11-2026 15:33:35"),
    (7018, 7124, 3, 2, 137900, "22-11-2026 15:35:52"),
    (7095, 7188, 2, 2, 129400, "22-11-2026 15:38:17"),
    (7162, 7245, 1, 1, 121650, "22-11-2026 15:40:41"),
    (8043, 8210, 1, 3, 109850, "22-11-2026 15:43:06"),
    (8119, 8279, 1, 3,  94600, "22-11-2026 15:45:29"),
    (8475, 8607, 2, 3, 124300, "22-11-2026 15:48:11")
]

riwayat = [
    {
        "id": id_tes,
        "username": _build_by_id[id_b]["username"],
        "id_team": _build_by_id[id_b]["id_team"],
        "id_build": id_b,
        "nama_tim": _build_by_id[id_b]["nama_tim"],
        "nama_build": _build_by_id[id_b]["nama_build"],
        "karakter_build": [dict(data) for data in _build_by_id[id_b]["karakter_build"]],
        "id_preset": id_p,
        "id_dummy": id_d,
        "dps": nilai_dps,
        "waktu": waktu_tes
    }
    for id_tes, id_b, id_p, id_d, nilai_dps, waktu_tes in _data_tes_awal
]

elemen_karakter_valid = ("Anemo", "Geo", "Electro", "Dendro", "Hydro", "Pyro", "Cryo")
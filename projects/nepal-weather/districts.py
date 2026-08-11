"""
districts.py

Contains data for all 77 districts of Nepal, organized by Province.
Includes approximate latitude and longitude for accurate weather fetching.
"""

DISTRICTS = {
    "Koshi Province": {
        "Bhojpur": {"latitude": 27.1667, "longitude": 87.0500},
        "Dhankuta": {"latitude": 26.9833, "longitude": 87.3333},
        "Ilam": {"latitude": 26.9167, "longitude": 87.9167},
        "Jhapa": {"latitude": 26.6500, "longitude": 87.8833},
        "Khotang": {"latitude": 27.2000, "longitude": 86.7833},
        "Morang": {"latitude": 26.6667, "longitude": 87.4000},
        "Okhaldhunga": {"latitude": 27.3167, "longitude": 86.5000},
        "Panchthar": {"latitude": 27.1500, "longitude": 87.7500},
        "Sankhuwasabha": {"latitude": 27.5833, "longitude": 87.2167},
        "Solukhumbu": {"latitude": 27.8167, "longitude": 86.6667},
        "Sunsari": {"latitude": 26.6000, "longitude": 87.1667},
        "Taplejung": {"latitude": 27.3500, "longitude": 87.6667},
        "Terhathum": {"latitude": 27.2500, "longitude": 87.5833},
        "Udayapur": {"latitude": 26.8333, "longitude": 86.6167}
    },
    "Madhesh Province": {
        "Bara": {"latitude": 27.0333, "longitude": 85.0000},
        "Dhanusha": {"latitude": 26.7333, "longitude": 86.0000},
        "Mahottari": {"latitude": 26.8833, "longitude": 85.8000},
        "Parsa": {"latitude": 27.2667, "longitude": 84.8667},
        "Rautahat": {"latitude": 26.9833, "longitude": 85.3167},
        "Saptari": {"latitude": 26.5833, "longitude": 86.7500},
        "Sarlahi": {"latitude": 27.0833, "longitude": 85.5667},
        "Siraha": {"latitude": 26.6500, "longitude": 86.2000}
    },
    "Bagmati Province": {
        "Bhaktapur": {"latitude": 27.6667, "longitude": 85.4167},
        "Chitwan": {"latitude": 27.5833, "longitude": 84.5000},
        "Dhading": {"latitude": 27.9667, "longitude": 84.8833},
        "Dolakha": {"latitude": 27.7667, "longitude": 86.1667},
        "Kathmandu": {"latitude": 27.7000, "longitude": 85.3333},
        "Kavrepalanchok": {"latitude": 27.5333, "longitude": 85.5500},
        "Lalitpur": {"latitude": 27.6667, "longitude": 85.3167},
        "Makwanpur": {"latitude": 27.4167, "longitude": 85.0333},
        "Nuwakot": {"latitude": 27.9167, "longitude": 85.1667},
        "Ramechhap": {"latitude": 27.3333, "longitude": 86.0833},
        "Rasuwa": {"latitude": 28.1167, "longitude": 85.3167},
        "Sindhuli": {"latitude": 27.2500, "longitude": 85.9667},
        "Sindhupalchok": {"latitude": 27.9500, "longitude": 85.8000}
    },
    "Gandaki Province": {
        "Baglung": {"latitude": 28.2667, "longitude": 83.5833},
        "Gorkha": {"latitude": 28.0000, "longitude": 84.6333},
        "Kaski": {"latitude": 28.2000, "longitude": 83.9833}, # Pokhara
        "Lamjung": {"latitude": 28.2333, "longitude": 84.4167},
        "Manang": {"latitude": 28.6667, "longitude": 84.0167},
        "Mustang": {"latitude": 28.9833, "longitude": 83.9833},
        "Myagdi": {"latitude": 28.3333, "longitude": 83.5000},
        "Nawalpur": {"latitude": 27.7000, "longitude": 84.1000},
        "Parbat": {"latitude": 28.2167, "longitude": 83.6833},
        "Syangja": {"latitude": 28.1000, "longitude": 83.8667},
        "Tanahun": {"latitude": 27.9667, "longitude": 84.2500}
    },
    "Lumbini Province": {
        "Arghakhanchi": {"latitude": 27.9000, "longitude": 83.2333},
        "Banke": {"latitude": 28.0833, "longitude": 81.6167},
        "Bardiya": {"latitude": 28.2500, "longitude": 81.3333},
        "Dang": {"latitude": 28.0000, "longitude": 82.2667},
        "Gulmi": {"latitude": 28.1000, "longitude": 83.2500},
        "Kapilvastu": {"latitude": 27.6167, "longitude": 83.0500},
        "Parasi": {"latitude": 27.5333, "longitude": 83.7167},
        "Palpa": {"latitude": 27.8667, "longitude": 83.5500},
        "Pyuthan": {"latitude": 28.1000, "longitude": 82.8667},
        "Rolpa": {"latitude": 28.3500, "longitude": 82.6333},
        "Rukum East": {"latitude": 28.5333, "longitude": 82.7833},
        "Rupandehi": {"latitude": 27.5000, "longitude": 83.4500}
    },
    "Karnali Province": {
        "Dailekh": {"latitude": 28.8333, "longitude": 81.7167},
        "Dolpa": {"latitude": 29.1333, "longitude": 83.0000},
        "Humla": {"latitude": 29.9500, "longitude": 81.8500},
        "Jajarkot": {"latitude": 28.7167, "longitude": 82.2000},
        "Jumla": {"latitude": 29.2833, "longitude": 82.1833},
        "Kalikot": {"latitude": 29.2000, "longitude": 81.7000},
        "Mugu": {"latitude": 29.5333, "longitude": 82.1667},
        "Rukum West": {"latitude": 28.5833, "longitude": 82.4667},
        "Salyan": {"latitude": 28.3667, "longitude": 82.1667},
        "Surkhet": {"latitude": 28.6000, "longitude": 81.6333}
    },
    "Sudurpashchim Province": {
        "Achham": {"latitude": 29.1167, "longitude": 81.2500},
        "Baitadi": {"latitude": 29.5333, "longitude": 80.5667},
        "Bajhang": {"latitude": 29.5500, "longitude": 81.1833},
        "Bajura": {"latitude": 29.5833, "longitude": 81.6667},
        "Dadeldhura": {"latitude": 29.3000, "longitude": 80.5833},
        "Darchula": {"latitude": 29.8333, "longitude": 80.5333},
        "Doti": {"latitude": 29.2667, "longitude": 80.9500},
        "Kailali": {"latitude": 28.6333, "longitude": 80.8833},
        "Kanchanpur": {"latitude": 28.8167, "longitude": 80.2167}
    }
}

import os, json
from dotenv import load_dotenv
from psnawp_api import PSNAWP

load_dotenv()

npsso = os.getenv("NPSSO")
psnawp = PSNAWP(npsso)

parsed_data = {}

my_data = psnawp.me()

ad = my_data.get_account_devices()
parsed_data["account_devices"] = []
for device in ad:
    parsed_device = {
        "device_type": device["deviceType"],
        "activation_type": device["activationType"],
        "activation_date": device["activationDate"],
    }
    parsed_data["account_devices"].append(parsed_device)

pl = my_data.get_profile_legacy()
parsed_data["profile_legacy"] = {
    "plus": pl["profile"]["plus"],
    "languages_used": pl["profile"]["languagesUsed"],
    "is_officially_verified": pl["profile"]["isOfficiallyVerified"],
    "personal_detail_sharing": pl["profile"]["personalDetailSharing"],
    "request_message_flag": pl["profile"]["personalDetailSharingRequestMessageFlag"],
}

parsed_data["title_stats"] = []
for title in my_data.title_stats(200):
    parsed_title = {
        "name": title.name,
        "first_time_played": title.first_played_date_time.strftime(
            "%d/%m/%Y, %H:%M:%S"
        ),
        "last_time_played": title.last_played_date_time.strftime("%d/%m/%Y, %H:%M:%S"),
        "play_count": title.play_count,
        "play_time": str(title.play_duration),
        "category": title.category.name,
    }
    parsed_data["title_stats"].append(parsed_title)

ts = my_data.trophy_summary()
parsed_data["trophy_summary"] = {
    "level": ts.trophy_level,
    "progress": ts.progress,
    "tier": ts.tier,
    "bronze": ts.earned_trophies.bronze,
    "silver": ts.earned_trophies.silver,
    "gold": ts.earned_trophies.gold,
    "platinum": ts.earned_trophies.platinum,
}

tt = my_data.trophy_titles()
parsed_data["trophy_titles"] = []
for trophy_title in tt:
    parsed_data["trophy_titles"].append(
        {
            "total_items_count": trophy_title.total_items_count,
            "service": trophy_title.np_service_name,
            "id": trophy_title.np_communication_id,
            "name": trophy_title.title_name,
            "detail": trophy_title.title_detail,
            "progress": trophy_title.progress,
            "earned_bronze": trophy_title.earned_trophies.bronze,
            "earned_silver": trophy_title.earned_trophies.silver,
            "earned_gold": trophy_title.earned_trophies.gold,
            "earned_platinum": trophy_title.earned_trophies.platinum,
            "defined_bronze": trophy_title.defined_trophies.bronze,
            "defined_silver": trophy_title.defined_trophies.silver,
            "defined_gold": trophy_title.defined_trophies.gold,
            "defined_platinum": trophy_title.defined_trophies.platinum,
            "date_of_last_trophy": trophy_title.last_updated_date_time.strftime(
                "%d/%m/%Y, %H:%M:%S"
            ),
            "title_id": trophy_title.np_title_id,
        }
    )

with open("output/parsed_data.json", "w") as file:
    json.dump(parsed_data, file, indent=4)

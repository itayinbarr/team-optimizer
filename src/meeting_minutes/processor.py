def extract_action_items(minutes):
    action_items = []
    for line in minutes.split('\n'):
        if "Action Item:" in line:
            action_items.append(line.replace("Action Item:", "").strip())
    return action_items

def process_all_minutes(minutes_dict):
    all_action_items = {}
    for filename, minutes in minutes_dict.items():
        all_action_items[filename] = extract_action_items(minutes)
    return all_action_items

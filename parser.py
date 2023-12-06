import csv
import os
import pandas as pd
from utility import print_updated as custom_print

def extract_feature_names(features_dict):
    feature_names = []
    for key, val in features_dict.items():
        feature_names.append(key)
    return feature_names

def process_top_performers(data, base_filename):
    rows = []
    for event in data['events']:
        competition_round = event['id']
        top_performer_id = event['top_element']
        points_earned = event['top_element_info']['points']
        row = {'round': competition_round, 'top_performer_id': top_performer_id, 'points_earned': points_earned}
        rows.append(row)
    
    output_file_path = os.path.join(base_filename, 'top_performers.csv')
    with open(output_file_path, 'w+', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['round', 'top_performer_id', 'points_earned'])
        writer.writeheader()
        writer.writerows(rows)

def process_participants(participants_list, base_filename):
    feature_names = extract_feature_names(participants_list[0])
    filename = base_filename + 'participants_raw.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w+', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, sorted(feature_names))
        writer.writeheader()
        for participant in participants_list:
            writer.writerow({k: str(v).encode('utf-8').decode('utf-8') for k, v in participant.items()})


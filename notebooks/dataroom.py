import os

# Define the root folder and subfolder structure
data_room_structure = {
    "1. Executive Summary": ["Company Overview", "Transaction Overview"],
    "2. Financial Information": ["Historical Financials", "Forecasts and Projections", "Financial Statements"],
    "3. Legal Documents": ["Incorporation Documents", "Shareholder Agreements", "Intellectual Property"],
    "4. Operational Information": ["Organizational Structure", "Key Contracts", "Product Information"],
    "5. HR and Employee Information": ["Employee Contracts", "Employee Benefits", "HR Policies"],
    "6. Market and Competitive Analysis": ["Market Research", "Competitor Analysis"],
    "7. Other Relevant Documents": ["Additional Information"]
}

def create_folder_structure(base_path, structure):
    for main_folder, subfolders in structure.items():
        main_folder_path = os.path.join(base_path, main_folder)
        os.makedirs(main_folder_path, exist_ok=True)
        for subfolder in subfolders:
            subfolder_path = os.path.join(main_folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
        print(f"Created folder: {main_folder_path}")

# Define the root directory for the data room
root_directory = "DataRoom"

# Create the folder structure
create_folder_structure(root_directory, data_room_structure)

print("Data room folder structure created successfully.")
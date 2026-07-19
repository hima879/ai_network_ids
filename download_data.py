import pandas as pd
import urllib.request
import os

def download_nsl_kdd():
    """Download NSL-KDD dataset files"""
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # URLs for NSL-KDD dataset
    urls = {
        'train': 'https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain%2B.txt',
        'test': 'https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTest%2B.txt'
    }
    
    # Column names for the dataset
    columns = [
        'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
        'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
        'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
        'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
        'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate',
        'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
        'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
        'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
        'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label', 'difficulty'
    ]
    
    print("Downloading NSL-KDD dataset...")
    
    for name, url in urls.items():
        print(f"Downloading {name} data...")
        try:
            urllib.request.urlretrieve(url, f'data/{name}.txt')
            print(f"✓ {name} data downloaded successfully")
        except Exception as e:
            print(f"✗ Error downloading {name}: {e}")
            return False
    
    print("\n✓ Dataset downloaded successfully!")
    print(f"Files saved in: {os.path.abspath('data')}")
    return True

if __name__ == "__main__":
    download_nsl_kdd()

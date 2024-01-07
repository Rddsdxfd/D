import os

# Mount drive at the same location each time
drive_path = '/content/drive/MyDrive/Fooocus'
if not os.path.exists(drive_path):
    from google.colab import drive
    drive.mount('/content/drive')
    !mkdir -p {drive_path}
    
# Clone and run from the mounted drive path    
%cd {drive_path}  
!if [ ! -d "Fooocus" ]; then git clone https://github.com/lllyasviel/Fooocus.git; fi
%cd Fooocus
!python entry_with_update.py --share

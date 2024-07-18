import os
import shutil
import time

# jellyfin video and actor image dir
video_dir = "/volume1/video/Movie"
jellyfin_actor_dir = "/volume1/docker/jellyfin/config/metadata/People"

def repair_actor_images(base_dir, target_dir):
    # init
    actor_total_number = 0
    actor_new_number = 0

    # 1. Iterate through the source directory, looking for the.actors directory

    for root, dirs, files in os.walk(base_dir):
        # Check whether the current directory contains the.actors folder
        if '.actors' in dirs:
            actors_dir = os.path.join(root, '.actors')

            # 2. Traverse the images of actors in the.actors directory

            for filename in os.listdir(actors_dir):
                actor_total_number = actor_total_number + 1

                # 3. Find out if the image of the actor exists in the jellyfin actor library

                # Check whether the file is in a supported image format
                if os.path.splitext(filename)[1].lower() in ('.png', '.jpg', '.jpeg', '.gif', '.bmp'):
                    # Take the first character of the actor's name
                    actor_first_char = filename[0]
                    # get acotor name
                    actor_name = os.path.splitext(filename)[0]
                    # Assemble the target actor library picture path
                    actor_path = os.path.join(target_dir, actor_first_char, actor_name)
                    # If already exists, skip it
                    if os.path.exists(actor_path):
                        continue

                    # 4. If does not exist, add a picture of the actor

                    print(f"Actors don't exist：{actor_name}")
                    # Ensure that the target directory exists 
                    os.makedirs(actor_path, exist_ok=True)
                    # Construct the source image path and the target image path
                    src_path = os.path.join(actors_dir, filename)
                    dst_path = os.path.join(actor_path, 'folder.jpg')
                    # Copy  
                    shutil.copy(src_path, dst_path)
                    # Print processed image file information 
                    print(f"Copyed {src_path} to {dst_path}")
                    actor_new_number = actor_new_number + 1

    # Statistics
    print(f"Total: {actor_total_number}, New: {actor_new_number}")

# Record start time
start_time = time.time()
# Calling function
repair_actor_images(video_dir, jellyfin_actor_dir)
# Record end time
end_time = time.time()
# Calculations take time and print
elapsed_time = end_time - start_time
print(f"Program execution took time: {elapsed_time:.1f} seconds")

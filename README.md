# Projekt-BBD

## Requirements

* Python 3.6 (`pip install -r python_requirements.txt`)

## ISIC dataset
<img src="sample_images/ISIC_0000000.jpg?raw=true" height="300">
<img src="sample_images/ISIC_0000010.jpg?raw=true" height="300">
<img src="sample_images/ISIC_0000020.jpg?raw=true" height="300">

[ISIC Gallery](https://www.isic-archive.com/#!/topWithHeader/onlyHeaderTop/gallery)  

[ISIC Archive Downloader](https://github.com/GalAvineri/ISIC-Archive-Downloader)

Usage:  
`python ../ISIC-Archive-Downloader/download_archive.py --num-images 5000 -s --images-dir data/ISIC/images --descs-dir data/ISIC/description --seg-dir data/ISIC/segmentation --seg-skill expert --p 100`
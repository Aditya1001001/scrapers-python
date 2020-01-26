## Color Scraper

 This is a basic web scraper I made to create a color database for my py-dropper tool script that you can find [here](https://github.com/Aditya1001001/py-dropper).
 It scrapes the URL-https://www.december.com/html/spec/colorhex.html

It extracts the color names and their respective hexcode, it then converts the hexcode to RBG values and stores all the information in a .csv file.

### Instructions for use:
 * I recommend creating a conda environment using `conda create --name=<env_name> python=3.7`
 * Run `pip install -r requirements,txt`
 * Use the scraper- `python color-scraper.py`
 * The .csv file has the format- `navy (16 SVG),#000080,0,0,128 `



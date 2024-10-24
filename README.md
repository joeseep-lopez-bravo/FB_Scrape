# Scrape_FB

## Setup Instructions

Before you begin, make sure to create the database. You can find the necessary SQL commands in the `facebook_db.sql` file. Execute this file in your PostgreSQL environment to create the required tables.

### Database Configuration

Once you have created the database, update the connection parameters in the code (`user`, `password`, `port`, and `localhost`) to match your PostgreSQL database settings.

### Running the Script

To execute the scraping code, run the following command:

```bash
python execute_FB_scrape.py
````

## Requirements
To Run this scapre code you'll need to install : 
- Python 
- Seleniuum
- PostgreSQL

### Dependencies
Libraries that you will need:

- **selenium**: 
- **fake_useragent**: 
- **psycopg2**: 
- **pyautogui**:
- **logging**: 
- **configparser**: 
```bash
pip install selenium

pip install fake-useragent

pip install psycopg2

pip install pyautogui

pip install logging 
```

## Appendix

### Links to Scrape

To specify the links you want to scrape, enter them in the following files:

- `Pages_FB.py`
- `Groups_FB.py`
- `Profiles.py`

In each of these files, update the `self."type_page"_links` list with the URLs you wish to scrape:

```python
self."type_page"_links = [
    'https://www.facebook.com/groups/chamba.dev',
    # Uncomment and add more links as needed
    # 'https://www.facebook.com/groups/1444669812310758',
    # 'https://www.facebook.com/groups/820135186662129',
    # 'https://www.facebook.com/groups/315599014441',
    # 'https://www.facebook.com/groups/2901591359932748',
    # 'https://www.facebook.com/groups/971462149627421',
    # Add more links based on the file you are using
]
````
### Adding Profiles

To add profile credentials, save them in the `credentials.conf` file using the following format:

```conf
usernamekey=934399812
passwordkey=SergioMaldito1

usernamekey2=username__tuyo
passwordkey2=password_tuyo

usernamekey3=daniel@gmail.com
passwordkey3=E721

usernamekey4=gabielmax@gmail.com
passwordkey4=Aquispepower72

````
### Run separately

```bash
py pagina_fb.py

py groups_fb.py

py perfil_fb.py

py image_process.py
````
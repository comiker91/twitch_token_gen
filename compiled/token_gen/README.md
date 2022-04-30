# Twitch Token Genertator


## Run from Exe:

Only Windows support:

To use you have to fill your app informations in the config_template.ini 
and save it ass config.ini.

Now use the token_gen.exe 

## Run from code:

Install the requiremets.txt

Windows
> pip install -r requirements.txt

Linux
> pip3 install -r requirements.txt


Now fill your app informations in the config_template.ini 
and save it ass config.ini.

If you don't have an app you can create it at [Twitch Console](https://dev.twitch.tv/console/apps)

After that just use token_gen.py 

Windows:
> python token_gen.py

Linux:
> python3 token_gen.py

Your files with the token are in the outputfolder (if you have changed in the config at this path)
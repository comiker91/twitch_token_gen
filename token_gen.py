import os
import configparser

from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope


print("Start generate Token....")
config = configparser.ConfigParser()

if os.path.isfile("config.ini"):
    config.read("config.ini")

    output_path = config.get("output","path", fallback="./output/")
    oaut = output_path + config.get("output","token", fallback="token.txt")
    refresh = output_path + config.get("output","refresh", fallback="refresh.txt")
    scopes = config.get("twitch", "scopes", fallback="chat_read,chat_edit")

    try:
        app_id = config.get("twitch","id")
        app_secret = config.get("twitch","secret")

    except configparser.NoOptionError:
        print("Not all twitch data found...")
        input("Press enter to exit...")
        exit()

else:
    print("You need to create a config.ini from the config_template.ini")
    input("Press enter to exit...")
    exit()


target_scope = []

scopes = scopes.split(", ")

for scope in scopes:
    target = scope.upper()
    target_scope.append(eval(f"AuthScope.{target}"))


twitch = Twitch(app_id=app_id, app_secret=app_secret)
auth = UserAuthenticator(twitch, target_scope, force_verify=False)

# this will open your default browser and prompt you with the twitch verification website
print("please check your browser!")
token, refresh_token = auth.authenticate()


print("Write Token")
with open(oaut, "w") as write:
    write.write(token)

print("Write refresh token")
with open(refresh, "w") as write:
    write.write(refresh_token)

print("Finished")
input("Press enter to close")

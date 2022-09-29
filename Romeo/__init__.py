from Romeo.modules.core.app import App
from Romeo.modules.core.bot import Bot
from Romeo.modules.core.dir import dirr
from Romeo.modules.core.git import git
from Romeo.misc import dbb, heroku, sudo

from .console import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
bot = Bot()

# Assistant Client
app = App()

from Romeo.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

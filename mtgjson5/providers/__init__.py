"""
Provider Dispatcher
"""

from .cardhoarder import CardHoarderProvider
from .cardkingdom import CardKingdomProvider
from .cardmarket.monolith import CardMarketProvider
from .cardmarket.set_name_translations import CardMarketProviderSetNameTranslations
from .edhrec.card_ranks import EdhrecProviderCardRanks
from .gatherer import GathererProvider
from .github_boosters import GitHubBoostersProvider
from .github_decks import GitHubDecksProvider
from .github_mtgsqlite import GitHubMTGSqliteProvider
from .mtgban import MTGBanProvider
from .multiversebridge import MultiverseBridgeProvider
from .scryfall import ScryfallProvider
from .tcgplayer import TCGPlayerProvider
from .whats_in_standard import WhatsInStandardProvider
from .wizards import WizardsProvider

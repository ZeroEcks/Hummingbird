class Anime(object):
    """
    Object to model the anime structure.
    """

    anime_id = 0
    slug = ''
    title = {'canonical':'','english':'','romanji':''}
    status = ''
    url = ''
    episode_count = 0
    episode_length = 0
    cover_image = ''
    synopsis = ''
    show_type = ''
    genres = []
    airInfo = {'start':'','end':''}
    screencaps = []
    yt_id = ''
    com_rating = 0
    age_rating = ''



    def __init__(self, anime_dict):
        """
        anime_dict: a dict with all the elements of the anime object struct

        Instalises the class and assigns all the elements to internal objects.

        genres is optional and defaults to an empty list.
        """

        self.anime_id = anime_dict['id']
        self.slug = anime_dict['slug']
        self.title = (anime_dict['canonical_title'],anime_dict['english_title'],anime_dict['romaji_title'])
        self.status = anime_dict['status']
        self.url = anime_dict['url']
        self.episode_count = anime_dict['episode_count']
        self.episode_length = anime_dict['episode_length']
        self.cover_image = anime_dict['cover_image']
        self.synopsis = anime_dict['synopsis']
        self.show_type = anime_dict['show_type']
        self.airInfo = (anime_dict['started_airing'],anime_dict['finished_airing'])
        self.screencaps =  anime_dict['screencaps']
        self.yt_id =  anime_dict['youtube_trailer_id']
        self.com_rating = anime_dict['community_rating']
        self.age_rating =  anime_dict['age_rating']
        try:
            self.genres = anime_dict['genres']
        except KeyError:
            self.genres = []


class LibraryEntry(object):
    """
    Object to model a library entry.
    """

    entry_id = 0
    episodes_watched = 0
    last_watched = ''
    rewatched_times = 0
    notes = ''
    notes_present = False
    status = ''
    private = False
    rewatching = False
    anime = None
    rating = None

    def __init__(self, entry_dict):
        """
        entry_dict: A dictionary witht he elements of a library entry struct

        Instalises the class and assigns all the elements to internal objects.

        notes_present determines if notes is empty or not, you can check by
            seeing if notes is '' also.
        """
        self.entry_id = entry_dict['id']
        self.episodes_watched = entry_dict['episodes_watched']
        # The date in ISO 8601 format.
        self.last_watched = entry_dict['last_watched']
        self.rewatched_times = entry_dict['rewatched_times']
        self.notes_present = entry_dict['notes_present']
        if self.notes_present is True:
            self.notes = entry_dict['notes']
        self.status = entry_dict['status']
        self.private = entry_dict['private']
        self.rewatching = entry_dict['rewatching']
        self.anime = Anime(entry_dict['anime'])
        self.rating = LibraryEntryRating(entry_dict['rating'])


class LibraryEntryRating(object):
    """
    Object to model a library entry rating.
    """

    rating_type = ''
    value = ''

    def __init__(self, rating_dict):
        """
        rating_dict: a dictionary with the elements of a rating object.

        Instalises the class and assigns all the elements to internal objects.

        Rating type determines if value is an int.
        """
        self.rating_type = rating_dict['type']
        self.value = rating_dict['value']


class User(object):
    """
    Object to model a user.
    """

    name = ''
    waifu = ''
    waifu_or_husbando = ''
    waifu_slug = ''
    waifu_char_id = ''
    location = ''
    website = ''
    avatar = ''
    cover_image = ''
    about = ''
    bio = ''
    karma = ''
    life_spent_on_anime = ''
    show_adult_content = False
    title_language_preference = ''
    last_library_update = ''
    online = False
    following = ''
    favorites = []

    def __init__(self, user_dict):
        """
        user_dict: a dictionary with the elements of a user object.

        Instalises the class and assigns all the elements to internal objects.
        """
        self.name = user_dict['name']
        self.waifu = user_dict['waifu']
        self.waifu_or_husbando = user_dict['waifu_or_husbando']
        self.waifu_slug = user_dict['waifu_slug']
        self.waifu_char_id = user_dict['waifu_char_id']
        self.location = user_dict['location']
        self.website = user_dict['website']
        self.avatar = user_dict['avatar']
        self.cover_image = user_dict['cover_image']
        self.about = user_dict['about']
        self.bio = user_dict['bio']
        self.karma = user_dict['karma']
        self.life_spent_on_anime = user_dict['life_spent_on_anime']
        self.show_adult_content = user_dict['show_adult_content']
        self.title_language_preference = user_dict['title_language_preference']
        self.last_library_update = user_dict['last_library_update']
        self.online = user_dict['online']
        self.following = user_dict['following']
        for item in user_dict['favorites']:
            self.favorites.append(Favorite(item))


class Favorite(object):
    """
    Object to model a favorite anime.
    """

    fav_id = 0
    user_id = 0
    item_id = 0
    item_type = ''
    created_at = ''
    updated_at = ''
    fav_rank = 0

    def __init__(self, fav_dict):
        """
        fav_dict: a dictionary with the elements of a favorite object.

        Instalises the class and assigns all the elements to internal objects.
        """
        self.fav_id = fav_dict['id']
        self.user_id = fav_dict['user_id']
        self.item_id = fav_dict['item_id']
        self.item_type = fav_dict['item_type']
        self.created_at = fav_dict['created_at']
        self.updated_at = fav_dict['updated_at']
        self.fav_rank = fav_dict['fav_rank']


class MiniUser(object):
    """
    Object to model a user.
    """

    name = ''
    url = ''
    avatar = ''
    avatar_small = ''
    nb = False

    def __init__(self, user_dict):
        """
        user_dict: a dictionary with the elements of a user object.

        Instalises the class and assigns all the elements to internal objects.
        """
        self.name = user_dict['name']
        self.url = user_dict['url']
        self.avatar = user_dict['avatar']
        self.avatar_small = user_dict['avatar_small']
        self.nb = user_dict['nb']


class Story(object):
    """
    Object to model a story.
    """

    story_id = 0
    story_type = ''
    user = None
    updated_at = ''
    self_post = False
    poster = None
    media = None
    substories_count = 0
    substories = []

    def __init__(self, story_dict):
        """
        story_dict: a dictionary with the elements of a user object.

        Instalises the class and assigns all the elements to internal objects.
        """

        self.story_id = story_dict['id']
        self.user = Miniuser(story_dict['user'])
        self.updated_at = story_dict['updated_at']
        self.story_type = story_dict['story_type']
        if self.story_type == 'comment':
            self.self_post = story_dict['self_post']
            self.poster = Miniuser(story_dict['poster'])
        elif self.story_type == media_story:
            self.media = Anime(story_dict['media'])
        self.substories_count = story_dict['substories_count']
        for item in story_dict['substories_count']:
            self.substories.append(Substory(story_dict['substories']))


class Substory(object):
    """
    Object to model a substory.
    """

    substory_id = 0
    substory_type = ''
    created_at = ''
    comment = ''
    episode_number = 0
    followed_user = None
    new_status = ''
    service = None
    permissions = {}

    def __init__(self, story_dict):
        """
        story_dict: a dictionary with the elements of a substory object.

        Instalises the class and assigns all the elements to internal objects.
        """

        self.substory_id = story_dict['id']
        self.substory_type = story_dict['substory_type']
        if self.substory_type == 'comment':
            self.comment = story_dict['comment']
        elif self.substory_type == 'watched_episode':
            self.episode_number = story_dict['episode_number']
        elif self.substory_type == 'watchlist_status_update':
            self.service = story_dict['service']
            self.new_status = story_dict['new_status']
        elif self.substory_type == 'followed':
            self.followed_user = Miniuser(story_dict['followed_user'])

        self.created_at = story_dict['created_at']
        for item in story_dict['substories_count']:
            self.substories.append(Substory(story_dict['substories']))

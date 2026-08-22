# achievement_manage.py

import json
import os


class AchievementManage:
    SAVE_FILE = "achievements.json"

    # Achievements that represent dragon types.
    # These are used for "four of a kind".
    DRAGON_TYPES = {
        "icey_dragon",
        "grey_psychic",
        "firery_dragon",
        "greenish_dragon",
    }

    @classmethod
    def _load(cls):
        """
        Load achievement data from the JSON save file.
        Creates an empty/default structure if the file does not exist.
        """
        if not os.path.exists(cls.SAVE_FILE):
            raise FileNotFoundError(
                f"Could not find {cls.SAVE_FILE}. "
                "Create it first using your achievement JSON."
            )

        with open(cls.SAVE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    @classmethod
    def _save(cls, data):
        """Save all achievement data."""
        with open(cls.SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @classmethod
    def Achieve(cls, row):
        """
        Unlock an achievement.

        Usage:
            AchievementManage.Achieve("first things first")

        If the achievement is already unlocked (1), nothing happens.

        Also checks special achievement rules afterwards.
        """

        data = cls._load()

        # Check if the requested achievement exists
        if row not in data:
            print(f"Achievement '{row}' does not exist.")
            return False

        # Prevent non-achievement data from being unlocked
        if row in ("quests", "Number of killed dragons"):
            print(f"'{row}' is not an achievement.")
            return False

        # Already achieved
        if data[row] == 1:
            return False

        # Unlock achievement
        data[row] = 1

        print(f"Achievement unlocked: {row}")

        # Check special rules
        cls._check_special_achievements(data)

        cls._save(data)
        return True

    @classmethod
    def Quests(cls, quest_name):
        """
        Add a completed quest to the 'quests' array.

        A quest can only be added once.

        Usage:
            AchievementManage.Quests(quest.name)

        Example:
            AchievementManage.Quests("Save the village")
        """

        data = cls._load()

        # Make sure quests exists
        if "quests" not in data:
            data["quests"] = []

        # Only add unique quests
        if quest_name not in data["quests"]:
            data["quests"].append(quest_name)

            print(f"Quest completed: {quest_name}")

            # Check quest progress achievements
            cls._check_quest_achievements(data)

            cls._save(data)
            return True

        # Quest was already completed before
        return False

    @classmethod
    def DragonSlayed(cls, dragon_type=None):
        """
        Increase the total number of dragons killed by 1.

        Optional:
            You can provide a dragon achievement/type:

            AchievementManage.DragonSlayed("icey_dragon")

        This will:
        1. Increase total dragons killed.
        2. Unlock the specified dragon type.
        3. Check "four of a kind".
        4. Check "Dragon slayer".
        """

        data = cls._load()

        if "Number of killed dragons" not in data:
            data["Number of killed dragons"] = 0

        data["Number of killed dragons"] += 1

        # Unlock the dragon type if provided
        if dragon_type is not None:
            if dragon_type in cls.DRAGON_TYPES:
                data[dragon_type] = 1
            else:
                print(
                    f"Warning: '{dragon_type}' "
                    "is not a registered dragon type."
                )

        # Check achievements
        cls._check_special_achievements(data)

        cls._save(data)

        return data["Number of killed dragons"]

    @classmethod
    def _check_special_achievements(cls, data):
        """
        Check achievements that depend on other achievements
        or counters.

        Important:
        Simply unlocking a dragon-type achievement will NOT
        automatically increase the dragon kill counter.

        This prevents achievements from accidentally progressing
        other achievements.
        """

        # --------------------------------------------------
        # FOUR OF A KIND
        # Requires 4 DIFFERENT dragon types.
        # --------------------------------------------------

        dragon_types_killed = sum(
            1
            for dragon in cls.DRAGON_TYPES
            if data.get(dragon, 0) == 1
        )

        if dragon_types_killed >= 4:
            data["four of a kind"] = 1

        # --------------------------------------------------
        # DRAGON SLAYER
        # Requires killing 5 dragons.
        # --------------------------------------------------

        if data.get("Number of killed dragons", 0) >= 5:
            data["Dragon slayer"] = 1

    @classmethod
    def _check_quest_achievements(cls, data):
        """
        Check achievements based on the percentage of
        original quests completed.

        You MUST set TOTAL_ORIGINAL_QUESTS to the actual
        number of original quests in your game.
        """

        TOTAL_ORIGINAL_QUESTS = 100  # CHANGE THIS

        completed_quests = len(data.get("quests", []))

        if TOTAL_ORIGINAL_QUESTS <= 0:
            return

        progress = completed_quests / TOTAL_ORIGINAL_QUESTS

        # 1/4 of quests
        if progress >= 0.25:
            data["Boooring"] = 1

        # 1/2 of quests
        if progress >= 0.50:
            data["Boooringer"] = 1

        # 3/4 of quests
        if progress >= 0.75:
            data["Questinggg"] = 1

        # All quests
        if progress >= 1.0:
            data["Boooringest"] = 1

    @classmethod
    def IsAchieved(cls, row):
        """
        Check whether an achievement is unlocked.

        Example:
            if AchievementManage.IsAchieved("abracarabra"):
                print("Player knows their first spell!")
        """

        data = cls._load()
        return data.get(row, 0) == 1

    @classmethod
    def GetData(cls):
        """
        Return all achievement/save data.
        """
        return cls._load()

import pygame
import json
import os


class AchievementManage:
    SAVE_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "achievements.json"
    )

    # Achievement descriptions
    ACHIEVEMENT_DESCRIPTIONS = {
        "first things first": "Complete your first quest.",
        "abracarabra": "Learn your first spell.",

        "Boooring": "Complete 1/4 of all original quests.",
        "Boooringer": "Complete 1/2 of all original quests.",
        "Boooringest": "Complete all original quests.",

        "Budda's friend": "Meditate for the first time.",
        "Calm in a storm": "Meditate 5 times in a row.",

        "weak spot": "Hit a dragon's weak spot.",
        "weakness": "Hit a dragon using its weakness.",

        "Questinggg": "Complete 3/4 of all original quests.",

        "What was that?": "Drink a magic potion.",
        "Intresting...": (
            "Learn a type of dragon weakness from quests "
            "instead of the library."
        ),

        "Thats usefull!": (
            "Learn all dragon weakness types at once."
        ),

        "Weapon collectioner": "Have 3 weapons at once.",
        "Armor collectioner": "Have 3 armors at once.",

        "book of spells": "Learn 3 spells in one run.",

        "Thats sorta unfair but whatever": (
            "Use any healing potion."
        ),

        "Magic in your veins!": "Drink a mana potion.",
        "Bad trip": "Drink too many mana potions.",
        "Hyper heal": "Drink a legendary healing potion.",

        "Legendary weapon": (
            "Obtain the legendary Arcanus Sword."
        ),

        "Not that game 1": "Obtain the Terrablade.",
        "Not that game 2": "Obtain the Dark Sword.",
        "Not that game 3": "Obtain the Obanium Sword.",

        "Legendary armor": "Obtain legendary armor.",

        "Wild beast": "Kill a werewolf.",
        "Self harm is bad": (
            "Experience a bandit hitting himself."
        ),

        "THIEEEF!": "Get robbed by a goblin.",
        "Ouch, you traidor!": (
            "Get hit by your own sword."
        ),

        "Lucky coins": "Kill a gremlin.",

        "Silent thief": (
            "Heal while completing the steal medicine quest."
        ),

        "Im a failure!": "Fail a quest twice in a row.",

        "Mage potencial": (
            "Learn a spell on the first try."
        ),

        "The chosen one": "Kill the final boss.",

        # Dragon achievements
        "icey_dragon": "Slay an Icey Dragon.",
        "grey_psychic": "Slay a Grey Psychic Dragon.",
        "firery_dragon": "Slay a Firery Dragon.",
        "greenish_dragon": "Slay a Greenish Dragon.",

        "four of a kind": (
            "Slay 4 different types of dragons."
        ),

        "Dragon slayer": "Slay 5 dragons."
    }

    @classmethod
    def _load(cls):
        with open(cls.SAVE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def AchievementMenu(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
        import pygame
        import colors
        from button import Button

        # Load achievement data once when opening the menu
        data = AchievementManage._load()

        # -----------------------------
        # FONTS
        # -----------------------------

        title_font = pygame.font.SysFont(
            "Arial",
            42,
            bold=True
        )

        achievement_font = pygame.font.SysFont(
            "Arial",
            24,
            bold=True
        )

        description_font = pygame.font.SysFont(
            "Arial",
            18
        )

        status_font = pygame.font.SysFont(
            "Arial",
            18,
            bold=True
        )

        # -----------------------------
        # BACK BUTTON
        # -----------------------------

        back_button_width = 200
        back_button_height = 60

        back_button = Button(
            SCREEN_WIDTH // 2 - back_button_width // 2,
            SCREEN_HEIGHT - 75,
            back_button_width,
            back_button_height,
            "Back",
            colors.RED,
            colors.DARK_RED
        )

        # -----------------------------
        # SCROLL SETTINGS
        # -----------------------------

        scroll_offset = 0
        scroll_speed = 40

        # Area where achievements can scroll
        top_area = 110
        bottom_area = SCREEN_HEIGHT - 250

        achievement_height = 75

        # -----------------------------
        # MAIN MENU LOOP
        # -----------------------------

        running = True

        while running:

            mouse_pos = pygame.mouse.get_pos()

            # -------------------------
            # EVENTS
            # -------------------------

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                # Scroll with mouse wheel
                if event.type == pygame.MOUSEWHEEL:

                    scroll_offset -= event.y * scroll_speed

                    # Prevent scrolling above the start
                    if scroll_offset < 0:
                        scroll_offset = 0

                # Back button
                if back_button.is_clicked(
                    mouse_pos,
                    event
                ):
                    running = False

            # -------------------------
            # UPDATE DATA
            # -------------------------

            # Reload every frame so achievement changes
            # can appear immediately if necessary
            data = AchievementManage._load()

            # -------------------------
            # BACKGROUND
            # -------------------------

            screen.fill((0, 0, 0))

            # -------------------------
            # TITLE
            # -------------------------

            title_surface = title_font.render(
                "ACHIEVEMENTS",
                True,
                colors.WHITE
            )

            title_rect = title_surface.get_rect(
                center=(
                    SCREEN_WIDTH // 2,
                    35
                )
            )

            screen.blit(
                title_surface,
                title_rect
            )

            # -------------------------
            # DRAGON COUNTER
            # -------------------------

            dragons_killed = data.get(
                "Number of killed dragons",
                0
            )

            dragon_text = achievement_font.render(
                f"Dragons killed: {dragons_killed}",
                True,
                colors.WHITE
            )

            screen.blit(
                dragon_text,
                (
                    30,
                    75
                )
            )

            # -------------------------
            # ACHIEVEMENTS
            # -------------------------

            achievement_count = len(
                AchievementManage.ACHIEVEMENT_DESCRIPTIONS
            )

            # Calculate maximum possible scroll
            content_height = (
                achievement_count
                * achievement_height
            )

            visible_height = (
                bottom_area
                - top_area
            )

            max_scroll = max(
                0,
                content_height
                - visible_height
            )

            # Keep scroll in valid range
            if scroll_offset > max_scroll:
                scroll_offset = max_scroll

            # Draw every achievement
            for index, (
                achievement_name,
                description
            ) in enumerate(
                AchievementManage.ACHIEVEMENT_DESCRIPTIONS.items()
            ):

                y = (
                    top_area
                    + index * achievement_height
                    - scroll_offset
                )

                # Don't draw achievements outside
                # the visible achievement area
                if y + achievement_height < top_area:
                    continue

                if y > bottom_area:
                    continue

                # Is achievement unlocked?
                unlocked = (
                    data.get(
                        achievement_name,
                        0
                    ) == 1
                )

                # Achievement rectangle
                achievement_rect = pygame.Rect(
                    20,
                    y,
                    SCREEN_WIDTH - 40,
                    achievement_height - 5
                )

                if unlocked:

                    background_color = (
                        45,
                        100,
                        55
                    )

                    status = "UNLOCKED"

                    status_color = (
                        100,
                        255,
                        120
                    )

                else:

                    background_color = (
                        60,
                        60,
                        70
                    )

                    status = "LOCKED"

                    status_color = (
                        255,
                        100,
                        100
                    )

                # Draw achievement background
                pygame.draw.rect(
                    screen,
                    background_color,
                    achievement_rect,
                    border_radius=10
                )

                # Achievement name
                name_surface = achievement_font.render(
                    achievement_name,
                    True,
                    colors.WHITE
                )

                screen.blit(
                    name_surface,
                    (
                        35,
                        y + 7
                    )
                )

                # Achievement description
                description_surface = description_font.render(
                    description,
                    True,
                    (220, 220, 220)
                )

                screen.blit(
                    description_surface,
                    (
                        35,
                        y + 40
                    )
                )

                # Achievement status
                status_surface = status_font.render(
                    status,
                    True,
                    status_color
                )

                status_rect = status_surface.get_rect(
                    right=SCREEN_WIDTH - 35,
                    centery=y + achievement_height // 2
                )

                screen.blit(
                    status_surface,
                    status_rect
                )

            # -------------------------
            # QUEST SECTION
            # -------------------------

            quest_box_y = SCREEN_HEIGHT - 230
            quest_box_height = 135

            quest_box = pygame.Rect(
                20,
                quest_box_y,
                SCREEN_WIDTH - 40,
                quest_box_height
            )

            pygame.draw.rect(
                screen,
                (35, 35, 50),
                quest_box,
                border_radius=10
            )

            quest_title = achievement_font.render(
                "Completed Quests",
                True,
                colors.WHITE
            )

            screen.blit(
                quest_title,
                (
                    35,
                    quest_box_y + 10
                )
            )

            quests = data.get(
                "quests",
                []
            )

            quest_y = quest_box_y + 50

            # Show completed quests
            if len(quests) == 0:

                no_quests = description_font.render(
                    "No quests completed yet.",
                    True,
                    (180, 180, 180)
                )

                screen.blit(
                    no_quests,
                    (
                        40,
                        quest_y
                    )
                )

            else:

                for quest in quests:

                    # Don't draw outside quest box
                    if quest_y > (
                        quest_box_y
                        + quest_box_height
                        - 25
                    ):
                        break

                    quest_surface = description_font.render(
                        f"- {quest}",
                        True,
                        colors.WHITE
                    )

                    screen.blit(
                        quest_surface,
                        (
                            40,
                            quest_y
                        )
                    )

                    quest_y += 25

            # -------------------------
            # BACK BUTTON
            # -------------------------

            back_button.check_hover(
                mouse_pos
            )

            back_button.draw(
                screen
            )

            # -------------------------
            # UPDATE SCREEN
            # -------------------------

            pygame.display.flip()
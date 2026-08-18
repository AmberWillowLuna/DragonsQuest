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
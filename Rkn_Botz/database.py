# AutoCaptionBot by RknDeveloper
# Copyright (c) 2024 RknDeveloper
# Licensed under the MIT License
# https://github.com/RknDeveloper/Rkn-AutoCaptionBot/blob/main/LICENSE
# Please retain this credit when using or forking this code.

# Developer Contacts:
# Telegram: @RknDeveloperr
# Updates Channel: @Rkn_Bots_Updates & @Rkn_Botz
# Special Thanks To: @ReshamOwner
# Update Channels: @Digital_Botz & @DigitalBotz_Support

# ⚠️ Please do not remove this credit!

import motor.motor_asyncio
from config import Rkn_Botz

class Database:
    def __init__(self):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(Rkn_Botz.DB_URL)
        self._database = self._client[Rkn_Botz.DB_NAME]
        self._users_collection = self._database.get_collection("users_data")
        self._channels_collection = self._database.get_collection("channels_data")

    async def register_user(self, user_id: int) -> bool:
        """
        Tries to register a user by their user_id.
        Returns True if inserted, False if user already existed.
        """
        try:
            result = await self._users_collection.insert_one({"userId": user_id})
            return bool(result.inserted_id)
        except Exception as exc:
            # If duplicate key error, user exists, silently ignore
            return False

    async def fetch_total_users(self) -> int:
        """
        Returns total number of unique users registered.
        """
        return await self._users_collection.count_documents({})

    async def list_all_users(self) -> list[int]:
        """
        Fetches all user IDs from database.
        """
        cursor = self._users_collection.find({}, {"userId": 1, "_id": 0})
        user_ids = []
        async for record in cursor:
            user_ids.append(record.get("userId"))
        return user_ids

    async def remove_user_by_id(self, user_id: int) -> int:
        """
        Deletes user by user_id.
        Returns number of deleted documents (0 or 1).
        """
        result = await self._users_collection.delete_one({"userId": user_id})
        return result.deleted_count

    async def add_channel_caption(self, channel_id: int, caption: str):
        """
        Insert a new channel with its caption.
        """
        doc = {"channelId": channel_id, "caption": caption}
        await self._channels_collection.insert_one(doc)

    async def update_channel_caption(self, channel_id: int, new_caption: str) -> bool:
        """
        Updates caption for existing channel.
        Returns True if updated, False if no matching channel found.
        """
        result = await self._channels_collection.update_one(
            {"channelId": channel_id},
            {"$set": {"caption": new_caption}},
            upsert=False
        )
        return result.modified_count > 0
        
rkn_botz = Database()

# ————
# End of file
# Original author: @RknDeveloperr
# GitHub: https://github.com/RknDeveloper

# Developer Contacts:
# Telegram: @RknDeveloperr
# Updates Channel: @Rkn_Bots_Updates & @Rkn_Botz
# Special Thanks To: @ReshamOwner
# Update Channels: @Digital_Botz & @DigitalBotz_Support

# ⚠️ Please do not remove this credit!
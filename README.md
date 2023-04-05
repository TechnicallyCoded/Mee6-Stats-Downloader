# Mee6 Stats Converter

## Description
Do you want to extract the data collected by Mee6 to use with your own bot? Mee6 won't provide this data to you for obvious reasons...
This is a script/program which will download all this data to a machine readable format "JSON" and act as your browser to evade restrictions of API access.
The machine readable format should allow you to then import all existing user data into your own bot.

## How to use it?
When loading the leaderboard page, Mee6's website loads the data in "pages". This allows quick access of the top X users immediately as you load the page, then loads the rest of the data as you request more instead of trying to get all the data immediately (slow).
We will ~~abuse~~ use this feature to download the data.

1. Open your developer tools on the website, and find the XHR request to get any page. It doesn't have
to be the first one.
2. Copy the cURL command from Chrome/Firefox developer tools. This program will simulate being your 
browser and retrieve all pages of data 0 -> X until there is no more data to retrieve.

Set the environment variable "CURL_COMMAND" to the curl command you copied, then run the script.

The format it saves the data to is JSON. Example output data:
```
[
  // First page of data
  [
    // First entry of this page
    {
      "avatar": "00000000000000000000000000000000", // avatar id (can be used to fetch the user's profile picture)
      "detailed_xp": [11873, 12980, 225198], 		// not sure?
      "discriminator": "0000", 						// #1234 "discriminator" of this user
      "guild_id": "000000000000000000", 			// guild id
      "id": "000000000000000000", 					// discord user snowflake
      "level": 46, 									// mee6 level of this user
      "message_count": 11258, 						// total messages counted for this user by mee6
      "username": "MY_USERNAME", 					// Human readable username of this user
      "xp": 225198 									// total xp of this user
    },
    // Entry X of this page
    {
      ...
    },

    ...
  ],
  // Next page of data
  [
    ...
  ]
]
```

## Extra details
You can retrive the user avatar using this link format: https://cdn.discordapp.com/avatars/USER_SNOWFLAKE_ID/AVATAR_ID.webp?size=512

## Example Mee6 page entry for other developers' reference
This is the data format for one entry of Mee6's website data (inside of one page). I automatically retrieve the "player" object and write it to a separate file.

```
{
  "admin": true,
  "banner_url": null,
  "country": "FR",
  "guild": {
    "allow_join": false,
    "application_commands_enabled": true,
    "commands_prefix": null,
    "icon": "GUILD_ICON_ID",
    "id": "GUILD_SNOWFLAKE_ID",
    "invite_leaderboard": false,
    "leaderboard_url": "https://mee6.xyz/leaderboard/GUILD_ID",
    "name": "GUILD_NAME",
    "premium": false
  },
  "is_member": true,
  "page": 39,
  "player": {
    "avatar": "USER_AVATAR_ID",
    "detailed_xp": [
      1530,
      9655,
      137575
    ],
    "discriminator": "0000",
    "guild_id": "GUILD_SNOWFLAKE_ID",
    "id": "USER_SNOWFLAKE_ID",
    "level": 39,
    "message_count": 6877,
    "rank": 4,
    "username": "TechnicallyCoded",
    "xp": 137575
  },
  "players": [],
  "role_rewards": [],
  "user_guild_settings": {
    "guild_id": "GUILD_SNOWFLAKE_ID",
    "use_default_rank_card": true,
    "user_id": "USER_SNOWLAKE_ID"
  },
  "xp_per_message": [
    15,
    25
  ],
  "xp_rate": 1
}
```
#!/usr/local/bin/env python3

import requests as R
import secrets as S
import importlib
importlib.reload(S)

base_url = f"http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks&user={S.username}&limit=1000&api_key={S.apikey}&format=json&from=0"

x = R.get(base_url)
print(x)
x.content
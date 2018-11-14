import json

import requests


# See
# https://github.com/todbot/Blink1Control2/blob/master/app/server/apiServer.js
# https://www.alfredapp.com/help/workflows/inputs/script-filter/json/


def items():
    yield {"uid": "off", "title": "Off", "arg": "http://localhost:8934/blink1/off"}
    yield {"uid": "on", "title": "On", "arg": "http://localhost:8934/blink1/on"}

    try:
        result = requests.get("http://localhost:8934/blink1/pattern")
        result.raise_for_status()
    except:
        yield {"title": "Error reading server"}
    else:
        for pattern in result.json().get("patterns", []):
            yield {
                "title": pattern["name"],
                "subtitle": pattern["pattern"],
                "arg": "http://localhost:8934/blink1/pattern/play?pname="
                + pattern["name"],
            }


print(json.dumps({"items": list(items())}))

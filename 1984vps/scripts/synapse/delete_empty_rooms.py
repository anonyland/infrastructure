import requests
import urllib

token = 'TOKEN'
server = 'https://matrix.anonymousland.org'
api_rooms = f'{server}/_synapse/admin/v1/rooms?dir=b&from=0&limit=20&order_by=joined_local_members&access_token={token}'
delete_api = f'{server}/_synapse/admin/v1/rooms/'

local_users = 0
while local_users == 0:
    r = requests.get(api_rooms)
    print(r.text)
    rooms = r.json()
    headers = {
        'authorization': f'Bearer {token}'
    }
    for room in rooms['rooms']:
        local_users = room['joined_local_members']
        if local_users == 0:
            roomid = urllib.parse.quote(room['room_id'])
            print('delete', delete_api + roomid)
            r = requests.delete(delete_api + roomid, headers=headers, json={})
            if r.status_code != 200:
                print(r.text)
                break
        else:
            print("there are local users in this room", room)
            break
print("Done.")
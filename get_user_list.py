import json
import urllib.request
import time
import csv
import codecs

dynamic_id = '408799797598853973'

ori = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?dynamic_id=" \
      + dynamic_id
ori_info = json.loads(urllib.request.urlopen(ori).read())
counts = ori_info['data']['card']['desc']['repost']
time.sleep(2)

repo_dict = {'counts': 0}
real_count = 0

tmp_count = 0

while tmp_count < counts:
    rep = "https://api.live.bilibili.com/dynamic_repost/v1/dynamic_repost/view_repost?dynamic_id=" + dynamic_id \
          + "&offset=" + str(tmp_count)
    bili_dict = json.loads(urllib.request.urlopen(rep).read())
    repo = bili_dict['data']['comments']

    for one_repo in repo:
        tmp_count += 1
        info_dict = {}

        desc = one_repo['detail']['desc']
        uid = 'U' + str(desc['uid'])
        if uid in repo_dict.keys():
            continue
        real_count += 1
        repo_dict[uid] = [desc['timestamp'], desc['user_profile']['info']['uname']]

    time.sleep(2)
repo_dict['counts'] = real_count

for uid in repo_dict.keys():
    if uid == 'counts':
        print(repo_dict[uid])
        continue
    t, name = repo_dict[uid]
    print(uid, name, t)

header = ['Num', 'Time', 'UID', 'Name']
rows = []
for key in repo_dict.keys():
    if key == 'counts':
        continue
    time, name = repo_dict[key]
    uid = int(key[1:])
    time = int(time)
    rows.append([time, uid, name])

rows.sort(key=lambda x: x[0])
for i in range(len(rows)):
    rows[i] = [str(i + 1)] + rows[i]

with codecs.open('repo.csv', 'w', encoding='utf-8-sig') as f:
    ff = csv.writer(f)
    ff.writerow(header)
    ff.writerows(rows)

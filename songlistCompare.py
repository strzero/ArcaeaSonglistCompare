import os
import json

result = []
oldTable, newTable = {}, {}
oldFile, newFile = input(['请输入旧版本Songlist文件名 Input file name of old Songlist']), input(['请输入新版本Songlist文件名 Input file name of new Songlist'])
with open(oldFile, encoding='utf-8') as file_obj:
    old = json.loads(file_obj.read())
with open(newFile, encoding='utf-8') as file_obj:
    new = json.loads(file_obj.read())
for k in old['songs']:
    oldTable[k['id']] = k
for k in new['songs']:
    newTable[k['id']] = k
for k in oldTable:
    if oldTable[k]['difficulties'][0]['rating'] != newTable[k]['difficulties'][0]['rating']:
        result.append(str(oldTable[k]['title_localized']['en']) + ' [PST] ' + str(oldTable[k]['difficulties'][0]['rating'])
                      + ' to ' + str(newTable[k]['difficulties'][0]['rating']))
    if oldTable[k]['difficulties'][1]['rating'] != newTable[k]['difficulties'][1]['rating']:
        result.append(str(oldTable[k]['title_localized']['en']) + ' [PRS] ' + oldTable[k]['difficulties'][1]['rating']
                      + ' to ' + str(newTable[k]['difficulties'][1]['rating']))

    if 'ratingPlus' in oldTable[k]['difficulties'][2]:
        oldTable[k]['difficulties'][2]['rating'] = str(oldTable[k]['difficulties'][2]['rating'])+'+'
    if 'ratingPlus' in newTable[k]['difficulties'][2]:
        newTable[k]['difficulties'][2]['rating'] = str(newTable[k]['difficulties'][2]['rating'])+'+'

    if oldTable[k]['difficulties'][2]['rating'] != newTable[k]['difficulties'][2]['rating']:
        result.append(str(oldTable[k]['title_localized']['en']) + ' [FTR] ' + str(oldTable[k]['difficulties'][2]['rating'])
                      + ' to ' + str(newTable[k]['difficulties'][2]['rating']))
    if 3 in oldTable[k]['difficulties']:
        if oldTable[k]['difficulties'][3]['rating'] != newTable[k]['difficulties'][3]['rating']:
            result.append(str(oldTable[k]['title_localized']['en']) + ' [PRS] ' + oldTable[k]['difficulties'][3]['rating']
                        + ' to ' + str(newTable[k]['difficulties'][3]['rating']))
for p in result:
    print(p)
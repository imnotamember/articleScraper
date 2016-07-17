import aggregator
import os

foldr = 'C:\\Users\\Joshua\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\no041e92.default\\zotero\\storage'
#foldr = 'C:\\Users\\Joshua\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\no041e92.default\\zotero\\storage\\textFiles'
foldr2 = 'C:\\Users\\Joshua\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\no041e92.default\\zotero\\storage\\textFiles'
listTxt = aggregator.collect_files(foldr, 5)

for i in xrange(0, len(listTxt)):
    file_path = os.path.join(foldr2, 'Txt%s.txt' % i)
    with open(file_path, 'ab') as f:
        f_content = listTxt[i]
        f.write(f_content)

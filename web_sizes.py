import pickle

with open('./web_size.pickle', 'rb') as handle:
  sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
  sites_new = pickle.load(handle)

sum = 0
empty_sites = 0
print(sites[0])
print(sites_new[0])

### 1. feladat
print(f'------')
# For ciklussal végig a tömbön, és a "sum" növelése az egyes siteok méretével
for site in sites_new:
  sum += site['size']
total_size_gb = round(sum / 1024, 2)
print(f'total size is: {total_size_gb} Gb')

# Átlagos site méret kiszámitása GB-ban
avg_size_gb = round((sum / len(sites_new)) / 1024, 2)
print(f'avg site size is: {avg_size_gb} Gb')



### 2. feladat
print(f'------')
# Site méret változás ellenőrzése
for i in range(len(sites)):
  if sites[i]['size'] != sites_new[i]['size']:
    difference = sites_new[i]['size'] - sites[i]['size'] #ha csökkent akkor negativ érték lesz
    change_ratio = round(difference / (sites_new[i]['size'] / 100), 2)
    print(f"{sites_new[i]['domain']} changed by: {'+' if change_ratio > 0 else ''}{change_ratio} %")
      


### 3. feladat
print(f'------')
# Üres siteok megszámlálása a sites_new -ba
for site in sites_new:
  if site['size'] == 0:
    empty_sites += 1
print(f'there are {empty_sites} empty sites')



### 4. feladat
print(f'------')
# Weboldalak méretének listázása
for site in sites_new:
  if site['size'] == 0: #ha 0 akkor nem történik semmi
    continue
  elif site['size'] >= 1024: # ha nagyobb vagy éppen 1GB akkor GB-ban irja ki
    size_gb = round(site['size'] / 1024, 2)
    print(f"{site['domain']} is: {size_gb} Gb")
  else:
    print(f"{site['domain']} is: {site['size']} Mb") #minden egyéb eset (0 és 1024mb között)
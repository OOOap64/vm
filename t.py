import sqlite3

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('datas.db')
    conn.row_factory = sqlite3.Row
    return conn


conn=get_db_connection()
conn.execute("""
DROP TABLE Comp
""")
conn.execute("""CREATE TABLE IF NOT EXISTS Comp(id INTEGER PRIMARY KEY,
                  name VARCHAR(50), 
                  price INTEGER, 
                  type VARCHAR(20),
                  videocard VARCHAR(70), 
                  processor VARCHAR(70),
                  mother_curcuit VARCHAR(70),
                  RAM VARCHAR(70),
                  SSD VARCHAR(70),
                  ads VARCHAR(100),
                  img VARCHAR(30))""")
conn.commit()
conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(1,'G1 PRO', 168700 , 'pro', 'NVIDIA RTX A1000', 'Intel® Core™ i5-14400F', '32GB TEAMGROUP T-Create Expert 
             Black [DDR5, 6400MHz, 2x16GB]', '1TB Samsung 990 PRO', '3 Vesnin Brothers Boulevard', 'img/pro1.png' )""")
conn.commit()
conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(2,'G2 PRO', 190700, 'pro', 'NVIDIA RTX A1000', 'Intel® Core™ i5-14400K[F]', '32GB TEAMGROUP T-Create Expert Black [DDR5, 6400MHz, 2x16GB]', '1TB Samsung 990 PRO', 'Avtozavodskaya St., 18', 'img/pro2.png')""")
conn.commit()
conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(3,'G3 PRO', 351400, 'pro', 'NVIDIA RTX 4000 Ada Generation [20GB, 6144 CUDA]',  'Intel® Core™ i7-14700F', '64GB TEAMGROUP T-Create
              Expert Black [DDR5, 6400MHz, 2x32GB]',  '1TB Samsung 990 PRO', 'Avtozavodskaya St., 18', 'img/pro3.png')""")
conn.commit()
conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(4, 'G4 PRO', 578200, 'pro',  'Palit GeForce RTX 5090 GameRock [32GB, 21760 CUDA]', 'AMD Ryzen 9 9950X', '64GB TEAMGROUP T-Create Expert Black [DDR5, 6400MHz, 2x32GB]', '1TB Samsung 990 PRO', '2nd Paveletsky Proyezd, 7s8, Moscow', 'img/pro4.png')""")
conn.commit()
conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(5, 'BrandStar G8184772', 97850, 'game', 'nVidia RTX 5060 8GB', 'Intel Core i5-13400F',  'DDR5 32GB PC-44800 5600MHz','1TB M.2 NVMe SSD', 'Avtozavodskaya St., 18', 'img/game1.png')""")
conn.commit()

conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(6, 'BrandStar G8105622', 154350, 'game', 'nVidia RTX 5070 Ti 16GB', 'Intel Core i7-14700F', 'DDR5 16GB PC-44800 5600MHz', '1TB M.2 NVMe SSD', 'Derbenevskaya Street, 3, Moscow', 'img/game2.png')""")
conn.commit()

conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(7, 'IRU Game 510H6SEA', 72290, 'game','NVIDIA GeForce RTX 3060 12288МБ', 'Intel Core i5 12400F','DDR4 16ГБ 3200МГц', 'SSD 512ГБ' , '37s12 Altufyevskoye Shosse, Moscow',  'img/game3.png')""")
conn.commit()

conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(8, 'Power-Play A88', 88200, 'game', 'Palit GeForce
              RTX 5060 8GB DUAL ','AMD Ryzen 5 7500F
              OEM 100-000000597',  ' ADATA XPG LANCER Blade RGB Black
              (AX5U6000C3016G-DTLABRBK)', 'Kingston NV3 (SNV3S/1000G)', '37s12 Altufyevskoye
              Shosse, Moscow', 'img/game4.png')""")
conn.commit()

conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(9, 'ARENA 30882', 96740, 'office', 'Radeon Graphics', 'AMD Ryzen 9 9950X', '64 ГБ/DDR5', 'M2 1 ТБ', '37s12 Altufyevskoye Shosse, Moscow', 'img/office1.png')""")
conn.commit()
conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(10, 'ARENA 30882', 42780, 'office', 'Radeon Graphics', 'AMD Ryzen 5 9600X', '16 ГБ/DDR5', 'M2 1 ТБ', 'Avtozavodskaya St., 18', 'img/office2.png')""")
conn.commit()
conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(11, 'AREANA 30887', 49420, 'office', 'Radeon Graphics', 'AMD Ryzen 7 9700X', '16 ГБ/DDR5', 'M2 1 ТБ', '2nd Paveletsky Proyezd, 7s8, Moscow', 'img/office3.png')""")
conn.commit()
conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(12, 'iRU Planio 310H6SEV',  31290, 'budjet', ' Intel UHD Graphics 730', ' Intel Core i3 12100, 3.3 ГГц', ' 8 ГБ, DDR4, DIMM, 3200 МГц', 'SSD 256 ГБ M.2 2280, PCI-E', '3 Vesnin Brothers Boulevard', 'img/budjet1.png' )""")
conn.commit()
conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(13, 'Неттоп Acer Gadget ETBox X', 33990, 'budjet', 'Intel UHD Graphics', 'Intel Core i3 1220P, 1.5 ГГц', '16 ГБ, DDR4, SO-DIMM','SSD 512 ГБ M.2 2280, PCI-E', 'Aminyevskoe shosse, 6', 'img/budjet2.png'
 )""")
conn.commit()

conn.execute("""insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
values(14, 'Неттоп iRU 110JLCN',  16990, 'budjet',' Intel UHD Graphics', 'Intel Celeron N5105, 2 ГГц ', '8 ГБ, DDR4, SO-DIMM, 2666 МГц', 'SSD 256 ГБ поддержка NVMe', 'Derbenevskaya Street, 3, Moscow', 'img/budjet3.png'
)""")
conn.commit()
# 12, 'iRU Planio 310H6SEV', False, 31290, 'budjet', ' Intel UHD Graphics 730', ' Intel Core i3 12100, 3.3 ГГц', ' 8 ГБ, DDR4, DIMM, 3200 МГц', 'SSD 256 ГБ M.2 2280, PCI-E', '1 5 6', 'img/budjet1.png'
# 13, 'Неттоп Acer Gadget ETBox X', False,33990, 'budjet', 'Intel UHD Graphics', 'Intel Core i3 1220P, 1.5 ГГц', '16 ГБ, DDR4, SO-DIMM','SSD 512 ГБ M.2 2280, PCI-E', '6 2 4', 'img/budjet2.png'
# 14, 'Неттоп iRU 110JLCN', False, 16990, 'budjet',' Intel UHD Graphics', 'Intel Celeron N5105, 2 ГГц ', '8 ГБ, DDR4, SO-DIMM, 2666 МГц', 'SSD 256 ГБ поддержка NVMe', '3 4 6', 'img/budjet3.png'


conn.close()
# insert into Comp(id, name, price, type, videocard, processor, RAM, SSD, ads, img) 
# values(1,'G1 PRO', 168700 , 'pro', 'NVIDIA RTX A1000', 'Intel® Core™ i5-14400F', '32GB TEAMGROUP T-Create Expert Black [DDR5, 6400MHz, 2x16GB]', '1TB Samsung 990 PRO', '1 6 4', 'img/pro1' ),
# (2,'G2 PRO', 190700, 'pro', NVIDIA RTX A1000', 'Intel® Core™ i5-14400K[F]', , '32GB TEAMGROUP T-Create Expert Black [DDR5, 6400MHz, 2x16GB]', '1TB Samsung 990 PRO', '2 3 5', 'img/pro2'),
# (3,'G3 PRO', 351400, 'pro', 'NVIDIA RTX 4000 Ada Generation [20GB, 6144 CUDA]',  'Intel® Core™ i7-14700F', '64GB TEAMGROUP T-Create Expert Black [DDR5, 6400MHz, 2x32GB]',  '1TB Samsung 990 PRO', '1 2 3', 'img/pro3'), 
# (4, 'G4 PRO', 578200, 'pro',  'Palit GeForce RTX 5090 GameRock [32GB, 21760 CUDA]', 'AMD Ryzen 9 9950X', '64GB TEAMGROUP T-Create Expert Black [DDR5, 6400MHz, 2x32GB]', '1TB Samsung 990 PRO', '4 1 2', 'img/pro4'),
# (5, 'BrandStar G8184772', 97 850, 'game', 'nVidia RTX 5060 8GB', 'Intel Core i5-13400F', ' Intel H610 M.2 DDR5 mATX', 'DDR5 32GB PC-44800 5600MHz','1TB M.2 NVMe SSD', '5 6 2', 'img/game1'),
# (6, 'BrandStar G8105622', 154350, 'game', 'nVidia RTX 5070 Ti 16GB', 'Intel Core i7-14700F', 'DDR5 16GB PC-44800 5600MHz' '1TB M.2 NVMe SSD', '2 3 4', 'img/game2'),
# (7, 'IRU Game 510H6SEA', 72290, 'game','NVIDIA GeForce RTX 3060 12288МБ', 'Intel Core i5 12400F','DDR4 16ГБ 3200МГц', 'SSD 512ГБ' , 'img/game3'),
# (8, 'Power-Play A88', 88200, 'game', 'Palit GeForce RTX 5060 8GB DUAL ','AMD Ryzen 5 7500F OEM 100-000000597',  ' ADATA XPG LANCER Blade RGB Black (AX5U6000C3016G-DTLABRBK)', 'Kingston NV3 (SNV3S/1000G)', '3 5 6', 'img/game4'),
# (9, 'ARENA 30882', 96740, 'Radeon Graphics', 'AMD Ryzen 9 9950X', '64 ГБ/DDR5', 'M2 1 ТБ', '2 1 4', 'img/office1'),
# (10, 'ARENA 30882', 42780, 'Radeon Graphics', 'AMD Ryzen 5 9600X', '16 ГБ/DDR5', 'M2 1 ТБ', '1 2', 'img/office2'),
# (11, 'AREANA 30887', 49420, 'Radeon Graphics', 'AMD Ryzen 7 9700X', '16 ГБ/DDR5', 'M2 1 ТБ', '3 5 6', 'img/office3'),


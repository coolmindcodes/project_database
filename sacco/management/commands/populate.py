from django.core.management import BaseCommand

from sacco.models import Customer


class Command(BaseCommand):
    def handle(self, *args, **options):
        customers = [{"first_name":"Piotr","last_name":"Rockwell","email":"prockwell0@ucoz.com","gender":"Male","weight":76,"dob":"2003-01-20"},
{"first_name":"Gilles","last_name":"Samms","email":"gsamms1@telegraph.co.uk","gender":"Male","weight":59,"dob":"1999-03-31"},
{"first_name":"Paige","last_name":"Szymaniak","email":"pszymaniak2@vistaprint.com","gender":"Female","weight":73,"dob":"2003-01-23"},
{"first_name":"Annadiana","last_name":"Andress","email":"aandress3@marketwatch.com","gender":"Female","weight":54,"dob":"2001-09-14"},
{"first_name":"Dalton","last_name":"Platts","email":"dplatts4@ustream.tv","gender":"Male","weight":75,"dob":"2000-02-11"},
{"first_name":"Bank","last_name":"Merveille","email":"bmerveille5@census.gov","gender":"Male","weight":93,"dob":"2004-01-23"},
{"first_name":"Parry","last_name":"Purslow","email":"ppurslow6@cyberchimps.com","gender":"Male","weight":71,"dob":"2001-08-07"},
{"first_name":"Cassie","last_name":"Grewcock","email":"cgrewcock7@topsy.com","gender":"Male","weight":67,"dob":"2000-06-07"},
{"first_name":"Burty","last_name":"McDugal","email":"bmcdugal8@myspace.com","gender":"Male","weight":87,"dob":"1999-04-29"},
{"first_name":"Casi","last_name":"Arrowsmith","email":"carrowsmith9@aboutads.info","gender":"Female","weight":54,"dob":"2004-06-07"},
{"first_name":"Vince","last_name":"Biasioni","email":"vbiasionia@who.int","gender":"Male","weight":61,"dob":"2001-07-06"},
{"first_name":"Farica","last_name":"Saunier","email":"fsaunierb@themeforest.net","gender":"Female","weight":98,"dob":"2002-06-05"},
{"first_name":"Chase","last_name":"Ochiltree","email":"cochiltreec@constantcontact.com","gender":"Male","weight":82,"dob":"2004-02-25"},
{"first_name":"Selene","last_name":"Rewbottom","email":"srewbottomd@imgur.com","gender":"Female","weight":65,"dob":"2001-01-04"},
{"first_name":"Vassili","last_name":"Brunel","email":"vbrunele@elegantthemes.com","gender":"Male","weight":93,"dob":"2001-01-09"},
{"first_name":"Carrissa","last_name":"Corke","email":"ccorkef@noaa.gov","gender":"Female","weight":53,"dob":"2002-10-09"},
{"first_name":"Clarisse","last_name":"Teasdale-Markie","email":"cteasdalemarkieg@gov.uk","gender":"Female","weight":94,"dob":"1999-08-04"},
{"first_name":"Bartie","last_name":"Coppeard","email":"bcoppeardh@theguardian.com","gender":"Male","weight":70,"dob":"2003-07-02"},
{"first_name":"Geri","last_name":"Young","email":"gyoungi@mediafire.com","gender":"Male","weight":64,"dob":"2002-03-02"},
{"first_name":"Eustace","last_name":"Rogliero","email":"eroglieroj@flavors.me","gender":"Male","weight":77,"dob":"2003-03-07"},
{"first_name":"Heath","last_name":"Durbann","email":"hdurbannk@wp.com","gender":"Male","weight":52,"dob":"2001-02-08"},
{"first_name":"Ingunna","last_name":"Rappport","email":"irappportl@nytimes.com","gender":"Female","weight":63,"dob":"2003-06-20"},
{"first_name":"Scotty","last_name":"Casper","email":"scasperm@statcounter.com","gender":"Male","weight":69,"dob":"2002-03-20"},
{"first_name":"Madelene","last_name":"Isselee","email":"misseleen@dell.com","gender":"Female","weight":49,"dob":"2004-05-08"},
{"first_name":"Aubrey","last_name":"Morilla","email":"amorillao@webeden.co.uk","gender":"Female","weight":91,"dob":"1999-12-30"},
{"first_name":"Georgie","last_name":"Gillow","email":"ggillowp@ow.ly","gender":"Male","weight":56,"dob":"2003-11-01"},
{"first_name":"Giustino","last_name":"Tweede","email":"gtweedeq@cafepress.com","gender":"Male","weight":74,"dob":"2004-10-27"},
{"first_name":"Law","last_name":"Sher","email":"lsherr@berkeley.edu","gender":"Male","weight":40,"dob":"1999-08-09"},
{"first_name":"Lyman","last_name":"Gater","email":"lgaters@huffingtonpost.com","gender":"Male","weight":41,"dob":"2004-03-17"},
{"first_name":"Marcellina","last_name":"Waterworth","email":"mwaterwortht@amazon.com","gender":"Female","weight":58,"dob":"2000-09-02"},
{"first_name":"Bondie","last_name":"Dorbon","email":"bdorbonu@sohu.com","gender":"Male","weight":51,"dob":"2001-09-20"},
{"first_name":"Livy","last_name":"Keatley","email":"lkeatleyv@deliciousdays.com","gender":"Female","weight":58,"dob":"2000-02-01"},
{"first_name":"Winnie","last_name":"Morphew","email":"wmorpheww@nps.gov","gender":"Male","weight":89,"dob":"2000-08-02"},
{"first_name":"Kippy","last_name":"Jannex","email":"kjannexx@smugmug.com","gender":"Male","weight":57,"dob":"1999-01-17"},
{"first_name":"Conan","last_name":"Dykins","email":"cdykinsy@opera.com","gender":"Male","weight":72,"dob":"2002-10-07"},
{"first_name":"Gwyn","last_name":"Bretherick","email":"gbretherickz@mtv.com","gender":"Female","weight":84,"dob":"2002-03-24"},
{"first_name":"Roarke","last_name":"Kiehnlt","email":"rkiehnlt10@weather.com","gender":"Male","weight":71,"dob":"1999-11-22"},
{"first_name":"Lu","last_name":"Coils","email":"lcoils11@ucoz.ru","gender":"Female","weight":55,"dob":"2000-02-23"},
{"first_name":"Anica","last_name":"Donke","email":"adonke12@jugem.jp","gender":"Female","weight":48,"dob":"2002-06-13"},
{"first_name":"Basilius","last_name":"Scoggin","email":"bscoggin13@engadget.com","gender":"Male","weight":80,"dob":"2003-10-12"},
{"first_name":"Denni","last_name":"Studman","email":"dstudman14@studiopress.com","gender":"Female","weight":88,"dob":"2001-08-01"},
{"first_name":"Elana","last_name":"Ronnay","email":"eronnay15@jalbum.net","gender":"Female","weight":77,"dob":"1999-02-18"},
{"first_name":"Wit","last_name":"Guerra","email":"wguerra16@photobucket.com","gender":"Male","weight":82,"dob":"2003-10-25"},
{"first_name":"Kalil","last_name":"Bram","email":"kbram17@gov.uk","gender":"Male","weight":46,"dob":"2000-09-21"},
{"first_name":"Gale","last_name":"Faulder","email":"gfaulder18@adobe.com","gender":"Female","weight":76,"dob":"2000-08-15"},
{"first_name":"Nessy","last_name":"Gentery","email":"ngentery19@msn.com","gender":"Female","weight":91,"dob":"2001-09-26"},
{"first_name":"Sherwood","last_name":"Dudny","email":"sdudny1a@biblegateway.com","gender":"Male","weight":48,"dob":"2003-08-10"},
{"first_name":"Daryle","last_name":"Spini","email":"dspini1b@ca.gov","gender":"Male","weight":76,"dob":"1999-02-01"},
{"first_name":"Dulci","last_name":"Pawelek","email":"dpawelek1c@salon.com","gender":"Female","weight":86,"dob":"1999-11-24"},
{"first_name":"Leonardo","last_name":"Goodbanne","email":"lgoodbanne1d@salon.com","gender":"Male","weight":69,"dob":"1999-09-23"},
{"first_name":"Rozelle","last_name":"O'Dyvoie","email":"rodyvoie1e@moonfruit.com","gender":"Female","weight":86,"dob":"2001-03-03"},
{"first_name":"Meyer","last_name":"Barbrook","email":"mbarbrook1f@bing.com","gender":"Male","weight":58,"dob":"2002-06-25"},
{"first_name":"Isidoro","last_name":"Gilders","email":"igilders1g@upenn.edu","gender":"Male","weight":97,"dob":"2001-03-16"},
{"first_name":"Brook","last_name":"Trevains","email":"btrevains1h@addtoany.com","gender":"Male","weight":50,"dob":"2002-01-13"},
{"first_name":"Rae","last_name":"Phizackarley","email":"rphizackarley1i@pbs.org","gender":"Female","weight":65,"dob":"2001-07-20"},
{"first_name":"Bartholemy","last_name":"Casazza","email":"bcasazza1j@sogou.com","gender":"Male","weight":88,"dob":"2001-06-17"},
{"first_name":"Lonnie","last_name":"Tomeo","email":"ltomeo1k@plala.or.jp","gender":"Male","weight":41,"dob":"2001-11-30"},
{"first_name":"Roch","last_name":"Stonhouse","email":"rstonhouse1l@nbcnews.com","gender":"Female","weight":89,"dob":"1999-10-07"},
{"first_name":"Nap","last_name":"Glazier","email":"nglazier1m@fastcompany.com","gender":"Male","weight":47,"dob":"1999-02-02"},
{"first_name":"Allyson","last_name":"Budgeon","email":"abudgeon1n@ihg.com","gender":"Female","weight":78,"dob":"2004-06-17"},
{"first_name":"Josephine","last_name":"Yardley","email":"jyardley1o@nymag.com","gender":"Female","weight":98,"dob":"2000-07-27"},
{"first_name":"Spenser","last_name":"Mickan","email":"smickan1p@4shared.com","gender":"Male","weight":64,"dob":"2000-07-18"},
{"first_name":"Trey","last_name":"Heigold","email":"theigold1q@jimdo.com","gender":"Male","weight":51,"dob":"2003-07-13"},
{"first_name":"Ilka","last_name":"Heaysman","email":"iheaysman1r@dell.com","gender":"Female","weight":91,"dob":"2004-03-28"},
{"first_name":"Kristel","last_name":"Urian","email":"kurian1s@rakuten.co.jp","gender":"Female","weight":91,"dob":"2004-06-06"},
{"first_name":"Karlotta","last_name":"Gillyett","email":"kgillyett1t@geocities.jp","gender":"Female","weight":46,"dob":"2004-05-28"},
{"first_name":"Harriot","last_name":"Winney","email":"hwinney1u@ucsd.edu","gender":"Female","weight":42,"dob":"1999-12-01"},
{"first_name":"Findley","last_name":"Whithalgh","email":"fwhithalgh1v@ft.com","gender":"Male","weight":80,"dob":"2001-05-16"},
{"first_name":"Melicent","last_name":"Cracie","email":"mcracie1w@fotki.com","gender":"Female","weight":78,"dob":"2003-07-19"},
{"first_name":"Taddeo","last_name":"Tennock","email":"ttennock1x@elpais.com","gender":"Male","weight":93,"dob":"1999-12-27"},
{"first_name":"Haydon","last_name":"Stoffersen","email":"hstoffersen1y@squarespace.com","gender":"Male","weight":86,"dob":"2000-05-02"},
{"first_name":"Sheilah","last_name":"Tulley","email":"stulley1z@amazon.de","gender":"Female","weight":48,"dob":"2001-05-28"},
{"first_name":"Alford","last_name":"Hindsberg","email":"ahindsberg20@163.com","gender":"Male","weight":63,"dob":"2004-04-03"},
{"first_name":"Lurline","last_name":"Willmott","email":"lwillmott21@etsy.com","gender":"Female","weight":45,"dob":"2003-07-31"},
{"first_name":"Billy","last_name":"Fogg","email":"bfogg22@pcworld.com","gender":"Male","weight":71,"dob":"2003-10-15"},
{"first_name":"Catrina","last_name":"Mathewson","email":"cmathewson23@devhub.com","gender":"Female","weight":44,"dob":"1999-11-19"},
{"first_name":"Brady","last_name":"Winters","email":"bwinters24@latimes.com","gender":"Male","weight":57,"dob":"2003-10-23"},
{"first_name":"Ruthy","last_name":"Bollans","email":"rbollans25@hao123.com","gender":"Female","weight":86,"dob":"2004-09-09"},
{"first_name":"Andree","last_name":"Bentall","email":"abentall26@vimeo.com","gender":"Female","weight":61,"dob":"1999-04-08"},
{"first_name":"Ruddie","last_name":"Eagle","email":"reagle27@microsoft.com","gender":"Male","weight":92,"dob":"2004-01-28"},
{"first_name":"Phillis","last_name":"Olander","email":"polander28@t-online.de","gender":"Female","weight":61,"dob":"2003-01-07"},
{"first_name":"Frank","last_name":"Wimbury","email":"fwimbury29@dailymail.co.uk","gender":"Male","weight":69,"dob":"2000-11-18"},
{"first_name":"Dame","last_name":"Constantine","email":"dconstantine2a@taobao.com","gender":"Male","weight":92,"dob":"2003-06-09"},
{"first_name":"Matthiew","last_name":"Orrett","email":"morrett2b@instagram.com","gender":"Male","weight":87,"dob":"2003-10-17"},
{"first_name":"Jade","last_name":"Deakes","email":"jdeakes2c@tripadvisor.com","gender":"Female","weight":54,"dob":"2000-11-04"},
{"first_name":"Lanita","last_name":"Climpson","email":"lclimpson2d@1688.com","gender":"Female","weight":91,"dob":"1999-04-07"},
{"first_name":"Etheline","last_name":"Foulstone","email":"efoulstone2e@tripod.com","gender":"Female","weight":87,"dob":"2000-01-03"},
{"first_name":"Arlyne","last_name":"Bickardike","email":"abickardike2f@nifty.com","gender":"Female","weight":73,"dob":"2002-06-04"},
{"first_name":"Ruprecht","last_name":"Siman","email":"rsiman2g@utexas.edu","gender":"Male","weight":41,"dob":"2000-12-21"},
{"first_name":"Lucita","last_name":"Pickston","email":"lpickston2h@behance.net","gender":"Female","weight":75,"dob":"2003-12-04"},
{"first_name":"Aila","last_name":"Tredwell","email":"atredwell2i@infoseek.co.jp","gender":"Female","weight":67,"dob":"2000-01-25"},
{"first_name":"Alisun","last_name":"Bortolozzi","email":"abortolozzi2j@tamu.edu","gender":"Female","weight":55,"dob":"2004-09-08"},
{"first_name":"Thaddus","last_name":"Burnard","email":"tburnard2k@google.fr","gender":"Male","weight":75,"dob":"2000-07-22"},
{"first_name":"Heath","last_name":"Lakeman","email":"hlakeman2l@macromedia.com","gender":"Female","weight":56,"dob":"2001-04-21"},
{"first_name":"Wash","last_name":"Piotr","email":"wpiotr2m@free.fr","gender":"Male","weight":44,"dob":"2000-08-06"},
{"first_name":"Carlin","last_name":"Kidney","email":"ckidney2n@walmart.com","gender":"Female","weight":58,"dob":"2002-10-19"},
{"first_name":"Claretta","last_name":"Barthram","email":"cbarthram2o@tuttocitta.it","gender":"Female","weight":71,"dob":"1999-01-29"},
{"first_name":"Maud","last_name":"Marquese","email":"mmarquese2p@mediafire.com","gender":"Female","weight":43,"dob":"2004-11-01"},
{"first_name":"Bucky","last_name":"Warcup","email":"bwarcup2q@lulu.com","gender":"Male","weight":40,"dob":"2003-07-23"},
{"first_name":"Chas","last_name":"Moulding","email":"cmoulding2r@dyndns.org","gender":"Male","weight":52,"dob":"2001-12-13"}]
        for c in customers:
            customer = Customer(**c)
            customer.save()

        self.stdout.write(
            self.style.SUCCESS('Successfully populated customers')
        )


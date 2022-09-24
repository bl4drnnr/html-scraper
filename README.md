```
 _   _ ________  ___ _          _____ _____ ______  ___  ______ ___________ 
| | | |_   _|  \/  || |        /  ___/  __ \| ___ \/ _ \ | ___ \  ___| ___ \
| |_| | | | | .  . || |  ______\ `--.| /  \/| |_/ / /_\ \| |_/ / |__ | |_/ /
|  _  | | | | |\/| || | |______|`--. \ |    |    /|  _  ||  __/|  __||    / 
| | | | | | | |  | || |____    /\__/ / \__/\| |\ \| | | || |   | |___| |\ \ 
\_| |_/ \_/ \_|  |_/\_____/    \____/ \____/\_| \_\_| |_/\_|   \____/\_| \_|
```

**HTML-Scraper** - is simple `Python` shell script that allows user to scrap `HTML` page and extract data.

Script also allows to provide cookie or headers if needed (for authorization, for example).

For data, that is placed on *pages* script allows to set pagination and extract data from pages.

### Documentation
```
-h, --help      Print documentation manual.
-u, --url       Pass URL of page of page to scrap. Example: -u https://example.com or --url=https://example.com
-o, --output    Write result in file.
```

Extracted data can be written down to file and saved on disk.

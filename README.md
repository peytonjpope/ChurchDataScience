# US Churches: Data Science

### About
- **Goal:** Create a map of the US distribution of churches by denomination
- **Skills:** Web-scraping, dataset manipulation and data visualization
- **Resource:** *Learn to Code with Basketball* by Nathan Braun

### Steps

1. **Web Scraping ([webscraper.py](https://github.com/peytonjpope/ChurchDataScience/blob/main/webscraper.py))**
   - Scraped church data from ExpertGPS for all 48 contiguous US states
   - Extracted church names, latitude, and longitude coordinates from HTML links
   - Used BeautifulSoup and requests libraries to parse web content
   - Implemented denomination classification based on church name keywords

2. **Data Processing ([webscraper.py](https://github.com/peytonjpope/ChurchDataScience/blob/main/webscraper.py))**
   - Combined data from all states into a single DataFrame
   - Cleaned and converted coordinate data to float format
   - Categorized churches into 11 denominations
   - Exported final dataset to ([churches.csv](https://github.com/peytonjpope/ChurchDataScience/blob/main/churches.csv))**

3. **Data Visualization ([graphs.py](https://github.com/peytonjpope/ChurchDataScience/blob/main/graphs.py))**
   - Created scatter plots showing geographic distribution of all churches and by denomination
   - Generated density contour maps to visualize concentration patterns
   - Used custom color palette for denomination differentiation
   - Produced both aggregate and denomination-specific visualizations

## Results

### Scatter Plot Visualizations
- ![All Churches Overview](graphs/dotmapAll.png) - Overview of all churches across the continental US
- ![Baptist Churches](graphs/dotmapBaptist.png) - Baptist denomination distribution
- ![Methodist Churches](graphs/dotmapMethodist.png) - Methodist denomination distribution
- ![Presbyterian Churches](graphs/dotmapPresbyterian.png) - Presbyterian denomination distribution
- ![Episcopal Churches](graphs/dotmapEpiscopal.png) - Episcopal denomination distribution
- ![Catholic Churches](graphs/dotmapCatholic.png) - Catholic denomination distribution
- ![LDS Churches](graphs/dotmapLDS.png) - Latter Day Saints denomination distribution
- ![Lutheran Churches](graphs/dotmapLutheran.png) - Lutheran denomination distribution
- ![Mennonite Churches](graphs/dotmapMennonite.png) - Mennonite denomination distribution
- ![Pentecostal Churches](graphs/dotmapPentecostal.png) - Pentecostal denomination distribution

### Density Map Visualizations  
- ![All Churches Density](graphs/conmapAll.png) - Density heatmap showing church concentration patterns
- ![Baptist Density](graphs/conmapBaptist.png) - Baptist denomination density map
- ![Methodist Density](graphs/conmapMethodist.png) - Methodist denomination density map
- ![Presbyterian Density](graphs/conmapPresbyterian.png) - Presbyterian denomination density map
- ![Episcopal Density](graphs/conmapEpiscopal.png) - Episcopal denomination density map
- ![Catholic Density](graphs/conmapCatholic.png) - Catholic denomination density map
- ![LDS Density](graphs/conmapLDS.png) - Latter Day Saints denomination density map
- ![Lutheran Density](graphs/conmapLutheran.png) - Lutheran denomination density map
- ![Mennonite Density](graphs/conmapMennonite.png) - Mennonite denomination density map
- ![Pentecostal Density](graphs/conmapPentecostal.png) - Pentecostal denomination density map


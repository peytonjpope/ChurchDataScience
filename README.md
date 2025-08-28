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

![All Churches](graphs/dotmapAll.png)  
*All churches*  

---

![Baptist Churches](graphs/dotmapBaptist.png)  
*Baptist churches*  

---

![Methodist Churches](graphs/dotmapMethodist.png)  
*Methodist churches*  

---

![Presbyterian Churches](graphs/dotmapPresbyterian.png)  
*Presbyterian churches*  

---

![Episcopal Churches](graphs/dotmapEpiscopal.png)  
*Episcopal churches*  

---

![Catholic Churches](graphs/dotmapCatholic.png)  
*Catholic churches*  

---

![LDS Churches](graphs/dotmapLDS.png)  
*Latter-Day Saints churches*  

---

![Lutheran Churches](graphs/dotmapLutheran.png)  
*Lutheran churches*  

---

![Mennonite Churches](graphs/dotmapMennonite.png)  
*Mennonite churches*  

---

![Pentecostal Churches](graphs/dotmapPentecostal.png)  
*Pentecostal churches*  

---

### Density Map Visualizations  

![All Churches Density](graphs/conmapAll.png)  
*All churches density*  

---

![Baptist Density](graphs/conmapBaptist.png)  
*Baptist churches density*  

---

![Methodist Density](graphs/conmapMethodist.png)  
*Methodist churches density*  

---

![Presbyterian Density](graphs/conmapPresbyterian.png)  
*Presbyterian churches density*  

---

![Episcopal Density](graphs/conmapEpiscopal.png)  
*Episcopal churches density*  

---

![Catholic Density](graphs/conmapCatholic.png)  
*Catholic churches density*  

---

![LDS Density](graphs/conmapLDS.png)  
*Latter-Day Saints churches density*  

---

![Lutheran Density](graphs/conmapLutheran.png)  
*Lutheran churches density*  

---

![Mennonite Density](graphs/conmapMennonite.png)  
*Mennonite churches density*  

---

![Pentecostal Density](graphs/conmapPentecostal.png)  
*Pentecostal churches density*  

---

<div id="top"></div>

<br />

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#how-it-works">How it works</a></li>
    <li><a href="#reflection">Reflection</a></li>
  </ol>
</details>

## About the project

Dit project is een minimalistische implementatie van een Document Managment System (DMS).
Je maakt binnen de root/markdown map notities aan in markdown, bij het runnen van het project zullen de markdown bestanden dan omgezet worden naar PDF bestanden
Na het converteren zal de root folder ook gepusht worden naar github zodat je bestanden altijd gebackupt zijn!

### Built With

Het project bestaat volledig uit deze technologieën en gebruikt volgende python modules:

* [python3](https://python.org/)
* [rinohtype](https://github.com/brechtm/rinohtype)

## Getting Started

### Prerequisites

Install pip, if not installed yet.

* pip
  1. Change directory to Downloads
  ```sh
  cd Downloads
  ```
  2. Download <a href="https://bootstrap.pypa.io/get-pip.py">pip.py</a> 
     1. Or use wget:
     ```sh
      wget https://bootstrap.pypa.io/get-pip.py      
      ```
      2. Or use Curl:
      ```sh
      curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
      ```
  1. Run install script
  ```sh
  python get-pip.py
  ```

### Installation

1. Clone deze repo
   ```sh
   git clone https://github.com/iniasdb/markdown-DMS
   ```
2. Create virtual environment
   ```sh
   cd markdown-DMS
   ```
   ```sh
   python -m venv venv
   ```
3. Start virtual environment
   ```sh
   cd venv/Scripts
   ```
   ```sh
   activate.bat
   ```
   ```sh
   cd ../../
   ```
4. Install python modules
   ```sh
   pip install -r reqs.txt
   ```
5. Deactive virtual environment (na het runnen van het script)
   ```sh
   deactivate
   ```

## Usage

Het programma kan gestart worden door `app.py` uit te voeren via de cli
   ```sh
   python app.py
   ```

## How it works

1. De root directery wordt geïterreerd
2. Indien er nieuwe mappen in de markdown map zitten, zullen deze ook in de pdf map aangemaakt worden
3. Indien er nieuwe files in de markdown map zitten, zullen deze toegevoegd worden aan een "conversion queue" (md_to_convert[])
4. Alle files worden ook toegevoegd aan een list, hieruit zal de table of contents gemaakt worden
5. De files zullen uit de conversion queue gehaald worden en geconverteerd worden naar PDF formaat
6. Indien ze er nog niet was, zal er een toc.md bestand aangemaakt worden (table of contents)
7. In toc.md zullen alle file uit de list (stap 4) gehaald worden, en ze zullen hierin geschreven worden
8. De toc.md wordt geconverteerd naar PDF
9. Als laatste stap zal de GithubHelper class de code committen en pushen naar github
10. De map wordt geïnitialiseerd via het git init commando, dit zal niets overwriten mocht je het meerdere keren doen
11. Alle veranderingen worden toegevoegd, en er zal een commit gemaakt worden
12. De commit wordt gepusht naar github
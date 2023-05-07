<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

 <a href="https://github.com/github_username/repo_name">
    <img src="/images/earth.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">TerraIntellect Analytics Infrastructure</h3>

  <p align="center">
    Buisness analytics infrastruture for a fictitious company dedicated to capturing and using data to act on climate. 
    <br />
    <a href="https://github.com/JackDoyleIRE/TerraIntellect "><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JackDoyleIRE/TerraIntellect">View Demo</a>
    ·
    <a href="https://github.com/JackDoyleIRE/TerraIntellect/issues">Report Bug</a>
    ·
    <a href="https://github.com/JackDoyleIRE/TerraIntellect/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
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
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

TerraIntellect is a fictitious company who collects primary environmental data for the fight against climate change. 

This project builds the core buisness data and analytics infrastrucutre to allow TerraIntellect to operate and make impact on climate though its data services. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the app and how to install them (mac only).
* python
  ```sh
  brew install python
  ```

### Installation

2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install anaconada
   ```sh
   brew install anaconda
   ```
4. Build the inital schema via pgAdmin4
5. Fill data tables with
    ```sh
   python /db.insert_data.py
   ```
6. Initalise the dbt project for processing
   ```sh
   dbt init
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

App currently in development.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Create the inital schema in postgres 
    - [ ] Fill the schema with data generated in the python package faker
- [ ] Use dbt to transform the raw buisness data into analytics ready data
    - [ ] Develop reports and analysis for operation
- [ ] Expand the companies schema to include new products, ventures and operations


See the [open issues](https://github.com/JackDoyleIRE/TerraIntellect/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



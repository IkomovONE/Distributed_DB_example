# Data-intensive systems assignment: Demonstration of a distributed database network for online store

**Author**: Daniil Komov

## Project Overview
This repository serves as an example of distributed network of databases for online international store. The repository contains folders with dummy data for each database location and a frontend program which accesses MongoDB to display data based on the location.
## Usage
### Running

To run the program, you will need to install Python, venv and have mongoDB connection, on port 27017. Create 3 databases (Europe, Asia and US), add collections (Users, Sellers, Products and Orders), then add data using file imports from repository folders (EU, Asia, US).

Set virtual environment, install needed libraries (Flask, pymongo) and then run this command:

```bash
flask --app store run
```
Then go to browser and enter URL given in terminal. 

### Locations

You can change the location using the selector on the top of the page. Then by pressing submit the data will change, as it will be gathered from another database.

### Demonstration video

You can access a demo video using this link:

https://www.youtube.com/watch?v=nIhKN3gcMi0

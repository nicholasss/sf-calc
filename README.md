# sf-calc
Tool to help you design your Satisfactory factories as you expand your game.

## LIMITATIONS
- Currently this program only uses a subset of recipes and resources. If you see `KeyError` then you have likely found one of the missing items.
- Currently this program utilizes a local JSON store of data. In order to add more data, there must be additional research, validation, etc.
- Currently this program does not make use of the `-c`/`--count` feature due to walls hit when implementing. It will only show and add each of the recipes required inputs instead of calculating how many are really needed at the end. 

## Original Scope and Final Scope
Originally, the scope included:
1. Data stored in TOML format instead of JSON.
2. Partially implemented TOML parser to load data from files.
3. Pointing to a TOML request document to output requirements.
4. Calculated ratios to enable the use of the `-c`/`--count` argument.

I found that I did not understand the TOML format as I implemented it, and decided to use JSON as it is intended as a data transfer format. Whereas TOML is intended for configurations. I believed that implementing even a partial parser from scratch would take a good portion of project implemention and that it would make for a good seperate project. Implementing loading requested recipes from file would require a large amount of refactoring or implemeting completely seperate logic. I thought this would increase the time needed to implement too much for my current knowledge and skills. Similarly, I found that in order to implement the count of the recipe to require quite a lot of refactoring of the RecipeNode/RecipeTree implemetation I had moved to.

**Final Scope**
This project, although conceived as a multifunction CLI tool, ended up being a single function CLI tool. It is useful for one thing, which is looking up a specific recipe and viewing its raw inputs required, intermediate products, as well as the machines required and the max potential power requirements.
It can still help in planning by helping the player to plan the size of various sub-factories or floors in a larger building. This can prove useful as it can alleviate some trips to the Satisfactory wiki. 

## How to Use
This tool does not require any external modules and so can run with the standard Python 3.12+ install.

Simply call the tool with the following syntax in order to receive the recipes requirements:
```bash
python3 ./source/sf_calc.py "reinforced iron plate"
python3 ./source/sf_calc.py screw
```

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

## Future Todo's
1. Refactor and fully implement the ability to request a specific amount of a material.
2. Calculate average power use utilizing machine effeciency calculations.
3. Implement argument to alphabetically sort the output of listing and calculations.

## How to Use
This tool does not require any external modules and so can run with the standard Python 3.12+ install. Simply clone it to whatever directory you would like.

#### --list or -l
You can list available recipes with the following syntax:
```
python3 ./source/sf_calc.py --list
-Iron Plate              made in Constructor
-Iron Ingot              made in Smelter
-Iron Rod                made in Constructor
-Screw                   made in Constructor
-Copper Ingot            made in Smelter
-Aluminum Ingot          made in Foundry
-Aluminum Scrap          made in Refinery
-Alumina Solution        made in Refinery
-Silica                  made in Constructor
-Wire                    made in Constructor
-Cable                   made in Constructor
-Copper Sheet            made in Constructor
-Reinforced Iron Plate   made in Assembler
-Modular Frame           made in Assembler
-Rotor                   made in Assembler
```
#### Calculating
*Note that material names with multiple words should be placed in quotation marks.*

You can find a particular materials requirements with the following syntax:
```
python3 ./source/sf_calc.py "reinforced iron plate"

Requested Recipes:
5 Reinforced Iron Plate per min

Raw Materials Needed:
60.0 of Iron Ore per min

Intermediate Materials to Produce:
60.0 of Screw per min
10.0 of Iron Rod per min
45.0 of Iron Ingot per min
30.0 of Iron Plate per min

Machines Needed For Production:
3.0 of Constructor per min
2.0 of Smelter per min
2.0 of Miner per min
1.0 of Assembler

Maximum Power Required: 45MW
```
Here is an additional example with the Screw:
```
python3 ./source/sf_calc.py screw

Requested Recipes:
40 Screw per min

Raw Materials Needed:
30.0 of Iron Ore per min

Intermediate Materials to Produce:
10.0 of Iron Rod per min
15.0 of Iron Ingot per min

Machines Needed For Production:
2.0 of Constructor per min
1.0 of Smelter per min
1.0 of Miner

Maximum Power Required: 17MW
```

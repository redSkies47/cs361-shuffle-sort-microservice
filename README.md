# cs361-shuffle-sort-microservice

## Overview

The Shuffle + Sort Microservice was created by redSkies47 and is written in Python. This microservice aims to provide shuffle and sort functionality to a Music Playlist Maker. It was created for exploring microservices in CS 361 - Software Engineering I. 

## Getting started

#### Step 1
Install [Python](https://www.python.org/downloads/).

#### Step 2
Either use `git clone https://github.com/redSkies47/cs361-shuffle-sort-microservice.git` on the command line to clone the repository or Code --> Download zip button to get the files.

#### Step 3
Both the Shuffle + Sort Microservice and the Music Playlist Maker need to access the same input and output files. In `microservice.py`:
* Update the input text file variable `input_playlist` with the appropriate relative path of the Music Playlist Maker's `songs.txt` file.
From the Music Playlist Maker:
* Update to read and write to the `output` file.

#### Step 4
Run `microservice.py`.

## How to Request data
To request data from the microservice:
* For **shuffling** a playlist, the Music Playlist Maker needs to write `shuffle` in the `output` file.
* For **sorting** a playlist alphabetically, the Music Playlist Maker needs to write `sort` in the `output` file.

#### Example Call
Inside the `order.txt` file:
```
sort
```

## How to Receive data
To receive data from the microservice:
1. The Music Playlist Maker needs to read from the `output` file.

The data in the `output` file is organized as 1 song per line. Each song includes information as
```
Song;Artist;Minute;Seconds;Album
```
And a sample entry is:
```
Africa;Toto;4;45;Toto IV
```

## UML Sequence Diagram

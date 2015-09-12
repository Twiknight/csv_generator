# csv_generator
a simple python tool that helps generate csv files from a json file

#how to use it
1. Download `csv_generator.py` and place it in a directory prepared for your csv files.
2. Download `example.json` and place it in the same directory.
3. edit the `example.json` to meet your requirements.
4. open cmd in this directory, and run:  
      <code>python csv_generator.py example.json</code>

#environments required
Python version: [v 3.4.3](https://www.python.org/downloads/)

#what's in `example.json`
In fact, `example.json` is a list of json objects. Each json object represents a csv file you want generate.

The object must contain following attributes:
- `title`: the title of the csv file, this should be a string. Remeber not to add `'.csv'` to the end.
- `length`: the lenght of each line.
- `lines`: a list of objects each represents the content of a line.

#example
If you have an `example.json` like this

    [{
      "title":"test1",  
      "length":10,  
      "lines":[  
        {"0":"00000001","1":"00000002","2":"name","5":"hello"},  
        {"0":"00000001","1":"00000003","2":"name","5":"hello"},  
        {"0":"00000001","1":"00000004","2":"name","5":"hello"}  
      ]  
    }]
    
You will get the following content:

    "00000001","00000002","name","","","hello","","","",""
    "00000001","00000003","name","","","hello","","","",""
    "00000001","00000004","name","","","hello","","","",""

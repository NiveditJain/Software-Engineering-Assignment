# Software Engineering Assignment (Unit Testing) (Request Reciept Processing Use Case)
This Repository contains my Solution of Software Engineering Assignment By Dr. Suman Kundu (IIT Jodhpur)

## Assumptions
1 - An api is already made which will provide the data in json format to generate recipt. <br>
2 - API supports GET request (we have hosted a temperary json file at https://niveditjain.github.io/reciept/10010010.json)

## Output 
On the basic of Data Provided by json object fetched from API a reciept is generated as PDF file with a name "reciept_<reciept_number>.pdf"

###### NOTE : For better clarity of use case, SRS Document is also uploaded to Repository!


## Running the Code
Use case is written in the file - reciept_generate.py <br><br>
To run the use case use the following command after successful installation of Python3 <br>
### Mac/Linux
`python3 reciept_generate.py`
### Windows
`python reciept_generate.py`
<br>

## Running the Test Cases
Test cases are written in file - test.py <br><br>
To run the test cases us the following commands after successful installation of Python3 <br>
### Mac/Linux
`python3 test.py`
### Windows
`python test.py`


###### Note : You might also need to install the following Python3 liabraries(if not already installed) Requests, Json and PIL

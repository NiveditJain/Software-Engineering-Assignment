from reciept_generate import GenerateReciept
import unittest
import os


# testing class
class TestGenerateReciept(unittest.TestCase):


    # checking reciept number must be same in json 
    # object fetched and requested number
    def test_reciept_number(self):
        reciept=GenerateReciept("10010010")
        self.assertEqual(reciept.response["reciept_number"],"10010010")



    # testing that no json object is empty
    def test_no_empty(self):
        reciept=GenerateReciept("10010010")
        self.assertNotEqual("",reciept.response["reciept_number"])
        self.assertNotEqual("",reciept.response["name"])
        self.assertNotEqual("",reciept.response["designation"])
        self.assertNotEqual("",reciept.response["id"])
        self.assertNotEqual("",reciept.response["status"])
        self.assertNotEqual("",reciept.response["requested"])
        self.assertNotEqual("",reciept.response["paid"])
        self.assertNotEqual("",reciept.response["currency"])
        self.assertNotEqual("",reciept.response["balance left"])
        self.assertNotEqual("",reciept.response["signatures"])




    # must have only 10 keys
    def test_number_of_keys(self):
        reciept=GenerateReciept("10010010")
        self.assertEqual(10,len(reciept.response))




    # check that designation must among some
    def test_designation(self):
        reciept=GenerateReciept("10010010")
        allowed_designations=["Student","Professor","Assistant Professor",
        "Associate Professor","Director","Associate Dean","Dean"
        ]
        self.assertIn(reciept.response["designation"],allowed_designations)



    # test if file is successfully generated
    def test_reciept_generation(self):
        reciept=GenerateReciept("10010010")

        if os.path.exists("reciept_10010010.pdf"):
            os.remove("reciept_10010010.pdf")

        reciept.export()        
        self.assertIn("reciept_10010010.pdf",os.listdir())

        if os.path.exists("reciept_10010010.pdf"):
            os.remove("reciept_10010010.pdf")



    # status must be among some
    def test_status(self):
        reciept=GenerateReciept("10010010")
        allowed_status=["Approved","Requested","Settled"]
        self.assertIn(reciept.response["status"],allowed_status)



    # requested must be less than 1.5 core
    def test_requested(self):
        reciept=GenerateReciept("10010010")
        self.assertGreaterEqual(int(reciept.response["requested"]),0)
        self.assertLessEqual(int(reciept.response["requested"]),15000000)



    #paid must be less than equal 90% of requested
    def test_paid(self):
        reciept=GenerateReciept("10010010")
        self.assertLessEqual(int(reciept.response["paid"]),0.9*int(reciept.response["requested"]))

           

    # only some currencies are allowed
    def  test_currency(self):
        reciept=GenerateReciept("10010010")
        allowed_currcies=["INR","USD"]
        self.assertIn(reciept.response["currency"],allowed_currcies)



    # balance left
    def test_balance_left(self):
        reciept=GenerateReciept("10010010")

        if(reciept.response["status"]!="Settled"):
            self.assertGreaterEqual(int(reciept.response["balance left"]),0.9*int(reciept.response["requested"]))
        else:
            self.assertGreaterEqual(int(reciept.response["balance left"]),0)




    # only few people can sign
    def test_signatures(self):
        reciept=GenerateReciept("10010010")
        allowed_signatures=["Director","Dean"]
        self.assertIn(reciept.response["signatures"],allowed_signatures)



    # name must not contain any number
    def test_name(self):
        reciept=GenerateReciept("10010010")
        numbers=sum(char.isdigit() for char  in reciept.response["name"])
        self.assertEqual(0,numbers)

    

# test case runner
if __name__ == '__main__':
    unittest.main()
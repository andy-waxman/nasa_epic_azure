import unittest
import json
import azure.functions as func
from GetAndResizeImage import main

# More an integration test using demo_key since really making http call.
class TestMainFunction(unittest.TestCase):

    def test_main_basetest(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        # base test, no adjust

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/bmp", resp.mimetype)
 
    def test_main_missing_identifier_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)
        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)
        
    def test_main_invalid_length_identifier_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        identifier = "20151031";
        content = { "identifier":identifier,"api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)
        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_invalid_date_identifier_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        identifier = "20151035174844";
        content = { "identifier":identifier,"api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)
        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_missing_api_key_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)
        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_format_enhanced(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "format":"enhanced" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/bmp", resp.mimetype)    

    def test_main_format_natural(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "format":"natural" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/bmp", resp.mimetype) 

    def test_main_format_invalid_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "format":"invalid" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)


    def test_main_output_bmp(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "output":"bmp" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/bmp", resp.mimetype)

    def test_main_output_png(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "output":"png" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/png", resp.mimetype)              

    def test_main_output_jpeg(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "output":"jpeg" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/jpeg", resp.mimetype)    

    def test_main_output_invalid_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "output":"invalid" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_width_200_as_string(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "width":"200" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/bmp", resp.mimetype)

    def test_main_width_200_as_int(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "width":200 }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/bmp", resp.mimetype)

    def test_main_width_too_small_as_string_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "width":"100" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_width_too_small_as_int_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "width":100 }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_width_too_large_as_string_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "width":"2200" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_width_too_large_as_int_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "width":2200 }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_width_not_a_number_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "width":"abc" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_height_200_as_string(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "height":"200" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/bmp", resp.mimetype)

    def test_main_height_200_as_int(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "height":200 }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(200, resp.status_code)
        self.assertEqual("image/bmp", resp.mimetype)

    def test_main_height_too_small_as_string_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "height":"100" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_height_too_small_as_int_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "height":100 }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_height_too_large_as_string_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "height":"2200" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)

    def test_main_height_too_large_as_int_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "height":2200 }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)   

    def test_main_height_not_a_number_returns_400(self):
        
        # Arrange
        identifier = "20151031074844";
        api_key = "DEMO_KEY"; # using this value as an api key is limited to 30 calls an hour
        content = { "identifier":identifier, "api_key":api_key }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Adjust
        content = { "identifier":identifier, "api_key":api_key, "height":"abc" }
        json_content = json.dumps(content).encode("utf-8")
        req = func.HttpRequest(method="POST", url="/GetAndResizeImage", body=json_content)

        # Act
        resp = main(req)

        # Assert
        self.assertEqual(400, resp.status_code)             
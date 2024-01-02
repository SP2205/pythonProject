

import requests
def main():

      response_body=  requests.get("https://restful-booker.herokuapp.com/booking/1")
      print(response_body.text)
      print(response_body.status_code)





if __name__ ==  "__main__":
        main()


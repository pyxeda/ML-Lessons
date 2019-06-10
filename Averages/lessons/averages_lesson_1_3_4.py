import requests
import json as json
import numpy as np

#calculate and print out the prediction
def get_prediction(data={"A":48,"B":23,"C":38,"D":54}):
    # data = data.encode('utf-8')
    url = 'https://jzsbkydi4g.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    decoded_response = json.loads(response) #convert string response to python

    if "dummy response" in response:
        response = "based on the null model, we think the average is 472!"
    elif "error" in response:
        response = "..hmm..looks like we couldn't predict, please only enter numbers."
    else:
        decoded_second = json.loads(decoded_response['body']) #converting body string response to python
        response = decoded_second["predicted_label"]

    print(response)  
    return response


if __name__ == "__main__":

    #getting player input 
    play = "yes"
    print("Hello! Today we are going to try to compute the average of four numbers with Machine Learning!")
    name = input("What is your name? ")
    type(name)
    print("Nice to meet you " + name + "!")
    
    while play == "yes":
        first = input("Please enter your first number(between 0-1000): ")
        type(first)
        second = input("Please enter your second number(between 0-1000): ")
        type(second)
        third = input("Please enter your third number(between 0-1000): ")
        type(third)
        fourth = input("Please enter your fourth number(between 0-1000): ")
        type(fourth)
        #pass in the data
        data = {"A": first, "B": second,"C": third, "D": fourth}
        print("Hey " + name + ", we think the average of the numbers you gave is...")
        get_prediction(data)
        play = input("Thank you for playing! Want to try again? (yes/no) ")
        type(play)
    print("Thanks for playing. Have a great day!")







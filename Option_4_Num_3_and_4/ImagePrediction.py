# -*- coding: utf-8 -*-
'''

Super Project Group 5

Daniel Molar Hurtado

Nicholas Hayes

Rebeca Lopez Valerio

EE104 Super Project Option 4

'''
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time 


def load_image(filename):
    FinalImage = load_img(filename, target_size=(32, 32))
    
    FinalImage = img_to_array(FinalImage)
    
    FinalImage = FinalImage.reshape(1, 32, 32, 3)
    
    FinalImage = FinalImage.astype('float32')
    
    FinalImage = FinalImage / 255.0
    
    return FinalImage


def Prediction(): 
    
    while(True):
        
        Choice=input('There are 10 Categories to choose from:\nAirplane\nAutomobile\nBird\nCat\nDeer\nDog\nFrog\nHorse\nShip\nTruck\n\nWhich Category Would You Like To View (Write Category Name Here): ')     
        
        NewChoice=Choice.lower()
        
        if Choice.isdigit():
            
            print("\nInvalid Input\n")
        
        elif (NewChoice != "airplane" and NewChoice != 'automobile' and NewChoice != 'bird' and NewChoice != 'cat' and NewChoice != 'deer' and NewChoice != 'dog' and NewChoice != 'frog' and NewChoice != 'horse' and NewChoice != 'ship' and NewChoice != 'truck'):
    
            print('\nInvalid Input\n')
      
        else:
        
            PictureSelect=input("Please select the number picture you would like to test (1 or 2): ")
    
            if PictureSelect.isdigit():
        
                Select=int(PictureSelect)
               
                if Select in range (1,3):
                
                    break
                
                else:
                
                    print("invalid input")
            
            else:
            
                print('\nInvalid Input\n') 
    
    print('\n')
   
    PictureSelect=int(PictureSelect)
   
    Choice=str(Choice)     
    
    NewChoice=Choice.lower()
    
    if (NewChoice=='airplane' and PictureSelect==1):
        
        ChosenImage='1stAirplaneConverted'
    
    if (NewChoice=='airplane' and PictureSelect==2):
        
        ChosenImage='2ndAirplaneConverted'    
    
    if (NewChoice=='automobile' and PictureSelect==1):
        
        ChosenImage='1stAutomobileConverted'
    
    if (NewChoice=='automobile' and PictureSelect==2):
        
        ChosenImage='2ndAutomobileConverted'           
    
    if (NewChoice=='bird' and PictureSelect==1):
        
        ChosenImage='1stBirdConverted'
    
    if (NewChoice=='bird' and PictureSelect==2):
        
        ChosenImage='2ndBirdConverted'    
    
    if (NewChoice=='cat' and PictureSelect==1):
        
        ChosenImage='1stCatConverted'
    
    if (NewChoice=='cat' and PictureSelect==2):
        
        ChosenImage='2ndCatConverted'
    
    if (NewChoice=='deer' and PictureSelect==1):
        
        ChosenImage='1stDeerConverted'
    
    if (NewChoice=='deer' and PictureSelect==2):
        
        ChosenImage='2ndDeerConverted'    
    
    if (NewChoice=='dog' and PictureSelect==1):
        
        ChosenImage='1stDogConverted'
    
    if (NewChoice=='dog' and PictureSelect==2):
        
        ChosenImage='2ndDogConverted'           
    
    if (NewChoice=='frog' and PictureSelect==1):
        
        ChosenImage='1stFrogConverted'
    
    if (NewChoice=='frog' and PictureSelect==2):
        
        ChosenImage='2ndFrogConverted'    
    
    if (NewChoice=='horse' and PictureSelect==1):
        
        ChosenImage='1stHorseConverted'
    
    if (NewChoice=='horse' and PictureSelect==2):
        
        ChosenImage='2ndHorseConverted'
    
    if (NewChoice=='ship' and PictureSelect==1):
        
        ChosenImage='1stShipConverted'
    
    if (NewChoice=='ship' and PictureSelect==2):
        
        ChosenImage='2ndShipConverted'    
    
    if (NewChoice=='truck' and PictureSelect==1):
    
        ChosenImage='1stTruckConverted'
    
    if (NewChoice=='truck' and PictureSelect==2):
        
        ChosenImage='2ndTruckConverted'         
    
    FinalImage = load_image(ChosenImage+'.png')
    
    PredictionModel = load_model('Final.h5')
   
    plt.imshow(mpimg.imread(ChosenImage+'.png'))

    time.sleep(2)

    print("\nStatistics of Prediction Model:\n")
   
    print("Airplane:",round((PredictionModel.predict(FinalImage)*100)[0][0],2),'%')
    
    print("Automobile:",round((PredictionModel.predict(FinalImage)*100)[0][1],2),'%')
    
    print("Bird:",round((PredictionModel.predict(FinalImage)*100)[0][2],2),'%')
    
    print("Cat:",round((PredictionModel.predict(FinalImage)*100)[0][3],2),'%')
    
    print("Deer:",round((PredictionModel.predict(FinalImage)*100)[0][4],2),'%')
    
    print("Dog:",round((PredictionModel.predict(FinalImage)*100)[0][5],2),'%')
    
    print("Frog:",round((PredictionModel.predict(FinalImage)*100)[0][6],2),'%')
    
    print("Horse:",round((PredictionModel.predict(FinalImage)*100)[0][7],2),'%')
    
    print("Ship:",round((PredictionModel.predict(FinalImage)*100)[0][8],2),'%')
    
    print("Truck:",round((PredictionModel.predict(FinalImage)*100)[0][9],2),'%')

while(True):
    
    Prediction()
  
    plt.show(block=True)
    
    termination = input("Type 'terminate' to end the program, else enter anything else to continue: ")
    
    if (termination.lower() == 'terminate'):
        
        break
    
    else:
        
        print("\nYou have chosen to continue the program!")
        
        

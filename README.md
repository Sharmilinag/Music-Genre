***********************************************************************************

Automatic and quick detection of the genre of audio/music files.

***********************************************************************************
1. Setup & Configuration

All the configuraton can be done using the ```config.cfg``` file. 

This file contains three variables that the user can modify as per his need. Comments begin with a ```#``` symbol and run till the end of a line.

The variables are:
* ```GENRE_DIR``` - This is directory where the music dataset is located (GTZAN dataset) 
* ```TEST_DIR``` - This is the directory where the test music is located
* ```GENRE_LIST``` - This is a list of the available genre types that you can use. 

2.The Dataset

The dataset used for training the model is the GTZAN dataset. A brief of the data set: 

* The dataset consists of 1000 audio tracks each 30 seconds long. It contains 10 genres, each represented by 100 tracks. The tracks are all 22050Hz Mono 16-bit audio files in .wav format.
* Download link: [Download the GTZAN genre collection](http://opihi.cs.uvic.ca/sound/genres.tar.gz)
* Download size: Approximately 1.2GB

Since the files in the dataset are in the ```au``` format, which is lossy because of compression, they need to be converted in the ```wav``` format (which is lossless) before we proceed further.

3. Model Generation & Caching

Now, the script ```cepsgen.py``` has to be run to analyzes and converts each file in the GTZAN dataset in a representation that can be used by the classifier and can be easily cached onto the disk. This little step prevents the classifier to convert the dataset each time the system is run. 

The GTZAN dataset is used for training the classifier, which generates an in-memory regression model. This process is done by the ```LogisticRegression``` module of the scikit-learn library. The ```classifier.py``` script has been provided for this purpose. Once the model has been generated, we can use it to predict genres of other audio files. For effecient further use of the generated model, it is permanently serialized to the disk, and is deserialized when it needs to be used again. This simple process improves performance greatly. For serialization, the ```joblib``` module in the ```sklearn.externals``` package is used.

As of now, the ```classifiermodel.py``` script must be run before any testing with unknown music can be done. Once the script is run, it will save the generated model at this path: ```./saved_model/model_ceps.pkl```. Once the model has been sucessfully saved, the classification script need not be run again until some newly labelled training data is available. 

4. Testing and Live Usage

The ```tester.py``` script is used for the classification of new and unlabelled audio files. This script deserializes the previously cached model (stored at the path: ```./saved_model/model_ceps.pkl```) and uses it for classifying new audio files. 

5. Interpreting the Output

When the ```classifiermodel.py``` script is run, it generates and saves the trained model to the disk. This process also results in the creation of some graphs(ROC curves and confusion matrix) which are stored in the ```/graphs``` directory. The genereated graphs tell the performance of the classification process.

6. Internal Details

Spectrograms: Proof of Concept

It is clearly analyzed from the spectrograms image that songs belonging to the same genre have similar spectrograms. Keeping this in mind, we can easily design a classifier that can learn to differentiate between the different genres with sufficient accuracy.

Improved Performance by using MFCC

MFCC = Mel Frequency Cepstral Coefficients

The Mel Frequency Cepstrum (MFC) encodes the power spectrum of a sound. It is calculated as the Fourier transform of the logarithm of the signal's spectrum. The Talkbox SciKit (scikits.talkbox) contains an implementation of of MFC that we can directly use. The data that we feed into the classifier is stored as ```ceps```, which contain 13 coeffecients to uniquely represent an audio file. 


#^^^()()^^^




















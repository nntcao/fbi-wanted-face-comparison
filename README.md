# FBI Wanted Face Comparison Application
An API to compare faces to the FBI's Most Wanted Criminals. "Finds your wanted doppelganger."

Originally intended to be the internal API server responsible for ML calculations. 
However, processing power required is beyond the scope of my hardware and the accuracy of the results was limited (there are maybe only ~500 wanted criminals in total. The likelihood you find someone that looks similar to you is slim.)

# How to use
Make sure Python 3.9 is installed, and install all the packages in requirements.txt.

Run the updatelist command to update the list of FBI's Most Wanted Criminals. 
Pulls from https://www.fbi.gov/wanted/api and generates a /photo/ directory in the project directory.
```
python manage.py updatelist
```
Then run the getdoppel command to get the face that resembles you the closest. Outputs the name in the command line.
```
python manage.py getdoppel photo_path
```


Example:
```
python manage.py updatelist
python manage.py getdoppel photos/personal/picture.jpg
```

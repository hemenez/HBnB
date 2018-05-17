<img src="https://github.com/jarehec/AirBnB_clone_v3/blob/master/dev/HBTN-hbnb-Final.png" width="160" height=auto />

# HBnB

## Environment

This project has been tested and interpeted on Ubuntu 14.04 LTS using Python3 (v3.4.3)

## Usage

To launch the console application in interactive mode simply run:

```console.py ```

or to use the non-interactive mode run:

```echo "your-command-goes-here" | ./console.py ```

#### Commands usable w/the console

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. followed by its parameters. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

## Tests

If you wish to run at the test for this application all of the test are located
under the **test/** folder and can execute all of them by simply running:

```python3 -m unittest discover tests ```

from the root directory.

## Folder Descriptions

### AirBnB_clone

This is the first installment of the AirBnB clone. It created a command line interface for the clone. With this CLI, you are able to interact with all the different components you may think would be necessary when picking an AirBnB rental (i.e. amenities, cities, states, reviews, etc.).

#### Important files in this folder

| **File** | **Description** |
| -------- | ----------- |
| `base_model` | This file creates an instance of the class BaseModel. It defines all common attributes/methods for other classes. Attributes include: id (string): a string with an uuid when an instance is created, created_at: assigned with the current datetime when an instance is created, updated_at: assigned with the current datetime when an instance is created and it will be updated every time the object gets changed |
| `file_storage` | This file creates an instance of the class FileStorage. It serializes instances to a JSON file and deserializes JSON file to instances. Attributes include: __file_path (private, string): that represents the path to the JSON file, __objects (dictionary): initialized empty, but will store all objects by class name and id. |

### AirBnB_clone_v2

This installment of the AirBnB clone handles database storage and integrates the backend using SQLAlchemy and Flask. 

### AirBnB_clone_v3

This installment of the AirBnB clone begins working with the Flask app and the API. This project uses my codebase for all Holberton students working on teh version. This project handles the routes and HTTP requests that the user may need in order to work with the application.

#### Important folders/files in this folder

| **File** | **Description** |
| -------- | ----------- |
| **api** | Holds everything that creates the API |
| **v1** | Holds the main flask application |
| **views** | Contains all the routes for the `GET` and `POST` requests |

### AirBnB_clone_v4

This installment of the AirBnB clone takes the loading of data from the back end and puts it into the front-end using JavaScript, Jquery, HTML, CSS and Ajax. 

#### Important folders/files in this folder

| **File** | **Description** |
| -------- | ----------- |
| **web_dynamic** | Holds all of the work that serves the application to the user via the front-end |
| **static** | Contains all static information (i.e. styling, images, and JavaScript scripts |
| **scripts** | The JavaScript that handles displaying the page to the user |
| **templates** | Contains all HTML templates |

## Bugs

+ No known bugs at this time.
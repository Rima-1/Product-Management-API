from art import *
import base64


# route to get all movies
@app.route('/arts', methods=['GET'])
def get_art():
    """Function to get all the movies in the database"""
    return jsonify({'Meow Art Gallery': Art.get_all_art()})


# route to get movie by id
@app.route('/arts/<int:id>', methods=['GET'])
def get_art_by_id(id):
    return_value = Art.get_art(id)
    if return_value != 0:
        return jsonify(return_value)
    else:
        response = Response("No art exists with this id in this gallery", 500, mimetype='application/json')
        return response


# route to add new movie
@app.route('/arts', methods=['POST'])
def add_art():
    """Function to add new movie to our database"""
    request_data1 = request.form["title"]  # getting data from client
    request_data2 = request.form["year"]
    request_data3 = request.form["category"]
    request_data4 = request.form["price"]
    request_data5 = request.form["synopsis"]
    imagefile = request.files['imagefile']
    mimetype = imagefile.mimetype
    print(mimetype)
    image_string ="data:"+mimetype+";base64,"+base64.b64encode(imagefile.read()).decode("utf-8")
    #imagefile.save('D:/temp/test_image.jpg')
    #check = Movie.add_movie(request_data["title"], request_data["year"],
                            #request_data["genre"])
    check = Art.add_art(request_data1, request_data2,
                  request_data3, request_data4, request_data5, image_string)
    if check == 1:
        response = Response("New art added in gallery", 201, mimetype='application/json')
    else:
        response = Response("This art already exists in gallery", 500, mimetype='application/json')
    return response


# route to update movie with PUT method
@app.route('/arts/<int:id>', methods=['PUT'])
def update_art(id):
    """Function to edit movie in our database using movie id"""
    request_data = request.get_json()
    art_if_updated = Art.update_art(id, request_data['title'], request_data['year'], request_data['category'])
    if art_if_updated != 0:
        response = Response("Art Updated", status=200, mimetype='application/json')
        return response
    else:
        response = Response("No such art to be updated with this id", status=500, mimetype='application/json')
        return response

# route to delete movie using the DELETE method
@app.route('/arts/<int:id>', methods=['DELETE'])
def remove_art(id):
    """Function to delete movie from our database"""
    check_if_deleted = Art.delete_art(id)
    if check_if_deleted != 0:
        response = Response("Art Deleted", status=200, mimetype='application/json')
        return response
    else:
        response = Response("No art exists with this id", status=500, mimetype='application/json')
        return response


if __name__ == "__main__":
    app.run(port=1234, debug=True)

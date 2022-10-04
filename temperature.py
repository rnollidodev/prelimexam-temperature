from flask import Flask, jsonify, request

app = Flask(__name__)
temperatures = [
    {
        "temp_id" : "1",
        "date" : "October 04, 2022",
        "temperature" : "35.6"
    },


]
#DISPLAY/READ A TEMPERATURE
@app.route('/temperatures', methods=['GET'])
def displayTemperature():
    return jsonify(temperatures)

@app.route('/temperatures/<int:index>', methods=['PUT'])
def editTemperature(index):
   temperatures.update(index)
   return temperatures

#ADD A TEMPERATURE
@app.route('/temperatures', methods=['POST'])
def addTemperature():
    temperature = request.get_json()
    temperatures.append(temperature)
    return{'id': len(temperatures)},200

#DELETE A TEMPERATURE
@app.route('/temperatures/<int:index>', methods=['DELETE'])
def deleteTemperature(index):
    temperatures.pop(index)
    return 'Temperature was successfully deleted', 200

if __name__ == '__main__':

    app.run()
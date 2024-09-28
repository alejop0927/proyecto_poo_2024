from conexion_bd import app, mysql

@app.route('/proyecto_terminado/vistas/templades/meter_datos/datos.html', methods=['POST'])
def upload_audio():
    nombre = request.form['nombre']
    artista = request.form['artista']
    imagen_file = request.files['imagen']
    audio_file = request.files['audio']
    imagen_data = imagen_file.read()
    audio_data = audio_file.read()
    

    cursor = mysql.conexion.cursor()
    cursor.execute("INSERT INTO cancion (artista, imagen, audio, name_cancion, tiempo) VALUES (%s, %s, %s, %s, %s)", 
                   (artista, imagen_data, audio_data, nombre, 0))
    mysql.conexion.commit()
    cursor.close()
    return 'Audio subido exitosamente'


@app.route('/audio/<int:audio_id>')
def get_audio(audio_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name_cancion, audio FROM cancion WHERE idCancion = %s", (audio_id,))
    result = cursor.fetchone()
    cursor.close()
    return send_file(io.BytesIO(result[1]), mimetype='audio/mpeg', as_attachment=False, attachment_filename=result[0])

if __name__ == '__main__':
    app.run(debug=True)


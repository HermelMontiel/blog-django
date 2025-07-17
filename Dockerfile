#1.  Imagen base de Python
FROM python:3.13

#2. Crer el directorio de trabajo
WORKDIR /app

#3. Copiar los archivos del proyecto
COPY . /app

#4. Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#5. Exponer el puerto
EXPOSE 8000

#6. Comando por defecto (levantamiento de app)
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
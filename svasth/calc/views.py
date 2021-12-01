from django.shortcuts import render
# from tensorflow import keras
from django.core.files.storage import FileSystemStorage

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import json
from tensorflow import Graph


with open('imagenet_classes.json', 'r') as f:
    labelInfo = f.read()

labelInfo = json.loads(labelInfo)
init_op = tf.compat.v1.global_variables_initializer()
session = tf.compat.v1.Session()


model = load_model('training_10.h5')
# model_graph = Graph()
# with model_graph.as_default():
# #     tf_session = session.run(init_op)
#     with tf.compat.v1.Session().as_default():
#         model = load_model('training_10.h5')

# Create your views here.
def index(request):
    return render(request, 'index.html')


def checkup(request):
    return render(request, 'Checkup.html')

def result(request):
	# model = keras.models.load_model('training_10.h5')
	if request.method == 'POST':
		# print(request)
		# print(request.POST.dict())
		doc = request.FILES['file'] # returns a dict-like object
		# doc_name = doc['file']
		fs = FileSystemStorage()
		filePathName = fs.save(doc.name, doc)

		filePathName = fs.url(filePathName)
		testimage='./'+filePathName
		img = image.load_img(testimage, target_size=(60, 60))
		x = image.img_to_array(img)
		x=x.reshape(1,60, 60,3)
		predi = model.predict(x)
		print("******************************************************")
		import numpy as np
		# predi = model.predict(testimage)
		print(predi)
		print(np.argmax(predi))
		print("******************************************************")
		Categories = ['BRAIN TUMOR IS DETECTED Yes', 'BRAIN TUMOR IS NOT DETECTED No']
		
		predictedLabel = Categories[np.argmax(predi)]

	
	# ans = "HI"

	return render(request, 'Result.html', {'result': predictedLabel})

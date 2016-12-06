from neuralmodules import NeuralModule
import zipfile
import imp
import json
import shutil
import atexit
import os.path


def loadModule(path):
	if(zipfile.is_zipfile(path)):
	    zf = zipfile.ZipFile(path, 'r')
	    extractDir = 'temp/neuralmodules/' + zf.filename.split(".")[0] + "/"

	    if(True):
		files = zf.namelist()
		if ("manifest.json" not in files):
		    raise IOError("No manifest.json file found in NeuralModule at " + path + "!")
		if("module.py" not in files):
		    raise IOError("No module.py file found in NeuralModule at " + path + "!")
		if ("weights.dat" not in files):
		    print("No weight file found in NeuralModule at " + path + "!")

		for file in files:
		    zf.extract(file, extractDir)
	    else:
		print ("Module was already extracted.")

	    manifestData = None
	    with open(extractDir + "manifest.json") as data_file:
		manifestData = json.load(data_file)
	    if(manifestData is not None):
		moduleName = manifestData["module"]["modulename"]
		if (moduleName == None): raise IOError("No modulename for NeuralModule specified at: " + path)
	    else:
		raise IOError("manifest.json file found in NeuralModule at " + path + " is malformed!")

	    mod = imp.load_source(moduleName, extractDir + "module.py", )
	    modInstance = mod.module()
	    modInstance.weight_path = extractDir + "weights.dat"
	    modInstance.mod_name = moduleName
	    modInstance.initializeModule()
	    return modInstance
	else:
	    raise IOError("NeuralModule file at "+path+" malformed!")

@atexit.register
def cleanup():
	try:
		shutil.rmtree("temp/neuralmodules")
	except:
		print("I: cleanup not needed")

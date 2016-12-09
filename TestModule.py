from NeuralModules import ModuleLoader

mod = ModuleLoader.loadModule("/home/jens/dev/NeuralModuleServer/modules/colorClassification.zip")
print(mod.predictsingle_string("/home/jens/Dropbox/Jensrwin/realset/real_?_30_180.png"))
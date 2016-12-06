from neuralmodules import ModuleLoader

mod = ModuleLoader.loadModule("/home/jens/dev/NeuralModules/LegoModule.zip")
print(mod.predictsingle_string("/home/jens/Desktop/realset/real_?_0_0.png"))
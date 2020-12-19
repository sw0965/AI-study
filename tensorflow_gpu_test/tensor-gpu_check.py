import tensorflow as tf

print('텐서플로 버전 :', tf.__version__)
print('cuda로 빌드 되었나? :', tf.test.is_built_with_cuda())
print('cuda와 같은 gpu로 빌드 되었나? :', tf.test.is_built_with_gpu_support())
print('사용가능한 gpu 출력 :', tf.test.gpu_device_name())
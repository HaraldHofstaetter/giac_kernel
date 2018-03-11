from ipykernel.kernelapp import IPKernelApp
from .kernel import GiacKernel
IPKernelApp.launch_instance(kernel_class=GiacKernel)


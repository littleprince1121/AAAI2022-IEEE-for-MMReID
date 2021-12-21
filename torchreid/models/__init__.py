from __future__ import absolute_import
from torchreid.models.ieee2modalBase import ieee2modalBase
from torchreid.models.mlfn3modal import mlfn3modal
import torch

from torchreid.models.new3modalInteract import new3modalInteract

from .pcb import *
from .mlfn import *
from .mudeep3modal import *
from .hacnn import *
from .osnet import *
from .senet import *
from .mudeep import *
from .mudeep3modal import *
from .nasnet import *
from .resnet import *
from .densenet import *
from .xception import *
from .osnet_ain import *
from .resnetmid import *
from .shufflenet import *
from .squeezenet import *
from .inceptionv4 import *
from .mobilenetv2 import *
from .resnet_ibn_a import *
from .resnet_ibn_b import *
from .shufflenetv2 import *
from .inceptionresnetv2 import *

from .hamnet import *
from .resnet3modal import *
from .pfnet import *

from .ieee3modalPart import *
from .hacnn3modal import *
from .pcb3modal import *
from .osnet3modal import *
from .pfnet3modal import *


__model_factory = {
    'new3modalInteract': new3modalInteract,
    'resnet3modal': resnet3modal,
    'mudeep3modal': mudeep3modal,
    'mlfn3modal': mlfn3modal,
    'ieee3modalPart': ieee3modalPart,
    'hacnn3modal': hacnn3modal,
    'pcb3modal': pcb3modal,
    'osnet3modal': osnet3modal,
    'pfnet3modal': pfnet3modal,
    'hamnet': MainNet,

    # image classification models

    'resnet18': resnet18,
    'resnet34': resnet34,
    'resnet50': resnet50,
    'resnet101': resnet101,
    'resnet152': resnet152,
    'resnext50_32x4d': resnext50_32x4d,
    'resnext101_32x8d': resnext101_32x8d,
    'resnet50_fc512': resnet50_fc512,
    'se_resnet50': se_resnet50,
    'se_resnet50_fc512': se_resnet50_fc512,
    'se_resnet101': se_resnet101,
    'se_resnext50_32x4d': se_resnext50_32x4d,
    'se_resnext101_32x4d': se_resnext101_32x4d,
    'densenet121': densenet121,
    'densenet169': densenet169,
    'densenet201': densenet201,
    'densenet161': densenet161,
    'densenet121_fc512': densenet121_fc512,
    'inceptionresnetv2': inceptionresnetv2,
    'inceptionv4': inceptionv4,
    'xception': xception,
    'resnet50_ibn_a': resnet50_ibn_a,
    'resnet50_ibn_b': resnet50_ibn_b,
    # lightweight models
    'nasnsetmobile': nasnetamobile,
    'mobilenetv2_x1_0': mobilenetv2_x1_0,
    'mobilenetv2_x1_4': mobilenetv2_x1_4,
    'shufflenet': shufflenet,
    'squeezenet1_0': squeezenet1_0,
    'squeezenet1_0_fc512': squeezenet1_0_fc512,
    'squeezenet1_1': squeezenet1_1,
    'shufflenet_v2_x0_5': shufflenet_v2_x0_5,
    'shufflenet_v2_x1_0': shufflenet_v2_x1_0,
    'shufflenet_v2_x1_5': shufflenet_v2_x1_5,
    'shufflenet_v2_x2_0': shufflenet_v2_x2_0,
}


def show_avai_models():
    """Displays available models.

    Examples::
        >>> from torchreid import models
        >>> models.show_avai_models()
    """
    print(list(__model_factory.keys()))


def build_model(
    name, num_classes, loss='softmax', pretrained=True, use_gpu=True
):
    """A function wrapper for building a model.

    Args:
        name (str): model name.
        num_classes (int): number of training identities.
        loss (str, optional): loss function to optimize the model. Currently
            supports "softmax" and "triplet". Default is "softmax".
        pretrained (bool, optional): whether to load ImageNet-pretrained weights.
            Default is True.
        use_gpu (bool, optional): whether to use gpu. Default is True.

    Returns:
        nn.Module

    Examples::
        >>> from torchreid import models
        >>> model = models.build_model('resnet50', 751, loss='softmax')
    """
    avai_models = list(__model_factory.keys())
    if name not in avai_models:
        raise KeyError(
            'Unknown model: {}. Must be one of {}'.format(name, avai_models)
        )
    return __model_factory[name](
        num_classes=num_classes,
        loss=loss,
        pretrained=pretrained,
        use_gpu=use_gpu
    )


import streamlit as st
import torch
import torchvision as tv
from torchvision.models.segmentation import fcn_resnet101,FCN_ResNet101_Weights
from torchvision.utils import draw_segmentation_masks
from torchvision.transforms.functional import to_pil_image
import numpy as np
from PIL import Image




weights = FCN_ResNet101_Weights.COCO_WITH_VOC_LABELS_V1
preprocess_func = weights.transforms(resize_size=None)
categories = FCN_ResNet101_Weights.COCO_WITH_VOC_LABELS_V1.meta["categories"]
class_to_idx = dict(zip(categories, range(len(categories))))

@st.cache_resource
def load_model():
    fcn_resnet = fcn_resnet101(weights=weights)
    fcn_resnet.eval()
    return fcn_resnet

model = load_model()

def make_prediction(processed_img):
    preds = model(processed_img.unsqueeze(dim=0))
    normalized_preds = preds["out"].squeeze().softmax(dim=0)
    masks = normalized_preds > 0.8
    return masks

def add_transparent_alpha_channel(pil_img):
    arr = np.array(pil_img.convert("RGBA"))
    mask = arr[:, :, :3] == (255, 255, 255)
    mask = mask.all(axis=2)
    alpha = np.where(mask, 0,255)
    arr[:, :, -1] = alpha
    transparent_img = Image.fromarray(arr.astype(np.uint8), mode="RGBA")
    return transparent_img

## Dashboard
st.title("Background Removal App/Arka Plan Kaldırma Uygulaması")
st.caption("PyTorch Image Segmentation Model")
upload = st.file_uploader(label="Upload Image Here/Buraya Resim Yükle:", type=["png", "jpg", "jpeg"])
if upload:
    img = Image.open(upload)
    img_tensor = torch.tensor(np.array(img).transpose(2, 0, 1))
    processed_img = preprocess_func(img_tensor)
    masks = make_prediction(processed_img)
    
    img_with_bg_removed =draw_segmentation_masks(img_tensor, masks=masks[class_to_idx["__background__"]], alpha=1.0, colors="white")
    img_with_bg_removed= to_pil_image(img_with_bg_removed)
    img_with_bg_removed = add_transparent_alpha_channel(img_with_bg_removed)

    coll, col2 = st.columns(2, gap="medium")
    with coll:
        st.subheader("Original Image/Gerçek görüntü")
        st.image(img)
    with col2:
        st.subheader("Image without Background/Arka Plansız Görüntü")
        st.image(img_with_bg_removed)
## English
##Background Removal App using PyTorch Image Segmentation Model 

### Overview
This is a simple application built using Streamlit and PyTorch to perform background removal from an uploaded image using a pre-trained image segmentation model (FCN-ResNet101). The app takes an input image, processes it using the segmentation model, and then displays the original image alongside the image with the background removed.

### Prerequisites

Before running the application, you need to have the following installed:

1. Python 3.x
2. Streamlit: You can install it using pip: pip install streamlit
3. PyTorch: You can install it according to your system and requirements from the official PyTorch website.

### Installation
1. Clone this repository or download the app.py file to your local machine.

### Usage

1. Open a terminal or command prompt and navigate to the directory where app.py is located.

2. Run the Streamlit app using the following command:

		streamlit run app.py

3. The app should open in your default web browser.

### How the App Works
1. The app starts by importing the necessary libraries, including Streamlit, Torch, Torchvision, and PIL (Python Imaging Library).

2. The pre-trained model and its weights are loaded. The model used here is FCN-ResNet101, which is a fully convolutional neural network for image segmentation.

3. A function make_prediction() is defined, which takes a processed image tensor and applies the pre-trained model to predict the segmentation masks.

4. The function add_transparent_alpha_channel() is defined, which takes a PIL image, adds an alpha channel to make it transparent, and returns the image.

5. In the Streamlit dashboard, the user is prompted to upload an image.

6. Once the user uploads an image, the app processes it and makes a prediction using the pre-trained model.

7. The original image and the image with the background removed are displayed side by side using Streamlit's st.image() function.

### Important Functions

- **load_model():** Loads the pre-trained FCN-ResNet101 model and sets it to evaluation mode.
- **make_prediction(processed_img):** Uses the pre-trained model to predict segmentation masks for the processed image.
- **add_transparent_alpha_channel(pil_img):** Adds an alpha channel to the PIL image to make it transparent.

### Note
- The background removal process relies on a threshold value of 0.8 for the segmentation masks. You may experiment with this threshold value to achieve better results.

### Acknowledgments
This app is based on PyTorch and Torchvision libraries, which are open-source projects. Credits go to the developers of these libraries and the creators of the FCN-ResNet101 model.

### Disclaimer
This app is meant for educational and demonstration purposes. The quality of background removal may not be perfect for all images, and it is not intended for professional use without further refinement.

## İngilizce
##PyTorch Görüntü Segmentasyon Modelini Kullanan Arka Plan Kaldırma Uygulaması

### Genel Bakış
Bu, önceden eğitilmiş bir görüntü segmentasyon modeli (FCN-ResNet101) kullanılarak yüklenen bir görüntüden arka planı kaldırmak için Streamlit ve PyTorch kullanılarak oluşturulmuş basit bir uygulamadır. Uygulama bir giriş görüntüsü alır, segmentasyon modelini kullanarak işler ve ardından orijinal görüntüyü, arka planı kaldırılmış olarak görüntünün yanında görüntüler.

### Önkoşullar

Uygulamayı çalıştırmadan önce, aşağıdakilerin kurulu olması gerekir:

1. Python 3.x
2. Streamlit: pip kullanarak kurabilirsiniz: pip install streamlit
3. PyTorch: Sisteminize ve gereksinimlerinize göre resmi PyTorch web sitesinden kurabilirsiniz.

### Kurulum
1. Bu depoyu kopyalayın veya app.py dosyasını yerel makinenize indirin.

### Kullanım

1. Bir terminal veya komut istemi açın ve app.py'nin bulunduğu dizine gidin.

2. Aşağıdaki komutu kullanarak Streamlit uygulamasını çalıştırın:

streamlit run app.py

3. Uygulama, varsayılan web tarayıcınızda açılmalıdır.

### Uygulama Nasıl Çalışır?
1. Uygulama, Streamlit, Torch, Torchvision ve PIL (Python Imaging Library) dahil olmak üzere gerekli kitaplıkları içe aktararak başlar.

2. Önceden eğitilmiş model ve ağırlıkları yüklenir. Burada kullanılan model, görüntü bölümleme için tamamen evrişimli bir sinir ağı olan FCN-ResNet101'dir.

3. İşlenmiş bir görüntü tensörünü alan ve segmentasyon maskelerini tahmin etmek için önceden eğitilmiş modeli uygulayan make_prediction() işlevi tanımlanır.

4. Bir PIL görüntüsünü alan, şeffaf hale getirmek için bir alfa kanalı ekleyen ve görüntüyü döndüren add_transparent_alpha_channel() işlevi tanımlanır.

5. Streamlit panosunda, kullanıcıdan bir görüntü yüklemesi istenir.

6. Kullanıcı bir resim yüklediğinde, uygulama onu işler ve önceden eğitilmiş modeli kullanarak bir tahmin yapar.

7. Orijinal görüntü ve arka planı kaldırılmış görüntü, Streamlit'in st.image() işlevi kullanılarak yan yana görüntülenir.

### Önemli İşlevler

- **load_model():** Önceden eğitilmiş FCN-ResNet101 modelini yükler ve onu değerlendirme moduna ayarlar.
- **make_prediction(processed_img):** İşlenen görüntü için segmentasyon maskelerini tahmin etmek için önceden eğitilmiş modeli kullanır.
- **add_transparent_alpha_channel(pil_img):** PIL görüntüsünü şeffaf hale getirmek için bir alfa kanalı ekler.

### Not
- Arka plan kaldırma işlemi, segmentasyon maskeleri için 0,8'lik bir eşik değerine dayanır. Daha iyi sonuçlar elde etmek için bu eşik değerini deneyebilirsiniz.

### Teşekkürler
Bu uygulama, açık kaynaklı projeler olan PyTorch ve Torchvision kitaplıklarına dayanmaktadır. Bu kitaplıkların geliştiricilerine ve FCN-ResNet101 modelinin yaratıcılarına teşekkür ederiz.

### Feragatname
Bu uygulama eğitim ve tanıtım amaçlıdır. Arka plan kaldırmanın kalitesi tüm görüntüler için mükemmel olmayabilir ve daha fazla iyileştirme yapılmadan profesyonel kullanım için tasarlanmamıştır.
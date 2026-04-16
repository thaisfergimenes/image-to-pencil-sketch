# ✏️ Image to Pencil Sketch

Transforma imagens RGB em desenhos estilo lápis utilizando técnicas de processamento de imagem com OpenCV.

---

## 📌 Overview

Este projeto explora um pipeline de processamento de imagem para simular o efeito de sketch, aplicando transformações clássicas como:

- Conversão para escala de cinza  
- Inversão de imagem  
- Suavização com Gaussian Blur  
- Combinação via divisão de pixels  
- Realce de contraste com CLAHE  

---

## 🧠 Pipeline do Projeto

1. Leitura da imagem RGB  
2. Conversão para grayscale  
3. Inversão da imagem  
4. Aplicação de Gaussian Blur  
5. Inversão da imagem borrada  
6. Combinação com a imagem original (dodge blend via divisão)  
7. Realce de contraste adaptativo (CLAHE)  
8. Geração do efeito final de desenho a lápis  

---

## 🖼️ Resultado

![Before and After](images/output/before_after_sketch.png)

---

## ⚙️ Tecnologias Utilizadas

- Python  
- OpenCV  
- NumPy  

---

## 📁 Estrutura do Projeto
```bash
image-to-pencil-sketch/
│
├── images/
│ ├── input/
│ │ └── dog.jpg
│ └── output/
│ ├── pencil_sketch.png
│ └── before_after_sketch.png
│
├── src/
│ └── sketch.py
│
├── requirements.txt
└── README.md
...

---

## 🚀 Como Executar

```bash
pip install -r requirements.txt
python src/sketch.py


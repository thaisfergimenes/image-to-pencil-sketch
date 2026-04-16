import cv2
import os


def convert_to_pencil_sketch(input_path: str, output_path: str) -> None:
    image = cv2.imread(input_path)

    if image is None:
        raise FileNotFoundError(f"Não foi possível abrir a imagem: {input_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (11, 11), 0)
    inverted_blur = 255 - blurred

    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    sketch = clahe.apply(sketch)

    sketch_bgr = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

    cv2.putText(image, "Original", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    cv2.putText(sketch_bgr, "Sketch", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, sketch)

    height = image.shape[0]
    sketch_bgr = cv2.resize(sketch_bgr, (image.shape[1], height))

    comparison = cv2.hconcat([image, sketch_bgr])
    cv2.imwrite("images/output/before_after_sketch.png", comparison)

    cv2.imshow("Comparison", comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    convert_to_pencil_sketch(
        "images/input/dog.jpg",
        "images/output/pencil_sketch.png"
    )
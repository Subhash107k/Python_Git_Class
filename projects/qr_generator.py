import argparse
from pathlib import Path
import qrcode


def generate_qr(text: str, output_path: str, box_size: int = 10, border: int = 4) -> Path:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M, # type: ignore
        box_size=box_size,
        border=border,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output) # type: ignore
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code image from text or a URL")
    parser.add_argument("text", nargs="?", help="The text or URL to encode")
    parser.add_argument("-o", "--output", default="projects/qr_output.png", help="Output image path")
    parser.add_argument("--box-size", type=int, default=10, help="QR box size")
    parser.add_argument("--border", type=int, default=4, help="QR border size")
    args = parser.parse_args()

    text_to_encode = args.text
    if not text_to_encode:
        text_to_encode = input("Enter the text or URL to encode: ").strip()

    output_file = generate_qr(text_to_encode, args.output, box_size=args.box_size, border=args.border)
    print(f"QR code saved to: {output_file}")

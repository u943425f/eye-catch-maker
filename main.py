from PIL import Image, ImageDraw, ImageFont
import os
import ast
from dotenv import load_dotenv


def create_frame(img_size, rgba, frame_margin):
    """
    透過性のあるフレームを作成する

    Args:
        img_size:     画像サイズ
        rgba:         フレームのRGBA
        frame_margin: フレーム高の余白

    Returns:
        frame(Image):           Image型のフレーム
        draw_frame(ImageDraw):  ImageDraw型のフレーム

    """
    frame = Image.new('RGBA', img_size)
    draw_frame = ImageDraw.Draw(frame)
    draw_frame.rectangle(
        [(0, img_size[1] / 3 - frame_margin), (img_size[0], img_size[1] * 2 / 3 + frame_margin)],
        fill=rgba
    )

    return (frame, draw_frame)


def insert_text(draw_frame, text, font, color, img_size, spacing):
    """
    フレームにテキストを挿入する
    new_line_positionが指定された場合、改行を入れる

    Args:
        draw_frame:        ImageDraw型のフレーム
        text:              挿入するテキスト
        font:              フォント
        color:             フォントカラー
        img_size:          画像サイズ
        spacing:           改行する場合の行間サイズ

    Returns:
        なし

    """
    draw_frame.text(
        (img_size[0] / 2, img_size[1] / 2),
        text,
        fill=color,
        font=font,
        anchor='mm',
        spacing=spacing,
        align='center'
    )


def main():

    # envファイルの読み込み
    load_dotenv()
    IMG_PATH = os.environ['IMG_PATH']
    OUTPUT_PATH = os.environ['OUTPUT_PATH']
    TEXT = os.environ['TEXT']
    FONT_TTF = os.environ['FONT_TTF']
    FONT_SIZE = int(os.environ['FONT_SIZE'])
    RGBA = ast.literal_eval(os.environ['RGBA'])
    FONT_COLOR = os.environ['FONT_COLOR']
    SPACING = int(os.environ.get('SPACING', 0))
    FRAME_MARGIN=int(os.environ.get('FRAME_MARGIN', 0))

    img = Image.open(IMG_PATH).convert('RGBA')
    img_size = img.size

    # フレームの作成
    frame, draw_frame = create_frame(img_size, RGBA, FRAME_MARGIN)

    font = ImageFont.truetype(FONT_TTF, FONT_SIZE)

    # フレームに文字を挿入
    insert_text(draw_frame, TEXT, font, FONT_COLOR, img_size, SPACING)

    # 画像とフレームを合成
    result_img = Image.alpha_composite(img, frame)
    result_img = result_img.convert('RGB')

    # 合成後の画像を保存
    result_img.save(OUTPUT_PATH)

    img.close()


if __name__ == "__main__":
    main()

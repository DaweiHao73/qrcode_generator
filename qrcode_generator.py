import qrcode
from PIL import Image
import io

def generate_qr_code(data, filename=None, size=10, border=4):
    """
    生成 QR Code
    
    參數:
    data: 要編碼的數據（文字、網址等）
    filename: 保存的檔案名稱（可選）
    size: QR Code 的大小（預設為 10）
    border: 邊框寬度（預設為 4）
    
    返回: PIL Image 物件
    """
    # 創建 QR Code 實例
    qr = qrcode.QRCode(
        version=1,  # 控制 QR Code 的大小（1 是最小的）
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 錯誤修正等級
        box_size=size,  # 每個方格的像素大小
        border=border,  # 邊框的方格數
    )
    
    # 添加數據
    qr.add_data(data)
    qr.make(fit=True)
    
    # 創建圖像
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 如果提供了檔案名稱，則保存圖像
    if filename:
        img.save(filename)
        print(f"QR Code 已保存為: {filename}")
    
    return img

def generate_qr_with_logo(data, logo_path, filename=None):
    """
    生成帶有 Logo 的 QR Code
    
    參數:
    data: 要編碼的數據
    logo_path: Logo 圖片的路徑
    filename: 保存的檔案名稱（可選）
    """
    # 生成基本 QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 使用高錯誤修正等級
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # 創建 QR Code 圖像
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # 開啟並調整 Logo 大小
    try:
        logo = Image.open(logo_path)
        
        # 計算 Logo 大小（QR Code 大小的 1/5）
        qr_width, qr_height = qr_img.size
        logo_size = min(qr_width, qr_height) // 5
        
        # 調整 Logo 大小
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # 計算 Logo 位置（置中）
        logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        
        # 將 Logo 貼到 QR Code 上
        qr_img.paste(logo, logo_pos)
        
        if filename:
            qr_img.save(filename)
            print(f"帶 Logo 的 QR Code 已保存為: {filename}")
        
        return qr_img
        
    except Exception as e:
        print(f"無法加載 Logo: {e}")
        return qr_img

# 使用範例
if __name__ == "__main__":
    # IKEA 新莊店維修服務頁面 QR Code
    
    # 中文版網址
    url_zh = "https://www.ikea.com.tw/zh/store/hsin-chuang/repair"
    qr_zh = generate_qr_code(url_zh, "ikea_repair_zh.png", size=10)
    print("IKEA 維修服務 (中文版) QR Code 生成完成")
    
    # 英文版網址
    url_en = "https://www.ikea.com.tw/en/store/hsin-chuang/repair"
    qr_en = generate_qr_code(url_en, "ikea_repair_en.png", size=10)
    print("IKEA 維修服務 (英文版) QR Code 生成完成")
    
    print("\n✅ 兩個 QR Code 都已生成完成！")
    print("📁 檔案位置:")
    print("   - ikea_repair_zh.png (中文版)")
    print("   - ikea_repair_en.png (英文版)")
    
    # 顯示圖像（如果在 Jupyter notebook 中執行）
    # qr_zh.show()  # 取消註解以顯示中文版圖像
    # qr_en.show()  # 取消註解以顯示英文版圖像
import os

def replace_in_html_files(input_path, input_text):
    # Lặp qua tất cả các thư mục và tệp trong đường dẫn input_path
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith(".html"):  # Chỉ làm việc với các tệp .html
                file_path = os.path.join(root, file)

                # Đọc nội dung của tệp .html
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Thay thế chuỗi 'src="/images/' bằng 'src="/<input_text>/images/'
                new_content = content.replace('src="/images/', f'src="/{input_text}/images/')

                # Ghi lại nội dung đã thay đổi vào tệp
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Đã thay thế trong file: {file_path}")

# Sử dụng hàm replace_in_html_files
input_path = "public"  # Thay đổi đường dẫn này thành đường dẫn trỏ đến thư mục public của bạn
input_text = "my_workshop_aws_intern"  # Thay đổi chuỗi này thành chuỗi bạn muốn thêm vào

replace_in_html_files(input_path, input_text)
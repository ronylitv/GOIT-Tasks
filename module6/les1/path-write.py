from pathlib import Path

path_text = Path('Test/my_txt_file.txt')
path_text.write_text('Tewsfdslkjfdskhfkdhkfjhsdkjfj\n'
                     'jdfjksdfkjsdjkfhjksd')

print(path_text.read_text())

path_bytes = Path('Test/my_txt_file.txt')
path_bytes.write_bytes(b'Tewsfdslkjfdskhfkdhkfjhsdkjfj\njdfjksdfkjsdjkfhjksd')

path_text.write_bytes(b'adsadasd')
print(path_text.read_bytes())

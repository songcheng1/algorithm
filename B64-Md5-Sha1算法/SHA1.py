# -*- coding:utf8 -*-
"""
密文长度：40
"""
import hashlib

def get_sha1(keyword):
    # 创建sha1对象
    m = hashlib.sha1()
    # 待加密信息 必须encode编码
    m.update(keyword.encode('utf8'))
    # 进行加密
    keyword_sh1 = m.hexdigest()

    print(f'sha1加密前：{keyword}')
    print(f'sha1加密后：{keyword_sh1}')
    print(f'密文长度：{len(m.hexdigest())}')

    return m.hexdigest()

if __name__ == '__main__':
    keyword = 'woaini'
    get_sha1(keyword)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms

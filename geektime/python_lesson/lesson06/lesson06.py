# Python “黑箱”：输入与输出

# name = input('your name:')
# gender = input('you are a boy?(y/n)')
# if gender == None:
#     gender = 'n'
# welcome_str = 'Welocme to the matrix {prefix} {name}.'
# welcome_dict = {
#     'prefix': 'Mr.' if gender == 'y' else 'Mrs.',
#     'name': name
# }
# print('authorizing....')
# print(welcome_str.format(**welcome_dict))


# in.txt文件进行自然语言处理
import re

def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w ]', '', text)
    # print(text)

    # 转为小写
    text = text.lower()

    # 生成所有单词的列表
    word_list = text.split(' ')
    # print(word_list)

    # 去除空白单词
    word_list = filter(None, word_list)

    # 生成单词和词频的字典
    word_cnt = dict()
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    
    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_cnt

with open('in.txt', 'r') as fin:
    text = fin.read()

word_and_freq = parse(text)
print(word_and_freq)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write(f'{word} {freq}\n')
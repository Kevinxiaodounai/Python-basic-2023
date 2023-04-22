from matplotlib import pyplot as plt


def mat_bing(name_list, count_list, bing_name):
    # 设置中文
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # plt.rcParams['font.family'] = 'Arial'
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 使用count_list的比列来绘制饼图
    # 使用name_list作为注释
    patches, l_text, p_text = plt.pie(count_list,
                                      labels=name_list,
                                      labeldistance=1.1,
                                      autopct='%3.1f%%',
                                      shadow=False,
                                      startangle=90,
                                      pctdistance=0.6)
    # labeldistance.文本的位置远点有多远，1.1指1.1倍半径的位置
    # autopct, 圆里面饿文本格式， %3.1f%%表示占3个位，保留1位小数
    # shadow, 饼是否有阴影
    # startangle, 起始角度， 0，表示从0 开始逆时针转， 为第一块。 一般选择从90度开始比较好看
    # pctdistance, 百分比的text离圆心的距离
    # patches, l_texts, p_texts, 为了得到饼图的返回值， p_texts饼图为内部文本的，l_texts饼图外label的文本

    # 改变文本的大小
    # 方法是把每一个text遍历。 调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = 30
    for t in p_text:
        t.set_size = 30
    # 设置x ,y轴刻度一致， 这样饼图才能是圆的
    plt.axis('equal')
    plt.title(bing_name)  # 主题
    plt.legend()

    # 保存到图片
    # plt.savefig('result1.png')

    # 显示图片
    plt.show()


if __name__ == '__main__':
    mat_bing(['名称1', '名称2', '名称'], [1000, 123, 444], '测试饼图')

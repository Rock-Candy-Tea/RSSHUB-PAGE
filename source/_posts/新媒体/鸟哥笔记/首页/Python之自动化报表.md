
---
title: 'Python之自动化报表'
categories: 
 - 新媒体
 - 鸟哥笔记
 - 首页
headimg: 'https://qnssl.niaogebiji.com/115548136560a222849fd509.24679172.png'
author: 鸟哥笔记
comments: false
date: Mon, 17 May 2021 08:29:00 GMT
thumbnail: 'https://qnssl.niaogebiji.com/115548136560a222849fd509.24679172.png'
---

<div>   
<div style="height: 6px"></div>
                        <section><section><section><section><section><p><strong>作者介绍</strong></p></section></section></section></section></section><p></p><section><section><section><p><strong>@阿星</strong></p><p>互联网资深数据分析师。</p><p>专注自动化，醉心自动化处理一切。</p><p>“数据人创作者联盟”成员。</p></section></section></section><section><p><br></p><p>人生苦短，我用python。</p><p>相信做过报表的都对其烦不胜烦，周报，月报，季报；一期期的报表，一次次的心酸泪，烦不胜烦。至于作者是怎么知道的，因为我也是这个苦逼报表大军的一员。</p><p><br></p><p>是这样的，当时参与公司的一个项目，我的任务是出报表，听到任务时，心中顿时乐开了花，呜呼，这个简单，不就是出个报表吗。So easy！可拿到历史数据做成的表格顿时就不淡定了，一共是6个excel，每个excel是4-5个sheet，每个sheet里还有一堆花花绿绿的表格需要填写，心里顿时不淡定了。完成整个任务之后，唯一感觉到的是，痛苦麻木。</p><p><br></p><p>之后通过网络查询资料，发现这个报表居然可以自动化。接着花了一个星期的时间将报表自动化，当最后一个表格自动化代码写完后，打开python，运行程序，不得不说，一个字爽，再也不用一点一点的往sheet里弄数据了。</p><p><br></p><p>好了，接下来就为大家介绍今天的主角，xlwings。</p><p>先简单的看一下最终生成的表格效果吧。</p><p><br></p></section><section><section style="text-align: center;"><img src="https://qnssl.niaogebiji.com/115548136560a222849fd509.24679172.png" style="vertical-align: middle; box-sizing: border-box; width: 500px; height: auto;" class="article_img" width="500" height="169" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" alt="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" referrerpolicy="no-referrer"></section></section><section><p>下面我们就来看看这个案例吧。</p><p><br></p><p>以下是我们的原始数据，一共以三个sheet，每个sheet，这三个sheet分别是原煤，原油，天然气的数据。，指标有产量当期值，产量累计值，产量同比增长，产量累计增长。</p><p><br></p><p>这些数据都是可以在国家统计局里下载出来的，有兴趣的小伙伴可以自行下载。这个案例是让我们将数据以上表格的形式输出，指标名称是白色，单元格是黑色，此外数据中，红色是大于平均值进行得标注，蓝色是小于平均值进行的标注，表格字体为宋体。</p><p><br></p></section><section><section style="text-align: center;"><img src="https://qnssl.niaogebiji.com/142913065560a222853e9486.02534509.png" style="vertical-align: middle; box-sizing: border-box; width: 500px; height: auto;" class="article_img" width="500" height="138" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" alt="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" referrerpolicy="no-referrer"></section></section><section><p><br></p></section><section><section style="text-align: center;"><img src="https://qnssl.niaogebiji.com/138967693760a22285c61591.93591181.png" style="vertical-align: middle; box-sizing: border-box; width: 500px; height: auto;" class="article_img" width="500" height="134" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" alt="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" referrerpolicy="no-referrer"></section></section><section><p><br></p></section><section><section style="text-align: center;"><img src="https://qnssl.niaogebiji.com/108366147860a222865a5f01.92834358.png" style="vertical-align: middle; box-sizing: border-box; width: 500px; height: auto;" class="article_img" width="500" height="128" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" alt="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" referrerpolicy="no-referrer"></section></section><section><p><br></p><p>首先呢，先导入相关库，用python读取原始数据。</p><section><p><br></p><pre>import pandas as pd</pre><pre><code>import xlwings as xw</code><code><br></code><code><br></code><code>raw_coal=pd.read_excel(r'统计局数据.xlsx',sheet_name='原煤')<br><br></code><code>crude_oil=pd.read_excel(r'统计局数据.xlsx',sheet_name='原油')<br><br></code><code>natural_gas=pd.read_excel(r'统计局数据.xlsx',sheet_name='天然气')<br><br></code><code>data=pd.merge(raw_coal,crude_oil,on='指标')<br><br></code><code>data=pd.merge(data,natural_gas,on='指标')<br><br></code><code>finally_data=data[['指标','原煤产量当期值(万吨)','原油产量当期值(万吨)','天然气产量当期值(亿立方米)']]<br><br></code><code>print(finally_data)</code></pre></section><p><br></p></section><section><section style="text-align: center;"><img src="https://qnssl.niaogebiji.com/30417514460a22286d88ab5.86881826.png" style="vertical-align: middle; box-sizing: border-box; width: 500px; height: auto;" class="article_img" width="500" height="140" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" alt="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" referrerpolicy="no-referrer"></section></section><section><p><br></p></section><section><p>就数据而言，已经离我们要的最终表格差的不远了，就差一点点细节了。</p><p><br></p><p>是时候上我们的主角xlwings，xlwings能够非常方便的读写excel文件中的数据，最重要的是它可以对单元的格式进行修改，可以与pandas无缝连接。</p><p><br></p><p>使用xlwings库创建一个excel工作簿，在工作簿中创建一个表，表的名称为finally_data。</p><p><br></p></section><section><p>然后将上面利用pandas整合的数据复制到finally_data表格中，当然了将数据复制到表格中，在此看来有三种方式。</p><p><br></p></section><section><p>第一种：将一个数据看成一个单位，一个一个写入创建的表格中，此时需要注意的是，每一个数据在excel的位置和在dataframe表格中的位置，以免出现错误。</p><p><br></p><p>第二种：将一行数据看成一个单位，此时需要注意的是，每行数据的第一个在excel中的位置，参考复制粘贴形式。</p><p><br></p><p>第三种：将一张表的数据看成一个单位，本质上与第二种没什么区别，都是切片式传入数据，但是第三种方法是一二维数组的形式写入。</p><section><p><br></p><pre>wb=xw.Book()
sht=wb.sheets['Sheet1']
sht.name='finally_data'
columns=list(finally_data.columns)##得到列名
sht.range('A1').value = columns####在第一行复制列名
##第一种方式，将一个数据为单位，一个个写入创建的表格中
# for row in range(2,11):
#     for col in range(1,5):
#         sht.range(row,col).value =finally_data.iloc[row-2,col-1]
##第二中方式，将一行数据为单位，一行一行的写入创建的表格中
# for i in range(0,len(finally_data)):
#     data_row=list(finally_data.iloc[i,:])
#     row=i+2#     row_clo='A'+str(row)
#     sht.range(row_clo).value =data_row
#第三种方式，将一张表格为单位，直接写入创建的表格中
finally_data1=finally_data.values
sht.range('A2').value = finally_data1</pre></section><p><br></p></section><section><section style="text-align: center;"><img src="https://qnssl.niaogebiji.com/205970603260a222874d0972.06874933.png" style="vertical-align: middle; box-sizing: border-box; width: 500px; height: auto;" class="article_img" width="500" height="236" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" alt="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" referrerpolicy="no-referrer"></section></section><section><p>三者均能达到我们想要结果，各有优劣，作者喜欢的是第三种。达到这一步的时候，剩下的就是对表格内单元格的格式进行修改了。</p><p><br></p></section><section><p>再对单元格进行修改之前，我们要先求出来原煤产量当期值，原油产量长期值，天然气产量当期值，这三列数据中大于平均值和小于平均值的数据在Dataframe的位置，同时得出该数据在excel的位置，方便在进行单元格的格式修改。</p><section><p><br></p><pre>describe=finally_data.describe()</pre><pre>avg=list(describe.loc['mean',:])</pre><pre><code>##计算大于均值的数在excel的位置<br><br></code><code>red_原煤=list(finally_data.index[finally_data['原煤产量当期值(万吨)']>avg[0]])<br><br></code><code>red_position1=['B'+str(i+2) for i in red_原煤 ]<br><br></code><code>red_原油=list(finally_data.index[finally_data['原油产量当期值(万吨)']>avg[1]])<br><br></code><code>red_position2=['C'+str(i+2) for i in red_原油 ]<br><br></code><code>red_天然气=list(finally_data.index[finally_data['天然气产量当期值(亿立方米)']>avg[2]])<br><br></code><code>red_position3=['D'+str(i+2) for i in red_天然气 ]<br><br></code><code>red=red_position1+red_position2+red_position3</code><code><br></code><code><br></code><code>##计算小于均值的数在excel的位置<br><br></code><code>blue_原煤=list(finally_data.index[finally_data['原煤产量当期值(万吨)']<avg[0]])< p=""><br><br></code><code>blue_position1=['B'+str(i+2) for i in blue_原煤 ]<br><br></code><code>blue_原油=list(finally_data.index[finally_data['原油产量当期值(万吨)']<avg[1]])< p=""><br><br></code><code>blue_position2=['C'+str(i+2) for i in blue_原油 ]<br><br></code><code>blue_天然气=list(finally_data.index[finally_data['天然气产量当期值(亿立方米)']<avg[2]])< p=""><br><br></code><code>blue_position3=['D'+str(i+2) for i in blue_天然气 ]<br><br></code><code>blue=blue_position1+blue_position2+blue_position3<br><br></code><code>print(red)<br><br></code><code>print(blue</code></pre></section><p>终于所有的条件全部满足了，最后可以对表格的格式进行修改了。<br></p></section><section><p><br></p><p>首先就是将字体全部改成宋体同时在表格中有数据的区域加上边框。</p><section><p><br></p><pre>#区域内字体改变成宋体,加上边框
a_range = f'A1:D10'#区域
sht.range(a_range).api.Font.Name='宋体' #字体
sht.range(a_range).api.Borders(8).LineStyle = 1 #上边框
sht.range(a_range).api.Borders(9).LineStyle = 1 #下边框
sht.range(a_range).api.Borders(7).LineStyle = 1 #左边框
sht.range(a_range).api.Borders(10).LineStyle = 1 #右边框
sht.range(a_range).api.Borders(12).LineStyle = 1 #内横边框
sht.range(a_range).api.Borders(11).LineStyle = 1 #内纵边框</pre></section><p><br></p><p>第二步就是将第一行的字体变成白色，单元格填充黑色。</p><section><p><br></p><pre>#区域内字体颜色成白色，单元格变成黑色
b_range = f'A1:D1'#区域第一行
sht.range(b_range).api.Font.Color = 0xffffff
sht.range(b_range).color=(0, 0, 0)</pre></section><p><br></p><p>最后一步就是将大于均值的数据字体改成红色，小于均值的字体改成蓝色。然后在进行保存。</p><section><p><br></p><pre>#######在excel 表格里改变字体颜色
for i in red:
sht.range(i).api.Font.Color = 0x0000ff
for i in blue:
sht.range(i).api.Font.Color = 0xFF0000
wb.save('结果数据.xlsx')
wb.close()</pre></section><p><br></p></section><section><section style="text-align: center;"><img src="https://qnssl.niaogebiji.com/12761531260a222882fa6f7.07737545.png" style="vertical-align: middle; box-sizing: border-box; width: 500px; height: auto;" class="article_img" width="500" height="153" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" alt="鸟哥笔记,数据运营,一个数据人的自留地,数据分析,数据模型,数据运营" referrerpolicy="no-referrer"></section></section><section><p><br></p><p>结果出来后，符合我们的要求。本次案例完整结束，当然了真正入手一个完整的自动化报表项目，远不止这么简单，中间还会出现一下别的问题。如果想要了解更多请持续关注.</p><p label="图片描述" style="font-size: 12px; color: rgb(129, 131, 134); text-align: center; font-weight: 300; line-height: 30px; margin-bottom: 25px;">-END-</p></section>                        <div style="height: 1px"></div>
                      
</div>
            
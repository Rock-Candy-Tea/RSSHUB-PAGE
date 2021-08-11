
---
title: 'Pandas数据清理，看这一篇就够了'
categories: 
 - 新媒体
 - 鸟哥笔记
 - 首页
headimg: 'https://notecdn.yiban.io/cloud_res/716532255/imgs/21-8-10_12:43:55.076_38769.png'
author: 鸟哥笔记
comments: false
date: Wed, 11 Aug 2021 03:14:46 GMT
thumbnail: 'https://notecdn.yiban.io/cloud_res/716532255/imgs/21-8-10_12:43:55.076_38769.png'
---

<div>   
<div style="height: 6px"></div>
                        <section><section><section><section><section><p><strong>作者｜</strong><strong>吃货第一名的Claire</strong></p></section></section></section></section></section><section><section><section><p><br></p></section></section></section><section><p>吐血整理数据人常用Pandas数据清理（附代码）</p><p>全文干货，阅读请自备奶茶解渴（wink）。</p><p><br></p><p>数据行业的从业者都知道数据清理是整个数据分析周期（见下图）最重要也是最耗时的步骤。没有“干净”的、符合特定规范的数据输入，就没有有效的结果引导决策，更糟糕的是，数据清理不完整或者错误甚至会误导决策，GIGO (garbage in, garbage out)就是我们数据人最想避免的情况。</p><p><br></p></section><section><section style="text-align: center;"><img src="https://notecdn.yiban.io/cloud_res/716532255/imgs/21-8-10_12:43:55.076_38769.png" style="vertical-align: middle; box-sizing: border-box; width: 500px; height: auto;" class="article_img" width="500" height="426" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,业务,策略,数据可视化,数据统计,策略,数据可视化" alt="鸟哥笔记,数据运营,一个数据人的自留地,业务,策略,数据可视化,数据统计,策略,数据可视化" referrerpolicy="no-referrer"></section></section><section><p>Source: Quora</p></section><section><p><br></p><p>备注：The step of data preparation is also known as Data Cleaning or Data Wrangling。</p><p><br></p><p>这篇文章是我通过工作中处理大几十个公司的数据遇到的问题而做的总结，问题都源于工业界实际应用案例，大家可以当作备考、面试、工作的cheat sheet，还不快点赞收藏~</p><p><br></p><p>此处附有GitHub代码：请自行下载。</p><p>https://github.com/ClaireWithGithub/pandas_data_cleaning/blob/main/data_cleaning_github_08052021.ipynb</p><p><br></p><p>本文的方法都尽量致力于用最短的代码、最快的运行速度来解决问题，当然，如果有更好的方法欢迎大家留言。</p><p><br></p><p>建议：阅读code前，大家可以先想想当你们遇到这些问题会怎么写，先思考再“抄作业”看解析，印象会更加深刻哦。</p><p><br></p><p>Note：数据清理好习惯 - 代码run完，记得要double check清理结果。</p><h2 label="二级标题" style="background-image: url("/img/article/h2_icon.png"); background-size: 8px 20px; background-position: 0px 5px; background-repeat: no-repeat; margin: 25px 0px 20px; padding-left: 12px; font-size: 18px; font-weight: 600; color: rgb(33, 38, 41); line-height: 30px;"><strong>问题一：合并多个excel文件的多个工作表</strong></h2><p>完整代码：</p><section><p><br></p><pre>df = pd.DataFrame()
# the glob module is used to retrieve files/pathnames matching a specified pattern
dir_filenames = sorted(glob('./*.xlsx')) # all excel files from current directory
for dir_file in dir_filenames: 
   dict_xlsx = pd.read_excel(dir_file, sheet_name=None)
   workbook = pd.concat([v_df.assign(Sheet = k) for k,v_df in dict_xlsx.items()], ignore_index=True) 
   df = pd.concat([df,workbook],ignore_index=True)
print(f'shape of merged files:&#123;df.shape&#125;')
解析：总体思路是读取每个工作簿，再读取每个工作簿的工作表，list comprehension内循环合并表，外循环合并工作簿
glob用于返回符合某个pattern的路径和文件名glob('./*.xlsx') 返回当前目录下的所有Excel文件名
python的built-in function sorted()不改变原list，要赋值给新的variable才实现排序
pd.read_excel(dir_file, sheet_name=None) 返回dictionary，key是sheet name， value是工作表的数据
[v_df.assign(Sheet = k) for k,v_df in dict_xlsx.items()]是list comprehension，通常能简化代码的同时加快代码的运行速度
df.assign()是新加一列，记录工作表名称
pd.concat([])是纵向合并数据的好方法</pre></section><h2 label="二级标题" style="background-image: url("/img/article/h2_icon.png"); background-size: 8px 20px; background-position: 0px 5px; background-repeat: no-repeat; margin: 25px 0px 20px; padding-left: 12px; font-size: 18px; font-weight: 600; color: rgb(33, 38, 41); line-height: 30px;"><strong>问题二：查看空值和处理空值</strong></h2><p>完整代码：</p><section><p><br></p><pre>count_null_series = df.isnull().sum() # returns series
count_null_df = pd.DataFrame(data=count_null_series, columns=['Num_Nulls'])
# what % of the null values take for that column
pct_null_df = pd.DataFrame(data=count_null_series/len(df), columns=['Pct_Nulls'])
null_stats = pd.concat([count_null_df, pct_null_df],axis=1)
null_stats</pre></section><p><br></p><p>结果：</p></section><section><section style="text-align: center;"><img src="https://notecdn.yiban.io/cloud_res/716532255/imgs/21-8-10_12:43:55.186_53318.png" style="vertical-align: middle; box-sizing: border-box; width: 350px; height: auto;" class="article_img" width="350" height="274" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,业务,策略,数据可视化,数据统计,策略,数据可视化" alt="鸟哥笔记,数据运营,一个数据人的自留地,业务,策略,数据可视化,数据统计,策略,数据可视化" referrerpolicy="no-referrer"></section></section><section><p><br></p><p>解析：df.isnull().sum()会算出每列缺失值的数量，再算一个缺失值占本列的百分比可以让自己更清楚数据的情况和下一步如何清理缺失值。</p><p><br></p><p>处理缺失值：</p><section><p><br></p><pre>-  时间序列的数据常用df[col_name].fillna(method="ffill",inplace=True)，ffill表示按上一个值填充
-  不同列补不同的值df.fillna(value=&#123;col1:50, col2:67, col3:100&#125;, inplace=True)
-  以当列的平均值弥补空值df.where(pd.notna(df), df.mean(), axis="columns", inplace=True)
-  任意选定的列为空就删除该行df.dropna(subset=subset_list, inplace=True)
-  当一半的行为空，删除该列df.dropna(thresh=len(df)*N, axis=1, inplace=True)</pre></section><h2 label="二级标题" style="background-image: url("/img/article/h2_icon.png"); background-size: 8px 20px; background-position: 0px 5px; background-repeat: no-repeat; margin: 25px 0px 20px; padding-left: 12px; font-size: 18px; font-weight: 600; color: rgb(33, 38, 41); line-height: 30px;"><strong>问题三：删除多列</strong></h2><p>有没有小伙伴像我一样，当数据有很多无关不重要的列，而不愿意copy paste列名去drop的童鞋，这里提供用column index一行搞定删除多列的问题。</p><p><br></p><p>完整代码：</p><section><p><br></p><pre>df.info()
df.drop(df.columns[start_ind:stop_ind],axis=1,inplace=True)
df.info()</pre></section><p><br></p><p>当列很多的时候，每个column对应的index一个个数可太麻烦了，df.info()是一个非常简洁又高效的方法。他会返回dataframe的行数，列数，列名对应的index，数据类型，非空值和memory usage。</p><p><br></p><p>所以第一个df.info()就是为了找出你要删的列明的起始index和终止index，注意，如果你要删2-4列，stop_index应该是5才会把第4列删掉。第二个df.info()是为了double check最后的数据列都是你想要的，如果还有要删列还可以循环进行这样的步骤。</p><h2 label="二级标题" style="background-image: url("/img/article/h2_icon.png"); background-size: 8px 20px; background-position: 0px 5px; background-repeat: no-repeat; margin: 25px 0px 20px; padding-left: 12px; font-size: 18px; font-weight: 600; color: rgb(33, 38, 41); line-height: 30px;"><strong>问题一：批量改列名</strong></h2><p>完整代码：</p><section><p><br></p><pre>df.rename(columns= &#123;'Order_No_1':'OrderID','ItemNo':'ItemID'&#125;, inplace=True) 
   # remove special characters from column name
   df.columns = df.columns.str.replace('[&,#,@,(,)]', '')
   # remove leading/trailing space and add _ to in-between spaces
   df.columns = df.columns.str.strip().str.replace(' ','_')</pre></section><p><br></p><p>df.rename()是常见的改列名的方法，在这里想格外强调后两行代码，是批量格式化列名的“黑科技”。</p><p><br></p><p>note：数据工作中，文件命名的convention（约定习俗）是不留空格，要么加’_’，要么加’-‘,要么CamelCase，这同样适用于数据的列名命名，因为计算机不擅于处理/解析空格。</p><h2 label="二级标题" style="background-image: url("/img/article/h2_icon.png"); background-size: 8px 20px; background-position: 0px 5px; background-repeat: no-repeat; margin: 25px 0px 20px; padding-left: 12px; font-size: 18px; font-weight: 600; color: rgb(33, 38, 41); line-height: 30px;"><strong>问题二：批量更改数据格式</strong></h2><section><pre>for c in ['OrderID','ItemID','Class']:
df[c] = df[c].astype('str')</pre></section><h2 label="二级标题" style="background-image: url("/img/article/h2_icon.png"); background-size: 8px 20px; background-position: 0px 5px; background-repeat: no-repeat; margin: 25px 0px 20px; padding-left: 12px; font-size: 18px; font-weight: 600; color: rgb(33, 38, 41); line-height: 30px;"><strong>问题三：处理重复值</strong></h2><p>完整代码：</p><section><p><br></p><pre>len_df = len(df)
len_drop = len(df.drop_duplicates(subset = subset_list))
len_diff = len_df-len_drop
print(f'difference of length:&#123;len_diff&#125;')
if len_diff>0: 
   dups = df.duplicated(keep=False).sort_values(by=sort_list) 
df_drop = df.drop_duplicates(subset=subset_list, keep='last')</pre></section><p><br></p><p>解析：df.drop_duplicates(subset = subset_list)会返回基于指定列subset_list去重后的dataframe。如果发现有重复值，</p><p>df.duplicated(keep=False).sort_values(by=sort_list)这段代码可以让你有方向的进行比较，keep=False是保证重复值都展示出来的必备参数，sort_values()是保证重复值挨着出现，方便你接下来决策如何处理他们。以上代码列举了保留重复值最后一项的例子（keep='last'）。</p><h2 label="二级标题" style="background-image: url("/img/article/h2_icon.png"); background-size: 8px 20px; background-position: 0px 5px; background-repeat: no-repeat; margin: 25px 0px 20px; padding-left: 12px; font-size: 18px; font-weight: 600; color: rgb(33, 38, 41); line-height: 30px;"><strong>问题四：处理日期和时间</strong></h2><p>当我们收到了这样的数据，dtype是object，要如何把他转化成date format并且分离出time和hour呢？</p></section><section><section><p id="_img_parent_tmp" style="text-align:center;"><img src="https://notecdn.yiban.io/cloud_res/716532255/imgs/21-8-10_12:43:55.191_49222.png" style="vertical-align: middle; box-sizing: border-box; width: 200px; height: auto;" class="article_img" width="200" height="69" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,业务,策略,数据可视化,数据统计,策略,数据可视化" alt="鸟哥笔记,数据运营,一个数据人的自留地,业务,策略,数据可视化,数据统计,策略,数据可视化" referrerpolicy="no-referrer"></p></section></section><section><p><br></p></section><section><p>代码：</p><section><p><br></p><pre># split by comma, retrieve the first column
df['date_com'] = df['date_com'].str.split(',', expand=True)[0] 
# format要和原日期的格式一致，最后总会返回YYYY-MM-DD HH:MM:SS格式的datetime
df['date_com'] = pd.to_datetime(df['date_com'], format='%Y-%m-%d %H:%M:%S')</pre></section><p><br></p><p>返回结果：</p></section><section><section><p id="_img_parent_tmp" style="text-align:center;"><img src="https://notecdn.yiban.io/cloud_res/716532255/imgs/21-8-10_12:43:55.078_21132.png" style="vertical-align: middle; box-sizing: border-box; width: 200px; height: auto;" class="article_img" width="200" height="81" border="0" vspace="0" title="鸟哥笔记,数据运营,一个数据人的自留地,业务,策略,数据可视化,数据统计,策略,数据可视化" alt="鸟哥笔记,数据运营,一个数据人的自留地,业务,策略,数据可视化,数据统计,策略,数据可视化" referrerpolicy="no-referrer"></p></section></section><section><p><br></p></section><section><p>如果要进一步分离date和time：</p><section><p><br></p><pre> df['Date'] = df['date_com'].dt.date 
    dt_lst = df['date_com'].str.split(' ', n=1, expand = True) 
    df['Time'] = dt_lst[1] 
    # extract hour from Time
    time_lst = df['date_com'].str.split(':', n=1, expand = True) 
    df['Hour'] = time_lst[0] #str</pre></section><p><br></p><p>今天的分享先到这里，感觉有学到新知识记得点赞转发加关注哦。下期见。</p></section><p></p><p label="图片描述" style="font-size: 12px; color: rgb(129, 131, 134); text-align: center; font-weight: 300; line-height: 30px; margin-bottom: 25px;">-END-</p>                        <div style="height: 1px"></div>
                      
</div>
            
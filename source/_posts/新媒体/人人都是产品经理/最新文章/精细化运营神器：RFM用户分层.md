
---
title: '精细化运营神器：RFM用户分层'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/tY4UtKmfdggPUGpdHdpD.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 21 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/tY4UtKmfdggPUGpdHdpD.jpg'
---

<div>   
<blockquote><p>编辑导语：在互联网红利逐渐消失的当下，粗狂式的运营已经难以为继，如何把有限的费用投入到我们最精准的用户上，也就是所谓的精细化运营，是每个公司应该关注的问题。这其中最重要的是用户分层，本文介绍了用户分层的一种最常见、也最常见的方法：RFM用户分层。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4913018 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/tY4UtKmfdggPUGpdHdpD.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、写在前面</h2>
<p>随着互联网流量红利的逐渐消失，之前粗狂式的拓客和一刀切的用户运营已经难以为继，越来越多的公司开始意识到，只靠烧钱圈用户、养用户成本太高，因为不是所有的用户都需要你重点投入，金主爸爸一定要好好维护，潜力股一定要加大投入挖掘价值，而羊毛党永远都是你应该严防的对象，这就是所谓的精细化运营，钱要花在刀刃上，要花在业务和核心用户上。</p>
<p>精细化运营讲究的是千人千面，一千类用户一千种运营策略，所以第一步就是要把用户进行分类，然后才有针对性的运营策略，而用户分类中一种尤为重要和常用的方法就是RFM。</p>
<h2 id="toc-2">二、什么是RFM？</h2>
<p>什么是RFM？RFM最早产生于电商领域，根据客户的交易频次和交易额衡量客户的价值，对客户进行细分。</p>
<p>RFM是衡量客户价值的三个维度，分别为R（Recency）交易间隔、F（Frequency）交易频度、M（Monetary）交易金额组成。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/V1CZKR89qZSfb0x6230i.png" alt width="700" height="168" referrerpolicy="no-referrer"></p>
<p>R表示间隔（Recency）：也就是客户最近一次交易距今的间隔，需要注意的是，R是最近一次交易时间到现在的间隔，而不是最近一次的交易时间，R越大，表示客户越久未发生交易，反之R越小，表示客户越近有交易发生。</p>
<p>F表示频次（Frequency）：也就是客户在最近一段时间内交易的次数，一般来说选取一个特定的时间段，F越大，表示客户交易越频繁，反之F越小，表示客户不够活跃。</p>
<p>M表示额度（Monetary）：也在同样的时间段内，客户交易的金额，M越大，表示客户价值越高，M越小，表示客户价值越低。</p>
<p>有了以上3个维度的数据，就可以对每个用户按照每个维度进行衡量，一般来说我们会选取一个合理的分值对R、F、M进行划分，将3个维度分别分为高、低两类，组合下来就是8类，也就形成了8个用户群体。</p>
<p>当然你说我每个维度分成3类行不行，最终分成27个用户群体不是更精细，当然没问题，但是我们能不能给出27种不同的运营方案，如果给不出，如此细分不就是自嗨么？</p>
<p>毕竟，分为多少个群体不重要，每个群体都要有个性化的运营策略才重要。</p>
<p>下面是一张经典RFM客户细分模型图，R分值、F分值和M分值三个指标构成了一个三维立方图，在各自维度上，根据得分值又可以分为高、低两个分类，分别用2、1表示，最终3个指标两两组合，就构成了8大客户群体。</p>
<p>对每个用户群体进行定性，例如R、F、M分值高的客户为重要价值客户，R、F、M三个分值都低的客户为潜在客户，其他类型客户可以此类推解读。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/KUbIzC4X4sfcpGO4ODxN.png" alt width="803" height="275" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、RFM实际案例</h2>
<p>RFM的原理到这里就讲完了，是不是很简单？确实很简单，但是也确实很实用，在实际的工作中是如何实施这个用户分层模型的呢？下面我们就用一个实际的案例手把手教你如何进行RFM用户分层。</p>
<p>整体来说，RFM模型实施需要以下几个关键的步骤。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/EvQ4Jttc7zttidfGD32k.png" alt referrerpolicy="no-referrer"></p>
<h3>1. 数据准备</h3>
<p>下面通过一个实际的案例学习RFM分析的使用，案例是用python做的，当然了Excel也能做，不必纠结于工具哈，首先将数据导入到data变量，代码如下：</p>
<blockquote><p>import pandas data=pandas.read_csv(‘./RFM分析.csv’,engine=’python’)</p></blockquote>
<p>可以大致看一眼data数据的样式，如下图所示。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/pzxHqE6Rf9TdXVLAkfJ3.png" alt referrerpolicy="no-referrer"></p>
<p>可以看到，这里记录的是客户的每一个订单的信息，第一列为订单ID，第二列为客户ID，第三列为交易日期，第四列为交易金额。</p>
<p>对数据进行一下加工，根据交易日期，计算出每次交易距今的间隔天数，代码如下：</p>
<blockquote><p>#将交易日期处理为日期数据类型</p>
<p>data[‘DealDateTime’]=pandas.to_datetime(data.DealDateTime,format=’%Y/%m/%d’)</p>
<p>#假设2015-10-1是计算当天，求交易日期至计算当天的距离天数</p>
<p>data[‘Days’]=pandas.to_datetime(‘2015-10-1’)-data[‘DealDateTime’]</p>
<p>#从时间距离中获取天数 data[‘Days’]=data[‘Days’].dt.days</p></blockquote>
<p>执行以上代码，即可得到用户每一次交易日期距离指定日期的天数，如下图所示。<img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/8jaDnekIe9ww1KvK4EBf.png" alt referrerpolicy="no-referrer"></p>
<h3>2. 计算R、F、M</h3>
<p>用户的明细数据准备好后，接下来就可以计算每个客户的最近交易间隔R、交易频率F以及交易总额M，计算方法如下：</p>
<p>最近交易间隔R：使用CustomerID作为分组列，距离指定日期间隔天数Days作为聚合列，统计函数使用最小值函数min，即可得到每个客户的最近交易间隔R。</p>
<p>交易频率F：使用CustomerID作为分组列，OrderID作为聚合列，统计函数使用计数函数count。</p>
<p>交易总额M：使用CustomerID作为分组列，订单金额Sales作为聚合列，统计函数使用求和函数sum。</p>
<p>对应的代码如下：</p>
<blockquote><p>#统计每个客户距离指定日期有多久没有消费了，即找出最小的最近消费距离</p>
<p>R=data.groupby(by=[‘CustomerID’],as_index=False)[‘Days’].agg(‘min’)</p>
<p>#统计每个客户交易的总次数，即对订单ID计数</p>
<p>F=data.groupby(by=[‘CustomerID’],as_index=False)[‘OrderID’].agg(‘count’)</p>
<p>#统计每个客户交易的总额，即对每次的交易金额求和</p>
<p>M=data.groupby(by=[‘CustomerID’],as_index=False)[‘Sales’].agg(‘sum’)</p></blockquote>
<p>执行以上代码，得到的结果如下图所示。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/XG4US6Ucapc4bnqCy4nh.png" alt referrerpolicy="no-referrer"></p>
<p>接下来使用merge方法，将R、F、M三个数据在客户CustomerID维度上关联起来，因为它们拥有共同的列名，在这种情况下，on参数可以省略不写，代码如下：</p>
<blockquote><p>#将R、F、M三个数据框关联，merge默认内连接，可省略，两表on条件的关联列名均为CustomerID</p>
<p>Data=R.merge(F).merge(M)</p>
<p>#修改列名 RFMData.columns=[‘CustomerID’,’R’,’F’,’M’]</p></blockquote>
<p>执行以上代码，得到的结果如下图所示。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/krrYAE3jYXC7XwOHzOOj.png" alt referrerpolicy="no-referrer"></p>
<h3>3. 计算R、F、M综合分值</h3>
<p>每个客户的R、F、M数据计算好后，接下来就可以对R、F、M这三个维度进行分组打分赋值，得到对应的R分值、F分值、M分值。</p>
<p>打分标准可以按照业务经验、平均值等标准进行划分。最好是按照业务经验划分，因为这里分类的的用户是要到后面进行精细化运营的，可以通过已有的运营策略反推这里的划分阈值。</p>
<p>当然，如果还没有特别清晰的运营策略，也可以采用平均值进行划分。本例将R、F、M三列分别按照各自的平均值划分为高、低2个组，并分别赋值1分、2分。</p>
<p>R分值（R_S）：距离指定日期越近，R_S越大，R>=平均值，R_S为1，R<平均值，R_S为2。</p>
<p>F分值（F_S）：定义为交易频率越高，F_S越大，F<=平均值，F_S为1，F>平均值，F_S为2。</p>
<p>M分值（M_S）：定义为交易金额越高，M_S越大，M<=平均值，M_S为1，M>平均值，M_S为2。对各个用户的RFM的数据行进行打分赋值，代码如下：</p>
<blockquote><p>#判断R列是否大于等于R列的平均值，使用loc将符合条件R_S列的值赋值为1</p>
<p>RFMData.loc[RFMData[‘R’]>=RFMData.R.mean(),’R_S’]=1</p>
<p>#判断R列是否小于R列的平均值，使用loc将符合条件R_S列的值赋值为2</p>
<p>RFMData.loc[RFMData[‘R’]<RFMData.R.mean(),’R_S’]=2</p>
<p>#同R_S赋值方法，对F_S、M_S进行赋值，但与R相反，F、M均为越大越好</p>
<p>RFMData.loc[RFMData[‘F’]<=RFMData.F.mean(),’F_S’]=1</p>
<p>RFMData.loc[RFMData[‘F’]>RFMData.F.mean(),’F_S’]=2</p>
<p>RFMData.loc[RFMData[‘M’]<=RFMData.M.mean(),’M_S’]=1RFMData.loc[RFMData[‘M’]>RFMData.M.mean(),’M_S’]=2</p></blockquote>
<p>执行代码，R_S、F_S、M_S的分组分值就计算出来了，如下图所示。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/tVdcuEPHNgFnut8LWWNW.png" alt referrerpolicy="no-referrer"></p>
<p>基于以上得出用户最终的RFM分层，如下图所示。</p>
<blockquote><p>#计算RFM综合分值</p>
<p>RFMData[‘RFM’]=100*RFMData.R_S+10*RFMData.F_S+1*RFMData.M_S</p></blockquote>
<p>执行代码，得到的RFM综合分值如下图所示。CustomerID:14568的分层为221，对应的就是一般价值用户。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/J7fEYaCJLfziWbsgRBhT.png" alt referrerpolicy="no-referrer"></p>
<h3>4. 用户分层</h3>
<p>接下来结合文章开头提到的用户分层定义，将用户细分为8种不同的类型。本例采用与RFM综合分值与用户类型的对应关系表映射的方式实现用户分层。</p>
<p>首先将各个RFM综合分值与用户类型的对应关系定义为一个映射匹配表。</p>
<p>然后再使用merge中的内连接inner方法，将RFMData与刚定义的RFM综合分值用户类型的映射匹配表，根据关联列名RFM匹配合并为一个dataframe，这样就完成了用户分层的操作，代码如下：</p>
<blockquote><p>#定义RFM综合分值与客户类型的对应关系表</p>
<p>CustomerType=pandas.DataFrame(data=&#123;‘RFM’:[111,112,121,122,211,212,221,222]’Type’:[‘潜在客户’,’重点挽留客户’,’一般保持客户’,’重点保持客户’,’一般发展客户’,’重点发展客户’,’一般价值客户’,’高价值客户’]&#125;)</p>
<p>#将RFMData与RFM综合分值客户类型的对应关系表合并为一个数据框#merge默认内连接，可省略，两表on条件的关联列名均为RFM，同样可省略 RFMData=RFMData.merge(CustomerType)</p></blockquote>
<p>执行代码，得到的数据如下图所示。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/dZVKN3t25ganHcDH2mWy.png" alt referrerpolicy="no-referrer"></p>
<p>可以看到，最后一列数据，就是对每个用户细分的用户分层。最后，我们来看看，每个类别的用户数是多少，代码如下：</p>
<blockquote><p>#按RFM、Type进行分组统计客户数</p>
<p>RFMData.groupby(by=[‘RFM’,’Type’])[‘CustomerID’].agg(‘count’)</p></blockquote>
<p>执行代码，就可以得到各个客户类型的客户数了。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/g7qPNASkrkd9leT6ClwU.png" alt referrerpolicy="no-referrer"></p>
<p>后续就可以对不同的客户群体，有针对性地采取相应运营策略进行推广、管理，进而提升客户价值和营收水平，限于篇幅，这里就不再展开，我们会在后续的用户运营专题上和大家继续讨论。</p>
<p> </p>
<p>本文由 @数据分析星球 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4617860" data-author="719544" data-avatar="https://static.woshipm.com/APP_U_202107_20210714180347_1885.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            
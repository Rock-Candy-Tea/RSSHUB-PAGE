
---
title: '如何七周成为数据分析师01：常见的Excel函数全部涵盖在这里了'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/41.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 25 Jul 2017 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/41.jpg'
---

<div>   
<img data-action="zoom" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/41.jpg" referrerpolicy="no-referrer"><blockquote><p>本文是<a href="http://www.woshipm.com/data-analysis/444009.html" target="_blank" rel="noopener noreferrer">《如何七周成为数据分析师》</a>的第一篇教程，如果想要了解写作初衷，可以先行阅读七周指南。温馨提示：如果您已经熟悉Excel，大可不必再看这篇文章，或只挑选部分。</p></blockquote>
<p>
</p><p>世界上的数据分析师分为两类，使用Excel的分析师，和其他分析师。</p>
<p>每一个数据新人的入门工具都离不开Excel。因为Excel涵盖的功能足够多。</p>
<p>很多传统行业的数据分析师只要求掌握Excel即可，会SPSS/SAS是加分项。即使在挖掘满街走，Python不如狗的互联网数据分析界，Excel也是不可替代的。</p>
<p>Excel有很多强大的函数，这篇文章主要介绍各种函数的用途。实战会后续文章讲解。</p>
<p>函数可以被我们想象成一个盒子，专门负责将输入转换成输出，不同的函数对应不同的输出。</p>
<blockquote><p>=Vlookup( lookup_value ,table_array,col_index_num,[range_lookup] )</p></blockquote>
<p>上文的Vlookup就是一个经典函数。函数中包含参数，括号里的部分都是参数。我们可以把参数想象成盒子上的开关。vlookup就有四个开关，不同开关组合决定了函数的输入和输出。</p>
<blockquote><p>=Vlookup( 参数1，参数2，参数3，参数4)</p></blockquote>
<p>复杂的原理不需要了解。这篇文章是常用函数汇总。甚至你不需要特别记忆怎么使用函数，<strong>应用Excel函数最重要的能力是学会搜索。</strong>因为绝大部分函数网上已经有相应的解释，图文结合，非常详尽。</p>
<p>学会将遇到的问题转换成搜索语句，在我还是新人时并不会vlookup，我遇到的第一个问题就是关联多张表的数据，我在网上搜索：excel怎么匹配多张表的数据。于是就学会了。这里推荐使用百度，因为前三行的结果基本是百度经验，对新人学习很友好。（后续图片均引用自百度经验）</p>
<p>在理解函数的基础上，我会适当引入高层次的内容，SQL和Python（内建函数）。将其和Excel结合学习，如果大家吃透了Excel的函数，那么后续学习会轻松不少。</p>
<h2 id="toc-1"><strong>清洗处理类</strong></h2>
<p>主要是文本、格式以及脏数据的清洗和转换。很多数据并不是直接拿来就能用的，需要经过数据分析人员的清理。数据越多，这个步骤花费的时间越长。</p>
<p><strong>Trim</strong></p>
<p>清除掉字符串两边的空格。</p>
<p>MySQL有同名函数，Python有近似函数strip。</p>
<p><strong>Concatenate</strong></p>
<blockquote><p>=Concatenate(单元格1，单元格2……)</p></blockquote>
<p>合并单元格中的内容，还有另一种合并方式是& 。”我”&”很”&”帅” ＝ 我很帅。当需要合并的内容过多时，concatenate的效率快也优雅。</p>
<p>MySQL有近似函数concat。</p>
<p><strong>Replace</strong></p>
<blockquote><p>=Replace（指定字符串，哪个位置开始替换，替换几个字符，替换成什么）</p></blockquote>
<p>替换掉单元格的字符串，清洗使用较多。</p>
<p>MySQL中有同名函数，Python中有同名函数。</p>
<p><img data-action="zoom" class="aligncenter" src="https://ask.hellobi.com/uploads/article/20170116/56680ab412cacc6debaa05d5fe2f3975.png" alt="Clipboard Image.png" width="499" height="271" referrerpolicy="no-referrer"></p>
<p><strong>Substitute</strong></p>
<p>和replace接近，区别是替换为全局替换，没有起始位置的概念</p>
<p><strong>Left／Right／Mid</strong></p>
<blockquote><p>=Mid(指定字符串，开始位置，截取长度)</p></blockquote>
<p>截取字符串中的字符。Left/Right（指定字符串，截取长度）。left为从左，right为从右，mid如上文示意。</p>
<p>MySQL中有同名函数。</p>
<p><strong>Len／Lenb</strong></p>
<p>返回字符串的长度，在len中，中文计算为一个，在lenb中，中文计算为两个。<br>
MySQL中有同名函数，Python中有同名函数。</p>
<p><strong>Find</strong></p>
<blockquote><p>=Find（要查找字符，指定字符串，第几个字符）</p></blockquote>
<p>查找某字符串出现的位置，可以指定为第几次出现，与Left／Right／Mid结合能完成简单的文本提取<br>
MySQL中有近似函数 find_in_set，Python中有同名函数。</p>
<p><img data-action="zoom" class="aligncenter" src="https://ask.hellobi.com/uploads/article/20170116/83157b935e0289c1c6e2972bb0feffae.png" alt="Clipboard Image.png" width="403" height="316" referrerpolicy="no-referrer"></p>
<p><strong>Search</strong></p>
<p>和Find类似，区别是Search大小写不敏感，但支持＊通配符</p>
<p><strong>Text</strong></p>
<p>将数值转化为指定的文本格式，可以和时间序列函数一起看</p>
<h2 id="toc-2"><strong>关联匹配类</strong></h2>
<p>在进行多表关联或者行列比对时用到的函数，越复杂的表用得越多。多说一句，良好的表习惯可以减少这类函数的使用。</p>
<p><strong>Lookup</strong></p>
<blockquote><p>=Lookup（查找的值，值所在的位置，返回相应位置的值）</p></blockquote>
<p>最被忽略的函数，功能性和Vlookup一样，但是引申有数组匹配和二分法。</p>
<p><strong>Vlookup</strong></p>
<blockquote><p>=Vlookup(查找的值，哪里找，找哪个位置的值，是否精准匹配)</p></blockquote>
<p>Excel第一大难关，因为涉及的逻辑对新手较复杂，通俗的理解是查找到某个值然后黏贴过来。</p>
<p><img data-action="zoom" class="aligncenter" src="https://ask.hellobi.com/uploads/article/20170116/26b48b8c4878f80de64bb851bfb73995.png" alt="Clipboard Image.png" width="489" height="217" referrerpolicy="no-referrer"></p>
<p><strong>Index</strong></p>
<blockquote><p>＝Index（查找的区域，区域内第几行，区域内第几列）</p></blockquote>
<p>和Match组合，媲美Vlookup，但是功能更强大。</p>
<p><img data-action="zoom" class="aligncenter" src="https://ask.hellobi.com/uploads/article/20170116/53be7cdd7e8e89f42df718fabd3dea57.png" alt="Clipboard Image.png" width="596" height="273" referrerpolicy="no-referrer"></p>
<p><strong>Match</strong></p>
<blockquote><p>＝Match（查找指定的值，查找所在区域，查找方式的参数）</p></blockquote>
<p>和Lookup类似，但是可以按照指定方式查找，比如大于、小于或等于。返回值所在的位置。</p>
<p><img data-action="zoom" class="aligncenter" src="https://ask.hellobi.com/uploads/article/20170116/13c25b686b26345348a94adaecd98552.png" alt="Clipboard Image.png" width="507" height="390" referrerpolicy="no-referrer"></p>
<p><strong>Row</strong></p>
<p>返回单元格所在的行</p>
<p><strong>Column</strong></p>
<p>返回单元格所在的列</p>
<p><strong>Offset</strong></p>
<blockquote><p>＝Offset（指定点，偏移多少行，偏移多少列，返回多少行，返回多少列）</p></blockquote>
<p>建立坐标系，以坐标系为原点，返回距离原点的值或者区域。正数代表向下或向左，负数则相反。</p>
<h2 id="toc-3"><strong>逻辑运算类</strong></h2>
<p>数据分析中不得不用到逻辑运算，逻辑运算返回的均是布尔类型，True和False。很多复杂的数据分析会牵扯到较多的逻辑运算</p>
<p><strong>IF</strong></p>
<p>经典的如果但是，在后期的Python中，也会经常用到，当然会有许多更优雅的写法。也有ifs用法，取代if(and())的写法。</p>
<p>MySQL中有同名函数，Python中有同名函数。</p>
<p><strong>And</strong></p>
<p>全部参数为True，则返回True，经常用于多条件判断。</p>
<p>MySQL中有同名函数，Python中有同名函数。</p>
<p><strong>Or</strong></p>
<p>只要参数有一个True，则返回Ture，经常用于多条件判断。</p>
<p>MySQL中有同名函数，Python中有同名函数。</p>
<p><strong>IS系列</strong></p>
<p>常用判断检验，返回的都是布尔数值True和False。常用ISERR，ISERROR，ISNA，ISTEXT，可以和IF嵌套使用。</p>
<h2 id="toc-4"><strong>计算统计类</strong></h2>
<p>常用的基础计算、分析、统计函数，以描述性统计为准。具体含义在后续的统计章节再展开。</p>
<p><strong>Sum／Sumif／Sumifs</strong></p>
<p>统计满足条件的单元格总和，SQL有中同名函数。</p>
<p>MySQL中有同名函数，Python中有同名函数。</p>
<p><strong>Sumproduct</strong></p>
<p>统计总和相关，如果有两列数据销量和单价，现在要求卖出增加，用sumproduct是最方便的。</p>
<p>MySQL中有同名函数。</p>
<p><strong>Count／Countif／Countifs</strong></p>
<p>统计满足条件的字符串个数</p>
<p>MySQL中有同名函数，Python中有同名函数。</p>
<p><strong>Max</strong></p>
<p>返回数组或引用区域的最大值</p>
<p>MySQL中有同名函数，Python中有同名函数。</p>
<p><strong>Min</strong></p>
<p>返回数组或引用区域的最小值</p>
<p>MySQL中有同名函数，Python中有同名函数。</p>
<p><strong>Rank</strong></p>
<p>排序，返回指定值在引用区域的排名，重复值同一排名。</p>
<p>SQL中有近似函数row_number() 。</p>
<p><img data-action="zoom" class="aligncenter" src="https://ask.hellobi.com/uploads/article/20170116/ba1259e384039d227e8784cdb4c2d4e0.png" alt="Clipboard Image.png" width="458" height="480" referrerpolicy="no-referrer"></p>
<p><strong>Rand／Randbetween</strong></p>
<p>常用随机抽样，前者返回0~1之间的随机值，后者可以指定范围。</p>
<p>MySQL中有同名函数。</p>
<p><strong>Averagea</strong></p>
<p>求平均值，也有Averageaif，Averageaifs</p>
<p>MySQL中有同名函数，python有近似函数mean。</p>
<p><strong>Quartile</strong></p>
<blockquote><p>=Quartile（指定区域，分位参数）</p></blockquote>
<p>计算四分位数，比如1~100的数字中，25分位就是按从小到大排列，在25%位置的数字，即25。参数0代表最小值，参数4代表最大值，1~3对应25、50（中位数）、75分位</p>
<p><img data-action="zoom" class="aligncenter" src="https://ask.hellobi.com/uploads/article/20170116/40540ca2d9461c06540358c24ad92050.png" alt="Clipboard Image.png" width="531" height="308" referrerpolicy="no-referrer"></p>
<p><strong>Stdev</strong></p>
<p>求标准差，统计型函数，后续数据分析再讲到</p>
<p><strong>Substotal</strong></p>
<blockquote><p>=Substotal（引用区域，参数）</p></blockquote>
<p>汇总型函数，将平均值、计数、最大最小、相乘、标准差、求和、方差等参数化，换言之，只要会了这个函数，上面的都可以抛弃掉了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://ask.hellobi.com/uploads/article/20170116/48943662c74d3648f79cb68b9bfd2e94.png" alt="Clipboard Image.png" width="389" height="255" referrerpolicy="no-referrer"></p>
<p><strong>Int／Round</strong></p>
<p>取整函数，int向下取整，round按小数位取数。</p>
<p>round(3.1415,2) =3.14 ;</p>
<p>round(3.1415,1)=3.1</p>
<h2 id="toc-5"><strong>时间序列类</strong></h2>
<p>专门用于处理时间格式以及转换，时间序列在金融、财务等数据分析中占有较大比重。时机序列的处理函数比我列举了还要复杂，比如时区、分片、复杂计算等。这里只做一个简单概述。</p>
<p><strong>Year</strong></p>
<p>返回日期中的年</p>
<p>MySQL中有同名函数。</p>
<p><strong>Month</strong></p>
<p>返回日期中的月</p>
<p>MySQL中有同名函数。</p>
<p><strong>Weekday</strong></p>
<blockquote><p>=Weekday(指定时间，参数)</p></blockquote>
<p>返回指定时间为一周中的第几天，参数为1代表从星期日开始算作第一天，参数为2代表从星期一开始算作第一天（中西方差异）。我们中国用2为参数即可。</p>
<p>MySQL中有同名函数。</p>
<p><strong>Weeknum</strong></p>
<blockquote><p>=Weeknum(指定时间，参数)</p></blockquote>
<p>返回一年中的第几个星期，后面的参数类同weekday，意思是从周日算还是周一。</p>
<p>MySQL中有近似函数 week。</p>
<p><strong>Day</strong></p>
<p>返回日期中的日（第几号）</p>
<p>MySQL中有同名函数。</p>
<p><strong>Date</strong></p>
<blockquote><p>=Date（年，月，日）</p></blockquote>
<p>时间转换函数，等于将year()，month()，day()合并</p>
<p>MySQL中有近似函数 date_format。</p>
<p><strong>Now</strong></p>
<p>返回当前时间戳，动态函数</p>
<p>MySQL中有同名函数。</p>
<p><strong>Today</strong></p>
<p>返回今天的日期，动态函数</p>
<p>MySQL中有同名函数。</p>
<p><strong>Datedif</strong></p>
<blockquote><p>=Datedif（开始日期，结束日期，参数）</p></blockquote>
<p>日期计算函数，计算两日期的差。参数决定返回的是年还是月等。</p>
<p>MySQL中有近似函数 DateDiff。</p>
<p>Tips：</p>
<p>1.后续数据类文章都会同步更新在菜单下。</p>
<p>2.Excel以2016版为准。</p>
<h3><strong>相关阅读</strong></h3>
<p><a href="http://www.woshipm.com/data-analysis/444009.html" target="_blank" rel="noopener noreferrer">互联网数据分析能力的养成，需一份七周的提纲</a></p>
<h3><strong>#专栏作家#</strong></h3>
<p>秦路，微信公众号ID：tracykanc，人人都是产品经理专栏作家。</p>
<p>本文由 @秦路 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自PEXELS，基于CCO协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="729892" data-author="159343" data-avatar="http://image.woshipm.com/wp-files/2016/11/yUKWggwqYEiHLgAgKPNt.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">5人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182915_2407.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182807_6948.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183303_2488.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175034_8755.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183351_6166.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            
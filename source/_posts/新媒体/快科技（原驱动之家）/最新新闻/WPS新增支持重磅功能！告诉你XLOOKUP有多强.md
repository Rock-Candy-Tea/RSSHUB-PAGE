
---
title: 'WPS新增支持重磅功能！告诉你XLOOKUP有多强'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211113/S681039e7-a512-4315-80ea-104f9be44b94.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sat, 13 Nov 2021 17:04:09 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211113/S681039e7-a512-4315-80ea-104f9be44b94.jpg'
---

<div>   
<p>不久前，WPS官微发布了一条消息，说是自即日起WPS开始正式支持XLOOKUP函数。</p>
<p>很多人就奇怪了，作为一款办公软件，增加个函数不是太正常了？这有啥可激动的？</p>
<p>其实能让WPS“激动”自然是有些道理，理由就是这个XLOOKUP实在太强了！</p>
<p><strong>示例1、反向查找</strong></p>
<p><strong>目的：通过“姓名“反查“工号“</strong></p>
<p><strong>公式：=XLOOKUP(G6,B:B,A:A)</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211113/681039e7-a512-4315-80ea-104f9be44b94.jpg" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="206" src="https://img1.mydrivers.com/img/20211113/S681039e7-a512-4315-80ea-104f9be44b94.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>日常工作中我们经常会遇到用姓名查工号的情况，由于原始数据中，“工号”字段通常是位于“姓名”之前，因此直接使用VLOOKUP肯定无法得到结果。</p>
<p>通常的办法，是借助IF函数建立一个虚拟数组”IF(&#123;1,0&#125;,B:B,A:A)”，将“工号”与“姓名”临时对调一下，以满足VLOOKUP的操作需求。</p>
<p>不过它的问题就是，对于新手童鞋来说，这个数组太难理解了。</p>
<p>如果换作XLOOKUP呢？很简单，直接输入“=XLOOKUP(G6,B:B,A:A)”就行。</p>
<p>整个语法基本参照了VLOOKUP的习惯，先确定好要查找的内容（G6），然后<span style="color:#ff0000;"><strong>告诉表格去哪里查找（B:B），最后返回对应列的结果就可以了（A:A）。</strong></span></p>
<p>相比之下，XLOOKUP的逻辑是不是就清晰多了！</p>
<p><strong>示例2、出错处理</strong></p>
<p><strong>目的：当查询无结果时，显示“查无此人“</strong></p>
<p><strong>公式：=XLOOKUP(G6,B:B,A:A,"查无此人")</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211113/84a90fd3-9838-4dda-a0d0-ad96ada1fbeb.jpg" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="198" src="https://img1.mydrivers.com/img/20211113/S84a90fd3-9838-4dda-a0d0-ad96ada1fbeb.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>为了防止LOOKUP、VLOOKUP等函数意外出错，我们通常会在函数外围包裹一层IFERROR，用于手工控制出错信息的显示。</p>
<p>不过这种做法一来会让公式变长，二来也不怎么高效。而XLOOKUP的处理方法绝对是简单粗暴，直接将出错信息标在了函数里。高效的同时，也让公式更加简练，就像下面这样：“=XLOOKUP(G6,B:B,A:A,"查无此人")”。</p>
<p>示例3、批量化查询</p>
<p><strong>目的：通过“工号“查询该员工所有信息</strong></p>
<p><strong>公式：=XLOOKUP(G8,A:A,B:E)</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211113/d61de2cc-f288-43a4-9e5c-1cb12eb14f6a.jpg" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="194" src="https://img1.mydrivers.com/img/20211113/Sd61de2cc-f288-43a4-9e5c-1cb12eb14f6a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>编写搜索器时，会在原始数据中批量查询所需的内容。通常有两种解决方法，一是借助VLOOKUP手工确定要查询的列，二是通过COLUMN函数配合VLOOKUP做一个半自动查询器。</p>
<p>那么XLOOKUP有没有更简单的办法呢？答案是有的，方法就是直接填写“=XLOOKUP(G8,A:A,B:E)”。</p>
<p>语法上依旧沿用了VLOOKUP的逻辑，先是确定好要查找的内容（G8），然后告诉表格去哪里查找（A:A），接下来返回B:E列里的对应信息即可。</p>
<p>由于函数的“溢出效应”，相邻几个单元格（性别、职务、部门）也会自动填好结果，连拖拽这一步都省去了。</p>
<p><strong>示例4、多条件查询</strong></p>
<p><strong>目的：通过“姓名”和“性别”两组条件查询员工信息</strong></p>
<p><strong>公式：=XLOOKUP(G7&H7,B:B&C:C,D:D)</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211113/d49ee2a1-4161-4581-bc53-3148fd0bf08a.jpg" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="168" src="https://img1.mydrivers.com/img/20211113/Sd49ee2a1-4161-4581-bc53-3148fd0bf08a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>现实中重名的情况并不少见，当一个条件无法确定一个人时，就要加载第二组条件。</p>
<p>比如本例中，小编就使用了“姓名”+“性别”的双重条件验证。对于此类需求，传统的VLOOKUP需要借助IF函数生成一个虚拟数组。而在XLOOKUP之下，上述公式可以直接简化为“=XLOOKUP(G7&H7,B:B&C:C,D:D)”。</p>
<p><strong>示例5、模糊查询</strong></p>
<p><strong>目的：根据分值为每个人标注等级。</strong></p>
<p><strong>公式：=XLOOKUP(D2,$H$2:$H$5,$I$2:$I$5,,-1)</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211113/e9a9e2d9-c7be-4850-8ea0-e564a7f9d0e7.jpg" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="210" src="https://img1.mydrivers.com/img/20211113/Se9a9e2d9-c7be-4850-8ea0-e564a7f9d0e7.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>熟悉VLOOKUP的小伙伴，大多知道这个函数最后有一个“精确匹配FALSE”和“近似匹配TRUE”的小参数。</p>
<p>其中的“近似匹配”，就是我们常说的模糊查找。通常来讲，模糊查找主要用作区域数值的界定，比如90-100分为“优秀”、70-89分为“良好”，类似这样的分数段筛选，就很适合使用模糊查找。</p>
<p>不过它有一个前提，那就是数值源必须提前使用升序排列，否则无法得到准确结果。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211113/bc357c84-43cb-4444-bd3a-5f1da426960a.jpg" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="245" src="https://img1.mydrivers.com/img/20211113/Sbc357c84-43cb-4444-bd3a-5f1da426960a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而使用XLOOKUP就不用这么麻烦了，它的第五个参数（输入公式时会有提示）直接提供了“0”、“-1”、“1”、“2”四种不同匹配条件。</p>
<p>以本例使用的“-1”为例，它的含义就是当搜索结果达不到目标值499时，会自动向下查找（小于499）。正是借助这样一个选项，我们就轻松配置出了一个业绩等级设定表。</p>
<p><strong>示例6、横向查找</strong></p>
<p><strong>目的：输入产品名称查询该产品的销量、销售额、利润、利润率</strong></p>
<p><strong>公式：=XLOOKUP(B7,B1:E1,B2:E2)</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211113/f2dea483-65b3-4737-90c6-418422edad5e.jpg" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="354" src="https://img1.mydrivers.com/img/20211113/Sf2dea483-65b3-4737-90c6-418422edad5e.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在Excel中，除了纵向搜索的VLOOKUP外，还有一个支持横向搜索的HLOOKUP。这两组函数虽然作用不一，但语法却基本相同。</p>
<p>区别是一个在列中查找，一个在行中查找。而我们的XLOOKUP其实也集合了纵向和横向两种查询机制，除了上面讲到的纵向查询外，你还可以通过变换查找区域来实现横向搜索。</p>
<p>具体效果，如上图所示。</p>
<p><strong>示例7、搜索最后记录</strong></p>
<p><strong>目的：快速查询某商品的最新入库价格</strong></p>
<p><strong>公式：=XLOOKUP(F4,B:B,C:C,,,-1)</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211113/859b3d09-0828-41f7-b3fa-0bf4f5f7226f.jpg" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="260" src="https://img1.mydrivers.com/img/20211113/S859b3d09-0828-41f7-b3fa-0bf4f5f7226f.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>很多出入库表格，都需要查找最后一次出入记录。这个看似简单的要求，实现起来却不容易。</p>
<p>通常我们都是使用LOOKUP建立一个虚拟数组，然后再对其进行查找。</p>
<p>但正如前面所言，这一类东东一来不适合新手理解，二来过多的数组函数对于系统性能也是拖累。特别在一些大型表格中，频繁地使用数组函数，会让表格变得异常缓慢。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211113/c65856fd-e944-4929-8f85-39bf9a31e922.jpg" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="233" src="https://img1.mydrivers.com/img/20211113/Sc65856fd-e944-4929-8f85-39bf9a31e922.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而XLOOKUP的加入，让这个问题变得简单多了。它的解决方法很简单，直接用一个参数来搞定。</p>
<p>依旧以上文为例，如果想查询某商品的最近一次入库价格，只要在它的第6参数位中，输入参数值“-1”。而返回的结果，正是该商品的最后一次入库价。</p>
<p><strong>写在最后</strong></p>
<p>怎么样？看完上面这些案例，是不是有种豁然开朗的感觉？其实在日常使用中，XLOOKUP还有逻辑清晰、语句简练等优势。</p>
<p>举个最简单例子，以往在使用VLOOKUP时，查找范围后面的列数常常要我们手工去数，而XLOOKUP由于直接使用了列标作为返回列，因此也就省掉了这个步骤。</p>
<p>同时由于XLOOKUP还是一个全能型选手，特别对于新手来说更加友好，再不用劳神记忆各种复杂的函数和数组，一个XLOOKUP统统就搞定了！</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211113/fdb4952075d243268ebb9fac444043b0.png" target="_blank"><img alt="WPS新增支持重磅功能！告诉你XLOOKUP有多强" h="337" src="https://img1.mydrivers.com/img/20211113/s_fdb4952075d243268ebb9fac444043b0.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/ruanjian.htm"><i>#</i>软件</a><a href="https://news.mydrivers.com/tag/wps_office.htm"><i>#</i>WPS Office</a></p>
<p class="url">
     <span>原文链接：<a href="https://pcedu.pconline.com.cn/1468/14689244.html">太平洋电脑网</a></span>
<span>责任编辑：振亭</span>
</p>
        
</div>
            
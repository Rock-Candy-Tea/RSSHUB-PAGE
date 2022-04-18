
---
title: '最干货的竞品分析方法：手机安全类APP深度分析'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/62.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 10 Mar 2017 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/62.jpg'
---

<div>   
<img data-action="zoom" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/62.jpg" referrerpolicy="no-referrer"><blockquote><p>本文全是干货，全是思维，全是自己的整理总结；通过现象看本质，带着俯视的角度跳出来看产品，并附有做产品的一些方法；以图>表>字的阅读体验为基础。</p></blockquote>
<p>
</p><h2 id="toc-1">一、概况</h2>
<h3><strong>1.产品名称及版本</strong></h3>
<ul>
<li>360手机卫士  7.7.0</li>
<li>腾讯手机管家 6.8.0</li>
</ul>
<h3><strong>2.体验环境</strong></h3>
<p>设备型号：OPPO N5207  操作系统：Android4.4.4</p>
<h2 id="toc-2">二、市场宏观环境 pest</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/hU5JRrivFVDLdFwTGWoD.jpg" width="450" height="476" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图片来源：2016Q3中国移动安全市场季度监测报告</p>
<h3><strong>P：</strong></h3>
<ul>
<li>《移动互联网应用程序信息服务管理规定》；</li>
<li>《工业和信息化部关于进一步防范和打击通讯信息诈骗工作的实施意见》；</li>
<li>以及国家对互联网重视，连续3届的乌镇互联网大会；</li>
</ul>
<p>可以看出： 国家支持互联网及”互联网+”的健康发展，通过政策重视网络环境的信息安全；卫士和管家的有政策保障。</p>
<h3><strong>E：</strong></h3>
<ul>
<li>“互联网+”继续铸造新经济增长点，改变宏观经济，带动相关产业发展；</li>
<li>2020全面小康实现，国民经济水平及用户将继续增长；</li>
<li>2016年，中国网民规模达7.31亿，互联网普及率达到53.2%，移动端占比95.1% ；</li>
<li>2016年移动支付业务高速发展，移动支付的市场覆盖率达87.8%，参与平台包括金融、网购、社交、餐饮、网约新车等；</li>
<li>但是2016年手机安全软件用户规模逐渐饱和，增长率呈现走低趋势，基本稳定在1.6%左右。</li>
</ul>
<p>可以看出： 互联网影响中国经济，市场前景巨大； 移动支付成为新的消费促进经济的增长点，已经达到了87.8%的市场覆盖率，预测将会继续抢占用户市场； 移动安全的360手机卫士和腾讯手机管家，由于互联网经济的快速发展红利，将会保障移动支付的安全可靠，保障公民信息； 安全软件用户红利逐渐减少，未来的安全软件市场成为红海。挖取和留存其他用户将威胁360手机卫士和腾讯手机管家。</p>
<h3><strong>S：</strong></h3>
<p>2016年，徐玉玉遭遇电信诈骗致死事件，清华大学老师被骗走1600万事件，以及众多的诈骗犯罪事件等；</p>
<p>可以看出：社会重视电信诈骗，关注信息安全；生活中的各种安全威胁成为选择安全产品时的痛点；安全市场符合社会预期。</p>
<h3><strong>T：</strong></h3>
<ul>
<li>安全领域前景开阔，未来物联网的智能硬件、云计算服务的安全、生物识别等技术实力，以及手机厂商的安全芯片，种种技术有利于开拓新的安全；</li>
<li>可以看出：安全领域的技术快速迭代，未来的卫士和管家将利用未来的新技术完善产品，提升用户体验；</li>
</ul>
<p>总之：整合起来，对于安全APP总体的发展来说，趋势还是乐观的，因此，安全软件类用户规模仍有一定的上升空间。</p>
<h2 id="toc-3">三、竞品分析正式开始</h2>
<blockquote><p>注：个人能力十分有限，个人思考总结很多。第一次完整做竞品分析，翻看资料众多，同时各方数据可能造假，所以难免有失误，望体谅。</p></blockquote>
<h3><strong>1.本文的分析维度</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/nJycKpnf831rszQFji6P.jpg" alt width="653" height="357" referrerpolicy="no-referrer"></p>
<p>主要方法如上图所示，采用5E维度为主，主要采用打分来具体形象化产品各方面；附加其他测试；由于是完整分析，故重点分析“有效性”。</p>
<h3><strong>2.基本信息</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/GfgeaGi58JTfrKI3mq3c.jpg" alt width="661" height="248" referrerpolicy="no-referrer"></p>
<ul>
<li>定位接近，类别相同，用户群体一致，此两种产品为直接竞品。</li>
<li>由于两者工具属性明显。产品内没有明显用户数据，运营活动。故运营不作为本分析重点，重点分析商业模式，功能，用户，架构，流程，信息设计和视觉。</li>
</ul>
<h2 id="toc-4">3.商业及战略</h2>
<h3><strong>3.1 本人统计了版本的更迭，试图发现产品规律,结合上述商业模式综合分析。</strong></h3>
<p><strong>360手机卫士</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/StWrVpSWSypykLNMjobI.jpg" alt width="636" height="271" referrerpolicy="no-referrer"></p>
<ul>
<li>360手机卫士几乎每版始终在做手机基本安全功能的完善，从1.0到最近的7.7.0；</li>
<li>360手机卫士前期重点在手机内的安全，中后期主要在人的线上线下生活；</li>
<li>产品定位基本路线即手机安全→人的线上线下生活安全。</li>
</ul>
<p><strong>腾讯手机管家</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/b3efhMyPfJ5lxI6q7L8G.jpg" alt width="632" height="298" referrerpolicy="no-referrer"></p>
<ul>
<li>公司前期以满足手机基本型需求为主，杀毒、优化、软件管理等；</li>
<li>随后增加了人们日常生活的骚扰电话拦截、网购等；</li>
<li>随后融入了人们生活场景的记账，红包提醒等；</li>
<li>定位基本路线即手机安全→人的安全→人的场景化需求。</li>
</ul>
<p>可以看出版本迭代很符合产品定位，360突出的“人与安全紧密连接”，以及管家突出的“安全优化大师，贴身管家”。</p>
<h3><strong>3.2 变现模式</strong></h3>
<p><strong>360手机卫士</strong></p>
<p><strong>广告：</strong></p>
<ul>
<li>软件下载：360公司广告和其他公司产品广告和软件排名；</li>
<li>新闻信息流：通过众媒号和其他商家资讯，增加PV,UV，获取广告收益，广告主要为硬广和feed流，但投放精准性不强；</li>
<li>商家推广广告：通过金币获取商家代金券、到达商品详情页等；</li>
</ul>
<p><strong>合作：</strong></p>
<p>泰康保险，淘宝，58同城，微车摇号等入驻卫士平台，与卫士共享用户价值；</p>
<p><strong>销售：</strong> 向用户销售安心借条、你财富、话费流量包、360实体产品等，并且推荐自家其他工具，如花椒直播、360商城等；</p>
<p>360手机卫士为奇虎360的平台级现金牛支柱产品（例如淘宝、qq），公司移动端商业布局围绕360手机卫士展开。 核心的安全工具不挣钱，360手机卫士主要通过其他上下游延伸产品变现。 360手机卫士上下游涉及的商业领域有新闻资讯、直播、金融、保险、o2o、商城等。每一个新的垂直产品线均依托360手机卫士平台引流。</p>
<p><strong>腾讯手机管家</strong></p>
<p><strong>广告：</strong></p>
<p>软件下载：做腾讯公司广告和其他公司产品广告及软件排名；</p>
<p>商家推广广告：到达商家产品详情页；</p>
<p><strong>合作：</strong></p>
<p>携手wifi商家入驻；58同城提供的服务，搭建平台，共享用户价值；</p>
<p><strong>销售： </strong></p>
<p>向用户销售腾讯大王卡、话费流量包等；</p>
<p>腾讯手机管家对于腾讯来说是一个安全领域的垂直产品，商业模式较为清晰，并没有出现360平台级别的复杂商业需求。 腾讯手机管家主打商业领域为用户场景化，未来会开拓更多场景上的商业模式。尤其是最近的免费WiFi，联系商家和用户，实现盈利。 考虑到腾讯用户付费能力，将来的增值服务可能围绕场景化展开。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/LDvuBmEelDW1VqmNrksS.jpg" alt width="544" height="316" referrerpolicy="no-referrer"></p>
<p>360手机卫士平台效应非常明显，产品线众多，涉及各种领域； 腾讯手机管家工具垂直效应很突出，产品线很少，主要针对安全场景化领域； 二者均符合公司对产品的战略定位。</p>
<h3><strong>3.3 商业的思考与反思</strong></h3>
<p>总结二者，为什么会出现如此不同功能点，甚至为什么他们可以做大呢？我想，这里有一个逻辑：产品战略的<strong>领域定位。</strong></p>
<p>何为爆款？为何会刷爆朋友圈？首先你要想普通老百姓为什么会给你疯狂转发？答案是：满足了<strong>我的兴奋型需求</strong>，我不得不转。在这里定位“我”，即<strong>大众主流</strong>用户，而不是小众非主流用户，这个产品同样可能是用户高频操作和刚需行为。不太好理解吧？我举个栗子。</p>
<p>ofo原来是做骑行旅游项目的，我们如果把“骑行旅游”当做一个终极领域去做，做好“骑行旅游领域”的基本需求和创造需求，那么可以想象，人群小众，非主流，并且这也不是小众非主流人群的高频、刚需行为，所以即使产品体验好到极致，即使那一小拨人群疯狂给你转发，然而还是引不起来主流用户群的兴趣，还是做不大，商业模式更是白白烧钱。</p>
<p>如果把产品定位领域最开始就定在“自行车”，这个用户规模巨大，高频，刚需行为，那么可以从自行车的“细分垂直”先入手，比如先做“大学校园”，然后领域变为“全社会”，垄断整个领域。接下来才涉及需求，发现痛点或者新需求，共享经济的切入点非常好，有大量用户，有盈利模式，于是商业模式从最初的定位就已经确定了。其实跳出来想想，我们觉得很简单，不就是自行车租聘嘛，所以生活中的机会还是很多的，比如我想到了几个领域来定位“衣、食、住、行”。选个具体领域，从细分做起，达到终极目标。</p>
<p>回到安全产品，好处是安全领域用户足够大众主流，这是所有人的痛点；谁都要每天保护下手机，看下流量等，这又足够高频刚需。得了，这个领域势必会有疯狂的竞争，但这样做没错！这总比一个仅针对清理加速的垂直领域，并且做到极致的手机安全软件更好，因为最初的定位就不一样。然而百度手机卫士和猎豹手机卫士同属手机安全，又为什么超不过卫士和管家呢？这就涉及到了宏观上的产品核心竞争力。</p>
<p>像这种工具类产品的变现模式一直是个难点。工具类产品往往是“用户用完即走”，即使是用户量庞大的美图秀秀，也只能靠广告挣钱。用户用完即走说的是满足需求，效率高超，而不是为了让用户走而不挣钱，我们可以学习安全产品的多种变现方式。</p>
<h2 id="toc-5">4.数据</h2>
<blockquote><p>这部分主要考虑活跃人数，并未考虑设备数量。通过艾瑞数据，发现卫士设备安装数比管家多。在各种排名中二者排名均不统一，仅做参考。</p></blockquote>
<h3><strong>4.1应用市场下载市场</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/VhhTK8LQw89SZrWkwr0V.jpg" width="592" height="771" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">数据来源：ASO应用数据下载量统计</p>
<ul>
<li>由图表可以看出，在安卓市场，当前腾讯手机管家占有率总体比360手机卫士高，排名靠前，而且用户对二者评价接近；</li>
<li>应用宝是腾讯管家的主要输出渠道；360手机助手是360手机卫士的主要渠道；</li>
<li>8大应用市场中腾讯领先7大市场，足以说明腾讯管家的用户渠道优势非常明显；</li>
<li>可以发现360劣势非常明显，仅360手机助手一家独大，所以存在刷下载量的情况，但腾讯总体的渠道优势可以得出。</li>
</ul>
<h3><strong>4.2 用户数据</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/ZruPoY5SrPXyBxJoAN39.jpg" alt width="684" height="306" referrerpolicy="no-referrer"></p>
<p>对大众主流用户而言，二者工具性能更明显，用户没有关注欲望。但管家由于用户年轻化，比卫士更为活跃些。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/7SijlBhi87CN6uhhQ2W2.jpg" width="599" height="306" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图像来源：易观APP排名，统计月活人数</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/9pST9bkUsSShn5yXcOmy.jpg" alt="图像来源：易观《中国手机安全市场监测报告2016年第2季度》" width="503" height="272" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图像来源：易观《中国手机安全市场监测报告2016年第2季度》</p>
<ul>
<li>2016年4月腾讯管家月活首度超过360卫士，兴趣转化为活跃用户。随后差距拉大至稳定。结合腾讯的渠道和平台优势，吸引新用户使用，提高活跃用户覆盖率。</li>
<li>计算16年全年平均月活比，管家：卫士=1.2:1；</li>
<li>2015年360卫士领先腾讯管家，但腾讯管家活跃用户量2016年增长迅猛，确保了安全领域第一用户活跃度。</li>
</ul>
<h3><strong>4.3 2017年市场预测</strong></h3>
<p>个人简单以当前的活跃人数环比变化和用户搜索指数兴趣分析</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/F8vIpbrioD6JnCiE6s10.jpg" width="607" height="353" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图像来源：易观APP排名，统计月活环比变化</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/Voa7qbZFcuAFVXdrXGzd.jpg" width="608" height="145" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图像来源：百度指数</p>
<ol>
<li>二者增长率波动较大，360手机卫士0-10%居多，腾讯管家增长率0-10%居多，但腾讯管家波峰和波谷均大于360卫士，曲线表现较好，所以腾讯手机管家增量总体上优于360手机卫士；</li>
<li>预计2017年二者的环比增长率以0—10%为主，但由于腾讯手机卫士活跃用户基数大，2017年腾讯手机管家将继续加大和360手机助手的用户量。</li>
</ol>
<h3><strong>4.4 功能数据</strong></h3>
<p>为了验证核心、主要功能的具体表现，本人在同一时刻对手机进行优化，查看清理数据，以及可发现的数据； 由于是工具类产品，没有某些功能的用户使用数据，无法通过用户表现进一步验证。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/ZsN4PSxOTNBTUehvmYyp.jpg" width="715" height="588" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">参考资料：360手机卫士《2016年中国手机安全状况报告》腾讯安全《2016年度互联网安全报告》</p>
<h3><strong>4.5 数据总结</strong></h3>
<p>大致查看了一些数据，我们把他们总结下：</p>
<p><strong>市场：</strong>360手机卫士的活跃用户在15年多于腾讯手机管家，但16年后被超越。</p>
<p><strong>用户表现：</strong> 对大众主流用户而言，二者工具性能更明显，用户没有关注欲望。但管家由于用户年轻化，更为活跃些。 腾讯手机管家的用户活跃度和参与度高于360手机卫士，无论是使用频率还是参与产品相关活动，如标记，论坛反馈信息等。推测腾讯管家用户群画像年轻，爱分享交流；</p>
<p><strong>渠道：</strong>腾讯利用自身qq平台优势吸引新用户使用，在其他应用市场渠道上也非常具有竞争力； 360的平台自身劣势，且用户接受信息的应用市场少；</p>
<p><strong>具体功能：</strong>360卫士骚扰拦截强于腾讯管家； 腾讯用户标记活跃度较高； 清理加速卫士更加彻底，但选择负荷大，腾讯清理更简洁方便； 管家对于qq、微信账号保护是360卫士没有的。</p>
<p><strong>预测：</strong>2017年腾讯手机管家将继续加大和360手机助手的活跃用户量，环比增长率以0—10%为主。</p>
<h3><strong>4.6 数据的总结与反思</strong></h3>
<p>个人找数据用的是“先假设，后验证”的方法，并且验证手法一定越多越好。之前做过一个报告，因为只看了一个数据，即360手机卫士的微博粉丝远远多于腾讯手机管家，就下了个卫士比管家用户活跃的错误结论，非常后悔。</p>
<p>由于本次测试产品没有用户使用数据，所以我想说下我自创的横向和纵向数据法。</p>
<p><strong>横向数据法：主要验证方法</strong></p>
<p><strong>1.几个产品横向对比数据。对同样的功能，根据用户数据表现，按照一个标准去划分阶级。这样查找的数据非常客观具体。目的是区分哪些产品某个功能做的好。比如下表。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/41ZEKFwWrlQqVOf2XlS8.jpg" alt width="648" height="128" referrerpolicy="no-referrer"></p>
<p>我根据贴吧的回帖数“100”为标准看数据表现，结果发现管家的质量比卫士高。再看论坛，我以评论“400”、最高数据等为标准，验证功能表现。</p>
<p><strong>2.某个产品各个功能的数据横向对比。根据用户数据验证核心、主要功能。</strong></p>
<p>比如经常性的清理加速使用人数日活卫士5000w，一键优化日活6000w，骚扰拦截3000w，那么一键优化>清理加速>骚扰拦截。（注：骚然拦截是重要非特别高频功能）</p>
<p><strong>纵向数据法：辅助验证方法</strong></p>
<ol>
<li>以某个产品的一些可能的主要功能为目标对象，分析它们的变化趋势，验证活跃度以及它们是否为重要功能。这样分析比较费时间，统计功能的数据，24h一统计，哪些活跃，哪些就是核心主要功能。</li>
<li>多个产品间，通过变化趋势，进一步验证哪些产品特定功能做得好。</li>
</ol>
<p>数据最客观，只有没看到的数据，没有查得完的数据，我从有态度的社区和APP评论下载量查看二者的数据，简单的总结出了一些粗糙的结论。</p>
<h2 id="toc-6">5. 功能</h2>
<h3><strong>5.1 需求分析</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/zsHAydvxj3FccvZCw565.jpg" width="562" height="286" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">数据来源：艾媒咨询报告</p>
<p>根据上图，我们按照kano模型来分析，可以得出如下脑图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/dXUXp7zrPBsNE9iRndtD.jpeg" alt width="710" height="938" referrerpolicy="no-referrer"></p>
<p>可以发现，调研报告中的手机安全，就是一些安全产品的基本需求。在做需求分析时，除了用户需要的基本功能外，还要考虑到用户未来的需求，在期望和兴奋型需求上做长远规划。对于360手机卫士和腾讯手机管家，由于产品定位明确，且为成熟期，所以对于要加入的创造功能，做好优先级划分，swot分析，避免臃肿。</p>
<h3><strong>5.2 任务分析图</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/YzRhuJwItnevjDKw3WpV.jpg" alt width="686" height="409" referrerpolicy="no-referrer"></p>
<p>根据调研数据、页面中的功能交互优先级、调查报告、应用评论，做出了如上图所示的两个产品的现阶段任务分析图，可以看到清理加速，流量监控，小火箭加速，一键优化等属于高频且重要功能点。</p>
<h3><strong>5.3 核心、主要功能</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/Sn7yBgccBcvqXU05AoTO.jpg" alt width="741" height="489" referrerpolicy="no-referrer"></p>
<p>核心、主要功能的界定，同样是根据调研数据（横向和纵向数据分析）、页面中的功能交互优先级、调查报告、应用评论等，主要参考点是用户使用规模、使用频率、对产品重要程度，以用户的角度为侧重点考察重要程度。</p>
<h3><strong>5.4 具体功能内容</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/sGpwnVBTQL9DV7Yyg04R.jpg" alt width="766" height="796" referrerpolicy="no-referrer"></p>
<h3><strong>5.5 功能价值曲线分析</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/BU2A3q0PDDDEQElfNr6J.jpg" alt width="595" height="448" referrerpolicy="no-referrer"></p>
<p>由图可得，二者各有优劣势：</p>
<ul>
<li>对于360手机卫士：总体得分4.7分 。曲线高的地方是产品的核心功能，没有明显弱势，表现良好；</li>
<li>对于腾讯手机管家：总体得分4.2分。 曲线高的地方为用户体验好的核心竞争力和核心功能，低的地方也很平均，表现良好；</li>
<li>曲线均为良性，均符合产品整体的竞争力，符合未来发展趋势。</li>
</ul>
<h3><strong>5.6 功能的总结与反思</strong></h3>
<p>结合功能和需求，我们再来看一看2个产品。</p>
<p>从功能上看，二者均是从基本功能起家，靠硬实力吸收用户，现阶段的功能，在强化基本功能基础上，还在做差异化的功能，试图找回新的用户增长点。</p>
<p>从需求上看，两个产品在用户基本需求能上都基本做到了极致，卫士比管家更全面、能力更突出。</p>
<p>两个产品均涉及了一部分未来的需求。360主要做的是“手机管理便利工具”、“全方位的安全连接”、管家主要做“生活场景化便利服务”。</p>
<p>这种“基本+未来”的挖掘需求方式非常好，既可避免产品不能用，又可以给用户带来兴奋感。难点在于如何挖掘创新需求，新需求的优先级，技术能力，以及和基本需求的融合方式（和老功能渗透在一起还是各立门户）。当然，这里有个度，避免功能冗杂，大而全，面面俱到。平衡点的拿捏是个非常困难的问题，这就需要根据产品当前的定位和优先级来界定了。</p>
<h2 id="toc-7">6. 用户</h2>
<h3><strong>6.1 核心、主流用户行为</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/n3dQSuGOButnWJtZNuV3.jpg" alt width="670" height="306" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/OTxSnn6uiGFe9xcieQAH.jpg" alt width="669" height="342" referrerpolicy="no-referrer"></p>
<p>核心主流用户群，最重要还是看粘性，我在这里根据用户行为，将具有这类行为的用户划分为为不同的用户群体。一般而言，主流用户群占比通常最多，但只会使用20%功能，通常为用完即走。核心用户群通常会因为付费、活动、品牌信仰等而使用更多的功能，并且粘性非常高。</p>
<h3><strong>6.2 用户构成</strong></h3>
<p>笔者通过前面的具体功能的数据验证，得到可能的大致构成比例；</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/JGfFGwrJswdemy63JmJp.jpg" alt width="637" height="289" referrerpolicy="no-referrer"></p>
<ul>
<li>从图中看出，腾讯手机管家核心用户群规模大，构成比例大于360卫士，活跃度高；360手机卫士pc时代留存老用户多，没有管家活跃；</li>
<li>腾讯手机管家和360手机卫士主流用户均当做安全工具使用，他们占用户总数中大部分；</li>
<li>腾讯的平台和渠道优势更加明显，更容易吸引未来用户。</li>
</ul>
<h3><strong>6.3 用户行为分析</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/DfUEMGgSiTIHW2ppMjhW.jpg" alt width="684" height="293" referrerpolicy="no-referrer"></p>
<p>管家和卫士的用户行为总体差异化不大，重合度高，这也是由于工具类产品特性决定的，同质化比较严重。</p>
<p>如果作为竞品，可以考虑如下方式挖掘用户。</p>
<ul>
<li>首先从使用基本功能的主流用户出发，只有两条路，在基本功能上加强实力或者创造新的需求撬动这部分用户，且要被用户感知到。</li>
<li>竞品的优势同时也是它的劣势，成为它定位转型发展，改变用户固有行为的桎梏，这就是创造新需求的强大力量。</li>
<li>但是，工具类产品在用户看来就是一个工具，安全的认知早已被pc版360安全卫士教育，很难改变用户心智模型。同时，操作流程是否繁琐，复杂，易用性，易懂性，认知负荷等，都会影响用户体验，所以新产品很难超越，被教育过的工具类产品很难做。</li>
<li>所以，我们不改基本功能，我们只从未来的需求做产品定位，结合我分析的5.1中的kano需求分析，在满足基本需求的前提下，在兴奋型需求中找其中一两项做到极致，试图打造爆款。虽然同属安全领域，然而创造的新需求会使用户不得不接受新产品，结果就显而易见了。</li>
<li>比如，新产品可从安全+社区，安全+个性化，安全+人工智能等等出发，某些强差异化功能可以当做DNA链接起整个产品，不只是产品功能的一个小部分，正如云音乐的歌单定位一样。安全社区的粘性，以及安全个性化，智能化给予主流用户使用。这是避免工具类产品用户行为同质化的方向。</li>
</ul>
<h3><strong>6.4 用户人口统计学特征</strong></h3>
<p>实在找不到最新的第三方报告，只有2015年的，见谅。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/zpzK0ofLVc8Sk6Jq951E.jpg" width="499" height="667" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">来源于：易观智库：《2015年第3季度中国手机安全市场》</p>
<p>我只选择了2个变量，没有选择性别、收入、地域、学历等其他的因子，因为个人觉得选择越多，人物就越复杂难懂，不清晰。应该选择年龄和手机使用习惯作为安全领域最重要的因子，但是手机使用习惯数据查找不到，所以以职业代替。</p>
<p>我们的目的是结合核心、主流用户行为，确立典型用户画像。</p>
<p>上图可以看到，管家的用户群有优势，他们比较年轻。</p>
<ol>
<li>90后，00后更符合未来的发展趋势，他们乐于分享，推荐给身边的朋友；</li>
<li>推荐给自己60后、70后的父母，父母的互联网使用频率，规模，技术较好。</li>
<li>未来的世界是年轻人主导的，抓住他们等于抓住了风口。</li>
</ol>
<h3><strong>6.5 用户画像</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/TGF5K5npBiRyk9wHRzRv.jpg" alt width="544" height="407" referrerpolicy="no-referrer"></p>
<p>上面的模型，对于建立和完善用户画像很重要，由于资料和能力匮乏，我主要通过某些方法来推测画像，各做了一个各产品特色用户画像（主流用户都是个体户、自由职业）。</p>
<p><strong>360手机卫士</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/YY6BtOVXrh5tr5sR7yWt.jpg" alt width="707" height="302" referrerpolicy="no-referrer"></p>
<p><strong>腾讯手机管家</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/hIWbxahkWa7ncL21QOXq.jpg" alt width="750" height="334" referrerpolicy="no-referrer"></p>
<h3><strong>6.6 用户总结</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/0kPaOTC5AIoTuRbVKVik.jpg" alt width="531" height="292" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/CatZvIuNdgx7Jvz7ZR7h.jpg" alt width="527" height="301" referrerpolicy="no-referrer"></p>
<p>结合上面的统计信息，我试图对用户质量进行打分，按照移动应用生命周期的AARRR模型，虽然这个属于移动应用用户运营，但是毕竟属于用户全周期。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/8SfDWeu04dZR4G2axXa9.jpg" alt width="507" height="320" referrerpolicy="no-referrer"></p>
<h3><strong>6.7 用户的总结与反思</strong></h3>
<p>结合数据，用户这部分最重要的还是用户获取渠道、活跃度和用户画像的初步建立。</p>
<p>一个完整的用户获取到留存应该是用户→渠道→产品→视觉→信息。其中个人理解的渠道是，应用市场、意见领袖、广告、口碑、社群、社交媒体、地推等，让用户知道产品的存在，根据渠道分析，鉴别带来大量优质用户注渠道做重点投放。从上面的分析中，腾讯霸占了应用市场的渠道优势，并且也曾经邀请金秀贤做广告，对年轻用户吸引力明显。</p>
<p>年轻人的活跃度肯定是最高的，管家的活跃人数高于卫士，跟他们的需求满足和用户体验不无关系。</p>
<p>用户画像我认为是非常重要形象具体理解目标用户的，就像隔壁老王一样大家都知道他是男人的克星画像。我在上面做的是“行为、观点”和“人口统计学”，主观+客观。最后再加上一个典型场景化，把人物做活，这样盯着照片就能想象到他是什么人。</p>
<h2 id="toc-8">7. 架构与流程</h2>
<h3><strong>7.1 架构</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/9aZJ9KVyxvzVj4CCZyG6.jpeg" alt width="696" height="708" referrerpolicy="no-referrer"></p>
<p>卫士的信息架构总体窄而浅。一级架构非常简单。 但是“卫士”的下层又是宽而浅的架构，使得整个架构在二级及以下的地方比较宽，带来认知和操作负荷，效率降低； “我”的领域跨度很大，是广而深的架构。整个产品架构显得有些臃肿。</p>
<p>打分：4分</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/PBmMYrKJyRAyePLmLVR3.jpeg" alt width="679" height="500" referrerpolicy="no-referrer"></p>
<p>管家的信息架构总体广而浅。架构在一级的地方非常宽，主要信息全部呈献给用户，容易找到想要的功能，但这会对用户主入口产生认知干扰以及操作的繁杂； 且二级的地方却比较浅显，易学性高，容易找到。 整个产品架构简单明了，方便用户操作与认知。</p>
<p>打分：4.5分</p>
<h3><strong>7.2 用户典型流程</strong></h3>
<p>赋予一个场景：小A使用的是360手机卫士，小B使用的是腾讯手机管家；有一天，他们碰面了…</p>
<p>7.2.1 他们玩着手机，觉得手机发热，卡，于是想到了清理垃圾提速…</p>
<p>小A：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/YyNPY1LCa6FBHrUstKCD.jpg" alt width="749" height="101" referrerpolicy="no-referrer">小B：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/RRP40BOdnOYYRXcE2qZN.jpg" alt width="731" height="103" referrerpolicy="no-referrer"></p>
<p>可以看到，小A和小B的操作路径几乎一致。流程简短，操作2步即完成，且具有明显操作反馈，操作顺畅； 二者可均给5分。</p>
<p>7.2.2 他们接收电话，短信。发现是骚扰电话，垃圾短信，于是想要举报…</p>
<p>小A：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/rbInsy8ciE7rXrurENUf.jpg" alt width="664" height="130" referrerpolicy="no-referrer"></p>
<p>小B：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/C7kkj8WP9Gi2YezZDiRL.jpg" alt width="635" height="125" referrerpolicy="no-referrer"></p>
<p>可以看到，小A和小B的举报骚扰电话和垃圾短信的操作流程同样非常简短，流程基本一致。二者均可给5分；工具类产品的流程设计非常重要，十分追求速度效率。因为这就是工具，只有在我有困难的场景中我才想起你。</p>
<h3><strong>7.3 架构流程总结与反思</strong></h3>
<p>笔者认为产品架构是一个产品承上启下的信息连接器，同时也是用户看到和看不到的分界线。学习新产品，一定要先从架构画起。由于产品简单，我在这里做的架构的颗粒度比较小，比较细。如果再细化，甚至可以把页面上一个细节，甚至交互动作都写进架构。</p>
<p>从需求到功能的设计，正是由产品需求架构到功能架构逐步完善的过程，由大到小，最终还是梳理出要做上线的功能点。</p>
<p>用户流程图做的是典型操作，不是业务流程图那样面面俱到。好多需求的来源其实都是从用户流程中来的，我举个栗子。直播的简单流程：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/8KFKtd9jf3Bkc9ix47uk.jpg" alt width="712" height="209" referrerpolicy="no-referrer"></p>
<p>根据主流用户到达直播间的流程不同，场景化模拟用户。挖掘最基本需求，由大到小不断细分，这样才会打造高效率，短路径的用户流程。像卫士和管家这种工具产品，基本功能的流程效率更重要，因为只有在我有困难的危急时刻，我才会想起你，使用你。这点上二者都做的很棒。</p>
<h2 id="toc-9">8. 信息设计</h2>
<h3><strong>8.1 框架层</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/hRjOndgaKOAyIamlgYUE.jpg" width="559" height="320" referrerpolicy="no-referrer"></p>
<p>注：仅针对主要页面讨论框架</p>
<p>可以发现：</p>
<ul>
<li>卫士运用了4种框架形式处理信息，3个一级页面；而管家只用了2种，1个一级页面以列表式为主；所以管家的结构统一性是最好的，易学性也占优势；</li>
<li>信息处理上，由于功能全面，卫士处理的信息更多，管家在信息的简约易学性上更占据优势。</li>
</ul>
<h3><strong>8.2 信息设计汇总</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/bFCoMHPzqBjGaCukmp1K.jpg" alt width="694" height="561" referrerpolicy="no-referrer"></p>
<p>对信息设计打分，结果360手机卫士4.5分，腾讯手机管家5.0分；</p>
<h3><strong>8.3 信息承载力</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/9qNmtTGq2UsSCAAlivcZ.jpg" alt width="691" height="283" referrerpolicy="no-referrer"></p>
<p>我们分析一级界面，观察一个界面的信息承载力。</p>
<p>腾讯手机管家共显示5个功能和一个隐藏功能。占据页面空间大概1/3；360手机卫士的5大核心功能彻底覆盖了“卫士”页面，工具也是占据了“工具箱”的绝大多数空间，其他信息也全部覆盖了“我”。</p>
<p>并且二者对于核心的功能都在区位和大小上突出呈现，留白更加突出信息本质。管家的操作负荷较大，而卫士的认知负荷较大。</p>
<h3><strong>8.4 信息的总结与反思</strong></h3>
<p>以上4个“友好性、易懂、易用性、一致性”是笔者自己总结的，我所列的只是信息分析方法。一个界面的信息无非是认知和操作两种，通常首先框架结构处理信息，然后通过对比、统一、分组等完善信息。宗旨就是信息的传递，不要有干扰。</p>
<p>360卫士和腾讯管家信息设计都以突出信息简约为主，没有明显干扰信息传递效率的问题出现。页面承载力的影响也和信息处于平衡之中。</p>
<h2 id="toc-10">9. 视觉设计</h2>
<h3><strong>9.1 视觉设计</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/KSVQacj07DAdavViA1n5.jpg" alt width="580" height="459" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/MTUqi5RKMTa0hp7PIpME.jpg" alt width="721" height="295" referrerpolicy="no-referrer"></p>
<h3><strong>9.2 视觉吸引性</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/0qmscaFRvUVh6kEBP4G9.jpg" alt width="693" height="409" referrerpolicy="no-referrer"></p>
<p>总体打分：360手机卫士 4.5分，腾讯手机管家 5分</p>
<h3><strong>9.3 视觉总结与反思</strong></h3>
<p>视觉的目的就是一种氛围的沉浸感，它不应该干扰信息的传递，即使是图片、动画也要和产品定位一致。我们会发现360手机卫士和腾讯手机管家视觉很简洁明确，一致性突出产品的安全定位主题。也正是这种沉浸的氛围，使用户接触产品的前10秒钟，产生稳定的美感。</p>
<h2 id="toc-11">10. 总结</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/03/Xwc1PxOdBI2A1khev5SH.jpg" width="484" height="473" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">总体特征雷达图</p>
<h3><strong>10.1 核心竞争力</strong></h3>
<p>卫士：<strong>安全功能</strong>上最具竞争力，这正符合360手机卫士的定位；</p>
<p>管家：用户、信息架构、信息设计、视觉，处于优势。<strong>用户体验和渠道</strong>为核心竞争力，这正符合管家的定位“青春、酷”。</p>
<h3><strong>10.2 总体建议</strong></h3>
<p>从图中可以看到，360手机卫士和腾讯手机管家总体各项评分均在4分以上，二者总体接近，具有市场竞争力；</p>
<p>如果有新产品，要在灰色区域全覆盖。 在用户质量、信息架构、视觉设计上挑战360手机卫士； 在功能上挑战腾讯手机管家。</p>
<p>同时结合上文提到的商业模式、需求、渠道、流程、信息设计、视觉的一些建议，认真理解用户，才可以做到知己知彼，百战不殆；以己之长，攻彼之短。</p>
<p>如果你对这篇文章有建议或者意见，非常欢迎留言讨论，个人观点还不成熟，虚心求教。本人还有其他关于产品和生活的独特思维，希望和大家分享，谢谢~</p>
<p> </p>
<p>作者：张绍琰，微信号：shao_yan 1992。一个酷爱思考，观察生活，有梦想的产品新人。本科主修建筑设计，15届毕业生。对于产品设计非常感兴趣，目前离职，期待一份北京产品经理的岗位。</p>
<p>本文由 @张绍琰 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="595625" data-author="153083" data-avatar="http://image.woshipm.com/wp-files/2017/03/lMe0ARnZ3Kb3STzcELKv.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">3人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_201911_20191125142632_8277.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_201703_20170306150634_2343.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/WD_U_201607_20160728120307_6016.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            
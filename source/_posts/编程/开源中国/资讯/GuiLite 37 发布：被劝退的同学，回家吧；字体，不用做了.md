
---
title: 'GuiLite 3.7 发布：被劝退的同学，回家吧；字体，不用做了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-14d104afca2fc81169c15105982cc9a4e5e.gif'
author: 开源中国
comments: false
date: Wed, 31 Mar 2021 10:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-14d104afca2fc81169c15105982cc9a4e5e.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>问题：你被GuiLite劝退的主要原因？</h2> 
<p>根据开发群同学的反馈，特别是精英开发者直面不讳的批评，我们发现被劝退的主要原因是：不支持freetype！</p> 
<p>先看看在以前的字体开发流程下，开发者是如何被劝退的吧：</p> 
<p>1. 使用字体工具做字体的cpp文件</p> 
<p>2. 将cpp文件加入到工程中编译</p> 
<p>3. 运行后，发现字体大小有点不合适，重复步骤1，2，3</p> 
<p>4. 再运行，发现有些字的点阵是缺失的，需要加上；于是再重复步骤1，2，3</p> 
<p>所以，开发者至少需要做6个步骤，才能在程序显示出一个初步的字体。开发者，太南了~~</p> 
<p>可能有的同学认为：单片机开发，为了最小的占用资源，以上的步骤是不可避免的。诚然，GuiLite最初的单片机开发者众多，这些琐事，大部分同学是司空见惯的。但最近一年来，我们的统计显示Windows，Linux开发者增长的非常快。如此繁琐的字体制作流程，完全是在赶人。</p> 
<h2>行动：支持freetype</h2> 
<p>为了与流行的TTF字体接轨，我们选择了支持freetype，都是开源项目，用起来格外亲切；根据GuiLite的一贯作风，精简代码是第一需求，编译100%通过是基本标准。操作上面，我们通过一个100行的文件对freetype进行了接口上面的适配。具体使用方法可以参看HelloFreetype这个demo。经过这些操作后，大家以后开发字体的流程是这样的：</p> 
<p>1. 加入你中意的TTF字体文件到工程里面</p> 
<p>2. 通过你熟悉的draw_string绘制各个国家的任意文字</p> 
<p>3. 调整文字大小，可以直接在代码中调整</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-14d104afca2fc81169c15105982cc9a4e5e.gif" referrerpolicy="no-referrer"></p> 
<p>当然，该功能可能在某些单片机环境无法使用，毕竟freetype本身也需要几兆的空间。目前的主要受益者是Windows，Linux开发者。其实，群主也很好奇，大家用GuiLite在Windows，Linux上面都在开发什么应用程序呢？请知道的同学，在下面留言回复我一下，谢谢！</p> 
<h2>我不喜欢freetype，我要用其他字体库</h2> 
<p>请放心，这次我们还重构了c_word，使其支持灵活扩展其他字体方案（相信利用C++的继承机制，新增代码应该在100行以内），还是参考HelloFreetype\UIcode\freetype_operator.h代码，在相关函数里面适配你一下你喜欢的字体库就好。</p> 
<h2>接下来的工作：</h2> 
<ol> 
 <li>跟踪freetype的使用状况，积极处理发现的任何问题</li> 
 <li>仿照加载TTF字体文件的方法，即将支持图片的直接加载、显示</li> 
 <li>继续收集开发者的反馈，您的每一次反馈，都是GuiLite难得的进步机会</li> 
</ol> 
<p> 最后，跟大家分享一下GuiLite IoT项目给我们带来的全球开发者统计图，再次感谢大家的支持；世界不能缺少中国力量，加油，奥利给💪</p> 
<p>全球开发者分布图：</p> 
<p><img alt height="797" src="https://oscimg.oschina.net/oscnet/up-5f6eac8039a28c345b979200c5de5ccbad0.png" width="1935" referrerpolicy="no-referrer"></p> 
<p>运行GuiLite的设备分布图</p> 
<p><img alt height="524" src="https://oscimg.oschina.net/oscnet/up-2a973ba9f18bbb40f3998113d8a10a9467b.png" width="1161" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            
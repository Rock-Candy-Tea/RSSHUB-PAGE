
---
title: 'LiteFlow 深度和 IDEA 结合，发布 IDEA 插件，规则编排如虎添翼！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d9af0cc0af16d1c99421fb176fc8ba1bc59.jpg'
author: 开源中国
comments: false
date: Wed, 18 May 2022 02:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d9af0cc0af16d1c99421fb176fc8ba1bc59.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img height="383" src="https://oscimg.oschina.net/oscnet/up-d9af0cc0af16d1c99421fb176fc8ba1bc59.jpg" width="900" referrerpolicy="no-referrer"></p> 
<h2>前言</h2> 
<p>LiteFlow今天正式发布IDEA插件LiteFlowX！</p> 
<p>这款IDEA插件能深度和LiteFlow规则文件结合，能够方便的在IDEA进行跳转，定位组件。极大的弥补了LiteFlow的规则文件不能很好的定位代码的问题！</p> 
<p>先简单介绍下LiteFlow框架：</p> 
<p>LiteFlow框架是一个Java领域小而美的开源规则编排引擎，在2020年开源，到目前为止迭代了36个版本，有日益庞大的社区和众多使用者，如你想了解这款开源引擎，可以移步官网，强大的文档让你快速上手：</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2F" target="_blank">https://liteflow.yomahub.com/</a></p> 
</blockquote> 
<p>我虽然是LiteFlow框架的作者，但是这款插件却并不是出自我手，是出自一个非常有才的群友小易，也是LiteFlow框架的使用者之一，感谢他为LiteFlow框架做了这么一款插件，为开源精神狂赞！</p> 
<p><img alt src="https://www.oschina.net/news/196268/images/1.png" referrerpolicy="no-referrer"></p> 
<p><img height="770" src="https://oscimg.oschina.net/oscnet/up-c801bef4139fe7912283e9e2fa8aadb96bd.png" width="1068" referrerpolicy="no-referrer"></p> 
<h2>审核过程中的一个趣事</h2> 
<p>小易同学和我说了开发计划后，我就很看好。没想到一周后，就给我看了样品。并且表示已经提交Jetbrains Marketplace了。</p> 
<p>在等审核的过程中，还发生一件啼笑皆非的趣事。</p> 
<p>大概在发文的前一天下午，小易同学找到我说，插件审核请求被驳回了。理由十分让我们哭笑不得，大家请看图：</p> 
<p><img height="323" src="https://oscimg.oschina.net/oscnet/up-353a6b4dd3b0f42585ca84b76c64b335712.png" width="1258" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://www.oschina.net/news/196268/images/2.png" referrerpolicy="no-referrer"></p> 
<p>小易同学使用了LiteFlow的LOGO作为插件的ICON，但是JetBrains那边表示，这图标有点像"那脆"标志(谐音自己体会)，这会让有些用户觉得不舒服。。。。</p> 
<p>我就想问，这LOGO怎么看都是个风车，怎么就和XX扯上了呢。。</p> 
<p><img alt src="https://www.oschina.net/news/196268/images/3.png" referrerpolicy="no-referrer"></p> 
<p><img height="1180" src="https://oscimg.oschina.net/oscnet/up-1718fa5667412b210301c77d5c618c8e2bf.png" width="2628" referrerpolicy="no-referrer"></p> 
<p>这是逼我要换LOGO吗。</p> 
<p>最后不得以，只能对LOGO进行了一些简单的变形，重新提交审核。</p> 
<h2>如何安装</h2> 
<p>以上是审核期间一个趣事，我就顺便记录下来了。</p> 
<p>目前插件已经发到了插件市场，不过目前发布的是alpha版本的，如果直接在IDEA的Marketplace上搜是搜不到的，要添加一下Marketplace的Alpha Channel才能搜到。</p> 
<p><img alt src="https://www.oschina.net/news/196268/images/4.png" referrerpolicy="no-referrer"></p> 
<p><img height="1414" src="https://oscimg.oschina.net/oscnet/up-f46a1471dc6241bc5ba7a9c8d20758240a5.png" width="1948" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://www.oschina.net/news/196268/images/5.png" referrerpolicy="no-referrer"></p> 
<p><img height="468" src="https://oscimg.oschina.net/oscnet/up-f8c045402aeb16a1574f52af3c52f38d742.png" width="980" referrerpolicy="no-referrer"></p> 
<p>新增以下链接：</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugins%2Falpha%2Flist" target="_blank">https://plugins.jetbrains.com/plugins/alpha/list</a></p> 
</blockquote> 
<p>添加后，搜索<code>LiteFlowX</code>，就会出现LiteFLow插件：</p> 
<p><img height="1424" src="https://oscimg.oschina.net/oscnet/up-12706a33390ae8b10afc35b01ee6ee0b686.png" width="1964" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://www.oschina.net/news/196268/images/6.png" referrerpolicy="no-referrer"></p> 
<h2>如何使用</h2> 
<p>安装了插件之后，再回到规则文件里。就可以看到规则里有了一些变化：</p> 
<p><img height="1566" src="https://oscimg.oschina.net/oscnet/up-3240806c0ab229a854e2351409a788f8db0.png" width="2284" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://www.oschina.net/news/196268/images/7.png" referrerpolicy="no-referrer"></p> 
<p>各个图标解释下：</p> 
<ul> 
 <li> <p>文件图标跳转组件的定义类(如果你的Node是定义在规则内)</p> </li> 
 <li> <p>红色跳转组件的定义类</p> </li> 
 <li> <p>绿色跳转Chain的定义处</p> </li> 
 <li> <p>紫色跳转Node的定义(如果你的Node是定义在规则内)</p> </li> 
</ul> 
<p>LiteFlow支持三种配置格式，xml/json/yml。</p> 
<p>这款插件目前对xml和json有支持，yml格式的暂时还没支持哦。</p> 
<h2>最后</h2> 
<p>这款插件也是开源的，在这里放上这款插件的开源仓库地址，大家去点star哦。</p> 
<blockquote> 
 <p>Gitee：<a href="https://gitee.com/liupeiqiang/LiteFlowX">https://gitee.com/liupeiqiang/LiteFlowX</a> Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCoder-XiaoYi%2FLiteFlowX" target="_blank">https://github.com/Coder-XiaoYi/LiteFlowX</a></p> 
</blockquote> 
<p>众人拾材火焰高，开源精神每个人都可以有，这样开源项目才能变的越来越好，感谢这位兄弟为LiteFlow所做的贡献。如果大家正在学习和使用LiteFlow，可以按文中的方法去下载插件使用看看。</p>
                                        </div>
                                      
</div>
            
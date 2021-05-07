
---
title: 'Django简介、ORM、核心模块'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cfef269f507457aa4d7cf7ba877de2f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 00:32:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cfef269f507457aa4d7cf7ba877de2f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Django简介</h1>
<p>    Django是一种开源的大而且全的Web应用框架，是由python语言来编写的。他采用了MVC模式，什么是MVC？大家不要着急，MVC这么好的东西我在下面会精细的讲一下！Django最初是被开发来用于管理劳伦斯出版集团下的一些以新闻为主内容的网站。一款CMS（内容管理系统）软件。并于 2005 年 7 月在 BSD 许可证下发布。这套框架是以比利时的吉普赛爵士吉他手 Django Reinhardt 来命名的。</p>
<h1 data-id="heading-1">Django版本</h1>
<p>至今Django版本已经更新到Django3.0.5，官网下载https://www.djangoproject.com/download/</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cfef269f507457aa4d7cf7ba877de2f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Django最新版本</p>
<p>说到Django版本不得不提及python版本，Python3.8 的热乎劲还没过去，Python 就又双叒叕要更新了。近日，3.9 版本（<a href="https://www.python.org/downloads/release/python-390a4/%EF%BC%89%E7%9A%84%E7%AC%AC%E5%9B%9B%E4%B8%AA" target="_blank" rel="nofollow noopener noreferrer">www.python.org/downloads/r…</a> alpha 版已经开源。从文档中，我们可以看到官方透露的对 dict、math 等组件增加的新特性，以及下一步的开发进展。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b11004f11822454388edc097c21af572~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Python最新版本</p>
<h1 data-id="heading-2">Django优点</h1>
<p><strong>强大的数据库功能</strong></p>
<p>    用 python 的类继承，几行代码就可以拥有一个丰富、动态的数据库操作接口（API），如果需要，你也能执行 SQL 语句<strong>ORM</strong>（Object-Relational Mapping“对象-关系-映射”），它实现了数据模型与数据库的<strong>解耦</strong>，即数据模型的设计不需要依赖于特定的数据库，通过简单的配置就可以轻松更换数据库</p>
<p><strong>自带强大的后台功能</strong></p>
<p>    在admin.py中写入需要实现功能的代码，几行简单的代码就可以实现你当管理员的梦。再也不用为设计管理员而发愁了！</p>
<p><strong>优雅的网址</strong></p>
<p>    在urls.py中用正则匹配网址，传递到对应的函数，随意你自己定义，网址可以如你所想，如你所愿。 <strong>(需要注意的是:正则是一种独立的语法，并不是哪个语言所拥有的。)</strong></p>
<p><strong>具有模板系统</strong></p>
<p>    模板系统大大的降低了开发者头疼脑热的概率。因为模板系统设计简单，容易扩展。代码，样式分开设计。查找更清晰，修改更容易！</p>
<p><strong>缓存系统</strong></p>
<p>    Django和memcached、redis或者其他的缓存系统联用，提高了页面的加载速度。让用户的体验度更好了！</p>
<p>templates 文件夹views.py 中的函数渲染 templates 中的 Html 模板，得到动态内容的网页，当然可以用缓存来提高速度。</p>
<p><strong>国际化</strong></p>
<p>    这么好的东西，想不走上国际化都难啊。想要网页显示不同语言，比如中文、英文、还有各种语言。只需要在一个文件的设置中稍微那么修改一下。页面就会穿上各种语言的外衣。</p>
<p><strong>Django 的 App 理念很好。</strong></p>
<p>    App 可插拔，是不可多得的思想。不需要了，可以直接删除，对系统影响不大。</p>
<p>怎么样？Django是否强大到不可想象的地步了？不过大家也不用高兴的太早了。因为代码还是要写的，只不过用上了Django开发网站的时候更快速，更便捷了而已！</p>
<h1 data-id="heading-3">Django具有以下特点：</h1>
<ul>
<li>功能完善、要素齐全：该有的、可以没有的都有，常用的、不常用的工具都用。Django提供了大量的特性和工具，无须你自己定义、组合、增删及修改。但是，在有些人眼里这被认为是‘臃肿’不够灵活，发挥不了程序员的主动能力。（一体机和DIY你更喜欢哪个？^-^）</li>
<li>完善的文档：经过十多年的发展和完善，Django有广泛的实践经验和完善的在线文档（可惜大多数为英文）。开发者遇到问题时可以搜索在线文档寻求解决方案。</li>
<li>强大的数据库访问组件：Django的Model层自带数据库ORM组件，使得开发者无须学习其他数据库访问技术（SQL、pymysql、SQLALchemy等）。当然你也可以不用Django自带的ORM，而是使用其它访问技术，比如SQLALchemy。</li>
<li>灵活的URL映射：Django使用正则表达式管理URL映射，灵活性高。</li>
<li>丰富的Template模板语言：类似jinjia模板语言，不但原生功能丰富，还可以自定义模板标签。</li>
<li>自带免费的后台管理系统：只需要通过简单的几行配置和代码就可以实现一个完整的后台数据管理控制平台。</li>
<li>完整的错误信息提示：在开发调试过程中如果出现运行错误或者异常，Django可以提供非常完整的错误信息帮助定位问题。</li>
</ul>
<h1 data-id="heading-4">好了，开始正式跟大家说MVC 、MVT、ORM</h1>
<p>大部分开发语言中都有 MVC</p>
<p>MVC 框架的核心思想是： 解耦.即数据模型的设计不需要依赖于特定的数据库，通过简单的配置就可以轻松更换数据库</p>
<p>降低各功能模块之间的耦合性，方便变更，更容易重构代码，最大程度上实现代码的重用</p>
<p>M 表示 model，主要用于对数据库层的封装</p>
<p>V 表示 view，用于向用户展示结果</p>
<p>C 表示 controller，是核心，用于处理请求、获取数据、返回结果</p>
<p>M代表的是模型(Model), V代表的是视图(View), C代表的是控制(Contrle)</p>
<p><strong>MVT</strong></p>
<p>Django 是一款 python 的 Web 开发框架</p>
<p>与 MVC 有所不同，属于 MVT 框架(是不是跟没说一样？不过我真的找不到更合适的语句了)</p>
<p>M 表示 model，负责与数据库交互</p>
<p>V 表示 view，是核心，负责接收请求、获取数据、返回结果</p>
<p>T 表示 template，负责呈现内容到浏览器</p>
<p><strong>什么是ORM？</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c494be9511943d7b030884996f788f3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>给大家一个图吧:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6faf3ad9ad747abbc10acce8f844661~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>最后在给大家说一下Django中的核心模块：在坚持一下就看完了</p>
<h1 data-id="heading-5">Django核心模块</h1>
<p><strong>urls.py</strong></p>
<p>网址入口，关联到对应的 views.py 中的一个函数（或者 generic 类），访问网址就对应一个函数。小心在设置函数的时候写错单词哦！</p>
<p><strong>views.py</strong></p>
<p>处理用户发出的请求，从 urls.py 中对应过来, 通过渲染 templates 中的网页可以将一些想要看到的内容输入到网页上。</p>
<p><strong>models.py</strong></p>
<p>与数据库操作相关，存入或读取数据时用到这个，当然用不到数据库的时候 你可以不使用。</p>
<p><strong>forms.py</strong></p>
<p>表单，用户在浏览器上输入数据提交，对数据的验证工作以及输入框的生成等工作。</p>
<p><strong>templates 文件夹</strong></p>
<p>views.py 中的函数渲染 templates 中的 Html 模板，得到动态内容的网页，当然可以用缓存来提高速度。这么好的东西，不用确实可惜！</p>
<p><strong>admin.py</strong></p>
<p>后台，这个就是可以用很少代码就能实现后台管理的神奇东东</p>
<p><strong>settings.py</strong></p>
<p>Django 的设置，配置文件，比如 DEBUG 的开关，静态文件的位置等。</p>
<h1 data-id="heading-6">结语</h1>
<p>总之，Django的功能很强大，包括DRF等一些框架，要学的还有很多，一起加油哇</p></div>  
</div>
            
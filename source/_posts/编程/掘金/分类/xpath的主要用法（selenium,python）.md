
---
title: 'xpath的主要用法（selenium,python）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/653285bbe64c4ed19e93fd1a7485d04e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 19:08:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/653285bbe64c4ed19e93fd1a7485d04e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看<a href="https://juejin.cn/post/6967194882926444557" target="_blank">：更文挑战</a></p>
<h5 data-id="heading-0">python爬虫或者自动化时xpath的应用</h5>
<h5 data-id="heading-1">不管是在进行爬虫或者浏览器自动化时我们首先要进行元素的获取，而xpath则是一种非常高效的手段</h5>
<p>首先来进行xpath的概念说明：
xpath是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。简单的意思就是说xpath是从一段xml文档中根据节点属性来查找具体的元素。
而html和xml 都是标记语言，都是基于文本编辑和修改的。所以xpath也可用于在html语言中获取信息</p>
<h5 data-id="heading-2"><strong>xpath主要语法</strong></h5>
<ol>
<li>
<p>一个正斜杠（/）和两个正斜杠（//）</p>
<p>在获取元素时一个斜杠'/'代表了从整个文档的根节点开始</p>
<p>比如/html/body/div/ul/li[1] 这个【1】相当于从数组中元素的下标</p>
</li>
<li>
<p>两个斜杠代表了从文档中匹配到的当前节点开始</p>
<p>比如"//div[@class = 'table-con']/ul/li[3]/input"而不用从根节点html开始</p>
</li>
<li>
<p>'@'表达式代表选取属性 比如href class id 等</p>
</li>
</ol>
<p>实例：
下图是我在项目中的xpath获取
获取一个inPut输入框的节点进行操作
首先找到他的父节点 看是否唯一如果唯一直接使用相对路径//进行开始
在控制台进行xpath语法的验证</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
Start --> Stop
</code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/653285bbe64c4ed19e93fd1a7485d04e~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-06-18_10-15-21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">xpath几个常用的函数</h5>
<ol>
<li>contains ()： //div[contains(@id,'in')] ,表示选择id中包含有’in’的div节点</li>
<li>text()：由于一个节点的文本值不属于属性，比如'<a class="”baidu“" href="https://juejin.cn/post/undefined">baidu</a>',所以，用text()函数来匹配节点：//a[text()='baidu']</li>
<li>starts-with()： //div[starts-with(@id,'in')] ，表示选择以’in’开头的id属性的div节点</li>
<li>not()函数，表示否定，//input[@name=‘identity’ and not(contains(@class,‘a’))] ，表示匹配出name为identity并且class的值中不包含a的input节点。写法如下：//input[@id]，如果我们要匹配出input节点不含用id属性的，则为：//input[not(@id)]</li>
</ol>
<p><strong>xpath 轴目前未使用到 以后若有使用再来进行补全</strong></p></div>  
</div>
            

---
title: 'DOM 简介及相关API'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0039cfa3c05642b9b0ec8617766adf9e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 22:58:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0039cfa3c05642b9b0ec8617766adf9e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、什么是 DOM</h3>
<p>文档对象模型（Document Object Model，简称 DOM），是 W3C 组织推荐的处理可扩展标记语言（HTML或者XML）的标准编程接口。
W3C 已经定义了一系列的 DOM 接口，通过这些 DOM 接口可以改变网页的内容、结构和样式。</p>
<h3 data-id="heading-1">二、DOM 树</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0039cfa3c05642b9b0ec8617766adf9e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"> 文档：一个页面就是一个文档，DOM 中使用 document 表示
 元素：页面中的所有标签都是元素，DOM 中使用 element 表示
 节点：网页中的所有内容都是节点（标签、属性、文本、注释等），DOM 中使用 node 表示
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DOM 把以上内容都看做是对象</p>
<h3 data-id="heading-2">三、获取页面元素</h3>
<p>DOM在我们实际开发中主要用来操作元素。获取页面中的元素可以使用以下几种方式:</p>
<h4 data-id="heading-3">1、根据 ID 获取</h4>
<p>使用 <code>getElementById()</code> 方法可以获取带有 ID 的元素对象。</p>
<pre><code class="copyable">document.getElementById('id');

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>console.dir()</code> 可以打印我们获取的元素对象，更好的查看对象里面的属性和方法。</p>
<h4 data-id="heading-4">2、根据标签名获取</h4>
<p>使用 <code>getElementsByTagName() </code>方法可以返回带有指定标签名的对象的集合。</p>
<pre><code class="copyable">document.getElementsByTagName('标签名');

<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：
(1)因为得到的是一个对象的集合，所以我们想要操作里面的元素就需要遍历。
(2)得到元素对象是动态的
(3)如果获取不到元素,则返回为空的伪数组(因为获取不到对象)
还可以使用<code>getElementsByTagName</code>获取某个元素(父元素)内部所有指定标签名的子元素,但父元素必须是单个对象(必须指明是哪一个元素对象). 获取的时候不包括父元素自己。</p>
<pre><code class="copyable"><div id="demo">
  <ul>
    <li>hello</li>
  </ul>
  <ol>
    <li>你好</li>
  </ol>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如获取以上<code>ul</code>中的<code>li</code>，我们可以这样</p>
<pre><code class="copyable">var ul=document.geElementById("demo");//获取到父元素
var li=ul.getElementsByTagName("li");//再获取父元素下面所有的li
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3、通过 HTML5 新增的方法获取</h4>
<pre><code class="copyable">1. document.getElementsByClassName(‘类名’)；// 根据类名返回元素对象集合
2. document.querySelector('选择器');        // 根据指定选择器返回第一个元素对象
3. document.querySelectorAll('选择器');     // 根据指定选择器返回所有元素对象集合
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="copyable"><body>
    <div class="box">盒子1</div>
    <div class="box">盒子2</div>
    <div id="nav">
        <ul>
            <li>首页</li>
            <li>产品</li>
        </ul>
    </div>
    <script>
        // 1. getElementsByClassName 根据类名获得某些元素集合
        var boxs = document.getElementsByClassName('box');

        // 2. querySelector 返回指定选择器的第一个元素对象  切记 里面的选择器需要加符号 .box  #nav
        var firstBox = document.querySelector('.box');

        // 3. 获取id为nav的第一个元素
        var nav = document.querySelector('#nav');

        // 4. querySelectorAll()返回指定选择器的所有元素对象集合
        var allBox = document.querySelectorAll('.box');

        // 5. 获取第一个li标签
        var li = document.querySelector('li');
 
        // 6. 获取所有li标签
        var lis = document.querySelectorAll('li');

    </script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注意：</code></p>
<p><code>querySelector</code> 和 <code>querySelectorAll</code>里面的选择器需要加符号,比如:<code>document.querySelector('#nav')</code>;</p>
<h4 data-id="heading-6">4、特殊元素获取（body，html）</h4>
<pre><code class="copyable">1. doucumnet.body  // 返回body元素对象
2. document.documentElement  // 返回html元素对象
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            
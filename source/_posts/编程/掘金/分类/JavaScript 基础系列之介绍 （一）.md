
---
title: 'JavaScript 基础系列之介绍 （一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26af24272d2f4f64bd889328d3bbd718~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 02:01:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26af24272d2f4f64bd889328d3bbd718~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">简介</h3>
<p>JavaScript <strong>解释型</strong>或<strong>即时编译型</strong>的编程语言。是属于 HTML 和 Web 的编程语言。</p>
<p>JavaScript 是 web 开发者必学的三种语言之一：</p>
<ul>
<li><em>HTML</em> 网页的内容</li>
<li><em>CSS</em> 网页的布局</li>
<li><em>JavaScript</em> 对网页行为进行编程</li>
</ul>
<h3 data-id="heading-1">使用</h3>
<h5 data-id="heading-2">script 标签</h5>
<pre><code class="copyable">JavaScript 代码必须位于<script></script>标签内。<script></script>标签可放置与HML中的head、body中
属性有：src(外部引入)、type
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><!DOCTYPE html>
<html>
  <head>
    <title>Hello JavaScript</title>
  </head>

  <body>
    <h5 id="title">JavaScript</h5>
    <button type="button" onclick="setTitle()">改变title内容</button>
    
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
      function setTitle() &#123;
        document.getElementById("title").innerText = "Hello JavaScript";
      &#125;
    </script>
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">输出</h3>
<pre><code class="copyable">// 写入警告
window.alert()

// 写入HTNL输出
doucment.write()

// 写入HTML元素
innerHtml

// 写入浏览器控制台
console.log()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">注释</h3>
<ul>
<li>单行注释 <code>//</code> 开头，任何位于 <code>//</code>与行尾之间的js代码都会被注释；</li>
<li>多行注释 <code>/* </code>开始， <code>*/</code> 结尾。任何位于<code>/* </code>与 <code>*/</code> 之间的js代码都会被注释。</li>
</ul>
<h3 data-id="heading-5">变量</h3>
<p>JS 的变量是用来存储数据值的容器。</p>
<p>使用 <code>var</code> 声明变量，以 <code>;</code> 结束。如果声明变量不赋值，那么该变量为<code>undefined</code>。
重复声明同一变量，如果不赋值，返回该变量有赋值的值；如果赋值，将会是最后一个的值。</p>
<pre><code class="copyable">var a = 1; 
var b = 2;

// 一条语句，多个变量使用 , 隔开
var c = 1, d = 2, e = 3;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26af24272d2f4f64bd889328d3bbd718~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>标识符</strong></p>
<p>所有 JavaScript <em>变量</em>必须以<em>唯一的名称</em>的<em>标识</em>。<br>
构造变量名称（唯一标识符）的通用规则是： （转自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3school.com.cn%2Fjs%2Fjs_variables.asp%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3school.com.cn/js/js_variables.asp%EF%BC%89" ref="nofollow noopener noreferrer">www.w3school.com.cn/js/js_varia…</a></p>
<ul>
<li>名称可包含字母、数字、下划线和美元符号</li>
<li>名称必须以字母开头</li>
<li>名称也可以 $ 和 _ 开头</li>
<li>名称对大小写敏感（y 和 Y 是不同的变量）</li>
<li>保留字（比如 JavaScript 的关键词）无法用作变量名称</li>
</ul>
<h3 data-id="heading-6">运算符</h3>
<p><strong>算数运算符</strong></p>





































<table><thead><tr><th>运算符</th><th>描述</th></tr></thead><tbody><tr><td>+</td><td>加法</td></tr><tr><td>-</td><td>减法</td></tr><tr><td>*</td><td>乘法</td></tr><tr><td>/</td><td>除法</td></tr><tr><td>%</td><td>求模/余数</td></tr><tr><td>++</td><td>递加</td></tr><tr><td>--</td><td>递减</td></tr></tbody></table>
<p><strong>赋值运算符</strong></p>








































<table><thead><tr><th>运算符</th><th>列子</th><th>解释</th></tr></thead><tbody><tr><td>=</td><td>x=y</td><td>x=y</td></tr><tr><td>+=</td><td>x+=y</td><td>x=x+y</td></tr><tr><td>-=</td><td>x-=y</td><td>x=x-y</td></tr><tr><td>*=</td><td>x*=y</td><td>x=x*y</td></tr><tr><td>/=</td><td>x/=y</td><td>x=x/y</td></tr><tr><td>%=</td><td>x%=y</td><td>x=x%y</td></tr></tbody></table>
<p><strong>字符串运算符</strong></p>
<p><code>+</code> 运算符可用于字符串相加（concat）;字符串与数字相加返回字符串。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/469ba5f113154794b8d460b99f37a935~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>比较运算符</strong></p>













































<table><thead><tr><th>运算符</th><th>描述</th></tr></thead><tbody><tr><td>==</td><td>相等</td></tr><tr><td>===</td><td>等值等数据类型</td></tr><tr><td>!=</td><td>不相等</td></tr><tr><td>!==</td><td>不等值或不等数据类型</td></tr><tr><td>></td><td>大于</td></tr><tr><td><</td><td>小于</td></tr><tr><td>>=</td><td>大于或等于</td></tr><tr><td><=</td><td>小于或等于</td></tr><tr><td>?</td><td>三元运算符</td></tr></tbody></table>
<p><strong>逻辑运算符</strong></p>





















<table><thead><tr><th>运算符</th><th>描述</th></tr></thead><tbody><tr><td>&&</td><td>与</td></tr><tr><td></td><td></td></tr><tr><td>!</td><td>非</td></tr></tbody></table>
<p><strong>类型运算符</strong></p>

















<table><thead><tr><th>运算符</th><th>描述</th></tr></thead><tbody><tr><td>typeof</td><td>返回变量的类型</td></tr><tr><td>instanceof</td><td>返回 true，如果对象是对象类型的实例。</td></tr></tbody></table></div>  
</div>
            
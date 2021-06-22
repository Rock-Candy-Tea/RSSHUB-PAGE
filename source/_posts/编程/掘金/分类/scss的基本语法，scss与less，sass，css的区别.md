
---
title: 'scss的基本语法，scss与less，sass，css的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6149'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 17:15:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=6149'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>less,  sass, scss都是<strong>css预处理语言</strong>（也是对应的文件后缀名），它们的语法功能比css更强大。</p>
<p>预处理语言使用是：<strong>开发</strong>时用<strong>预处理语言</strong>，在<strong>打包上线</strong>时，用webpack再配合loader工具给<strong>转成css</strong>（Cascading Style Sheets）给浏览器使用。</p>
<blockquote>
<p>细节：</p>
<ol>
<li>
<p>后缀名：SASS（<strong>S</strong>yntactically <strong>A</strong>wesome <strong>S</strong>tyle<strong>S</strong>heets）版本3.0之前的后缀名为.sass，而版本3.0之后的后缀名.scss</p>
</li>
<li>
<p>语法规范：</p>
<p>​sass没有<code>&#123;&#125;</code>和<code>;</code>, 有严格的缩进规范 ;</p>
<p>​    scss和css的缩进规范是一致的</p>
</li>
</ol>
</blockquote>
<p><strong>我们在实际开发过程中，scss是常用写法</strong></p>
<h2 data-id="heading-0"><strong>scss 的基本语法：</strong></h2>
<h3 data-id="heading-1">1. 可以使用$来标识变量（可以将常用的样式标记成变量，后续复用即可，方便维护）</h3>
<pre><code class="copyable">$highlight-color: #f40;
$basic-border: 1px solid black;

#app &#123;
    background-color: $highlight-color;
  border: $basic-border;
&#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2. 嵌套语法（和less语法相同）</h3>
<pre><code class="copyable"><div id="app">
    <div class="container">container</div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// scss语法
$highlight-color: #f90;
$basic-border: 1px solid black;

#app&#123;
  background-color:  $highlight-color;
  border:$basic-border;
  .container&#123;
    font-size:30px;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3. &父选择器(跟less语法相同)</h3>
<p><strong>假如你想针对某个特定子元素 进行设置</strong></p>
<pre><code class="copyable">$highlight-color: #f90;
$basic-border: 1px solid black;

#app&#123;
  background-color:  $highlight-color;
  border:$basic-border;
  .container&#123;
    font-size:30px;
  &#125;
  a&#123;
    color:blue;
    &:hover&#123;
      color: red;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4. 模块化</h3>
<p><strong>可以将需要的变量定义在一个新的js文件中，需要使用的样式文件直接引入即可</strong></p>
<pre><code class="copyable">@import './base.scss';
$highlight-color: #f90;
$basic-border: 1px solid black;
#app&#123;
  background-color:  $base-color;
  border:$basic-border;
  .container&#123;
    font-size:30px;
  &#125;
  a&#123;
    color:blue;
    &:hover&#123;
      color: red;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用scss作为你的样式后，一般在html页面中不得直接引入（因为浏览器中只支持css），vscode中有个名为<strong>Easy Sass</strong>的扩展可以将sass文件或scss文件自动转移成一个css文件，我们用的时候直接引入css文件</p>
<p><strong>致敬我当码农的每一天！！！</strong></p></div>  
</div>
            
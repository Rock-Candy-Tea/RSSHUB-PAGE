
---
title: 'HTML入门笔记1'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c1ee8b370c34bcaa5497285521e879a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 17:57:30 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c1ee8b370c34bcaa5497285521e879a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一. HTML由谁发明的呢？</h2>
<p>HTML的英文全称是 Hyper Text Marked Language，即超文本标记语言。HTML是由Web的发明者 <strong>Tim Berners-Lee和同事 Daniel W. Connolly</strong>于1990年创立的一种标记语言。
Tim Berners-Lee还成立了万维网联盟（W3C），并担任万维网联盟的主席。万维网的主要工作也是围绕HTML开展。</p>
<h2 data-id="heading-1">二. HTML 起手式</h2>
<p>在VSCODE中，使用! + Tab 键会直接显示出html的基本格式。
如图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c1ee8b370c34bcaa5497285521e879a~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-07-27_09-19-21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>第一行的<code><!DOCTYPE html> </code>表示文档类型</li>
<li>第二行表示的是html标签，lang属性一般改为"zh-CN"。</li>
<li><code>head</code>标签里面的第一行表示文字编码，默认为<code>UTF-8</code>即可；第二行和第三行表示禁止缩放、兼容手机和告诉IE使用最新内核；最后的<code>title</code>标签表示的是网页上打开后标题。</li>
</ol>
<h2 data-id="heading-2">三. HTML常用的章节标签</h2>
<pre><code class="copyable">1. h1-h6: 标题
2. section: 章节
3. article: 文章
4. p: 段落
5. header: 头部
6. footer: 脚部
7. main: 主要内容
8. aside: 旁支内容
9. div: 简单划分
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">四. HTML的全局属性(所有标签都有的属性)</h2>
<pre><code class="copyable">1. class(类)
2. contenteditable(内容可编辑的)、
3. hidden(隐藏)
4. id、style(样式)
5. tabindex(表示tab的顺序)
6. title(隐藏文字或者图片时，鼠标放上去会显示出完整的信息)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">五. HTML常用的内容标签</h2>
<pre><code class="copyable">1. ol + li (ordered list + list item)表示有序列表
2. ul + li (unordered list + list item)表示无序列表
3. dl + dt + dd (description list + term + data) 表示一个说明表，描述其相关的内容
4. pre (preview) 表示预览，如果你想保留空格、回车等操作，可以使用改标签。
5. hr (分割线)
6. br (break) 换行
7. a (anchor) 表示链接标签，翻译为锚。
8. em (emphasis) 表示强调，一般指语气上的强调。
9. strong 表示对内容本身重要性进行强调
10. code (code里面的字是等宽的)
11. q (quote)定义短的引用。浏览器经常在引用的内容周围添加引号。
12. blockquote 表示块引用。标签之间的所有文本都会从常规文本中分离出来，经常会在左、右两边进行缩进（增加外边距），而且有时会使用斜体。也就是说，块引用拥有它们自己的空间。

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            
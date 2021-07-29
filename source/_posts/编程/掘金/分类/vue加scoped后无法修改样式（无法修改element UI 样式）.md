
---
title: 'vue加scoped后无法修改样式（无法修改element UI 样式）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6839'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 01:45:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=6839'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>之前在项目中用到了 vant，使用特别简单，而且组建也非常的丰富。即时这样，在项目中肯定也需要用额外的样式来打造自己的应用。直接在  ....  中编写的话只会影响当前组件内的样式，但如果去掉scoped话又会影响全局样式。想了好多方法，都没得到很好的解决。\</p>
<p>百度之后发现 可以用 /deep/或::v-deep来解决***（不过在vue3.0的环境下，使用/deep/时，编译会报错）***。没想到官方文档中其实早就给出了解决方案，怪自己没有认真看过文档，对vue的掌握还是不够熟悉啊，得好好学习了。</p>
<p>深度作用选择器\</p>
<p>如果你希望 scoped 样式中的一个选择器能够作用得“更深”，例如影响子组件，你可以使用 >>> 操作符：<br>
<code><style scoped> .a >>> .b &#123; /* ... */ &#125; </style></code> 上述代码将会编译成：<br>
<code>.a[data-v-f3f3eg9] .b &#123; /* … */ &#125;</code></p>
<p>有些像 Sass 之类的预处理器无法正确解析 >>>。这种情况下你可以使用 /deep/ 或 ::v-deep 操作符取而代之——两者都是 >>> 的别名，同样可以正常工作。</p>
<p>1、>>>\</p>
<p>如果vue的style使用的是css，那么则</p>
<pre><code class="copyable"><style lang="css" scoped>
.a >>> .b &#123; 
 /* ... */ 
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是像scss等预处理器却无法解析>>>，所以我们使用下面的方式.</p>
<p>2、/deep/\</p>
<pre><code class="copyable"><style lang="scss" scoped>
.a&#123;
 /deep/ .b &#123; 
  /* ... */ 
 &#125;
&#125; 
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是有些开发者反应，在vue-cli3编译时，deep的方式会报错或者警告。<br>
此时我们可以使用第三种方式</p>
<p>3、::v-deep\</p>
<p>切记必须是双冒号</p>
<pre><code class="copyable"><style lang="scss" scoped>
.a&#123;
 ::v-deep .b &#123; 
  /* ... */ 
 &#125;
&#125; 
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用场景:</p>
<p>当我们需要覆盖element-ui中的样式时只能通过深度作用选择器\</p>
<p>style为css时的写法如下\</p>
<pre><code class="copyable"> .a >>> .b &#123;
  ***
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>style使用css的预处理器(less, sass, scss)的写法如下\</p>
<p>第一种/deep/\</p>
<pre><code class="copyable"> /deep/ .a &#123;
  ***
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种::v-deep\</p>
<pre><code class="copyable">::v-deep .a&#123;
 ***
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考：</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_42221334%2Farticle%2Fdetails%2F88533329" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_42221334/article/details/88533329" ref="nofollow noopener noreferrer">blog.csdn.net/qq_42221334…</a></p>
</blockquote></div>  
</div>
            
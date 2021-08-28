
---
title: 'HTML和CSS当中的BFC模块作用和特点。（面试经典题目，大厂必问）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fff5bd268aa544b284882650239c77db~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 18:31:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fff5bd268aa544b284882650239c77db~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>1.BFC中的英文全称是 block formatter context(块级格式化执行上下文)，是css里面的一种块级概念。</p>
<p>我们都知道。如果有一对父组关系的元素，如果子元素有原先的高度和宽度，并且设置为浮动元素脱离文档流。则父元素会因此造成高度塌陷，进而使元素的样式变得十分难看。</p>
<p>来演示一下代码</p>
<pre><code class="copyable"><div class="fath">
    <div class="son"></div>
  </div>
<style>
    .fath&#123;
      width: 400px;
      height: 30px;
      background-color: blue;
    &#125;
    .son&#123;
      width: 300px;
      height: 200px;
      background-color: aqua;
      float: left;
    &#125;
  </style>
    
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fff5bd268aa544b284882650239c77db~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由图可知在这样情况下，父元素的高度承载不下子元素。</p>
<p>那么，此时就是展现BFC作用的重要时刻。</p>
<p><strong>bfc的几个重要特征：(是针对父元素设置的)</strong></p>
<p><strong>1.overflow的值设为hidden。</strong></p>
<p><strong>2.display的值设置为inline-block</strong></p>
<p><strong>3.position的值不是static和relative(也就是说是absolute和fix都行)</strong></p>
<p><strong>4.父元素float的值同样也不能为none</strong>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd85bd61b11344c3ad1b71aa183c8b61~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由图可知，父元素的css样式只要满足如上的条件之一，父元素就能够形成与子元素一致的元素流，并根据子元素的宽高把自己的宽高给撑开。</p>
<p><strong>为什么呢？在bfc盒子中，所有的样式有个块级作用域，只针对bfc盒子内的元素有效，与外部区域没有任何关系，</strong></p>
<p><strong>！！注意：将父元素设置为bfc时，父元素是不需要设置初始的宽高的。</strong></p>
<p>bfc的其他作用。</p>
<p>还是一对父子元素。</p>
<pre><code class="copyable">body&#123;
      background-color: brown;
    &#125;
.fath&#123;
      width: 400px;
      height: 400px;
      background-color: blue;
    &#125;
    .son&#123;
      margin-top: 20px;
      width: 300px;
      height: 200px;
      background-color: aqua;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码表示：我想要在子元素的顶部跟父元素的顶部有个20px的边距。可是代码写完会发现。</p>
<p>效果是这样的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/828ecc480a164fdcb1fd9c4ad982faf3~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>明显可知，在这个情况下，父元素与子元素一同产生与浏览器视口顶部的一段20px的边距。
也是因为盒子在使用margin时导致的margin塌陷。</p>
<p>此时通过bfc的是个特点任选其一在父元素的css中进行摄制，就能解决该问题。</p></div>  
</div>
            

---
title: '前端路上遇见的奇怪问题--魔幻的float？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73bd0c55e53541a7a023b6ad52c8f9f9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 22:17:28 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73bd0c55e53541a7a023b6ad52c8f9f9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="copyable">.parent 
&#123; background-color: red;/* border: blue solid 1px; */&#125;
.son
&#123;width: 100px;height: 100px;background-color: silver;&#125;
.box1
&#123;  height: 200px;  width: 200px;  background-color: pink;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css代码如上 页面结构如下</p>
<pre><code class="copyable"> <div class="parent ">
    <div class="son">儿子</div>
 </div>
 <div class="box1"> </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示效果如下 可以理解：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73bd0c55e53541a7a023b6ad52c8f9f9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时给son添加float：left，父元素高度丢失，导致son和box1重叠 这也能理解</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3f4cbfcf26e48a7917180fea300d92c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时在给选择器box1 clear：left; 此时呢son和box1就不会重叠效果图如下</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a221023b23b94728b4cb1805b6dc3681~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来就有些奇怪了 注释掉clear： left，给box1 添加一个上外边距 页面结构不变显示效果就是如下和我想象中的不一样。想象中的应该是son不动 box1下移150px；</p>
<pre><code class="copyable">.parent 
&#123; background-color: red; /* border: blue solid 1px; */ &#125;
.son
&#123;width: 100px;height: 100px;background-color: silver;float: left;            &#125;
.box1
&#123;height: 200px;width: 200px;background-color: pink; /* clear: left; */
 margin-top: 150px;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f665bfa75074cc28a5039cff3f8a7c8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>**儿子为什么也下移了呢？？**原因是什么呢？不知道！parent元素没有了高度，那么给父元素一个border此时的显示效果就是如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49ecc7fdc3394371a90e2a0a2f6e1338~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>既然想到了是父亲没有了高度，那么给父亲一个height:100px;</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f519e1199f3492b951e2f4186ed5833~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这就正常了。修改一下css代码</p>
<pre><code class="copyable">.parent&#123; 
    background-color: red;
    /* border: blue solid 1px; */
    /* height: 100px; */
&#125;
.son&#123;
    width: 100px;
    height: 100px;
    background-color: silver;float: left;
      &#125;
.box1&#123;
height: 200px;
width: 200px;
background-color: pink;
/* clear: left; */
 margin-top: 150px;&#125;
.clearfix::before&#123;
display: table;content: '';
 /* clear: both; */&#125;

  <div class="parent clearfix"> 
           <div class="son">儿子</div>
    </div>    
<div class="box1">box1</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/065187ee81dd4641a09a22bfead819ba~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结一下：默认情况下 ，父元素的高度由子元素的内容撑开，当使用float属性后，son脱离了文档流，父元素高度丢失，此时给box1添加一个上外边距无法使得只有box1下移150px;实际上是son和box1都会下移，经过上面的测试发现只要给parent高度撑开，margin-top就会起效果，除此之外在box1前面加一个</p><div>111<div> 也会起效，完全不需要写clearfix这个类选择器。如下图所示。 <p></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dd92aab88e048c3bebd6f1441d661d4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.parent 
&#123; background-color: red;   
/* border: blue solid 1px; */ 
/* height: 100px; */
 &#125; 
.son&#123;  
width: 100px; 
height: 100px;
background-color: silver; 
float: left;
   &#125;        
.box1&#123;
 height: 200px;
width: 200px;
background-color: pink; 
/* clear: left; */
margin-top: 150px;
&#125;



<body>
<div>111</div><div class="parent"> 
  <div class="son">儿子</div><
/div
><div class="box1">box1</div>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至于为什么，个人表示目前不清楚。。。只能说因吹斯听！！</p></div></div></div>  
</div>
            
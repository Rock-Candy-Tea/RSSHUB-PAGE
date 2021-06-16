
---
title: 'SVG图打点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5836'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 00:56:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=5836'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第4天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>在平时的工作中 ，我们可能会遇到需要在SVG图上或是某个DOM上打点的需求，下面实现了在SVG图上打点的功能，如果需要在其他DOM上打点也可以参照此方法。</p>
<p>说一下思路：<br>
一、如何在SVG图片里再插入图片</p>
<ol>
<li>要想在SVG图上打点，首先想着怎么在SVG图片里插入图片，创建一个SVG的image标签</li>
</ol>
<pre><code class="copyable">const svgImgDom = document.createElementNS(
    'http://www.w3.org/2000/svg',
    'image',
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>然后引入图片，设置图片的宽高，并添加class,这都可以用setAttributeNS() 来实现</li>
<li>之后可以通过appendChild()将带有图片信息的svgImgDom插入到SVG图片中</li>
</ol>
<p>二、插入图片的位置</p>
<ol>
<li>获取svg图片针对整个窗口的页面偏移量</li>
</ol>
<pre><code class="copyable"> const svgDom = this.$refs.svgBox;
  const svgOffset = &#123;
    x: svgDom.getBoundingClientRect().left,
    y: svgDom.getBoundingClientRect().top,
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>svg页面缩放系数</li>
</ol>
<pre><code class="copyable"> const pageScale = &#123;
    x: 752.333 / svgDom.offsetWidth,　// svg标签内viewBox的值
    y: 430 / svgDom.offsetHeight,
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.鼠标偏移量 （缩放页面后正确的鼠标位置）</p>
<pre><code class="copyable">// 这里 svgDom.offsetWidth/21 和 svgDom.offsetHeight/2.77  宽高相除的比例可以根据实际点位灵调整，
// 有了整个缩放比例，当窗口size更改时也可以自动适用点位的偏移
const mouseOffset = &#123;
    x: ((e.pageX + svgDom.offsetWidth/21) - svgOffset.x) * pageScale.x, 
    y: ((e.pageY + svgDom.offsetHeight/2.77) -  svgOffset.y) * pageScale.y,
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是完整的代码<br>
HTML</p>
<pre><code class="copyable"><div @click="clickPoint" class="svgBox" id="svgBox" ref="svgBox">
  <svg id='SVGDom' class='SVGDom' version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
   y="0px" viewBox="78 205.89 752.333 430" style="enable-background:new 78 205.89 752.333 430;" xml:space="preserve">
  </svg>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JS部分</p>
<pre><code class="copyable">clickPoint(e) &#123;
  const svgDom = this.$refs.svgBox;
  const svgOffset = &#123;
    x: svgDom.getBoundingClientRect().left,
    y: svgDom.getBoundingClientRect().top,
  &#125;;
  const pageScale = &#123;
    x: 752.333 / svgDom.offsetWidth,　// svg标签内viewBox的值
    y: 430 / svgDom.offsetHeight,
  &#125;;
  const mouseOffset = &#123;
    x: ((e.pageX + svgDom.offsetWidth/21) - svgOffset.x) * pageScale.x, 
    y: ((e.pageY + svgDom.offsetHeight/2.77) -  svgOffset.y) * pageScale.y,
  &#125;;
  const svgImgDom = document.createElementNS(
    'http://www.w3.org/2000/svg',
    'image',
  );
  svgImgDom.setAttributeNS(null, 'height', '50');
  svgImgDom.setAttributeNS(null, 'width', '50');
  svgImgDom.setAttributeNS(
    'http://www.w3.org/1999/xlink',
    'href',
    require('../../assets/greenPoint.jpeg'),
  );
  svgImgDom.setAttributeNS(null, 'x', mouseOffset.x);
  svgImgDom.setAttributeNS(null, 'y', mouseOffset.y);
  svgImgDom.setAttributeNS(null, 'class', 'addPointImgs');
  document.getElementById('SVGDom').appendChild(svgImgDom);

// 删除图标
  const className = e.target.classList[0];
  if (className === 'addPointImgs') &#123;
    this.deletePointFun(e);
  &#125;
&#125;,
// 删除点位
deletePointFun(e) &#123;
  const el = e.target;
  this.$confirm('确定删除该点位信息吗?', '提示', &#123;
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning',
  &#125;).then(() => &#123;
    this.$message(&#123;
      type: 'success',
      message: '删除成功!',
    &#125;);
    el.remove();
  &#125;).catch(() => &#123;
    this.$message(&#123;
      type: 'info',
      message: '已取消删除',
    &#125;);
  &#125;);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            
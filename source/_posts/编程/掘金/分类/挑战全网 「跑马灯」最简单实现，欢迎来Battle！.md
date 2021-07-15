
---
title: '挑战全网 「跑马灯」最简单实现，欢迎来Battle！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://maomao.ink/usr/uploads/2021/07/201113899.png'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 07:46:33 GMT
thumbnail: 'https://maomao.ink/usr/uploads/2021/07/201113899.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>提到跑马灯，你会想到怎么实现？</p>
<h1 data-id="heading-0"><strong>用<code><marquee></marquee></code>标签实现？</strong></h1>
<p>上百度搜<code>marquee</code>,第一条答案就告诉你——<strong>已废弃</strong></p>
<p><img src="https://maomao.ink/usr/uploads/2021/07/201113899.png" alt="06906-lzulkunbru.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1"><strong>用<code>JS</code>实现一套？</strong></h1>
<p>这大概是目前最普遍的实现方式。</p>
<p>思路有很多，比如用js计算偏移量，用循环定时任务去移动偏移量。</p>
<p>可以是：</p>
<ul>
<li>定时任务+transform</li>
<li>定时任务+scroll</li>
</ul>
<p>不管是哪种方式，代码量少说也有100行左右，还需处理各种状态判断。</p>
<p>由于没有找到合适的方案（在我看来，不能直接拿来用的代码就不是好代码）；</p>
<p>所以只能自己造轮子，今天刚出炉的，给你介绍一下。</p>
<h1 data-id="heading-2"><strong>用<code>css</code>实现</strong></h1>
<p>本例方案：用纯CSS动画实现跑马灯。</p>
<blockquote>
<p><strong>思路：采用animation循环动画，搭配CSS属性做到循环滚动，再根据文案长短动态设置动画时长。</strong></p>
</blockquote>
<h2 data-id="heading-3">代码实现</h2>
<p>标签：</p>
<pre><code class="copyable">      <div className="marquee-root">
        <div className="marquee-content">
          跑马灯滚动起来…… 
        </div>
      </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css：</p>
<pre><code class="copyable">@keyframes marqueeAnim &#123;
  0% &#123;
    transform: translateX(100vw);
  &#125;
  100% &#123;
    transform: translateX(-100%);
  &#125;
&#125;

.marquee-content &#123;
  white-space: nowrap;
  display: inline-block;
  color: chocolate;
  animation: marqueeAnim 5s linear 0s infinite;
&#125;

.marquee-root &#123;
  width: 100%;
  height: 30px;
  text-align: left;
  line-height: 30px;
  overflow: hidden;
  background-color: burlywood;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>over</strong></p>
<p>以上就是跑马灯的简单实现了。<strong>上面的跑马灯可以做到不管是多少文案，都能够展示完毕再进行下一次循环滚动。</strong></p>
<p>但是在变换莫测的产线环境，文案可短可长，这种固定动画时长的方案可能会导致下面这种问题：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcaa8b0b4fd946fab6892f1e75dd7cc0~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制 2021-07-14 下午10.19.22.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d6cdc6036014612ac1dc4f26536bc17~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制 2021-07-14 下午10.22.52.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没错，有的快有的慢，文案很多的时候就快得离谱。</p>
<h2 data-id="heading-4">动态控制动画时间</h2>
<p>根据文案的多少来决定动画时长。很简单，只要一行代码。</p>
<pre><code class="copyable">style=&#123;&#123; animationDuration: marqueeStrs.length * 0.2 + 5 + "s" &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在你的动画div上面添加这个<code>style</code>，<code>marqueeStrs</code>是你的跑马灯文案，<code>0.2</code>是时间系数，可以根据实际情况修改，<code>+ 5</code>是添加时间基数，不然文案少的时候就飞起来了。</p>
<p>全代码：</p>
<pre><code class="copyable">  //todo test data
  const marqueeStrs = "跑马灯滚动起来…… 跑马灯滚动起来…… 跑马灯滚动起来…… ";
  return (
    <div className="App">
      <div className="marquee-root">
        <div
          className="marquee-content"
          style=&#123;&#123; animationDuration: marqueeStrs.length * 0.2 + 5 + "s" &#125;&#125;
        >
          &#123;marqueeStrs&#125;
        </div>
      </div>
    </div>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>前面的css不需要修改。</strong></p>
<p>效果图对比：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f5cac41210b4a72b299292274ba9312~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制 2021-07-14 下午11.15.14.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8e9f28fbb7b430a873d62cefc6b60db~tplv-k3u1fbpfcp-watermark.image" alt="屏幕录制 2021-07-14 下午11.17.45.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到两张图的速度基本相等。</p>
<h2 data-id="heading-5">小结</h2>
<p>这个方案看起来很简单，但是有一些点是需要注意的。</p>
<ol>
<li><code>white-space: nowrap;</code> 可以让你的文案强制不换行。</li>
<li><code>display: inline-block;</code> 可以让你的跑马灯布局根据内容自适应。</li>
<li><code>overflow: hidden;</code> 父布局设置这个属性可以让跑马灯内容超出部分被隐藏。</li>
<li><code>0%</code>时<code>transform: translateX(100vw);</code> 是为了让跑马灯从屏幕外开始移动。</li>
<li><code>100%</code>时<code>transform: translateX(-100%);</code> 是为了让跑马灯布局滚动整个布局宽度（不是屏幕宽度），最后滚到屏幕外。</li>
</ol>
<p>以上几个CSS样式是本次跑马灯实现的核心支撑。当然，还有最后的<code>动态计算动画时间</code>也是核心步骤。</p>
<p>那么，你应该会了。</p>
<p>如果你有更好的方案，欢迎评论区留言，Show出你的代码！</p></div>  
</div>
            
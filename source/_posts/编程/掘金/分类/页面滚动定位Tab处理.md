
---
title: '页面滚动定位Tab处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8956'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 07:58:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=8956'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr>
<h2 data-id="heading-0">theme: cyanosis
highlight: a11y-dark</h2>
<p>这是我参与更文挑战的第 12 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>Lynne，一个能哭爱笑永远少女心的前端开发工程师。身处互联网浪潮之中，热爱生活与技术。</p>
</blockquote>
<h2 data-id="heading-1">前言</h2>
<p>首先描述下问题，应用场景如下：</p>
<p>随着滚动条的滚动，tab会对应进行切换，切换tab时，又会定位到tab对应内容的高度变化。</p>
<p>切换 tab 定位到对应内容这个可以用简单的锚点定位来实现，但如果需要平滑地进行内容滚动切换最好借助scrollIntoView 来实现，而要实现tab随滚动条的滚动进行切换则需要监听当前页面的滚动。</p>
<p>接下来以一段代码为例，分析实现思路。</p>
<pre><code class="copyable"><div class="box">
 <div class="tab" ref="tab">
  <div v-for="(item, index) in tabs" :key="index">
    <div :class="&#123; active: active === index &#125;" @click="switchTab(index)">
      &#123;&#123; item &#125;&#125;
    </div>
  </div>
 </div>
 <div class="cont" ref="cont">
  <div :class="'cont_'+active">内容&#123;&#123;mapCont[active]&#125;&#125;</div>
 </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">tab 切换时平滑滚动定位</h2>
<p>定义data:</p>
<pre><code class="copyable">data() &#123;
 return () &#123;
   tabs: [],
   active: 0,
   mapCont: &#123;
     
   &#125;
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义切换方法：</p>
<pre><code class="copyable">methods: &#123;
  switchTab(index) &#123;
      const cont_n = mapCont[index + 1];
      this.cont_n.scrollIntoView(&#123;
          block: "start",
          behavior: "smooth"
      &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">监听滚动实现tab切换</h2>
<p>在mounted中挂载滚动监听：</p>
<pre><code class="copyable">mounted() &#123;
  const n = this.active;
  const cont_n = this.$refs["cont_"+$&#123;n&#125;];
  const tabH = this.$refs["tab"].offsetHeight;
  this.$refs["cont"].addEventListener("scroll", () => &#123;
    if (this.cont_n.getBoundingClientRect().top <= tabH) &#123;
      this.active = n-1;
      return false;
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当tab项已知时，监听并定位到具体tab得切换很简单，举一个实例如下：</p>
<pre><code class="copyable">// 监听滚动距离
    getScrollTop () &#123;
      let scrollTop = window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop
      if (scrollTop && scrollTop > this.topValue + (this.openIndex * 68) + 90) &#123;
        this.isFixedClass = true
      &#125; else &#123;
        this.isFixedClass = false
      &#125;
      if (scrollTop <= this.slotsTopList[1]) &#123;
        this.tabIndex = 0
      &#125; else if (scrollTop <= this.slotsTopList[2]) &#123;
        this.tabIndex = 1
      &#125; else &#123;
        this.tabIndex = 2
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但tab项数量未知时我们也可以根据以上原理，抽象并完成代码实现。</p>
<h2 data-id="heading-4">总结</h2>
<p>以上是抽象的实现原理和流程，最主要的是通过监听 window的滚动事件，通过滚动高度来判断那个内容区在当前视口， 从而操作对应的导航菜单里的状态的转换。 点击导航菜单触发滚动， 与此相对应。</p></div>  
</div>
            
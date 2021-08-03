
---
title: '手把手一起学一次前端Debug'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02b18f802acf437fa7eefd3a0a38684f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 00:19:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02b18f802acf437fa7eefd3a0a38684f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">故事的开始</h2>
<p>在一个阳光明媚的早晨，我吃完早餐准时来上班，听着吴亦凡的freestyle，觉得今天应该是一个无风无浪的日子</p>
<p>可是，事情的发展总是会出乎我们的意料</p>
<hr>
<h2 data-id="heading-1">出现线上问题</h2>
<p>出现问题的视频大概是：</p>
<p>用户通过第三方OA系统跳转到我们的Saas系统，结果出现一直页面重新加载情况.</p>
<h2 data-id="heading-2">问题分析</h2>
<p>1.此登录为授权登录，非单点登录，通过url的参数携带登录的参数传递给后端</p>
<p>2.授权登录一直是稳定的，去年做过企业微信打通，应该没问题</p>
<p>3.通过录制的视频查看用户出现的问题应该是前端页面不断重载，不像是后端的重定向</p>
<h2 data-id="heading-3">定位问题的边界</h2>
<p>1.确认授权登录是正常的，登录态有写入</p>
<p>2.确定非后端重定向导致</p>
<p>3.那么定位到问题属于纯前端问题</p>
<h2 data-id="heading-4">问题复现</h2>
<p>1.首先登录客户的第三方OA系统</p>
<p>2.然后跳转到我们的Saas系统，进行问题复现</p>
<h2 data-id="heading-5">从结果出发寻找问题</h2>
<p>能造成线上页面不端刷新的，大概率是前端调用了reload函数,于是我通过<code>performance</code>面板，录制了一波得到了火焰图（调用栈的图）如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02b18f802acf437fa7eefd3a0a38684f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过搜索<code>reload</code>后，发现有5个匹配的结果，通过查看，发现<code>reload</code>函数调用后，页面就立刻重载了，是每次页面重载最后调用的那个函数，应该是这个导致的</p>
<h2 data-id="heading-6">问题处理</h2>
<p>由于我们是微前端模式，子应用全局搜索</p>
<pre><code class="copyable">window.reload
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只有一个地方匹配的，是跟cookie处理有关</p>
<p>由于我们是一个比较复杂的Saas系统，出现问题的原因是进行了微前端改造，基座中已经对授权登录进行了处理，进入子应用时候，都已经有登录态了</p>
<p>而且我们自身对于授权登录和cookie等的处理机制，造成了这个冲突，于是就不断触发了子应用的reload</p>
<p>解决,加上下面判断即可（通过基座加载时候不用reload）：</p>
<pre><code class="copyable">if (!window.__POWERED_BY_QIANKUN__)&#123;
  window.reload()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>最终，在中午一点前解决发布了，没有阻碍同事下午到客户那边的演示</p>
</blockquote>
<h2 data-id="heading-7">学习总结</h2>
<p>处理线上问题时候，一般步骤：</p>
<p>1.复现问题</p>
<p>2.定位问题的边界，是前端or后端</p>
<p>3.找出问题出现的原因：技术问题？业务设计问题？还是人为代码漏洞等</p>
<p>4.确定问题后看是否能彻底根治，如果不能，是否有其他风险，拉相关负责人探讨。如果能根治，快速设计根治方案，实施后测试上线发布</p></div>  
</div>
            
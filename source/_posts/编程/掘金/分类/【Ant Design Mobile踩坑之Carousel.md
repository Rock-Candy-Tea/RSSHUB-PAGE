
---
title: '【Ant Design Mobile踩坑之Carousel'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ddfad48067a401faff6d7ce14afc326~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 00:36:21 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ddfad48067a401faff6d7ce14afc326~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1、从后台获取图片，页面轮播显示。</h3>
<p>结果如下：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ddfad48067a401faff6d7ce14afc326~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
代码如下：</p>
<pre><code class="copyable"><Carousel autoplay=&#123;true&#125; infinite=&#123;true&#125;>
          &#123;this.state.aSwiper && this.state.aSwiper.length
            ? this.state.aSwiper.map((item, index) => (
                <div key=&#123;index&#125; className=&#123;Css["swiper-wrap"]&#125;>
                  <img src=&#123;item&#125; alt="" />
                </div>
              ))
            : ""&#125;
        </Carousel>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原因：数据是从后台获取的，Carousel初始化的时候aSwiper为空导致的，所以把为空判断放在Carousel外面，确保aSwiper不为空后再初始化Carousel，修改后代码如下：</p>
<pre><code class="copyable">&#123;this.state.aSwiper && this.state.aSwiper.length ? (
          <Carousel autoplay=&#123;true&#125; infinite=&#123;true&#125;>
            &#123;this.state.aSwiper.map((item, index) => (
              <div key=&#123;index&#125; className=&#123;Css["swiper-wrap"]&#125;>
                <img src=&#123;item&#125; alt="" />
              </div>
            ))&#125;
          </Carousel>
        ) : (
          ""
        )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2 当aSwiper只有一项的时候，显示效果同问题1，还未找到解决方法</h3>
<h3 data-id="heading-2">3 在chrome浏览器中用鼠标左右切换图片的时候报错如下：</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/213dcc79a7964f82b6d31254519dbe3c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
网上的解决方案是全局设置touch-action,如下：</p>
<pre><code class="copyable">*&#123;
  touch-action: none; //或者pan-y
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我尝试了下，报错还在，继续摸索</p></div>  
</div>
            
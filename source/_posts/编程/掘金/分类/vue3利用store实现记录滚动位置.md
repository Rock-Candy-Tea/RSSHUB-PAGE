
---
title: 'vue3利用store实现记录滚动位置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ca689b8ebf84a8984b8995f76147607~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 22:50:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ca689b8ebf84a8984b8995f76147607~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">整体效果</h1>
<p>在首页列表进行滚动浏览时进入详情页后，切换回首页时可以定位到之前浏览的位置。</p>
<p><img alt="Tab-1617766933831(1).gif" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ca689b8ebf84a8984b8995f76147607~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">监听容器滚动事件</h2>
<p>定义一个滚动事件，绑定到容器的滚动事件上,我这里做了一下节流</p>
<pre><code class="copyable">const savePosY = () => &#123;
      if(state.timer) return;
      state.timer = setTimeout(() => &#123;
        let node = document.querySelector(".contentWrapper")；
        //记录滚动位置
        store.commit("setY",node.scrollTop)
        state.timer = null;
        clearTimeout(state.timer);
      &#125;,100)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在mounted中获取到容器进行绑定事件</p>
<pre><code class="copyable">onMounted(() => &#123;
    let contentWrapper = document.querySelector(".contentWrapper");
    contentWrapper.addEventListener("scroll",savePosY);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">store中的配置</h2>
<blockquote>
<p>store中比较简单，仅包含一个state：y 以及 mutations：setY</p>
</blockquote>
<pre><code class="copyable">export default &#123;
    state:&#123;
         y:0
    &#125;,
    mutations:&#123;
        setY(state,value)&#123;
            state.y = value;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">在页面跳回时获取滚动位置</h2>
<p>同样在onMounted中操作，否则获取不到容器元素,而且由于vue中dom是异步渲染，所以我们需要在nextTick中操作才有效果</p>
<p><code> nextTick(() => &#123;         contentWrapper.scrollTop = store.state.y;       &#125;)</code></p>
<h2 data-id="heading-4">最后</h2>
<p>以上就是本文的全部内容啦，如果有写的不对或者有更好的方法，欢迎大家交流指出</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            
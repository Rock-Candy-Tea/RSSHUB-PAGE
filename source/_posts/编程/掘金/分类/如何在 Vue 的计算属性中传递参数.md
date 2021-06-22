
---
title: '如何在 Vue 的计算属性中传递参数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3467'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 03:36:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=3467'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>【这是我参与更文挑战的第 <strong>21</strong> 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”】</p>
<p>在 Vue 中，计算属性（<code>computed</code> ）是从其他响应式属性派生的属性，是用于自动监听响应式属性的变化，从而动态计算返回值。计算属性（<code>computed</code> ）通常是一个没有参数的函数。当然如果需要像调用方法一样给计算属性传递参数也是可以的，本文介绍两种向计算属性传参的方法。</p>
<h3 data-id="heading-0">1.返回函数</h3>
<p>这种方式通过计算属性返回的函数来进行传参，如下代码片段，对于一条未审核通过的记录，审核时间为 <code>0</code>，这是显示 <code>--</code> ：</p>
<pre><code class="copyable"><template>
    <div id="app">
        <p>
            <label>审核时间：</label>
            <i class="number">
                &#123;&#123; auditTime(1624314956) &#125;&#125;
            </i>
        </p>
    </div>
</template>

<script>
export default &#123;
  computed: &#123;
    auditTime: () => &#123;
        return (timestamp) => (timestamp > 0 ? convertDate(timestamp) : "--");
    &#125;,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的计算属性 <code>auditTime</code>，返回一个箭头函数，接收参数<code>timestamp</code>为时间戳，函数 <code>convertDate</code> 实现了时间戳时间格式化。</p>
<h3 data-id="heading-1">2.filters</h3>
<p>可以为组件添加一个过滤器 <code>filters</code>，以便可以在模板中按照想要的方式格式化值。</p>
<p>关于 vue 过滤器，在<a href="https://cn.vuejs.org/v2/guide/filters.html" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>中定义如下：</p>
<blockquote>
<p><code>Vue.js</code> 允许你自定义过滤器，可被用于一些常见的文本格式化。过滤器可以用在两个地方：双花括号插值和 <code>v-bind</code> 表达式（后者从 2.1.0+ 开始支持）。过滤器应该被添加在 JavaScript 表达式的尾部，由“管道”符号指示。</p>
</blockquote>
<pre><code class="copyable"><template>
    <div id="app">
        <p>
            <label>审核时间：</label>
            <i class="number">
                &#123;&#123; 1624314956 | auditTime("--") &#125;&#125;
            </i>
        </p>
    </div>
</template>

<script>
export default &#123;
    filters: &#123;
        auditTime: (timestamp, defaultValue = "--") =>
            timestamp > 0 ? convertDate(timestamp) : defaultValue,
    &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的片段中，当时间戳为<code>0</code>的时候输出的是 <code>--</code> ，这个格式是否有种似曾相识的感觉，在《<a href="https://juejin.cn/post/6975722363241365534" target="_blank">Angular管道PIPE介绍</a>》中介绍的管道，方式类似。</p>
<pre><code class="copyable"> &#123;&#123; 1621836603 | auditTime("--") &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码最终显示为：<code>2021-06-22 06:35</code>。</p>
<pre><code class="copyable"> &#123;&#123; 0 | auditTime("--") &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码最终显示为：<code>--</code>。</p>
<h3 data-id="heading-2">总结</h3>
<p>关于计算属性中传参，当然可以在 <code>methods</code> 中定义相应的方法，两者主要区别是：<code>computed</code> 是可以被缓存的，<code>methods</code> 不能缓存。</p></div>  
</div>
            
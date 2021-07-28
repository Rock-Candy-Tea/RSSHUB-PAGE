
---
title: '利用axios解决误触造成的多次请求发送问题。'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5169'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 18:53:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=5169'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">问题场景：</h2>
<p>在一次小程序开发过程中，由于用户手机卡顿问题，造成用户多次点击按钮，发送多次请求的情况。</p>
<h2 data-id="heading-1">解决方式：</h2>
<p>采用axios中cancelToken来取消ajax请求。以下为解决代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">/**
     * 如果请求带有repetitiveRequestLimit参数
     * 则会进行防止重复提交的操作
     * 利用axios的CancelToken
     */</span>
  <span class="hljs-comment">// 1. 初试化一个pending，用存放每一次请求</span>
    <span class="hljs-keyword">const</span> pending = &#123;&#125;;
    <span class="hljs-comment">// 2. 判断时候带有repetitiveRequestLimit参数，带有本参数才会开启。</span>
    <span class="hljs-keyword">if</span> (config.data.hasOwnProperty(<span class="hljs-string">"repetitiveRequestLimit"</span>)) &#123;
      <span class="hljs-comment">// 3. 生成唯一一个key区分每一次请求</span>
      <span class="hljs-keyword">const</span> key = <span class="hljs-string">`<span class="hljs-subst">$&#123;config.url&#125;</span>&<span class="hljs-subst">$&#123;config.method&#125;</span>&<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(
        config.data
      )&#125;</span>`</span>;
      <span class="hljs-comment">// 4. 调用CancelToken方法</span>
      config.cancelToken = <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function">(<span class="hljs-params">c</span>) =></span> &#123;
        <span class="hljs-comment">// 5. 判断是否是重复请求</span>
        <span class="hljs-keyword">if</span> (pending[key]) &#123;
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Date</span>.now() - pending[key] > <span class="hljs-number">500</span>) &#123;
            <span class="hljs-comment">// 超过0.5s，删除对应的请求记录，可以重新发起请求</span>
            <span class="hljs-keyword">delete</span> pending[key];
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 0.5s以内的重复请求，取消掉</span>
            c(<span class="hljs-string">"repeated"</span>);
          &#125;
        &#125;
      &#125;);
      <span class="hljs-comment">// 6. 记录下发起请求的时间</span>
      pending[key] = <span class="hljs-built_in">Date</span>.now();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            

---
title: '不同浏览器版本关于referer的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: '…'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 04:16:37 GMT
thumbnail: '…'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>微信的鉴权需要判断原域名为可校验的域名，而这一判断是通过跳转地址的referer来判断的，正常情况下浏览器会取当前页面的地址为其referer，我们可也可以通过修改document.referer来进行获取。</p>
<p>但在chrome较高版本以及部分ua情况下，其策略发生了改变，在地址跳转时，不会再添加referer域名以外的参数。这样就会直接导致鉴权失败。</p>
<p>在部分业务场景下，我们可能做了这样的判断，在code无效的情况下会发生302跳转，去重新鉴权，这样就会导致重复鉴权的死循环，问题更为严重。</p>
<p>那么这个问题应该如何解决呢？</p>
<h2 data-id="heading-1">referer的理解</h2>
<ul>
<li>document.referer : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FDocument%2Freferrer" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Document/referrer" ref="nofollow noopener noreferrer">链接</a></li>
<li>referer : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTTP%2FHeaders%2FReferrer-Policy" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Referrer-Policy" ref="nofollow noopener noreferrer">链接</a></li>
</ul>
<p>一句话描述：在跳转地址后，追加该字段可用来判断页面来源的字段，该字段不仅仅可用于页面跳转还可以用于资源类的请求。</p>
<h2 data-id="heading-2">chrome高版本（85）带来的问题</h2>
<p>原本默认的 referer 策略（policy）是no-referrer-when-downgrade，即允许referer带上来源页面地址上的请求参数，Chrome85将策略修改为strict-origin-when-cross-origin，即如果请求地址与请求页面非同源，将只携带请求的域名，不会再带上来源页面地址的请求参数。</p>
<p>那么为什么chrome要修改为这样的策略呢？增强隐私</p>
<h2 data-id="heading-3">如何主动开启这个策略（低版本下）</h2>
<p>如果我们也有这个期望，那么我们可以如何主动开启呢 ？</p>
<p>前端的设置：</p>
<pre><code class="copyable"><meta name="referrer" content="strict-origin-when-cross-origin" />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>服务端的请求：</p>
<p>Referer Policy: strict-origin-when-cross-origin</p>
<h2 data-id="heading-4">如何关闭这个策略</h2>
<p>前端的设置：</p>
<pre><code class="copyable"><meta name="referrer" content="no-referrer-when-downgrade"" /> 
<!-- 对某个特定资源设置 referer 策略 --> 
<img src="…" referrerpolicy="no-referrer-when-downgrade" />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后端的设置：</p>
<p>服务端将Referer Policy设置为no-referrer-when-downgrade</p>
<h2 data-id="heading-5">回到问题</h2>
<p>我们需要将方案调整为关闭即可 。</p>
<p>但如果直接设置为关闭，在低版本时会有相应的兼容问题 ，所以最终的技术方案如下 ：</p>
<p>1 低版本时不做处理</p>
<p>2 chrome高版本，或者指定ua增加指定的meta标签</p>
<p>具体代码如下：仅供参考 ：</p>
<pre><code class="copyable">  <!-- 针对不同版本的内核，设置referrer属性 -->
    <script script type="text/javascript">
      var chromeVersionMatch = window.navigator.userAgent.match(/Chrome/(\d*)/);
      var version = chromeVersionMatch && chromeVersionMatch[1];
      if (version > 84) &#123;
        var meta = document.createElement('meta');
        meta.content='no-referrer-when-downgrade';
        meta.name = 'referrer';
        document.getElementsByTagName('head')[0].appendChild(meta);
      &#125;
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">更多</h2>
<p>因为这个策略暂时没有相应的语法可以直接判断，所以建议在相应的问题上进行数据跟踪，不断追加需要兼容的ua名单和版本。如果你有更好的方案欢迎联系我更新。</p></div>  
</div>
            
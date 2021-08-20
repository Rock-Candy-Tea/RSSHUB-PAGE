
---
title: '全局监听url跳转，并记录返回。'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a70335e19cde4633b5eec3e965a8bdca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 19:08:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a70335e19cde4633b5eec3e965a8bdca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>1.尝试onhashchange 只能监听 前进后退事件 和 hash 的变化</strong></p>
<p><strong>2.尝试 onbeforeunload 事件在即将离开当前页面（刷新或关闭）时触发。</strong><br>
1)关闭浏览器窗口<br>
2)通过地址栏或收藏夹前往其他页面的时候<br>
3)点击返回，前进，刷新，主页其中一个的时候<br>
4)点击 一个前往其他页面的url连接的时候<br>
5)点击事件触发的跳转<br>
但无法获取url的变化，且只支持PC端。</p>
<p><strong>3.尝试添加自定义事件</strong></p>
<pre><code class="copyable">history.pushState = ( f => function pushState()&#123;
    var ret = f.apply(this, arguments);
    window.dispatchEvent(new Event('pushstate'));
    window.dispatchEvent(new Event('locationchange'));
    return ret;
&#125;)(history.pushState);

history.replaceState = ( f => function replaceState()&#123;
    var ret = f.apply(this, arguments);
    window.dispatchEvent(new Event('replacestate'));
    window.dispatchEvent(new Event('locationchange'));
    return ret;
&#125;)(history.replaceState);

window.addEventListener('popstate',()=>&#123;
    window.dispatchEvent(new Event('locationchange'))
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相比hash的变化，添加了历史改变的监听。</p>
<p><strong>4.想尝试nginx的ip拦截记录，但外链根本就不访问我们服务器所以，该方案也不行。</strong></p>
<p><strong>5.参照 CSDN 封装了如下函数</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a70335e19cde4633b5eec3e965a8bdca~tplv-k3u1fbpfcp-watermark.image" alt="输入图片说明" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">let middleJump = function (el = 'a') &#123;
    $(el).on('click', function (e) &#123;
        let href = $(this).attr('href') || '';
        url = ''; //跳转前网页
        hrefRegExp(href) ? (url = href) : (url = url + '?target=' + encodeURIComponent(href));
        e.preventDefault();
        href && window.open(url, '_blank');
    &#125;);
&#125;;

let hrefRegExp = function (href) &#123;
    let reg = "" //正则
    return reg.test(href);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：该方法如果全局使用需要会监听所有a标签，恐有性能问题，但可以在用户使用自定义a标签的页面使用</p>
<p><strong>6.使用jQuery.ajaxStart 方法</strong></p>
<p>该方法类似于请求vue的拦截，可以在所有ajax请求前进行操作，但因无法获取url的变化，该方案也无法使用。</p></div>  
</div>
            
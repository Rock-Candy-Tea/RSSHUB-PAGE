
---
title: '前端常用的函数封装js篇（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2401'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 18:36:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=2401'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">在字符串指定位置插入字符</h2>
<p>方法有多种：</p>
<ol>
<li>先使用split将字符串分割成数组，然后在指定位置索引上添加字符，最后使用join将数组转换成字符串</li>
<li>使用silce方法分别将字符0到指定索引和指定索引到字符串尾巴的字符串分割出来，再讲插入字符拼接在两个字符串中间</li>
</ol>
<p>出于代码简洁性考虑这里提供slice方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @Description: 在字符串指定位置插入字符
 * @param &#123;String&#125; character 原字符串
 * @param &#123;Number&#125; site 要插入的字符的位置
 * @param &#123;String&#125; newStr 想要插入的字符
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insertStr</span>(<span class="hljs-params">character, site, newStr</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> character != <span class="hljs-string">"string"</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'type error!'</span>);
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-keyword">return</span> character.slice(<span class="hljs-number">0</span>, site) + newStr + character.slice(site);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">身份证号验证</h2>
<p>这里只检查身份证号码是否符合规范，包括长度，类型。</p>
<p>身份证号码规范：身份证号码为15位或者18位，15位时全为数字，18位前17位为数字，最后一位是校验位，可能为数字或字符X</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @Description: 身份证号验证
 * @param &#123;String&#125; val 需要验证的号码
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkCardNo</span>(<span class="hljs-params">val</span>) </span>&#123;
  <span class="hljs-keyword">var</span> reg = <span class="hljs-regexp">/(^\d&#123;15&#125;$)|(^\d&#123;18&#125;$)|(^\d&#123;17&#125;(\d|X|x)$)/</span>;
  <span class="hljs-keyword">return</span> reg.test(val)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">浏览器判断</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">qfyParseUA</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> u = navigator.userAgent;
  <span class="hljs-keyword">var</span> u2 = navigator.userAgent.toLowerCase();
  <span class="hljs-keyword">return</span> &#123; <span class="hljs-comment">//移动终端浏览器版本信息</span>
    <span class="hljs-attr">trident</span>: u.indexOf(<span class="hljs-string">'Trident'</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">//IE内核</span>
    <span class="hljs-attr">presto</span>: u.indexOf(<span class="hljs-string">'Presto'</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">//opera内核</span>
    <span class="hljs-attr">webKit</span>: u.indexOf(<span class="hljs-string">'AppleWebKit'</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">//苹果、谷歌内核</span>
    <span class="hljs-attr">gecko</span>: u.indexOf(<span class="hljs-string">'Gecko'</span>) > -<span class="hljs-number">1</span> && u.indexOf(<span class="hljs-string">'KHTML'</span>) == -<span class="hljs-number">1</span>, <span class="hljs-comment">//火狐内核</span>
    <span class="hljs-attr">mobile</span>: !!u.match(<span class="hljs-regexp">/AppleWebKit.*Mobile.*/</span>), <span class="hljs-comment">//是否为移动终端</span>
    <span class="hljs-attr">ios</span>: !!u.match(<span class="hljs-regexp">/\(i[^;]+;( U;)? CPU.+Mac OS X/</span>), <span class="hljs-comment">//ios终端</span>
    <span class="hljs-attr">android</span>: u.indexOf(<span class="hljs-string">'Android'</span>) > -<span class="hljs-number">1</span> || u.indexOf(<span class="hljs-string">'Linux'</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">//android终端或uc浏览器</span>
    <span class="hljs-attr">iPhone</span>: u.indexOf(<span class="hljs-string">'iPhone'</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">//是否为iPhone或者QQHD浏览器</span>
    <span class="hljs-attr">iPad</span>: u.indexOf(<span class="hljs-string">'iPad'</span>) > -<span class="hljs-number">1</span>, <span class="hljs-comment">//是否iPad</span>
    <span class="hljs-attr">webApp</span>: u.indexOf(<span class="hljs-string">'Safari'</span>) == -<span class="hljs-number">1</span>, <span class="hljs-comment">//是否web应该程序，没有头部与底部</span>
    <span class="hljs-attr">iosv</span>: u.substr(u.indexOf(<span class="hljs-string">'iPhone OS'</span>) + <span class="hljs-number">9</span>, <span class="hljs-number">3</span>),
    <span class="hljs-attr">weixin</span>: u2.match(<span class="hljs-regexp">/MicroMessenger/i</span>) == <span class="hljs-string">"micromessenger"</span>,
    <span class="hljs-attr">ali</span>: u.indexOf(<span class="hljs-string">'AliApp'</span>) > -<span class="hljs-number">1</span>,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">动态加载JS</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @param &#123;String&#125; url JS路径
 * @param &#123;Function&#125; callback JS加载完回调方法
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">qfyLoadScript</span>(<span class="hljs-params">url, callback</span>) </span>&#123;
  <span class="hljs-keyword">var</span> script = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"script"</span>);
  script.type = <span class="hljs-string">"text/javascript"</span>;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> (callback) != <span class="hljs-string">"undefined"</span> && <span class="hljs-keyword">typeof</span> callback == <span class="hljs-string">"function"</span>) &#123;
    <span class="hljs-keyword">if</span> (script.readyState) &#123;
      script.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span> (script.readyState == <span class="hljs-string">"loaded"</span> || script.readyState == <span class="hljs-string">"complete"</span>) &#123;
          script.onreadystatechange = <span class="hljs-literal">null</span>;
          callback();
        &#125;
      &#125;;
    &#125; <span class="hljs-keyword">else</span> &#123;
      script.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        callback();
      &#125;;
    &#125;
  &#125;
  script.src = url;
  <span class="hljs-built_in">document</span>.body.appendChild(script);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">移动端自适应</h2>
<p>使用rem做移动自适应，rem（font size of the root element）是指相对于根元素的字体大小的单位。简单的说它就是一个相对单位，1rem = 根元素的字体大小的单位，比如html&#123;font-size:20px;&#125;,那么1rem = 20px。</p>
<p>由于UI移动端一般用iphone6来做图，所有我们已iphone6的宽度375为基数来设置需要自适应元素的rem值，然后根据机型宽度和iphone6宽度的比例来设置根元素的字体大小。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setRem</span>(<span class="hljs-params">remNum</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> remNum != <span class="hljs-string">"number"</span>) &#123;
    remNum = <span class="hljs-number">20</span>
  &#125;
  (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">doc, win</span>) </span>&#123;
    <span class="hljs-keyword">var</span> docEl = doc.documentElement,
      resizeEvt = <span class="hljs-string">'orientationchange'</span> <span class="hljs-keyword">in</span> <span class="hljs-built_in">window</span> ? <span class="hljs-string">'orientationchange'</span> : <span class="hljs-string">'resize'</span>,
      recalc = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> clientWidth = docEl.clientWidth; <span class="hljs-comment">//win.screen.width;//</span>
        <span class="hljs-keyword">if</span> (!clientWidth) <span class="hljs-keyword">return</span>;
        docEl.style.fontSize = remNum * (clientWidth / <span class="hljs-number">375</span>) + <span class="hljs-string">'px'</span>;
      &#125;;
    <span class="hljs-keyword">if</span> (!doc.addEventListener) <span class="hljs-keyword">return</span>;
    win.addEventListener(resizeEvt, recalc, <span class="hljs-literal">false</span>);
    doc.addEventListener(<span class="hljs-string">'DOMContentLoaded'</span>, recalc, <span class="hljs-literal">false</span>);
  &#125;)(<span class="hljs-built_in">document</span>, <span class="hljs-built_in">window</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">控制input文本框只能输入整数</h2>
<pre><code class="hljs language-js copyable" lang="js"><input onkeyup=<span class="hljs-string">"if(this.value.length==1)&#123;this.value=this.value.replace(/[^1-9]/g,'')&#125;else&#123;this.value=this.value.replace(/\D/g,'')&#125;"</span> onafterpaste=<span class="hljs-string">"if(this.value.length==1)&#123;this.value=this.value.replace(/[^1-9]/g,'')&#125;else&#123;this.value=this.value.replace(/\D/g,'')&#125;"</span>>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            
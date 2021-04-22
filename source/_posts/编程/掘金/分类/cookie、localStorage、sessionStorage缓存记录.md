
---
title: 'cookie、localStorage、sessionStorage缓存记录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7530'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 19:34:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=7530'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前言：最近在做项目的时候遇到一个问题，将项目嵌入到一个平台，该平台A的用户在项目B下可能拥多个不同角色的账户，每个账户的token不同，每个账户下的操作需要携带该账户的的token信息，因此采取的方案就是使用本地缓存localStorage存储token信息，但是又出现了另一个问题，在同一浏览器不同页面切换到不同账户时，页面a账户进行操作拿到的是页面b账户的token值，同一浏览器不同页面之间的token值串错，因此后续解决方案是用sessionStorage进行存储，保证了不同会话之间的token值相互独立。<br></p>
<blockquote>
<p>用户1在平台A的登录plat_token + 用户1在项目B上的某一账户ID   ->  用户1在项目B下的某账号对应的唯一item_token</p>
</blockquote>
<h1 data-id="heading-0">cookie</h1>
<h2 data-id="heading-1">cookie使用方法</h2>
<h3 data-id="heading-2">JavaScript原生的用法</h3>
<p>Cookie 以名/值对形式存储。JavaScript 可以使用 document.cookie 属性来创建 、读取、及删除 cookie。</p>
<pre><code class="copyable">JavaScript 中，创建 cookie如下所示：
document.cookie="itemToken=10001110";

为 cookie 添加一个过期时间（以 UTC 或 GMT 时间）
document.cookie="itemToken=10001110; expires=Thu, 22 Apr 2021 12:00:00 GMT";

使用 path 参数告诉浏览器 cookie 的路径。默认情况下，cookie 属于当前页面。
document.cookie="itemToken=10001110; expires=Thu, 22 Apr 2021 12:00:00 GMT; path=/";
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">设置cookie的值</h3>
<pre><code class="copyable">const setCookie = (name,value,extime) =>&#123;
  let SetTime = new Date();                                         //设置过期时间
  SetTime.setTime(SetTime.getTime()+(extime*24*60*60*1000));        //设置过期时间
  let expires = "expires="+SetTime.toGMTString();                   //设置过期时间
  document.cookie = name + "=" + value + "; " + expires;            //创建一个cookie
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">获取指定名称的cookie值</h3>
<pre><code class="copyable">const getcookie = (objname)=>&#123; // 获取指定名称的cookie的值  
    let arrstr = document.cookie.split(";");  
    let res = null  
    for(var i = 0;i < arrstr.length;i ++)&#123;
      let temp = arrstr[i].split("=");    
      if(temp[0] == objname) &#123;      
        res = unescape(temp[1])    
      &#125;   
    &#125;  
    return res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">localStorage</h1>
<pre><code class="copyable">localStorage.getItem(keyName);  //获取指定key的本地存储的值

localStorage.setItem(keyName,value);  //将value存储到key字段中

localStorage.removeItem(keyName);  //删除指定ke的本地存储的值
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">sessionStorage</h1>
<pre><code class="copyable">sessionStorage.getItem(keyName);  //获取指定key的本地存储的值

sessionStorage.setItem(keyName,value); //将value存储到key字段中

sessionStorage.removeItem(keyName); //删除指定ke的本地存储的值
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">其他</h1>
<h2 data-id="heading-8">三者的异同</h2>



































<table><thead><tr><th>特性</th><th>cookie</th><th>localStorage</th><th>sessionStorage</th></tr></thead><tbody><tr><td>数据的生命期</td><td>可设置失效时间，默认是关闭浏览器后失效</td><td>除非被清除，否则永久保存</td><td>仅在当前会话下有效，关闭页面或浏览器后被清除</td></tr><tr><td>存放数据大小</td><td>4K左右</td><td>一般为5MB</td><td>一般为5MB</td></tr><tr><td>与服务器端通信</td><td>每次都会携带在HTTP头中，如果使用cookie保存过多数据会带来性能问题</td><td>仅在客户端（即浏览器）中保存，不参与和服务器的通信</td><td>仅在客户端（即浏览器）中保存，不参与和服务器的通信</td></tr><tr><td>易用性</td><td>需要程序员自己封装，源生的Cookie接口不友好</td><td>源生接口可以接受，亦可再次封装来对Object和Array有更好的支持</td><td>源生接口可以接受，亦可再次封装来对Object和Array有更好的支持</td></tr></tbody></table>
<h2 data-id="heading-9">缓存原理及优缺点</h2>
<p>原理：先查询缓存中有没有要的数据，如果有，就直接返回缓存中的数据。如果缓存中没有要的数据，才去查询数据库，将得到数据先存放到缓存中，然后再返回给后端。</p>
<p>优点：</p>
<ol>
<li>减少了对数据库的读操作，数据库的压力降低</li>
<li>加快了响应速度  </li>
</ol>
<p>缺点：</p>
<ol>
<li>因为内存断电就清空数据，存放到内存中的数据可能丢失</li>
<li>缓存中的数据可能与数据库中数据不一致</li>
<li>内存的成本高 </li>
<li>内存容量相对硬盘小</li>
</ol>
<h2 data-id="heading-10">参考链接</h2>
<p><a href="https://segmentfault.com/a/1190000002723469" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000000…</a><br>
<a href="https://juejin.cn/post/6844903516826255373" target="_blank">juejin.cn/post/684490…</a><br>
<a href="https://segmentfault.com/a/1190000010098593?utm_source=sf-similar-article" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            
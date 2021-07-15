
---
title: '【收藏就会】浏览器WebStorage存储技术使用指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42a3704f4522426096696990b19de2f6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 15:02:20 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42a3704f4522426096696990b19de2f6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<h2 data-id="heading-0">背景</h2>
<p>在我们网页刷新的时候，页面上所有数据都会被清空。而在一些网站的搜索上，即使是你关闭了浏览器，下次打开时还是会有数据在页面上，如下图一个简单的搜索记录功能，当用户进行搜索时，所有的记录会被保存起来，不论是刷新还是重启浏览器，搜索的历史记录依旧显示在页面上。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42a3704f4522426096696990b19de2f6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一系列的需求都可以通过浏览器的存储技术来实现。本篇文章，我们就来学习下浏览器存储技术中的<code>WebStorage</code> ，全面了解它的基础使用和进阶，以及如何利用这些方法实践两个常见场景。介绍使用方法的同时，我也会以封装一个<code>工具类</code>的方式来统一所有调用方法，学会这一点，可以让你在业务开发调用的时候更加方便。</p>
<h2 data-id="heading-1">为什么选择WebStorage？</h2>
<p>我们知道，常见的轻量浏览器存储技术包括<code>Cookie</code>和<code>WebStorage</code>。那么，我们为什么选择<code>WebStorage</code>而不是<code>Cookie</code>呢？</p>
<p>首先，<code>WebStorage</code>在使用上相比Cookie更友好，不再需要刻意封装成一些工具库来对一些常见的操作进行简化的调用，尽管市面上已经有很多成熟的方案帮我们做了这件事情。</p>
<p>其次，<code>chrome(80+)</code>浏览器默认屏蔽所有<code>三方Cookie</code>已经不是什么值得震惊的事情了，随着这一次改动，<code>Cookie</code>无疑又被斩断了一只有力的手臂。
不了解的小伙伴，强烈安利一手这篇文章，里面非常详细的对其进行了一些分析。<a href="https://juejin.cn/post/6844904128557105166#heading-5" target="_blank" title="https://juejin.cn/post/6844904128557105166#heading-5">当浏览器全面禁用三方 Cookie</a>。</p>
<p>除此之外，使用<code>Cookie</code>还需要面临以下问题：</p>
<ul>
<li>存放数据太小，<code>Cookie</code>的存储大小只有<code>4k</code>，如果你需要存储的数据非常多，那么很显然并不能够满足你的需求，且一般没有人这么做。</li>
<li>每次都会携带在<code>HTTP请求头</code>中，会与服务端进行一些交互，当我单纯存储一些本地数据时，很明显会造成性能浪费。</li>
</ul>
<p>而<code>WebStorage</code>在浏览器中的主要功能，就是在客户端进行临时和永久的数据存储，不直接参与服务端的通信和交互，因此可以很好地避免一些劫持的安全风险。同时，也具备了良好的存储容量，能胜任绝大部份的应用场景，且每个存储都是挂载在对应的空间当中，彼此独立去管理对应的数据，不会造成串数据和错数据的一些困扰。</p>
<p>基于此，如果有需要存储到本地的一些数据，还是尽可能使用<code>WebStorage</code>来做为存储的首要选择。</p>
<h2 data-id="heading-2">基础使用</h2>
<p>在本章节，我会从一个封装工具类的角度带大家学习一些webStorage的基础使用技巧。这里也先分享一个在线的源码地址链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fplay%3F%23code%2FJYWwDg9gTgLgBAbzjAFlCB3AoldUCyApgM7ECGA5oQDRwpnEDKMUwAdhcAGYCecAvnC7oQcAOQA6APQBXGMAA2YgFDL2MQlC5kAxoTjNolQgCEIEGMyhkwAYQhsuwComVw4ICABNCALnHEJMTADmJwAD7iChA6ZErUbsighBBy-mwyIABGmsr8quqa2noGMEZUjGQAboQAYtAgZPAIiYlSAFTtcIDj8YD45oBvpoAvqXDtUonyICQwZODpmTlQqu4dXQACbDP6gA6mgHbGgHnagMryI2PuXk1k-mRsPHmqOgoMxHC2MsRlIIbWVK7uYKxVTX0UEIZC8n2M-nBVESf2AAI0cB0DicFEhZS%2BpnMlhYNnsjmcMP%2BgLgrwhcAy2VyvyJCIAjjILBdyfNcokkWw3lAZDp0XAABQASh%2B7jg3H5GHYXkwcAAZDK4BK2FKMBJorEFFD9HKFZLMBJAqQQmxNUKWiKRahgMQJMDQZq4ABeHVKvVquKaxLuQSEBSBYXm1DobC4aBEUjGPliQDK%2BoBZJUA9c6AYI1AHrpgHlbQATkYALNUAMP%2BAA9NAKs2gAjbQCcsYALRUAAjqK5V7QDR8oAgBjEAs9AkS%2BTanU9XUA7cGANeVAAJGgEhzADWhBuIrWwJgMigHLggD21N7lQhRwC0cgPhzxAGNpgAgVDsnOBUGAAaRHxEF-gAgrgyDwADyc9gUAB8-rgE6nbDgAHksgArQg8iR11PS1rVtMF0WMRsvSWOAVg7OAewHAEFBkQh4NWN9pyeAddm3XdEgPAA1OJUNPU0m0wj9vz-ADkNIvkQJtEFwMXKDmzbdp4MAXCVAGnNQA0ZU1QAQt12dCwDIaxRHZFFSkXMwLCsXFkQJMc9yyLEFLAfkpOcNFZPUnE7CUigBX8KoIGALwX2ICUYB0FAtKMiRPB8cjzXcWI-TEA1glCXwmwDFArSYu0IO%2BJ1Kz1byjQ9NyRSyW1BwAbhg80PP0MQ3SUPzYvcRiwPtcLdRVTKYpy%2BKQSSpt-LgHxtBkBQYGynLA0wHA8DDcgqEjWNAFlEwA7f0E5zCEAKnNAFjFfrAC5lQBQxSzQB75UAU7lAAGLQBT80AAnlAFNFfr6zY2LyrISrzXyAKgu0lwnVOlsYLgsc4EAFfjZ1jQANbUACoVAGS9QByTUAeB10Mop4KQWfD3GCAAvQgz2ZSkoBfSjkEC0DmM1VVCA4VBLvcRJ6GIABJDQQD5dd-HvDgTLgNSIAUEEPzNEUYbyhHQsICRMc-DA2AABXQMBNBgHh8ZHNjW2WdsbtE8SZjgdc4EAPui%2Bqe5711FiS4Do-QZbllXAbgQIYBxwg8YJrWWAfWgVdckUxT5TGrAfbhedNs3UocN4teqQgABFzl0jFKhqeooEaeAnWp2KJimGYwHSQgMDgD2NEFCQDwAFWSQUEhymrPeVki0Nio63PZYhycZ6IKD5cgaljshaC813K4baq6ZCxd9UIHXcb5nhaAAKUYT8ADl9SNjhbbL2vzgFHaBDgH0-WDi00FakMCCCCMxEAAHTAEDIl7BLOaZAFg5QB6U0AQGMe-7wfWGH3hAE7TPMs0Ad%2BiVtjXZ68Oy6OPgnsRJu1YxKVyWeyfjsBW39fpwBel-dwowCKt11iAG8idHRwCuDwR8HdCZD2Mv4BBkQMgKAUC%2BAu8B2QaDYI1GS3tXZ%2BwDhEZkeDEGnwHr-QIDE4bBRYhiBOMD27rgnk2C2xDkYwAAPwSFDm8cOsp5RsCjjHQE8ck4pyFAAWkRA4EhMBRHJHEeAOAj4nSMVOpoyYqQYAO3nkFYEngaiwI7pPdwMNcEKCbHnexrd3yqNIYIkRu8yARBwfVJx0F343UAN%2BegATNMAABygBDcwgSMOAP8xaiEluE4BkC9yWIgNY7hI50EX2Mi%2BC2jFMY2J4WY3KrD8oMyYlYwgJT%2BbOLfu5egHBam4xvIwRByDUEGyJhQWgDhbDNKoP4Pk5MvDERQn4AwQoHTPg6f4vBtAsgMEIBM1CQjLjXDMYQjO0xEGMQPLA9p3T6nHWtNrOpnc4ADKGWDHxfjSYrLWYQXhQT3IU3EuePBgoXyN3YcYCQ9wQRQEFG-VsyhrpdBrHxWMmpADQcoJe4jw3BQMIAAD0gLAGqhA6oNWeK8d4mogA" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/play?#code/JYWwDg9gTgLgBAbzjAFlCB3AoldUCyApgM7ECGA5oQDRwpnEDKMUwAdhcAGYCecAvnC7oQcAOQA6APQBXGMAA2YgFDL2MQlC5kAxoTjNolQgCEIEGMyhkwAYQhsuwComVw4ICABNCALnHEJMTADmJwAD7iChA6ZErUbsighBBy-mwyIABGmsr8quqa2noGMEZUjGQAboQAYtAgZPAIiYlSAFTtcIDj8YD45oBvpoAvqXDtUonyICQwZODpmTlQqu4dXQACbDP6gA6mgHbGgHnagMryI2PuXk1k-mRsPHmqOgoMxHC2MsRlIIbWVK7uYKxVTX0UEIZC8n2M-nBVESf2AAI0cB0DicFEhZS+pnMlhYNnsjmcMP+gLgrwhcAy2VyvyJCIAjjILBdyfNcokkWw3lAZDp0XAABQASh+7jg3H5GHYXkwcAAZDK4BK2FKMBJorEFFD9HKFZLMBJAqQQmxNUKWiKRahgMQJMDQZq4ABeHVKvVquKaxLuQSEBSBYXm1DobC4aBEUjGPliQDK+oBZJUA9c6AYI1AHrpgHlbQATkYALNUAMP+AA9NAKs2gAjbQCcsYALRUAAjqK5V7QDR8oAgBjEAs9AkS+TanU9XUA7cGANeVAAJGgEhzADWhBuIrWwJgMigHLggD21N7lQhRwC0cgPhzxAGNpgAgVDsnOBUGAAaRHxEF-gAgrgyDwADyc9gUAB8-rgE6nbDgAHksgArQg8iR11PS1rVtMF0WMRsvSWOAVg7OAewHAEFBkQh4NWN9pyeAddm3XdEgPAA1OJUNPU0m0wj9vz-ADkNIvkQJtEFwMXKDmzbdp4MAXCVAGnNQA0ZU1QAQt12dCwDIaxRHZFFSkXMwLCsXFkQJMc9yyLEFLAfkpOcNFZPUnE7CUigBX8KoIGALwX2ICUYB0FAtKMiRPB8cjzXcWI-TEA1glCXwmwDFArSYu0IO+J1Kz1byjQ9NyRSyW1BwAbhg80PP0MQ3SUPzYvcRiwPtcLdRVTKYpy+KQSSpt-LgHxtBkBQYGynLA0wHA8DDcgqEjWNAFlEwA7f0E5zCEAKnNAFjFfrAC5lQBQxSzQB75UAU7lAAGLQBT80AAnlAFNFfr6zY2LyrISrzXyAKgu0lwnVOlsYLgsc4EAFfjZ1jQANbUACoVAGS9QByTUAeB10Mop4KQWfD3GCAAvQgz2ZSkoBfSjkEC0DmM1VVCA4VBLvcRJ6GIABJDQQD5dd-HvDgTLgNSIAUEEPzNEUYbyhHQsICRMc-DA2AABXQMBNBgHh8ZHNjW2WdsbtE8SZjgdc4EAPui+qe5711FiS4Do-QZbllXAbgQIYBxwg8YJrWWAfWgVdckUxT5TGrAfbhedNs3UocN4teqQgABFzl0jFKhqeooEaeAnWp2KJimGYwHSQgMDgD2NEFCQDwAFWSQUEhymrPeVki0Nio63PZYhycZ6IKD5cgaljshaC813K4baq6ZCxd9UIHXcb5nhaAAKUYT8ADl9SNjhbbL2vzgFHaBDgH0-WDi00FakMCCCCMxEAAHTAEDIl7BLOaZAFg5QB6U0AQGMe-7wfWGH3hAE7TPMs0Ad+iVtjXZ68Oy6OPgnsRJu1YxKVyWeyfjsBW39fpwBel-dwowCKt11iAG8idHRwCuDwR8HdCZD2Mv4BBkQMgKAUC+Au8B2QaDYI1GS3tXZ+wDhEZkeDEGnwHr-QIDE4bBRYhiBOMD27rgnk2C2xDkYwAAPwSFDm8cOsp5RsCjjHQE8ck4pyFAAWkRA4EhMBRHJHEeAOAj4nSMVOpoyYqQYAO3nkFYEngaiwI7pPdwMNcEKCbHnexrd3yqNIYIkRu8yARBwfVJx0F343UAN+egATNMAABygBDcwgSMOAP8xaiEluE4BkC9yWIgNY7hI50EX2Mi+C2jFMY2J4WY3KrD8oMyYlYwgJT+bOLfu5egHBam4xvIwRByDUEGyJhQWgDhbDNKoP4Pk5MvDERQn4AwQoHTPg6f4vBtAsgMEIBM1CQjLjXDMYQjO0xEGMQPLA9p3T6nHWtNrOpnc4ADKGWDHxfjSYrLWYQXhQT3IU3EuePBgoXyN3YcYCQ9wQRQEFG-VsyhrpdBrHxWMmpADQcoJe4jw3BQMIAAD0gLAGqhA6oNWeK8d4mogA" ref="nofollow noopener noreferrer">Storage操作封装实践代码</a></p>
<p>然后，在浏览器调试工具的<code>Application</code>菜单当中，左侧可以看到<code>Storage</code>的调试版，其中就有我们通过<code>API</code>保存到存储当中的值，可以在这里进行调试。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76e394b991624d31b9f79a73a89f349b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">环境支持 & 初始化</h3>
<p>在开始前第一步肯定是需要做一些环境检查，不然在部分不支持这些特性的浏览器下是无法使用的，<a href="https://link.juejin.cn/?target=http%3A%2F%2Fcaniuse.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://caniuse.com/" ref="nofollow noopener noreferrer">这个可以在caniuse</a>上查看一些浏览器支持程度。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcd3eea3212e43d394cb332760f601c3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而在我们的代码中，也要加上一层容错判断，如果需要对其做兼容的话可以进行一个处理降解。如<code>Cookie</code>或者是<code>IE6中</code>的<code>userData持久化用户数据</code>。</p>
<p>下面是一个比较简单的判断，也可以封装成为一个简单的函数来进行调用。如果浏览器不支持则抛出一些错误到控制台当中。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CustomStorage</span> </span>&#123;
  <span class="hljs-keyword">private</span> readStorage: Storage

  <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'当前环境非浏览器，无法消费全局window实例。'</span>)
    &#125;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>.localStorage) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'当前环境非无法使用localStorage'</span>)
    &#125;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>.sessionStorage) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'当前环境非无法使用sessionStorage'</span>)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当环境支持使用<code>WebStorage</code>的条件下，就可以初始化默认的一些数据了，在这里选择使用哪个<code>Storage</code>，同时将配置保存起来。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> StorageBootStrapConfig &#123;
  <span class="hljs-comment">/** 当前环境 */</span>
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'session'</span> | <span class="hljs-string">'local'</span>,
  
  <span class="hljs-comment">/** 超时时间 */</span>
  <span class="hljs-attr">timeout</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-comment">/**
   * 初始化Storage的数据
   * <span class="hljs-doctag">@param </span>config StorageBootStrapConfig
   */</span>
 bootStrap (config: StorageBootStrapConfig): <span class="hljs-built_in">void</span> &#123;
  <span class="hljs-keyword">switch</span> (config.mode) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'session'</span>:
      <span class="hljs-built_in">this</span>.readStorage = <span class="hljs-built_in">window</span>.sessionStorage
      <span class="hljs-keyword">break</span>;

    <span class="hljs-keyword">case</span> <span class="hljs-string">'local'</span>:
      <span class="hljs-built_in">this</span>.readStorage = <span class="hljs-built_in">window</span>.localStorage
      <span class="hljs-keyword">break</span>;
  
    <span class="hljs-keyword">default</span>:
      throwErrorMessage(<span class="hljs-string">'当前配置的mode未再配置区内，可以检查传入配置。'</span>)
      <span class="hljs-keyword">break</span>;
  &#125;
  <span class="hljs-built_in">this</span>.config = config
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，通过<code>bootstrap</code>来初始化当前的一些配置后，在页面里就可以通过当前实例<code>customStorage</code>去使用一些函数方法。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> CustomStorage <span class="hljs-keyword">from</span> <span class="hljs-string">'web-storage-db'</span>

<span class="hljs-keyword">const</span> customStorage = <span class="hljs-keyword">new</span> CustomStorage()

customStorage.bootStrap(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'local'</span>,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">3000</span>,
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> customStorage
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">JSON序列化</h3>
<p>对于<code>WebStorage</code>来说，值的存储是非常依赖<code>JSON的序列化</code>。如下图:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e68369653b8b449983987f87171930d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当存入<code>Object类型</code>时，存入的数据会变成其类型的字符串，因为<code>WebStorage</code>的存储只能以<code>字符串</code>的形式存在，所以我们想要存储引用类型的数据，就需要依赖<code>JSON序列化</code>的能力了。通过<code>stringify</code>和<code>parse</code>等一些方法对值做出处理，就能很好的存储一些引用类型。</p>
<p>但是也有一些<code>JSON.stringify</code>不友好的类型数据，尽量不要去存储，如<code>undefined</code>, <code>Function</code>, <code>Symbol</code>等等，我在这里也写了一个简单的函数用于检查存储值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 判断当前值是否能够呗JSON.stringify识别
 * <span class="hljs-doctag">@param </span>data 需要判断的值
 * <span class="hljs-doctag">@returns </span>前参数是否可以string化
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hasStringify</span> (<span class="hljs-params">data: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">if</span> (data === <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-keyword">if</span> (data <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-keyword">if</span> (isSymbol(data)) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>isSymbol</code>方法做了一个<code>Symbol</code>类型值的判断。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 判断当前类型是否是Symbol
 * <span class="hljs-doctag">@param </span>val 需要判断的值
 * <span class="hljs-doctag">@returns </span>当前参数是否是symbol
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isSymbol</span>(<span class="hljs-params">val: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'symbol'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">存入数据</h3>
<p>如果需要将数据存储到<code>WebStorage</code>当中，其本身提供一个<code>setItem</code>的API 来做这件事情，在这里以<code>localStorage</code>为例子，可以通过以下形式来存入一个值：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// # 原生</span>
<span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">'key'</span>, <span class="hljs-string">'value'</span>)

<span class="hljs-comment">// # attribute形式存储</span>
<span class="hljs-built_in">window</span>.localStorage[<span class="hljs-string">'key1'</span>] = <span class="hljs-string">'value'</span>
<span class="hljs-built_in">window</span>.localStorage.name = <span class="hljs-string">'wangly19'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e76f04ac41c417e9cf85963d9e44711~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而我们在使用中，显然不会去使用<code>原生API</code>的方式处理，绝大部分都会封装成一个<code>工具方法</code>，来处理一些重复性的工作。就比如在下面的封装中，我就对存储数据的内容做了一层包装，加入了<code>JSON序列化数据</code>和<code>过期时间</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
   * 设置当前
   * <span class="hljs-doctag">@param </span>key 设置当前存储key
   * <span class="hljs-doctag">@param </span>value 设置当前存储value
   */</span>
 <span class="hljs-function"><span class="hljs-title">setItem</span>(<span class="hljs-params">key: <span class="hljs-built_in">string</span>, value</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (hasStringify(value)) &#123;
    <span class="hljs-keyword">const</span> saveData: StorageSaveFormat = &#123;
      <span class="hljs-attr">timestamp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime(),
      <span class="hljs-attr">data</span>: value
    &#125;
    <span class="hljs-built_in">console</span>.log(saveData, <span class="hljs-string">'saveData'</span>)
    <span class="hljs-built_in">this</span>.readStorage.setItem(key, <span class="hljs-built_in">JSON</span>.stringify(saveData))
  &#125; <span class="hljs-keyword">else</span> &#123;
    throwErrorMessage(<span class="hljs-string">'需要存储的data不支持JSON.stringify方法，请检查当前数据'</span>)
  &#125;
&#125;


<span class="hljs-comment">// 使用</span>
customStorage.setItem(<span class="hljs-string">'setItem'</span>, [<span class="hljs-number">1</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/649f9dc4088744008db0026d27c382e2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">读取数据</h3>
<p>既然有存入，那么必然会有读取，我们可以通过<code>getItem</code>或者是<code>Object</code>的形式进行值的读取。下面，我们就来看看三种方式的实例吧。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1834bb5cbc2460da17b87831502d45b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">'person'</span>, <span class="hljs-built_in">JSON</span>.stringify(&#123; 
    <span class="hljs-attr">name</span>: <span class="hljs-string">'wangly19'</span>, 
    <span class="hljs-attr">age</span>: <span class="hljs-number">22</span> 
&#125;))

<span class="hljs-keyword">const</span> person = <span class="hljs-built_in">window</span>.localStorage.getItem(<span class="hljs-string">'person'</span>)


<span class="hljs-built_in">JSON</span>.parse(person)

<span class="hljs-comment">// &#123; name: "wangly19", age: 22 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90141ce4b01243bbb6beb2f7abff718a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面是<code>普通的使用方式</code>，而我们<code>封装</code>时，也会对存入的数据进行一些<code>判断</code>，将存入的JSON数据做一个<code>解析化的处理</code>，直接返回<code>解析后的数据</code>，更加的方便和易于使用。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
  * 获取数据
  * <span class="hljs-doctag">@param </span>key 获取当前数据key
  * <span class="hljs-doctag">@returns </span>存储数据
*/</span>
getItem<T = <span class="hljs-built_in">any</span>>(key: <span class="hljs-built_in">string</span>): T | <span class="hljs-literal">null</span> &#123;
  <span class="hljs-keyword">const</span> content: StorageSaveFormat | <span class="hljs-literal">null</span> = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">this</span>.readStorage.getItem(key))
  <span class="hljs-keyword">return</span> content?.data || <span class="hljs-literal">null</span>
&#125;

<span class="hljs-comment">// # 使用</span>
customStorage.getItem(<span class="hljs-string">'setItem'</span>) <span class="hljs-comment">// [1]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">移除</h3>
<p>对于存储的移除不仅可以使用<code>removeItem</code>，<code>delete</code>等操作来对存储中的值进行<code>移除</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// # removeItem</span>
<span class="hljs-built_in">window</span>.localStorage.removeItem(<span class="hljs-string">'person'</span>)

<span class="hljs-comment">// # delete</span>
<span class="hljs-keyword">delete</span> <span class="hljs-built_in">window</span>.localStorage.person
<span class="hljs-keyword">delete</span> <span class="hljs-built_in">window</span>.localStorage[<span class="hljs-string">'peson'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还可以使用clear来清除存储中所有的数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.localStorage.clear()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，如果移除某条数据时<code>Storage</code>没有存储当前<code>key</code>的数据，那么我们就不需要去执行当前<code>移除数据</code>的操作。我们来看下面封装的<code>removeItem</code>方法，我加入了一层<code>值是否存在</code>的判断来决定是不是真的需要执行移除这步操作。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
   * 移除一条数据
   * <span class="hljs-doctag">@param </span>key 移除key
   */</span>
<span class="hljs-function"><span class="hljs-title">removeItem</span>(<span class="hljs-params">key: <span class="hljs-built_in">string</span></span>)</span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.hasItem(key)) &#123;
      <span class="hljs-built_in">this</span>.readStorage.removeItem(key)
  &#125;
&#125;

<span class="hljs-comment">/**
 * 清除存储中所有数据
 */</span>
<span class="hljs-function"><span class="hljs-title">clearAll</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-built_in">this</span>.readStorage.clear()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">长度length</h3>
<p><code>WebStorage</code>自带<code>length</code>属性，可以获取当前<code>Storage</code>的长度。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.localStorage.length

<span class="hljs-comment">/**
   * 返回当前存储库大小
   * <span class="hljs-doctag">@returns <span class="hljs-variable">number</span></span>
*/</span>
size(): number &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.readStorage.length
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aecc758c5ec6415c8653c6669deb259a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">keys 和 values</h3>
<p>看到这里，很多朋友应该知道会怎么实现了吧？没错，通过<code>Object.keys</code>和<code>Object.values</code>可以拿到当前<code>Storage</code>中所有的<code>key</code>和<code>value</code>。部分<code>埋点SDK</code>会有上报<code>Storage</code>来做数据筛选。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">localStorage</span>)
<span class="hljs-comment">// (4) ["wwwPassLogout", "BIDUPSID", "BDSUGSTORED", "safeIconHis"]</span>
<span class="hljs-built_in">Object</span>.values(<span class="hljs-built_in">localStorage</span>)
<span class="hljs-comment">// (4) ["0", "30B3EE0AF6EE9F4F89EF16486C288502", "[&#123;\"q\":\"localstorage%20%E8%BF%87%E6%9C%9F%E6%97%B6%…:\"new%20dateshijianchuo\",\"s\":4,\"t\":206989341223&#125;]", ""]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其次就是通过<code>key(index)</code>方法，可以直接获取某个位置的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.localStorage.key(<span class="hljs-number">0</span>)
<span class="hljs-built_in">window</span>.localStorage.key(<span class="hljs-number">1</span>)
<span class="hljs-built_in">window</span>.localStorage.key(<span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>工具类</code>当中，我也对其进行了<code>封装</code>，可以使用<code>getKeys</code>, <code>getValues</code>来获取存储空间的所有<code>Key</code>和<code>Value</code>的集合。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
   * 获取所有key
   * <span class="hljs-doctag">@returns </span>回storage当中所有key集合
   */</span>
getKeys(): <span class="hljs-built_in">Array</span> < <span class="hljs-built_in">string</span> > &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>.readStorage)
&#125;

<span class="hljs-comment">/**
 * 获取所有value
 * <span class="hljs-doctag">@returns </span>所有数据集合
 */</span>
<span class="hljs-function"><span class="hljs-title">getValues</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.values(<span class="hljs-built_in">this</span>.readStorage)
&#125;

<span class="hljs-comment">// # 使用</span>
customStorage.getKeys()
customStorage.getValues()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19dd2494d9984daf9b58bbfde0b28022~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">是否存在某个属性？</h3>
<p>判断当前<code>Storage</code>中是否存在某个属性，很多同学都是通过<code>getItem</code>去获取一个值，然后判断value是否存在进行一个判断。</p>
<p>但是很显然，我们能够像操作Object的<code>hasOwnProperty</code>方法来判断当前是否有这个属性，由于返回的是boolean类型，相对来说更易于理解。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">localStorage</span>.key(<span class="hljs-number">2</span>)
<span class="hljs-comment">// "BDSUGSTORED"</span>
<span class="hljs-built_in">localStorage</span>.hasOwnProperty(<span class="hljs-string">'BDSUGSTORED'</span>)
<span class="hljs-comment">// true</span>
<span class="hljs-built_in">localStorage</span>.hasOwnProperty(<span class="hljs-string">'1111'</span>)
<span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9a0ebb84f94444bacd2a48f15a216c8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>基于此，我也封装了判断存储中是否存在该值的<code>hasItem</code>方法，用于做一些<code>key</code>是否在存储中存在的一些判断。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 判断是否存在该属性
 * <span class="hljs-doctag">@param </span>key 需要判断的key
 */</span>
hasItem(key: string): boolean &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.readStorage.hasOwnProperty(key)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">进阶使用</h2>
<p>在进阶使用当中，我会介绍一些工作中可能会<code>碰到的问题</code>，并且给出一些<code>解决方案</code>。</p>
<h3 data-id="heading-12">过期时间</h3>
<p><code>WebStorage</code>中<code>SessionStorage</code>的一个周期是当前会话。而<code>localStorage</code>则如果不手动清除，则不会主动清除存储的数据。</p>
<blockquote>
<p>关键词，面试会问：localStorage如果不是主动清除，存储数据是不会过期的。</p>
</blockquote>
<p>所以，很多时候如果需要过期时间则需要开发者自己去处理，而处理的方式也非常简单暴力。
那就是给予存储值时带一个时间。参考下面代码，通过<code>new Date().getTime()</code>来取到当前时间，然后设置到存储当中去。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> person = &#123;
    <span class="hljs-comment">// 存储数据</span>
    <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'wangly19'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">22</span>
    &#125;,
    <span class="hljs-comment">// 过期时间</span>
    <span class="hljs-attr">timestamp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
&#125;
<span class="hljs-built_in">window</span>.localStorage.setItem(<span class="hljs-string">'person'</span>, <span class="hljs-built_in">JSON</span>.stringify(person))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取时间的时候，会进行一个简单的判断，<code>当前时间 - 存储时间 >= 过期时间</code>，这样就能够在值操作的时候做一些判断处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// # 原生</span>

<span class="hljs-keyword">let</span> person = <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'person'</span>)
person = <span class="hljs-built_in">JSON</span>.parse(val)

<span class="hljs-comment">// 这里可以使用一些库在做处理，如`dayjs`</span>
<span class="hljs-keyword">if</span>(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() - person.timestamp > [过期时间]) &#123;
    <span class="hljs-comment">// 数据已经过期的一些操作</span>
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 正常处理</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，需要在原有的<code>getItem</code>的方法上，添加一条过期时间的判断，我也直接封装在函数内处理这一份逻辑。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
  * 获取数据
  * <span class="hljs-doctag">@param </span>key 获取当前数据key
  * <span class="hljs-doctag">@returns </span>存储数据
*/</span>
getItem<T = <span class="hljs-built_in">any</span>>(key: <span class="hljs-built_in">string</span>): T | <span class="hljs-literal">null</span> &#123;
  <span class="hljs-keyword">const</span> content: StorageSaveFormat | <span class="hljs-literal">null</span> = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">this</span>.readStorage.getItem(key))
  <span class="hljs-keyword">if</span> (content?.timestamp && <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() - content.timestamp >= <span class="hljs-built_in">this</span>.config.timeout) &#123;
    <span class="hljs-built_in">this</span>.removeItem(key)
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-keyword">return</span> content?.data || <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">监听函数</h3>
<p><code>WebStorage</code>修改时，会触发浏览器<code>storage</code>事件。</p>
<p>而在应用中可以使用<code>addEventListener</code>添加一个<code>storage</code>事件对其进行绑定。</p>
<p>而这个触发机制可以看下图。在不同窗口对<code>storage</code>触发的时候会输出当前的<code>event</code>信息。在<code>event</code>当中，我们可以拿到触发的<code>url</code>,<code>新值</code>, <code>旧值</code>, <code>触发的key</code>等信息，我们可以通过这个API去做一些浏览器URL监听的事情。</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
 <span class="hljs-built_in">document</span>.body.innerHTML = <span class="hljs-string">'初始化数据'</span>
 <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"storage"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
 <span class="hljs-keyword">const</span> values = &#123;
 <span class="hljs-attr">url</span>: event.url,
 <span class="hljs-attr">key</span>: event.key,
 <span class="hljs-attr">old</span>: event.oldValue,
 <span class="hljs-attr">new</span>: event.newValue,
 &#125;
 <span class="hljs-built_in">document</span>.body.innerHTML = <span class="hljs-built_in">JSON</span>.stringify(values)
 &#125;);
 </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2746e6114f7140cab072d949c7b85862~tplv-k3u1fbpfcp-watermark.image" alt="iShot2021-07-04 12.27.57.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">修改数据</h3>
<p>由于原生没有<code>changeItem</code>这类的方法，因此我们需要自己去做一些方法的<code>封装</code>来方便我们频繁的需要去修改存储当中数据。</p>
<p>如下面的一个类似于<code>useState</code>回调的形式来做一些值的修改。</p>
<pre><code class="hljs language-js copyable" lang="js">changeItem(<span class="hljs-string">'name'</span>, <span class="hljs-function">(<span class="hljs-params">oldValue</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> name = <span class="hljs-string">`update: <span class="hljs-subst">$&#123;oldValue&#125;</span> update`</span>
    <span class="hljs-keyword">return</span> name
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现方式也相对比较易懂，通过<code>getItem</code>先获取数据，然后在通过<code>setItem</code>设置<code>onChange</code>回调函数的值，将一个连贯的操作串联起来。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
   * 修改当前存储内容数据
   * <span class="hljs-doctag">@param </span>key 当前存储key
   * <span class="hljs-doctag">@param </span>onChange 修改函数
   * <span class="hljs-doctag">@param </span>baseValue 基础数据
   */</span>
 changeItem<S = <span class="hljs-built_in">any</span>>(
  key: <span class="hljs-built_in">string</span>, 
  <span class="hljs-attr">onChange</span>: <span class="hljs-function">(<span class="hljs-params">oldValue: S</span>) =></span> S | <span class="hljs-literal">null</span>, baseValue?: <span class="hljs-built_in">any</span>
) &#123;
  <span class="hljs-keyword">const</span> data = <span class="hljs-built_in">this</span>.getItem<S>(key)
  <span class="hljs-built_in">this</span>.setItem(key, onChange(data || baseValue))
&#125;

<span class="hljs-comment">// # 使用</span>
customStorage.changeItem(<span class="hljs-string">'key'</span>, <span class="hljs-function">(<span class="hljs-params">oldValue</span>) =></span> &#123;
    retutn oldValue + <span class="hljs-string">'newUpadte'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">空间 & 溢出</h3>
<p>如果是重度使用用户，如一些文档构建项目，往往很多都是会往<code>localStorage</code>中存很多数据，很多开发者都会担心会不会直接<code>溢出</code>。</p>
<p>所以在这里，也设想了一些解决方案来处理这些问题。</p>
<h4 data-id="heading-16">存储状态 & StorageEstimate</h4>
<p>在安全的上下文和支持的浏览器下，通过<code>StorageEstimate</code>可以获取到当前浏览器的一个缓存情况，如：使用多少， 总共多少。</p>
<p>如下代码，首先判断了浏览器是否存在<code>navigator</code>，然后继续判断了<code>navigator</code>是否有<code>storage</code>，最后再去执行<code>estimate</code>异步获取我们的存储信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (navigator && navigator.storage) &#123;
    navigator.storage.estimate().then(<span class="hljs-function"><span class="hljs-params">estimate</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(estimate)
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/490c660cd5e7442a91760712e4cc6edd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>该Web API需要当前项目在https下。获取到的quota（存储总量）相对来说在3M左右，在开发场景下，这绝对是一个安全的内存范围。</p>
</blockquote>
<h4 data-id="heading-17">缓存溢出清理</h4>
<p>如果是在<code>内存濒临溢出</code>的场景下，那么我们就需要释放一些空间来做处理后面的数据修改了。
首先我们对带有时间的数据进行汇总排序，如下方法就是将<code>storage</code>中所有带有<code>timestamp</code>字段的数据汇总后进行排序。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 获取当前清除存储空间，并且进行排序
 */</span>
<span class="hljs-function"><span class="hljs-title">getClearStorage</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> keys: <span class="hljs-built_in">string</span>[] = <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>.readStorage)
  <span class="hljs-keyword">const</span> db: <span class="hljs-built_in">Array</span><&#123;
    <span class="hljs-attr">key</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">data</span>: StorageSaveFormat
  &#125;> = []
  keys.forEach(<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
    <span class="hljs-keyword">const</span> item = <span class="hljs-built_in">this</span>.getItem(name)
    <span class="hljs-keyword">if</span> (item.timestamp) &#123;
      db.push(&#123;
        <span class="hljs-attr">key</span>: name,
        <span class="hljs-attr">data</span>: item
      &#125;)
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> db.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> a.data.timestamp - b.data.timestamp
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当拥有了一个排序好的数据列表时，就需要考虑数据清空了，按照时间线将距离当前越久的时间清除。而这个时候，需要理解一个条件:
<code>总大小(quota) - (使用大小)usage > [当前存入大小currentSize]</code></p>
<p>当我们有一个排序好的存储时，只需要循环判断当前空间是否满足需求即可，如果满足跳出循环。反之继续异步，直到我们的空间够为止。</p>
<blockquote>
<p>initCacheSize单纯对容量数据最一个刷新。获取新的容量数据。</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * 容量清理，直到满足存储大小为止
 */</span>
<span class="hljs-function"><span class="hljs-title">detectionStorageContext</span>(<span class="hljs-params">currentSize: <span class="hljs-built_in">number</span></span>)</span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.usage + currentSize >= <span class="hljs-built_in">this</span>.quota) &#123;
      <span class="hljs-keyword">const</span> storage = <span class="hljs-built_in">this</span>.getClearStorage()
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> &#123; key, data &#125; <span class="hljs-keyword">of</span> storage) &#123;
          <span class="hljs-comment">// 如果满足要求就跳出，还不够就继续清除。</span>
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.usage + currentSize < <span class="hljs-built_in">this</span>.quota) <span class="hljs-keyword">break</span>
          <span class="hljs-comment">// 刷新容量大小</span>
          <span class="hljs-built_in">this</span>.removeItem(key)
          initCacheSize()
      &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一步就是在<code>setItem</code>中执行<code>detectionStorageContext</code>, 每次更新存储内容都会先判断下<code>是否要溢出</code>，如果添加或者修改的数据会溢出，那么我就会做一个<code>空间清理</code>了。</p>
<h2 data-id="heading-18">实践场景</h2>
<p>本章节，主要讲述了一些简单的<code>WebStorage</code>的使用场景。</p>
<h3 data-id="heading-19">搜索历史</h3>
<p>到这里，我们的一个<code>工具类</code>就已经基本成型了。最后，再回到<code>一开始的案例</code>中，我们就可以通过工具类中的<code>changItem</code>迅速的实现这个搜索历史的功能，而不必关心一些数据兼容上的问题。我们需要关注的只是存储值的设置。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32a66f42210047c8ac5c0db6e5565f30~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>事例代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Search</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [searchList, setSearchList] = useState([]);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> data = localStore.getItem(<span class="hljs-string">'search'</span>)
    setSearchList(data || [])
  &#125;, [])

  <span class="hljs-keyword">const</span> onSearch = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (value) &#123;
      localStore.changeItem(
        <span class="hljs-string">'search'</span>,
        <span class="hljs-function">(<span class="hljs-params">oldValue</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (oldValue.includes(value)) &#123;
            <span class="hljs-keyword">return</span> oldValue;
          &#125;

          <span class="hljs-keyword">if</span> (oldValue) &#123;
            <span class="hljs-keyword">const</span> newValue = [...oldValue, value];
            setSearchList(newValue);
            <span class="hljs-built_in">console</span>.log(newValue, <span class="hljs-string">'value'</span>);
            <span class="hljs-keyword">return</span> newValue;
          &#125;

          <span class="hljs-keyword">if</span> (value) &#123;
            setSearchList([value]);
            <span class="hljs-keyword">return</span> [value];
          &#125;

          <span class="hljs-keyword">return</span> [];
        &#125;,
        [],
      );
    &#125;
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"demo-app"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Search</span>
        <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入搜索内容"</span>
        <span class="hljs-attr">enterButton</span>=<span class="hljs-string">"Search"</span>
        <span class="hljs-attr">size</span>=<span class="hljs-string">"large"</span>
        <span class="hljs-attr">suffix</span>=<span class="hljs-string">&#123;suffix&#125;</span>
        <span class="hljs-attr">onSearch</span>=<span class="hljs-string">&#123;onSearch&#125;</span>
      /></span>

      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"tag-wrapper"</span>></span>
        &#123;searchList.map((e) => &#123;
          return (
            <span class="hljs-tag"><<span class="hljs-name">Tag</span>
              <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;e&#125;</span>
              <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
                <span class="hljs-attr">margin:</span> <span class="hljs-attr">10</span>,
              &#125;&#125;
              <span class="hljs-attr">color</span>=<span class="hljs-string">"#108ee9"</span>
            ></span>
              &#123;e&#125;
            <span class="hljs-tag"></<span class="hljs-name">Tag</span>></span>
          );
        &#125;)&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">图片数据</h3>
<p>浏览器对于请求是有限制的，而我们项目中绝大部份图片其实是通过后端接口进行返回的，在这里以<code>emoji</code>表情包做个例子。</p>
<p>我们拿知乎的表情包数据来进行一个模拟，发现一共有73条数据，如果每次刷新网页都请求一次后端数据是一件非常难受的事情，而这些数据显然也不需要存放在<code>Store</code>当中，在一定的时间中，发生改变的几率很小，那么我们将它放在<code>本地存储</code>显然是一个不错的选择。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e6e7e9391db4720bf5c2d3d078582d6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在页面加载时，我会对接口数据请求加一层判断，只有<code>数据为空</code>时才会请求后端图标数据列表。如果是过期时间的话，获取数据时会清空本地图标数据，然后重新请求后端图标数据，在重新放入缓存中并且更新新的过期时间。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> emojiRef = useRef(localStore.getItem(<span class="hljs-string">'emoji'</span>));

useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!emojiRef.current) &#123;
      fetchEmojiIcon()
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你项目中存在大量的资源路径，可以将其放在<code>localStorage</code>中进行存储，方便需要用到时进行使用。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ae77f8169114c769afa1779ffe274b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-21">资源 & 资料</h2>
<ul>
<li><a href="https://juejin.cn/post/6844904128557105166#heading-5" target="_blank" title="https://juejin.cn/post/6844904128557105166#heading-5">当浏览器全面禁用三方 Cookie</a></li>
<li><a href="https://juejin.cn/post/6844903989096497159" target="_blank" title="https://juejin.cn/post/6844903989096497159">localStorage、sessionStorage、cookie、session几种web数据存储方式对比总结</a></li>
<li><a href="https://juejin.cn/post/6844904192549584903" target="_blank" title="https://juejin.cn/post/6844904192549584903">前端存储除了 localStorage 还有啥</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2Fwebstorage%2F%23implementation-risks" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/webstorage/#implementation-risks" ref="nofollow noopener noreferrer">Web Storage (Second Edition)</a></li>
<li><a href="https://juejin.cn/post/6854573211594522631#heading-4" target="_blank" title="https://juejin.cn/post/6854573211594522631#heading-4">项目实战|缓存处理</a></li>
</ul>
<h2 data-id="heading-22">总结</h2>
<p>本文对<code>WebStorage</code>中绝大部分使用技巧都做了一些使用的总结，将常用的一些操作存储方法都进行了封装，同时也对工作中经常碰到的一些复杂场景，如过期时间、数据更改、缓存溢出等功能进行了一些叙述，最后将其封装到了工具类 当中，方便在日常开发中进行调用。</p>
<p>最后在对<code>WebStorage</code>有了一些了解之后，那么我们在后续工作中，是不是可以思考有些数据可以考虑放到存储当中去？在节省资源的同时，也能有更好的性能，同时也缓解了部分服务端的压力。</p>
<h2 data-id="heading-23">近期好文</h2>
<ul>
<li><a href="https://juejin.cn/post/6976782987480432670" target="_blank" title="https://juejin.cn/post/6976782987480432670">我 & 掘金，毕业一年后，我被掘金签约了｜2021 年中总结</a></li>
<li><a href="https://juejin.cn/post/6970841540776329224" target="_blank" title="https://juejin.cn/post/6970841540776329224">总结TypeScript在项目开发中的应用实践体会</a></li>
</ul>
<h2 data-id="heading-24">尾注</h2>
<blockquote>
<p>如果本文对你有帮助，希望能够给我点一赞支持一下。<br></p>
</blockquote>
<p>本文首发于：掘金技术社区<br>
类型：签约文章<br>
作者：wangly19<br>
收藏于专栏：javaScript基础进阶<br>
公众号: ItCodes 程序人生</p></div>  
</div>
            
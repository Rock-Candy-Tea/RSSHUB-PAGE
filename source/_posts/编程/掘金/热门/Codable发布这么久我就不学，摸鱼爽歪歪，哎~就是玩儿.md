
---
title: 'Codable发布这么久我就不学，摸鱼爽歪歪，哎~就是玩儿'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30caa2d3c5574b298ae6e73443882fda~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 10 May 2021 17:37:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30caa2d3c5574b298ae6e73443882fda~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">写在开头</h3>
<blockquote>
<p>祝天下所有伟大的母亲：</p>
<p>节日快乐，身体健康， 感谢您的付出，感谢您的仁爱！</p>
<p>---- 写在母亲节当天</p>
</blockquote>
<h3 data-id="heading-1">前言</h3>
<p>对于大多数的应用程序来说，最常见的任务就是进行网络数据的发送和接收，但是在执行此操作之前，我们需要通过编码或者序列化的方式将数据转换为合适的格式来发送，然后还需要将收到的网络数据转换为合适的格式，这样才能在应用中使用它们，这样的过程叫做解码或着叫反序列化。</p>
<p>那如何去定义这个格式呢！这里就不得不提 JSON 了，JSON 目前是网络通信发送和接收数据最常用的格式，但是在 Swift4.0 之前，大家都是用一些第三方的开源库来对 JSON 格式进行解析。</p>
<p>终于， Apple 在 Swift4.0 的 Foundtion 模块中添加了对 JSON 解析的原生支持，它的功能强大而且易于使用，接下来就让我带大家
了解下在 swift 里如何来对你的数据进行 encoding 和 decoding 吧！</p>
<h3 data-id="heading-2">基础知识介绍</h3>
<p>在 swift 里要对 JSON 进行处理的话，首先需要了解的概念就是：Codable，
Codable 其实它不是一个协议，而是另外俩个协议的组合：Decodable 和 Encodable，它的源码如下所示：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">public</span> <span class="hljs-keyword">typealias</span> <span class="hljs-type">Codable</span> <span class="hljs-operator">=</span> <span class="hljs-type">Decodable</span> & <span class="hljs-type">Encodable</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以聪明的你一定可以猜到，只要数据模型遵行了 Codable 协议，那么就可以方便的进行 JSON 和数据模型的相互转换了。</p>
<p>在 Swift4.0 中，Apple 提供了 JSONEncoder 和 JSONDecoder 俩对象来处理 JSON 的编码和解码，核心代码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> encoder <span class="hljs-operator">=</span> <span class="hljs-type">JSONEncoder</span>()
<span class="hljs-keyword">let</span> decoder <span class="hljs-operator">=</span> <span class="hljs-type">JSONDecoder</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相关的概念已介绍完毕，你准备好迎接挑战了吗？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30caa2d3c5574b298ae6e73443882fda~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">JSON 转数据模型</h3>
<h4 data-id="heading-4">TASK 1：简单的数据结构</h4>
<p>如果你的 JSON 结构和你使用的数据模型结构一致的话，那么解析过程将会非常简单，请看下面内容：</p>
<p>下面给出的是一个歌曲的 JSON 数据，我现在要将其转换为 SongModel。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> song <span class="hljs-operator">=</span> <span class="hljs-string">"""
        &#123;
            "singer": "The Chainsmokers",
            "name": "Something Just Like This",
        &#125;
    """</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>SongModel</strong></em></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">/// SongModel模型，遵循 Codable 协议</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SongModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-keyword">var</span> singer: <span class="hljs-type">String</span>?
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>转换过程如下</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> jsonData <span class="hljs-operator">=</span> song.data(using: <span class="hljs-type">String</span>.<span class="hljs-type">Encoding</span>.utf8) &#123;
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> sSong <span class="hljs-operator">=</span> <span class="hljs-keyword">try?</span> <span class="hljs-type">JSONDecoder</span>().decode(<span class="hljs-type">SongModel</span>.<span class="hljs-keyword">self</span>, from: jsonData) &#123;
        <span class="hljs-built_in">dump</span>(sSong)
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>输出结果如下</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>
  <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
  <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就完成了解析，是不是很简单！</p>
<blockquote>
<p>NOTE：在数据模型的成员变量中，基本数据类型如：String、Int、Float等都已经实现了 Codable 协议，因此如果你的数据类型只包含这些基本数据类型的属性，只需要在类型声明中加上 Codable 协议就可以了，不需要写任何实际实现的代码。</p>
</blockquote>
<h4 data-id="heading-5">TASK 2: 解析数组</h4>
<p>假如这是我们收到的一张专辑 Album 的 JSON 数据，现在要把它转化成 AlbumModel 数据模型。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> album <span class="hljs-operator">=</span> <span class="hljs-string">"""
        &#123;
            "singer": "The Chainsmokers",
            "name": "Something Just Like This",
            "songs":[
                "Something Just Like This",
                "Closer",
                "Young",
                "All We Know"
            ]
        &#125;
    """</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>AlbumModel</strong></em></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">AlbumModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-keyword">var</span> singer: <span class="hljs-type">String</span>?
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
    <span class="hljs-keyword">var</span> songs: [<span class="hljs-type">String</span>]<span class="hljs-operator">?</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>转换过程如下</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> jsonData <span class="hljs-operator">=</span> album.data(using: <span class="hljs-type">String</span>.<span class="hljs-type">Encoding</span>.utf8) &#123;
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> sSong <span class="hljs-operator">=</span> <span class="hljs-keyword">try?</span> <span class="hljs-type">JSONDecoder</span>().decode(<span class="hljs-type">AlbumModel</span>.<span class="hljs-keyword">self</span>, from: jsonData) &#123;
        <span class="hljs-built_in">dump</span>(sSong)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>输出结果为</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">AlbumModel</span>
  <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
  <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
  <span class="hljs-operator">▿</span> songs: <span class="hljs-type">Optional</span>([<span class="hljs-string">"Something Just Like This"</span>, <span class="hljs-string">"Closer"</span>, <span class="hljs-string">"Young"</span>, <span class="hljs-string">"All We Know"</span>])
    <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">4</span> elements
      <span class="hljs-operator">-</span> <span class="hljs-string">"Something Just Like This"</span>
      <span class="hljs-operator">-</span> <span class="hljs-string">"Closer"</span>
      <span class="hljs-operator">-</span> <span class="hljs-string">"Young"</span>
      <span class="hljs-operator">-</span> <span class="hljs-string">"All We Know"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和上面的转换如出一辙，想必你现在心里已经在默默的嘀咕：这么简单还用你讲？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e805700e5e37493e879c02ef7b3dbff1~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那接下来就请准备迎接新的挑战把！</p>
<h4 data-id="heading-6">TASK 3：结构不一致</h4>
<p>上面所演示的 JSON 数据格式都是与数据模型里的成员变量一一对应的，但是，在实际开发中，你会经常遇到数据源的格式和数据模型结构
不一致的情况，很多情况下可能是服务端与客户端没有统一好接口的格式，然后各自就开始开发，到需要进行调试的时候，客户端一收到消息，就懵逼了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1a78ea291fa407bbb083e42705488d5~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>NOTE: 所以在这里我非常建议大家在做功能开发之前一定要先把接口文档定义好，定义好，定义好，重要的事情讲三遍。</p>
</blockquote>
<p>这样服务端和客户端之间定义的数据格式就存在了差异，无论怎样当然总有一方需要作出让步来做到兼容，那么当客户端想要做兼容时，该怎么处理呢！我们先来看个例子：</p>
<p>例如服务端返回的数据为:</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> album <span class="hljs-operator">=</span> <span class="hljs-string">"""
        &#123;
            "singer": "The Chainsmokers",
            "name": "Something Just Like This",
            "songList":[
                "Something Just Like This",
                "Closer",
                "Young",
                "All We Know"
            ]
        &#125;
    """</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，原来的 songs 换成了 songList，我们执行下原先的代码，看下输出：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">AlbumModel</span>
  <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
  <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
  <span class="hljs-operator">-</span> songs: <span class="hljs-literal">nil</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发现 songs 字段变成了 nil, 这个解析就失败了，那如何做到不修改我之前定义的数据模型的成员变量，来做到兼容呢！这时候就需要用到 CodingKey 协议了，
借助 CodingKey 可以用来映射数据模型的成员变量，首先在数据模型中添加一个特殊的枚举类型：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">private</span> <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">CodingKeys</span>: <span class="hljs-title">String</span>, <span class="hljs-title">CodingKey</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>添加完后的数据模型代码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">AlbumModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-keyword">var</span> singer: <span class="hljs-type">String</span>?
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
    <span class="hljs-keyword">var</span> songs: [<span class="hljs-type">String</span>]<span class="hljs-operator">?</span>
    
    <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">CodingKeys</span>: <span class="hljs-title">String</span>, <span class="hljs-title">CodingKey</span> </span>&#123;
        <span class="hljs-keyword">case</span> singer <span class="hljs-operator">=</span> <span class="hljs-string">"singer"</span>
        <span class="hljs-keyword">case</span> name <span class="hljs-operator">=</span> <span class="hljs-string">"name"</span>
        <span class="hljs-keyword">case</span> songs <span class="hljs-operator">=</span> <span class="hljs-string">"songList"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>输出结果为</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">AlbumModel</span>
  <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
  <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
  <span class="hljs-operator">▿</span> songs: <span class="hljs-type">Optional</span>([<span class="hljs-string">"Something Just Like This"</span>, <span class="hljs-string">"Closer"</span>, <span class="hljs-string">"Young"</span>, <span class="hljs-string">"All We Know"</span>])
    <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">4</span> elements
      <span class="hljs-operator">-</span> <span class="hljs-string">"Something Just Like This"</span>
      <span class="hljs-operator">-</span> <span class="hljs-string">"Closer"</span>
      <span class="hljs-operator">-</span> <span class="hljs-string">"Young"</span>
      <span class="hljs-operator">-</span> <span class="hljs-string">"All We Know"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们是不是就可以正常解析 JSON 数据了，是不是很强大。</p>
<p>接下来再增加一个难度！</p>
<p>当给你的唱片的 JSON 结构是这样的，你该怎么解析呢！</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> album <span class="hljs-operator">=</span> <span class="hljs-string">"""
        &#123;
            "singer": "The Chainsmokers",
            "name": "Something Just Like This",
            "songs": "Something Just Like This"
        &#125;
    """</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上面给出的例子，你会发现它依然与你的数据模型不匹配，原来的 songs 字段不是数组格式了，那如何才能正常的解析到数据模型上去呢，这时候就需要我们自己来实现编码解码的逻辑了。</p>
<p>首先在 <em><strong>AlbumModel</strong></em> 中加入以下代码：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">AlbumModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-keyword">var</span> singer: <span class="hljs-type">String</span>?
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
    <span class="hljs-keyword">var</span> songs: [<span class="hljs-type">String</span>]<span class="hljs-operator">?</span>

    <span class="hljs-comment">// 1</span>
    <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">CodingKeys</span>: <span class="hljs-title">String</span>, <span class="hljs-title">CodingKey</span> </span>&#123;
        <span class="hljs-keyword">case</span> singer <span class="hljs-operator">=</span> <span class="hljs-string">"singer"</span>
        <span class="hljs-keyword">case</span> name <span class="hljs-operator">=</span> <span class="hljs-string">"name"</span>
        <span class="hljs-keyword">case</span> songs <span class="hljs-operator">=</span> <span class="hljs-string">"songs"</span>
    &#125;
    
    <span class="hljs-comment">// 解码: JSON 转 Model</span>
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">from</span> <span class="hljs-params">decoder</span>: <span class="hljs-type">Decoder</span>)</span> <span class="hljs-keyword">throws</span> &#123;
    <span class="hljs-comment">// 2</span>
        <span class="hljs-keyword">let</span> container <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> decoder.container(keyedBy: <span class="hljs-type">CodingKeys</span>.<span class="hljs-keyword">self</span>)
        <span class="hljs-comment">// 3</span>
        singer <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> container.decode(<span class="hljs-type">String</span>.<span class="hljs-keyword">self</span>, forKey: .singer)
        name <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> container.decode(<span class="hljs-type">String</span>.<span class="hljs-keyword">self</span>, forKey: .name)
        <span class="hljs-keyword">let</span> ss <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> container.decode(<span class="hljs-type">String</span>.<span class="hljs-keyword">self</span>, forKey: .songs)
        songs <span class="hljs-operator">=</span> [ss]
    &#125;
    
    <span class="hljs-comment">// 编码: Model 转 JSON</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">encode</span>(<span class="hljs-params">to</span> <span class="hljs-params">encoder</span>: <span class="hljs-type">Encoder</span>)</span> <span class="hljs-keyword">throws</span> &#123;
    <span class="hljs-comment">// 4</span>
        <span class="hljs-keyword">var</span> container <span class="hljs-operator">=</span> encoder.container(keyedBy: <span class="hljs-type">CodingKeys</span>.<span class="hljs-keyword">self</span>)
        <span class="hljs-keyword">try</span> container.encode(singer, forKey: .singer)
        <span class="hljs-keyword">try</span> container.encode(name, forKey: .name)
        <span class="hljs-keyword">try</span> container.encode(songs, forKey: .songs)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>解释如下</em>：</strong></p>
<ol>
<li>创建 CodingKeys 枚举，用于映射 JSON 字段。</li>
<li>创建一个解码器容器，来存储 JSON 里的属性。</li>
<li>使用适当的类型和编码键从容器中提取歌手和专辑名和歌单，由于歌单是数组类型的，所以需要将提取到的歌转换成数组。</li>
<li>创建 KeyedEncodingContainer 容器来对数据模型里的属性进行编码。</li>
</ol>
<p><strong><em>转换过程如下</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> jsonData <span class="hljs-operator">=</span> album.data(using: <span class="hljs-type">String</span>.<span class="hljs-type">Encoding</span>.utf8) &#123;
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> aAlbum <span class="hljs-operator">=</span> <span class="hljs-keyword">try?</span> <span class="hljs-type">JSONDecoder</span>().decode(<span class="hljs-type">AlbumModel</span>.<span class="hljs-keyword">self</span>, from: jsonData) &#123;
        <span class="hljs-built_in">dump</span>(aAlbum)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>结果如下</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">AlbumModel</span>
  <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
  <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
  <span class="hljs-operator">▿</span> songs: <span class="hljs-type">Optional</span>([<span class="hljs-string">"Something Just Like This"</span>])
    <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">1</span> element
      <span class="hljs-operator">-</span> <span class="hljs-string">"Something Just Like This"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到通过上面的代码，已经可以将 JSON 中原先的 String 转换成数据模型中的数组类型了。</p>
<blockquote>
<p>注意：如果需要借助 CodingKeys 解决字段不一致的情况，即使其他的属性不需要映射，也必须将其包含在枚举中，譬如：singer, name，否则会报错。</p>
</blockquote>
<h4 data-id="heading-7">TASK 4： 复杂的嵌套</h4>
<p>除了处理简单的数据模型，Codable 还可以处理复杂的嵌套数据模型，首先解释下什么是嵌套数据模型：</p>
<p>譬如我有个专门处理专辑的数据模型叫 <em><strong>AlbumModel</strong></em>，它里面内嵌了 <em><strong>SongModel</strong></em> 的属性，这就是嵌套。这里必须要说明的就是嵌套的数据模型以及嵌套的子模型都必须遵循 Codable 协议，下面我们举个嵌套的数据模型的例子来说明一下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">/// 专辑模型</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">AlbumModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-comment">// 专辑名</span>
    <span class="hljs-keyword">var</span> albumName: <span class="hljs-type">String</span>?
    <span class="hljs-comment">// 发布时间</span>
    <span class="hljs-keyword">var</span> releaseTime: <span class="hljs-type">String</span>?
    <span class="hljs-comment">// 歌单（嵌套）</span>
    <span class="hljs-keyword">var</span> songs: [<span class="hljs-type">SongModel</span>]<span class="hljs-operator">?</span>
&#125;

<span class="hljs-comment">/// 歌曲模型</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SongModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-comment">// 歌手（嵌套）</span>
    <span class="hljs-keyword">var</span> singer: <span class="hljs-type">SingerModel</span>?
    <span class="hljs-comment">// 歌曲</span>
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
&#125;

<span class="hljs-comment">/// 歌手模型</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SingerModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-comment">// 姓名</span>
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
    <span class="hljs-comment">// 年龄</span>
    <span class="hljs-keyword">var</span> age: <span class="hljs-type">Int</span>?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>JSON</em> 数据结构</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift">    <span class="hljs-keyword">let</span> album <span class="hljs-operator">=</span> <span class="hljs-string">"""
        &#123;
            "albumName": "Something Just Like This",
            "releaseTime": "2017-02-22",
            "songs":[
                &#123;
                    "singer": &#123;
                        "name":"The Chainsmokers",
                        "age": 30
                    &#125;,
                    "name": "Something Just Like This"
                &#125;,
                &#123;
                    "singer": &#123;
                        "name":"The Chainsmokers",
                        "age": 30
                    &#125;,
                    "name": "Closer"
                &#125;,
                &#123;
                    "singer": &#123;
                        "name":"The Chainsmokers",
                        "age": 30
                    &#125;,
                    "name": "Young"
                &#125;,
                &#123;
                    "singer": &#123;
                        "name":"The Chainsmokers",
                        "age": 30
                    &#125;,
                    "name": "All We Know"
                &#125;
            ]
        &#125;
    """</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>转换过程如下</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> jsonData <span class="hljs-operator">=</span> album.data(using: <span class="hljs-type">String</span>.<span class="hljs-type">Encoding</span>.utf8) &#123;
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> aAlbum <span class="hljs-operator">=</span> <span class="hljs-keyword">try?</span> <span class="hljs-type">JSONDecoder</span>().decode(<span class="hljs-type">AlbumModel</span>.<span class="hljs-keyword">self</span>, from: jsonData) &#123;
        <span class="hljs-built_in">dump</span>(aAlbum)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>输出结果为</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">AlbumModel</span>
  <span class="hljs-operator">▿</span> albumName: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
  <span class="hljs-operator">▿</span> releaseTime: <span class="hljs-type">Optional</span>(<span class="hljs-string">"2017-02-22"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"2017-02-22"</span>
  <span class="hljs-operator">▿</span> songs: <span class="hljs-type">Optional</span>([<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>(singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>))), name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)), <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>(singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>))), name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Closer"</span>)), <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>(singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>))), name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Young"</span>)), <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>(singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>))), name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"All We Know"</span>))])
    <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">4</span> elements
      <span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>
        <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)))
          <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>
            <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
            <span class="hljs-operator">▿</span> age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">30</span>
        <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
          <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
      <span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>
        <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)))
          <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>
            <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
            <span class="hljs-operator">▿</span> age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">30</span>
        <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Closer"</span>)
          <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Closer"</span>
      <span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>
        <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)))
          <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>
            <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
            <span class="hljs-operator">▿</span> age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">30</span>
        <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Young"</span>)
          <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Young"</span>
      <span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>
        <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)))
          <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>
            <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
            <span class="hljs-operator">▿</span> age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">30</span>
        <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"All We Know"</span>)
          <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"All We Know"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样这个嵌套就被解决了，接下来再挑战一个难度更大的，请看代码：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> album <span class="hljs-operator">=</span> <span class="hljs-string">"""
        &#123;
            "albumName": "Something Just Like This",
            "releaseTime": "2017-02-22",
            "songs": &#123;
                "favorite":[
                    &#123;
                        "singer": &#123;
                            "name":"The Chainsmokers",
                            "age": 30
                        &#125;,
                        "name": "Something Just Like This"
                    &#125;,
                    &#123;
                        "singer": &#123;
                            "name":"The Chainsmokers",
                            "age": 30
                        &#125;,
                        "name": "Closer"
                    &#125;,
                    &#123;
                        "singer": &#123;
                            "name":"The Chainsmokers",
                            "age": 30
                        &#125;,
                        "name": "Young"
                    &#125;,
                    &#123;
                        "singer": &#123;
                            "name":"The Chainsmokers",
                            "age": 30
                        &#125;,
                        "name": "All We Know"
                    &#125;
                ]
            &#125;
        &#125;
    """</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，在歌单 Songs 中又嵌套了一个 favorite 字段，这个 JSON 结构相比 AlbumModel 这个数据模型又加深了一层，那该如何解析呢！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af4f63aa07094afba5e299d880cd490c~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们就要用到 nestedContainer 来处理这种嵌套，首先在 AlbumModel 加入如下代码：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">/// 专辑模型</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">AlbumModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-comment">// 专辑名</span>
    <span class="hljs-keyword">var</span> albumName: <span class="hljs-type">String</span>?
    <span class="hljs-comment">// 发布时间</span>
    <span class="hljs-keyword">var</span> releaseTime: <span class="hljs-type">String</span>?
    <span class="hljs-comment">// 歌单</span>
    <span class="hljs-keyword">var</span> songs: [<span class="hljs-type">SongModel</span>]<span class="hljs-operator">?</span>
    
    <span class="hljs-comment">// 1</span>
    <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">CodingKeys</span>: <span class="hljs-title">String</span>, <span class="hljs-title">CodingKey</span> </span>&#123;
        <span class="hljs-keyword">case</span> albumName, releaseTime, songs
    &#125;
    <span class="hljs-comment">// 2</span>
    <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">favoriteKeys</span>: <span class="hljs-title">CodingKey</span> </span>&#123;
        <span class="hljs-keyword">case</span> favorite
    &#125;

    <span class="hljs-comment">// 解码: JSON 转 Model</span>
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">from</span> <span class="hljs-params">decoder</span>: <span class="hljs-type">Decoder</span>)</span> <span class="hljs-keyword">throws</span> &#123;
        <span class="hljs-comment">// 3</span>
        <span class="hljs-keyword">let</span> container <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> decoder.container(keyedBy: <span class="hljs-type">CodingKeys</span>.<span class="hljs-keyword">self</span>)
        albumName <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> container.decode(<span class="hljs-type">String</span>.<span class="hljs-keyword">self</span>, forKey: .albumName)
        releaseTime <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> container.decode(<span class="hljs-type">String</span>.<span class="hljs-keyword">self</span>, forKey: .releaseTime)
        <span class="hljs-comment">// 4</span>
        <span class="hljs-keyword">let</span> favoriteContainer <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> container.nestedContainer(keyedBy: favoriteKeys.<span class="hljs-keyword">self</span>, forKey: .songs)
        songs <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> favoriteContainer.decode([<span class="hljs-type">SongModel</span>].<span class="hljs-keyword">self</span>, forKey: .favorite)
    &#125;

    <span class="hljs-comment">// 编码: Model 转 JSON</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">encode</span>(<span class="hljs-params">to</span> <span class="hljs-params">encoder</span>: <span class="hljs-type">Encoder</span>)</span> <span class="hljs-keyword">throws</span> &#123;
        <span class="hljs-comment">// 5</span>
        <span class="hljs-keyword">var</span> container <span class="hljs-operator">=</span> encoder.container(keyedBy: <span class="hljs-type">CodingKeys</span>.<span class="hljs-keyword">self</span>)
        <span class="hljs-keyword">try</span> container.encode(albumName, forKey: .albumName)
        <span class="hljs-keyword">try</span> container.encode(releaseTime, forKey: .releaseTime)
        <span class="hljs-comment">// 6</span>
        <span class="hljs-keyword">var</span> favoriteContainer <span class="hljs-operator">=</span> container.nestedContainer(keyedBy: favoriteKeys.<span class="hljs-keyword">self</span>, forKey: .songs)
        <span class="hljs-keyword">try</span> favoriteContainer.encode(songs, forKey: .favorite)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">/// 歌曲模型</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SongModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-comment">// 歌手</span>
    <span class="hljs-keyword">var</span> singer: <span class="hljs-type">SingerModel</span>?
    <span class="hljs-comment">// 歌曲</span>
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
&#125;

<span class="hljs-comment">/// 歌手模型</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">SingerModel</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-comment">// 姓名</span>
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
    <span class="hljs-comment">// 年龄</span>
    <span class="hljs-keyword">var</span> age: <span class="hljs-type">Int</span>?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>解析如下</em>：</strong></p>
<ol>
<li>首先创建最顶层的 CodingKeys</li>
<li>创建嵌套层的 CodingKeys</li>
<li>创建顶层 CodingKeys 对应的容器，并对其解码</li>
<li>创建嵌套层的容器，并对 favorite 解码</li>
<li>创建编码容器，并对 albumName 和 releaseTime 编码</li>
<li>获取嵌套容器，并对 favorite 编码</li>
</ol>
<p><strong><em>转换过程</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> jsonData <span class="hljs-operator">=</span> album.data(using: <span class="hljs-type">String</span>.<span class="hljs-type">Encoding</span>.utf8) &#123;
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> aAlbum <span class="hljs-operator">=</span> <span class="hljs-keyword">try?</span> <span class="hljs-type">JSONDecoder</span>().decode(<span class="hljs-type">AlbumModel</span>.<span class="hljs-keyword">self</span>, from: jsonData) &#123;
        <span class="hljs-built_in">dump</span>(aAlbum)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>输出如下</strong></em>：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">AlbumModel</span>
  <span class="hljs-operator">▿</span> albumName: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
  <span class="hljs-operator">▿</span> releaseTime: <span class="hljs-type">Optional</span>(<span class="hljs-string">"2017-02-22"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"2017-02-22"</span>
  <span class="hljs-operator">▿</span> songs: <span class="hljs-type">Optional</span>([<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>(singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>))), name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)), <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>(singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>))), name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Closer"</span>)), <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>(singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>))), name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Young"</span>)), <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>(singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>))), name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"All We Know"</span>))])
    <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">4</span> elements
      <span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>
        <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)))
          <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>
            <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
            <span class="hljs-operator">▿</span> age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">30</span>
        <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
          <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
      <span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>
        <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)))
          <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>
            <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
            <span class="hljs-operator">▿</span> age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">30</span>
        <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Closer"</span>)
          <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Closer"</span>
      <span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>
        <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)))
          <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>
            <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
            <span class="hljs-operator">▿</span> age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">30</span>
        <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Young"</span>)
          <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Young"</span>
      <span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SongModel</span>
        <span class="hljs-operator">▿</span> singer: <span class="hljs-type">Optional</span>(<span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>(name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>), age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)))
          <span class="hljs-operator">▿</span> <span class="hljs-keyword">some</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">SingerModel</span>
            <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"The Chainsmokers"</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"The Chainsmokers"</span>
            <span class="hljs-operator">▿</span> age: <span class="hljs-type">Optional</span>(<span class="hljs-number">30</span>)
              <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-number">30</span>
        <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"All We Know"</span>)
          <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"All We Know"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>挑战成功，看到这里是不是已经有点晕了，说实话其实我自己也不知道我在表达啥，我也晕了，哈哈！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f7ef6a6bde94596b8194a8332f98914~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">Task 6：处理派生类</h4>
<p>下面我们来看下一个特殊的数据模型结构，它应该怎么去转换呢！</p>
<p>当一个类遵循了 Codable 协议，那么它自身是可以很方便的使用 JSONEncoder 和 JSONDecoder 来 JSON 化和反 JSON 化的，但是如果有别的类继承了它，那么对该子类的 JSON 化和反 JSON 化就不是那么方便了。</p>
<p>首先来看个例子，
<em><strong>Song</strong></em> 是 <em><strong>Music</strong></em> 的子类：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Music</span>: <span class="hljs-title">Codable</span> </span>&#123;
    <span class="hljs-keyword">var</span> kind: <span class="hljs-type">String</span>?
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Song</span>: <span class="hljs-title">Music</span> </span>&#123;
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>JSON</em> 数据为：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> jsonString <span class="hljs-operator">=</span> <span class="hljs-string">"""
        &#123;
            "kind": "popular",
            "name": "Something Just Like This"
        &#125;
    """</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>数据解析</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> jsonData <span class="hljs-operator">=</span> jsonString.data(using: <span class="hljs-type">String</span>.<span class="hljs-type">Encoding</span>.utf8) &#123;
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> song <span class="hljs-operator">=</span> <span class="hljs-keyword">try?</span> <span class="hljs-type">JSONDecoder</span>().decode(<span class="hljs-type">Song</span>.<span class="hljs-keyword">self</span>, from: jsonData) &#123;
        <span class="hljs-built_in">dump</span>(song)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>结果</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">Song</span> #<span class="hljs-number">0</span>
  <span class="hljs-operator">▿</span> <span class="hljs-keyword">super</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">Music</span>
    <span class="hljs-operator">▿</span> kind: <span class="hljs-type">Optional</span>(<span class="hljs-string">"popular"</span>)
      <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"popular"</span>
  <span class="hljs-operator">-</span> name: <span class="hljs-literal">nil</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的结果发现，<em><strong>Song</strong></em> 类的实例只解析出了父类中的 <em>kind</em> 字段，而自己的 <em>name</em> 未能解析，这说明 Codable 在继承中是无效的，当你在派生类中声明遵循该协议时，会报如下错误：</p>
<pre><code class="copyable">Redundant conformance of 'Song' to protocol 'Decodable'
Redundant conformance of 'Song' to protocol 'Encodable'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那如何才能解决这个问题呢！</p>
<p>这时候，就需要我们自行实现 Codable 协议了，代码如下：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Song</span>: <span class="hljs-title">Music</span> </span>&#123;
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
    
    <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">CodingKeys</span>: <span class="hljs-title">String</span>, <span class="hljs-title">CodingKey</span> </span>&#123;
        <span class="hljs-keyword">case</span> type
        <span class="hljs-keyword">case</span> name
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">type</span>: <span class="hljs-type">String</span>, <span class="hljs-params">name</span> <span class="hljs-params">songName</span>:<span class="hljs-type">String</span>)</span> &#123;
        <span class="hljs-keyword">self</span>.name <span class="hljs-operator">=</span> songName
        <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>(type: type)
    &#125;
    
    <span class="hljs-keyword">required</span> <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">from</span> <span class="hljs-params">decoder</span>: <span class="hljs-type">Decoder</span>)</span> <span class="hljs-keyword">throws</span> &#123;
        <span class="hljs-keyword">try</span> <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>(from: decoder)
        <span class="hljs-keyword">let</span> container <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> decoder.container(keyedBy: <span class="hljs-type">CodingKeys</span>.<span class="hljs-keyword">self</span>)
        type <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> container.decode(<span class="hljs-type">String</span>.<span class="hljs-keyword">self</span>, forKey: .type)
        name <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> container.decode(<span class="hljs-type">String</span>.<span class="hljs-keyword">self</span>, forKey: .name)
    &#125;
    
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">encode</span>(<span class="hljs-params">to</span> <span class="hljs-params">encoder</span>: <span class="hljs-type">Encoder</span>)</span> <span class="hljs-keyword">throws</span> &#123;
        <span class="hljs-keyword">var</span> container <span class="hljs-operator">=</span> encoder.container(keyedBy: <span class="hljs-type">CodingKeys</span>.<span class="hljs-keyword">self</span>)
        <span class="hljs-keyword">try</span> container.encode(type, forKey: .type)
        <span class="hljs-keyword">try</span> container.encode(name, forKey: .name)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>转换结果</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-operator">▿</span> <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">Song</span> #<span class="hljs-number">0</span>
  <span class="hljs-operator">▿</span> <span class="hljs-keyword">super</span>: <span class="hljs-type">JSONDecoderDemo</span>.<span class="hljs-type">Music</span>
    <span class="hljs-operator">▿</span> type: <span class="hljs-type">Optional</span>(<span class="hljs-string">"popular"</span>)
      <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"popular"</span>
  <span class="hljs-operator">▿</span> name: <span class="hljs-type">Optional</span>(<span class="hljs-string">"Something Just Like This"</span>)
    <span class="hljs-operator">-</span> <span class="hljs-keyword">some</span>: <span class="hljs-string">"Something Just Like This"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的结果显示，我已经成功将 JSON 转成了相应的数据模型，那么对派生类的处理，我们只需要参考上面的代码，自行实现 Codable 协议，就可以避免上述的错误。</p>
<h3 data-id="heading-9">数据模型转 JSON</h3>
<p>当实现 Codable 协议的某个对象想要转为 JSON 时，则可以借助 JSONEncoder 编码器来实现。</p>
<p>这个转换相对来说就比较简单了，这里就举个简单的例子吧！</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> song <span class="hljs-operator">=</span> <span class="hljs-type">Song</span>(type: <span class="hljs-string">"popular"</span>, name: <span class="hljs-string">"Something Just Like This"</span>)

<span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> jsonData <span class="hljs-operator">=</span> <span class="hljs-keyword">try?</span> <span class="hljs-type">JSONEncoder</span>().encode(song)&#123;
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> jsonString <span class="hljs-operator">=</span> <span class="hljs-type">String</span>.<span class="hljs-keyword">init</span>(data: jsonData, encoding: <span class="hljs-type">String</span>.<span class="hljs-type">Encoding</span>.utf8)&#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"jsonString:"</span> <span class="hljs-operator">+</span> <span class="hljs-string">"<span class="hljs-subst">\(jsonString)</span>"</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><em>输出结果</em>：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift">jsonString:&#123;<span class="hljs-string">"type"</span>:<span class="hljs-string">"popular"</span>,<span class="hljs-string">"name"</span>:<span class="hljs-string">"Something Just Like This"</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据模型转 JSON 就完成了，<strong>So Easy</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/252621a5b3e443d3a8b3093fd489ea5e~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">结语</h3>
<p>到这里本篇文章就结束了，首先非常感谢大家能耐着性子看到这里，说实话我在准备这篇文章的时候也有点痛苦，越写越无聊，时常在写的过程中脑子一直在想：这么无聊的内容连我自己都写不下去了，会有读者愿意看吗？但是开弓没有回头箭，毕竟我也花了几天时间准备了素材，所以还是耐着寂寞写完了，内容过于枯燥，希望大家别嫌弃。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd43e1ec54a94510bfd0a4c00b5f5311~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>往期文章：</strong></p>
<ul>
<li><a href="https://juejin.cn/post/6952682593372340237" target="_blank">iOS 优雅的处理网络数据，你真的会吗？不如看看这篇</a></li>
<li><a href="https://juejin.cn/post/6944994974614323213" target="_blank">UICollectionView 自定义布局！看这篇就够了 </a></li>
<li><a href="https://juejin.cn/post/6942356138960617508" target="_blank">Swift 探索 UICollectionView 之 SupplementaryView 和 Decoration View</a></li>
<li><a href="https://juejin.cn/post/6940140043042291748" target="_blank">Swift 自定义布局实现 Cover Flow 效果</a></li>
</ul>
<p><strong>请你喝杯 ☕️ 点赞 + 关注哦～</strong></p>
<ol>
<li>
<p>阅读完记得给我点个赞哦，有👍 有动力</p>
</li>
<li>
<p>关注公众号--- HelloWorld杰少，第一时间推送新姿势</p>
</li>
</ol></div>  
</div>
            
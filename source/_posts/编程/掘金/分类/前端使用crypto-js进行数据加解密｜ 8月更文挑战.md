
---
title: '前端使用crypto-js进行数据加解密｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58870f69e76c44849f57f7d20bebc008~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 01:59:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58870f69e76c44849f57f7d20bebc008~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>如果项目涉及到的敏感数据，前后端可以进行接口加密处理，采用的是 AES + BASE64 算法加密
网上关于 AES 对称加密的算法介绍挺多的，对这一块还不是特别理解的可自行查找</p>
<h1 data-id="heading-1">具体实现</h1>
<p>其实搞懂了是怎么一回事，做起来还是挺简单的，因为库都是现成的，我们只需要会用就好啦
这里我以 Vue 作为例子，其他的也就大同小异了</p>
<ul>
<li>要用 AES 算法加密，首先我们要引入 crypto-js ，crypto-js 是一个纯 javascript 写的加密算法类库 ，可以非常方便地在 javascript 进行 MD5、SHA1、SHA2、SHA3、RIPEMD-160 哈希散列，进行 AES、DES、Rabbit、RC4、Triple DES 加解密，我们可以采用 npm install crypto-js --save 进行下载安装</li>
<li>其次我们需要定义两个方法 ，分别是用于加密和解密，这里我将它放在了 utils 文件夹下，命名为 secret.js ，其具体代码如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CryptoJS = <span class="hljs-built_in">require</span>(<span class="hljs-string">'crypto-js'</span>); <span class="hljs-comment">//引用AES源码js</span>

<span class="hljs-keyword">const</span> key = CryptoJS.enc.Utf8.parse(<span class="hljs-string">"1234123412ABCDEF"</span>); <span class="hljs-comment">//十六位十六进制数作为密钥</span>

<span class="hljs-keyword">const</span> iv = CryptoJS.enc.Utf8.parse(<span class="hljs-string">'ABCDEF1234123412'</span>); <span class="hljs-comment">//十六位十六进制数作为密钥偏移量</span>

<span class="hljs-comment">//解密方法</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Decrypt</span>(<span class="hljs-params">word</span>) </span>&#123;

<span class="hljs-keyword">let</span> encryptedHexStr = CryptoJS.enc.Hex.parse(word);

<span class="hljs-keyword">let</span> srcs = CryptoJS.enc.Base64.stringify(encryptedHexStr);

<span class="hljs-keyword">let</span> decrypt = CryptoJS.AES.decrypt(srcs, key, &#123; <span class="hljs-attr">iv</span>: iv, <span class="hljs-attr">mode</span>: CryptoJS.mode.CBC, <span class="hljs-attr">padding</span>: CryptoJS.pad.Pkcs7 &#125;);

<span class="hljs-keyword">let</span> decryptedStr = decrypt.toString(CryptoJS.enc.Utf8);

<span class="hljs-keyword">return</span> decryptedStr.toString();

&#125;

<span class="hljs-comment">//加密方法</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Encrypt</span>(<span class="hljs-params">word</span>) </span>&#123;

<span class="hljs-keyword">let</span> srcs = CryptoJS.enc.Utf8.parse(word);

<span class="hljs-keyword">let</span> encrypted = CryptoJS.AES.encrypt(srcs, key, &#123; <span class="hljs-attr">iv</span>: iv, <span class="hljs-attr">mode</span>: CryptoJS.mode.CBC, <span class="hljs-attr">padding</span>: CryptoJS.pad.Pkcs7 &#125;);

<span class="hljs-keyword">return</span> encrypted.ciphertext.toString().toUpperCase();

&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;

Decrypt ,

Encrypt

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中的 key 是密钥 ，iv 是密钥偏移量，这个一般是接口返回的，为了方便，我们这里就直接在这里定义了。</p>
<p>值得注意的是密钥的长度，由于对称解密使用的算法是 AES-128-CBC算法，数据采用 PKCS#7 填充 ， 因此这里的 key 需要为16位！</p>
<p>接着我们定义了 解密方法Decrypt 和 加密方法 Encrypt ，最后通过 export default 将其暴露出去，方便在需要的时候进行引入~</p>
<p>ok，核心代码就这么多，是不是很简单啊，其实也么有你想的那么复杂哈，剩下的就是展示一下如何使用</p>
<h1 data-id="heading-2">示例</h1>
<p>这里我定义了一个 index.vue 用来展示数据加解密的操作~</p>
<p>加密操作： 假设我们现在要给后端发送一段文字，暂且定义为 This is a clear text ， 在发送之前我们需要对其进行加密操作，这时候我们可以调用上面介绍的 Encrypt 方法，通过加密后我们可以得到密文为：4ACEA01505ADAF9FB59A03B22FC1EF1B244AE28DDACFDFAEFA7E263655C44357</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58870f69e76c44849f57f7d20bebc008~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解密操作： 假设我们请求后端接口，后端返回了我们一堆如下的字符串 BBFE62335C28821AD2F4043B715BB0C3E45734908254666526DCFD86A605F3AF , 这让我很蒙蔽啊，这时候就要调用 Decrypt 方法，</p>
<p>通过解密我们可以拿到后端返回的信息其实是：&#123;"name":"Chris","sex":"male"&#125;</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef700877b1c4db59437b9d14d298bc3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">结语</h1>
<p>至此，你已经 get 了前端 AES 加解密的方法，是不是感觉很简单啊，用起来很简单，原理可不简单，况且这也只是其中的一种方案，关于加解密的方法还有很多，感兴趣的小伙伴们可以继续做一些深入的研究哈</p></div>  
</div>
            
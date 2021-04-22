
---
title: 'https是如何做到安全加密的？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f94b302f31154dc385821ec2c31c1e5b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 22:52:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f94b302f31154dc385821ec2c31c1e5b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>由于 HTTP 天生“明文”的特点，整个传输过程完全透明，任何人都能够在链路中截获、修改或者伪造请求 / 响应报文，数据不具有可信性。因此产生了如下问题：</p>
<ol>
<li>信息被窃听</li>
<li>信息被篡改</li>
<li>信息被劫持</li>
</ol>
<h2 data-id="heading-0">什么是https</h2>
<p>HTTPS 协议的主要功能基本都依赖于 TLS/SSL 协议，TLS/SSL 的功能实现主要依赖于三类基本算法</p>
<ul>
<li>散列函数 散列函数验证信息的完整性</li>
<li>对称加密 对称加密算法采用协商的密钥对数据加密</li>
<li>非对称加密 非对称加密实现身份认证和密钥协商</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f94b302f31154dc385821ec2c31c1e5b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">SSL/TLS的关系</h3>
<p>SSL 即安全套接层（Secure Sockets Layer），在 OSI 模型中处于第 5 层（会话层），由网景公司于 1994 年发明，有 v2 和 v3 两个版本，而 v1 因为有严重的缺陷从未公开过。
SSL 发展到 v3 时已经证明了它自身是一个非常好的安全通信协议，于是互联网工程组 IETF 在 1999 年把它改名为 TLS（传输层安全，Transport Layer Security），正式标准化，版本号从 1.0 重新算起，所以 TLS1.0 实际上就是 SSLv3.1。</p>
<p>了解了基础概念，我们一起来看看https是如何解决上述问题的。</p>
<h2 data-id="heading-2">加密信息</h2>
<p>我们知道http 是明文传输的，那我们很容易想到给明文加密呗，把传输的内容进行加密，服务端进行解密。这样子别人就不知道里面的内容是什么了。</p>
<blockquote>
<p>常见的加密算法叫做加密算法（RSA）</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> crypto = <span class="hljs-built_in">require</span>(<span class="hljs-string">'crypto'</span>);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">encrypt</span>(<span class="hljs-params">data, key, iv</span>) </span>&#123;
    <span class="hljs-keyword">let</span> decipher = crypto.createCipheriv(<span class="hljs-string">'aes-128-cbc'</span>, key, iv);
    decipher.update(data);
    <span class="hljs-keyword">return</span> decipher.final(<span class="hljs-string">'hex'</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">decrypt</span>(<span class="hljs-params">data, key, iv</span>) </span>&#123;
    <span class="hljs-keyword">let</span> decipher = crypto.createDecipheriv(<span class="hljs-string">'aes-128-cbc'</span>, key, iv);
    decipher.update(data, <span class="hljs-string">'hex'</span>);
    <span class="hljs-keyword">return</span> decipher.final(<span class="hljs-string">'utf8'</span>);
&#125;

<span class="hljs-keyword">let</span> key = <span class="hljs-string">'1234567890123456'</span>;
<span class="hljs-keyword">let</span> iv = <span class="hljs-string">'1234567890123456'</span>;
<span class="hljs-keyword">let</span> data = <span class="hljs-string">"hello"</span>;
<span class="hljs-keyword">let</span> encrypted = encrypt(data, key, iv);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"数据加密后:"</span>, encrypted);
<span class="hljs-keyword">let</span> decrypted = decrypt(encrypted, key, iv);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"数据解密后:"</span>, decrypted);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>我们发现堆成加密有一个秘钥，可以用这个秘钥进行加密解密。</p>
</blockquote>
<p>** 但是服务器和客户端怎么公用一个秘钥呢？在互联网上没有办法安全的交换密钥。**</p>
<h2 data-id="heading-3">使用非对称加密，加密秘钥</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123;
  generateKeyPairSync,
  privateEncrypt,
  publicDecrypt
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'crypto'</span>);
<span class="hljs-keyword">let</span> rsa = generateKeyPairSync(<span class="hljs-string">'rsa'</span>, &#123;
  <span class="hljs-attr">modulusLength</span>: <span class="hljs-number">1024</span>,
  <span class="hljs-attr">publicKeyEncoding</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'spki'</span>,
    <span class="hljs-attr">format</span>: <span class="hljs-string">'pem'</span>
  &#125;,
  <span class="hljs-attr">privateKeyEncoding</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'pkcs8'</span>,
    <span class="hljs-attr">format</span>: <span class="hljs-string">'pem'</span>,
    <span class="hljs-attr">cipher</span>: <span class="hljs-string">'aes-256-cbc'</span>,
    <span class="hljs-attr">passphrase</span>: <span class="hljs-string">'server_passphrase'</span>
  &#125;
&#125;);
<span class="hljs-keyword">let</span> message = <span class="hljs-string">'hello'</span>;
<span class="hljs-built_in">console</span>.log(rsa)
<span class="hljs-keyword">let</span> enc_by_prv = privateEncrypt(&#123;
  <span class="hljs-attr">key</span>: rsa.privateKey,
  <span class="hljs-attr">passphrase</span>: <span class="hljs-string">'server_passphrase'</span>
&#125;, Buffer.from(message, <span class="hljs-string">'utf8'</span>));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'encrypted by private key: '</span> + enc_by_prv.toString(<span class="hljs-string">'hex'</span>));


<span class="hljs-keyword">let</span> dec_by_pub = publicDecrypt(rsa.publicKey, enc_by_prv);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'decrypted by public key: '</span> + dec_by_pub.toString(<span class="hljs-string">'utf8'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这样子我们就可以安全的权属秘钥了，黑客无法知道我们秘钥，就无法知道我们的信息是啥，这样子就可以做到信息防止被窃听了。</p>
</blockquote>
<p>现在虽然可以做到数据防止被窃听，但是还是非常有可能被篡改的；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">比如说：
浏览器 发送 我爱你 加密后 waai;
浏览器 发送 我不爱你 加密后 wbai;

黑客拦截到数据，经过观察和分析，发现了规律。

当浏览器发送 我爱你 给服务器试，直接讲密文篡改成 wbai; 这样子就篡改了你消息的本意；
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">数字签名</h2>
<p>用数字签名可以防止，信息被篡改。（数字签名使用的是摘要算法）</p>
<p>我们用浏览器的私钥，进行信息摘要，做成签名，和信息一起发送给服务端；服务端进行验签，发现是本人，才继续执行逻辑；这样子就可以防止信息被篡改了。
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7292ac5495784877b0fbe7d04708d4bc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123; generateKeyPairSync, createSign, createVerify &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'crypto'</span>);
<span class="hljs-keyword">let</span> passphrase = <span class="hljs-string">'zhufeng'</span>;
<span class="hljs-keyword">let</span> rsa = generateKeyPairSync(<span class="hljs-string">'rsa'</span>, &#123;
    <span class="hljs-attr">modulusLength</span>: <span class="hljs-number">1024</span>,
    <span class="hljs-attr">publicKeyEncoding</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'spki'</span>,
        <span class="hljs-attr">format</span>: <span class="hljs-string">'pem'</span>
    &#125;,
    <span class="hljs-attr">privateKeyEncoding</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'pkcs8'</span>,
        <span class="hljs-attr">format</span>: <span class="hljs-string">'pem'</span>,
        <span class="hljs-attr">cipher</span>: <span class="hljs-string">'aes-256-cbc'</span>,
        passphrase
    &#125;
&#125;);
<span class="hljs-keyword">let</span> content = <span class="hljs-string">'hello'</span>;
<span class="hljs-keyword">const</span> sign = getSign(content, rsa.privateKey, passphrase);
<span class="hljs-keyword">let</span> serverCertIsValid = verifySign(content, sign, rsa.publicKey);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'serverCertIsValid'</span>, serverCertIsValid);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSign</span>(<span class="hljs-params">content, privateKey, passphrase</span>) </span>&#123;
    <span class="hljs-keyword">var</span> sign = createSign(<span class="hljs-string">'RSA-SHA256'</span>);
    sign.update(content);
    <span class="hljs-keyword">return</span> sign.sign(&#123; <span class="hljs-attr">key</span>: privateKey, <span class="hljs-attr">format</span>: <span class="hljs-string">'pem'</span>, passphrase &#125;, <span class="hljs-string">'hex'</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">verifySign</span>(<span class="hljs-params">content, sign, publicKey</span>) </span>&#123;
    <span class="hljs-keyword">var</span> verify = createVerify(<span class="hljs-string">'RSA-SHA256'</span>);
    verify.update(content);
    <span class="hljs-keyword">return</span> verify.verify(publicKey, sign, <span class="hljs-string">'hex'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">钓鱼网站</h2>
<p>通过上面的方式，黑客无法做好窃听和篡改了，但是可以做到截取，自己假装一个服务器（俗称钓鱼网站）；听过这种方式来欺骗用户；那么怎么防止呢？</p>
<blockquote>
<p>通过权威机构的颁布的数字证书，证明你的网站是好网站。</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5218a75e42b94ca8964721d362763a16~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123; generateKeyPairSync, createSign, createVerify, createHash &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'crypto'</span>);
<span class="hljs-keyword">let</span> passphrase = <span class="hljs-string">'zhufeng'</span>;
<span class="hljs-keyword">let</span> rsa = generateKeyPairSync(<span class="hljs-string">'rsa'</span>, &#123;
    <span class="hljs-attr">modulusLength</span>: <span class="hljs-number">1024</span>,
    <span class="hljs-attr">publicKeyEncoding</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'spki'</span>,
        <span class="hljs-attr">format</span>: <span class="hljs-string">'pem'</span>
    &#125;,
    <span class="hljs-attr">privateKeyEncoding</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'pkcs8'</span>,
        <span class="hljs-attr">format</span>: <span class="hljs-string">'pem'</span>,
        <span class="hljs-attr">cipher</span>: <span class="hljs-string">'aes-256-cbc'</span>,
        passphrase
    &#125;
&#125;);
<span class="hljs-keyword">const</span> info = &#123;
    <span class="hljs-attr">domain</span>: <span class="hljs-string">"http://127.0.0.1:8080"</span>,
    <span class="hljs-attr">publicKey</span>: rsa.publicKey
&#125;;
<span class="hljs-keyword">const</span> hash = createHash(<span class="hljs-string">'sha256'</span>).update(<span class="hljs-built_in">JSON</span>.stringify(info)).digest(<span class="hljs-string">'hex'</span>);
<span class="hljs-keyword">const</span> sign = getSign(hash, rsa.privateKey, passphrase);
<span class="hljs-keyword">const</span> cert = &#123; info, sign &#125;;

<span class="hljs-keyword">let</span> certIsValid = verifySign(hash, cert.sign, rsa.publicKey);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'certIsValid'</span>, certIsValid);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSign</span>(<span class="hljs-params">content, privateKey, passphrase</span>) </span>&#123;
    <span class="hljs-keyword">var</span> sign = createSign(<span class="hljs-string">'RSA-SHA256'</span>);
    sign.update(content);
    <span class="hljs-keyword">return</span> sign.sign(&#123; <span class="hljs-attr">key</span>: privateKey, <span class="hljs-attr">format</span>: <span class="hljs-string">'pem'</span>, passphrase &#125;, <span class="hljs-string">'hex'</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">verifySign</span>(<span class="hljs-params">content, sign, publicKey</span>) </span>&#123;
    <span class="hljs-keyword">var</span> verify = createVerify(<span class="hljs-string">'RSA-SHA256'</span>);
    verify.update(content);
    <span class="hljs-keyword">return</span> verify.verify(publicKey, sign, <span class="hljs-string">'hex'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过如上流程，可以成功避免坏人的信息劫持。</p>
<h2 data-id="heading-6">结论：</h2>
<p>上述就是https如果保证我们安全做的事情。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            

---
title: 'go-dongle 0.0.1 版本发布了，支持常规编码解码以及加密解密方法'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=197'
author: 开源中国
comments: false
date: Fri, 13 Aug 2021 15:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=197'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">dongle 是一个<span style="background-color:#ffffff; color:#40485b">轻量级、语义化、对开发者友好的Golang编码解码和加密解密库</span></p> 
<p style="text-align:left">如果您觉得不错，请给个 star 吧<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fdongle" target="_blank">github.com/golang-module/dongle</a><br> <a href="https://gitee.com/go-package/dongle">gitee.com/go-package/dongle</a></p> 
<h4 style="text-align:left">安装使用</h4> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 使用 github 库</span>
go <span style="color:#d73a49">get</span> -u github.com/golang-module/dongle

<span style="color:#d73a49">import</span> (
    <span style="color:#032f62">"github.com/golang-module/dongle"</span>
)

<span style="color:#6a737d">// 使用 gitee 库</span>
go <span style="color:#d73a49">get</span> -u gitee.com/go-package/dongle

<span style="color:#d73a49">import</span> (
    <span style="color:#032f62">"gitee.com/go-package/dongle"</span>
)</code></pre> 
<h4 style="text-align:left">编码&加密</h4> 
<p style="text-align:left">Base32 编码</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 base32 编码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByBase32</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// NBSWY3DPEB3W64TMMQ======</span>
<span style="color:#6a737d">// 对字符串进行 base32 编码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByBase32</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("NBSWY3DPEB3W64TMMQ======")</span>

<span style="color:#6a737d">// 对字节切片进行 base32 编码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"hello world"</span>))<span style="color:#6f42c1">.ByBase32</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// NBSWY3DPEB3W64TMMQ======</span>
<span style="color:#6a737d">// 对字节切片进行 base32 编码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"hello world"</span>))<span style="color:#6f42c1">.ByBase32</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("NBSWY3DPEB3W64TMMQ======")</span></code></pre> 
<p style="text-align:left">Base64 编码</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 base64 编码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByBase64</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// aGVsbG8gd29ybGQ=</span>
<span style="color:#6a737d">// 对字符串进行 base64 编码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByBase64</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("aGVsbG8gd29ybGQ=")</span>

<span style="color:#6a737d">// 对字节切片进行 base64 编码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"hello world"</span>))<span style="color:#6f42c1">.ByBase64</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// aGVsbG8gd29ybGQ=</span>
<span style="color:#6a737d">// 对字节切片进行 base64 编码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"hello world"</span>))<span style="color:#6f42c1">.ByBase64</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("aGVsbG8gd29ybGQ=")</span></code></pre> 
<p style="text-align:left">Hex 编码</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 hex 编码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByHex</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 68656c6c6f20776f726c64=</span>
<span style="color:#6a737d">// 对字符串进行 hex 编码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByHex</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("68656c6c6f20776f726c64")</span>

<span style="color:#6a737d">// 对字节切片进行 hex 编码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"hello world"</span>))<span style="color:#6f42c1">.ByHex</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 68656c6c6f20776f726c64</span>
<span style="color:#6a737d">// 对字节切片进行 hex 编码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"hello world"</span>))<span style="color:#6f42c1">.ByHex</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("68656c6c6f20776f726c64")</span></code></pre> 
<p style="text-align:left">Md5 加密</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 md5 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 5eb63bbbe01eeed093cb22bb8f5acdc3</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// 5eb63bbbe01eeed093cb22bb8f5acdc3</span>
<span style="color:#6a737d">// 对字符串进行 md5 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// L23DXO7AD3XNBE6LEK5Y6WWNYM======</span>
<span style="color:#6a737d">// 对字符串进行 md5 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// XrY7u+Ae7tCTyyK7j1rNww==</span>

<span style="color:#6a737d">// 对字符串进行 md5 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("5eb63bbbe01eeed093cb22bb8f5acdc3")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("5eb63bbbe01eeed093cb22bb8f5acdc3")</span>
<span style="color:#6a737d">// 对字符串进行 md5 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("L23DXO7AD3XNBE6LEK5Y6WWNYM======")</span>
<span style="color:#6a737d">// 对字符串进行 md5 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("XrY7u+Ae7tCTyyK7j1rNww==")</span>

<span style="color:#6a737d">// 对字节切片进行 md5 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 5eb63bbbe01eeed093cb22bb8f5acdc3</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// 5eb63bbbe01eeed093cb22bb8f5acdc3</span>
<span style="color:#6a737d">// 对字节切片进行 md5 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// L23DXO7AD3XNBE6LEK5Y6WWNYM======</span>
<span style="color:#6a737d">// 对字节切片进行 md5 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// XrY7u+Ae7tCTyyK7j1rNww==</span>

<span style="color:#6a737d">// 对字节切片进行 md5 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("5eb63bbbe01eeed093cb22bb8f5acdc3")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("5eb63bbbe01eeed093cb22bb8f5acdc3")</span>
<span style="color:#6a737d">// 对字节切片进行 md5 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("L23DXO7AD3XNBE6LEK5Y6WWNYM======")</span>
<span style="color:#6a737d">// 对字节切片进行 md5 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("XrY7u+Ae7tCTyyK7j1rNww==")</span>

<span style="color:#6a737d">// 对文件进行 md5 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromFile</span>(<span style="color:#032f62">"./LICENSE"</span>))<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 014f03f9025ea81a8a0e9734be540c53</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromFile</span>(<span style="color:#032f62">"./LICENSE"</span>))<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// 014f03f9025ea81a8a0e9734be540c53</span>
<span style="color:#6a737d">// 对文件进行 md5 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromFile</span>(<span style="color:#032f62">"./LICENSE"</span>))<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// AFHQH6ICL2UBVCQOS42L4VAMKM======</span>
<span style="color:#6a737d">// 对文件进行 md5 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromFile</span>(<span style="color:#032f62">"./LICENSE"</span>))<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// AU8D+QJeqBqKDpc0vlQMUw==</span>

<span style="color:#6a737d">// 对文件进行 md5 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromFile</span>(<span style="color:#032f62">"./LICENSE"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("014f03f9025ea81a8a0e9734be540c53")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromFile</span>(<span style="color:#032f62">"./LICENSE"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("014f03f9025ea81a8a0e9734be540c53")</span>
<span style="color:#6a737d">// 对文件进行 md5 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromFile</span>(<span style="color:#032f62">"./LICENSE"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("AFHQH6ICL2UBVCQOS42L4VAMKM======")</span>
<span style="color:#6a737d">// 对文件进行 md5 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromFile</span>(<span style="color:#032f62">"./LICENSE"</span>)<span style="color:#6f42c1">.ByMd5</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("AU8D+QJeqBqKDpc0vlQMUw==")</span></code></pre> 
<p style="text-align:left">Sha1 加密</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 sha1 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed</span>
<span style="color:#6a737d">// 对字符串进行 sha1 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// FKXGYNOJJ7H3IFO35FPUBC445EPOQRXN</span>
<span style="color:#6a737d">// 对字符串进行 sha1 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// Kq5sNclPz7QV2+lfQIuc6R7oRu0=</span>

<span style="color:#6a737d">// 对字符串进行 sha1 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("2aae6c35c94fcfb415dbe95f408b9ce91ee846ed")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("2aae6c35c94fcfb415dbe95f408b9ce91ee846ed")</span>
<span style="color:#6a737d">// 对字符串进行 sha1 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("FKXGYNOJJ7H3IFO35FPUBC445EPOQRXN")</span>
<span style="color:#6a737d">// 对字符串进行 sha1 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("Kq5sNclPz7QV2+lfQIuc6R7oRu0=")</span>

<span style="color:#6a737d">// 对字节切片进行 sha1 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed</span>
<span style="color:#d73a49">openssl</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed</span>
<span style="color:#6a737d">// 对字节切片进行 sha1 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// FKXGYNOJJ7H3IFO35FPUBC445EPOQRXN</span>
<span style="color:#6a737d">// 对字节切片进行 sha1 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// Kq5sNclPz7QV2+lfQIuc6R7oRu0=</span>

<span style="color:#6a737d">// 对字节切片进行 sha1 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("2aae6c35c94fcfb415dbe95f408b9ce91ee846ed")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("2aae6c35c94fcfb415dbe95f408b9ce91ee846ed")</span>
<span style="color:#6a737d">// 对字节切片进行 sha1 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("FKXGYNOJJ7H3IFO35FPUBC445EPOQRXN")</span>
<span style="color:#6a737d">// 对字节切片进行 sha1 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.BySha1</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("Kq5sNclPz7QV2+lfQIuc6R7oRu0=")</span></code></pre> 
<p style="text-align:left">Sha224 加密</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 sha224 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// 2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b</span>
<span style="color:#6a737d">// 对字符串进行 sha224 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// F4CUO76CJO2PV36YMULRK3NP33HMIW4K2PHSKIVFMNMCW===</span>
<span style="color:#6a737d">// 对字符串进行 sha224 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// LwVHf8JLtPrv2GUXFW2v3s7EW4rTzyUipWNYKw==</span>

<span style="color:#6a737d">// 对字符串进行 sha224 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b")</span>
<span style="color:#6a737d">// 对字符串进行 sha224 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("F4CUO76CJO2PV36YMULRK3NP33HMIW4K2PHSKIVFMNMCW===")</span>
<span style="color:#6a737d">// 对字符串进行 sha224 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("LwVHf8JLtPrv2GUXFW2v3s7EW4rTzyUipWNYKw==")</span>

<span style="color:#6a737d">// 对字节切片进行 sha224 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// 2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b</span>
<span style="color:#6a737d">// 对字节切片进行 sha224 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// F4CUO76CJO2PV36YMULRK3NP33HMIW4K2PHSKIVFMNMCW===</span>
<span style="color:#6a737d">// 对字节切片进行 sha224 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// LwVHf8JLtPrv2GUXFW2v3s7EW4rTzyUipWNYKw==</span>

<span style="color:#6a737d">// 对字节切片进行 sha224 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b")</span>
<span style="color:#6a737d">// 对字节切片进行 sha224 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("F4CUO76CJO2PV36YMULRK3NP33HMIW4K2PHSKIVFMNMCW===")</span>
<span style="color:#6a737d">// 对字节切片进行 sha224 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha224</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("LwVHf8JLtPrv2GUXFW2v3s7EW4rTzyUipWNYKw==")</span></code></pre> 
<p style="text-align:left">Sha256 加密</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 sha256 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9</span>
<span style="color:#6a737d">// 对字符串进行 sha256 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// XFGSPOMTJU7ARJJOKLL5U7NL7LCIJ37DPJJYB3UQRD32ZYXPZXUQ====</span>
<span style="color:#6a737d">// 对字符串进行 sha256 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// uU0nuZNNPgilLlLX2n2r+sSE7+N6U4DukIj3rOLvzek=</span>

<span style="color:#6a737d">// 对字符串进行 sha256 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9")</span>
<span style="color:#6a737d">// 对字符串进行 sha256 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("XFGSPOMTJU7ARJJOKLL5U7NL7LCIJ37DPJJYB3UQRD32ZYXPZXUQ====")</span>
<span style="color:#6a737d">// 对字符串进行 sha256 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("uU0nuZNNPgilLlLX2n2r+sSE7+N6U4DukIj3rOLvzek=")</span>

<span style="color:#6a737d">// 对字节切片进行 sha256 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9</span>
<span style="color:#6a737d">// 对字节切片进行 sha256 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// XFGSPOMTJU7ARJJOKLL5U7NL7LCIJ37DPJJYB3UQRD32ZYXPZXUQ====</span>
<span style="color:#6a737d">// 对字节切片进行 sha256 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// uU0nuZNNPgilLlLX2n2r+sSE7+N6U4DukIj3rOLvzek=</span>

<span style="color:#6a737d">// 对字节切片进行 sha256 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9")</span>
<span style="color:#6a737d">// 对字节切片进行 sha256 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("XFGSPOMTJU7ARJJOKLL5U7NL7LCIJ37DPJJYB3UQRD32ZYXPZXUQ====")</span>
<span style="color:#6a737d">// 对字节切片进行 sha256 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha256</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("uU0nuZNNPgilLlLX2n2r+sSE7+N6U4DukIj3rOLvzek=")</span></code></pre> 
<p style="text-align:left">Sha384 加密</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 sha384 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd</span>
<span style="color:#6a737d">// 对字符串进行 sha384 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// 7W6Y45NGP4U7OANE4BADQXROEOMGGA7KCARZEENPSB74XOBVPCZ6IF6LOHHGI3X5BAM53DAIRXQ32===</span>
<span style="color:#6a737d">// 对字符串进行 sha384 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// /b2OdaZ/KfcBpOBAOF4uI5hjA+oQI5IRr5B/y7g1eLPkF8txzmRu/QgZ3YwIjeG9</span>

<span style="color:#6a737d">// 对字符串进行 sha384 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd")</span>
<span style="color:#6a737d">// 对字符串进行 sha384 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("7W6Y45NGP4U7OANE4BADQXROEOMGGA7KCARZEENPSB74XOBVPCZ6IF6LOHHGI3X5BAM53DAIRXQ32===")</span>
<span style="color:#6a737d">// 对字符串进行 sha384 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("/b2OdaZ/KfcBpOBAOF4uI5hjA+oQI5IRr5B/y7g1eLPkF8txzmRu/QgZ3YwIjeG9")</span>

<span style="color:#6a737d">// 对字节切片进行 sha384 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd</span>
<span style="color:#6a737d">// 对字节切片进行 sha384 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// 7W6Y45NGP4U7OANE4BADQXROEOMGGA7KCARZEENPSB74XOBVPCZ6IF6LOHHGI3X5BAM53DAIRXQ32===</span>
<span style="color:#6a737d">// 对字节切片进行 sha384 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">openssl</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// /b2OdaZ/KfcBpOBAOF4uI5hjA+oQI5IRr5B/y7g1eLPkF8txzmRu/QgZ3YwIjeG9</span>

<span style="color:#6a737d">// 对字节切片进行 sha384 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd")</span>
<span style="color:#6a737d">// 对字节切片进行 sha384 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("7W6Y45NGP4U7OANE4BADQXROEOMGGA7KCARZEENPSB74XOBVPCZ6IF6LOHHGI3X5BAM53DAIRXQ32===")</span>
<span style="color:#6a737d">// 对字节切片进行 sha384 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha384</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("/b2OdaZ/KfcBpOBAOF4uI5hjA+oQI5IRr5B/y7g1eLPkF8txzmRu/QgZ3YwIjeG9")</span></code></pre> 
<p style="text-align:left">Sha512 加密</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 sha512 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f</span>
<span style="color:#6a737d">// 对字符串进行 sha512 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// GCPMYSE4CLLOWTGEB5IMSAXSWTIO257OKENHY6U3ZU6KQ3KM3BXZRHOTLPC76SMWODNDIJK3IWYM7WBQ5APWAXOPPXCVILUTV2ONO3Y=</span>
<span style="color:#6a737d">// 对字符串进行 sha512 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// MJ7MSJwS1utMxA9QyQLytNDtd+5RGnx6m808qG1M2G+YndNbxf9JlnDaNCVbRbDP2DDoH2Bdz33FVC6TrpzXbw==</span>

<span style="color:#6a737d">// 对字符串进行 sha512 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f")</span>
<span style="color:#6a737d">// 对字符串进行 sha512 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("GCPMYSE4CLLOWTGEB5IMSAXSWTIO257OKENHY6U3ZU6KQ3KM3BXZRHOTLPC76SMWODNDIJK3IWYM7WBQ5APWAXOPPXCVILUTV2ONO3Y=")</span>
<span style="color:#6a737d">// 对字符串进行 sha512 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("MJ7MSJwS1utMxA9QyQLytNDtd+5RGnx6m808qG1M2G+YndNbxf9JlnDaNCVbRbDP2DDoH2Bdz33FVC6TrpzXbw==")</span>

<span style="color:#6a737d">// 对字节切片进行 sha512 加密，输出 hex 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f</span>
<span style="color:#6a737d">// 对字节切片进行 sha512 加密，输出 base32 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// GCPMYSE4CLLOWTGEB5IMSAXSWTIO257OKENHY6U3ZU6KQ3KM3BXZRHOTLPC76SMWODNDIJK3IWYM7WBQ5APWAXOPPXCVILUTV2ONO3Y=</span>
<span style="color:#6a737d">// 对字节切片进行 sha512 加密，输出 base64 编码字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToString</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// MJ7MSJwS1utMxA9QyQLytNDtd+5RGnx6m808qG1M2G+YndNbxf9JlnDaNCVbRbDP2DDoH2Bdz33FVC6TrpzXbw==</span>

<span style="color:#6a737d">// 对字节切片进行 sha512 加密，输出 hex 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f")</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"hex"</span>) <span style="color:#6a737d">// []byte("309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f")</span>
<span style="color:#6a737d">// 对字节切片进行 sha512 加密，输出 base32 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base32"</span>) <span style="color:#6a737d">// []byte("GCPMYSE4CLLOWTGEB5IMSAXSWTIO257OKENHY6U3ZU6KQ3KM3BXZRHOTLPC76SMWODNDIJK3IWYM7WBQ5APWAXOPPXCVILUTV2ONO3Y=")</span>
<span style="color:#6a737d">// 对字节切片进行 sha512 加密，输出 base64 编码字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Encrypt</span><span style="color:#6f42c1">.FromBytes</span>(<span style="color:#032f62">"hello world"</span>)<span style="color:#6f42c1">.Sha512</span>()<span style="color:#6f42c1">.ToBytes</span>(<span style="color:#032f62">"base64"</span>) <span style="color:#6a737d">// []byte("MJ7MSJwS1utMxA9QyQLytNDtd+5RGnx6m808qG1M2G+YndNbxf9JlnDaNCVbRbDP2DDoH2Bdz33FVC6TrpzXbw==")</span></code></pre> 
<h4 style="text-align:left">解码&解密</h4> 
<p style="text-align:left">Base32 解码</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 base64 解码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"NBSWY3DPEB3W64TMMQ======"</span>)<span style="color:#6f42c1">.ByBase32</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// hello world</span>
<span style="color:#6a737d">// 对字符串进行 base64 解码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"NBSWY3DPEB3W64TMMQ======"</span>)<span style="color:#6f42c1">.ByBase32</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("hello world")</span>

<span style="color:#6a737d">// 对字节切片进行 base64 解码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"NBSWY3DPEB3W64TMMQ======"</span>))<span style="color:#6f42c1">.ByBase32</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// hello world</span>
<span style="color:#6a737d">// 对字节切片进行 base64 解码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"NBSWY3DPEB3W64TMMQ======"</span>))<span style="color:#6f42c1">.ByBase32</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("hello world")</span></code></pre> 
<p style="text-align:left">Base64 解码</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 base64 解码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"aGVsbG8gd29ybGQ="</span>)<span style="color:#6f42c1">.ByBase64</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// hello world</span>
<span style="color:#6a737d">// 对字符串进行 base64 解码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"aGVsbG8gd29ybGQ="</span>)<span style="color:#6f42c1">.ByBase64</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("hello world")</span>

<span style="color:#6a737d">// 对字节切片进行 base64 解码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"aGVsbG8gd29ybGQ="</span>))<span style="color:#6f42c1">.ByBase64</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// hello world</span>
<span style="color:#6a737d">// 对字节切片进行 base64 解码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"aGVsbG8gd29ybGQ="</span>))<span style="color:#6f42c1">.ByBase64</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("hello world")</span></code></pre> 
<p style="text-align:left">Hex 解码</p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#6a737d">// 对字符串进行 hex 解码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"68656c6c6f20776f726c64"</span>)<span style="color:#6f42c1">.ByHex</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// hello world</span>
<span style="color:#6a737d">// 对字符串进行 hex 解码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromString</span>(<span style="color:#032f62">"68656c6c6f20776f726c64"</span>)<span style="color:#6f42c1">.ByHex</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("hello world")</span>

<span style="color:#6a737d">// 对字节切片进行 hex 解码，输出字符串</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"68656c6c6f20776f726c64"</span>))<span style="color:#6f42c1">.ByHex</span>()<span style="color:#6f42c1">.ToString</span>() <span style="color:#6a737d">// hello world</span>
<span style="color:#6a737d">// 对字节切片进行 hex 解码，输出字节切片</span>
<span style="color:#d73a49">dongle</span><span style="color:#6f42c1">.Decode</span><span style="color:#6f42c1">.FromBytes</span>([]byte(<span style="color:#032f62">"68656c6c6f20776f726c64"</span>))<span style="color:#6f42c1">.ByHex</span>()<span style="color:#6f42c1">.ToBytes</span>() <span style="color:#6a737d">// []byte("hello world")</span></code></pre> 
<h4 style="text-align:left">错误处理</h4> 
<p style="text-align:left">如果有多个错误发生，只返回第一个错误，前一个错误排除后才返回下一个错误</p> 
<pre style="text-align:left"><code class="language-go">e := dongle.<span style="color:#d73a49">Encrypy</span>.<span style="color:#d73a49">FromFile</span>(<span style="color:#032f62">"./demo.txt"</span>).<span style="color:#d73a49">ByMd5</span>()
<span style="color:#d73a49">if</span> e.<span style="color:#d73a49">Error</span> != <span style="color:#005cc5">nil</span> &#123;
    <span style="color:#6a737d">// 错误处理...</span>
    log.<span style="color:#d73a49">Fatal</span>(c.<span style="color:#d73a49">Error</span>)
&#125;
fmt.<span style="color:#d73a49">Println</span>(c.<span style="color:#d73a49">ToString</span>())
<span style="color:#6a737d">// 输出</span>
invalid file <span style="color:#032f62">"./demo.txt"</span>, please make sure the file exists</code></pre> 
<h4 style="text-align:left">待做清单</h4> 
<ul> 
 <li> AES 加密解密</li> 
 <li> DES 加密解密</li> 
 <li> 3DES 加密解密</li> 
 <li> RSA 加密解密</li> 
 <li> RC2 加密解密</li> 
 <li> RC4 加密解密</li> 
 <li> RC5 加密解密</li> 
 <li> RC6 加密解密</li> 
 <li> SM1 加密解密</li> 
 <li> SM2 加密解密</li> 
 <li> SM3 加密解密</li> 
 <li> SM4 加密解密</li> 
</ul>
                                        </div>
                                      
</div>
            
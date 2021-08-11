
---
title: 'RSA分段解密 - Vue'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b6d036e7906449eb9fc05125491b53a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 05:41:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b6d036e7906449eb9fc05125491b53a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<p>上一篇文章实现了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_41182727%2Farticle%2Fdetails%2F119142779" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_41182727/article/details/119142779" ref="nofollow noopener noreferrer">Java RSA的分段加解密 </a> ，这里我们介绍在 Vue 项目中如何使用 RSA 分段解密，这里的加解密场景是：</p>
<ul>
<li>后端私钥分段加密 - 前端公钥分段解密</li>
</ul>
<p>前端如何使用公钥解密这里不做重复叙述，注重点是分段解密，有需要的参考之前的文章：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_41182727%2Farticle%2Fdetails%2F118488784" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_41182727/article/details/118488784" ref="nofollow noopener noreferrer">RSA加密 - Vue</a></p>
<br>
<h4 data-id="heading-1">具体实现</h4>
<ul>
<li><code>src/libs/jsencrypt/lib/JSEncrypt.js</code>中添加新的解密方法<code>decryptLong</code></li>
</ul>
<pre><code class="copyable">/**
  * 分段解密
  * @param string
  * @returns &#123;string|boolean&#125;
  */
 JSEncrypt.prototype.decryptLong = function (string) &#123;
     let k = this.getKey();
     let MAX_DECRYPT_BLOCK = 128;//分段解密最大长度限制为128字节
     try &#123;
         let ct = "";
         let t1;
         let bufTmp;
         let hexTmp;
         let str = bytesToHex(string);
         let buf = hexToBytes(str);
         let inputLen = buf.length;

         //开始长度
         let offSet = 0;
         //结束长度
         let endOffSet = MAX_DECRYPT_BLOCK;

         //分段解密
         while (inputLen - offSet > 0) &#123;
             if (inputLen - offSet > MAX_DECRYPT_BLOCK) &#123;
                 bufTmp = buf.slice(offSet, endOffSet);
                 hexTmp = bytesToHex(bufTmp);
                 t1 = k.decrypt(hexTmp);
                 ct += t1;
             &#125; else &#123;
                 bufTmp = buf.slice(offSet, inputLen);
                 hexTmp = bytesToHex(bufTmp);
                 t1 = k.decrypt(hexTmp);
                 ct += t1;
             &#125;
             offSet += MAX_DECRYPT_BLOCK;
             endOffSet += MAX_DECRYPT_BLOCK;
         &#125;
         return ct;
     &#125; catch (ex) &#123;
         console.log("RSA分段解密失败", ex)
         return false;
     &#125;
 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>添加<code>JSEncryptRSAassist.js</code>到<code>src/libs/jsencrypt/lib/</code>目录下</li>
</ul>
<pre><code class="copyable">/**
 * RSA 分段解密辅助
 * @param hex
 * @returns &#123;[]&#125;
 */

/**
 * 16进制转byte数组
 */
function hexToBytes(hex) &#123;
    let bytes = [];
    for (let c = 0; c < hex.length; c += 2)
        bytes.push(parseInt(hex.substr(c, 2), 16));
    return bytes;
&#125;

/**
 * byte数组转16进制
 * @param bytes
 * @returns &#123;string&#125;
 */
function bytesToHex(bytes) &#123;
    let hex = [];
    for (let i = 0; i < bytes.length; i++) &#123;
        hex.push((bytes[i] >>> 4).toString(16));
        hex.push((bytes[i] & 0xF).toString(16));
    &#125;
    return hex.join("");
&#125;

/**
 * base64转btye数组
 * @param base64
 * @returns &#123;Uint8Array&#125;
 */
function base64ToArrayBuffer(base64) &#123;
    let binary_string = window.atob(base64);
    let len = binary_string.length;
    let bytes = new Uint8Array(len);
    for (let i = 0; i < len; i++) &#123;
        bytes[i] = binary_string.charCodeAt(i);
    &#125;

    return bytes;
&#125;

export &#123;
    hexToBytes,
    bytesToHex,
    base64ToArrayBuffer
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>公钥分段解密<code>RSADecryption.js</code></li>
</ul>
<pre><code class="copyable">/**
 * 非对称加密 - RSA
 * 后端私钥分段加密 - 前端公钥分段解密
 */
import &#123; JSEncrypt &#125; from '../libs/jsencrypt/lib/JSEncrypt'
import &#123; base64ToArrayBuffer &#125; from '../libs/jsencrypt/lib/JSEncryptRSAassist';

const PUBLICKEY = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCaaI4MBywkCjIppZnraqN3pbrcZTq/t0+aMBo8K3pK9BDD6XkM6N2Yfcva7BSFbUWuAcI7piXak0UKn9CElDuhNzUSgQn4IXKxIt3Iva5cV83qYumj+0yRjjLT8Muu1Y1rgBZjY9oBwhVoV+Twg25+UJ+6Q6HM4xTwQQJDoyy4jwIDAQAB';

export const RSADECRY = &#123;
    /**
     * 公钥分段解密
     * @returns &#123;string&#125;
     * @param val
     */
    decryptLongByPublicKey: function (val = '') &#123;
        if(val === '')&#123;
            return '';
        &#125;
        let encrypt = new JSEncrypt()
        encrypt.setPublicKey(PUBLICKEY) // 设置公钥

        // 后端使用 URLEncoder 进行编码，前端解密后使用 decodeURIComponent 解码解决中文乱码问题
        let decryptStr = decodeURIComponent(encrypt.decryptLong(base64ToArrayBuffer(val)));

        return decryptStr ? decryptStr : val;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>前端公钥分段解密调用，这里的<code>encryptStr</code>是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_41182727%2Farticle%2Fdetails%2F119142779" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_41182727/article/details/119142779" ref="nofollow noopener noreferrer">RSA分段加密 - Java</a>  中加密的密文</li>
</ul>
<pre><code class="copyable">console.log("===================")
let encryptStr = 'LfQFzBVRelSjnohshZlMvTUPsfdaD9t7FEreaAKop5Pf4X33exYMykBS12XCgnMP+GtO08ir5qmsnwVU5iP/lHMlTBSkWiGX16zFV/pmwQF8OY62HrhzXZn0gSu1rIgPKIowQ2W254uYPHDIIxvWJB/dNmeeqrgc5JxDdLVEuZU=';
let decryptLongByPublicKey = RSADECRY.decryptLongByPublicKey(encryptStr);
console.log("decryptLongByPublicKey: ", decryptLongByPublicKey);
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<ul>
<li>结果如下：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b6d036e7906449eb9fc05125491b53a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h4 data-id="heading-2">源码</h4>
<ul>
<li>GitHub： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMaggieq8324%2Fcoisini-rsa" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Maggieq8324/coisini-rsa" ref="nofollow noopener noreferrer">github.com/Maggieq8324…</a></li>
<li>Gitee：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fmaggieq8324%2Fcoisini-rsa" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/maggieq8324/coisini-rsa" ref="nofollow noopener noreferrer">gitee.com/maggieq8324…</a></li>
</ul>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>−</mo><mi>E</mi><mi>n</mi><mi>d</mi><mo>−</mo></mrow><annotation encoding="application/x-tex">- End -</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.77777em;vertical-align:-0.08333em;"></span><span class="mord">−</span><span class="mord mathnormal" style="margin-right:0.05764em;">E</span><span class="mord mathnormal">n</span><span class="mord mathnormal">d</span><span class="mord">−</span></span></span></span></span></p></div>  
</div>
            
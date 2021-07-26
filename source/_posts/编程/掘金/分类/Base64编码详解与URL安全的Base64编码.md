
---
title: 'Base64编码详解与URL安全的Base64编码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5711d1138f4dc6a6f5f92d2af5b75d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 00:17:24 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5711d1138f4dc6a6f5f92d2af5b75d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Base64的基本编码方式</h2>
<p>base64编码是一种常见的编码方式，主要用于对8bit的字节进行编码。具体的编码方式是：</p>
<p>1. 把三个字节作为一组，转化为二进制的形式，一共3*8=24个二进制位。例如： abc 三个字符用ASCII编码，转换为二进制：</p>
<p>01100001 01100010 01100011</p>
<p>2. 把24个二进制数字每6个一组，分为4组：</p>
<p>01100001 01100010 01100011 被分为</p>
<p>011000 010110 001001 100011</p>
<p>3. 按照表格，把每组二进制串转为对应字符</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5711d1138f4dc6a6f5f92d2af5b75d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>表格来源于百度百科</p>
<p>011000 010110 001001 100011 先转为十进制数字：<br>
24 22 9 35 对照表格，转化为字符串：<br>
YWJj<br>
这个字符串就是最终的Base64编码，与网络上在线编码器生成的一致：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3af19c0e7c224c8594565aac313b671b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">字节数不能被三整除时的特殊处理</h2>
<p>如果需要编码的字节不能被3整除怎么办？比如最后剩下一个单字节a，或者双字节ab。这时候我们需要特殊处理：</p>
<ol>
<li>不足6个二进制位的补0</li>
<li>不足4组的，最后补字符串=</li>
</ol>
<p>单字节a：<br>
a => 01100001 => 011000 01 => 补0 =><br>
011000 010000 => 24 16 => YQ => 补=符号 => YQ==<br>
双字节ab：<br>
ab => 01100001 01100010 => 011000 010110 0010 => 补0 =><br>
011000 010110 001000 => 24 22 8 => YWI => 补=符号 => YWI=</p>
<h2 data-id="heading-2">安全的Base64编码概念</h2>
<p>通过上面的对照表可以看到，除了大小写字母和数字之外，Base64编码后的字符串中可能包含"+/="之类的字符，而"/"，"="等是URL的保留字符或不安全字符，因此如果直接在URL中传输Base64编码，保留字符和不安全字符会被替换为%XX的形式，对后端来说解码不方便。如果不替换，就会造成URL注入漏洞。<br>
因此，有一种URL安全的Base64编码，可以解决这个问题。 URL安全的Base64编码特点：</p>
<ol>
<li>不能被3整除时，不补=符号。</li>
<li>生成Base64编码中，"+"和"/"被替换成其他非URL保留字符，使其可以直接放入URL中传输。<br>
比如"+"和"/"被替换成"-"和"_"。</li>
</ol>
<p>安全的Base64编码也有好多种，有些编码不会去掉等号，有些编码替换的符号不同。</p>
<h2 data-id="heading-3">注意示项和示例</h2>
<p>注意，是编码后的"+"和"/"被替换，而不是编码前的原始字符被替换，而这种情况并不常见。在没有遇到补齐和编码后出现"+"和"/"的场景下，安全和不安全的Base64编码输出是一致的。<br>
这里看几个例子：</p>
<ol>
<li>原字符串 abcdef<br>
原始Base编码： YWJjZGVm<br>
安全Base编码： YWJjZGVm</li>
<li>原字符串 +/=<br>
原始Base编码： Ky89<br>
安全Base编码： Ky89</li>
<li>原字符串 06?<br>
原始Base编码： MDY/<br>
安全Base编码： MDY_</li>
</ol>
<p>可以看到，即使原字符串中包含+/等特殊字符，也与Base编码是否安全无关。只有在生成后的编码中包含+/等特殊字符时，才会出现安全的Base64编码与原始Base编码不同而情况。</p>
<h2 data-id="heading-4">#Web前端中的使用</h2>
<p>Web前端中有几种常见的Base64编码的函数和库，这几种库是安全的还是不安全的？我进行了测试：</p>
<pre><code class="copyable">import &#123; Base64 &#125; from "js-base64";
import &#123; btoau, atobu &#125; from "b2a";
const item = '06?';
// 方法1
const encode1 = Base64.encode(item);
const decode1 = Base64.decode(encode1);
// 方法2
const encode2 = btoau(item);
const decode2 = atobu(encode2);
// 方法3
const encode3 = window.btoa(item);
const decode3 = window.atob(encode3);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是三种web前端常用的Base64编码方法。方法1使用了js-base64库，方法2使用了b2a库，方法3是window对象自带的编码方法。我用几个字符串进行了测试：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd6f7c4aa7284befb4230601fc6c572c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf81058f054d454a8d0674dce3214419~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5734cf932814dfa9e6f2e5c862bb4e5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结：三个Base64编码函数，方法1是原始的，方法2和3是安全的。但是三个方法都没有去掉最后的"="符号。实际开发中使用时，需要和后端的解码方法保持一致即可，如果不一致，可能会遇到特殊数据时后端无法正常解码。另外，目前网络上常用的在线Base64编解码，一般都是原始的Base64编码形式，并不是安全的。</p></div>  
</div>
            
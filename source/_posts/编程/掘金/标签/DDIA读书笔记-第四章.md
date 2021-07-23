
---
title: 'DDIA读书笔记-第四章'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/927d2c97ccaa438aa604c49e29f2e7c0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 04:21:38 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/927d2c97ccaa438aa604c49e29f2e7c0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/927d2c97ccaa438aa604c49e29f2e7c0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">兼容性</h2>
<p>兼容性这块儿，个人理解:向前兼容是旧版本服务可以读取新版本服务写的数据，向后兼容则是新版本服务可以读取旧版本服务写的数据。实质上是服务不变，数据模式变（比如新插入一列）；数据模式不变，服务变（服务做了升级，业务逻辑有新的处理）。任何编码格式都要解决其中一种或者两种的兼容性问题。</p>
<h2 data-id="heading-1">数据编码格式</h2>
<h3 data-id="heading-2">数据表现形式</h3>
<ul>
<li>数据存储在内存。就有对象，结构体，列表，数组等。同时对访问和操作做了优化</li>
<li>数据在文件或网络中传输。就有字节序列</li>
</ul>
<p>内存---->字节序列====序列化或者编码</p>
<p>字节序列---->内存====反序列化或解码</p>
<h3 data-id="heading-3">数据交互格式</h3>
<p>主要分为语言自身的格式以及标准化编码和基于模式的二进制编码</p>
<ul>
<li>
<p><strong>语言自身格式</strong></p>
<p>这个容易理解，很多开发语言都有内置的编解码工具，比如java有 Serializable 。这种编码格式用起来方便，但是缺点多，不能跨语言传输，效率低，安全问题等等</p>
</li>
</ul>

<ul>
<li>
<p><strong>标准化编码</strong></p>
<p>Json和XML以及CSV。传输过程中是序列化为二进制</p>
</li>
<li>
<p><strong>基于模式的二进制编码</strong></p>
<p>书中提到了Thrift，PB，AVRO这三个。简而言之，前两个模式是固定，也就是说提前预置好的编解码格式，不能在运行中兼容其他模式，只能满足向后兼容，也就是说数据模式不变，服务来回更新。Thrift提供了两种编码方式，差别在于CompactProtocol对于字节进行了压缩，将高位的0全部干掉。PB用的方式和Thrift的CompactProtocol一样，节省空间。AVRO比较特殊，它提供了读和写两种模式。这两种模式是互相解耦的可以按照自己需要的模式进行读和写。因此它是支持向前向后兼容。向前兼容其实就是新模式作为写，旧模式作为读；向后兼容则是新模式作为读，旧模式作为写。</p>
</li>
</ul>
<h2 data-id="heading-4">数据流模式</h2>
<ul>
<li>
<p>基于数据库的数据流</p>
<p>数据库的数据模式向前向后兼容都支持。这种支持方式主要是靠服务来保证的。同时由于线上环境进行模式迁移（比如相同表之间结构的变化）成本较高，可以认为模式是不变。另外数据库进行归档存储时候模式也会存储，这个很好理解，任何一个数据库都不会只要数据不要格式进行归档</p>
</li>
<li>
<p>基于服务的数据流</p>
<p>web服务这里面主要有提到了 RestFull Soap rpc 这三个。restfull主要是Http的一种理念，后两者是实际传输的模式</p>
</li>
<li>
<p>基于消息传递的数据流</p>
<p>消息代理，作者罗列了一大堆特点，其实说的就是MQ。</p>
<p>Actor框架，实质就是消息代理和单个Actor节点的融合</p>
</li>
</ul></div>  
</div>
            
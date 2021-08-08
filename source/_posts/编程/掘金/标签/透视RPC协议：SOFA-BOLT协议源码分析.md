
---
title: '透视RPC协议：SOFA-BOLT协议源码分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e09c908ee8b495ea754a5f9d3740c25~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 03:57:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e09c908ee8b495ea754a5f9d3740c25~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前提</h2>
<p>最近在看<code>Netty</code>相关的资料，刚好<code>SOFA-BOLT</code>是一个比较成熟的<code>Netty</code>自定义协议栈实现，于是决定研读<code>SOFA-BOLT</code>的源码，详细分析其协议的组成，简单分析其客户端和服务端的源码实现。</p>
<ul>
<li>吐槽一下：<code>SOFA-BOLT</code>的代码缩进和<code>FastJson</code>类似，变量名称强制对齐，对于一般开发者来说看着源码会有不适感</li>
</ul>
<p>当前阅读的源码是<code>2021-08</code>左右的<code>SOFA-BOLT</code>仓库的<code>master</code>分支源码。</p>
<h2 data-id="heading-1">SOFA-BOLT简单介绍</h2>
<p><code>SOFA-BOLT</code>是蚂蚁金融服务集团开发的一套基于<code>Netty</code>实现的网络通信框架，本质是一套<code>Netty</code>私有协议栈封装，目的是为了让开发者能将更多的精力放在基于网络通信的业务逻辑实现上，而不是过多的纠结于网络底层<code>NIO</code>的实现以及处理难以调试的网络问题和<code>Netty</code>二次开发问题。<code>SOFA-BOLT</code>的架构设计和功能如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e09c908ee8b495ea754a5f9d3740c25~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>上图来源于SOFA-BOLT官网<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview" target="_blank" rel="nofollow noopener noreferrer" title="https://www.sofastack.tech/projects/sofa-bolt/overview" ref="nofollow noopener noreferrer">www.sofastack.tech/projects/so…</a></p>
</blockquote>
<h2 data-id="heading-2">SOFA-BOLT协议透视</h2>
<p>由于<code>SOFA-BOLT</code>协议是基于<code>Netty</code>实现的自定义协议栈，协议本身的实现可以快速地在<code>Encoder</code>和<code>Decoder</code>的实现中找到，进一步定位到<code>com.alipay.remoting.rpc</code>包中。从源码得知，<code>SOFA-BOLT</code>协议目前有两个版本，协议在<code>RpcProtocol</code>和<code>RpcProtocolV2</code>的类顶部注释中有比较详细的介绍，基于这些介绍可以简单整理出两个版本协议的基本构成。</p>
<h3 data-id="heading-3">V1版本协议的基本构成</h3>
<ul>
<li><code>V1</code>版本的协议请求<code>Frame</code>基本构成：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d453f31a6bbd434089e900df3319e1dd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>V1</code>版本的协议响应<code>Frame</code>基本构成：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d45010dbbdd482e94755edfdb727fa6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>针对<code>V1</code>版本的协议，各个属性展开如下：</p>
<ul>
<li>请求<code>Frame</code>和响应<code>Frame</code>的公共属性：</li>
</ul>






















































<table><thead><tr><th align="center">属性Code</th><th align="center">属性含义</th><th align="center">Java类型</th><th align="center">大小(byte)</th><th align="center">备注</th></tr></thead><tbody><tr><td align="center">proto</td><td align="center">协议编码</td><td align="center">byte</td><td align="center">1</td><td align="center"><code>V1</code>版本下，<code>proto = 1</code>，<code>V2</code>版本下，<code>proto = 2</code></td></tr><tr><td align="center">type</td><td align="center">类型</td><td align="center">byte</td><td align="center">1</td><td align="center"><code>0 => RESPONSE</code>，<code>1 =>  REQUEST</code>，<code>2 => REQUEST_ONEWAY</code></td></tr><tr><td align="center">cmdcode</td><td align="center">命令编码</td><td align="center">short</td><td align="center">2</td><td align="center"><code>1 => rpc request</code>，<code>2 => rpc response</code></td></tr><tr><td align="center">ver2</td><td align="center">命令版本</td><td align="center">byte</td><td align="center">1</td><td align="center">从源码得知目前固定为<code>1</code></td></tr><tr><td align="center">requestId</td><td align="center">请求ID</td><td align="center">int</td><td align="center">4</td><td align="center">某个请求<code>CMD</code>的全局唯一标识</td></tr><tr><td align="center">codec</td><td align="center">编码解码器</td><td align="center">byte</td><td align="center">1</td><td align="center">-</td></tr></tbody></table>
<blockquote>
<p>上表中，codec从字面上理解是编码解码器，实际上是序列化和反序列实现的标记，V1和V2目前都是固定codec = 1，通过源码跟踪到SerializerManager的配置值为Hessian2 = 1，也就是默认使用Hessian2进行序列化和反序列化，详细见源码中的HessianSerializer</p>
</blockquote>
<ul>
<li>请求<code>Frame</code>特有的属性：</li>
</ul>





























































<table><thead><tr><th align="center">属性Code</th><th align="center">属性含义</th><th align="center">Java类型</th><th align="center">大小(byte)</th><th align="center">备注</th></tr></thead><tbody><tr><td align="center">timeout</td><td align="center">请求超时时间</td><td align="center">int</td><td align="center">4</td><td align="center"></td></tr><tr><td align="center">classLen</td><td align="center">请求对象（参数）类型的名称长度</td><td align="center">short</td><td align="center">2</td><td align="center">值<code>>=0</code></td></tr><tr><td align="center">headerLen</td><td align="center">请求头长度</td><td align="center">short</td><td align="center">2</td><td align="center">值<code>>=0</code></td></tr><tr><td align="center">contentLen</td><td align="center">请求内容长度</td><td align="center">int</td><td align="center">4</td><td align="center">值<code>>=0</code></td></tr><tr><td align="center">className bytes</td><td align="center">请求对象（参数）类型的名称</td><td align="center"><code>byte[]</code></td><td align="center">-</td><td align="center"></td></tr><tr><td align="center">header bytes</td><td align="center">请求头</td><td align="center"><code>byte[]</code></td><td align="center">-</td><td align="center"></td></tr><tr><td align="center">content bytes</td><td align="center">请求内容</td><td align="center"><code>byte[]</code></td><td align="center">-</td><td align="center"></td></tr></tbody></table>
<ul>
<li>响应<code>Frame</code>特有的属性：</li>
</ul>





























































<table><thead><tr><th align="center">属性Code</th><th align="center">属性含义</th><th align="center">Java类型</th><th align="center">大小(byte)</th><th align="center">备注</th></tr></thead><tbody><tr><td align="center">respstatus</td><td align="center">响应状态值</td><td align="center">short</td><td align="center">2</td><td align="center">在<code>ResponseStatus</code>中定义，目前内置<code>13</code>种状态，例如<code>0 => SUCCESS</code></td></tr><tr><td align="center">classLen</td><td align="center">响应对象（参数）类型的名称长度</td><td align="center">short</td><td align="center">2</td><td align="center">值<code>>=0</code></td></tr><tr><td align="center">headerLen</td><td align="center">响应头长度</td><td align="center">short</td><td align="center">2</td><td align="center">值<code>>=0</code></td></tr><tr><td align="center">contentLen</td><td align="center">响应内容长度</td><td align="center">int</td><td align="center">4</td><td align="center">值<code>>=0</code></td></tr><tr><td align="center">className bytes</td><td align="center">响应对象（参数）类型的名称</td><td align="center"><code>byte[]</code></td><td align="center">-</td><td align="center"></td></tr><tr><td align="center">header bytes</td><td align="center">响应头</td><td align="center"><code>byte[]</code></td><td align="center">-</td><td align="center"></td></tr><tr><td align="center">content bytes</td><td align="center">响应内容</td><td align="center"><code>byte[]</code></td><td align="center">-</td><td align="center"></td></tr></tbody></table>
<p>这里可以看出<code>V1</code>版本中的请求<code>Frame</code>和响应<code>Frame</code>只有细微的差别，（请求<code>Frame</code>中独立存在<code>timeout</code>属性，而响应<code>Frame</code>独立存在<code>respstatus</code>属性），绝大部分的属性都是复用的，并且三个长度和三个字节数组是相互制约的：</p>
<ul>
<li><code>classLen <=> className bytes</code></li>
<li><code>headerLen <=> header bytes</code></li>
<li><code>contentLen <=> content bytes</code></li>
</ul>
<h3 data-id="heading-4">V2版本协议的基本构成</h3>
<ul>
<li><code>V2</code>版本的协议请求<code>Frame</code>基本构成：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9670b6e33584002a4060af0d99643f9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>V2</code>版本的协议响应<code>Frame</code>基本构成：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0add6582193647e4b1191510dcd5ce07~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>V2</code>版本的协议相比<code>V1</code>版本多了<code>2</code>个必传公共属性和<code>1</code>个可选公共属性：</p>

































<table><thead><tr><th align="center">属性Code</th><th align="center">属性含义</th><th align="center">Java类型</th><th align="center">大小(byte)</th><th align="center">备注</th></tr></thead><tbody><tr><td align="center">ver1</td><td align="center">协议版本</td><td align="center">byte</td><td align="center">1</td><td align="center">是为了在<code>V2</code>版本协议中兼容<code>V1</code>版本的协议</td></tr><tr><td align="center">switch</td><td align="center">协议开关</td><td align="center">byte</td><td align="center">1</td><td align="center">基于<code>BitSet</code>实现的开关，最多<code>8</code>个</td></tr><tr><td align="center">CRC32</td><td align="center">循环冗余校验值</td><td align="center">int</td><td align="center">4</td><td align="center">可选的，由开关<code>ProtocolSwitch.CRC_SWITCH_INDEX</code>决定是否启用，启用的时候会基于整个<code>Frame</code>进行计算</td></tr></tbody></table>
<p>这几个新增属性中，<code>switch</code>代表<code>ProtocolSwitch</code>实现中的<code>BitSet</code>转换出来的<code>byte</code>字段，由于<code>byte</code>只有<code>8</code>位，因此协议在传输过程中最多只能传递<code>8</code>个开关的状态，这些开关的下标为<code>[0,7]</code>。<code>CRC32</code>是基于整个<code>Frame</code>转换出来的<code>byte</code>数组进行计算，<code>JDK</code>中有原生从<code>API</code>，可以简单构建一个工具类如下进行计算：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">Crc32Utils</span> </span>&#123;

    <span class="hljs-comment">/**
     * 单例
     */</span>
    X;

    <span class="hljs-comment">/**
     * 进行CRC32结果计算
     *
     * <span class="hljs-doctag">@param</span> content 内容
     * <span class="hljs-doctag">@return</span> crc32 result
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">long</span> <span class="hljs-title">crc32</span><span class="hljs-params">(<span class="hljs-keyword">byte</span>[] content)</span> </span>&#123;
        CRC32 crc32 = <span class="hljs-keyword">new</span> CRC32();
        crc32.update(content, <span class="hljs-number">0</span>, content.length);
        <span class="hljs-keyword">long</span> r = crc32.getValue();
        <span class="hljs-comment">// crc32.reset();</span>
        <span class="hljs-keyword">return</span> r;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>V2</code>版本协议把<code>CRC32</code>的计算结果强制转换为<code>int</code>类型，可以思考一下这里为什么不会溢出。</p>
<h2 data-id="heading-5">SOFA-BOLT架构</h2>
<p>考虑到如果分析源码，文章篇幅会比较长，并且如果有开发过<code>Netty</code>自定义协议栈的经验，<code>SOFA-BOLT</code>的源码并不复杂，这里仅仅分析<code>SOFA-BOLT</code>的架构和核心组件功能。协议由接口<code>Protocol</code>定义：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Protocol</span> </span>&#123;
    
    <span class="hljs-comment">// 命令编码器</span>
    <span class="hljs-function">CommandEncoder <span class="hljs-title">getEncoder</span><span class="hljs-params">()</span></span>;

    <span class="hljs-comment">// 命令解码器</span>
    <span class="hljs-function">CommandDecoder <span class="hljs-title">getDecoder</span><span class="hljs-params">()</span></span>;

    <span class="hljs-comment">// 心跳触发器</span>
    <span class="hljs-function">HeartbeatTrigger <span class="hljs-title">getHeartbeatTrigger</span><span class="hljs-params">()</span></span>;

    <span class="hljs-comment">// 命令处理器</span>
    <span class="hljs-function">CommandHandler <span class="hljs-title">getCommandHandler</span><span class="hljs-params">()</span></span>;

    <span class="hljs-comment">// 命令工厂</span>
    <span class="hljs-function">CommandFactory <span class="hljs-title">getCommandFactory</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由<code>V2</code>版本协议实现<code>RpcProtocolV2</code>可以得知：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/544fda004ee944db8df87aa30fb68efa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外，所有需要发送或者接收的<code>Frame</code>都被封装为<code>Command</code>，而<code>Command</code>的类族如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95de99ae28744c8d81109fba65607ea2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>也就是：</p>
<ul>
<li><code>RequestCommand</code>定义了请求命令需要的所有属性，最终由<code>RpcCommandEncoderV2</code>进行编码</li>
<li><code>ResponseCommand</code>定义了响应命令需要的所有属性，最终由<code>RpcCommandDecoderV2</code>进行解码</li>
</ul>
<p>梳理完上面的组件就可以画出下面的一个基于<code>SOFA-BOLT</code>协议进行的<code>Client => Server</code>的交互图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67d7c17388af4769b6564d1b2e301d60~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">SOFA-BOLT使用</h2>
<p>由于<code>sofa-bolt</code>已经封装好了完整的<code>RpcClient</code>和<code>RpcServer</code>，使用此协议只需要引用依赖，然后初始化客户端和服务端，编写对应的<code>UserProcessor</code>实现即可。引入相关依赖：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.alipay.sofa<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>bolt<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>1.6.3<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.caucho<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>hessian<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>4.0.65<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建请求实体类<code>RequestMessage</code>、响应实体类<code>ResponseMessage</code>和对应的处理器<code>RequestMessageProcessor</code>：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RequestMessage</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Serializable</span> </span>&#123;

    <span class="hljs-keyword">private</span> Long id;

    <span class="hljs-keyword">private</span> String content;
&#125;

<span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ResponseMessage</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Serializable</span> </span>&#123;

    <span class="hljs-keyword">private</span> Long id;

    <span class="hljs-keyword">private</span> String content;

    <span class="hljs-keyword">private</span> Long status;
&#125;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RequestMessageProcessor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SyncUserProcessor</span><<span class="hljs-title">RequestMessage</span>> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Object <span class="hljs-title">handleRequest</span><span class="hljs-params">(BizContext bizContext, RequestMessage requestMessage)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
        ResponseMessage message = <span class="hljs-keyword">new</span> ResponseMessage();
        message.setContent(requestMessage.getContent());
        message.setId(requestMessage.getId());
        message.setStatus(<span class="hljs-number">10087L</span>);
        <span class="hljs-keyword">return</span> message;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">interest</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> RequestMessage.class.getName();
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中处理器需要同步处理需要继承超类<code>SyncUserProcessor</code>，选用异步处理的时候需要继承超类<code>AsyncUserProcessor</code>，作为参数的所有实体类必须实现<code>Serializable</code>接口（如果有嵌套对象，每个嵌套对象所在类也必须实现<code>Serializable</code>接口），否则会出现序列化相关的异常。最后编写客户端和服务端的代码：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Slf4j</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BlotApp</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> PORT = <span class="hljs-number">8081</span>;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String ADDRESS = <span class="hljs-string">"127.0.0.1:"</span> + PORT;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
        RequestMessageProcessor processor = <span class="hljs-keyword">new</span> RequestMessageProcessor();
        RpcServer server = <span class="hljs-keyword">new</span> RpcServer(<span class="hljs-number">8081</span>, <span class="hljs-keyword">true</span>);
        server.startup();
        server.registerUserProcessor(processor);
        RpcClient client = <span class="hljs-keyword">new</span> RpcClient();
        client.startup();
        RequestMessage request = <span class="hljs-keyword">new</span> RequestMessage();
        request.setId(<span class="hljs-number">99L</span>);
        request.setContent(<span class="hljs-string">"hello bolt"</span>);
        ResponseMessage response = (ResponseMessage) client.invokeSync(ADDRESS, request, <span class="hljs-number">2000</span>);
        log.info(<span class="hljs-string">"响应结果:&#123;&#125;"</span>, response);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行输出结果：</p>
<pre><code class="hljs language-shell copyable" lang="shell">响应结果:ResponseMessage(id=99, content=hello bolt, status=10087)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">基于SOFA-BOLT协议编写简单CURD项目</h2>
<p>本地测试<code>MySQL</code>服务构建客户表如下：</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">CREATE</span> DATABASE test;

USE test;

<span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> t_customer
(
    id            <span class="hljs-type">BIGINT</span> UNSIGNED <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">NULL</span> AUTO_INCREMENT <span class="hljs-keyword">PRIMARY</span> KEY,
    customer_name <span class="hljs-type">VARCHAR</span>(<span class="hljs-number">32</span>)     <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">NULL</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了简化<code>JDBC</code>操作，引入<code>spring-boot-starter-jdbc</code>（这里只借用<code>JdbcTemplate</code>的轻度封装）相关依赖：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>mysql<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>mysql-connector-java<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>8.0.20<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.boot<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-boot-starter-jdbc<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>2.3.0.RELEASE<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写核心同步处理器：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 创建</span>
<span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CreateCustomerReq</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Serializable</span> </span>&#123;

    <span class="hljs-keyword">private</span> String customerName;
&#125;

<span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CreateCustomerResp</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Serializable</span> </span>&#123;

    <span class="hljs-keyword">private</span> Long code;

    <span class="hljs-keyword">private</span> Long customerId;
&#125;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CreateCustomerProcessor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SyncUserProcessor</span><<span class="hljs-title">CreateCustomerReq</span>> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> JdbcTemplate jdbcTemplate;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">CreateCustomerProcessor</span><span class="hljs-params">(JdbcTemplate jdbcTemplate)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.jdbcTemplate = jdbcTemplate;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Object <span class="hljs-title">handleRequest</span><span class="hljs-params">(BizContext bizContext, CreateCustomerReq req)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
        KeyHolder keyHolder = <span class="hljs-keyword">new</span> GeneratedKeyHolder();
        jdbcTemplate.update(connection -> &#123;
            PreparedStatement ps = connection.prepareStatement(<span class="hljs-string">"insert into t_customer(customer_name) VALUES (?)"</span>,
                    Statement.RETURN_GENERATED_KEYS);
            ps.setString(<span class="hljs-number">1</span>, req.getCustomerName());
            <span class="hljs-keyword">return</span> ps;
        &#125;, keyHolder);
        CreateCustomerResp resp = <span class="hljs-keyword">new</span> CreateCustomerResp();
        resp.setCustomerId(Objects.requireNonNull(keyHolder.getKey()).longValue());
        resp.setCode(RespCode.SUCCESS);
        <span class="hljs-keyword">return</span> resp;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">interest</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> CreateCustomerReq.class.getName();
    &#125;
&#125;

<span class="hljs-comment">// 更新</span>
<span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UpdateCustomerReq</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Serializable</span> </span>&#123;

    <span class="hljs-keyword">private</span> Long customerId;

    <span class="hljs-keyword">private</span> String customerName;
&#125;


<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UpdateCustomerProcessor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SyncUserProcessor</span><<span class="hljs-title">UpdateCustomerReq</span>> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> JdbcTemplate jdbcTemplate;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">UpdateCustomerProcessor</span><span class="hljs-params">(JdbcTemplate jdbcTemplate)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.jdbcTemplate = jdbcTemplate;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Object <span class="hljs-title">handleRequest</span><span class="hljs-params">(BizContext bizContext, UpdateCustomerReq req)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
        UpdateCustomerResp resp = <span class="hljs-keyword">new</span> UpdateCustomerResp();
        <span class="hljs-keyword">int</span> updateCount = jdbcTemplate.update(<span class="hljs-string">"UPDATE t_customer SET customer_name = ? WHERE id = ?"</span>, ps -> &#123;
            ps.setString(<span class="hljs-number">1</span>, req.getCustomerName());
            ps.setLong(<span class="hljs-number">2</span>, req.getCustomerId());
        &#125;);
        <span class="hljs-keyword">if</span> (updateCount > <span class="hljs-number">0</span>) &#123;
            resp.setCode(RespCode.SUCCESS);
        &#125;
        <span class="hljs-keyword">return</span> resp;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">interest</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> UpdateCustomerReq.class.getName();
    &#125;
&#125;

<span class="hljs-comment">// 删除</span>
<span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DeleteCustomerReq</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Serializable</span> </span>&#123;

    <span class="hljs-keyword">private</span> Long customerId;
&#125;

<span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DeleteCustomerResp</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Serializable</span> </span>&#123;

    <span class="hljs-keyword">private</span> Long code;
&#125;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DeleteCustomerProcessor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SyncUserProcessor</span><<span class="hljs-title">DeleteCustomerReq</span>> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> JdbcTemplate jdbcTemplate;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">DeleteCustomerProcessor</span><span class="hljs-params">(JdbcTemplate jdbcTemplate)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.jdbcTemplate = jdbcTemplate;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Object <span class="hljs-title">handleRequest</span><span class="hljs-params">(BizContext bizContext, DeleteCustomerReq req)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
        DeleteCustomerResp resp = <span class="hljs-keyword">new</span> DeleteCustomerResp();
        <span class="hljs-keyword">int</span> updateCount = jdbcTemplate.update(<span class="hljs-string">"DELETE FROM t_customer WHERE id = ?"</span>, ps -> ps.setLong(<span class="hljs-number">1</span>,req.getCustomerId()));
        <span class="hljs-keyword">if</span> (updateCount > <span class="hljs-number">0</span>)&#123;
            resp.setCode(RespCode.SUCCESS);
        &#125;
        <span class="hljs-keyword">return</span> resp;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">interest</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> DeleteCustomerReq.class.getName();
    &#125;
&#125;

<span class="hljs-comment">// 查询</span>
<span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SelectCustomerReq</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Serializable</span> </span>&#123;

    <span class="hljs-keyword">private</span> Long customerId;
&#125;

<span class="hljs-meta">@Data</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SelectCustomerResp</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Serializable</span> </span>&#123;

    <span class="hljs-keyword">private</span> Long code;

    <span class="hljs-keyword">private</span> Long customerId;

    <span class="hljs-keyword">private</span> String customerName;
&#125;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SelectCustomerProcessor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SyncUserProcessor</span><<span class="hljs-title">SelectCustomerReq</span>> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> JdbcTemplate jdbcTemplate;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">SelectCustomerProcessor</span><span class="hljs-params">(JdbcTemplate jdbcTemplate)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.jdbcTemplate = jdbcTemplate;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Object <span class="hljs-title">handleRequest</span><span class="hljs-params">(BizContext bizContext, SelectCustomerReq req)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
        SelectCustomerResp resp = <span class="hljs-keyword">new</span> SelectCustomerResp();
        Customer result = jdbcTemplate.query(<span class="hljs-string">"SELECT * FROM t_customer WHERE id = ?"</span>, ps -> ps.setLong(<span class="hljs-number">1</span>, req.getCustomerId()), rs -> &#123;
            Customer customer = <span class="hljs-keyword">null</span>;
            <span class="hljs-keyword">if</span> (rs.next()) &#123;
                customer = <span class="hljs-keyword">new</span> Customer();
                customer.setId(rs.getLong(<span class="hljs-string">"id"</span>));
                customer.setCustomerName(rs.getString(<span class="hljs-string">"customer_name"</span>));
            &#125;
            <span class="hljs-keyword">return</span> customer;
        &#125;);
        <span class="hljs-keyword">if</span> (Objects.nonNull(result)) &#123;
            resp.setCustomerId(result.getId());
            resp.setCustomerName(result.getCustomerName());
            resp.setCode(RespCode.SUCCESS);
        &#125;
        <span class="hljs-keyword">return</span> resp;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">interest</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> SelectCustomerReq.class.getName();
    &#125;

    <span class="hljs-meta">@Data</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Customer</span> </span>&#123;

        <span class="hljs-keyword">private</span> Long id;
        <span class="hljs-keyword">private</span> String customerName;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写数据源、客户端和服务端代码：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CurdApp</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> PORT = <span class="hljs-number">8081</span>;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String ADDRESS = <span class="hljs-string">"127.0.0.1:"</span> + PORT;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
        HikariConfig config = <span class="hljs-keyword">new</span> HikariConfig();
        config.setJdbcUrl(<span class="hljs-string">"jdbc:mysql://localhost:3306/test?useSSL=false&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai"</span>);
        config.setDriverClassName(Driver.class.getName());
        config.setUsername(<span class="hljs-string">"root"</span>);
        config.setPassword(<span class="hljs-string">"root"</span>);
        HikariDataSource dataSource = <span class="hljs-keyword">new</span> HikariDataSource(config);
        JdbcTemplate jdbcTemplate = <span class="hljs-keyword">new</span> JdbcTemplate(dataSource);
        CreateCustomerProcessor createCustomerProcessor = <span class="hljs-keyword">new</span> CreateCustomerProcessor(jdbcTemplate);
        UpdateCustomerProcessor updateCustomerProcessor = <span class="hljs-keyword">new</span> UpdateCustomerProcessor(jdbcTemplate);
        DeleteCustomerProcessor deleteCustomerProcessor = <span class="hljs-keyword">new</span> DeleteCustomerProcessor(jdbcTemplate);
        SelectCustomerProcessor selectCustomerProcessor = <span class="hljs-keyword">new</span> SelectCustomerProcessor(jdbcTemplate);
        RpcServer server = <span class="hljs-keyword">new</span> RpcServer(PORT, <span class="hljs-keyword">true</span>);
        server.registerUserProcessor(createCustomerProcessor);
        server.registerUserProcessor(updateCustomerProcessor);
        server.registerUserProcessor(deleteCustomerProcessor);
        server.registerUserProcessor(selectCustomerProcessor);
        server.startup();
        RpcClient client = <span class="hljs-keyword">new</span> RpcClient();
        client.startup();
        CreateCustomerReq createCustomerReq = <span class="hljs-keyword">new</span> CreateCustomerReq();
        createCustomerReq.setCustomerName(<span class="hljs-string">"throwable.club"</span>);
        CreateCustomerResp createCustomerResp = (CreateCustomerResp)
                client.invokeSync(ADDRESS, createCustomerReq, <span class="hljs-number">5000</span>);
        System.out.println(<span class="hljs-string">"创建用户[throwable.club]结果:"</span> + createCustomerResp);
        SelectCustomerReq selectCustomerReq = <span class="hljs-keyword">new</span> SelectCustomerReq();
        selectCustomerReq.setCustomerId(createCustomerResp.getCustomerId());
        SelectCustomerResp selectCustomerResp = (SelectCustomerResp)
                client.invokeSync(ADDRESS, selectCustomerReq, <span class="hljs-number">5000</span>);
        System.out.println(String.format(<span class="hljs-string">"查询用户[id=%d]结果:%s"</span>, selectCustomerReq.getCustomerId(),
                selectCustomerResp));
        UpdateCustomerReq updateCustomerReq = <span class="hljs-keyword">new</span> UpdateCustomerReq();
        updateCustomerReq.setCustomerId(selectCustomerReq.getCustomerId());
        updateCustomerReq.setCustomerName(<span class="hljs-string">"throwx.cn"</span>);
        UpdateCustomerResp updateCustomerResp = (UpdateCustomerResp)
                client.invokeSync(ADDRESS, updateCustomerReq, <span class="hljs-number">5000</span>);
        System.out.println(String.format(<span class="hljs-string">"更新用户[id=%d]结果:%s"</span>, updateCustomerReq.getCustomerId(),
                updateCustomerResp));
        selectCustomerReq.setCustomerId(updateCustomerReq.getCustomerId());
        selectCustomerResp = (SelectCustomerResp)
                client.invokeSync(ADDRESS, selectCustomerReq, <span class="hljs-number">5000</span>);
        System.out.println(String.format(<span class="hljs-string">"查询更新后的用户[id=%d]结果:%s"</span>, selectCustomerReq.getCustomerId(),
                selectCustomerResp));
        DeleteCustomerReq deleteCustomerReq = <span class="hljs-keyword">new</span> DeleteCustomerReq();
        deleteCustomerReq.setCustomerId(selectCustomerResp.getCustomerId());
        DeleteCustomerResp deleteCustomerResp = (DeleteCustomerResp)
                client.invokeSync(ADDRESS, deleteCustomerReq, <span class="hljs-number">5000</span>);
        System.out.println(String.format(<span class="hljs-string">"删除用户[id=%d]结果:%s"</span>, deleteCustomerReq.getCustomerId(),
                deleteCustomerResp));
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果如下：</p>
<pre><code class="hljs language-shell copyable" lang="shell">创建用户[throwable.club]结果:CreateCustomerResp(code=0, customerId=1)
查询用户[id=1]结果:SelectCustomerResp(code=0, customerId=1, customerName=throwable.club)
更新用户[id=1]结果:UpdateCustomerResp(code=0)
查询更新后的用户[id=1]结果:SelectCustomerResp(code=0, customerId=1, customerName=throwx.cn)
更新用户[id=1]结果:DeleteCustomerResp(code=0)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>确认最后删除操作结束后验证数据库表，确认<code>t_customer</code>表为空。</p>
<h2 data-id="heading-8">基于GO语言编写SOFA-BOLT协议客户端</h2>
<p>这里尝试使用<code>GO</code>语言编写一个<code>SOFA-BOLT</code>协议客户端，考虑到实现一个完整版本会比较复杂，这里简化为只实现<code>Encode</code>和命令调用部分，暂时不处理响应和<code>Decode</code>。编写结构体<code>RequestCommand</code>如下：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-comment">// RequestCommand sofa-bolt v2 req cmd</span>
<span class="hljs-keyword">type</span> RequestCommand <span class="hljs-keyword">struct</span> &#123;
ProtocolCode    <span class="hljs-keyword">uint8</span>
ProtocolVersion <span class="hljs-keyword">uint8</span>
Type            <span class="hljs-keyword">uint8</span>
CommandCode     <span class="hljs-keyword">uint16</span>
CommandVersion  <span class="hljs-keyword">uint8</span>
RequestId       <span class="hljs-keyword">uint32</span>
Codec           <span class="hljs-keyword">uint8</span>
Switch          <span class="hljs-keyword">uint8</span>
Timeout         <span class="hljs-keyword">uint32</span>
ClassLength     <span class="hljs-keyword">uint16</span>
HeaderLength    <span class="hljs-keyword">uint16</span>
ContentLength   <span class="hljs-keyword">uint32</span>
ClassName       []<span class="hljs-keyword">byte</span>
Header          []<span class="hljs-keyword">byte</span>
Content         []<span class="hljs-keyword">byte</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里注意一点，所有的整数类型必须使用具体的类型，例如<code>uint</code>必须用<code>uint32</code>，否则会出现<code>Buffer</code>写入异常的问题。接着编写一个编码方法：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-comment">// encode req => slice</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">encode</span><span class="hljs-params">(cmd *RequestCommand)</span> []<span class="hljs-title">byte</span></span> &#123;
container := <span class="hljs-built_in">make</span>([]<span class="hljs-keyword">byte</span>, <span class="hljs-number">0</span>)
buf := bytes.NewBuffer(container)
buf.WriteByte(cmd.ProtocolCode)
buf.WriteByte(cmd.ProtocolVersion)
buf.WriteByte(cmd.Type)
binary.Write(buf, binary.BigEndian, cmd.CommandCode)
buf.WriteByte(cmd.CommandVersion)
binary.Write(buf, binary.BigEndian, cmd.RequestId)
buf.WriteByte(cmd.Codec)
buf.WriteByte(cmd.Switch)
binary.Write(buf, binary.BigEndian, cmd.Timeout)
binary.Write(buf, binary.BigEndian, cmd.ClassLength)
binary.Write(buf, binary.BigEndian, cmd.HeaderLength)
binary.Write(buf, binary.BigEndian, cmd.ContentLength)
buf.Write(cmd.ClassName)
buf.Write(cmd.Header)
buf.Write(cmd.Content)
<span class="hljs-keyword">return</span> buf.Bytes()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后编写<code>TCP</code>客户端：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">type</span> Req <span class="hljs-keyword">struct</span> &#123;
Id   <span class="hljs-keyword">int64</span>  <span class="hljs-string">`json:"id"`</span>
Name <span class="hljs-keyword">string</span> <span class="hljs-string">`json:"name"`</span>
&#125;

<span class="hljs-keyword">package</span> main

<span class="hljs-keyword">import</span> (
<span class="hljs-string">"bytes"</span>
<span class="hljs-string">"encoding/binary"</span>
<span class="hljs-string">"encoding/json"</span>
<span class="hljs-string">"fmt"</span>
<span class="hljs-string">"net"</span>
)

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
con, err := net.Dial(<span class="hljs-string">"tcp"</span>, <span class="hljs-string">"127.0.0.1:9999"</span>)
<span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> &#123;
fmt.Println(<span class="hljs-string">"err:"</span>, err)
<span class="hljs-keyword">return</span>
&#125;
<span class="hljs-keyword">defer</span> con.Close()
req := &Req&#123;
Id:   <span class="hljs-number">8080</span>,
Name: <span class="hljs-string">"throwx.cn"</span>,
&#125;
content, err := json.Marshal(req)
<span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> &#123;
fmt.Println(<span class="hljs-string">"err:"</span>, err)
<span class="hljs-keyword">return</span>
&#125;
<span class="hljs-keyword">var</span> header []<span class="hljs-keyword">byte</span>
className := []<span class="hljs-keyword">byte</span>(<span class="hljs-string">"com.alipay.remoting.Req"</span>)
cmd := &RequestCommand&#123;
ProtocolCode:    <span class="hljs-number">2</span>,
ProtocolVersion: <span class="hljs-number">2</span>,
Type:            <span class="hljs-number">1</span>,
CommandCode:     <span class="hljs-number">1</span>,
CommandVersion:  <span class="hljs-number">1</span>,
RequestId:       <span class="hljs-number">10087</span>,
Codec:           <span class="hljs-number">1</span>,
Switch:          <span class="hljs-number">0</span>,
Timeout:         <span class="hljs-number">5000</span>,
ClassLength:     <span class="hljs-keyword">uint16</span>(<span class="hljs-built_in">len</span>(className)),
HeaderLength:    <span class="hljs-number">0</span>,
ContentLength:   <span class="hljs-keyword">uint32</span>(<span class="hljs-built_in">len</span>(content)),
ClassName:       className,
Header:          header,
Content:         content,
&#125;
pkg := encode(cmd)
_, err = con.Write(pkg)
<span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> &#123;
fmt.Println(<span class="hljs-string">"err:"</span>, err)
<span class="hljs-keyword">return</span>
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>协议的V2版本Crc32属性是可选的，这里为了简化处理也暂时忽略了</p>
</blockquote>
<p>这里看到<code>Content</code>属性为了简化处理使用了<code>JSON</code>做序列化，因此需要稍微改动<code>SOFA-BOLT</code>的源码，引入<code>FastJson</code>和<code>FastJsonSerializer</code>，改动见下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bb03a1f7b18494f83c412de46f2da2b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>先启动<code>BoltApp</code>（<code>SOFA-BOLT</code>服务端），再执行<code>GO</code>编写的客户端，结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56f6c6e3065640aba982bba9e8fcb645~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">小结</h2>
<p><code>SOFA-BOLT</code>是一个高性能成熟可扩展的<code>Netty</code>私有协议封装，比起原生<code>Netty</code>编程，提供了便捷的同步、异步调用，提供基础心跳支持和重连等特性。引入<code>SyncUserProcessor</code>和<code>AsyncUserProcessor</code>的功能，对于业务开发更加友好。<code>SOFA-BOLT</code>协议本质也是一个紧凑、高性能的<code>RPC</code>协议。在考虑引入<code>Netty</code>进行底层通讯的场景，可以优先考虑使用<code>SOFA-BOLT</code>或者考虑把<code>SOFA-BOLT</code>作为候选方案之一，只因<code>SOFA-BOLT</code>是轻量级的，学习曲线平缓，基本没有其他中间件依赖。</p>
<p><code>Demo</code>所在仓库：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzjcscut%2Fframework-mesh%2Ftree%2Fmaster%2Fsofa-bolt-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zjcscut/framework-mesh/tree/master/sofa-bolt-demo" ref="nofollow noopener noreferrer">framework-mesh/sofa-bolt-demo</a></li>
</ul>
<p>（本文完 c-5-d e-a-20210806）</p></div>  
</div>
            
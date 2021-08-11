
---
title: 'uniapp集成设备终端PDA激光扫描功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b28fa78048794488b5b847d83c186dfc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 05:30:12 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b28fa78048794488b5b847d83c186dfc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>uniapp实现pda的具体原理是在设备端需要<strong>开启广播模式</strong>，uniapp端通过调用方法来获取设备端扫描到的数据，从而在APP端对扫描的结果进行控制</p>
</blockquote>
<h4 data-id="heading-0">一、设置终端设备的扫描设置</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b28fa78048794488b5b847d83c186dfc~tplv-k3u1fbpfcp-watermark.image" alt="dbd7cc2e3ff6b7ed2ce0a1e1333f394.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>设置扫描的输出模式为<code>广播输出</code>; 我的终端是在<code>扩展设置->扫描设置->输出模式</code>中</li>
<li>查看<strong>广播输出的配置</strong>信息
<ul>
<li>我的广播输出action是<code>nlscan.action.SCANNER_RESULT</code></li>
<li>extra是 <code>SCAN_BARCODE1</code></li>
</ul>
</li>
</ul>
<p><strong>PS: 需要记录广播输出配置的<code>action</code> 和 <code>extra</code>信息，在uniapp中需要对这两个参数哦</strong></p>
<p>用到<code>action</code> 和 <code>extra</code>的关键代码如下</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-comment">// 其中的'nlscan.action.SCANNER_RESULT'是需要和你设备中广播的action一致</span>
   <span class="hljs-built_in">this</span>.intentFilter.addAction(<span class="hljs-string">'nlscan.action.SCANNER_RESULT'</span>)
   
   <span class="hljs-comment">// 其中的 'SCAN_BARCODE1'和action一样的方式，需要和广播中配置的Extra一致</span>
   <span class="hljs-keyword">let</span> content = intent.getStringExtra(<span class="hljs-string">'SCAN_BARCODE1'</span>); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整代码参考 自定义组件"pda-scan" 的<code>initScan</code>方法</p>
<h4 data-id="heading-1">一、创建自定义组件<code>pda-scan</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">view</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">activity</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-attr">receiver</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-attr">intentFilter</span>: <span class="hljs-literal">null</span>
        &#125;
    &#125;,
    <span class="hljs-attr">created</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">option</span>) </span>&#123;
        <span class="hljs-built_in">this</span>.initScan()
        <span class="hljs-built_in">this</span>.startScan();
    &#125;,
    <span class="hljs-attr">onHide</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.stopScan();
    &#125;,
    <span class="hljs-attr">destroyed</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">//页面退出时一定要卸载监听,否则下次进来时会重复，造成扫一次出2个以上的结果/</span>
        <span class="hljs-built_in">this</span>.stopScan();
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">initScan</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>;
            <span class="hljs-built_in">this</span>.activity = plus.android.runtimeMainActivity(); <span class="hljs-comment">//获取activity</span>
            <span class="hljs-keyword">var</span> IntentFilter = plus.android.importClass(<span class="hljs-string">'android.content.IntentFilter'</span>);
            <span class="hljs-built_in">this</span>.intentFilter = <span class="hljs-keyword">new</span> IntentFilter();
            <span class="hljs-comment">// 其中的'nlscan.action.SCANNER_RESULT'是需要和你设备中广播的action一致</span>
            <span class="hljs-built_in">this</span>.intentFilter.addAction(<span class="hljs-string">'nlscan.action.SCANNER_RESULT'</span>)
            <span class="hljs-built_in">this</span>.receiver = plus.android.implements(<span class="hljs-string">'io.dcloud.feature.internal.reflect.BroadcastReceiver'</span>, &#123;
                <span class="hljs-attr">onReceive</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">context, intent</span>) </span>&#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"intent"</span>,intent)
                    plus.android.importClass(intent);
                    <span class="hljs-comment">// 其中的 'SCAN_BARCODE1'和action一样的方式，需要和广播中配置的Extra一致</span>
                    <span class="hljs-keyword">let</span> content = intent.getStringExtra(<span class="hljs-string">'SCAN_BARCODE1'</span>); 
                    uni.$emit(<span class="hljs-string">'scancodedate'</span>, content)
                &#125;
            &#125;);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">startScan</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.activity.registerReceiver(<span class="hljs-built_in">this</span>.receiver, <span class="hljs-built_in">this</span>.intentFilter);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">stopScan</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.activity.unregisterReceiver(<span class="hljs-built_in">this</span>.receiver);
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">二、引入自定义组件<code>pda-scan</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span>></span>你的页面内容<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in content"</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">pda-scan</span>></span><span class="hljs-tag"></<span class="hljs-name">pda-scan</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">view</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> scanCode <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/scan-code/scan-code.vue'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">components</span>: &#123; scanCode &#125;,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">content</span>: []
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">onLoad</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">var</span> _this = <span class="hljs-built_in">this</span>
        uni.$on(<span class="hljs-string">'scancodedate'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">content</span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"扫描到的内容为:"</span>, content)
            _this.content.push(content)
        &#125;)
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三个步骤完成后，只需要启动项目，打开存在app后，直接使用设备终端的扫描功能即可得到响应。</p>
<p>需要注意的是你打开的页面是要存在<code><scan-code></scan-code></code>标签的页面哦</p></div>  
</div>
            
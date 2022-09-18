
---
title: '《雨夜》 RocketMQ源码系列(一) NameServer 核心源码解析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44ededadf66845198e34fb1f4386e5b3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Wed, 14 Sep 2022 19:50:05 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44ededadf66845198e34fb1f4386e5b3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第n篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<h1 data-id="heading-0">序</h1>
<h2 data-id="heading-1">带着问题 往下看 （namesrv）</h2>
<ol>
<li>我们在写组件的时候 怎么管理version</li>
<li>如果现在让你 维护一个 各个jar包公用的属性</li>
<li>System.exit(-1); 0 -1 -2 各种数都是干什么的，什么时候 用哪个</li>
<li>环境变量如果不想使用 ROCKETMQ_HOME, 想变为 xxx 这怎么做，能做么？</li>
<li>我们启动broker 老是用 -n ip:9876  9876是什么，我们可以改变么？怎么改</li>
<li>大家如果想 把命令启动带着的 -c -p等参数放到 我们的属性中，怎么写代码？</li>
<li>如果我们想 自己设置使用的log 组件,怎么办</li>
<li>遍历 Field[] 的时候 想跳过 static的属性 怎么写代码？</li>
<li>多个对象的 属性需要进行聚合到一个对象中，要是你 怎么写</li>
<li>KVConfigManager 有什么作用，怎么保证的 并发操作的数据正确性？你感觉有什么问题么？</li>
<li>KVConfigManager 怎么保证的 持久化？</li>
<li>怎么在 并发操作的时候 保证数据的安全性？</li>
<li>方法的参数 使用final 有什么用？</li>
<li>怎么判断的broker 是不是master</li>
<li>netty 怎么让nameserver 通知broker 信息的。</li>
<li>nameserver 是否存活的判断标准是什么？ 能修改么？ 怎么修改</li>
<li>Runtime.getRuntime().addShutdownHook 有什么用，没有不行么？</li>
<li>@ImportantField 干什么的？ 什么时候 使用</li>
<li>在同一台计算机上部署多个代理时 想区分日志路径 用哪个参数，调成什么？</li>
<li>broker 为什么 -p 和 -m 同时有的时候 -m的总是不生效呢？</li>
</ol>
<h1 data-id="heading-2">请思考下 写写你的答案 再往下看</h1>
<h1 data-id="heading-3">nameserver 启动的逻辑</h1>
<h2 data-id="heading-4">nameserver 功能</h2>
<ol>
<li>管理broker 集群</li>
<li>属于注册中心 业务端 和nameserver 进行连接，获取broker地址</li>
<li>负责维护broker 连接/心跳/监控</li>
</ol>
<h1 data-id="heading-5">nameserver 问题解答</h1>
<h2 data-id="heading-6">我们在写组件的时候 怎么管理version</h2>
<p>一方面是 在父类的 pom.xml 通过  进行 控制版本，然后 业务端通过</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">dependencyManagement</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dependencies</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.xxx<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>xxx<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">version</span>></span>4.0.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">type</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">type</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>import<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">dependencies</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependencyManagement</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是第一个 ，第二个 是 rocketmq 这种 在common 包下面 新建一个 MQVersion 管理版本</p>
<p>这里会有一个问题，那这个版本管理 我用在哪里啊，不用不行么？</p>
<ol>
<li>为了方便测试，测试的时候 可能因为版本有差异 导致的问题。指定version 就没有这个问题了
2 broker 操作也是，（其实一句话 <strong>为了之后的版本兼容</strong>）比如</li>
</ol>
<pre><code class="hljs language-scss copyable" lang="scss">    
if (version < MQVersion.Version.V3_0_7_SNAPSHOT.ordinal()) &#123;
    result<span class="hljs-selector-class">.setCode</span>(ResponseCode.SYSTEM_ERROR);
    result<span class="hljs-selector-class">.setRemark</span>("the client does not support this feature. version="
        + MQVersion.getVersionDesc(version));
    log<span class="hljs-selector-class">.warn</span>("[get-consumer-status] the client does not support this feature. channel=&#123;&#125;, version=&#123;&#125;",
        RemotingHelper.parseChannelRemoteAddr(entry.getKey()), MQVersion<span class="hljs-selector-class">.getVersionDesc</span>(version));
    return result;
&#125; else if (UtilAll.isBlank(originClientId) || originClientId<span class="hljs-selector-class">.equals</span>(clientId)) &#123;
                                                          
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">如果现在让你 维护一个 各个jar包公用的属性</h2>
<p>1 在common包搞一个 公共的实体类 随时用随时取呗，大不了就一个map 然后就put get</p>
<p>2  System.setProperty  底层就是全局 map 进行put get</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">extends</span> <span class="hljs-title class_">Hashtable</span><<span class="hljs-title class_">Object</span>,<span class="hljs-title class_">Object</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">环境变量如果不想使用 ROCKETMQ_HOME, 想变为 xxx 这怎么做，能做么？</h2>
<p>设置 rocketmq.home.dir=xxx</p>
<h2 data-id="heading-9">我们启动broker 老是用 -n ip:9876  9876是什么，我们可以改变么？怎么改</h2>
<pre><code class="hljs language-ini copyable" lang="ini">nettyServerConfig.setListenPort(9876)<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码指定 的netty 监听端口，一般情况不改</p>
<h2 data-id="heading-10">大家如果想 把命令启动带着的 -c -p等参数放到 我们的属性中，怎么写代码？</h2>
<pre><code class="hljs language-ini copyable" lang="ini">MixAll.properties2Object(ServerUtil.commandLine2Properties(commandLine), namesrvConfig)<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是先把commandLine 转变为 Properties 对象，然后调用 namesrvConfig 反射方法 赋值</p>
<h2 data-id="heading-11">如果我们想 自己设置使用的log 组件,怎么办</h2>
<pre><code class="hljs language-ini copyable" lang="ini">LoggerContext <span class="hljs-attr">lc</span> = (LoggerContext) LoggerFactory.getILoggerFactory()<span class="hljs-comment">;</span>
JoranConfigurator <span class="hljs-attr">configurator</span> = new JoranConfigurator()<span class="hljs-comment">;</span>
configurator.setContext(lc)<span class="hljs-comment">;</span>
lc.reset()<span class="hljs-comment">;</span>
configurator.doConfigure(namesrvConfig.getRocketmqHome() + "/conf/logback_namesrv.xml")<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">遍历 Field[] 的时候 想跳过 static的属性 怎么写代码？</h2>
<pre><code class="hljs language-arduino copyable" lang="arduino"> (field.<span class="hljs-built_in">getModifiers</span>() & <span class="hljs-number">0x00000008</span>) != <span class="hljs-number">0</span> 如果为<span class="hljs-literal">true</span> 就是 <span class="hljs-type">static</span> <span class="hljs-literal">false</span>为 非<span class="hljs-type">static</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">多个对象的 属性需要进行聚合到一个对象中，要是你 怎么写</h2>
<pre><code class="hljs language-vbnet copyable" lang="vbnet"><span class="hljs-keyword">for</span> (Entry<<span class="hljs-type">Object</span>, <span class="hljs-type">Object</span>> <span class="hljs-keyword">next</span> : <span class="hljs-keyword">from</span>.entrySet()) &#123;
    <span class="hljs-type">Object</span> fromObj = <span class="hljs-keyword">next</span>.getValue(), toObj = <span class="hljs-keyword">to</span>.<span class="hljs-keyword">get</span>(<span class="hljs-keyword">next</span>.getKey());
    <span class="hljs-keyword">if</span> (toObj != null && !toObj.<span class="hljs-keyword">equals</span>(fromObj)) &#123;
        log.info(<span class="hljs-string">"Replace, key: &#123;&#125;, value: &#123;&#125; -> &#123;&#125;"</span>, <span class="hljs-keyword">next</span>.getKey(), toObj, fromObj);
    &#125;
    <span class="hljs-keyword">to</span>.put(<span class="hljs-keyword">next</span>.getKey(), fromObj);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 可能同时操作这个对象 导致 数据不一致 ，所以要加上 读写锁的 写锁</p>
<h2 data-id="heading-14">KVConfigManager 有什么作用，怎么保证的 并发操作的数据正确性？你感觉有什么问题么？</h2>
<p>是 kv 配置的管理器，主要是</p>
<pre><code class="hljs language-arduino copyable" lang="arduino">HashMap<<span class="hljs-type">String</span><span class="hljs-comment">/* Namespace */</span>, HashMap<<span class="hljs-type">String</span><span class="hljs-comment">/* Key */</span>, <span class="hljs-type">String</span><span class="hljs-comment">/* Value */</span>>> configTable
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以后写map 也要像这种方式 写注释。</p>
<pre><code class="hljs language-arduino copyable" lang="arduino"><span class="hljs-comment">//读取的是 ./namesrv/kvConfig.json</span>
kvConfigPath = System.<span class="hljs-built_in">getProperty</span>(<span class="hljs-string">"user.home"</span>) + <span class="hljs-built_in">File</span>.separator + <span class="hljs-string">"namesrv"</span> + <span class="hljs-built_in">File</span>.separator + <span class="hljs-string">"kvConfig.json"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>行吧 ，现在还不知道 这些kv的作用，先看看怎么存储的，到用的时候 我们接上，先知道 kv 存储在KVConfigManager类  configTable 属性中</p>
<p>putKVConfig 使用的 ReentrantReadWriteLock 的写锁 保证数据一致性，如果map的key 存在了，不会进行覆盖，而是 跳过。</p>
<h2 data-id="heading-15">KVConfigManager 怎么保证的 持久化？</h2>
<p>执行过 上面的 那些方法，执行 persist ，加读锁，如下图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44ededadf66845198e34fb1f4386e5b3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">怎么在 并发操作的时候 保证数据的安全性？</h2>
<p>一方面 是 <strong>不可变类</strong>，其中返回属性的时候 要进行copy 简单来说 就是我通过get 方法出去的 对象 是 copy的对象，而不是 原来的对象，防止 外面通过引用 修改 属性值，把我们的对象 属性 进行修改。</p>
<h2 data-id="heading-17">方法的参数 使用final 有什么用？</h2>
<ol>
<li>确保，不会也不能对于参数进行修改，保证了调用发起方数据的安全；</li>
<li>避免在方法体中修改参数，引起不必要的错误</li>
<li>程序员工作不是一个人的工作，你设置为final，别人将来维护的时候一看就知道这个变量不能修改，而不需要去记忆这个是不能变化的值，是常量。这个是代码规范。</li>
</ol>
<h2 data-id="heading-18">怎么判断的broker 是不是master</h2>
<pre><code class="hljs language-ini copyable" lang="ini">//<span class="hljs-attr">0</span> == brokerId
<span class="hljs-attr">MixAll.MASTER_ID</span> == brokerId
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这个其实可以 抽出来一个公共的方法， 方便之后的修改</strong></p>
<h2 data-id="heading-19">netty 怎么让nameserver 通知broker 信息的。</h2>
<p>netty 保存的 channel 到时候用了 直接从map 获取 然后发送消息</p>
<h2 data-id="heading-20">nameserver 是否存活的判断标准是什么？ 能修改么？ 怎么修改</h2>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-attr">BROKER_CHANNEL_EXPIRED_TIME</span> = <span class="hljs-number">1000</span> * <span class="hljs-number">60</span> * <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>static final 写死的，如果 最后一次心跳时间 + 2分钟 都小于System.currentTimeMillis() 执行删除操作</p>
<ol>
<li>关闭 netty channel</li>
<li>brokerLiveTable 删除对应的实例</li>
</ol>
<p>这是一个定时任务 从项目 启动5s之后 ，每10s执行一次，说明 对broker的感知 会有些许 延迟。（最大也就 20s，一般10s以内感知）</p>
<h2 data-id="heading-21">Runtime.getRuntime().addShutdownHook 有什么用，没有不行么？</h2>
<p>当程序正常退出,系统调用 System.exit方法或<a href="https://link.juejin.cn/?target=https%3A%2F%2Fso.csdn.net%2Fso%2Fsearch%3Fq%3D%25E8%2599%259A%25E6%258B%259F%25E6%259C%25BA%26spm%3D1001.2101.3001.7020" target="_blank" rel="nofollow noopener noreferrer" title="https://so.csdn.net/so/search?q=%E8%99%9A%E6%8B%9F%E6%9C%BA&spm=1001.2101.3001.7020" ref="nofollow noopener noreferrer">虚拟机</a>被关闭时才会执行添加的shutdownHook线程。其中shutdownHook是一个已初始化但并不有启动的线程，当jvm关闭的时候，会执行系统中已经设置的所有通过方法addShutdownHook添加的钩子，当系统执行完这些钩子后，jvm才会关闭。所以可通过这些钩子在jvm关闭的时候进行内存清理、资源回收等工作。</p>
<h2 data-id="heading-22">@ImportantField 干什么的？ 什么时候 使用</h2>
<p>最后的true 代表 是否只打印关键属性，写@ImportantField的 就一定会打，没有这个注解的就不打印了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title class_">MixAll</span>.<span class="hljs-title function_">printObjectProperties</span>(<span class="hljs-variable language_">console</span>, brokerConfig, <span class="hljs-literal">true</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">在同一台计算机上部署多个代理时 想区分日志路径 用哪个参数，调成什么？</h2>
<p>isolateLogEnable 改为 true</p>
<pre><code class="hljs language-erlang copyable" lang="erlang"><span class="hljs-function"><span class="hljs-title">if</span> <span class="hljs-params">(brokerConfig.isIsolateLogEnable())</span> &#123;
    S<span class="hljs-title">ystem</span>.<span class="hljs-title">setProperty</span><span class="hljs-params">(<span class="hljs-string">"brokerLogDir"</span>, brokerConfig.getBrokerName() + <span class="hljs-string">"_"</span> + brokerConfig.getBrokerId())</span>;
&#125;

<span class="hljs-title">if</span> <span class="hljs-params">(brokerConfig.isIsolateLogEnable() && messageStoreConfig.isEnableDLegerCommitLog())</span> &#123;
    S<span class="hljs-title">ystem</span>.<span class="hljs-title">setProperty</span><span class="hljs-params">(<span class="hljs-string">"brokerLogDir"</span>, brokerConfig.getBrokerName() + <span class="hljs-string">"_"</span> + messageStoreConfig.getdLegerSelfId())</span>;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">broker 为什么 -p 和 -m 同时有的时候 -m的总是不生效呢？</h2>
<p>无论是 -p 还是 -m 都是print 输出，本来就是希望打印日志，然后进程停止。</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-attr">opt</span> = new Option(<span class="hljs-string">"p"</span>, <span class="hljs-string">"printConfigItem"</span>, <span class="hljs-literal">false</span>, <span class="hljs-string">"Print all config item"</span>)<span class="hljs-comment">;</span>
<span class="hljs-attr">opt</span> = new Option(<span class="hljs-string">"m"</span>, <span class="hljs-string">"printImportantConfig"</span>, <span class="hljs-literal">false</span>, <span class="hljs-string">"Print important config item"</span>)<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-25">总结</h1>
<p>这些 只是 namestr 的NamesrvController 初始化，之后 慢慢的一点点往下写，如果感觉写的还有优化的，评论下 哈</p></div>  
</div>
            
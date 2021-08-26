
---
title: '「一探究竟」Java SPI机制'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f7ae0f25b2d4f5eadf2bcb5a61f79d1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 19:18:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f7ae0f25b2d4f5eadf2bcb5a61f79d1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<br>
<h2 data-id="heading-0">事件起因</h2>
<p>七月中旬，我司的系统潜在风险排查工作在如火如荼的进行，其中我发现当前系统的调用源缺少Token信息，难以做到具体的识别和监控，因此需要对其优化。</p>
<p>针对刚提到的两个问题，我只需要实现某个框架基类，然后做一点业务处理即可，根据框架的说明文档，按步骤实现以下内容即可：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f7ae0f25b2d4f5eadf2bcb5a61f79d1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开发、调试一气呵成之后，我对这种实现方式起了好奇之心，非常疑惑它们是如何在框架中实例化并发挥作用的，有兴趣的话就跟我一起一探究竟吧（😜）</p>
<br>
<h2 data-id="heading-1">什么是SPI</h2>
<p>最初我甚至都不知道这种技术/方案是Java自身支持的，还以为是框架自身设计的骚操作，后来询问其他同事才知晓这种灵活的提供服务能力的方式被称为<strong>SPI</strong>，官方一点的解释如下：</p>
<blockquote>
<p>SPI：全称为 Service Provider Interface。是Java提供的一套用来被第三方实现或者扩展的接口，多用于<strong>框架扩展、插件开发</strong>等等。</p>
</blockquote>
<p>例如上文中提到的实现参数过滤器就属于框架扩展范畴，简单了解后我们来整一个小Demo吧。</p>
<br>
<h2 data-id="heading-2">SPI的工作方式</h2>
<p>SPI的发现能力是不需要依赖于其他类库，主要有两种实现方式：</p>
<ul>
<li>sun.misc.Service Sun公司提供的加载能力</li>
<li>java.util.ServiceLoader#load JDK自身提供的加载能力</li>
</ul>
<blockquote>
<p>因为方法二是JDK内部代码，包含源码，因此后续都默认使用该方法进行说明</p>
</blockquote>
<p>基本使用步骤：</p>
<ol>
<li>
<p>定义一个需要对外提供能力的接口</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">SPIInterface</span> </span>&#123;
    <span class="hljs-function">String <span class="hljs-title">handle</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>定义实现类，实现指定接口</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SPIInterfaceImpl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">SPIInterface</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">handle</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"当前时间为: "</span> + LocalDateTime.now();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在指定位置配置相关的实现类：<strong>resource/META-INF/services</strong></p>
<p>注意 <strong>resource</strong>为资源文件</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 文件位置（resource/META-INF/services/com.mine.spi.SPIInterface）</span>
<span class="hljs-comment"># 内容（实现类的全类名）</span>
com.mine.spi.impl.SPIInterfaceImpl
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用JDK提供的初始化能力，直接调用即可</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SpiApp</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        ServiceLoader<SPIInterface> load = ServiceLoader.load(SPIInterface.class);
        <span class="hljs-keyword">for</span> (SPIInterface ser : load) &#123;
            System.out.println(ser.handle());
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// 响应</span>
<span class="hljs-comment">// 当前时间为: 2021-08-24T03:30:52.397</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>简单到爆炸，关键还是在于JDK已经帮助我们实现了这一套发现和初始化的步骤，下面咱们来深入分析一下它的基本源码 😁</p>
<p>从方法：<code>java.util.ServiceLoader#load</code> 为入口，将当前接口Class类型及其类加载器传入至Loader变量中：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * service：接口类型
 * loader：类加载器
 * acc：安全管理器
 */</span>
<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">ServiceLoader</span><span class="hljs-params">(Class<S> svc, ClassLoader cl)</span> </span>&#123;
    service = Objects.requireNonNull(svc, <span class="hljs-string">"Service interface cannot be null"</span>);
    loader = (cl == <span class="hljs-keyword">null</span>) ? ClassLoader.getSystemClassLoader() : cl;
    acc = (System.getSecurityManager() != <span class="hljs-keyword">null</span>) ? AccessController.getContext() : <span class="hljs-keyword">null</span>;
    reload();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>变量传入之后，初始化类：<code>LazyIterator</code>，从名称就可以看出来这是一个懒加载的迭代器，只有真正使用触发时才会进行实例的初始化，核心初始化逻辑在方法：<code>java.util.ServiceLoader.LazyIterator#nextService</code>中。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> S <span class="hljs-title">nextService</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-comment">// 省略其他代码...</span>
    
    Class<?> c = <span class="hljs-keyword">null</span>;
    <span class="hljs-keyword">try</span> &#123;
        c = Class.forName(cn, <span class="hljs-keyword">false</span>, loader);
    &#125; <span class="hljs-keyword">catch</span> (ClassNotFoundException x) &#123;
        fail(service,
             <span class="hljs-string">"Provider "</span> + cn + <span class="hljs-string">" not found"</span>);
    &#125;
    
    <span class="hljs-comment">// 省略其他代码...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为拿到了接口类型及其全类名，所以通过反射构建出实例对象还是非常容易的，拿到实例化的对象后，就和普通的代码没有什么区别了。</p>
<p>下面我们再看看几个框架实际使用SPI的例子，瞻仰一下前辈们的代码 😎</p>
<br>
<h2 data-id="heading-3">SPI使用案例分析</h2>
<h3 data-id="heading-4">Log4j-Api</h3>
<p>以Log4j日志框架为例，<code>log4j-api-2.13.3.jar </code>版本就基于 <code>SPI</code>实现了 <code>PropertySource</code>接口，用以收集当前服务器相关的配置信息，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5feaff93e6d440a893f0c51442acfa48~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<p>同样的，<code>log4j-core-2.13.3.jar</code>基于 <code>SPI</code>实现了日志门面的绑定，核心代码如下所示：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * Binding for the Log4j API.
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Log4jProvider</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Provider</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Log4jProvider</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>(<span class="hljs-number">10</span>, <span class="hljs-string">"2.6.0"</span>, Log4jContextFactory.class);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">JDBC驱动</h3>
<p>以我们常用的JDBC驱动 <code>mysql-connector-java-5.1.43.jar</code>为例，它同样实现了SPI接口，驱动类分别为：<code>Driver</code>，<code>FabricMySQLDriver</code>，其底层实现是向驱动管理类注册自身，核心代码如下，它帮我们自动做了 <code>Class.forName("com.mysql.jdbc.Driver")</code>这一步加载动作。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Driver</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">NonRegisteringDriver</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">java</span>.<span class="hljs-title">sql</span>.<span class="hljs-title">Driver</span> </span>&#123;
    <span class="hljs-comment">//</span>
    <span class="hljs-comment">// Register ourselves with the DriverManager</span>
    <span class="hljs-comment">//</span>
    <span class="hljs-keyword">static</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            java.sql.DriverManager.registerDriver(<span class="hljs-keyword">new</span> Driver());
        &#125; <span class="hljs-keyword">catch</span> (SQLException E) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> RuntimeException(<span class="hljs-string">"Can't register driver!"</span>);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>FabricMySQLDriver</code>类则同理，当然了，我们也可以主动破坏这种加载的机制，比如自行实现一个MySQLDriver，来实现数据库连接，核心代码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CustomDriver</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">NonRegisteringDriver</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Driver</span> </span>&#123;

    <span class="hljs-keyword">static</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            java.sql.DriverManager.registerDriver(<span class="hljs-keyword">new</span> CustomDriver());
        &#125; <span class="hljs-keyword">catch</span> (SQLException ignored) &#123;&#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">CustomDriver</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> SQLException </span>&#123; &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Connection <span class="hljs-title">connect</span><span class="hljs-params">(String url, Properties info)</span> <span class="hljs-keyword">throws</span> SQLException </span>&#123;
        System.out.println(<span class="hljs-string">"[Kerwin] 执行数据库连接..."</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.connect(url, info);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Logger <span class="hljs-title">getParentLogger</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> SQLFeatureNotSupportedException </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后将 <code>CustomDriver</code>注入到SPI中即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b4b4152af6c4093b1d3d0d7ad674a1f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要注意的是 <code>CustomDriver</code>类需要实现继承 <code>NonRegisteringDriver</code>类，否则会被默认的Driver优先注册，完成之后使用上古的JDBC代码调用，即可模拟破坏SPI的情况，如图：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">customDriver</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> SQLException </span>&#123;
    Connection conn = DriverManager.getConnection(<span class="hljs-string">"jdbc:mysql://127.0.0.1:3306/db_file?characterEncoding=UTF-8&useSSL=false"</span>, <span class="hljs-string">"root"</span>, <span class="hljs-string">""</span>);
    Statement stmt = conn.createStatement();
    ResultSet rs = stmt.executeQuery(<span class="hljs-string">"SELECT * FROM script_dir LIMIT 1"</span>);
    <span class="hljs-keyword">while</span> (rs.next()) &#123;
        System.out.println(rs.getString(<span class="hljs-number">1</span>));
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，我们使用自定义驱动类成功获取到数据库连接，替换了原本的Driver驱动类，具体细节需要大家再Debug看看，因为涉及接口类型，拿到连接后Return等等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a5cae10eb234eaea07ab6d0e9b0be6a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>控制台输出：</p>
<pre><code class="hljs language-bash copyable" lang="bash">[Kerwin] 执行数据库连接...
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h2 data-id="heading-6">SPI的应用场景</h2>
<p>了解完它的基本使用方法和原理之后，<code>SPI</code>的神秘感顿时化为虚有，说到底就是<strong>基于约定在指定位置选择性配置接口实现类，由JDK动态初始化及执行的机制</strong>。</p>
<br>
<h3 data-id="heading-7">日常开发要不要使用SPI？</h3>
<p>我们从上文中能直接体会到<code>SPI</code>机制的好处，它可以起到策略选择、动态初始化、解耦的作用，那我们在普通项目开发中要不要使用呢？我个人是不推荐使用SPI的方式，主要原因还是我们可以使用更优雅的方式来替代<code>SPI</code>机制，比如：</p>
<ul>
<li>动态初始化、策略选择 =》我们可以使用策略+工厂模式实现策略的动态选择，配合ZK来实现动态初始化（启用/禁用）</li>
<li>解耦 =》基于良好的设计，可以很容易的实现解耦</li>
</ul>
<p>基于上述的方案，可以保证项目代码具备SPI的好处的同时更加易读，降低理解成本。</p>
<br>
<h3 data-id="heading-8">框架/组件工具开发要不要使用SPI？</h3>
<p>答案是毋庸置疑的，现在的诸多框架及工具就是使用SPI来实现的，引入了SPI机制后，服务接口与服务实现就会达成分离的状态，可以实现解耦以及可扩展机制。</p>
<p>例如<code>Sharding-jdbc</code>的加密算法接口，原生仅提供了AES和MD5两种加密方式，需要其他加密方式的项目就可以使用SPI机制将自己需要的加密方式写入框架内，然后根据需要调用即可，无论是使用还是维护都更加方便。</p>
<p>因为Java实现的SPI版本相对比较粗糙和暴力，导致它会把所有接口实现类全部实例化一遍，所以还有框架会对Java的SPI进行封装和优化，比如<code>Dubbo</code>，它将配置文件中的全类名修改为了键值对的方式，以满足按需加载的需要，同时增加了IOC及AOP的特性，自适应扩展等机制。</p>
<p>通过上文的工作方式我们就可以了解到SPI的机制并不神秘，如果个人需要简单封装的话，还是轻而易举的。</p>
<br>
<h2 data-id="heading-9">学习SPI的思想</h2>
<p>SPI机制有一定的必然性，以上文提到的<code>Sharding-jdbc</code>的加密算法为例，只有真正的使用者才知道自己到底需要什么，因此<strong>把一部分决定权（实现）交给用户的能力</strong>是必须要具备的，不然的话框架也好，工具也罢，为了满足所有的情况，代码势必都会变的非常臃肿。这其中最关键的设计原则即：</p>
<blockquote>
<p>依赖倒置原则（要针对抽象层编程，而不要针对具体类编程）</p>
</blockquote>
<p>我们在日常开发中同样要思考如何设计接口，如何依赖抽象层进行编程，减少与实现类之间的耦合，同样的，为了实现这一要求，我们必然会去学习设计模式、设计原则之类的知识，去了解各种设计模式的最佳实践，一步步的去优化代码，在此推荐一下我之前的文章：<a href="https://juejin.cn/post/6846687591425638413" target="_blank" title="https://juejin.cn/post/6846687591425638413">设计模式总篇：从为什么需要原则到实际落地（附知识图谱）</a>。</p>
<br>
<h2 data-id="heading-10">总结</h2>
<p>截止到这里，我们明白了什么是SPI及其工作的原理，熟悉了它的典型案例，也了解了它的应用场景、设计理念等等，下面是一些针对性的建议：</p>
<ol>
<li>SPI机制是框架/工具级项目必备的能力之一，立志于高级工程师的小伙伴一定要吃透它的设计理念和实现原理</li>
<li>SPI的核心思想：<strong>把一部分决定权（实现）交给用户，即依赖倒置</strong></li>
<li>了解SPI的优势和特点后，在单体项目中我们完全可以使用别的方案达到更好的效果，切忌为了使用而去用它</li>
<li>未来在开发或使用某些中间件/工具时，可以多加留意它是否提供了相关的SPI接口，可能会起到事半功倍的效果。</li>
</ol>
<br>
<p>如果觉得这篇内容对你有帮助的话：</p>
<ol>
<li>当然要点赞支持一下啦~</li>
<li>另外，可以搜索并关注公众号「<strong>是Kerwin啊</strong>」，一起在技术的路上走下去吧~ 😋</li>
</ol>
<br>
<h2 data-id="heading-11">参考文章</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fjavase%2F8%2Fdocs%2Fapi%2Fjava%2Futil%2FServiceLoader.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/javase/8/docs/api/java/util/ServiceLoader.html" ref="nofollow noopener noreferrer">ServiceLoader</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcxis.me%2F2017%2F04%2F17%2FJava%25E4%25B8%25ADSPI%25E6%259C%25BA%25E5%2588%25B6%25E6%25B7%25B1%25E5%2585%25A5%25E5%258F%258A%25E6%25BA%2590%25E7%25A0%2581%25E8%25A7%25A3%25E6%259E%2590%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cxis.me/2017/04/17/Java%E4%B8%ADSPI%E6%9C%BA%E5%88%B6%E6%B7%B1%E5%85%A5%E5%8F%8A%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90/" ref="nofollow noopener noreferrer">Java中SPI机制深入及源码解析</a></li>
</ol></div>  
</div>
            
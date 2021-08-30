
---
title: 'Mybatis(三)：架构及解析器模块详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a7ad4af038a46af97d0f0131311c152~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 08:14:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a7ad4af038a46af97d0f0131311c152~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在前面的文章中我们了解了<code>Mybatis</code>的基本使用及其执行流程。相信你已经对<code>Mybatis</code>有了简单的了解。</p>
<p>今天我们正式进去源码学习阶段，在这篇文章中，我们首先介绍下<code>Mybatis</code>的结构，之后再学习下解析器模块的内容。</p>
<p>首先自行去<code>github</code>上下载其源码，地址为：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mybatis/mybatis-3" ref="nofollow noopener noreferrer">github.com/mybatis/myb…</a></p>
<p>为方便查看，我们将下载的源码导入到<code>idea</code>中，<code>Mybaits</code>的项目结构还是比较清晰明了的，目录如下所示:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a7ad4af038a46af97d0f0131311c152~tplv-k3u1fbpfcp-watermark.image" alt="image-20210819180007905" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">1 架构</h2>
<p>通过<code>Mybatis</code>的源码我们发现，<code>Mybatis</code>将其模块分成了一个个的包，我们可以很清楚的知道其有哪些模块组成，接下来我们依次简单的介绍下这些模块：</p>
<ul>
<li><code>annotations</code> 注解 这个没什么可说的，<code>Mybatis</code>中的一些注解定义在了这个包里，例如：<code>@Select @Insert @Update...</code></li>
<li><code>io</code> 这个模块主要负责资源的加载，在上篇文章中提到的<code>Resources</code>类便是定义在这个模块下。</li>
<li><code>parsing</code> 解析器 <code>XPathParser</code>封装了对xml文件的解析。</li>
<li><code>builder</code> 配置解析模块 解析<code>Mybatis</code>配置文件及映射文件，将里面的信息封装到<code>Configuration</code>对象中。</li>
<li><code>parsing</code> 解析器 这个模块的功能是负责我们定义的配置文件及映射文件的解析。<code>XPathParser</code>。</li>
<li><code>binding</code> 这个模块是负责将<code>Mapper</code>中的方法同<code>xml</code>文件中相关的<code>SQL</code>进行关联，<code>MapperRegistry</code>、<code>MypperProxyFactory</code>、<code>MypperProxy</code>、<code>MapperMethod</code>都是定义在这个模块下。</li>
<li><code>cache</code> 缓存 使用<code>Mybatis</code>的同学应该都知道其有一级和二级缓存，这些功能便定义在这个模块中，有了缓存的存在，能够提高一些查询的性能，但如果在开发中不注意的话也会导致一些问题。</li>
<li><code>cursor</code> 游标</li>
<li><code>datasource</code> 数据源模块</li>
<li><code>executor</code> 执行器模块 负责<code>SQL</code>的执行及结果的映射。</li>
<li><code>transaction</code> 事务</li>
<li><code>logging</code> 日志模块</li>
<li><code>mapping</code> mapper对应的java类</li>
<li><code>plugin</code> 插件</li>
<li><code>reflection</code> 反射</li>
<li><code>scripting</code> 动态<code>sql</code>解析</li>
<li><code>type</code> 类型处理器</li>
<li><code>session</code> sql会话</li>
</ul>
<p><code>Mybatis</code>的架构由接口层、核心处理层、基础支持层三部分组成。各层的组成模块如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17f2c381cfbb4c82a76f2730b539cc81~tplv-k3u1fbpfcp-watermark.image" alt="image-20210819212430029" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2 解析器模块</h2>
<p>解析器模块为<code>Mybatis</code>初始化时加载配置文件和mapper映射文件解析及动态<code>SQL</code>占位符的处理提供了支持。</p>
<p><code>Mybatis</code>解析器模块的目录如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97472100d957439abd6051a636021ff3~tplv-k3u1fbpfcp-watermark.image" alt="image-20210826201954683" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">2.1 XPathParser</h3>
<p><code>XPathParser</code>是<code>Mybatis</code>中的解析器，其对<code>XPath</code>进行了封装，其属性字段如下：</p>
<ul>
<li><code>Document document</code> <code>Document</code>对象</li>
<li><code>boolean validation</code> 是否校验<code>xml</code></li>
<li><code>EntiryResolver entityResolver</code></li>
<li><code>Properties variables</code> 属性</li>
<li><code>XPath xpath</code> <code>Xpath</code>对象</li>
</ul>
<h4 data-id="heading-3">2.1.1 构造方法</h4>
<p>在<code>XPathParser</code>中提供了很多个构造方法，这里就不进行列举了，在这些方法中没有过多的逻辑，就是创建<code>Document</code>和<code>XPath</code>对象并设置其他属性字段。</p>
<p>在其构造方法中会调用到<code>commonConstructor</code>和<code>createDocument</code>两个方法，其源码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">commonConstructor</span><span class="hljs-params">(<span class="hljs-keyword">boolean</span> validation, Properties variables, EntityResolver entityResolver)</span> </span>&#123;
    <span class="hljs-comment">// 设置是否校验XML</span>
    <span class="hljs-keyword">this</span>.validation = validation;
    <span class="hljs-comment">// EntityResolver用于解析本地DTD或XSD</span>
    <span class="hljs-keyword">this</span>.entityResolver = entityResolver;
    <span class="hljs-comment">// 配置文件中配置的properties</span>
    <span class="hljs-keyword">this</span>.variables = variables;
    <span class="hljs-comment">// 创建XPath对象</span>
    XPathFactory factory = XPathFactory.newInstance();
    <span class="hljs-keyword">this</span>.xpath = factory.newXPath();
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">private</span> Document <span class="hljs-title">createDocument</span><span class="hljs-params">(InputSource inputSource)</span> </span>&#123;
    <span class="hljs-comment">// important: this must only be called AFTER common constructor</span>
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 创建DocumentBuilderFactory对象</span>
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, <span class="hljs-keyword">true</span>);
        <span class="hljs-comment">// 是否校验</span>
        factory.setValidating(validation);
        <span class="hljs-comment">// 设置其他一些属性</span>
        factory.setNamespaceAware(<span class="hljs-keyword">false</span>);
        factory.setIgnoringComments(<span class="hljs-keyword">true</span>);
        factory.setIgnoringElementContentWhitespace(<span class="hljs-keyword">false</span>);
        factory.setCoalescing(<span class="hljs-keyword">false</span>);
        factory.setExpandEntityReferences(<span class="hljs-keyword">true</span>);
        <span class="hljs-comment">// 创建DocumentBuilder对象</span>
        DocumentBuilder builder = factory.newDocumentBuilder();
        <span class="hljs-comment">// 设置EntityResolver</span>
        builder.setEntityResolver(entityResolver);
        builder.setErrorHandler(<span class="hljs-keyword">new</span> ErrorHandler() &#123;
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">error</span><span class="hljs-params">(SAXParseException exception)</span> <span class="hljs-keyword">throws</span> SAXException </span>&#123;
                <span class="hljs-keyword">throw</span> exception;
            &#125;
​
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">fatalError</span><span class="hljs-params">(SAXParseException exception)</span> <span class="hljs-keyword">throws</span> SAXException </span>&#123;
                <span class="hljs-keyword">throw</span> exception;
            &#125;
​
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">warning</span><span class="hljs-params">(SAXParseException exception)</span> <span class="hljs-keyword">throws</span> SAXException </span>&#123;
                <span class="hljs-comment">// NOP</span>
            &#125;
        &#125;);
        <span class="hljs-comment">// 创建Document对象并返回</span>
        <span class="hljs-keyword">return</span> builder.parse(inputSource);
    &#125; <span class="hljs-keyword">catch</span> (Exception e) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> BuilderException(<span class="hljs-string">"Error creating document instance.  Cause: "</span> + e, e);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这些代码也没什么可说的，这些都是创建<code>Xpath</code>和<code>Document</code>对象时固定的代码。</p>
<h4 data-id="heading-4">2.1.2 解析方法</h4>
<p>在<code>XPathParser</code>中提供了多个<code>eval*</code>方法，用于解析<code>XML</code>获取到不同类型的数据，提供了如下的方法</p>
<ul>
<li><code>evalString</code> 获取字符串数据</li>
<li><code>evalBoolean</code> 获取布尔数据</li>
<li><code>evalShort</code> 获取short类型数据</li>
<li><code>evalInteger</code> 获取Integer类型数据</li>
<li><code>evalLong</code> 获取Long类型数据</li>
<li><code>evalFloat</code> 获取Float类型数据</li>
<li><code>evalDouble</code> 获取Double类型数据</li>
<li><code>evalNodes</code> 获取<code>XNode</code>列表数据</li>
<li><code>evalNode</code> 获取<code>XNode</code>数据</li>
</ul>
<p>这些方法最后都调用到<code>evaluate</code>方法，在这个方法中调用了<code>XPath.evaluate</code>方法，其源码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> Object <span class="hljs-title">evaluate</span><span class="hljs-params">(String expression, Object root, QName returnType)</span> </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 调用XPath.evaluate</span>
        <span class="hljs-keyword">return</span> xpath.evaluate(expression, root, returnType);
    &#125; <span class="hljs-keyword">catch</span> (Exception e) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> BuilderException(<span class="hljs-string">"Error evaluating XPath.  Cause: "</span> + e, e);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们看下<code>evalString</code>、<code>evalNode</code>和<code>evalNodes</code>方法。</p>
<p><code>evalString</code>的源码如下如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">evalString</span><span class="hljs-params">(Object root, String expression)</span> </span>&#123;
    <span class="hljs-comment">// 解析出字符串值</span>
    String result = (String) evaluate(expression, root, XPathConstants.STRING);
    <span class="hljs-comment">// 处理字符串中的占位符</span>
    result = PropertyParser.parse(result, variables);
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>evalNode</code>和<code>evalNodes</code>的源码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 获取XNode列表对象</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> List<XNode> <span class="hljs-title">evalNodes</span><span class="hljs-params">(Object root, String expression)</span> </span>&#123;
    <span class="hljs-comment">// XNode列表</span>
    List<XNode> xnodes = <span class="hljs-keyword">new</span> ArrayList<>();
    <span class="hljs-comment">// XPath.evaluate方法中获取到的NodeList列表</span>
    NodeList nodes = (NodeList) evaluate(expression, root, XPathConstants.NODESET);
    <span class="hljs-comment">// 遍历NodeList获取其中的Node对象</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < nodes.getLength(); i++) &#123;
        <span class="hljs-comment">// 封装成一个XNode对象并添加到列表中</span>
        xnodes.add(<span class="hljs-keyword">new</span> XNode(<span class="hljs-keyword">this</span>, nodes.item(i), variables));
    &#125;
    <span class="hljs-comment">// 返回XNode列表对象</span>
    <span class="hljs-keyword">return</span> xnodes;
&#125;
<span class="hljs-comment">// 获取XNode对象</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> XNode <span class="hljs-title">evalNode</span><span class="hljs-params">(Object root, String expression)</span> </span>&#123;
    Node node = (Node) evaluate(expression, root, XPathConstants.NODE);
    <span class="hljs-keyword">if</span> (node == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> XNode(<span class="hljs-keyword">this</span>, node, variables);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这两段源码我们可以看到，在<code>XPathParser</code>中解析出字符串后会再调用<code>PropertyParser.parse</code>方法，该方法是用来处理配置文件中的占位符，对<code>org.w3c.dom.Node</code>类进行了封装，接下来我们看看占位符的处理及<code>XNode</code>对象。</p>
<h3 data-id="heading-5">2.2 占位符处理</h3>
<p>在上面解析源码中，我们看到获取到<code>XML</code>中的字符串后调用<code>PropertyParser.parser</code>方法替换其中的占位符，其逻辑如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String KEY_PREFIX = <span class="hljs-string">"org.apache.ibatis.parsing.PropertyParser."</span>;
<span class="hljs-comment">// 通过这个配置设置是否支持默认值</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String KEY_ENABLE_DEFAULT_VALUE = KEY_PREFIX + <span class="hljs-string">"enable-default-value"</span>;
<span class="hljs-comment">// 通过这个配置自定义分隔符</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String KEY_DEFAULT_VALUE_SEPARATOR = KEY_PREFIX + <span class="hljs-string">"default-value-separator"</span>;
<span class="hljs-comment">// 默认是否支持默认值为false</span>
<span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String ENABLE_DEFAULT_VALUE = <span class="hljs-string">"false"</span>;
<span class="hljs-comment">// 默认分隔符为:</span>
<span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String DEFAULT_VALUE_SEPARATOR = <span class="hljs-string">":"</span>;
​
<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">PropertyParser</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-comment">// Prevent Instantiation</span>
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> String <span class="hljs-title">parse</span><span class="hljs-params">(String string, Properties variables)</span> </span>&#123;
    <span class="hljs-comment">// 创建VariableTokenHandler对象</span>
    VariableTokenHandler handler = <span class="hljs-keyword">new</span> VariableTokenHandler(variables);
    <span class="hljs-comment">// 创建GenericTokenParser对象</span>
    GenericTokenParser parser = <span class="hljs-keyword">new</span> GenericTokenParser(<span class="hljs-string">"$&#123;"</span>, <span class="hljs-string">"&#125;"</span>, handler);
    <span class="hljs-comment">// 处理占位符</span>
    <span class="hljs-keyword">return</span> parser.parse(string);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>PropertyParser.parser</code>方法中创建了<code>VariableTokenHandler</code>和<code>GenericTokenParser</code>对象，最后调用<code>GenericTokenParser.parse</code>方法。</p>
<ul>
<li><code>GenericTokenParser</code> 负责解析出占位符中的字面值。</li>
<li><code>VariableTokenHandler</code> 负责从<code>Properties</code>中获取占位符所代表的值。</li>
</ul>
<p><code>GenericTokenParser.parser</code>方法，是解析出字符串中的占位符，然后调用<code>VariableTokenHandler.tokenHandler</code>方法获取到其对应的值。</p>
<p><code>VariableTokenHandler</code>是<code>PropertyParser</code>中的一个内部类，该类实现了<code>TokenHandler</code>接口。其源码如下:</p>
<pre><code class="copyable">private static class VariableTokenHandler implements TokenHandler &#123;
    // 配置文件中的Properties
    private final Properties variables;
    // 是否支持默认值
    private final boolean enableDefaultValue;
    // 分隔符
    private final String defaultValueSeparator;
​
    private VariableTokenHandler(Properties variables) &#123;
        this.variables = variables;
        // 获取是否支持默认值配置
        this.enableDefaultValue = Boolean.parseBoolean(getPropertyValue(KEY_ENABLE_DEFAULT_VALUE, ENABLE_DEFAULT_VALUE));
        // 获取分隔符
        this.defaultValueSeparator = getPropertyValue(KEY_DEFAULT_VALUE_SEPARATOR, DEFAULT_VALUE_SEPARATOR);
    &#125;
​
    // 根据key查找对应的value   如果不存在返回默认值
    private String getPropertyValue(String key, String defaultValue) &#123;
        return (variables == null) ? defaultValue : variables.getProperty(key, defaultValue);
    &#125;
​
    @Override
    public String handleToken(String content) &#123;
        // 判断Properties是否为空
        if (variables != null) &#123;
            String key = content;
            // 是否支持默认值
            if (enableDefaultValue) &#123;
                final int separatorIndex = content.indexOf(defaultValueSeparator);
                String defaultValue = null;
                if (separatorIndex >= 0) &#123;
                    // 分隔符前是Properties中的key
                    key = content.substring(0, separatorIndex);
                    // 分隔符后是默认值
                    defaultValue = content.substring(separatorIndex + defaultValueSeparator.length());
                &#125;
                // 默认值存在，先从Properties中查找   没有找到则返回默认值
                if (defaultValue != null) &#123;
                    return variables.getProperty(key, defaultValue);
                &#125;
            &#125;
            // 如果存在这个配置则返回
            if (variables.containsKey(key)) &#123;
                return variables.getProperty(key);
            &#125;
        &#125;
        return "$&#123;" + content + "&#125;";
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>TokenHandler</code>还有其他的三个实现类，在之后的内容中我们会进行介绍，其实现类如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5066c7b9a03f4cf1bbd363cf8a3a2f12~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828160048333" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">2.3 XNode</h3>
<p><code>XNode</code>是<code>Mybatis</code>中用来表示节点的数据，其对<code>org.w3c.dom.Node</code>进行了封装，该类的属性字段如下：</p>
<ul>
<li><code>Node node</code></li>
<li><code>String name</code></li>
<li><code>String body</code></li>
<li><code>Properties attributes</code></li>
<li><code>Properties variabes</code></li>
<li><code>XPathParser xpathParser</code></li>
</ul>
<p>构造方法如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">XNode</span><span class="hljs-params">(XPathParser xpathParser, Node node, Properties variables)</span> </span>&#123;
    <span class="hljs-keyword">this</span>.xpathParser = xpathParser;
    <span class="hljs-keyword">this</span>.node = node;
    <span class="hljs-comment">// 获取Node名称   标签类型</span>
    <span class="hljs-keyword">this</span>.name = node.getNodeName();
    <span class="hljs-comment">// 传递过来的Properties</span>
    <span class="hljs-keyword">this</span>.variables = variables;
    <span class="hljs-comment">// 解析节点中的属性字段   存储到一个Properties对象</span>
    <span class="hljs-keyword">this</span>.attributes = parseAttributes(node);
    <span class="hljs-keyword">this</span>.body = parseBody(node);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>parseAttributes</code>是解析出<code>org.w3c.dom.NOde</code>中的属性字段存储到一个Properties对象中，其源码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> Properties <span class="hljs-title">parseAttributes</span><span class="hljs-params">(Node n)</span> </span>&#123;
    Properties attributes = <span class="hljs-keyword">new</span> Properties();
    <span class="hljs-comment">// 获取NamedNodeMap</span>
    NamedNodeMap attributeNodes = n.getAttributes();
    <span class="hljs-keyword">if</span> (attributeNodes != <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-comment">// 遍历NamedNodeMap</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < attributeNodes.getLength(); i++) &#123;
            Node attribute = attributeNodes.item(i);
            <span class="hljs-comment">// 解析配置的value值</span>
            String value = PropertyParser.parse(attribute.getNodeValue(), variables);
            <span class="hljs-comment">// 存储到Properties中</span>
            attributes.put(attribute.getNodeName(), value);
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> attributes;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>parseBody</code>方法如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> String <span class="hljs-title">parseBody</span><span class="hljs-params">(Node node)</span> </span>&#123;
    <span class="hljs-comment">// 获取文本数据</span>
    String data = getBodyData(node);
    <span class="hljs-keyword">if</span> (data == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-comment">// 如果不是文本节点   获取子节点</span>
        NodeList children = node.getChildNodes();
        <span class="hljs-comment">// 遍历子节点  获取文本</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < children.getLength(); i++) &#123;
            Node child = children.item(i);
            data = getBodyData(child);
            <span class="hljs-keyword">if</span> (data != <span class="hljs-keyword">null</span>) &#123;
                <span class="hljs-keyword">break</span>;
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> data;
&#125;
​
<span class="hljs-function"><span class="hljs-keyword">private</span> String <span class="hljs-title">getBodyData</span><span class="hljs-params">(Node child)</span> </span>&#123;
    <span class="hljs-comment">// 处理文本节点</span>
    <span class="hljs-keyword">if</span> (child.getNodeType() == Node.CDATA_SECTION_NODE
        || child.getNodeType() == Node.TEXT_NODE) &#123;
        <span class="hljs-comment">// 获取内容</span>
        String data = ((CharacterData) child).getData();
        <span class="hljs-comment">// 处理占位符</span>
        data = PropertyParser.parse(data, variables);
        <span class="hljs-keyword">return</span> data;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>XNode</code>中还提供了一些<code>get</code>和<code>eval</code>方法，这些逻辑也比较简单，这里就不一一粘贴了，大家自行查看源码吧。</p>
<h2 data-id="heading-7">3 总结</h2>
<p>至此今天的内容就结束了，在今天的文章中我们介绍了<code>Mybatis</code>的架构及一个基础模块-解析器。通过对解析器的分析，我们可以看到其作用如下：</p>
<ul>
<li>封装<code>Document</code>和<code>XPath</code>为<code>XML</code>配置文件的解析提供了支持。</li>
<li>处理配置文件中的占位符。</li>
</ul>
<p>该模块所包含的类如下：</p>
<ul>
<li><code>XPathParser</code> 解析器，里面维护了<code>Document</code>和<code>Xpath</code>对象，提供了一系列的<code>eval</code>方法用于配置文件解析。</li>
<li><code>XNode</code> 节点对象，维护了<code>org.w3c.Node</code>对象。</li>
<li><code>PropertyParser</code> 用来处理占位符的入口</li>
<li><code>PropertyParser.VariableTokenHandler</code> 继承自<code>TokenHandler</code>，用于从<code>Properties</code>中获取占位符对应的值。</li>
<li><code>GenericTokenParser</code> 获取字符串中的占位符。</li>
</ul>
<p>这个模块的逻辑不复杂，大家多跟着源码看看相信都能看明白的。</p>
<p>如果感觉对您有帮助，欢迎关注下公众号，您的关注是我更新的最大动力~</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e7b6dd2e27143ecadbee8030211375b~tplv-k3u1fbpfcp-watermark.image" alt="qrcode_for_gh_8febd60b14c9_258.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            
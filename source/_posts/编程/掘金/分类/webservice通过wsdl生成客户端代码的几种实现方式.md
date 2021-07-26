
---
title: 'webservice通过wsdl生成客户端代码的几种实现方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fb8755ba4fd40cf9e3e1dd7f08fbc67~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 01:35:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fb8755ba4fd40cf9e3e1dd7f08fbc67~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>网上的一个 wsdl可以根据这个案例去测试代码生成</strong></p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-meta"><?xml version='1.0' encoding='UTF-8'?></span><span class="hljs-tag"><<span class="hljs-name">wsdl:definitions</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"HelloWorldService"</span> <span class="hljs-attr">targetNamespace</span>=<span class="hljs-string">"http://test.demo1/"</span> <span class="hljs-attr">xmlns:ns1</span>=<span class="hljs-string">"http://schemas.xmlsoap.org/soap/http"</span> <span class="hljs-attr">xmlns:soap</span>=<span class="hljs-string">"http://schemas.xmlsoap.org/wsdl/soap/"</span> <span class="hljs-attr">xmlns:tns</span>=<span class="hljs-string">"http://test.demo1/"</span> <span class="hljs-attr">xmlns:wsdl</span>=<span class="hljs-string">"http://schemas.xmlsoap.org/wsdl/"</span> <span class="hljs-attr">xmlns:xsd</span>=<span class="hljs-string">"http://www.w3.org/2001/XMLSchema"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">wsdl:types</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">xs:schema</span> <span class="hljs-attr">elementFormDefault</span>=<span class="hljs-string">"unqualified"</span> <span class="hljs-attr">targetNamespace</span>=<span class="hljs-string">"http://test.demo1/"</span> <span class="hljs-attr">version</span>=<span class="hljs-string">"1.0"</span> <span class="hljs-attr">xmlns:tns</span>=<span class="hljs-string">"http://test.demo1/"</span> <span class="hljs-attr">xmlns:xs</span>=<span class="hljs-string">"http://www.w3.org/2001/XMLSchema"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">xs:element</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHello"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"tns:sayHello"</span>/></span>
            <span class="hljs-tag"><<span class="hljs-name">xs:element</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHelloResponse"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"tns:sayHelloResponse"</span>/></span>
            <span class="hljs-tag"><<span class="hljs-name">xs:complexType</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHello"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">xs:sequence</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">xs:element</span> <span class="hljs-attr">minOccurs</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"arg0"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"xs:string"</span>/></span>
                <span class="hljs-tag"></<span class="hljs-name">xs:sequence</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">xs:complexType</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">xs:complexType</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHelloResponse"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">xs:sequence</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">xs:element</span> <span class="hljs-attr">minOccurs</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"return"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"xs:string"</span>/></span>
                <span class="hljs-tag"></<span class="hljs-name">xs:sequence</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">xs:complexType</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">xs:schema</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">wsdl:types</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">wsdl:message</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHelloResponse"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">wsdl:part</span> <span class="hljs-attr">element</span>=<span class="hljs-string">"tns:sayHelloResponse"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"parameters"</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">wsdl:part</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">wsdl:message</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">wsdl:message</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHello"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">wsdl:part</span> <span class="hljs-attr">element</span>=<span class="hljs-string">"tns:sayHello"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"parameters"</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">wsdl:part</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">wsdl:message</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">wsdl:portType</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"HelloWorld"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">wsdl:operation</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHello"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">wsdl:input</span> <span class="hljs-attr">message</span>=<span class="hljs-string">"tns:sayHello"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHello"</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">wsdl:input</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">wsdl:output</span> <span class="hljs-attr">message</span>=<span class="hljs-string">"tns:sayHelloResponse"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHelloResponse"</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">wsdl:output</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">wsdl:operation</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">wsdl:portType</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">wsdl:binding</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"HelloWorldServiceSoapBinding"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"tns:HelloWorld"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">soap:binding</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"document"</span> <span class="hljs-attr">transport</span>=<span class="hljs-string">"http://schemas.xmlsoap.org/soap/http"</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">wsdl:operation</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHello"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">soap:operation</span> <span class="hljs-attr">soapAction</span>=<span class="hljs-string">""</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"document"</span>/></span>
            <span class="hljs-tag"><<span class="hljs-name">wsdl:input</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHello"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">soap:body</span> <span class="hljs-attr">use</span>=<span class="hljs-string">"literal"</span>/></span>
            <span class="hljs-tag"></<span class="hljs-name">wsdl:input</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">wsdl:output</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sayHelloResponse"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">soap:body</span> <span class="hljs-attr">use</span>=<span class="hljs-string">"literal"</span>/></span>
            <span class="hljs-tag"></<span class="hljs-name">wsdl:output</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">wsdl:operation</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">wsdl:binding</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">wsdl:service</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"HelloWorldService"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">wsdl:port</span> <span class="hljs-attr">binding</span>=<span class="hljs-string">"tns:HelloWorldServiceSoapBinding"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"HelloWorldPort"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">soap:address</span> <span class="hljs-attr">location</span>=<span class="hljs-string">"http://localhost:8080/helloWorld"</span>/></span>
        <span class="hljs-tag"></<span class="hljs-name">wsdl:port</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">wsdl:service</span>></span>
<span class="hljs-tag"></<span class="hljs-name">wsdl:definitions</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-0">1、<a id="user-content-1" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">jdk自带的方式<code>wsimport</code></a></h4>
<blockquote>
<p>参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fu012614715%2Farticle%2Fdetails%2F80420095" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/u012614715/article/details/80420095" ref="nofollow noopener noreferrer">通过wsdl生成客户端代码</a></p>
<p><strong>PS: 在 java.bin目录下执行 wsimport 命令</strong></p>
</blockquote>
<pre><code class="copyable">用法: wsimport [options] <WSDL_URI>

\其中 [options] 包括:
  -b <path>                 指定 jaxws/jaxb 绑定文件或附加模式
                            (每个 <path> 都必须具有自己的 -b)
  -B<jaxbOption>            将此选项传递给 JAXB 模式编译器
  -catalog <file>           指定用于解析外部实体引用的目录文件
                            支持 TR9401, XCatalog 和 OASIS XML 目录格式。
  -d <directory>            指定放置生成的输出文件的位置
  -encoding <encoding>      指定源文件所使用的字符编码
  -extension                允许供应商扩展 - 不按规范
                            指定功能。使用扩展可能会
                            导致应用程序不可移植或
                            无法与其他实现进行互操作
  -help                     显示帮助
  -httpproxy:<host>:<port>  指定 HTTP 代理服务器 (端口默认为 8080)
  -keep                     保留生成的文件
  -p <pkg>                  指定目标程序包
  -quiet                    隐藏 wsimport 输出
  -s <directory>            指定放置生成的源文件的位置
  -target <version>         按给定的 JAXWS 规范版本生成代码
                            默认为 2.2, 接受的值为 2.0, 2.1 和 2.2
                            例如, 2.0 将为 JAXWS 2.0 规范生成兼容的代码
  -verbose                  有关编译器在执行什么操作的输出消息
  -version                  输出版本信息
  -wsdllocation <location>  @WebServiceClient.wsdlLocation 值
  -clientjar <jarfile>      创建生成的 Artifact 的 jar 文件以及
                            调用 Web 服务所需的 WSDL 元数据。
  -generateJWS              生成存根 JWS 实现文件
  -implDestDir <directory>  指定生成 JWS 实现文件的位置
  -implServiceName <name>   生成的 JWS 实现的服务名的本地部分
  -implPortName <name>      生成的 JWS 实现的端口名的本地部分

\扩展:
  -XadditionalHeaders              映射标头不绑定到请求或响应消息不绑定到
                                   Java 方法参数
  -Xauthfile                       用于传送以下格式的授权信息的文件:
                                   http://username:password@example.org/stock?wsdl
  -Xdebug                          输出调试信息
  -Xno-addressing-databinding      允许 W3C EndpointReferenceType 到 Java 的绑定
  -Xnocompile                      不编译生成的 Java 文件
  -XdisableAuthenticator           禁用由 JAX-WS RI 使用的验证程序,
                                   将忽略 -Xauthfile 选项 (如果设置)
  -XdisableSSLHostnameVerification 在提取 wsdl 时禁用 SSL 主机名
                                   验证

\示例:
  wsimport stock.wsdl -b stock.xml -b stock.xjb
  wsimport -d generated http://example.org/stock?wsdl
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2、<a id="user-content-2" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">Apache-cxf的wsdl2java方式</a></h4>
<ol>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fcxf.apache.org%2Fdownload.html" target="_blank" rel="nofollow noopener noreferrer" title="http://cxf.apache.org/download.html" ref="nofollow noopener noreferrer">Apache CXF 下载</a> 一般选择 Binary distribution 的就可以</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fb8755ba4fd40cf9e3e1dd7f08fbc67~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>
<p>下载后解压到指定目录</p>
<pre><code class="hljs language-tex copyable" lang="tex">E:<span class="hljs-keyword">\service</span><span class="hljs-keyword">\webservice</span><span class="hljs-keyword">\apache</span>-cxf-3.3.11
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47419699dcad43e8908513a72d3f8846~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>
<p>将 <code>apache-cxf-*/bin</code>目录加入到系统变量<code>path</code>中</p>
<pre><code class="hljs language-tex copyable" lang="tex">E:<span class="hljs-keyword">\service</span><span class="hljs-keyword">\webservice</span><span class="hljs-keyword">\apache</span>-cxf-3.3.11<span class="hljs-keyword">\bin</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29225ac383e443eaacd937d75ec598b7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>CMD命令输入 <code>wsdl2java -help</code> 测试是否正常</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbdfa4d2265b4fc5a1c2ef565cb6eddc~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>
<p>在解压的目录 <code>apache-cxf-*/bin</code>下执行<code>wsdl2java</code>命令</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae825d1e14bf4cb5a21456579e0bc1ff~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16be813dbc9e4a71a7b6d8f85e6ffaad~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>wsdl2java -encoding utf-8 -d <code>生成文件的目录</code> <code>wsdl文件地址或wsdl url地址</code></strong></p>
<pre><code class="hljs language-shell copyable" lang="shell">PS E:\service\webservice\apache-cxf-3.3.11\bin> wsdl2java -encoding utf-8 -p com.example.order -d D:\ideaProject\htlm\demo\web-service-demo\src\main\java D:\ideaProject\htlm\demo\web-service-demo\src\main\resources\Air.wsdl
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<pre><code class="copyable">   用法: wsdl2java [options] <WSDL_URI>
   
   \其中 [options] 包括:
   -p <[wsdl-namespace =]package-name>*    指定生成的代码要使用的 java 包名称
   -d <output-directory>                   指定放置生成的目录
   -server                                 指定生成服务端代码
   -client                                 指定生成客户端代码
   -autoNameResolution                     指定该工具将尝试解决类的命名冲突，而不要求使用绑定定制。
   \示例:
     wsdl2java -d D:\demo D:\t.wsdl
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3、IDEA自带插件生成</h4>
<ol>
<li>
<p>idea菜单栏选择<code>Tools->WebServices->Generate Java Code From Wsdl</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cfbc90d92cb40f4b2505a40ce32d96c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ol>
<h4 data-id="heading-3">常见问题</h4>
<ol>
<li>IDEA生成代码时，如果使用的jdk11编译的项目，可能会出现如下错误， 请使用jdk8。或者使用<a href="https://juejin.cn/post/6989166390708011015#1" target="_blank" title="#1">第二种</a>生成方式</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25d828967956497a937f2c383df97dc1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>
<p>提示 <code>具有相同名称 的类/接口已在使用。请使用类定制设置来解决此冲突</code></p>
<p>以<a href="https://juejin.cn/post/6989166390708011015#1" target="_blank" title="#1">第二种</a>生成方式为例, 只要在命令中添加 <code>-autoNameResolution</code>参数即可</p>
<pre><code class="copyable">wsdl2java -autoNameResolution -d D:\demo D:\t.wsdl
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol></div>  
</div>
            

---
title: 'Java后端架构开荒实战（一）——基础设施'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3bc8abd5994192916adfd91f9feb3e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 23:56:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3bc8abd5994192916adfd91f9feb3e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、前言</h3>
<p>之前的文章有讲过后端架构演进系列，这个系列文章还是以一个经典的电商系统为例子，来讲讲Robben是如何在实际开发中一步一步打造出一个大型的后端架构的。本系列文章更多的一些实践操作方面的操作和选型。</p>
<p>工欲善其事，必先利其器。在业务代码开发前，让我们先做好相关的基础设置建设。</p>
<h3 data-id="heading-1">二、云平台</h3>
<p>云服务的选择有阿里云、腾讯云、华为云等等。阿里云是老牌云服务商了，产品配套齐全，文档丰富，价格也是相应的贵一点。腾讯云算是后起之秀，有腾讯背书，价格比阿里云便宜点。华为云没用过就不评价。</p>
<p>运行环境可以选择jar包直接运行在Linux环境上，也可以选择使用Kubernets进行部署。</p>
<p>我们这里云服务商选择腾讯云，然后平台选择Kubernetes去管理我们整个后端应用周期。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3bc8abd5994192916adfd91f9feb3e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">三、代码管理</h3>
<p>关于Git和Svn现在基本都是选择Git了吧。可以使用私有的GitLab，或者使用云服务的Git仓库也是一个不错的选择。大部分公司为了代码安全考虑会选择自建仓库。</p>
<ul>
<li>自建GitLab参考：<a href="https://cloud.tencent.com/developer/article/1556751" target="_blank" rel="nofollow noopener noreferrer">TKE容器集群中部署GitLab服务器</a></li>
<li>云服务腾讯云coding：</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f30dc80868d438e8a0e34ee4dc523bf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>本系列文章使用coding的代码仓库来管理。</p>
<h3 data-id="heading-3">四、文件服务</h3>
<p>这里把文件服务单独拎出来，因为文件存储的安全和维护是比较重要和独立的。</p>
<ul>
<li>自建分布式文件服务fastdfs</li>
</ul>
<p>fastdfs是开源的分布式文件系统，充分考虑了冗余备份、负载均衡、线性扩容等机制，并注重高可用、高性能等指标。一般用在图片和音频这种中小文件存储，有自建需求的团队可以考虑。</p>
<ul>
<li>使用云服务商提供的文件服务</li>
</ul>
<p>这种就没什么好说的，像阿里云OSS，七牛云等等都可以。</p>
<p>综合成本使用考虑本系列文章使用七牛云的文件服务。</p>
<h3 data-id="heading-4">五、统一依赖管理Maven</h3>
<p>随着依赖的不断增多，内部服务的不断产生。统一的版本管理就显得十分重要。</p>
<h4 data-id="heading-5">Maven私服</h4>
<p>用来统一管理依赖和内部二方库。可以选择自建，也可以用云服务的。<br>
自建Nexus: 省略了，网上一搜以大把。<br>
云服务：Coding的制品库管理。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30f0eecd85624a3c9639b89755aeb3a9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>maven setting中指定</p>
<pre><code class="copyable"><profile>
    <id>robbendev-robbendev-robbendev</id>
    <activation>
        <activeByDefault>true</activeByDefault>
    </activation>
    <repositories>
        <repository>
            <id>robbendev-robbendev-robbendev</id>
            <name>robbendev</name>
            <url>https://robbendev-maven.pkg.coding.net/repository/robbendev/robbendev/</url>
            <releases>
                <enabled>true</enabled>
                <updatePolicy>always</updatePolicy>
            </releases>
            <snapshots>
                <enabled>true</enabled>
                <updatePolicy>always</updatePolicy>
            </snapshots>
        </repository>
    </repositories>
</profile>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">统一依赖项目</h4>
<p>统一依赖项目结构</p>
<pre><code class="copyable">robbendev-maven
├── pom.xml
├── robbendev-bom
│   ├── pom.xml
├── robbendev-dependencies
│   ├── pom.xml
└── robbendev-parent
    ├── pom.xml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看下具体代码</p>
<p>robbendev.maven/pom.xml主要是配置私服的地址</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
<span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-maven<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
<span class="hljs-tag"><<span class="hljs-name">version</span>></span>1.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">version</span>></span>

<span class="hljs-tag"><<span class="hljs-name">modules</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>robbendev-bom<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>robbendev-dependencies<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">module</span>></span>robbendev-parent<span class="hljs-tag"></<span class="hljs-name">module</span>></span>
<span class="hljs-tag"></<span class="hljs-name">modules</span>></span>

<span class="hljs-tag"><<span class="hljs-name">packaging</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">packaging</span>></span>

<span class="hljs-tag"><<span class="hljs-name">name</span>></span>robbendev-maven<span class="hljs-tag"></<span class="hljs-name">name</span>></span>
<span class="hljs-tag"><<span class="hljs-name">description</span>></span>robbendev maven nexus 基础配置<span class="hljs-tag"></<span class="hljs-name">description</span>></span>

<span class="hljs-comment"><!-- omitted xml --></span>
<span class="hljs-tag"><<span class="hljs-name">distributionManagement</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">repository</span>></span>
        <span class="hljs-comment"><!--必须与 settings.xml 的 id 一致--></span>
        <span class="hljs-tag"><<span class="hljs-name">id</span>></span>robbendev-robbendev-robbendev<span class="hljs-tag"></<span class="hljs-name">id</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">name</span>></span>robbendev<span class="hljs-tag"></<span class="hljs-name">name</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">url</span>></span>https://robbendev-maven.pkg.coding.net/repository/robbendev/robbendev/<span class="hljs-tag"></<span class="hljs-name">url</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">repository</span>></span>
<span class="hljs-tag"></<span class="hljs-name">distributionManagement</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>robbendev-maven/robbendev-bom/pom.xml主要是统一内部二方库的依赖版本</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">parent</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-maven<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>1.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">parent</span>></span>
<span class="hljs-tag"><<span class="hljs-name">modelVersion</span>></span>4.0.0<span class="hljs-tag"></<span class="hljs-name">modelVersion</span>></span>

<span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-bom<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
<span class="hljs-tag"><<span class="hljs-name">name</span>></span>robbendev-bom<span class="hljs-tag"></<span class="hljs-name">name</span>></span>
<span class="hljs-tag"><<span class="hljs-name">description</span>></span>robbendev二方库依赖配置<span class="hljs-tag"></<span class="hljs-name">description</span>></span>
<span class="hljs-tag"><<span class="hljs-name">packaging</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">packaging</span>></span>

<span class="hljs-tag"><<span class="hljs-name">properties</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">robbendev-common.version</span>></span>1.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">robbendev-common.version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">properties</span>></span>

<span class="hljs-tag"><<span class="hljs-name">dependencyManagement</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dependencies</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbdendev-common<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;robbendev-common.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">dependencies</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependencyManagement</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>robbendev-maven/robbendev-dependencies/pom.xml主要是统一外部三方库的依赖版本</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">parent</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-maven<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>1.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">parent</span>></span>
<span class="hljs-tag"><<span class="hljs-name">modelVersion</span>></span>4.0.0<span class="hljs-tag"></<span class="hljs-name">modelVersion</span>></span>

<span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-dependencies<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
<span class="hljs-tag"><<span class="hljs-name">name</span>></span>robbendev-dependencies<span class="hljs-tag"></<span class="hljs-name">name</span>></span>
<span class="hljs-tag"><<span class="hljs-name">description</span>></span>robbendev三方库依赖配置<span class="hljs-tag"></<span class="hljs-name">description</span>></span>
<span class="hljs-tag"><<span class="hljs-name">packaging</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">packaging</span>></span>

<span class="hljs-tag"><<span class="hljs-name">properties</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">spring-cloud.version</span>></span>Hoxton.SR7<span class="hljs-tag"></<span class="hljs-name">spring-cloud.version</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">spring-boot.version</span>></span>2.3.3.RELEASE<span class="hljs-tag"></<span class="hljs-name">spring-boot.version</span>></span>
    ...
<span class="hljs-tag"></<span class="hljs-name">properties</span>></span>

<span class="hljs-tag"><<span class="hljs-name">dependencyManagement</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">dependencies</span>></span>

        <span class="hljs-comment"><!--spring cloud--></span>
        <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.cloud<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-cloud-dependencies<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;spring-cloud.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">type</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">type</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>import<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>

        <span class="hljs-comment"><!--spring boot--></span>
        <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.boot<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-boot-dependencies<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;spring-boot.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">type</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">type</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>import<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
        ...

    <span class="hljs-tag"></<span class="hljs-name">dependencies</span>></span>

<span class="hljs-tag"></<span class="hljs-name">dependencyManagement</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>robbendev-maven/robbendev-parent/pom.xml聚合二方库和三方库依赖配置的pom作为所有项目的父pom文件</p>
<pre><code class="hljs language-xml copyable" lang="xml">    <span class="hljs-tag"><<span class="hljs-name">properties</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">robbendev-bom.version</span>></span>1.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">robbendev-bom.version</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">robbendev-dependencies.version</span>></span>1.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">robbendev-dependencies.version</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">properties</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">dependencyManagement</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">dependencies</span>></span>

            <span class="hljs-comment"><!--二方库依赖管理--></span>
            <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-bom<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;robbendev-bom.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>import<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">type</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">type</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>

            <span class="hljs-comment"><!--一方库依赖管理--></span>
            <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-dependencies<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">version</span>></span>$&#123;robbendev-dependencies.version&#125;<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>import<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">type</span>></span>pom<span class="hljs-tag"></<span class="hljs-name">type</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">dependencies</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">dependencyManagement</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们的依赖管理就完成了，新的项目只用继承</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">parent</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.robbendev<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>robbendev-parent<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>1.0-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">parent</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">六、自动集成CI/CD</h3>
<p>自定集成将开发人员从繁杂的打包发布过程解脱出来，能专注于业务代码的开发。是团队提效的有效方法。</p>
<h4 data-id="heading-8">二方库的发布</h4>
<p>以robbendev-maven项目为例子，我们在每次依赖版本有变更的时候，如何快速推送Maven私服呢？
以本项目为例业内有一下常见方案</p>
<ol>
<li>gitlab-ci 如果使用的gitlab仓库的话可以考虑这个方案。</li>
</ol>
<ul>
<li>自建jenkins 如果有自己的运维团队，可以考虑使用自建的运维平台。</li>
<li>使用云服务</li>
</ul>
<p>这里简单介绍下笔者使用的coding持续继承，这个也是完全兼容jenkins的。
基本上也是在控制台配置好：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7299c102e4704ec583432ae592876957~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以使用流程配置，也可以使用仓库中的Jenkinsfile</p>
<pre><code class="hljs language-groovy copyable" lang="groovy">...
stage(<span class="hljs-string">'编译'</span>) &#123;
    steps &#123;
        sh <span class="hljs-string">'mvn clean package'</span>
    &#125;
&#125;
stage(<span class="hljs-string">'推送到 CODING Maven 制品库'</span>) &#123;
    steps &#123;
        echo <span class="hljs-string">'发布中...'</span>
        sh <span class="hljs-string">'mvn deploy -DskipTests'</span>
        echo <span class="hljs-string">'发布完成.'</span>
    &#125;
&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包机器由于要配置maven的setting文件，所以选择自定义节点构建。</p>
<p>选择适合自己的触发方式，现在提交代码就可以看到触发了自动集成和部署：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/247f6e0abb00456a940dc4eceada05ff~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">服务的发布</h4>
<p>以一个最基础的SpringBoot的程序为例子
在腾讯云镜像仓库获取账号密码后
在maven setting中配置</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">server</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">id</span>></span>robbendev-docker<span class="hljs-tag"></<span class="hljs-name">id</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">username</span>></span>100000000000<span class="hljs-tag"></<span class="hljs-name">username</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">password</span>></span>xxxxxxxxxx<span class="hljs-tag"></<span class="hljs-name">password</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">configuration</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">email</span>></span>xxxxxxx<span class="hljs-tag"></<span class="hljs-name">email</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">configuration</span>></span>
<span class="hljs-tag"></<span class="hljs-name">server</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应用代码结构</p>
<pre><code class="copyable">├── pom.xml
├── src
│   ├── main
│   │   ├── docker
│   │   │   └── Dockerfile
│   │   ├── java
│   └── test

<span class="copy-code-btn">复制代码</span></code></pre>
<p>pom.xml使用docker插件，注意这里的serveId对应setting.xml中的配置，maven.build.timestamp.format属性一定要指定。imageName的含义是使用时间戳作为版本号。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">properties</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">maven.build.timestamp.format</span>></span>yyyyMMddHHmm<span class="hljs-tag"></<span class="hljs-name">maven.build.timestamp.format</span>></span>
    ...
<span class="hljs-tag"></<span class="hljs-name">properties</span>></span>

<span class="hljs-tag"><<span class="hljs-name">plugin</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.spotify<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>docker-maven-plugin<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>1.0.0<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">configuration</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">skipDockerBuild</span>></span>false<span class="hljs-tag"></<span class="hljs-name">skipDockerBuild</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">imageName</span>></span>ccr.ccs.tencentyun.com/robbendev.hello-docker/robbendev-hello-docker:$&#123;maven.build.timestamp&#125;
        <span class="hljs-tag"></<span class="hljs-name">imageName</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">dockerDirectory</span>></span>src/main/docker<span class="hljs-tag"></<span class="hljs-name">dockerDirectory</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">resources</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">resource</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">targetPath</span>></span>/<span class="hljs-tag"></<span class="hljs-name">targetPath</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">directory</span>></span>$&#123;project.build.directory&#125;<span class="hljs-tag"></<span class="hljs-name">directory</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">include</span>></span>$&#123;project.build.finalName&#125;.jar<span class="hljs-tag"></<span class="hljs-name">include</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">resource</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">resources</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">serverId</span>></span>my-docker<span class="hljs-tag"></<span class="hljs-name">serverId</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">configuration</span>></span>
<span class="hljs-tag"></<span class="hljs-name">plugin</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下jenkins关键代码</p>
<pre><code class="hljs language-groovy copyable" lang="groovy">stage(<span class="hljs-string">'编译打包部署'</span>) &#123;
    steps &#123;
        sh <span class="hljs-string">'''
            git checkout master
            git pull
            mvn clean package docker:build -DpushImage'''</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在提交代码的时候就可以自动打包镜像推送到腾讯云镜像仓库，然后通过镜像触发器可以实现自动发布。</p>
<h3 data-id="heading-10">七、小结</h3>
<p>这样一套组合拳下来，Robben终于可以开始好好开发了。接下来会介绍Robben是如何从单体应用到集群再到微服务进行开发的。</p>
<p>觉得有帮助的同学帮忙点个赞。
有问题拍砖<a href="mailto:robbendev@gmail.com">robbendev@gmail.com</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            
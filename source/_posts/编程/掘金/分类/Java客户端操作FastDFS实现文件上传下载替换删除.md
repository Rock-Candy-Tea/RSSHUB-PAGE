
---
title: 'Java客户端操作FastDFS实现文件上传下载替换删除'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9efaa4570f24d499e3558f9802e56bd~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 22:51:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9efaa4570f24d499e3558f9802e56bd~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>　　FastDFS 的作者余庆先生已经为我们开发好了 Java 对应的 SDK。这里需要解释一下：作者余庆并没有及时更新最新的 Java SDK 至 Maven 中央仓库，目前中央仓库最新版仍旧是 1.27 版。所以我们需要通过 Github：<a href="https://github.com/happyfish100/fastdfs-client-java" target="_blank" rel="nofollow noopener noreferrer">github.com/happyfish10…</a> 下载项目源码，再通过命令 <code>mvn clean install</code> 编译打包导入 Maven 本地仓库使用。（文章转载自乐字节）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9efaa4570f24d499e3558f9802e56bd~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　接下来我们通过 Java API 操作 FastDFS 实现文件的上传、下载、替换、删除、查询元数据、查询详情等功能。</p>
<h2 data-id="heading-0">创建项目</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f86b7628f97c4e409290d233b433a156~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/764f477420294f35aa2084a8798c0781~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">添加依赖</h2>
<p>　　在项目的 pom.xml 中添加以下依赖。因为我们需要一些常用工具包和单元测试，所以需要引入它们。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-comment"><!-- fastdfs java client --></span>
<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.csource<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>fastdfs-client-java<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>1.29-SNAPSHOT<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
<span class="hljs-comment"><!-- apache commons lang3 工具包 --></span>
<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.apache.commons<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>commons-lang3<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>3.11<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
<span class="hljs-comment"><!-- junit 单元测试 --></span>
<span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>junit<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>junit<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">version</span>></span>4.13<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>test<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">编写配置文件</h2>
<p>　　fdfs_client.conf</p>
<pre><code class="hljs language-conf copyable" lang="conf"># 超时时间
connect_timeout = 10
network_timeout = 30
# 编码字符集
charset = UTF-8
# tracker 服务器 HTTP 协议下暴露的端口
http.tracker_http_port = 8080
# tracker 服务器的 IP 和端口
tracker_server = 192.168.10.101:22122
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">工具类</h2>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">package</span> org.example.client;

<span class="hljs-keyword">import</span> org.apache.commons.lang3.StringUtils;
<span class="hljs-keyword">import</span> org.csource.common.MyException;
<span class="hljs-keyword">import</span> org.csource.common.NameValuePair;
<span class="hljs-keyword">import</span> org.csource.fastdfs.*;

<span class="hljs-keyword">import</span> java.io.*;

<span class="hljs-comment">/**
 * FastDFS 分布式文件系统 Java 客户端工具类
 * 具体功能：文件上传、下载、替换、删除、查询文件元数据、查看文件详情
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FastDFSClient</span> </span>&#123;

    <span class="hljs-comment">// 获取配置文件地址</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String CONF_FILENAME = Thread.currentThread()
            .getContextClassLoader().getResource(<span class="hljs-string">""</span>).getPath() + <span class="hljs-string">"fdfs_client.conf"</span>;
    <span class="hljs-comment">// Storage 存储服务器客户端</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> StorageClient storageClient = <span class="hljs-keyword">null</span>;

    <span class="hljs-keyword">static</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 加载配置文件</span>
            ClientGlobal.init(CONF_FILENAME);
            <span class="hljs-comment">// 初始化 Tracker 客户端</span>
            TrackerClient trackerClient = <span class="hljs-keyword">new</span> TrackerClient(ClientGlobal.g_tracker_group);
            <span class="hljs-comment">// 初始化 Tracker 服务端</span>
            TrackerServer trackerServer = trackerClient.getTrackerServer();
            <span class="hljs-comment">// 初始化 Storage 服务端</span>
            StorageServer storageServer = trackerClient.getStoreStorage(trackerServer);
            <span class="hljs-comment">// 初始化 Storage 客户端</span>
            storageClient = <span class="hljs-keyword">new</span> StorageClient(trackerServer, storageServer);
        &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (MyException e) &#123;
            e.printStackTrace();
        &#125;
    &#125;

    <span class="hljs-comment">/**
     * 文件上传
     *
     * <span class="hljs-doctag">@param</span> inputStream 上传的文件的字节输入流
     * <span class="hljs-doctag">@param</span> fileName    上传的文件的原始名
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> String[] uploadFile(InputStream inputStream, String fileName) &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 准备字节数组</span>
            <span class="hljs-keyword">byte</span>[] fileBuff = <span class="hljs-keyword">null</span>;
            <span class="hljs-comment">// 文件元数据</span>
            NameValuePair[] metaList = <span class="hljs-keyword">null</span>;
            <span class="hljs-keyword">if</span> (inputStream != <span class="hljs-keyword">null</span>) &#123;
                <span class="hljs-comment">// 查看文件的长度</span>
                <span class="hljs-keyword">int</span> len = inputStream.available();
                <span class="hljs-comment">// 初始化元数据数组</span>
                metaList = <span class="hljs-keyword">new</span> NameValuePair[<span class="hljs-number">2</span>];
                <span class="hljs-comment">// 第一组元数据，文件的原始名称</span>
                metaList[<span class="hljs-number">0</span>] = <span class="hljs-keyword">new</span> NameValuePair(<span class="hljs-string">"file_name"</span>, fileName);
                <span class="hljs-comment">// 第二组元数据，文件的长度</span>
                metaList[<span class="hljs-number">1</span>] = <span class="hljs-keyword">new</span> NameValuePair(<span class="hljs-string">"file_length"</span>, String.valueOf(len));
                <span class="hljs-comment">// 创建对应长度的字节数组</span>
                fileBuff = <span class="hljs-keyword">new</span> <span class="hljs-keyword">byte</span>[len];
                <span class="hljs-comment">// 将输入流中的字节内容，读到字节数组中</span>
                inputStream.read(fileBuff);
            &#125;
            <span class="hljs-comment">/*
                上传文件。
                参数含义：要上传的文件的内容（使用字节数组传递），上传的文件的类型（扩展名），元数据
             */</span>
            String[] fileids = storageClient.upload_file(fileBuff, getFileExt(fileName), metaList);
            <span class="hljs-keyword">return</span> fileids;
        &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (MyException e) &#123;
            e.printStackTrace();
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;

    <span class="hljs-comment">/**
     * 文件上传
     *
     * <span class="hljs-doctag">@param</span> file     上传的文件
     * <span class="hljs-doctag">@param</span> fileName 上传的文件的原始名
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> String[] uploadFile(File file, String fileName) &#123;
        <span class="hljs-keyword">try</span> (FileInputStream fis = <span class="hljs-keyword">new</span> FileInputStream(file)) &#123;
            <span class="hljs-keyword">return</span> uploadFile(fis, fileName);
        &#125; <span class="hljs-keyword">catch</span> (FileNotFoundException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
            e.printStackTrace();
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;

    <span class="hljs-comment">/**
     * 获取文件后缀名（不带点）
     *
     * <span class="hljs-doctag">@param</span> fileName
     * <span class="hljs-doctag">@return</span> 如："jpg" or ""
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> String <span class="hljs-title">getFileExt</span><span class="hljs-params">(String fileName)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (StringUtils.isBlank(fileName) || !fileName.contains(<span class="hljs-string">"."</span>)) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">""</span>;
        &#125;
        <span class="hljs-keyword">return</span> fileName.substring(fileName.lastIndexOf(<span class="hljs-string">"."</span>) + <span class="hljs-number">1</span>); <span class="hljs-comment">// 不带最后的点</span>
    &#125;

    <span class="hljs-comment">/**
     * 获取文件详情
     *
     * <span class="hljs-doctag">@param</span> groupName      组/卷名，默认值：group1
     * <span class="hljs-doctag">@param</span> remoteFileName 文件名，例如："M00/00/00/wKgKZl9tkTCAJAanAADhaCZ_RF0495.jpg"
     * <span class="hljs-doctag">@return</span> 文件详情
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> FileInfo <span class="hljs-title">getFileInfo</span><span class="hljs-params">(String groupName, String remoteFileName)</span> </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">return</span> storageClient.get_file_info(groupName == <span class="hljs-keyword">null</span> ? <span class="hljs-string">"group1"</span> : groupName, remoteFileName);
        &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (MyException e) &#123;
            e.printStackTrace();
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;

    <span class="hljs-comment">/**
     * 获取元数据
     *
     * <span class="hljs-doctag">@param</span> groupName      组/卷名，默认值：group1
     * <span class="hljs-doctag">@param</span> remoteFileName 文件名，例如："M00/00/00/wKgKZl9tkTCAJAanAADhaCZ_RF0495.jpg"
     * <span class="hljs-doctag">@return</span> 文件的元数据数组
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> NameValuePair[] getMetaData(String groupName, String remoteFileName) &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 根据组名和文件名通过 Storage 客户端获取文件的元数据数组</span>
            <span class="hljs-keyword">return</span> storageClient.get_metadata(groupName == <span class="hljs-keyword">null</span> ? <span class="hljs-string">"group1"</span> : groupName, remoteFileName);
        &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (MyException e) &#123;
            e.printStackTrace();
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;

    <span class="hljs-comment">/**
     * 文件下载
     *
     * <span class="hljs-doctag">@param</span> groupName      组/卷名，默认值：group1
     * <span class="hljs-doctag">@param</span> remoteFileName 文件名，例如："M00/00/00/wKgKZl9tkTCAJAanAADhaCZ_RF0495.jpg"
     * <span class="hljs-doctag">@return</span> 文件的字节输入流
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> InputStream <span class="hljs-title">downloadFile</span><span class="hljs-params">(String groupName, String remoteFileName)</span> </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 根据组名和文件名通过 Storage 客户端获取文件的字节数组</span>
            <span class="hljs-keyword">byte</span>[] bytes = storageClient.download_file(groupName == <span class="hljs-keyword">null</span> ? <span class="hljs-string">"group1"</span> : groupName, remoteFileName);
            <span class="hljs-comment">// 返回字节流对象</span>
            InputStream inputStream = <span class="hljs-keyword">new</span> ByteArrayInputStream(bytes);
            <span class="hljs-keyword">return</span> inputStream;
        &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (MyException e) &#123;
            e.printStackTrace();
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;

    <span class="hljs-comment">/**
     * 文件删除
     *
     * <span class="hljs-doctag">@param</span> groupName      组/卷名，默认值：group1
     * <span class="hljs-doctag">@param</span> remoteFileName 文件名，例如："M00/00/00/wKgKZl9tkTCAJAanAADhaCZ_RF0495.jpg"
     * <span class="hljs-doctag">@return</span> 0为成功，非0为失败
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">int</span> <span class="hljs-title">deleteFile</span><span class="hljs-params">(String groupName, String remoteFileName)</span> </span>&#123;
        <span class="hljs-keyword">int</span> result = -<span class="hljs-number">1</span>;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 根据组名和文件名通过 Storage 客户端删除文件</span>
            result = storageClient.delete_file(groupName == <span class="hljs-keyword">null</span> ? <span class="hljs-string">"group1"</span> : groupName, remoteFileName);
        &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (MyException e) &#123;
            e.printStackTrace();
        &#125;
        <span class="hljs-keyword">return</span> result;
    &#125;

    <span class="hljs-comment">/**
     * 修改一个已经存在的文件
     *
     * <span class="hljs-doctag">@param</span> oldGroupName 旧组名
     * <span class="hljs-doctag">@param</span> oldFileName  旧文件名
     * <span class="hljs-doctag">@param</span> file         新文件
     * <span class="hljs-doctag">@param</span> fileName     新文件名
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> String[] modifyFile(String oldGroupName, String oldFileName, File file, String fileName) &#123;
        <span class="hljs-comment">// 先上传</span>
        String[] fileids = uploadFile(file, fileName);
        <span class="hljs-keyword">if</span> (fileids == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
        &#125;
        <span class="hljs-comment">// 再删除</span>
        <span class="hljs-keyword">int</span> delResult = deleteFile(oldGroupName, oldFileName);
        <span class="hljs-keyword">if</span> (delResult != <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
        &#125;
        <span class="hljs-keyword">return</span> fileids;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">测试</h2>
<h3 data-id="heading-5">文件上传</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 文件上传</span>
<span class="hljs-meta">@Test</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testUploadFile</span><span class="hljs-params">()</span> </span>&#123;
    String[] fileids = FastDFSClient.uploadFile(<span class="hljs-keyword">new</span> File(<span class="hljs-string">"D:/china.jpg"</span>), <span class="hljs-string">"china.jpg"</span>);
    <span class="hljs-keyword">for</span> (String fileid : fileids) &#123;
        System.out.println(<span class="hljs-string">"fileid = "</span> + fileid);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　返回值：</p>
<pre><code class="hljs language-shell copyable" lang="shell">fileid = group1
fileid = M00/00/00/wKgKZl9xMdiAcOLdAADhaCZ_RF0096.jpg
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdd87d490e694781be75ee5c0003875e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">文件详情</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 查看文件详情</span>
<span class="hljs-meta">@Test</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testGetFileInfo</span><span class="hljs-params">()</span> </span>&#123;
    FileInfo fileInfo = FastDFSClient.getFileInfo(<span class="hljs-string">"group1"</span>, <span class="hljs-string">"M00/00/00/wKgKZl9xMdiAcOLdAADhaCZ_RF0096.jpg"</span>);
    System.out.println(<span class="hljs-string">"fileInfo = "</span> + fileInfo);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　返回值：</p>
<pre><code class="hljs language-shell copyable" lang="shell">fileInfo = fetch_from_server = false, file_type = 1, source_ip_addr = 192.168.10.102, file_size = 57704, create_timestamp = 2020-09-28 08:44:08, crc32 = 645874781
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">文件元数据</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 获取文件数据</span>
<span class="hljs-meta">@Test</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testGetMetaData</span><span class="hljs-params">()</span> </span>&#123;
    NameValuePair[] metaDatas = FastDFSClient.getMetaData(<span class="hljs-string">"group1"</span>, <span class="hljs-string">"M00/00/00/wKgKZl9xMdiAcOLdAADhaCZ_RF0096.jpg"</span>);
    <span class="hljs-keyword">for</span> (NameValuePair metaData : metaDatas) &#123;
        System.out.println(metaData.getName() + <span class="hljs-string">"---"</span> + metaData.getValue());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　返回值：</p>
<pre><code class="hljs language-shell copyable" lang="shell">file_length---57704
file_name---china.jpg
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">文件下载</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 文件下载</span>
<span class="hljs-meta">@Test</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testDownloadFile</span><span class="hljs-params">()</span> </span>&#123;
    InputStream is = FastDFSClient.downloadFile(<span class="hljs-string">"group1"</span>, <span class="hljs-string">"M00/00/00/wKgKZl9xMdiAcOLdAADhaCZ_RF0096.jpg"</span>);
    <span class="hljs-keyword">try</span> (FileOutputStream fos = <span class="hljs-keyword">new</span> FileOutputStream(<span class="hljs-string">"D:/wKgKZl9xMdiAcOLdAADhaCZ_RF0096.jpg"</span>)) &#123;
        <span class="hljs-keyword">int</span> len = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">byte</span>[] bytes = <span class="hljs-keyword">new</span> <span class="hljs-keyword">byte</span>[<span class="hljs-number">1024</span>];
        <span class="hljs-keyword">while</span> ((len = is.read(bytes)) != -<span class="hljs-number">1</span>) &#123;
            fos.write(bytes, <span class="hljs-number">0</span>, len);
            fos.flush();
        &#125;
    &#125; <span class="hljs-keyword">catch</span> (FileNotFoundException e) &#123;
        e.printStackTrace();
    &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
        e.printStackTrace();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">文件删除</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 文件删除</span>
<span class="hljs-meta">@Test</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testDeleteFile</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">int</span> result = FastDFSClient.deleteFile(<span class="hljs-string">"group1"</span>, <span class="hljs-string">"M00/00/00/wKgKZl9xMdiAcOLdAADhaCZ_RF0096.jpg"</span>);
    System.out.println(<span class="hljs-string">"result = "</span> + result);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　返回值：</p>
<pre><code class="hljs language-shell copyable" lang="shell">result = 0
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">文件替换</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 文件替换</span>
<span class="hljs-meta">@Test</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testModifyFile</span><span class="hljs-params">()</span> </span>&#123;
    String[] fileids = FastDFSClient.modifyFile(<span class="hljs-string">"group1"</span>, <span class="hljs-string">"M00/00/00/wKgKZl9xOS2ASdu8AADhaCZ_RF0898.jpg"</span>,
                                                <span class="hljs-keyword">new</span> File(<span class="hljs-string">"D:/mhw.jpg"</span>), <span class="hljs-string">"mhw.jpg"</span>);
    <span class="hljs-keyword">for</span> (String fileid : fileids) &#123;
        System.out.println(<span class="hljs-string">"fileid = "</span> + fileid);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　返回值：</p>
<pre><code class="hljs language-shell copyable" lang="shell">fileid = group1
fileid = M00/00/00/wKgKZl9xOeaAFO00AACmo7QBGtA298.jpg
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed0f56f816ed42d4a04baba2feef382e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　至此 Java 客户端操作 FastDFS 实现文件上传下载替换删除等操作就到这里，下一篇我们带大家搭建 FastDFS 的集群环境，多 Tracker 多 Storage 然后通过 Nginx 代理。</p>
<p>jpg",
new File("D:/mhw.jpg"), "mhw.jpg");
for (String fileid : fileids) &#123;
System.out.println("fileid = " + fileid);
&#125;
&#125;</p>
<pre><code class="copyable">
　　返回值：

```shell
fileid = group1
fileid = M00/00/00/wKgKZl9xOeaAFO00AACmo7QBGtA298.jpg
<span class="copy-code-btn">复制代码</span></code></pre>
<p>[外链图片转存中...(img-9gDPTpcj-1622011693354)]</p>
<p>　　至此 Java 客户端操作 FastDFS 实现文件上传下载替换删除等操作就到这里，下一篇我们带大家搭建 FastDFS 的集群环境，多 Tracker 多 Storage 然后通过 Nginx 代理。（文章转载自乐字节）</p></div>  
</div>
            

---
title: 'X Spring File Storage 0.6.0 发布，新增支持 FTP、SFTP、WebDAV'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2691'
author: 开源中国
comments: false
date: Wed, 17 Aug 2022 08:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2691'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:start">简介</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#40485b">在 SpringBoot 中通过简单的方式将文件存储到 本地、</span>FTP、SFTP、WebDAV、<span style="background-color:#ffffff; color:#40485b">阿里云 OSS、华为云 OBS、七牛云 Kodo、腾讯云 COS、百度云 BOS、又拍云 USS、MinIO、 AWS S3、金山云 KS3、美团云 MSS、京东云 OSS、天翼云 OOS、移动云 EOS、沃云 OSS、 网易数帆 NOS、Ucloud US3、青云 QingStor、平安云 OBS、首云 OSS、IBM COS、其它兼容 S3 协议的平台</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">后续即将支持 谷歌云存储、Samba、NFS</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F1171736840%2Fspring-file-storage" target="_blank">https://github.com/1171736840/spring-file-storage</a><br> Gitee：<a href="https://gitee.com/XYW1171736840/spring-file-storage">https://gitee.com/XYW1171736840/spring-file-storage</a><br> 官网文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring-file-storage.xuyanwu.cn" target="_blank">https://spring-file-storage.xuyanwu.cn</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">更新日志</h3> 
<ul> 
 <li>增加对 FTP 的支持</li> 
 <li>增加对 SFTP 的支持</li> 
 <li>增加对 WebDAV 的支持</li> 
 <li>增加增强版的本地存储平台<span> </span><code>LocalPlusFileStorage</code>，建议新项目使用，老项目为了兼容性继续使用<span> </span><code>LocalFileStorage</code></li> 
 <li>优化又拍云 Uss</li> 
 <li>优化七牛云 Kodo</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">使用说明</h3> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A3000%2F%23%2F%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%3Fid%3D%25e9%2585%258d%25e7%25bd%25ae" target="_blank"><span style="color:#34495e">配置</span></a></h2> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><code>pom.xml</code>引入依赖</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependencies</span><span style="color:#525252">></span></span>
    <span style="color:#8e908c"><!-- spring-file-storage 必须要引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>cn.xuyanwu<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>spring-file-storage<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>0.5.0<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 华为云 OBS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.huaweicloud<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>esdk-obs-java<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>3.22.3.1<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 阿里云 OSS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.aliyun.oss<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>aliyun-sdk-oss<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>3.15.1<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 七牛云 Kodo 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.qiniu<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>qiniu-java-sdk<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>7.11.0<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 腾讯云 COS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.qcloud<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>cos_api<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>5.6.98<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 百度云 BOS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.baidubce<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>bce-java-sdk<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>0.10.218<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 又拍云 USS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.upyun<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>java-sdk<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>4.2.3<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- MinIO 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>io.minio<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>minio<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>8.4.3<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- AWS S3 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.amazonaws<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>aws-java-sdk-s3<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>1.12.272<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- FTP 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>commons-net<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>commons-net<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>3.8.0<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- SFTP 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.jcraft<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>jsch<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>0.1.55<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!--糊涂工具类扩展，如果要使用 FTP、SFTP 则必须引入，否则不用引入--></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>cn.hutool<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>hutool-extra<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>5.8.5<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- WebDAV 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.github.lookfirst<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>sardine<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>5.10<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependencies</span><span style="color:#525252">></span></span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><code>application.yml</code>配置文件中添加以下相关配置（不使用的平台可以不配置）</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#22a2c9">spring</span><span style="color:#525252">:</span>
  <span style="color:#22a2c9">file-storage</span><span style="color:#525252">:</span> <span style="color:#8e908c">#文件存储配置</span>
    <span style="color:#22a2c9">default-platform</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c">#默认使用的存储平台</span>
    <span style="color:#22a2c9">thumbnail-suffix</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">".min.jpg"</span> <span style="color:#8e908c">#缩略图后缀，例如【.min.jpg】【.png】</span>
    <span style="color:#22a2c9">local</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 本地存储（不推荐使用），不使用的情况下可以不写</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c">#启用存储</span>
        <span style="color:#22a2c9">enable-access</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong> <span style="color:#8e908c">#启用访问（线上请使用 Nginx 配置，效率更高）</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">""</span> <span style="color:#8e908c"># 访问域名，例如：“http://127.0.0.1:8030/test/file/”，注意后面要和 path-patterns 保持一致，“/”结尾，本地存储建议使用相对路径，方便后期更换域名</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> D<span style="color:#525252">:</span>/Temp/test/ <span style="color:#8e908c"># 存储地址</span>
        <span style="color:#22a2c9">path-patterns</span><span style="color:#525252">:</span> /test/file/<strong style="color:#c94922">**</strong> <span style="color:#8e908c"># 访问路径，开启 enable-access 后，通过此路径可以访问到上传的文件</span>
    <span style="color:#22a2c9">local-plus</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 本地存储升级版，不使用的情况下可以不写</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span>plus<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c">#启用存储</span>
        <span style="color:#22a2c9">enable-access</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong> <span style="color:#8e908c">#启用访问（线上请使用 Nginx 配置，效率更高）</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">""</span> <span style="color:#8e908c"># 访问域名，例如：“http://127.0.0.1:8030/”，注意后面要和 path-patterns 保持一致，“/”结尾，本地存储建议使用相对路径，方便后期更换域名</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span>plus/ <span style="color:#8e908c"># 基础路径</span>
        <span style="color:#22a2c9">path-patterns</span><span style="color:#525252">:</span> /<strong style="color:#c94922">**</strong> <span style="color:#8e908c"># 访问路径</span>
        <span style="color:#22a2c9">storage-path</span><span style="color:#525252">:</span> D<span style="color:#525252">:</span>/Temp/ <span style="color:#8e908c"># 存储路径</span>
    <span style="color:#22a2c9">huawei-obs</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 华为云 OBS ，不使用的情况下可以不写</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> huawei<span style="color:#525252">-</span>obs<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">false</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：http://abc.obs.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">aliyun-oss</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 阿里云 OSS ，不使用的情况下可以不写</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> aliyun<span style="color:#525252">-</span>oss<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">false</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://abc.oss-cn-shanghai.aliyuncs.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">qiniu-kodo</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 七牛云 kodo ，不使用的情况下可以不写</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> qiniu<span style="color:#525252">-</span>kodo<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">false</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：http://abc.hn-bkt.clouddn.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> base/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">tencent-cos</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 腾讯云 COS</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> tencent<span style="color:#525252">-</span>cos<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">secret-id</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">region</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c">#存仓库所在地域</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://abc.cos.ap-nanjing.myqcloud.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">baidu-bos</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 百度云 BOS</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> baidu<span style="color:#525252">-</span>bos<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 例如 abc.fsh.bcebos.com</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://abc.fsh.bcebos.com/abc/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">upyun-uss</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 又拍云 USS</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> upyun<span style="color:#525252">-</span>uss<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">username</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">password</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：http://abc.test.upcdn.net/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">minio</span><span style="color:#525252">:</span> <span style="color:#8e908c"># MinIO，由于 MinIO SDK 支持 AWS S3，其它兼容 AWS S3 协议的存储平台也都可配置在这里</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> minio<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：http://minio.abc.com/abc/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">aws-s3</span><span style="color:#525252">:</span> <span style="color:#8e908c"># AWS S3，其它兼容 AWS S3 协议的存储平台也都可配置在这里</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> aws<span style="color:#525252">-</span>s3<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">region</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 与 end-point 参数至少填一个</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 与 region 参数至少填一个</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://abc.hn-bkt.clouddn.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> s3/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">ftp</span><span style="color:#525252">:</span> <span style="color:#8e908c"># FTP</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> ftp<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">host</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 主机，例如：192.168.1.105</span>
        <span style="color:#22a2c9">port</span><span style="color:#525252">:</span> <span style="color:#c76b29">21</span> <span style="color:#8e908c"># 端口，默认21</span>
        <span style="color:#22a2c9">user</span><span style="color:#525252">:</span> anonymous <span style="color:#8e908c"># 用户名，默认 anonymous（匿名）</span>
        <span style="color:#22a2c9">password</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">""</span> <span style="color:#8e908c"># 密码，默认空</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：ftp://192.168.1.105/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> ftp/ <span style="color:#8e908c"># 基础路径</span>
        <span style="color:#22a2c9">storage-path</span><span style="color:#525252">:</span> /www/wwwroot/file.abc.com/ <span style="color:#8e908c"># 存储路径，可以配合 Nginx 实现访问，注意“/”结尾，默认“/”</span>
    <span style="color:#22a2c9">sftp</span><span style="color:#525252">:</span> <span style="color:#8e908c"># SFTP</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> sftp<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">host</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 主机，例如：192.168.1.105</span>
        <span style="color:#22a2c9">port</span><span style="color:#525252">:</span> <span style="color:#c76b29">22</span> <span style="color:#8e908c"># 端口，默认22</span>
        <span style="color:#22a2c9">user</span><span style="color:#525252">:</span> root <span style="color:#8e908c"># 用户名</span>
        <span style="color:#22a2c9">password</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 密码或私钥密码</span>
        <span style="color:#22a2c9">private-key-path</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 私钥路径，兼容Spring的ClassPath路径、文件路径、HTTP路径等，例如：classpath:id_rsa_2048</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://file.abc.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> sftp/ <span style="color:#8e908c"># 基础路径</span>
        <span style="color:#22a2c9">storage-path</span><span style="color:#525252">:</span> /www/wwwroot/file.abc.com/ <span style="color:#8e908c"># 存储路径，可以配合 Nginx 实现访问，注意“/”结尾，默认“/”</span>
    <span style="color:#22a2c9">webdav</span><span style="color:#525252">:</span> <span style="color:#8e908c"># WebDAV</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> webdav<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">server</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 服务器地址，例如：http://192.168.1.105:8405/</span>
        <span style="color:#22a2c9">user</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 用户名</span>
        <span style="color:#22a2c9">password</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 密码</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://file.abc.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> webdav/ <span style="color:#8e908c"># 基础路径</span>
        <span style="color:#22a2c9">storage-path</span><span style="color:#525252">:</span> / <span style="color:#8e908c"># 存储路径，可以配合 Nginx 实现访问，注意“/”结尾，默认“/”</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">注意配置每个平台前面都有个<code>-</code>号，通过以下方式可以配置多个</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#22a2c9">local</span><span style="color:#525252">:</span>
  <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
    <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>
    <span style="color:#22a2c9">enable-access</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>
    <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">""</span>
    <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> D<span style="color:#525252">:</span>/Temp/test/
    <span style="color:#22a2c9">path-patterns</span><span style="color:#525252">:</span> /test/file/<strong style="color:#c94922">**</strong>
  <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span><span style="color:#c76b29">2</span> <span style="color:#8e908c"># 存储平台标识，注意这里不能重复</span>
    <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>
    <span style="color:#22a2c9">enable-access</span><span style="color:#525252">:</span> <strong style="color:#c94922">true</strong>
    <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">""</span>
    <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> D<span style="color:#525252">:</span>/Temp/test2/
    <span style="color:#22a2c9">path-patterns</span><span style="color:#525252">:</span> /test2/file/<strong style="color:#c94922">**</strong></code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A3000%2F%23%2F%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%3Fid%3D%25e7%25bc%2596%25e7%25a0%2581" target="_blank"><span style="color:#34495e">编码</span></a></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">在启动类上加上<span> </span><code>@EnableFileStorage</code><span> </span>注解</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#525252"><span style="color:#032f62">@EnableFileStorage</span></span>
<span style="color:#525252"><span style="color:#032f62">@SpringBootApplication</span></span>
<span style="color:#e96900">public</span> <span style="color:#e96900">class</span> SpringFileStorageTestApplication <span style="color:#525252">&#123;</span>

    <span style="color:#e96900"><span style="color:#d73a49">public</span></span> <span style="color:#e96900"><span style="color:#d73a49">static</span></span> <span style="color:#e96900"><span style="color:#d73a49">void</span></span> <span style="color:#e96900"><span style="color:#d73a49">main</span></span><span style="color:#525252">(</span>String<span style="color:#525252">[</span><span style="color:#525252">]</span> args<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span style="color:#d73a49">SpringApplication</span><span style="color:#525252"><span style="color:#6f42c1">.</span></span><span style="color:#e96900"><span style="color:#6f42c1">run</span></span><span style="color:#525252">(</span>SpringFileStorageTestApplication<span style="color:#525252">.</span><span style="color:#e96900">class</span><span style="color:#525252">,</span> args<span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>
    
<span style="color:#525252">&#125;</span></code></pre> 
<h2 style="margin-left:.8rem; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring-file-storage.xuyanwu.cn%2F%23%2F%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%3Fid%3D%25e5%25bc%2580%25e5%25a7%258b%25e4%25bd%25bf%25e7%2594%25a8" target="_blank"><span style="color:#34495e">开始使用</span></a></h2> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#525252">@RestController</span>
<span style="color:#e96900">public</span> <span style="color:#e96900">class</span> <span>FileDetailController</span> <span style="color:#525252">&#123;</span>

    <span style="color:#525252">@Autowired</span>
    <span style="color:#e96900">private</span> <span>FileStorageService</span> fileStorageService<span style="color:#525252">;</span><span style="color:#8e908c">//注入实列</span>

    <span style="color:#8e908c">/**
     * 上传文件，成功返回文件 url
     */</span>
    <span style="color:#525252">@PostMapping</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"/upload"</span><span style="color:#525252">)</span>
    <span style="color:#e96900">public</span> <span>String</span> <span style="color:#e96900">upload</span><span style="color:#525252">(</span><span>MultipartFile</span> file<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span>FileInfo</span> fileInfo <span>=</span> fileStorageService<span style="color:#525252">.</span><span style="color:#e96900">of</span><span style="color:#525252">(</span>file<span style="color:#525252">)</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setPath</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"upload/"</span><span style="color:#525252">)</span> <span style="color:#8e908c">//保存到相对路径下，为了方便管理，不需要可以不写</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setObjectId</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"0"</span><span style="color:#525252">)</span>   <span style="color:#8e908c">//关联对象id，为了方便管理，不需要可以不写</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setObjectType</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"0"</span><span style="color:#525252">)</span> <span style="color:#8e908c">//关联对象类型，为了方便管理，不需要可以不写</span>
                <span style="color:#525252">.</span><span style="color:#e96900">putAttr</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"role"</span><span style="color:#525252">,</span><span style="color:var(--theme-color,#42b983)">"admin"</span><span style="color:#525252">)</span> <span style="color:#8e908c">//保存一些属性，可以在切面、保存上传记录、自定义存储平台等地方获取使用，不需要可以不写</span>
                <span style="color:#525252">.</span><span style="color:#e96900">upload</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>  <span style="color:#8e908c">//将文件上传到对应地方</span>
        <span style="color:#e96900">return</span> fileInfo <span>==</span> <span style="color:#e96900">null</span> <span>?</span> <span style="color:var(--theme-color,#42b983)">"上传失败！"</span> <span>:</span> fileInfo<span style="color:#525252">.</span><span style="color:#e96900">getUrl</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>

    <span style="color:#8e908c">/**
     * 上传图片，成功返回文件信息
     * 图片处理使用的是 https://github.com/coobird/thumbnailator
     */</span>
    <span style="color:#525252">@PostMapping</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"/upload-image"</span><span style="color:#525252">)</span>
    <span style="color:#e96900">public</span> <span>FileInfo</span> <span style="color:#e96900">uploadImage</span><span style="color:#525252">(</span><span>MultipartFile</span> file<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span style="color:#e96900">return</span> fileStorageService<span style="color:#525252">.</span><span style="color:#e96900">of</span><span style="color:#525252">(</span>file<span style="color:#525252">)</span>
                <span style="color:#525252">.</span><span style="color:#e96900">image</span><span style="color:#525252">(</span>img <span>-></span> img<span style="color:#525252">.</span><span style="color:#e96900">size</span><span style="color:#525252">(</span><span style="color:#c76b29">1000</span><span style="color:#525252">,</span><span style="color:#c76b29">1000</span><span style="color:#525252">)</span><span style="color:#525252">)</span>  <span style="color:#8e908c">//将图片大小调整到 1000*1000</span>
                <span style="color:#525252">.</span><span style="color:#e96900">thumbnail</span><span style="color:#525252">(</span>th <span>-></span> th<span style="color:#525252">.</span><span style="color:#e96900">size</span><span style="color:#525252">(</span><span style="color:#c76b29">200</span><span style="color:#525252">,</span><span style="color:#c76b29">200</span><span style="color:#525252">)</span><span style="color:#525252">)</span>  <span style="color:#8e908c">//再生成一张 200*200 的缩略图</span>
                <span style="color:#525252">.</span><span style="color:#e96900">upload</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>

    <span style="color:#8e908c">/**
     * 上传文件到指定存储平台，成功返回文件信息
     */</span>
    <span style="color:#525252">@PostMapping</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"/upload-platform"</span><span style="color:#525252">)</span>
    <span style="color:#e96900">public</span> <span>FileInfo</span> <span style="color:#e96900">uploadPlatform</span><span style="color:#525252">(</span><span>MultipartFile</span> file<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span style="color:#e96900">return</span> fileStorageService<span style="color:#525252">.</span><span style="color:#e96900">of</span><span style="color:#525252">(</span>file<span style="color:#525252">)</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setPlatform</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"aliyun-oss-1"</span><span style="color:#525252">)</span>    <span style="color:#8e908c">//使用指定的存储平台</span>
                <span style="color:#525252">.</span><span style="color:#e96900">upload</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>
<span style="color:#525252">&#125;</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果还想使用除了保存文件之前的其它功能，例如删除、下载等功能可以查看详细的使用文档</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F1171736840%2Fspring-file-storage" target="_blank">https://github.com/1171736840/spring-file-storage</a><br> Gitee：<a href="https://gitee.com/XYW1171736840/spring-file-storage">https://gitee.com/XYW1171736840/spring-file-storage</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官网文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring-file-storage.xuyanwu.cn" target="_blank">https://spring-file-storage.xuyanwu.cn</a></p>
                                        </div>
                                      
</div>
            
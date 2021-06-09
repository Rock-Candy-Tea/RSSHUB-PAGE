
---
title: 'X Spring File Storage 0.4.0 发布，新增支持 AWS S3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1499'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 09:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1499'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">简介</h3> 
<p style="text-align:start"><span style="background-color:#ffffff; color:#40485b">在 SpringBoot 中通过简单的方式将文件存储到 本地、阿里云OSS、华为云OBS、七牛云Kodo、腾讯云COS、百度云 BOS、又拍云USS、MinIO、 AWS S3、金山云 KS3、美团云 MSS、京东云 OSS、天翼云 OOS、移动云 EOS、沃云 OSS、 网易数帆 NOS、Ucloud US3、青云 QingStor、平安云 OBS、首云 OSS、IBM COS、其它兼容 S3 协议的平台</span></p> 
<p style="text-align:start">后续即将支持 谷歌云存储、FTP、SFTP、WebDAV、Samba、NFS</p> 
<p style="text-align:start">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F1171736840%2Fspring-file-storage" target="_blank">https://github.com/1171736840/spring-file-storage</a><br> Gitee：<a href="https://gitee.com/XYW1171736840/spring-file-storage">https://gitee.com/XYW1171736840/spring-file-storage</a><br> 官网文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring-file-storage.xuyanwu.cn" target="_blank">https://spring-file-storage.xuyanwu.cn</a></p> 
<h3 style="text-align:start">更新日志</h3> 
<p style="text-align:left">- 增加对 AWS S3 的支持</p> 
<h3 style="text-align:start">使用说明</h3> 
<h2 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A3000%2F%23%2F%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%3Fid%3D%25e9%2585%258d%25e7%25bd%25ae" target="_blank"><span style="color:#34495e">配置</span></a></h2> 
<p style="text-align:start"><code>pom.xml</code>引入依赖</p> 
<pre style="text-align:start"><code><span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependencies</span><span style="color:#525252">></span></span>
    <span style="color:#8e908c"><!-- spring-file-storage 必须要引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>cn.xuyanwu<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>spring-file-storage<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>0.4.0<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 华为云 OBS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.huaweicloud<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>esdk-obs-java<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>3.20.6.1<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 阿里云 OSS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.aliyun.oss<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>aliyun-sdk-oss<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>3.6.0<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 七牛云 Kodo 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.qiniu<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>qiniu-java-sdk<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>7.4.0<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 腾讯云 COS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.qcloud<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>cos_api<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>5.6.38<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 百度云 BOS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.baidubce<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>bce-java-sdk<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>0.10.162<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- 又拍云 USS 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.upyun<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>java-sdk<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>4.2.2<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- MinIO 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>io.minio<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>minio<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>7.0.2<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

    <span style="color:#8e908c"><!-- AWS S3 不使用的情况下可以不引入 --></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>dependency</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>groupId</span><span style="color:#525252">></span></span>com.amazonaws<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>groupId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>artifactId</span><span style="color:#525252">></span></span>aws-java-sdk-s3<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>artifactId</span><span style="color:#525252">></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><</span>version</span><span style="color:#525252">></span></span>1.11.1034<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>version</span><span style="color:#525252">></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependency</span><span style="color:#525252">></span></span>

<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"></</span>dependencies</span><span style="color:#525252">></span></span></code></pre> 
<p style="text-align:start"><code>application.yml</code>配置文件中添加以下相关配置（不使用的平台可以不配置）</p> 
<pre style="text-align:start"><code><span style="color:#22a2c9">spring</span><span style="color:#525252">:</span>
  <span style="color:#22a2c9">file-storage</span><span style="color:#525252">:</span> <span style="color:#8e908c">#文件存储配置</span>
    <span style="color:#22a2c9">default-platform</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c">#默认使用的存储平台</span>
    <span style="color:#22a2c9">thumbnail-suffix</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">".min.jpg"</span> <span style="color:#8e908c">#缩略图后缀，例如【.min.jpg】【.png】</span>
    <span style="color:#22a2c9">local</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 本地存储，不使用的情况下可以不写</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>true</strong>  <span style="color:#8e908c">#启用存储</span>
        <span style="color:#22a2c9">enable-access</span><span style="color:#525252">:</span> <strong>true</strong> <span style="color:#8e908c">#启用访问（线上请使用 Nginx 配置，效率更高）</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">""</span> <span style="color:#8e908c"># 访问域名，例如：“http://127.0.0.1:8030/test/file/”，注意后面要和 path-patterns 保持一致，“/”结尾，本地存储建议使用相对路径，方便后期更换域名</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> D<span style="color:#525252">:</span>/Temp/test/ <span style="color:#8e908c"># 存储地址</span>
        <span style="color:#22a2c9">path-patterns</span><span style="color:#525252">:</span> /test/file/<strong>**</strong> <span style="color:#8e908c"># 访问路径，开启 enable-access 后，通过此路径可以访问到上传的文件</span>
    <span style="color:#22a2c9">huawei-obs</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 华为云 OBS ，不使用的情况下可以不写</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> huawei<span style="color:#525252">-</span>obs<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>false</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：http://abc.obs.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">aliyun-oss</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 阿里云 OSS ，不使用的情况下可以不写</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> aliyun<span style="color:#525252">-</span>oss<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>false</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://abc.oss-cn-shanghai.aliyuncs.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">qiniu-kodo</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 七牛云 kodo ，不使用的情况下可以不写</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> qiniu<span style="color:#525252">-</span>kodo<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>false</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：http://abc.hn-bkt.clouddn.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> base/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">tencent-cos</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 腾讯云 COS</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> tencent<span style="color:#525252">-</span>cos<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">secret-id</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">region</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c">#存仓库所在地域</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://abc.cos.ap-nanjing.myqcloud.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">baidu-bos</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 百度云 BOS</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> baidu<span style="color:#525252">-</span>bos<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 例如 abc.fsh.bcebos.com</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://abc.fsh.bcebos.com/abc/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">upyun-uss</span><span style="color:#525252">:</span> <span style="color:#8e908c"># 又拍云 USS</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> upyun<span style="color:#525252">-</span>uss<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">username</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">password</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：http://abc.test.upcdn.net/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">minio</span><span style="color:#525252">:</span> <span style="color:#8e908c"># MinIO，由于 MinIO SDK 支持 AWS S3，其它兼容 AWS S3 协议的存储平台也都可配置在这里</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> minio<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：http://minio.abc.com/abc/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> hy/ <span style="color:#8e908c"># 基础路径</span>
    <span style="color:#22a2c9">aws-s3</span><span style="color:#525252">:</span> <span style="color:#8e908c"># AWS S3，其它兼容 AWS S3 协议的存储平台也都可配置在这里</span>
      <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> aws<span style="color:#525252">-</span>s3<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
        <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>true</strong>  <span style="color:#8e908c"># 启用存储</span>
        <span style="color:#22a2c9">access-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">secret-key</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span>
        <span style="color:#22a2c9">region</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 与 end-point 参数至少填一个</span>
        <span style="color:#22a2c9">end-point</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 与 region 参数至少填一个</span>
        <span style="color:#22a2c9">bucket-name</span><span style="color:#525252">:</span> ？？
        <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:#525252">?</span><span style="color:#525252">?</span> <span style="color:#8e908c"># 访问域名，注意“/”结尾，例如：https://abc.hn-bkt.clouddn.com/</span>
        <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> s3/ <span style="color:#8e908c"># 基础路径</span></code></pre> 
<p style="text-align:start">注意配置每个平台前面都有个<code>-</code>号，通过以下方式可以配置多个</p> 
<pre style="text-align:start"><code><span style="color:#22a2c9">local</span><span style="color:#525252">:</span>
  <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span><span style="color:#c76b29">1</span> <span style="color:#8e908c"># 存储平台标识</span>
    <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>true</strong>
    <span style="color:#22a2c9">enable-access</span><span style="color:#525252">:</span> <strong>true</strong>
    <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">""</span>
    <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> D<span style="color:#525252">:</span>/Temp/test/
    <span style="color:#22a2c9">path-patterns</span><span style="color:#525252">:</span> /test/file/<strong>**</strong>
  <span style="color:#525252">-</span> <span style="color:#22a2c9">platform</span><span style="color:#525252">:</span> local<span style="color:#525252">-</span><span style="color:#c76b29">2</span> <span style="color:#8e908c"># 存储平台标识，注意这里不能重复</span>
    <span style="color:#22a2c9">enable-storage</span><span style="color:#525252">:</span> <strong>true</strong>
    <span style="color:#22a2c9">enable-access</span><span style="color:#525252">:</span> <strong>true</strong>
    <span style="color:#22a2c9">domain</span><span style="color:#525252">:</span> <span style="color:var(--theme-color,#42b983)">""</span>
    <span style="color:#22a2c9">base-path</span><span style="color:#525252">:</span> D<span style="color:#525252">:</span>/Temp/test2/
    <span style="color:#22a2c9">path-patterns</span><span style="color:#525252">:</span> /test2/file/<strong>**</strong></code></pre> 
<h2 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A3000%2F%23%2F%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%3Fid%3D%25e7%25bc%2596%25e7%25a0%2581" target="_blank"><span style="color:#34495e">编码</span></a></h2> 
<p style="text-align:start">在启动类上加上<code>@EnableFileStorage</code>注解</p> 
<pre style="text-align:start"><code><span style="color:#525252">@EnableFileStorage</span>
<span style="color:#525252">@SpringBootApplication</span>
<span style="color:#e96900">public</span> <span style="color:#e96900">class</span> SpringFileStorageTestApplication <span style="color:#525252">&#123;</span>

    <span style="color:#e96900">public</span> <span style="color:#e96900">static</span> <span style="color:#e96900">void</span> <span style="color:#e96900">main</span><span style="color:#525252">(</span>String<span style="color:#525252">[</span><span style="color:#525252">]</span> args<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        SpringApplication<span style="color:#525252">.</span><span style="color:#e96900">run</span><span style="color:#525252">(</span>SpringFileStorageTestApplication<span style="color:#525252">.</span><span style="color:#e96900">class</span><span style="color:#525252">,</span> args<span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>
    
<span style="color:#525252">&#125;</span></code></pre> 
<h2 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A3000%2F%23%2F%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%3Fid%3D%25e5%25bc%2580%25e5%25a7%258b%25e4%25bd%25bf%25e7%2594%25a8" target="_blank"><span style="color:#34495e">开始使用</span></a></h2> 
<pre style="text-align:start"><code>
<span style="color:#525252">@RestController</span>
<span style="color:#e96900">public</span> <span style="color:#e96900">class</span> FileDetailController <span style="color:#525252">&#123;</span>

    <span style="color:#525252">@Autowired</span>
    <span style="color:#e96900">private</span> FileStorageService fileStorageService<span style="color:#525252">;</span><span style="color:#8e908c">//注入实列</span>

    <span style="color:#8e908c">/**
     * 上传文件，成功返回文件 url
     */</span>
    <span style="color:#525252">@PostMapping</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"/upload"</span><span style="color:#525252">)</span>
    <span style="color:#e96900">public</span> String <span style="color:#e96900">upload</span><span style="color:#525252">(</span>MultipartFile file<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        FileInfo fileInfo = fileStorageService<span style="color:#525252">.</span><span style="color:#e96900">of</span><span style="color:#525252">(</span>file<span style="color:#525252">)</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setPath</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"upload/"</span><span style="color:#525252">)</span> <span style="color:#8e908c">//保存到相对路径下，为了方便管理，不需要可以不写</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setObjectId</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"0"</span><span style="color:#525252">)</span>   <span style="color:#8e908c">//关联对象id，为了方便管理，不需要可以不写</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setObjectType</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"0"</span><span style="color:#525252">)</span> <span style="color:#8e908c">//关联对象类型，为了方便管理，不需要可以不写</span>
                <span style="color:#525252">.</span><span style="color:#e96900">upload</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>  <span style="color:#8e908c">//将文件上传到对应地方</span>
        <span style="color:#e96900">return</span> fileInfo == <span style="color:#e96900">null</span> ? <span style="color:var(--theme-color,#42b983)">"上传失败！"</span> : fileInfo<span style="color:#525252">.</span><span style="color:#e96900">getUrl</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>

    <span style="color:#8e908c">/**
     * 上传图片，成功返回文件信息
     * 图片处理使用的是 https://github.com/coobird/thumbnailator
     */</span>
    <span style="color:#525252">@PostMapping</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"/upload-image"</span><span style="color:#525252">)</span>
    <span style="color:#e96900">public</span> FileInfo <span style="color:#e96900">uploadImage</span><span style="color:#525252">(</span>MultipartFile file<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span style="color:#e96900">return</span> fileStorageService<span style="color:#525252">.</span><span style="color:#e96900">of</span><span style="color:#525252">(</span>file<span style="color:#525252">)</span>
                <span style="color:#525252">.</span><span style="color:#e96900">image</span><span style="color:#525252">(</span>img -> img<span style="color:#525252">.</span><span style="color:#e96900">size</span><span style="color:#525252">(</span><span style="color:#c76b29">1000</span><span style="color:#525252">,</span><span style="color:#c76b29">1000</span><span style="color:#525252">)</span><span style="color:#525252">)</span>  <span style="color:#8e908c">//将图片大小调整到 1000*1000</span>
                <span style="color:#525252">.</span><span style="color:#e96900">thumbnail</span><span style="color:#525252">(</span>th -> th<span style="color:#525252">.</span><span style="color:#e96900">size</span><span style="color:#525252">(</span><span style="color:#c76b29">200</span><span style="color:#525252">,</span><span style="color:#c76b29">200</span><span style="color:#525252">)</span><span style="color:#525252">)</span>  <span style="color:#8e908c">//再生成一张 200*200 的缩略图</span>
                <span style="color:#525252">.</span><span style="color:#e96900">upload</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>

    <span style="color:#8e908c">/**
     * 上传文件到指定存储平台，成功返回文件信息
     */</span>
    <span style="color:#525252">@PostMapping</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"/upload-platform"</span><span style="color:#525252">)</span>
    <span style="color:#e96900">public</span> FileInfo <span style="color:#e96900">uploadPlatform</span><span style="color:#525252">(</span>MultipartFile file<span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span style="color:#e96900">return</span> fileStorageService<span style="color:#525252">.</span><span style="color:#e96900">of</span><span style="color:#525252">(</span>file<span style="color:#525252">)</span>
                <span style="color:#525252">.</span><span style="color:#e96900">setPlatform</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"aliyun-oss-1"</span><span style="color:#525252">)</span>    <span style="color:#8e908c">//使用指定的存储平台</span>
                <span style="color:#525252">.</span><span style="color:#e96900">upload</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>
<span style="color:#525252">&#125;</span></code></pre> 
<p style="text-align:start">如果还想使用除了保存文件之前的其它功能，例如删除、下载等功能可以查看详细的使用文档</p> 
<p style="text-align:start">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F1171736840%2Fspring-file-storage" target="_blank">https://github.com/1171736840/spring-file-storage</a><br> Gitee：<a href="https://gitee.com/XYW1171736840/spring-file-storage">https://gitee.com/XYW1171736840/spring-file-storage</a></p> 
<p style="text-align:left">官网文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring-file-storage.xuyanwu.cn" target="_blank">https://spring-file-storage.xuyanwu.cn</a></p>
                                        </div>
                                      
</div>
            
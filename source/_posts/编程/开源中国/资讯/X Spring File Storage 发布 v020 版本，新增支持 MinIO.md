
---
title: 'X Spring File Storage 发布 v0.2.0 版本，新增支持 MinIO'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6807'
author: 开源中国
comments: false
date: Tue, 25 May 2021 14:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6807'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">简介</h3> 
<p style="text-align:start">在SpringBoot中通过简单的方式将文件存储到本地、阿里云OSS、华为云OBS、七牛云Kodo、腾讯云COS、百度云 BOS、又拍云USS、MinIO</p> 
<p style="text-align:start">后续即将支持 亚马逊S3、谷歌云存储、FTP、SFTP、WebDAV、Samba、NFS</p> 
<p style="text-align:start">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F1171736840%2Fspring-file-storage" target="_blank">https://github.com/1171736840/spring-file-storage</a><br> Gitee：<a href="https://gitee.com/XYW1171736840/spring-file-storage">https://gitee.com/XYW1171736840/spring-file-storage</a></p> 
<h3 style="text-align:start">使用说明</h3> 
<h4 style="text-align:start">配置</h4> 
<p style="text-align:start"><code>pom.xml</code>引入依赖</p> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependencies</span>>
    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)"><!--</span> spring-file-storage 必须要引入 <span style="color:var(--color-prettylights-syntax-comment)">--></span></span>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>cn.xuyanwu</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>spring-file-storage</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>0.2.0</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
    </<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)"><!--</span> 华为云 OBS 不使用的情况下可以不引入 <span style="color:var(--color-prettylights-syntax-comment)">--></span></span>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.huaweicloud</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>esdk-obs-java</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>3.20.6.1</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
    </<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)"><!--</span> 阿里云 OSS 不使用的情况下可以不引入 <span style="color:var(--color-prettylights-syntax-comment)">--></span></span>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.aliyun.oss</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>aliyun-sdk-oss</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>3.6.0</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
    </<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)"><!--</span> 七牛云 Kodo 不使用的情况下可以不引入 <span style="color:var(--color-prettylights-syntax-comment)">--></span></span>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.qiniu</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>qiniu-java-sdk</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>7.4.0</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
    </<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)"><!--</span> 腾讯云 COS 不使用的情况下可以不引入 <span style="color:var(--color-prettylights-syntax-comment)">--></span></span>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.qcloud</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>cos_api</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>5.6.38</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
    </<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)"><!--</span> 百度云 BOS 不使用的情况下可以不引入 <span style="color:var(--color-prettylights-syntax-comment)">--></span></span>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.baidubce</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>bce-java-sdk</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>0.10.162</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
    </<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)"><!--</span> 又拍云 USS 不使用的情况下可以不引入 <span style="color:var(--color-prettylights-syntax-comment)">--></span></span>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.upyun</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>java-sdk</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>4.2.2</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
    </<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)"><!--</span> MinIO 不使用的情况下可以不引入 <span style="color:var(--color-prettylights-syntax-comment)">--></span></span>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>io.minio</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>minio</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
        <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>7.0.2</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
    </<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>

</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependencies</span>></pre> 
</div> 
<p style="text-align:start"><code>application.yml</code>配置文件中添加以下相关配置（不使用的平台可以不配置）</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-entity-tag)">spring</span>:
  <span style="color:var(--color-prettylights-syntax-entity-tag)">file-storage</span>: <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span>文件存储配置</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">default-platform</span>: <span style="color:var(--color-prettylights-syntax-string)">local-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span>默认使用的存储平台</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">thumbnail-suffix</span>: <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>.min.jpg<span style="color:var(--color-prettylights-syntax-string)">"</span></span> <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span>缩略图后缀，例如【.min.jpg】【.png】</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">local</span>: <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 本地存储，不使用的情况下可以不写</span>
      - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">local-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-string)">true  </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span>启用存储</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-access</span>: <span style="color:var(--color-prettylights-syntax-string)">true </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span>启用访问（线上请使用 Nginx 配置，效率更高）</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span><span style="color:var(--color-prettylights-syntax-string)">"</span></span> <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 访问域名，例如：“http://127.0.0.1:8030/test/file/”，注意后面要和 path-patterns 保持一致，“/”结尾，本地存储建议使用相对路径，方便后期更换域名</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">D:/Temp/test/ </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储地址</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">path-patterns</span>: <span style="color:var(--color-prettylights-syntax-string)">/test/file/** </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 访问路径，开启 enable-access 后，通过此路径可以访问到上传的文件</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">huawei-obs</span>: <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 华为云 OBS ，不使用的情况下可以不写</span>
      - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">huawei-obs-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-string)">false  </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 启用存储</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">access-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">secret-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">end-point</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">bucket-name</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)">?? </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 访问域名，注意“/”结尾，例如：http://abc.obs.com/</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">hy/ </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 基础路径</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">aliyun-oss</span>: <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 阿里云 OSS ，不使用的情况下可以不写</span>
      - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">aliyun-oss-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-string)">false  </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 启用存储</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">access-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">secret-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">end-point</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">bucket-name</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)">?? </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 访问域名，注意“/”结尾，例如：https://abc.oss-cn-shanghai.aliyuncs.com/</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">hy/ </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 基础路径</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">qiniu-kodo</span>: <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 七牛云 kodo ，不使用的情况下可以不写</span>
      - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">qiniu-kodo-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-string)">false  </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 启用存储</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">access-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">secret-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">bucket-name</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)">?? </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 访问域名，注意“/”结尾，例如：http://abc.hn-bkt.clouddn.com/</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">base/ </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 基础路径</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">tencent-cos</span>: <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 腾讯云 COS</span>
      - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">tencent-cos-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-string)">true  </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 启用存储</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">secret-id</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">secret-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">region</span>: <span style="color:var(--color-prettylights-syntax-string)">?? </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span>存仓库所在地域</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">bucket-name</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)">?? </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 访问域名，注意“/”结尾，例如：https://abc.cos.ap-nanjing.myqcloud.com/</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">hy/ </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 基础路径</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">baidu-bos</span>: <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 百度云 BOS</span>
      - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">baidu-bos-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-string)">true  </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 启用存储</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">access-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">secret-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">end-point</span>: <span style="color:var(--color-prettylights-syntax-string)">?? </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 例如 abc.fsh.bcebos.com</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">bucket-name</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)">?? </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 访问域名，注意“/”结尾，例如：https://abc.fsh.bcebos.com/abc/</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">hy/ </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 基础路径</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">upyun-uss</span>: <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 又拍云 USS</span>
      - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">upyun-uss-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-string)">true  </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 启用存储</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">username</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">password</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">bucket-name</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)">?? </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 访问域名，注意“/”结尾，例如：http://abc.test.upcdn.net/</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">hy/ </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 基础路径</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">minio</span>: <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> MinIO</span>
      - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">minio-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-string)">true  </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 启用存储</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">access-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">secret-key</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">end-point</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">bucket-name</span>: <span style="color:var(--color-prettylights-syntax-string)">??</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)">?? </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 访问域名，注意“/”结尾，例如：http://minio.abc.com/abc/</span>
        <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">hy/ </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 基础路径</span></pre> 
</div> 
<p style="text-align:start">注意配置每个平台前面都有个<code>-</code>号，通过以下方式可以配置多个</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-entity-tag)">local</span>:
  - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">local-1 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-access</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span><span style="color:var(--color-prettylights-syntax-string)">"</span></span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">D:/Temp/test/</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">path-patterns</span>: <span style="color:var(--color-prettylights-syntax-string)">/test/file/**</span>
  - <span style="color:var(--color-prettylights-syntax-entity-tag)">platform</span>: <span style="color:var(--color-prettylights-syntax-string)">local-2 </span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 存储平台标识，注意这里不能重复</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-storage</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">enable-access</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">domain</span>: <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span><span style="color:var(--color-prettylights-syntax-string)">"</span></span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">base-path</span>: <span style="color:var(--color-prettylights-syntax-string)">D:/Temp/test2/</span>
    <span style="color:var(--color-prettylights-syntax-entity-tag)">path-patterns</span>: <span style="color:var(--color-prettylights-syntax-string)">/test2/file/**</span></pre> 
</div> 
<h4 style="text-align:start">编码</h4> 
<p style="text-align:start">在启动类上加上<code>@EnableFileStorage</code>注解</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">@EnableFileStorage</span>
<span style="color:var(--color-prettylights-syntax-keyword)">@SpringBootApplication</span>
<span style="color:var(--color-prettylights-syntax-keyword)">public</span> <span style="color:var(--color-prettylights-syntax-keyword)">class</span> <span style="color:var(--color-prettylights-syntax-entity)">SpringFileStorageTestApplication</span> &#123;

<span style="color:var(--color-prettylights-syntax-keyword)">public</span> <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-keyword)">void</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>(<span style="color:var(--color-prettylights-syntax-keyword)">String</span>[] <span style="color:var(--color-prettylights-syntax-variable)">args</span>) &#123;
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">SpringApplication</span><span style="color:var(--color-prettylights-syntax-keyword)">.</span>run(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">SpringFileStorageTestApplication</span><span style="color:var(--color-prettylights-syntax-keyword)">.</span>class, args);
&#125;

&#125;</pre> 
</div> 
<h4 style="text-align:start">开始使用</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">@RestController</span>
<span style="color:var(--color-prettylights-syntax-keyword)">public</span> <span style="color:var(--color-prettylights-syntax-keyword)">class</span> <span style="color:var(--color-prettylights-syntax-entity)">FileDetailController</span> &#123;

    <span style="color:var(--color-prettylights-syntax-keyword)">@Autowired</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">private</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">FileStorageService</span> fileStorageService;<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">//</span>注入实列</span>

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">/**</span></span>
<span style="color:var(--color-prettylights-syntax-comment)">     * 上传文件，成功返回文件 url</span>
<span style="color:var(--color-prettylights-syntax-comment)">     <span style="color:var(--color-prettylights-syntax-comment)">*/</span></span>
    <span style="color:var(--color-prettylights-syntax-keyword)">@PostMapping</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>/upload<span style="color:var(--color-prettylights-syntax-string)">"</span></span>)
    <span style="color:var(--color-prettylights-syntax-keyword)">public</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span style="color:var(--color-prettylights-syntax-entity)">upload</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">MultipartFile</span> <span style="color:var(--color-prettylights-syntax-variable)">file</span>) &#123;
        <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">FileInfo</span> fileInfo <span style="color:var(--color-prettylights-syntax-keyword)">=</span> fileStorageService<span style="color:var(--color-prettylights-syntax-keyword)">.</span>of(file)
                .setPath(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>upload/<span style="color:var(--color-prettylights-syntax-string)">"</span></span>) <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">//</span>保存到相对路径下，为了方便管理，不需要可以不写</span>
                .setObjectId(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>0<span style="color:var(--color-prettylights-syntax-string)">"</span></span>)   <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">//</span>关联对象id，为了方便管理，不需要可以不写</span>
                .setObjectType(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>0<span style="color:var(--color-prettylights-syntax-string)">"</span></span>) <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">//</span>关联对象类型，为了方便管理，不需要可以不写</span>
                .upload();  <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">//</span>将文件上传到对应地方</span>
        <span style="color:var(--color-prettylights-syntax-keyword)">return</span> fileInfo <span style="color:var(--color-prettylights-syntax-keyword)">==</span> <span style="color:var(--color-prettylights-syntax-constant)">null</span> <span style="color:var(--color-prettylights-syntax-keyword)">?</span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>上传失败！<span style="color:var(--color-prettylights-syntax-string)">"</span></span> <span style="color:var(--color-prettylights-syntax-keyword)">:</span> fileInfo<span style="color:var(--color-prettylights-syntax-keyword)">.</span>getUrl();
    &#125;

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">/**</span></span>
<span style="color:var(--color-prettylights-syntax-comment)">     * 上传图片，成功返回文件信息</span>
<span style="color:var(--color-prettylights-syntax-comment)">     * 图片处理使用的是 https://github.com/coobird/thumbnailator</span>
<span style="color:var(--color-prettylights-syntax-comment)">     <span style="color:var(--color-prettylights-syntax-comment)">*/</span></span>
    <span style="color:var(--color-prettylights-syntax-keyword)">@PostMapping</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>/upload-image<span style="color:var(--color-prettylights-syntax-string)">"</span></span>)
    <span style="color:var(--color-prettylights-syntax-keyword)">public</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">FileInfo</span> <span style="color:var(--color-prettylights-syntax-entity)">uploadImage</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">MultipartFile</span> <span style="color:var(--color-prettylights-syntax-variable)">file</span>) &#123;
        <span style="color:var(--color-prettylights-syntax-keyword)">return</span> fileStorageService<span style="color:var(--color-prettylights-syntax-keyword)">.</span>of(file)
                .image(img <span style="color:var(--color-prettylights-syntax-keyword)">-</span><span style="color:var(--color-prettylights-syntax-keyword)">></span> img<span style="color:var(--color-prettylights-syntax-keyword)">.</span>size(<span style="color:var(--color-prettylights-syntax-constant)">1000</span>,<span style="color:var(--color-prettylights-syntax-constant)">1000</span>))  <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">//</span>将图片大小调整到 1000*1000</span>
                .thumbnail(th <span style="color:var(--color-prettylights-syntax-keyword)">-</span><span style="color:var(--color-prettylights-syntax-keyword)">></span> th<span style="color:var(--color-prettylights-syntax-keyword)">.</span>size(<span style="color:var(--color-prettylights-syntax-constant)">200</span>,<span style="color:var(--color-prettylights-syntax-constant)">200</span>))  <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">//</span>再生成一张 200*200 的缩略图</span>
                .upload();
    &#125;

    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">/**</span></span>
<span style="color:var(--color-prettylights-syntax-comment)">     * 上传文件到指定存储平台，成功返回文件信息</span>
<span style="color:var(--color-prettylights-syntax-comment)">     <span style="color:var(--color-prettylights-syntax-comment)">*/</span></span>
    <span style="color:var(--color-prettylights-syntax-keyword)">@PostMapping</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>/upload-platform<span style="color:var(--color-prettylights-syntax-string)">"</span></span>)
    <span style="color:var(--color-prettylights-syntax-keyword)">public</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">FileInfo</span> <span style="color:var(--color-prettylights-syntax-entity)">uploadPlatform</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">MultipartFile</span> <span style="color:var(--color-prettylights-syntax-variable)">file</span>) &#123;
        <span style="color:var(--color-prettylights-syntax-keyword)">return</span> fileStorageService<span style="color:var(--color-prettylights-syntax-keyword)">.</span>of(file)
                .setPlatform(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>aliyun-oss-1<span style="color:var(--color-prettylights-syntax-string)">"</span></span>)    <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">//</span>使用指定的存储平台</span>
                .upload();
    &#125;
&#125;</pre> 
</div> 
<p style="text-align:start">如果还想使用除了保存文件之前的其它功能，例如删除、下载等功能可以查看详细的使用文档</p> 
<p style="text-align:start">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F1171736840%2Fspring-file-storage" target="_blank">https://github.com/1171736840/spring-file-storage</a><br> Gitee：<a href="https://gitee.com/XYW1171736840/spring-file-storage">https://gitee.com/XYW1171736840/spring-file-storage</a></p>
                                        </div>
                                      
</div>
            
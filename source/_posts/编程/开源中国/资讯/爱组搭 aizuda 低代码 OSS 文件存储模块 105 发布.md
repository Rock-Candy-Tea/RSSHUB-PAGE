
---
title: '爱组搭 aizuda 低代码 OSS 文件存储模块 1.0.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=66'
author: 开源中国
comments: false
date: Fri, 26 Aug 2022 18:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=66'
---

<div>   
<div class="content">
                                                                                            <p>爱组搭 aizuda-oss 文件存储模块 1.0.5 发布，新增支持腾讯云 TencentCos</p> 
<p>支持文件类型合法校验</p> 
<pre><code>OSS.fileStorage(platform).bucket(bucketName)
                        // 使用默认 yml 配置媒体类型
                        .allowMediaType(bis)
                        // 只允许gif图片上传,所有图片可以是 image/ 部分匹配
                        .allowMediaType(fis, t -> t.startsWith("image/gif"))
                        .upload(bis, filename);</code></pre> 
<p>最新源码已经适配 amazon aws s3 更多尽快支持期待</p> 
<p>目前支持 Minio  ，阿里云 OSS ，腾讯COS ，亚马逊 AWSS3 ，本地存储</p> 
<p>源码地址： <a href="https://gitee.com/aizuda/aizuda-components">https://gitee.com/aizuda/aizuda-components</a></p> 
<p>仓库地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsearch.maven.org%2Fsearch%3Fq%3Daizuda-oss" target="_blank">https://search.maven.org/search?q=aizuda-oss</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Faizuda.com%2Fpages%2F40d5c3" target="_blank">文档地址 http://aizuda.com/pages/40d5c3</a></p> 
<div style="text-align:start"> 
 <div> 
  <h2 style="margin-left:0; margin-right:0">SpringBoot 使用</h2> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li>application.yml 配置</li> 
  </ul> 
  <div> 
   <pre style="margin-left:20px; margin-right:0; text-align:left"><code><span style="color:#6a737d"># 配置存储平台 ，第一位 test-minio 为默认存储平台</span>
<span style="color:#6f42c1">aizuda:</span>
  <span style="color:#6f42c1">oss:</span>
    <span style="color:#6f42c1">test-minio:</span>
      <span style="color:#6f42c1">platform:</span> <span style="color:#032f62">minio</span>
      <span style="color:#6f42c1">endpoint:</span> <span style="color:#032f62">http://xxxxxx</span>
      <span style="color:#6f42c1">accessKey:</span> <span style="color:#032f62">xxx</span>
      <span style="color:#6f42c1">secretKey:</span> <span style="color:#032f62">xxxxxxx</span>
      <span style="color:#6f42c1">bucketName:</span> <span style="color:#032f62">test1</span>
    <span style="color:#6f42c1">aliyun-oss:</span>
      <span style="color:#6f42c1">platform:</span> <span style="color:#032f62">aliyun</span>
      <span style="color:#6f42c1">endpoint:</span> <span style="color:#032f62">http://xxxxxx</span>
      <span style="color:#6f42c1">accessKey:</span> <span style="color:#032f62">xxx</span>
      <span style="color:#6f42c1">secretKey:</span> <span style="color:#032f62">xxxxxxx</span>
      <span style="color:#6f42c1">bucketName:</span> <span style="color:#032f62">test</span>
</code></pre> 
  </div> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li>Bean 方式注入，以下注入 minio3 为平台别名</li> 
  </ul> 
  <div> 
   <pre style="margin-left:20px; margin-right:0; text-align:left"><code><span style="color:#999999"><span style="color:#6a737d">@Bean</span></span>
<span style="color:#0077aa"><span><span style="color:#d73a49">public</span></span></span><span> </span><span style="color:#dd4a68"><span>IFileStorage</span></span><span> </span><span style="color:#dd4a68"><span><span style="color:#6f42c1">minio3</span></span></span><span style="color:#999999"><span><span>(</span></span></span><span style="color:#999999"><span><span>)</span></span></span><span> </span><span style="color:#999999">&#123;</span>
    <span style="color:#708090"><span style="color:#6a737d">// 注入一个自定义存储平台</span></span>
    <span style="color:#dd4a68">OssProperty</span> ossProperty <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> <span style="color:#0077aa"><span style="color:#d73a49">new</span></span> <span style="color:#dd4a68">OssProperty</span><span style="color:#999999">(</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setPlatform</span><span style="color:#999999">(</span><span style="color:#dd4a68">StoragePlatform</span><span style="color:#999999">.</span>minio<span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setBucketName</span><span style="color:#999999">(</span><span style="color:#669900"><span style="color:#032f62">"test3"</span></span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setEndpoint</span><span style="color:#999999">(</span><span style="color:#669900"><span style="color:#032f62">"http://xxxxx"</span></span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setAccessKey</span><span style="color:#999999">(</span><span style="color:#669900"><span style="color:#032f62">"q7RNi6elbvQ0j1ry"</span></span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setSecretKey</span><span style="color:#999999">(</span><span style="color:#669900"><span style="color:#032f62">"HMoKkeu0zGSvSdDGWlMDuytaRON12St9"</span></span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    <span style="color:#0077aa"><span style="color:#d73a49">return</span></span> <span style="color:#0077aa"><span style="color:#d73a49">new</span></span> <span style="color:#dd4a68">Minio</span><span style="color:#999999">(</span>ossProperty<span style="color:#999999">)</span><span style="color:#999999">;</span>
<span style="color:#999999">&#125;</span>
</code></pre> 
  </div> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li>测试上传 platform 存储平台（不设置使用默认）bucketName 存储桶（不设置使用默认）</li> 
  </ul> 
  <div> 
   <pre style="margin-left:20px; margin-right:0; text-align:left"><code><span style="color:#6a737d">// 静态方法方式调用</span>
<span style="color:#d73a49">OSS</span><span style="color:#6f42c1">.fileStorage</span>(platform)<span style="color:#6f42c1">.bucket</span>(bucketName)<span style="color:#6f42c1">.upload</span>(fis, filename);

<span style="color:#6a737d">// 依赖注入方式调用</span>
<span style="color:#d73a49">fileStorage</span><span style="color:#6f42c1">.bucket</span>(bucketName)<span style="color:#6f42c1">.upload</span>(fis, filename);
</code></pre> 
  </div> 
  <h1 style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Faizuda.com%2Fpages%2F40d5c3%2F%23ifilestorage-%25E6%2596%25B9%25E6%25B3%2595%25E8%25AF%25B4%25E6%2598%258E" target="_blank">#</a>IFileStorage 方法说明</h1> 
  <table cellspacing="0" style="border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:inline-table; font-size:14px; line-height:inherit; margin:1rem 0px; max-width:100%; overflow:auto; width:auto; word-break:keep-all"> 
   <thead> 
    <tr> 
     <th>属性</th> 
     <th>说明</th> 
    </tr> 
   </thead> 
   <tbody> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">upload</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">上传</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">delete</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">删除</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">download</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">下载</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">getUrl</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">文件可预览地址</td> 
    </tr> 
   </tbody> 
  </table> 
  <h1 style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Faizuda.com%2Fpages%2F40d5c3%2F%23%25E9%2585%258D%25E7%25BD%25AE%25E5%25B1%259E%25E6%2580%25A7%25E8%25AF%25B4%25E6%2598%258E" target="_blank">#</a>配置属性说明</h1> 
  <table cellspacing="0" style="border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:inline-table; font-size:14px; line-height:inherit; margin:1rem 0px; max-width:100%; overflow:auto; width:auto; word-break:keep-all"> 
   <thead> 
    <tr> 
     <th>属性</th> 
     <th>说明</th> 
    </tr> 
   </thead> 
   <tbody> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">platform</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">存储平台，目前支持 Minio  ，阿里云 OSS ，腾讯COS ，亚马逊 AWSS3 ，本地存储</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">endpoint</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">域名</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">accessKey</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">访问 KEY</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">secretKey</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">密钥</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">bucketName</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">存储空间桶名</td> 
    </tr> 
    <tr> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">connectionTimeout</td> 
     <td style="border-color:#dddddd; border-style:solid; border-width:1px">连接超时，阿里云 OSS 有效</td> 
    </tr> 
   </tbody> 
  </table> 
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            
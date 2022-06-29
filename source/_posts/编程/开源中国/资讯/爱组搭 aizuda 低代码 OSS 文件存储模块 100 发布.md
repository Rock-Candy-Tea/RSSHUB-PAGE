
---
title: '爱组搭 aizuda 低代码 OSS 文件存储模块 1.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100'
author: 开源中国
comments: false
date: Tue, 28 Jun 2022 22:30:00 GMT
thumbnail: 'https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100'
---

<div>   
<div class="content">
                                                                                            <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="logo" src="https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">爱组搭  =  选择你喜欢的 + 组件 + 搭配 = 架构搞定</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">爱组搭～低代码组件化开发平台之组件库</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">愿景：每个人都是架构师</p> </li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/aizuda/aizuda-components-examples">爱组搭～组件源码示例演示</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">模块介绍</h1> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">主要功能 文件对象存储 支持选择使用不同存储方式，也可以同时使用多种存储方式。</p> 
</blockquote> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Faizuda.com%2Fpages%2F40d5c3" target="_blank">文档地址 http://aizuda.com/pages/40d5c3</a></p> 
<div style="text-align:start"> 
 <div> 
  <h2>SpringBoot使用</h2> 
  <ul> 
   <li>application.yml 配置</li> 
  </ul> 
  <div> 
   <pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code># 配置存储平台 ，第一位 test-minio 为默认存储平台
aizuda:
  oss:
    test-minio:
      platform: minio
      endpoint: http://xxxxxx
      accessKey: xxx
      secretKey: xxxxxxx
      bucketName: test1
    aliyun-oss:
      platform: aliyun
      endpoint: http://xxxxxx
      accessKey: xxx
      secretKey: xxxxxxx
      bucketName: test
</code></pre> 
  </div> 
  <ul> 
   <li>Bean 方式注入，以下注入 minio3 为平台别名</li> 
  </ul> 
  <div> 
   <pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code><span style="color:#999999">@Bean</span>
<span style="color:#0077aa">public</span> <span style="color:#dd4a68">IFileStorage</span> <span style="color:#dd4a68">minio3</span><span style="color:#999999">(</span><span style="color:#999999">)</span> <span style="color:#999999">&#123;</span>
    <span style="color:#708090">// 注入一个自定义存储平台</span>
    <span style="color:#dd4a68">OssProperty</span> ossProperty <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> <span style="color:#0077aa">new</span> <span style="color:#dd4a68">OssProperty</span><span style="color:#999999">(</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setPlatform</span><span style="color:#999999">(</span><span style="color:#dd4a68">StoragePlatform</span><span style="color:#999999">.</span>minio<span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setBucketName</span><span style="color:#999999">(</span><span style="color:#669900">"test3"</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setEndpoint</span><span style="color:#999999">(</span><span style="color:#669900">"http://xxxxx"</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setAccessKey</span><span style="color:#999999">(</span><span style="color:#669900">"q7RNi6elbvQ0j1ry"</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    ossProperty<span style="color:#999999">.</span><span style="color:#dd4a68">setSecretKey</span><span style="color:#999999">(</span><span style="color:#669900">"HMoKkeu0zGSvSdDGWlMDuytaRON12St9"</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    <span style="color:#0077aa">return</span> <span style="color:#0077aa">new</span> <span style="color:#dd4a68">Minio</span><span style="color:#999999">(</span>ossProperty<span style="color:#999999">)</span><span style="color:#999999">;</span>
<span style="color:#999999">&#125;</span>
</code></pre> 
  </div> 
  <ul> 
   <li>测试上传 platform 存储平台（不设置使用默认）bucketName 存储桶（不设置使用默认）</li> 
  </ul> 
  <div> 
   <pre style="margin-left:.85rem; margin-right:.85rem; text-align:left"><code>// 静态方法方式调用
OSS.fileStorage(platform).bucket(bucketName).upload(fis, filename);

// 依赖注入方式调用
fileStorage.bucket(bucketName).upload(fis, filename);
</code></pre> 
  </div> 
  <h1><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Faizuda.com%2Fpages%2F40d5c3%2F%23ifilestorage-%25E6%2596%25B9%25E6%25B3%2595%25E8%25AF%25B4%25E6%2598%258E" target="_blank">#</a>IFileStorage 方法说明</h1> 
  <table cellspacing="0" style="border-collapse:collapse; display:inline-table; margin:1rem 0px; overflow-x:auto; width:auto"> 
   <thead> 
    <tr> 
     <th>属性</th> 
     <th>说明</th> 
    </tr> 
   </thead> 
   <tbody> 
    <tr> 
     <td style="border-style:solid; border-width:1px">upload</td> 
     <td style="border-style:solid; border-width:1px">上传</td> 
    </tr> 
    <tr> 
     <td style="border-style:solid; border-width:1px">delete</td> 
     <td style="border-style:solid; border-width:1px">删除</td> 
    </tr> 
    <tr> 
     <td style="border-style:solid; border-width:1px">download</td> 
     <td style="border-style:solid; border-width:1px">下载</td> 
    </tr> 
    <tr> 
     <td style="border-style:solid; border-width:1px">getUrl</td> 
     <td style="border-style:solid; border-width:1px">文件可预览地址</td> 
    </tr> 
   </tbody> 
  </table> 
  <h1><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Faizuda.com%2Fpages%2F40d5c3%2F%23%25E9%2585%258D%25E7%25BD%25AE%25E5%25B1%259E%25E6%2580%25A7%25E8%25AF%25B4%25E6%2598%258E" target="_blank">#</a>配置属性说明</h1> 
  <table cellspacing="0" style="border-collapse:collapse; display:inline-table; margin:1rem 0px; overflow-x:auto; width:auto"> 
   <thead> 
    <tr> 
     <th>属性</th> 
     <th>说明</th> 
    </tr> 
   </thead> 
   <tbody> 
    <tr> 
     <td style="border-style:solid; border-width:1px">platform</td> 
     <td style="border-style:solid; border-width:1px">存储平台，目前支持 minio aliyun</td> 
    </tr> 
    <tr> 
     <td style="border-style:solid; border-width:1px">endpoint</td> 
     <td style="border-style:solid; border-width:1px">域名</td> 
    </tr> 
    <tr> 
     <td style="border-style:solid; border-width:1px">accessKey</td> 
     <td style="border-style:solid; border-width:1px">访问 KEY</td> 
    </tr> 
    <tr> 
     <td style="border-style:solid; border-width:1px">secretKey</td> 
     <td style="border-style:solid; border-width:1px">密钥</td> 
    </tr> 
    <tr> 
     <td style="border-style:solid; border-width:1px">bucketName</td> 
     <td style="border-style:solid; border-width:1px">存储空间桶名</td> 
    </tr> 
    <tr> 
     <td style="border-style:solid; border-width:1px">connectionTimeout</td> 
     <td style="border-style:solid; border-width:1px">连接超时，阿里云OSS有效</td> 
    </tr> 
   </tbody> 
  </table> 
 </div> 
</div>
                                        </div>
                                      
</div>
            
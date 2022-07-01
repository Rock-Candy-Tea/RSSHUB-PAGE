
---
title: 'aizuda 低代码 OSS 文件存储模块 1.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100'
author: 开源中国
comments: false
date: Fri, 01 Jul 2022 10:01:00 GMT
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Faizuda.com%2Fpages%2F40d5c3" target="_blank">文档地址 http://aizuda.com/pages/40d5c3</a></p> 
<p style="color:#004050; text-align:start">源码地址 <span> </span><a href="https://gitee.com/aizuda/aizuda-components/tree/master/aizuda-oss" target="_blank">aizuda-oss</a> 测试 <a href="https://gitee.com/aizuda/aizuda-components-examples/tree/master/aizuda-oss-example" target="_blank">demo</a></p> 
<ul> 
</ul> 
<pre><code class="language-java">// 静态方法方式调用
OSS.fileStorage(platform).bucket(bucketName).upload(fis, filename);

// 依赖注入方式调用
fileStorage.bucket(bucketName)
    // 使用默认 yml 配置媒体类型
    .allowMediaType(fis)
    // 只允许gif图片上传,所有图片可以是 image/ 部分匹配
    //.allowMediaType(fis, t -> t.startsWith("image/gif"))
    .upload(fis, filename);
</code></pre> 
<p>升级日志：</p> 
<p>- 本地文件存储能力支持。</p> 
<p>- 媒体类型检查支持，可配置和动态支持上传限制类型。</p> 
<p>- 优化下载逻辑，其它优化。</p>
                                        </div>
                                      
</div>
            

---
title: 'FastBoot v1.5 发布，完善存储和短信，支持主流云平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/makunet/fast-boot/raw/master/fast-server/src/main/resources/public/1.png'
author: 开源中国
comments: false
date: Fri, 26 Aug 2022 15:10:00 GMT
thumbnail: 'https://gitee.com/makunet/fast-boot/raw/master/fast-server/src/main/resources/public/1.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">介绍</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>FastBoot 是采用 SpringBoot、SpringSecurity、Mybatis-Plus 等框架，开发的一套 SpringBoot 快速开发系统，使用门槛极低，且采用 MIT 开源协议，完全免费开源，可免费用于<strong>商业项目</strong>等场景。</li> 
 <li>采用组件模式，扩展不同的业务功能，可以很方便的实现各种业务需求，且不会导致系统臃肿，若想使用某个组件，按需引入即可，反之亦然。</li> 
 <li>开发文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaku.net%2Fdocs%2Ffast-boot" target="_blank">https://maku.net/docs/fast-boot</a></li> 
 <li>演示环境：<a href="https://gitee.com/link?target=https%3A%2F%2Fdemo.maku.net%2Ffast-boot">https://demo.maku.net/fast-boot</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新日志</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>新增七牛云、华为云短信平台，现已支持阿里云、腾讯云、七牛云、华为云短信平台，且支持多平台轮询发送</li> 
 <li>新增腾讯云、七牛云、华为云、Minio等云存储，现已支持阿里云、腾讯云、七牛云、华为云、Minio、本地存储</li> 
 <li>新增文件上传接口，方便前端直接调用接口上传文件</li> 
 <li>新增附件管理功能，可以上传、下载和删除附件</li> 
 <li>新增对外文件上传接口，方便其他模块调用，实现各模块间解耦</li> 
 <li>新增前端文件下载Hooks方法，解决前端下载需求</li> 
 <li>优化文件上传方式，提供最新的测试用例</li> 
 <li>升级VueUse到9.1.1</li> 
 <li>升级TypeScript到4.6.3</li> 
 <li>修复菜单样式错位问题</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">前端工程</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Github 仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmakunet%2Ffast-admin" target="_blank">https://github.com/makunet/fast-admin</a></li> 
 <li>Gitee 仓库：<a href="https://gitee.com/makunet/fast-admin">https://gitee.com/makunet/fast-admin</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">后端工程</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Github 仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmakunet%2Ffast-boot" target="_blank">https://github.com/makunet/fast-boot</a></li> 
 <li>Gitee 仓库：<a href="https://gitee.com/makunet/fast-boot">https://gitee.com/makunet/fast-boot</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">代码生成器</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Github 仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmakunet%2Ffast-generator" target="_blank">https://github.com/makunet/fast-generator</a></li> 
 <li>Gitee 仓库：<a href="https://gitee.com/makunet/fast-generator">https://gitee.com/makunet/fast-generator</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">交流和反馈</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官方社区：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaku.net" target="_blank">https://maku.net</a></li> 
 <li>技术解答、交流、反馈、建议等，请移步到官方社区，我们会及时回复，也方便今后的小伙伴寻找答案，感谢理解！</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">效果图</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://gitee.com/makunet/fast-boot/raw/master/fast-server/src/main/resources/public/1.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://gitee.com/makunet/fast-boot/raw/master/fast-server/src/main/resources/public/2.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://gitee.com/makunet/fast-boot/raw/master/fast-server/src/main/resources/public/3.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://gitee.com/makunet/fast-boot/raw/master/fast-server/src/main/resources/public/4.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://gitee.com/makunet/fast-boot/raw/master/fast-server/src/main/resources/public/5.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://gitee.com/makunet/fast-boot/raw/master/fast-server/src/main/resources/public/6.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            
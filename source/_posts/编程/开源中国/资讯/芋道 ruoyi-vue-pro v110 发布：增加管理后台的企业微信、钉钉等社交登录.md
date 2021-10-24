
---
title: '芋道 ruoyi-vue-pro v1.1.0 发布：增加管理后台的企业微信、钉钉等社交登录'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4026'
author: 开源中国
comments: false
date: Sun, 24 Oct 2021 20:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4026'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">项目地址：</span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro">https://gitee.com/zhijiantianya/ruoyi-vue-pro</a></p> 
<p>项目介绍：<strong style="color:#40485b">芋道</strong><span style="background-color:#ffffff; color:#40485b">，一套</span><strong style="color:#40485b">全部开源</strong><span style="background-color:#ffffff; color:#40485b">的</span><strong style="color:#40485b">企业级</strong><span style="background-color:#ffffff; color:#40485b">的快速开发平台，毫无保留给个人及企业免费使用。</span></p> 
<ul> 
 <li><code>yudao-admin-server</code> + <code>yudao-admin-ui</code>面向 B 端的管理后台。</li> 
 <li><code>yudao-user-server</code> + <code>yudao-user-ui</code>面向 C 端的用户前台（微信小程序 + H5 页面）。</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">更新说明：</span></p> 
<ul> 
 <li><span style="color:#e74c3c"><strong>新增管理后台的企业微信、钉钉等社交登录</strong></span></li> 
 <li><strong><span style="color:#e74c3c">新增用户前台(例如说，用户使用的小程序)的后端项目 <code>yudao-user-server</code></span></strong></li> 
 <li>新增公共服务<span> </span><code>yudao-core-service</code><span> </span>项目，通过 Jar 包的方式，提供<span> </span><code>yudao-user-server</code><span> </span>和<span> </span><code>yudao-admin-server</code><span> </span>的共享逻辑的复用</li> 
 <li>新增用户前台的手机登录、验证码登录</li> 
 <li>修复管理后台的用户头像上传 404 的问题，原因是请求路径不对</li> 
 <li>修复用户导入失败的问题，原因是 Lombok 链式与 cglib 读取属性有冲突</li> 
 <li>修复阿里云短信发送失败的问题，原因是 Opentracing 依赖的版本太低，调整成 0.31.0</li> 
</ul> 
<p>v1.2.0 计划：</p> 
<ul> 
 <li>三方支付：https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/pay_extension</li> 
</ul> 
<p>v1.3.0 计划：</p> 
<ul> 
 <li>基于 uniapp 实现跨端的用户前台</li> 
</ul> 
<p>v1.4.0 计划：</p> 
<ul> 
 <li>工作流：https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/feature%2Factiviti</li> 
</ul>
                                        </div>
                                      
</div>
            
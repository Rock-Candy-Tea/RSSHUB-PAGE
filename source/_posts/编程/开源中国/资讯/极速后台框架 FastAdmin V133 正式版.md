
---
title: '极速后台框架 FastAdmin V1.3.3 正式版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0b1aee1b0efb35f650c8d22e13ade6e99fa.png'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 10:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0b1aee1b0efb35f650c8d22e13ade6e99fa.png'
---

<div>   
<div class="content">
                                                                                            <p><img height="567" src="https://oscimg.oschina.net/oscnet/up-0b1aee1b0efb35f650c8d22e13ade6e99fa.png" width="902" referrerpolicy="no-referrer"></p> 
<p><em><span style="color:#bdc3c7">img: NastasyaDay</span></em></p> 
<p>FastAdmin 开源于 2017 年，历经五年迭代更新，发布正式版 V1.3.3，感谢支持国内的开源社区。</p> 
<p>更新记录：</p> 
<ul> 
 <li>新增插件配置分组功能</li> 
 <li>新增动态可见组件</li> 
 <li>新增常规配置动态可见</li> 
 <li>新增是否默认展示子菜单功能</li> 
 <li>优化邮件发送判断</li> 
 <li>优化计算月天数</li> 
 <li>修复表格dropdown被遮挡的BUG</li> 
 <li>修复新版本密码长度导致无法添加管理员的BUG</li> 
 <li>优化错误提示</li> 
 <li>优化移动端弹窗大小判断</li> 
 <li>优化上传文件名过滤</li> 
 <li>全局前台Layer样式</li> 
 <li>优化用户名密码长度检测</li> 
 <li>优化插件管理</li> 
 <li>修复附件选择列表无法上传文件的BUG</li> 
 <li>移除插件授权按钮</li> 
 <li>移除cdnurl后台系统配置中配置</li> 
 <li>新增一对多CRUD功能</li> 
 <li>新增一键生成tagsinput组件</li> 
 <li>新增自动生成标签&时间区间组件</li> 
 <li>新增Autocomplete和Tagsinput前端组件</li> 
 <li>新增配置全局启用上传时使用完整URL功能</li> 
 <li>新增附件列表上传归类</li> 
 <li>新增后台管理布局个性化配置</li> 
 <li>新增插件安装成功导入测试数据提示</li> 
 <li>新增后缀生成icon缓存</li> 
 <li>新增全局列表图片缩略图样式</li> 
 <li>新增自动生成固定列</li> 
 <li>新增弱密码检测</li> 
 <li>新增验证码长度配置</li> 
 <li>优化插件相关命令行命令</li> 
 <li>优化默认管理员和前台用户头像</li> 
 <li>优化插件安装后自动刷新JS缓存</li> 
 <li>优化后台管理左侧菜单展现方式</li> 
 <li>优化全局样式</li> 
 <li>优化后台管理菜单</li> 
 <li>优化Fieldlist组件</li> 
 <li>优化上传组件归类功能</li> 
 <li>优化Bootstrap-table固定列高度</li> 
 <li>优化Layer弹窗焦点框</li> 
 <li>优化Citypicker城市地区数据</li> 
 <li>优化附件选择</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">FastAdmin 介绍</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">FastAdmin 是一款 PHP 后台开发框架，使用 Apache 2.0 开源协议，开源协议友好，可免费用于商业，基于 Auth 验证的权限管理系统，一键生成 CRUD，自动生成控制器、模型、视图、JS、语言包、菜单、回收站。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云仓库 <a href="https://gitee.com/karson/fastadmin">https://gitee.com/karson/fastadmin</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">开源中国 <a href="https://www.oschina.net/p/fastadmin">https://www.oschina.net/p/fastadmin</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官网 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.fastadmin.net%2F" target="_blank">https://www.fastadmin.net/</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="控制台" src="https://oscimg.oschina.net/oscnet/up-847845e6886399e6f5cf0e76e735a490f57.gif" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于<code>Auth</code>验证的权限管理系统 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>支持无限级父子级权限继承，父级的管理员可任意增删改子级管理员及权限设置</li> 
   <li>支持单管理员多角色</li> 
   <li>支持管理子级数据或个人数据</li> 
  </ul> </li> 
 <li>强大的一键生成功能 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>一键生成CRUD,包括控制器、模型、视图、JS、语言包、菜单、回收站等</li> 
   <li>一键压缩打包JS和CSS文件，一键CDN静态资源部署</li> 
   <li>一键生成控制器菜单和规则</li> 
   <li>一键生成API接口文档</li> 
  </ul> </li> 
 <li>完善的前端功能组件开发 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>基于<code>AdminLTE</code>二次开发</li> 
   <li>基于<code>Bootstrap</code>开发，自适应手机、平板、PC</li> 
   <li>基于<code>RequireJS</code>进行JS模块管理，按需加载</li> 
   <li>基于<code>Less</code>进行样式开发</li> 
  </ul> </li> 
 <li>强大的插件扩展功能，在线安装卸载升级插件</li> 
 <li>通用的会员模块和API模块</li> 
 <li>共用同一账号体系的Web端会员中心权限验证和API接口会员权限验证</li> 
 <li>二级域名部署支持，同时域名支持绑定到应用插件</li> 
 <li>多语言支持，服务端及客户端支持</li> 
 <li>支持大文件分片上传、剪切板粘贴上传、拖拽上传，进度条显示，图片上传前压缩</li> 
 <li>支持表格固定列、固定表头、跨页选择、Excel导出、模板渲染等功能</li> 
</ul> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            
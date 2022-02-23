
---
title: 'JeeSite Vue 5.0.1 发布，无用户限制，快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ee8581b5edc0ba450a1513b272631bb50da.png'
author: 开源中国
comments: false
date: Wed, 23 Feb 2022 09:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ee8581b5edc0ba450a1513b272631bb50da.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:start">升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">新增 路由模式参数 VITE_ROUTE_WEB_HISTORY（true: history、false: hash）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 主题及黑暗主题优化细节改进，提高用户体验</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 Tabs 为 1 个页签的时候，自动隐藏页签栏</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 Select 下拉 options 选项类型兼容改进，ide 类型提示</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 TreeSelect 下拉 treeData 选项类型兼容改进，ide 类型提示</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 Tree 与 TreeSelect 的 treeData 类型，保持一致，方便后台返回直接使用</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 更改默认设置，发布到 / 路径，默认 history 模式</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 登录页高度过小时，可以垂直滚动登录表单</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 layout 组件，自适应页面边距，适应折叠边距</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正 Select 使用 API 方式的时候未加载数据问题 #I4T86A</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正 遇到特殊字符时，表单远程验证提示错误 #I4U6AR</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正 代码生成的时候 选择报错问题 #I4QGOS</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正 Build 编译后切换主题色失效问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正 InputNumber 不能设置 0 问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更多细节优化改进</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">请与 <code>jeesite-vue</code> 代码仓库源码进行同步，合并代码。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">暂且不跟随后端版本号，仍使用 JeeSite v5.0.0 版本（无用户限制）</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">后端升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">新增 转为 JeeSite Vue 提供服务的 web-api 工程</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 独立 orderBy 过滤规则，只允许的特定字符</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化 后端 UI 跟随 JeeSite Vue 风格，IFRAME 时更贴合</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正 Redis 反序列化遇到错误时，忽略并更新缓存数据</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正 PinyinUtils 有特殊字符的时候报空问题</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">后端升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修改 <code>pom.xml</code> 文件中的 <code>jeesite-parent</code> 版本号为 <code>5.0.0-SNAPSHOT</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-common</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-module-core</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">执行 <code>root/package.bat(sh)</code> 打包脚本，强制更新依赖即可。</p> </li> 
</ul> 
<p><img height="717" src="https://oscimg.oschina.net/oscnet/up-ee8581b5edc0ba450a1513b272631bb50da.png" width="1676" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>进一步了解</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>JeeSite 官网地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeesite.com" target="_blank">http://jeesite.com</a></li> 
 <li>JeeSite 在线文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.jeesite.com" target="_blank">http://docs.jeesite.com</a></li> 
 <li>JeeSite 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.jeesite.com" target="_blank">http://demo.jeesite.com</a></li> 
 <li>JeeSite Vue 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.jeesite.com" target="_blank">http://vue.jeesite.com</a>  (Vue3分离版本)</li> 
 <li>JeeSite Vue 前端源码：<a href="https://gitee.com/thinkgem/jeesite-vue" target="_blank">https://gitee.com/thinkgem/jeesite-vue</a></li> 
 <li>JeeSite Vue 后端源码：<a href="https://gitee.com/thinkgem/jeesite4/tree/v5.0_dev/" target="_blank">https://gitee.com/thinkgem/jeesite4/tree/v5.0_dev/</a></li> 
 <li>JeeSite 手机端/移动端：<a href="https://gitee.com/thinkgem/jeesite4-uniapp" target="_blank">https://gitee.com/thinkgem/jeesite4-uniapp</a></li> 
</ul>
                                        </div>
                                      
</div>
            
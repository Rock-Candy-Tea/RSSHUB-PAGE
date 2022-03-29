
---
title: '洛甲WAF，Web 应用防火墙 1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/main.png'
author: 开源中国
comments: false
date: Tue, 29 Mar 2022 03:46:00 GMT
thumbnail: 'https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/main.png'
---

<div>   
<div class="content">
                                                                                            <div>
 1.0版本新增功能
</div> 
<div> 
 <ul> 
  <li>针对封禁的IP,  可以配置记录请求信息, 可以有效的分析攻击时的记录</li> 
  <li>对指定HOST限制流入流出流量或者对全局限制</li> 
  <li>可在后台配置负载均衡, 添加域名转发, 无需重启服务器</li> 
  <li>对指定时间, 或者指定星期进行限制, 防止高峰期流量过载</li> 
  <li>对GET或者POST参数进行检查, 防止SQL注入</li> 
 </ul> 
</div> 
<div> 
 <h3 style="margin-left:0; margin-right:0; text-align:left">洛甲WAF, 它能做什么</h3> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">洛甲WAF是基于openresty的web防火墙，它由多个或者单个节点服务器和中控服务器组成, 它将节点的数据请求汇总到中控服务器做统一的分析, 从而可以自动的识别出哪些用户是非法IP, 从而实行自动封禁, 基本上能保证90%以上的CC攻击自动拦截, 保证服务器的有效正常的运转.</p> 
 <h4 style="margin-left:0; margin-right:0; text-align:left">除了防CC, 他还能做什么</h4> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>可在后台配置限制访问频率,URI访问频率</li> 
  <li>可后台封禁IP,记录IP访问列表</li> 
  <li>对指定HOST限制流入流出流量或者对全局限制</li> 
  <li>可统计服务端错误内容500错误等</li> 
  <li>可查看请求耗时列表, 服务器内部负载情况</li> 
  <li>可在后台配置负载均衡, 添加域名转发, 无需重启服务器</li> 
  <li>可在后台配置SSL证书, 无需重启服务器</li> 
  <li>对黑名单的用户,如果频繁访问,则防火墙对IP封禁</li> 
  <li>对GET或者POST参数进行检查, 防止SQL注入</li> 
  <li>对指定时间, 或者指定星期进行限制, 防止高峰期流量过载</li> 
  <li> <p>针对封禁的IP,  可以配置记录请求信息, 可以有效的分析攻击时的记录</p> <h4 style="margin-left:0; margin-right:0; text-align:left">应用截图</h4> <p>主页</p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/main.png" referrerpolicy="no-referrer"></p> <p>配置</p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/config.png" referrerpolicy="no-referrer"></p> <p>负载均衡</p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/upstream.png" referrerpolicy="no-referrer"></p> <p>SSL证书</p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/ssl.png" referrerpolicy="no-referrer"></p> <h4 style="margin-left:0; margin-right:0; text-align:left">相关链接</h4> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/tickbh/luojiawaf_lua">节点服务器 luojiawaf_lua(nginx+lua)</a></p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/tickbh/luojiawaf_web">中控服务器前端 luajiawaf_web(ant.design)</a></p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/tickbh/luojiawaf_server">中控服务器后端 luajiawaf_server(django)</a></p> </li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            
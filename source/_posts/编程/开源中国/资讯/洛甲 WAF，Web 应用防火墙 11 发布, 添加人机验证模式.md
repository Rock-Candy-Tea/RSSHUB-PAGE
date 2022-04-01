
---
title: '洛甲 WAF，Web 应用防火墙 1.1 发布, 添加人机验证模式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/main.png'
author: 开源中国
comments: false
date: Fri, 01 Apr 2022 09:45:00 GMT
thumbnail: 'https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/main.png'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:left">
 1.1版本新增功能
</div> 
<div style="text-align:left"> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>添加人机验证模式, 被封禁时可选择人机模式, 以减少误封的可能</li> 
  <li>增加对服务器信息的简易收集(流量, cpu及内存占用率)</li> 
  <li>对触发防御参数的请求自动记录, 有效的帮助开发人员针对性的防御</li> 
 </ul> 
 <p>1.1版本更新功能</p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>调整同步频率, 保证信息能及时得到回馈</li> 
  <li>调整分析数据, 保证更精准的拦截非法的IP</li> 
  <li>优化数据获取, 减少对节点服务器的压力</li> 
 </ul> 
</div> 
<div style="text-align:left"> 
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
  <li> 
   <div> 
    <div>
     <span style="color:#000000">针对解发风控的IP, 可以选择人机验证模式, 保证不会被误</span>
    </div> 
   </div> </li> 
  <li> <p style="margin-left:0; margin-right:0">针对封禁的IP,  可以配置记录请求信息, 可以有效的分析攻击时的记录</p> <h4 style="margin-left:0; margin-right:0; text-align:left">应用截图</h4> <p style="margin-left:0; margin-right:0">主页</p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/main.png" referrerpolicy="no-referrer"></p> <p style="margin-left:0; margin-right:0">配置</p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/config.png" referrerpolicy="no-referrer"></p> <p style="margin-left:0; margin-right:0">负载均衡</p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/upstream.png" referrerpolicy="no-referrer"></p> <p style="margin-left:0; margin-right:0">SSL证书</p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/ssl.png" referrerpolicy="no-referrer"></p> <p>行为验证码</p> <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/tickbh/luojiawaf_lua/raw/master/screenshot/captcha.png" referrerpolicy="no-referrer"></p> </li> 
  <li> <h4 style="margin-left:0; margin-right:0; text-align:left">相关链接</h4> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/tickbh/luojiawaf_lua">节点服务器 luojiawaf_lua(nginx+lua)</a></p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/tickbh/luojiawaf_web">中控服务器前端 luajiawaf_web(ant.design)</a></p> <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/tickbh/luojiawaf_server">中控服务器后端 luajiawaf_server(django)</a></p> </li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            
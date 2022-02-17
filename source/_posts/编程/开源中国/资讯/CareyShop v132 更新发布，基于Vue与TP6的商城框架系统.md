
---
title: 'CareyShop v1.3.2 更新发布，基于Vue与TP6的商城框架系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://aliyun.oss.careyshop.cn/poster/banner.png'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 06:46:00 GMT
thumbnail: 'https://aliyun.oss.careyshop.cn/poster/banner.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt="careyshop_banner" src="https://aliyun.oss.careyshop.cn/poster/banner.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">CareyShop（简称 CS）是一套基于 ThinkPHP6.0 框架开发的高性能开源商城框架系统，秉承极简、极速、极致的开发理念，采用前后端分离，支持分布式部署。框架内部使用面向对象模块化调用，在多个终端、跨平台时采用 REST API 进行数据交互，可直接对接 PC、移动设备、小程序、云部署，构建 Android、IOS 的 APP。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">预览</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.careyshop.cn%2Fadmin" target="_blank">后台 Demo 预览</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.careyshop.cn%2Fapi" target="_blank">RestAPI 接口调试</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.careyshop.cn%2Fguide%2Fwhite%2F" target="_blank">经典配套款</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.careyshop.cn%2Fguide%2Fgray%2F" target="_blank">深灰商务款</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">文档</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.careyshop.cn%2F" target="_blank">文档中心</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">仓库</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdnyz520%2Fcareyshop" target="_blank">Github 仓库</a> | <a href="https://gitee.com/careyshop/careyshop">码云仓库</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fe.coding.net%2Fcareyshop%2Fcareyshop.git" target="_blank">Coding 仓库</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">生态</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">CareyShop 后台管理模板 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdnyz520%2Fcareyshop-admin" target="_blank">Github 仓库</a> | <a href="https://gitee.com/careyshop/careyshop-admin">码云仓库</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">CareyShop Rest接口调试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdnyz520%2Fcareyshop-rest" target="_blank">Github 仓库</a> | <a href="https://gitee.com/careyshop/careyshop-rest">码云仓库</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">V1.3.2 更新内容</h2> 
<h4 style="margin-left:0em; margin-right:0em; text-align:start">新增</h4> 
<ul> 
 <li>[新增] 增加API接口"重新绑定手机或邮箱"</li> 
 <li>[新增] 订单中的开票内容结合票据管理使用</li> 
 <li>[新增] 增加"redis"配置</li> 
 <li>[新增] 增加微信公众号API"发送消息模板"</li> 
 <li>[新增] 新增”重置票据“接口</li> 
 <li>[新增] 发票开具完毕允许将附件通过电子邮件发送</li> 
 <li>[新增] 增加API接口"根据事件获取替换变量"</li> 
 <li>[新增] OAuth2.0支持微信、QQ、抖音、淘宝等</li> 
 <li>[新增] 渠道系统，支持微信公众号等</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">修正</h4> 
<ul> 
 <li>[修正] 修复生成订单时商品重量没有与商品数量进行累计</li> 
 <li>[修正] 修复退款额计算出现"Nan"</li> 
 <li>[修正] 修复模型关联查询后报错模型成员不存在</li> 
 <li>[修正] 修复服务层下验证器并非实际生效</li> 
 <li>[修正] 修复"字段自动转换"与"获取器"冲突</li> 
 <li>[修正] 修复接口调用部分函数未传递请求参数</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">优化</h4> 
<ul> 
 <li>[优化] 快递鸟快递查询模块修改,主要配合"顺丰速递"查询方式变更</li> 
 <li>[优化] 优化函数注释中的<a href="https://gitee.com/throws">@throws</a></li> 
 <li>[优化] 改用箭头函数(短匿名函数)</li> 
 <li>[优化] 优化"withJoin"查询方式</li> 
 <li>[优化] 关联查询时对排序字段的优化</li> 
 <li>[优化] 修改默认参数配置</li> 
 <li>[优化] 对模型中的"find"成员函数进行更改使用</li> 
 <li>[优化] 短信与邮件"验证码"机制将从通知版块中分离,并且通知模块也将重构</li> 
 <li>[优化] 将短信与邮件发送从"通知系统"中剥离成为独立模块</li> 
 <li>[优化] 将"通知系统"模块暂时剥离,将会进行重构.</li> 
 <li>[优化] 将模型中的数据验证成员函数独立为"trait",之后可在任意类中通过"use"使用.</li> 
 <li>[优化] 本地上传(CareyShop)增加自定义参数"x:is_actual",值为真时将返回物理路径.</li> 
 <li>[优化] "智能字符串模糊化"支持显示位数</li> 
 <li>[优化] 命名空间引用采用按组方式</li> 
 <li>[优化] 翻页页码规则修改</li> 
 <li>[优化] 允许管理组获取顾客的购物车列表与数量统计</li> 
 <li>[优化] 增加敏感词过滤字段</li> 
 <li>[优化] 系统邮件对附件的添加支持多种数据结构</li> 
 <li>[优化] 顾客的开票信息允许管理组介入管理</li> 
 <li>[优化] 更换响应头设值函数</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能</h2> 
<ul> 
 <li>发票申请、审批管理（1.3.2）</li> 
 <li>OAuth2.0支持微信、QQ、抖音、淘宝等（1.3.2）</li> 
 <li>通知订阅（1.3.2）</li> 
 <li>渠道系统，支持微信公众号等（1.3.2）</li> 
 <li>数据统计</li> 
 <li>重构至ThinkPHP6.0</li> 
 <li>REST API内置调试工具</li> 
 <li>商品管理</li> 
 <li>商品分类</li> 
 <li>商品品牌</li> 
 <li>商品模型</li> 
 <li>商品规格</li> 
 <li>商品属性</li> 
 <li>商品评价</li> 
 <li>内置商品预览</li> 
 <li>商品咨询</li> 
 <li>购物车</li> 
 <li>我的足迹</li> 
 <li>我的收藏夹</li> 
 <li>订单管理</li> 
 <li>订单详情</li> 
 <li>订单导出</li> 
 <li>订单打印</li> 
 <li>订单退款</li> 
 <li>退款日志</li> 
 <li>售后管理</li> 
 <li>售后详情</li> 
 <li>满额包邮</li> 
 <li>商品折扣</li> 
 <li>订单促销</li> 
 <li>优惠劵管理</li> 
 <li>优惠劵发放</li> 
 <li>购物卡(充值卡)管理</li> 
 <li>购物卡(充值卡)使用管理</li> 
 <li>会员账户</li> 
 <li>会员账户资金(可充值)</li> 
 <li>会员提现账户</li> 
 <li>会员收货地址</li> 
 <li>会员等级折扣</li> 
 <li>交易结算日志</li> 
 <li>积分发放兑换机制</li> 
 <li>提现管理</li> 
 <li>问答列表</li> 
 <li>内置后台消息通知体制</li> 
 <li>广告位置</li> 
 <li>广告列表</li> 
 <li>文章管理</li> 
 <li>文章分类</li> 
 <li>专题管理</li> 
 <li>资源OSS管理</li> 
 <li>资源OSS样式管理</li> 
 <li>客服模块</li> 
 <li>配送轨迹模块</li> 
 <li>友情链接</li> 
 <li>二维码模块</li> 
 <li>条形码模块</li> 
 <li>管理组人员管理</li> 
 <li>操作日志</li> 
 <li>用户组</li> 
 <li>菜单管理</li> 
 <li>权限规则</li> 
 <li>系统配置管理</li> 
 <li>前台导航</li> 
 <li>支付模块</li> 
 <li>支付日志</li> 
 <li>支付原路退回</li> 
 <li>区域管理</li> 
 <li>快递公司管理</li> 
 <li>配送方式配置</li> 
 <li>APP 应用管理</li> 
 <li>APP 安装包</li> 
 <li>短信消息</li> 
 <li>邮件消息</li> 
 <li>接口批量调用</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">必须将项目下的<code>public</code>目录设为<code>web访问</code>目录，第一次访问首页时会进入<code>安装向导</code>，务必请通过向导完成安装。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">快速启动</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">切换到项目根目录，在命令行输入<code>php think run -H 127.0.0.1 -p 8080</code>，启动 PHP 自带的<code>webserver</code>服务，按键<code>Ctrl + C</code>退出服务。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">建议使用<code>IP</code>启动，避免使用<code>localhost</code>，并且此方法只适合调试环境。</p> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:left">常见问题</h2> 
<ul> 
 <li>如何隐藏<code>index.php</code>入口文件?<br> 建议采用<code>PATH_INFO</code>访问地址，隐藏入口文件可做伪静态，请参见：<br> <a href="https://gitee.com/link?target=https%3A%2F%2Fdoc.careyshop.cn%2Fguide%2Frewrite%2F">https://doc.careyshop.cn/guide/rewrite/</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">接口调试</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://aliyun.oss.careyshop.cn/poster/rest_api.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">管理后台</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E9%A6%96%E9%A1%B5-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E5%95%86%E5%93%81%E5%88%97%E8%A1%A8-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E5%95%86%E5%93%81%E8%A7%84%E6%A0%BC-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E5%AA%92%E4%BD%93%E8%AE%BE%E7%BD%AE-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E5%95%86%E5%93%81%E9%A2%84%E8%A7%88-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E5%95%86%E5%93%81%E5%88%86%E7%B1%BB-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E5%95%86%E5%93%81%E8%AF%84%E4%BB%B7-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E8%AF%84%E4%BB%B7%E6%98%8E%E7%BB%86-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E8%AE%A2%E5%8D%95%E5%88%97%E8%A1%A8-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E8%AE%A2%E5%8D%95%E8%AF%A6%E6%83%85-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E8%AE%A2%E5%8D%95%E6%89%93%E5%8D%B0-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E5%94%AE%E5%90%8E%E5%88%97%E8%A1%A8-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E5%94%AE%E5%90%8E%E8%AF%A6%E6%83%85-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E8%B5%84%E6%BA%90%E7%AE%A1%E7%90%86-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E8%B5%84%E6%BA%90%E9%80%89%E6%8B%A9-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E7%89%A9%E6%B5%81%E8%BD%A8%E8%BF%B9-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E8%B5%84%E6%BA%90%E9%A2%84%E8%A7%88-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E8%A7%86%E9%A2%91%E6%92%AD%E6%94%BE-%E7%81%B0.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://aliyun.oss.careyshop.cn/poster/gray/%E7%BC%A9%E7%95%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1-%E7%81%B0.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            
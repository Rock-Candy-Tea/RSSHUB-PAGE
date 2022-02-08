
---
title: 'CareyShop v1.3.2 已经发布，商城框架系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5031'
author: 开源中国
comments: false
date: Tue, 08 Feb 2022 17:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5031'
---

<div>   
<div class="content">
                                                                                            <p>CareyShop v1.3.2 已经发布，商城框架系统</p> 
<p>此版本更新内容包括：</p> 
<h4>新增</h4> 
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
<h4>修正</h4> 
<ul> 
 <li>[修正] 修复生成订单时商品重量没有与商品数量进行累计</li> 
 <li>[修正] 修复退款额计算出现"Nan"</li> 
 <li>[修正] 修复模型关联查询后报错模型成员不存在</li> 
 <li>[修正] 修复服务层下验证器并非实际生效</li> 
 <li>[修正] 修复"字段自动转换"与"获取器"冲突</li> 
 <li>[修正] 修复接口调用部分函数未传递请求参数</li> 
</ul> 
<h4>优化</h4> 
<ul> 
 <li>[优化] 快递鸟快递查询模块修改,主要配合"顺丰速递"查询方式变更</li> 
 <li>[优化] 优化函数注释中的<a href="https://www.oschina.net/throws">@throws </a></li> 
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
<p>详情查看：<a href="https://gitee.com/careyshop/careyshop/releases/v1.3.2">https://gitee.com/careyshop/careyshop/releases/v1.3.2</a></p>
                                        </div>
                                      
</div>
            
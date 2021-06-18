
---
title: '基于 TP6 的 bwsaas 多租户多应用多终端 SAAS 平台框架重大 V1.4.0 更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8235'
author: 开源中国
comments: false
date: Thu, 17 Jun 2021 22:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8235'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">废话：又经过一个月的沉淀和开发，框架的稳定性和完善性又上升到了一个新层次，本次版本跳过了v1.3.3定义到了V1.4.0，大家也会知道了改动还是比较大的，最重要的就是 <strong>官方网站插件市场上线了</strong>【www.buwangyun.com】<br> 下面详细说明变动：</p> 
<p style="text-align:start">新增<br> 1 通用注册增加用户注册时的默认头像【多端统一】<br> 2 增加插件类型all_system，这种插件能同时在租户后台和总平台后台有管理菜单<br> 3 插件类型:admin_system=总后台插件,member_system=租户系统,member_bwwechat=租户bwwechat应用插件 ，租户后台和总后台都有操作节点的插件类型 all_system<br> 4 租户应用增加续费功能，支持总平台为每个应用单独配置续费升级套餐【余额支付续费升级】<br> 5 租户后台样式调整为左侧导航双列布局导航，细分租户后台管理菜单并调整展示样式<br> 6 框架安装sql更改（增加套餐菜单，附件删除菜单，微信消息菜单...）<br> 7 增加Bwmall商城签到插件<br> 8 增加bwmall应用的打印机插件【支持易联云，中午，飞鹅】<br> 9 增加头条小程序和支付配置设置<br> 10 bwmall商城头条系小程序支付回调<br> 11 框架增加租户应用PC端扫码支付<br> 更新<br> 1 更新了演示地址<br> 2 总平台对租户用户管理整合到了一个管理界面【方便管理】<br> 3 租户所有用户详情配色修改</p> 
<p style="text-align:start">修复<br> 1 bwmall商城的打印插件修改为应用级插件<br> 2 框架公共API接口绑定上下级关系修复【不能绑定自己的下级用户】<br> 3 修复应用用户列表详情内user_bill展示问题</p>
                                        </div>
                                      
</div>
            
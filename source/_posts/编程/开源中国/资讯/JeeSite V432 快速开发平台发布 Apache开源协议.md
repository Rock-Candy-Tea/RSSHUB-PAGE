
---
title: 'JeeSite V4.3.2 快速开发平台发布 Apache开源协议'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5004'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 15:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5004'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-right:0; text-align:start">升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">菜单主题风格，激活菜单圆润风格。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">主题整体美化，标准14字号，色调细节。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Tab 页签增加关闭全部功能；Tab 增加图标。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">dataGrid 列表设置，选择列全选按钮放左下角。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">表单组件：增加 readonly 全局只读属性，支持整个表单只读。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">文件预览：如果有预览文件就预览，不管是否安装office转换服务</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">代码生成模板：非字符串类型默认增加 isUpdateForce</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">访问日志：提交前后差异数据输出结果优化</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">安全升级：防登录信息过长攻击</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">SqlMap 增加 maxJoinTableNum 选项，可设置最大联表个数（-1 为不限制，n 为 JoinTable n张表，0 为 不进行 JoinTable 查询）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">layer 优化 msg 弹窗，超时时间比较长的加关闭创建按钮，全屏消息的增宽显示更多内容。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Select2 组件优化，当超过设置最大选择长度时，自动关闭下拉框</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果开启租户模式，登录未设置 corpCode 的不在在线列表中显示</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">代码生成优化，字段类型有精度的时候也可以返回数值</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">BPM 待办接口增加 identityLinks 的返回。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">BPM 增加取消签收 unclaim 接口</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">微信接口工具升级 wxjava 4.2.2.B</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">在线文档UI升级 knife4j 2.0.9</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">大屏升级，修复已知问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">升级其它依赖库</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正左树右表的情况下，没有刷新树表的表格问题</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正ie9的上传问题，因为ie9的flash不能获取md5，所以不支持秒传</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修正租户模式下，相同的表单Key，不同的流程Key，时缓存串的问题 v4.2.3+</p> </li> 
</ul> 
<h3 style="margin-right:0; text-align:start">升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修改 <code>pom.xml</code> 文件中的 <code>jeesite-parent</code> 版本号为 <code>4.3.2-SNAPSHOT</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-common</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-module-core</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">执行 <code>root/package.bat(sh)</code> 打包脚本，强制更新依赖即可。</p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:justify">新品鉴赏</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">TS + Vue3 + Antdv : http://vue.jeesite.com</p> </li> 
</ul>
                                        </div>
                                      
</div>
            
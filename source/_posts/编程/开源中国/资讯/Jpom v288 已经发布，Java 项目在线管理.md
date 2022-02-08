
---
title: 'Jpom v2.8.8 已经发布，Java 项目在线管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4022'
author: 开源中国
comments: false
date: Tue, 08 Feb 2022 15:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4022'
---

<div>   
<div class="content">
                                                                                            <p>Jpom v2.8.8 已经发布，Java 项目在线管理</p> 
<p>此版本更新内容包括：</p> 
<h3>新增功能</h3> 
<ol> 
 <li>【server】新增容器构建(感谢@ℳ๓₯㎕斌)</li> 
 <li>【server】新增容器管理基础版</li> 
 <li>【server】节点脚本列表新增快速查看日志入口（感谢@ʟᴊx）</li> 
 <li>【server】构建新增备注字段,可以用于记录版本日志或者本次构建备注（感谢@Alex）</li> 
 <li>【server】新增解绑节点、节点分发功能 用于服务器过期或者已经确定不在使用直接删除节点相关数据（感谢<a href="https://www.oschina.net/zhanghaov">@︶ </a></li> 
 <li>【server】构建命令新增预设命令提示输入,减少用户输入（感谢<a href="https://www.oschina.net/hjk2008">@hjk2008 </a> <a href="https://gitee.com/dromara/Jpom/issues/I4SHC9" target="_blank">Gitee issues I4SHC9</a> ）</li> 
 <li>【server】批量构建支持指定部分参数使构建更灵活（感谢<a href="https://www.oschina.net/hjk2008">@hjk2008 </a> <a href="https://gitee.com/dromara/Jpom/issues/I4SHB4" target="_blank">Gitee issues I4SHB4</a> ）</li> 
 <li>【server】用户账号新增两步验证(MFA) 提升账号安全性(感谢@ℳ๓₯㎕斌)</li> 
</ol> 
<h3>解决BUG、优化功能</h3> 
<ol> 
 <li>【server】优化定时任务检查逻辑,避免不能正常关闭定时任务</li> 
 <li>【server】数据库备份新增修改人字段（可以表示备份人和还原操作人）</li> 
 <li>【server】邮箱配置权限修改为超级管理员</li> 
 <li>【server】修复服务端脚本分发到节点特殊字符编码问题（感谢@ʟᴊx）</li> 
 <li>【server】修复删除节点未删除节点统计数据（感谢@以为）</li> 
 <li>升级 SpringBoot 到 2.6.3 (感谢@ℳ๓₯㎕斌)</li> 
 <li>【server】解除 SSH 终端禁止命令权限保存失败（感谢@Alex）</li> 
 <li>【server】本地构建模式模糊匹配支持匹配多个结果</li> 
 <li>【server】修复节点分发不能删除节点问题（感谢<a href="https://www.oschina.net/bysdy">@a19920714liou </a> <a href="https://gitee.com/dromara/Jpom/issues/I4SHSP" target="_blank">Gitee issues I4SHSP</a> ）</li> 
 <li>【server】ssh 快捷安装插件端保存安装包避免多次上传 （感谢<a href="https://www.oschina.net/bysdy">@a19920714liou </a> <a href="https://gitee.com/dromara/Jpom/issues/I4SHJC" target="_blank">Gitee issues I4SHJC</a> ）</li> 
 <li>【server】ssh 快捷安装插件端权限改为管理员</li> 
 <li>【server】构建 ssh 发布授权目录采用下拉模式,提升用户操作感知 (感谢<a href="https://www.oschina.net/hjk2008">@hjk2008 </a> <a href="https://gitee.com/dromara/Jpom/issues/I4SICE" target="_blank">Gitee issues I4SICE</a> )</li> 
 <li>【server】修复数据库自动备份失败问题</li> 
</ol> 
<blockquote> 
 <p>特别感谢：<a href="https://gitee.com/weihongbin" target="_blank">ℳ๓₯㎕斌</a> 贡献容器构建相关架构</p> 
</blockquote> 
<p>详情查看：<a href="https://gitee.com/dromara/Jpom/releases/v2.8.8">https://gitee.com/dromara/Jpom/releases/v2.8.8</a></p>
                                        </div>
                                      
</div>
            